"""Storia dei Soldi - documentario 16:9 (carta, Playfair + Source Sans, linea del tempo, capitoli).
Uso: python3 doc/render_doc.py <spec.py> <cartella_lavoro> [preview 0,5,12]
Prima serve la voce: python3 lib/tts.py <spec.py> <cartella_lavoro>
La spec definisce TITLE, CHAPTERS {numero: "Capitolo 1 · Nome"}, TIMELINE (anno_inizio, 2026), SCENES, COVER."""
import os, sys, json, subprocess
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "lib"))
import numpy as np
from PIL import Image, ImageDraw
from common import *

spec = load_spec(sys.argv[1]); WD = sys.argv[2]
W, H = 1920, 1080
BG = make_bg(W, H, border=12)
Y0, Y1 = getattr(spec, "TIMELINE", (1860, 2026))
TITLE = spec.TITLE; CHAPTERS = getattr(spec, "CHAPTERS", {})

def timeline(d, year):
    x0, x1, y = 150, 1770, 968
    def X(yr): return x0 + (x1 - x0) * (yr - Y0) / (Y1 - Y0)
    d.line([(x0, y), (x1, y)], fill=DARK, width=4)
    step = 10 if (Y1 - Y0) <= 180 else 20
    start = Y0 + (-Y0) % step
    for yr in range(start, 2021, step):
        big = (yr // step) % 2 == 0
        d.line([(X(yr), y - (14 if big else 8)), (X(yr), y + (14 if big else 8))], fill=DARK, width=4 if big else 3)
        if big and X(2026) - X(yr) > 90: d.text((X(yr), y + 22), str(yr), font=F("ss6", 26), fill=GREY, anchor="mt")
    d.line([(x1, y - 14), (x1, y + 14)], fill=DARK, width=4); d.text((x1, y + 22), "2026", font=F("ss6", 26), fill=GREY, anchor="mt")
    if year is not None:
        xm = X(year)
        d.line([(x0, y), (xm, y)], fill=RED, width=7)
        d.ellipse((xm - 13, y - 13, xm + 13, y + 13), fill=RED)
        f = F("ss7", 34); tw = d.textlength(str(year), font=f)
        d.rounded_rectangle((xm - tw / 2 - 18, y - 76, xm + tw / 2 + 18, y - 26), radius=10, fill=RED)
        d.text((xm, y - 51), str(year), font=f, fill=CREAM, anchor="mm")

def base_frame(s):
    im = BG.copy(); d = ImageDraw.Draw(im)
    d.text((110, 64), "STORIA DEI SOLDI", font=F("ss7", 32), fill=KICK)
    kx = 110 + d.textlength("STORIA DEI SOLDI", font=F("ss7", 32)) + 22
    d.text((kx, 60), TITLE, font=F("pfi", 34), fill=GREY)
    ch = CHAPTERS.get(s.get("chunk", 0), "")
    if ch and not s.get("card"):
        d.text((W - 110, 66), ch.upper(), font=F("ss6", 28), fill=KICK, anchor="ra")
    if s.get("card"):
        f = fit(d, s["big"], "pf9", 170, 1500)
        d.text((W / 2, 300), s["big"], font=f, fill=RED, anchor="mm")
        d.line([(W / 2 - 180, 420), (W / 2 + 180, 420)], fill=DARK, width=6)
        d.text((W / 2, 530), s["sub1"], font=fit(d, s["sub1"], "pf7", 110, 1500), fill=DARK, anchor="mm")
        d.text((W / 2, 660), s.get("sub2", ""), font=F("ss4", 50), fill=GREY, anchor="mm")
        timeline(d, s.get("year")); return im
    LX, LW_ = 110, 1100
    f = fit(d, s["big"], "pf9", 150, LW_, 60)
    bb = d.textbbox((LX, 0), s["big"], font=f)
    ytop = 165; d.text((LX, ytop - bb[1]), s["big"], font=f, fill=RED)
    y = ytop + (bb[3] - bb[1]) + 40
    d.line([(LX, y), (LX + 300, y)], fill=DARK, width=6); y += 34
    f1 = F("pf7", 60)
    for l in wrap(d, s.get("sub1", ""), f1, LW_)[:2]:
        d.text((LX, y), l, font=f1, fill=DARK); y += 74
    y += 10; f2 = F("ss4", 40)
    for l in wrap(d, s.get("sub2", ""), f2, LW_)[:2]:
        d.text((LX, y), l, font=f2, fill=GREY); y += 52
    if s.get("src"): d.text((LX, y + 14), s["src"], font=F("pfi", 30), fill=GREY)
    ic = get_icon(s.get("icon", "coin"), 430); im.paste(ic, (1500 - 215, 150), ic)
    timeline(d, s.get("year"))
    return im

def caption(im, text):
    if not text: return im
    im = im.copy(); d = ImageDraw.Draw(im)
    f = F("ss6", 46); tw = d.textlength(text, font=f)
    while tw > 1640: f = F("ss6", f.size - 2); tw = d.textlength(text, font=f)
    cx, cy = W / 2, 820
    d.rounded_rectangle((cx - tw / 2 - 36, cy - 44, cx + tw / 2 + 36, cy + 44), radius=18, fill=CAPBG)
    d.text((cx, cy - 2), text, font=f, fill=CAPTX, anchor="mm")
    return im

def main():
    fr = os.path.join(WD, "frames"); os.makedirs(fr, exist_ok=True)
    SR = 48000; audio = []; concat = []; fidx = 0; SC = spec.SCENES
    for i, s in enumerate(SC):
        words = json.load(open(f"{WD}/tts/s{i:02d}.json"))
        pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", f"{WD}/tts/s{i:02d}.mp3", "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout
        a = np.frombuffer(pcm, np.float32)
        lead = 0.5 if s.get("card") else 0.3
        tail = 1.6 if s.get("card") else 1.0
        if i + 1 < len(SC) and SC[i + 1].get("card"): tail += 0.8
        seg = np.zeros(int(round((lead + len(a) / SR + tail) * SR)), np.float32)
        seg[int(lead * SR):int(lead * SR) + len(a)] = a; audio.append(seg)
        base = base_frame(s)
        if s.get("card"):
            p = f"{fr}/f{fidx:04d}.png"; base.save(p, compress_level=1); fidx += 1
            concat.append((p, len(seg) / SR))
        else:
            cc = caption_chunks(s["text"], words)
            starts = [lead + t for t, _ in cc] + [len(seg) / SR]; starts[0] = 0.0
            for k, (t, text) in enumerate(cc):
                p = f"{fr}/f{fidx:04d}.png"; caption(base, text).save(p, compress_level=1); fidx += 1
                concat.append((p, starts[k + 1] - starts[k]))
        print("scena", i, round(len(seg) / SR, 1), flush=True)
    full = np.concatenate(audio); full.astype(np.float32).tofile(f"{WD}/narr.f32")
    with open(f"{WD}/concat.txt", "w") as f:
        for p, du in concat: f.write(f"file '{os.path.abspath(p)}'\nduration {du:.4f}\n")
        f.write(f"file '{os.path.abspath(concat[-1][0])}'\n")
    # tempi dei capitoli per la descrizione di YouTube
    t = 0.0; chap = []
    for i, s in enumerate(SC):
        if s.get("card"): chap.append((t, s["big"] + " - " + s["sub1"]))
        t += len(audio[i]) / SR
    json.dump([{"t": round(c[0], 1), "titolo": c[1]} for c in chap], open(f"{WD}/capitoli.json", "w"), ensure_ascii=False, indent=1)
    print("totale secondi", round(len(full) / SR, 1), "fotogrammi", fidx, "capitoli", [(int(c[0] // 60), int(c[0] % 60), c[1]) for c in chap])

def preview(idx):
    os.makedirs(WD, exist_ok=True)
    for i in idx:
        caption(base_frame(spec.SCENES[i]), "Didascalia di prova").save(f"{WD}/prev_{i:02d}.png")
    print("anteprime in", WD)

def cover():
    c = spec.COVER; CW, CH = 1280, 720
    bg = make_bg(CW, CH, border=10, seed=3); d = ImageDraw.Draw(bg)
    d.text((70, 58), "STORIA DEI SOLDI", font=F("ss7", 30), fill=DARK)
    d.text((64, 232), c["line1"], font=fit(d, c["line1"], "pf9", 128, 760, 70), fill=DARK, anchor="ls")
    d.text((60, 455), c["big"], font=fit(d, c["big"], "pf9", 200, 780, 90), fill=RED, anchor="ls")
    f = F("ss7", 50); t = c["pill"]; tw = d.textlength(t, font=f)
    while tw > 1100: f = F("ss7", f.size - 2); tw = d.textlength(t, font=f)
    d.rounded_rectangle((70, 500, 70 + tw + 56, 584), radius=12, fill=DARK); d.text((98, 542), t, font=f, fill=CAPTX, anchor="lm")
    d.text((72, 612), c["sub"], font=fit(d, c["sub"], "pfi", 40, 1140, 28), fill=GREY)
    ic = get_icon(c.get("icon", "coin"), 380); bg.paste(ic, (840, 150), ic)
    bg.save(f"{WD}/copertina.png"); print("copertina", f"{WD}/copertina.png")

if __name__ == "__main__":
    if len(sys.argv) > 3 and sys.argv[3] == "preview": preview([int(x) for x in sys.argv[4].split(",")])
    elif len(sys.argv) > 3 and sys.argv[3] == "cover": cover()
    else: main()
