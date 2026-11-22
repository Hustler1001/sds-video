#!/usr/bin/env bash
# Prepara l'ambiente (una volta per sessione). Tutto gratuito.
set -e
cd "$(dirname "$0")"
export SSL_CERT_FILE=${SSL_CERT_FILE:-/root/.ccr/ca-bundle.crt}
python3 -c "import edge_tts, PIL, numpy" 2>/dev/null || pip install --break-system-packages -q edge-tts pillow numpy
[ -d node_modules/@fontsource/playfair-display ] || npm install --silent --no-audit --no-fund
command -v ffmpeg >/dev/null || (apt-get update -qq && apt-get install -y -qq ffmpeg)
echo "setup ok"
