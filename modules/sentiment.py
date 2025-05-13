import os
from dotenv import load_dotenv
from openai import OpenAI

def analyze_sentiment(text: str) -> str:
    """Analyze sentiment of text using OpenAI GPT."""
    # Reload env and init client per call
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OpenAI API key not configured")
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Analyze the sentiment of the following text and return a single word or short phrase."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()
