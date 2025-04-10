from typing import List, Tuple
import feedparser

def load_rss_links(filepath: str) -> List[str]:
    with open(filepath, "r") as f:
        return [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]

def fetch_latest_articles(url: str, limit: int = 3) -> List[Tuple[str, str, str, str]]:
    feed = feedparser.parse(url)
    source = url.split("//")[-1].split("/")[0]
    results = []
    for entry in feed.entries[:limit]:
        title = entry.title
        link = entry.link
        summary = getattr(entry, "summary", title)  # fallback si pas de summary
        results.append((title, link, source, summary))
    return results
