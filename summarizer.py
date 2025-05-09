import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_with_gpt(content):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assistant that summarizes meeting notes."},
            {"role": "user", "content": f"Please summarize the following content:\n\n{content}"}
        ]
    )
    return response.choices[0].message.content.strip()
