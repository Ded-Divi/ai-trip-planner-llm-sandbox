import json
import os
from dotenv import load_dotenv
from groq import Groq

from src.llm.structured import TripPlan
from src.llm.retry import call_with_retry

load_dotenv()

client = Groq(api_key=os.environ["GROQ_API_KEY"])
def create_trip_plan():
    return client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a budget-conscious travel planner. "
                    "Do not invent current prices, availability, weather, "
                    "opening hours, or transport routes."
                ),
            },
            {
                "role": "user",
                "content": (
                    "Create a 4-day budget trip plan from Pune to Goa. "
                    "The traveller likes beaches, Goan food, and nightlife. "
                    "Include assumptions and items that need current verification."
                ),
            },
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "trip_plan",
                "schema": TripPlan.model_json_schema(),
            },
        },
    )

response = call_with_retry(create_trip_plan)

raw_plan = json.loads(response.choices[0].message.content or "{}")
trip_plan = TripPlan.model_validate(raw_plan)

print(trip_plan.model_dump_json(indent=2))



