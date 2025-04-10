
.PHONY: veille flux-check

# Génère le rapport de veille
veille:
	pipenv run python main.py

# Affiche les flux RSS activés
flux-check:
	pipenv run python tools/flux_check.py

publish:
	git add exports/
	git commit -m "💾 Veille du $(shell date +'%Y-%m-%d')"
	git push

# Génère la veille ET la pousse sur Git
deploy: veille publish
