# 🧠 RHEA - Roadmap & Idées d'Amélioration

## ✅ Fonctionnalités existantes
- [x] Lecture de flux RSS (avec lignes commentées)
- [x] Résumés IA via OpenAI
- [x] Classement par catégorie
- [x] Export Markdown quotidien
- [x] Top 5 des actus du jour
- [x] Makefile : veille + flux-check

---

## 🛠️ Idées & améliorations futures

### 🧩 Ergonomie & usage
- [ ] `make veille-dry-run` (affiche les résumés sans exporter)
- [ ] Interface CLI avec `argparse` ou `typer`
- [ ] Prompt IA customisable par catégorie ou source
- [ ] Fichier `flux-example.txt` avec suggestions

### 📚 Traitement enrichi
- [ ] Récupérer les `summary` complets des articles RSS
- [ ] Résumer tout l'article (pas juste le titre)
- [ ] Générer export `.json` ou `.csv`

### 🌐 Intégration
- [ ] Exporter par email
- [ ] Commit automatique dans un dépôt Git
- [ ] Générer une page statique HTML (Docsify / Hugo)
- [ ] Ajouter un raccourci Raycast pour déclencher `make veille`

### 🤖 Bonus IA
- [ ] Génération de bullet points synthétiques
- [ ] Traduction automatique (en option)
- [ ] Génération d’un tag cloud de mots-clés
