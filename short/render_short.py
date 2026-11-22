"""Storia dei Soldi - short verticale 1080x1920 (stesso stile degli short già pubblicati).
Uso: python3 short/render_short.py <spec.py> <cartella_lavoro> [preview]
Prima serve la voce: python3 lib/tts.py <spec.py> <cartella_lavoro>
Scrive <cartella>/frames, concat.txt, narr.f32 (oppure, con preview, prev_NN.png)."""
import os, sys, json, subprocess
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "lib"))
import numpy as np
from PIL import Image, ImageDraw
from common import *

spec = load_spec(sys.argv[1]); WD = sys.argv[2]
W, H = 1080, 1920
BG = make_bg(W, H, border=0, seed=11)
Y0, Y1 = getattr(spec, "TIMELINE", (1900, 2026))
TITLE = spec.TITLE; UNDER = getattr(spec, "UNDER", "")
DEFAULT_YEAR = getattr(spec, "YEAR", None)

def draw_title(d):
    f = F("pf7", 66); lines = wrap(d, TITLE, f, 940)[:2]; y = 168
    for l in lines:
        d.text((W / 2, y), l, font=f, fill=INK, anchor="ma")
        if UNDER and UNDER in l:
            x0 = W / 2 - d.textlength(l, font=f) / 2 + d.textlength(l[:l.index(UNDER)], font=f)
            x1 = x0 + d.textlength(UNDER, font=f)
            d.line([(x0, y + 82), (x1, y + 82)], fill=RED, width=5)
        y += 84

def timeline(d, year):
    x0, x1, y = 90, 990, 1545
    def X(yr): return x0 + (x1 - x0) * (yr - Y0) / (Y1 - Y0)
    d.line([(x0, y), (x1, y)], fill=DARK, width=3)
    start = Y0 - Y0 % 10
    for yr in range(start, 2021, 10):
        if yr < Y0: continue
        big = (yr - Y0) % 20 == 0
        d.line([(X(yr), y - (11 if big else 6)), (X(yr), y + (11 if big else 6))], fill=DARK, width=3 if big else 2)
        if big and yr <= 2010: d.text((X(yr), y + 20), str(yr), font=F("ss6", 22), fill=GREY, anchor="mt")
    d.line([(x1, y - 11), (x1, y + 11)], fill=DARK, width=3); d.text((x1, y + 20), "2026", font=F("ss6", 22), fill=GREY, anchor="mt")
    if year is not None:
        xm = X(year)
        d.line([(x0, y), (xm, y)], fill=RED, width=6)
        d.ellipse((xm - 11, y - 11, xm + 11, y + 11), fill=RED)
        f = F("ss7", 28); tw = d.textlength(str(year), font=f)
        d.rounded_rectangle((xm - tw / 2 - 14, y - 62, xm + tw / 2 + 14, y - 22), radius=8, fill=RED)
        d.text((xm, y - 42), str(year), font=f, fill=CREAM, anchor="mm")

