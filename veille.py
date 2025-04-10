import os
import feedparser
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
FLUX_FILE = "sources/flux.txt"

def get_rss_links():
    with open(FLUX_FILE, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def summarize(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu es un assistant DevOps qui résume des actualités techniques de façon claire et concise."},
                {"role": "user", "content": f"Résume ceci en une phrase : {text}"}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"⚠️ Erreur de résumé : {e}"

def main():
    print("📰 RHEA - Agent de veille technologique")
    links = get_rss_links()
    for url in links:
        print(f"
🔗 Lecture du flux : {url}")
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:
            print(f"
→ {entry.title}")
            summary = summarize(entry.title)
            print(f"   Résumé IA : {summary}")

if __name__ == "__main__":
    main()
