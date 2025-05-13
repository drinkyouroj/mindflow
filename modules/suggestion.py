import os
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def why_am_i_feeling_this(prompt: str) -> str:
    """Generate introspective suggestions using OpenAI GPT."""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a supportive assistant that helps users understand why they might be feeling certain emotions."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
