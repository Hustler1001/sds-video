#!/usr/bin/env bash
# Pubblica dei file su un branch temporaneo del repo pubblico e stampa gli indirizzi diretti per Posty.
# Uso: bash consegna.sh <file1> [file2 ...]
# Dopo il caricamento su Posty (upload_media_from_url) cancella il branch:  git push origin --delete <branch>
set -e
cd "$(dirname "$0")"
REMOTE=$(git remote get-url origin)
B="consegna-$(date +%Y%m%d-%H%M%S)"
TMP=$(mktemp -d)
for f in "$@"; do cp "$f" "$TMP/"; done
( cd "$TMP" && git init -q && git checkout -q -b "$B" && git add -A && \
  git -c user.name="Storia dei Soldi" -c user.email="noreply@storiadeisoldi.local" commit -q -m "consegna $B" && \
  git push -q "$REMOTE" "$B" )
echo "BRANCH=$B"
for f in "$@"; do echo "URL=https://raw.githubusercontent.com/Hustler1001/sds-video/$B/$(basename "$f")"; done
