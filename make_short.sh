#!/usr/bin/env bash
# Uso: bash make_short.sh <spec.py> <nome>   ->  lavoro/<nome>/<nome>.mp4
set -e
cd "$(dirname "$0")"
export SSL_CERT_FILE=${SSL_CERT_FILE:-/root/.ccr/ca-bundle.crt}
SPEC="$1"; NOME="$2"; WD="lavoro/$NOME"; mkdir -p "$WD"
python3 lib/tts.py "$SPEC" "$WD"
python3 short/render_short.py "$SPEC" "$WD"
ffmpeg -v error -y -f f32le -ar 48000 -ac 1 -i "$WD/narr.f32" -af "highpass=f=70,loudnorm=I=-16:TP=-1.5:LRA=11" -ar 48000 -ac 2 -c:a pcm_s16le "$WD/narr.wav"
ffmpeg -v error -y -f concat -safe 0 -i "$WD/concat.txt" -i "$WD/narr.wav" -vf "fps=30,format=yuv420p" \
  -c:v libx264 -preset veryfast -tune stillimage -crf 23 -g 60 -c:a aac -b:a 128k -shortest -movflags +faststart "$WD/$NOME.mp4"
ffprobe -v error -show_entries format=duration,size -of default=nw=1 "$WD/$NOME.mp4"
ffmpeg -v info -i "$WD/$NOME.mp4" -af ebur128 -f null - 2>&1 | grep -E "^\s+I:" | tail -1
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$WD/$NOME.mp4")
ffmpeg -v error -y -i "$WD/$NOME.mp4" -vf "fps=8/$D,scale=270:-1,tile=8x1" -frames:v 1 "$WD/controllo.png"
echo "fatto: $WD/$NOME.mp4  (guarda $WD/controllo.png)"
