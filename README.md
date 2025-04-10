# 🤖 RHEA — Assistant de veille technologique IA

**RHEA** (Recherche Heuristique d'Événements d'Actualité) est un outil de veille technique automatisée, propulsé par OpenAI.  
Il collecte les actualités depuis des flux RSS, génère des résumés, les classe par catégorie et les exporte au format Markdown.

> 🧠 Le tout en un simple `make veille`.

---

## ✨ Fonctionnalités

- 📡 Lecture de flux RSS (commentaires supportés dans `sources/flux.txt`)
- 🧠 Résumés générés par OpenAI à partir du titre + résumé RSS
- 🏷️ Catégorisation automatique (via LLM) : Kubernetes, GitLab, Terraform, etc.
- 📦 Export au format `Markdown` (avec icônes 🐳 ☁️ ☸️)
- 💡 Synthèse IA par catégorie
- 🚀 Commande `make publish` pour pousser les veilles sur un dépôt Git

---

## 🗂️ Structure

```
rhea/
├── main.py               # Point d'entrée
├── rhea/
│   ├── rss.py            # Chargement RSS
│   ├── llm.py            # Résumés OpenAI
│   ├── categorizer.py    # Catégorisation LLM
│   ├── export.py         # Export Markdown
├── sources/
│   └── flux.txt          # Liste des flux RSS
├── exports/              # Fichiers générés (.md)
├── Makefile              # Commandes utiles
├── .env                  # Clé OpenAI API
├── .gitignore
└── README.md
```

---

## 🚀 Utilisation

### 1. Cloner le projet

```bash
git clone git@github.com:ton-utilisateur/rhea.git
cd rhea
```

### 2. Installer les dépendances

```bash
pipenv install
```

### 3. Ajouter ta clé OpenAI

Crée un fichier `.env` :

```dotenv
OPENAI_API_KEY=sk-...
```

### 4. Lancer la veille

```bash
make veille
```

### 5. Pousser la veille sur Git

```bash
make publish
```

Ou les deux d’un coup :

```bash
make deploy
```

---

## 📰 Ajouter des flux

Ajoute simplement les liens RSS dans `sources/flux.txt`.  
Tu peux commenter des lignes avec `#`.

```txt
# Flux Kubernetes
https://kubernetes.io/feed.xml

# Rancher
https://www.suse.com/c/rancherblog/feed/
```

---

## 🔭 Roadmap (TODO)

- [x] Catégorisation IA
- [x] Synthèse par catégorie
- [x] Export Markdown
- [ ] Export JSON
- [ ] Interface HTML (Docsify ?)
- [ ] Intégration Raycast
- [ ] Assistant vocal (Jarvis style 😏)

---

## 🧠 Licence

MIT — libre de t’inspirer, modifier, forker, adapter.

---

> Codé avec ❤️ par un humain et une IA complice.
