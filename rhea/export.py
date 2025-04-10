from datetime import datetime
from pathlib import Path
from typing import List, Tuple
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def icon_for(category: str) -> str:
    return {
        "Kubernetes": "☸️",
        "GitLab": "🦊",
        "Terraform": "🌍",
        "Docker": "🐳",
        "Sécurité": "🔐",
        "Cloud": "☁️",
        "Autres": "🧩"
    }.get(category, "📄")

def summarize_category(category: str, items: List[Tuple[str, str, str]]) -> str:
    prompt = f"Voici une série d'articles de la catégorie {category} :\n\n"
    for title, _, _, summary in items:
        prompt += f"- {title}: {summary}\n"
    prompt += "\nDonne-moi un résumé global de ces actus en une ou deux phrases."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu es un assistant DevOps qui synthétise l'actualité technique."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"(Erreur dans le résumé de la catégorie : {e})"

def export_markdown(entries: List[Tuple[str, str, str, str, str]]) -> str:
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"veille_{date_str}.md"
    output_path = Path("exports")
    output_path.mkdir(exist_ok=True)
    full_path = output_path / filename

    categorized = {}
    for title, link, source, summary, category in entries:
        categorized.setdefault(category, []).append((title, link, source, summary))

    top_entries = sorted(entries, key=lambda x: len(x[3]), reverse=True)[:5]

    with open(full_path, "w") as f:
        f.write(f"# Veille Tech - {date_str}\n\n")

        f.write("## 🚀 Top 5 des actus du jour\n\n")
        for title, link, source, summary, _ in top_entries:
            max_length = 200
            short_summary = summary if len(summary) <= max_length else summary[:max_length].rstrip() + "..."
            f.write(f"- **[{title}]({link})**\n  - Source : {source}\n  - {short_summary}\n\n")

        f.write("---\n\n")

        for cat, items in categorized.items():
            f.write(f"## {icon_for(cat)} {cat}\n\n")
            cat_summary = summarize_category(cat, items)
            f.write(f"**Synthèse :** {cat_summary}\n\n")
            for title, link, source, summary in items:
                f.write(f"- **[{title}]({link})**\n  - Source : {source}\n  - Résumé : {summary}\n\n")

    return str(full_path)
