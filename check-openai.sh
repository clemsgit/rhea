#!/bin/bash

# Vérifie l'accès à l'API OpenAI

if [ -z "$OPENAI_API_KEY" ]; then
  echo "❌ Variable OPENAI_API_KEY non définie."
  echo "Exporte-la avec : export OPENAI_API_KEY=sk-xxx"
  exit 1
fi

echo "🔍 Test de l'accès à l'API OpenAI..."

curl -s https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  | jq '.data[] | .id' || echo "⚠️ Échec ou jq non installé."

echo "✅ Terminé."
