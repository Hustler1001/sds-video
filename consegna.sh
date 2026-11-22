#!/usr/bin/env bash
# Mette dei file su un branch temporaneo del repo pubblico (sovrascritto ogni volta) e stampa gli indirizzi
# diretti per Posty (upload_media_from_url). L'indirizzo usa il codice del commit, quindi non cambia mai.
# Uso: bash consegna.sh <file1> [file2 ...]
set -e
cd "$(dirname "$0")"
REMOTE=$(git remote get-url origin)
B="consegna"
TMP=$(mktemp -d)
for f in "$@"; do cp "$f" "$TMP/"; done
cd "$TMP"
git init -q && git checkout -q -b "$B" && git add -A
git -c user.name="Storia dei Soldi" -c user.email="noreply@storiadeisoldi.local" commit -q -m "consegna $(date +%Y%m%d-%H%M%S)"
SHA=$(git rev-parse HEAD)
git push -q -f "$REMOTE" "$B" 2>&1 | grep -v "^remote:" || true
git ls-remote "$REMOTE" "refs/heads/$B" | grep -q "$SHA" || { echo "ERRORE: push non riuscito"; exit 1; }
for f in "$@"; do echo "URL=https://raw.githubusercontent.com/Hustler1001/sds-video/$SHA/$(basename "$f")"; done
