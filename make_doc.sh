#!/usr/bin/env bash
# Uso: bash make_doc.sh <spec.py> <nome>  ->  lavoro/<nome>/<nome>.mp4 + copertina.png + capitoli.json
set -e
cd "$(dirname "$0")"
export SSL_CERT_FILE=${SSL_CERT_FILE:-/root/.ccr/ca-bundle.crt}
SPEC="$1"; NOME="$2"; WD="lavoro/$NOME"; mkdir -p "$WD"
python3 lib/tts.py "$SPEC" "$WD"
python3 doc/render_doc.py "$SPEC" "$WD"
python3 doc/render_doc.py "$SPEC" "$WD" cover
ffmpeg -v error -y -f f32le -ar 48000 -ac 1 -i "$WD/narr.f32" -af "highpass=f=70,loudnorm=I=-16:TP=-1.5:LRA=11" -ar 48000 -ac 2 -c:a pcm_s16le "$WD/narr.wav"
ffmpeg -v error -y -f concat -safe 0 -i "$WD/concat.txt" -i "$WD/narr.wav" -vf "fps=15,format=yuv420p" \
  -c:v libx264 -preset veryfast -tune stillimage -crf 23 -g 300 -c:a aac -b:a 96k -shortest -movflags +faststart "$WD/$NOME.mp4"
rm -f "$WD/narr.f32" "$WD/narr.wav"
ffprobe -v error -show_entries format=duration,size -of default=nw=1 "$WD/$NOME.mp4"
SIZE=$(stat -c %s "$WD/$NOME.mp4"); [ "$SIZE" -lt 95000000 ] || echo "ATTENZIONE: file oltre 95 MB, GitHub non lo accetta: alza crf a 26"
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$WD/$NOME.mp4")
ffmpeg -v error -y -i "$WD/$NOME.mp4" -vf "fps=12/$D,scale=320:-1,tile=4x3" -frames:v 1 "$WD/controllo.png"
echo "fatto: $WD/$NOME.mp4  (guarda $WD/controllo.png e $WD/copertina.png)"
