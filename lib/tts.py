"""Voce gratuita (Edge TTS) per ogni scena di una spec.
Uso: python3 lib/tts.py <spec.py> <cartella_lavoro> [velocita, es. +5%]
Scrive <cartella>/tts/sNN.mp3 e sNN.json (tempi delle parole)."""
import asyncio, os, json, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import edge_tts
from common import load_spec

spec = load_spec(sys.argv[1]); OUT = os.path.join(sys.argv[2], "tts")
# voce della spec (VOICE) o della singola scena (campo "voce"); voci provate il 22/11/2026:
# it-IT-GiuseppeMultilingualNeural = la più espressiva (variazione di tono 5,3 semitoni contro 3,7 di Elsa)
VOICE = getattr(spec, "VOICE", "it-IT-ElsaNeural")
RATE = sys.argv[3] if len(sys.argv) > 3 else getattr(spec, "RATE", "-4%")
os.makedirs(OUT, exist_ok=True)

async def one(i, s, sem):
    mp3 = f"{OUT}/s{i:02d}.mp3"; js = f"{OUT}/s{i:02d}.json"
    if os.path.exists(mp3) and os.path.exists(js) and os.path.getsize(mp3) > 1000:
        return
    async with sem:
        for attempt in range(5):
            try:
                c = edge_tts.Communicate(s["text"], s.get("voce", VOICE), rate=s.get("rate", RATE), boundary="WordBoundary",
                                         proxy=os.environ.get("HTTPS_PROXY"))
                words = []
                with open(mp3, "wb") as f:
                    async for ch in c.stream():
                        if ch["type"] == "audio": f.write(ch["data"])
                        elif ch["type"] == "WordBoundary":
                            words.append(dict(t=ch["offset"] / 1e7, d=ch["duration"] / 1e7, w=ch["text"]))
                if not words: raise RuntimeError("nessun tempo di parola")
                json.dump(words, open(js, "w"), ensure_ascii=False)
                print("voce ok", i, len(words), flush=True); return
            except Exception as e:
                print("riprovo", i, attempt, e, flush=True); await asyncio.sleep(4)
        raise RuntimeError(f"voce fallita alla scena {i}")

async def main():
    sem = asyncio.Semaphore(4)
    await asyncio.gather(*[one(i, s, sem) for i, s in enumerate(spec.SCENES)])

asyncio.run(main())
