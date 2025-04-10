from dotenv import load_dotenv
from rhea.rss import load_rss_links, fetch_latest_articles
from rhea.llm import summarize
from rhea.categorizer import categorize
from rhea.export import export_markdown

load_dotenv()

RSS_FILE = "sources/flux.txt"

def run():
    print("🧠 RHEA Veille Tech - catégorisation IA")
    urls = load_rss_links(RSS_FILE)
    all_entries = []

    for url in urls:
        for title, link, source, summary_text in fetch_latest_articles(url):
            print(f"• {title}")
            summary = summarize(summary_text)
            print(f"  Résumé : {summary}")

            full_text = f"{title} - {summary_text}"
            category = categorize(full_text)
            print(f"  Catégorie : {category}\n")

            all_entries.append((title, link, source, summary, category))

    md_path = export_markdown(all_entries)
    print(f"📄 Export markdown généré : {md_path}")

if __name__ == "__main__":
    run()
