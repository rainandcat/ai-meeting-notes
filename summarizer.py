from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_with_gpt(content):
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "You are an assistant that summarizes meeting notes."},
            {"role": "user", "content": f"Please summarize the following content:\n\n{content}"}
        ]
    )
    return response.choices[0].message.content.strip()
