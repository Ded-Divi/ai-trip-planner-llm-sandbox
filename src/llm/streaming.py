import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.environ["GROQ_API_KEY"])

stream = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": "Write three concise tips for a first-time budget traveller to Goa.",
        }
    ],
    stream=True,
    max_completion_tokens=180,
    reasoning_effort="low",
)

for chunk in stream:
    text = chunk.choices[0].delta.content

    if text:
        print(text, end="", flush=True)

print()