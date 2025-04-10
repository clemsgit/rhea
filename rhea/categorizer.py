import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

CATEGORIES = [
    "Kubernetes",
    "GitLab",
    "Terraform",
    "Docker",
    "Sécurité",
    "Cloud",
    "Autres"
]

def categorize(text: str) -> str:
    try:
        prompt = f"Voici une actualité technique :\n\n{text}\n\n" +                  "Catégorise-la dans l'une des catégories suivantes (et uniquement une) : " + ", ".join(CATEGORIES) +                  ". Réponds uniquement par le nom de la catégorie."

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu es un assistant DevOps qui classifie des actualités techniques."},
                {"role": "user", "content": prompt}
            ]
        )
        category = response.choices[0].message.content.strip()
        return category if category in CATEGORIES else "Autres"
    except Exception as e:
        return f"Autres  # erreur : {e}"
