import json
import os

from src.tools.calculator import calculate_daily_budget
from src.tools.weather import get_weather

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.environ["GROQ_API_KEY"])

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calculate_daily_budget",
            "description": "Calculate the daily budget from a total budget and trip duration.",
            "parameters": {
                "type": "object",
                "properties": {
                    "total_budget": {
                        "type": "integer",
                        "description": "Total trip budget in INR.",
                    },
                    "days": {
                        "type": "integer",
                        "description": "Number of trip days.",
                    },
                },
                "required": ["total_budget", "days"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather information for a city when weather is needed.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "City whose weather is requested.",
                    },
                },
                "required": ["city"],
                "additionalProperties": False,
            },
        },
    },
]

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": (
                "I have ₹15,000 for four days in Goa. "
                "Calculate my daily budget and check the weather."
            ),
        }
    ],
    tools=TOOLS,
    tool_choice="auto",
)

message = response.choices[0].message

available_functions = {
    "calculate_daily_budget": calculate_daily_budget,
    "get_weather": get_weather,
}

if not message.tool_calls:
    print(message.content)

else:
    # Keep the model's tool-call request in conversation history.
    messages = [
        {
            "role": "user",
            "content": (
                "I have ₹15,000 for four days in Goa. "
                "Calculate my daily budget and check the weather."
            ),
        }
    ]
    messages.append(message)

    # Your Python program—not the model—executes each requested tool.
    for tool_call in message.tool_calls:
        function_name = tool_call.function.name
        function_arguments = json.loads(tool_call.function.arguments)

        function_to_call = available_functions[function_name]
        tool_result = function_to_call(**function_arguments)

        print(f"Executed: {function_name}")
        print(f"Result: {tool_result}\n")

        # Send the tool's result back as a new conversation message.
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": function_name,
                "content": json.dumps(tool_result),
            }
        )

    messages = [
    {
        "role": "user",
        "content": (
            "I have ₹15,000 for four days in Goa. "
            "Calculate my daily budget and check the weather."
        ),
    }
]

available_functions = {
    "calculate_daily_budget": calculate_daily_budget,
    "get_weather": get_weather,
}

max_iterations = 3

for iteration in range(max_iterations):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        tools=TOOLS,
        tool_choice="auto",
    )

    message = response.choices[0].message

    # No tool request means this is the final answer.
    if not message.tool_calls:
        print("\nFinal answer:")
        print(message.content)
        break

    # Preserve the model's tool-call request as conversation state.
    messages.append(message)

    for tool_call in message.tool_calls:
        function_name = tool_call.function.name
        function_arguments = json.loads(tool_call.function.arguments)

        function_to_call = available_functions[function_name]
        tool_result = function_to_call(**function_arguments)

        print(f"\nIteration {iteration + 1}: {function_name}")
        print(f"Tool result: {tool_result}")

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": function_name,
                "content": json.dumps(tool_result),
            }
        )

else:
    print("Stopped: maximum tool-call iterations reached.")

    print("Final answer:")
    