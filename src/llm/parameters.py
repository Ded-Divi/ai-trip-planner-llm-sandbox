import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.environ["GROQ_API_KEY"])


def ask(temperature: float) -> None:
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": (
                    "Write one vivid, surprising sentence about arriving in Goa for a beach holiday."
                ),
            }
        ],
        temperature=temperature,
        max_completion_tokens=180,
        reasoning_effort="low"
    )

    print(f"\nTemperature: {temperature}")
    print("Finish reason:", response.choices[0].finish_reason)
    print("Content:", repr(response.choices[0].message.content))
    print(
        "Tokens — "
        f"input: {response.usage.prompt_tokens}, "
        f"output: {response.usage.completion_tokens}, "
        f"total: {response.usage.total_tokens}"
    )


ask(0.2)
ask(1.2)