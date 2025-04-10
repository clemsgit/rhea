import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize(text: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu es un assistant DevOps qui résume des actualités techniques de façon claire et concise."},
                {"role": "user", "content": f"Résume ceci en une phrase : {text}"}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Erreur : {e}"
