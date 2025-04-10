import sys
from pathlib import Path

# ➕ Ajoute le dossier racine du projet au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent))

from rhea.rss import load_rss_links

flux_file = "sources/flux.txt"

print("📡 Flux RSS activés :\n")
for link in load_rss_links(flux_file):
    print(f"• {link}")

