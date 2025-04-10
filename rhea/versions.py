import feedparser
import json
from pathlib import Path

CONFIG_FILE = "sources/tracked_components.json"

def load_tracked_components():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def get_latest_version_from_rss(url: str) -> str:
    feed = feedparser.parse(url)
    if not feed.entries:
        return "N/A"
    return feed.entries[0].title.strip()

def check_versions():
    print("🔍 Vérification des versions suivies :\n")
    components = load_tracked_components()
    for name, info in components.items():
        current = info.get("current", "N/A")
        latest = get_latest_version_from_rss(info["url"])
        status = "✅ À jour" if latest == current else "⬆️ Màj dispo"
        print(f"- {name:<12} | Actuelle : {current:<15} | Dernière : {latest:<15} | {status}")

if __name__ == "__main__":
    check_versions()