def frame(s, shown_items=0):
    im = BG.copy(); d = ImageDraw.Draw(im)
    d.text((W / 2, 100), "STORIA DEI SOLDI", font=F("ss7", 30), fill=KICK, anchor="mm")
    kind = s.get("kind", "hero")
    if kind != "end": draw_title(d)
    if kind == "hero":
        ic = get_icon(s.get("icon", "coin"), 380); im.paste(ic, (W // 2 - 190, 420), ic)
        f = fit(d, s["big"], "pf9", 230, 960, 90)
        d.text((W / 2, 930), s["big"], font=f, fill=RED, anchor="mm")
        d.line([(W / 2 - 180, 1082), (W / 2 + 180, 1082)], fill=DARK, width=6)
        y = 1110
        f1 = F("pf7", 58)
        for l in wrap(d, s.get("sub1", ""), f1, 960)[:2]:
            if l: d.text((W / 2, y), l, font=f1, fill=DARK, anchor="ma"); y += 72
        f2 = F("ss4", 40)
        for l in wrap(d, s.get("sub2", ""), f2, 960)[:2]:
            if l: d.text((W / 2, y + 4), l, font=f2, fill=GREY, anchor="ma"); y += 50
        if s.get("src"): d.text((W / 2, y + 14), s["src"], font=F("pfi", 30), fill=GREY, anchor="ma")
    elif kind == "list":
        f = F("pf7", 62); hd = s["heading"]
        d.text((W / 2, 415), hd, font=f, fill=DARK, anchor="mm")
        tw = d.textlength(hd, font=f); d.line([(W / 2 - tw / 2 + 40, 460), (W / 2 + tw / 2 - 40, 460)], fill=RED, width=5)
        fi = F("ss6", 50); y = 552
        for k, it in enumerate(s["items"][:shown_items]):
            txt = it[0] if isinstance(it, (list, tuple)) else it
            fi_ = fit(d, txt, "ss6", 50, 820, 34)
            d.ellipse((150, y - 26, 202, y + 26), fill=RED)
            d.text((176, y), str(k + 1), font=F("ss7", 34), fill=CREAM, anchor="mm")
            d.text((228, y), txt, font=fi_, fill=INK, anchor="lm"); y += 100
        if s.get("src"): d.text((W / 2, 1290), s["src"], font=F("pfi", 30), fill=GREY, anchor="ma")
    elif kind == "end":
        d.rectangle((0, 420, W, 1180), fill=CARD)
        d.text((W / 2, 530), "STORIA DEI SOLDI", font=F("ss7", 34), fill=GOLD, anchor="mm")
        fb = F("pf9", 112); lines = wrap(d, s["big"], fb, 940)[:3]
        while len(lines) > 2 and fb.size > 80:
            fb = F("pf9", fb.size - 8); lines = wrap(d, s["big"], fb, 940)[:3]
        y = 680 - (len(lines) - 1) * 60
        for l in lines: d.text((W / 2, y), l, font=fb, fill=CREAM, anchor="mm"); y += 120
        if s.get("sub1"): d.text((W / 2, y + 6), s["sub1"], font=fit(d, s["sub1"], "pfi", 80, 960), fill=CAPTX, anchor="mm"); y += 100
        if s.get("sub2"): d.text((W / 2, y - 10), s["sub2"], font=fit(d, s["sub2"], "ss4", 40, 980, 28), fill=CAPTX, anchor="mm")
    timeline(d, s.get("year", DEFAULT_YEAR))
    return im

def caption(im, text):
    if not text: return im
    im = im.copy(); d = ImageDraw.Draw(im)
    size = 50; f = F("ss6", size)
    while d.textlength(text, font=f) > 940 and size > 30: size -= 2; f = F("ss6", size)
    tw = d.textlength(text, font=f); cx, cy = W / 2, 1375
    d.rounded_rectangle((cx - tw / 2 - 30, cy - 40, cx + tw / 2 + 30, cy + 40), radius=14, fill=CAPBG)
    x = cx - tw / 2
    for i, w_ in enumerate(text.split(" ")):
        piece = w_ + (" " if i < len(text.split(" ")) - 1 else "")
        col = CAPNUM if any(ch.isdigit() for ch in w_) else CAPTX
        d.text((x, cy - 2), piece, font=f, fill=col, anchor="lm"); x += d.textlength(piece, font=f)
    return im

def scene_events(s, words, lead):
    """Momenti (s, dall'inizio della scena) in cui cambia qualcosa: didascalia o voce di elenco."""
    cc = caption_chunks(s["text"], words, maxlen=34, minlen=10)
    ev = [(lead + t, "cap", txt) for t, txt in cc]
    if s.get("kind") == "list":
        for k, it in enumerate(s["items"]):
            cue = it[1] if isinstance(it, (list, tuple)) and len(it) > 1 else None
            t = cue_time(s["text"], words, cue) if cue else None
            if t is None: t = (words[-1]["t"] if words else 0) * (k + 1) / (len(s["items"]) + 1)
            ev.append((lead + t - 0.15, "item", k + 1))
    ev.sort(key=lambda e: e[0]); return ev

def main():
    fr = os.path.join(WD, "frames"); os.makedirs(fr, exist_ok=True)
    SR = 48000; audio = []; concat = []; fidx = 0
    for i, s in enumerate(spec.SCENES):
        words = json.load(open(f"{WD}/tts/s{i:02d}.json"))
        pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", f"{WD}/tts/s{i:02d}.mp3", "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout
        a = np.frombuffer(pcm, np.float32)
        lead = 0.0 if i == 0 else 0.25
        tail = 1.4 if s.get("kind") == "end" and i == len(spec.SCENES) - 1 else 0.5
        seg = np.zeros(int(round((lead + len(a) / SR + tail) * SR)), np.float32)
        seg[int(lead * SR):int(lead * SR) + len(a)] = a; audio.append(seg); dur = len(seg) / SR
        ev = scene_events(s, words, lead)
        cap = ""; items = 1 if s.get("kind") == "list" else 0
        # primo fotogramma pieno: la prima didascalia e (per gli elenchi) il primo elemento già visibili
        pts = [0.0] + [max(0.0, e[0]) for e in ev] + [dur]
        state = []
        for e in ev:
            if e[1] == "cap": cap = e[2]
            else: items = max(items, e[2])
            state.append((max(0.0, e[0]), cap, items))
        first_cap = next((e[2] for e in ev if e[1] == "cap"), "")
        segs = [(0.0, first_cap, 1 if s.get("kind") == "list" else 0)] + state
        # tieni solo cambi reali e ordinati
        clean = []
        for t, c, it in segs:
            if clean and abs(t - clean[-1][0]) < 0.12: clean[-1] = (clean[-1][0], c, it); continue
            clean.append((t, c, it))
        for k, (t, c, it) in enumerate(clean):
            t_next = clean[k + 1][0] if k + 1 < len(clean) else dur
            if t_next - t <= 0.01: continue
            p = f"{fr}/f{fidx:04d}.png"; caption(frame(s, it), c).save(p, compress_level=1); fidx += 1
            concat.append((p, t_next - t))
        print("scena", i, round(dur, 1), "s", flush=True)
    full = np.concatenate(audio); full.astype(np.float32).tofile(f"{WD}/narr.f32")
    with open(f"{WD}/concat.txt", "w") as f:
        for p, du in concat: f.write(f"file '{os.path.abspath(p)}'\nduration {du:.4f}\n")
        f.write(f"file '{os.path.abspath(concat[-1][0])}'\n")
    print("totale secondi", round(len(full) / SR, 1), "fotogrammi", fidx)

def preview():
    os.makedirs(WD, exist_ok=True)
    for i, s in enumerate(spec.SCENES):
        n = len(s.get("items", []))
        caption(frame(s, n), "Didascalia di prova con 1.234 lire").save(f"{WD}/prev_{i:02d}.png")
    print("anteprime in", WD)

if __name__ == "__main__":
    preview() if len(sys.argv) > 3 and sys.argv[3] == "preview" else main()
