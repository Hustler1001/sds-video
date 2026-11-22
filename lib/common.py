"""Storia dei Soldi - parti comuni: font, colori, carta, icone, testo, didascalie."""
import os, re, importlib.util
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FD = os.path.join(ROOT, "node_modules", "@fontsource")
_FONTS = {"pf9": "playfair-display/files/playfair-display-latin-900-normal.woff",
          "pf7": "playfair-display/files/playfair-display-latin-700-normal.woff",
          "pfi": "playfair-display/files/playfair-display-latin-400-italic.woff",
          "ss4": "source-sans-3/files/source-sans-3-latin-400-normal.woff",
          "ss6": "source-sans-3/files/source-sans-3-latin-600-normal.woff",
          "ss7": "source-sans-3/files/source-sans-3-latin-700-normal.woff"}
_FC = {}
def F(name, size):
    k = (name, int(size))
    if k not in _FC:
        _FC[k] = ImageFont.truetype(os.path.join(FD, _FONTS[name]), int(size))
    return _FC[k]

DARK = (34, 30, 28); INK = (40, 36, 33); GREY = (114, 106, 93); KICK = (94, 85, 70)
RED = (179, 62, 44); GOLD = (196, 150, 52); CREAM = (250, 246, 234); TEAL = (30, 91, 91)
CAPBG = (44, 40, 37); CAPTX = (243, 234, 216); CAPNUM = (240, 196, 76)
CARD = (36, 32, 29)

def load_spec(path):
    spec = importlib.util.spec_from_file_location("spec", path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

# ---------- carta ----------
def make_bg(W, H, border=0, seed=7):
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    d = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
    v = np.clip(d / 1.35, 0, 1)
    base = np.array([241, 232, 214], np.float32); edge = np.array([226, 217, 199], np.float32)
    img = base[None, None, :] * (1 - v[..., None]) + edge[None, None, :] * v[..., None]
    noise = rng.normal(0, 1, (H // 2, W // 2)).astype(np.float32)
    noise = np.array(Image.fromarray(((noise * 40) + 128).clip(0, 255).astype(np.uint8)).resize((W, H), Image.BILINEAR).filter(ImageFilter.GaussianBlur(1.2)), np.float32) - 128
    img += noise[..., None] * 0.09
    img += rng.normal(0, 2.2, (H, W)).astype(np.float32)[..., None]
    im = Image.fromarray(img.clip(0, 255).astype(np.uint8))
    if border:
        ImageDraw.Draw(im).rectangle((0, 0, W - 1, H - 1), outline=DARK, width=border)
    return im

# ---------- icone (disegnate su 840x840, poi ridotte) ----------
S2 = 840
ICONS = ["percent", "chart", "doc", "scale", "steps", "stairs", "coin", "coin:<testo>", "house", "wheat", "rings",
         "boxes", "envelope", "handshake", "receipt", "table", "people", "bank", "lock", "euro", "phone", "screen",
         "magnifier", "gamepad", "car", "cambiale", "cart", "piggy", "calendar", "bottle", "card", "factory", "oldman", "tv"]

def icon(name):
    im = Image.new("RGBA", (S2, S2), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    LW = 18
    def rr(box, fill=CREAM, r=30, w=LW, outline=DARK): d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=w)
    def ell(box, fill=CREAM, w=LW): d.ellipse(box, fill=fill, outline=DARK, width=w)
    def line(pts, col=DARK, w=LW): d.line(pts, fill=col, width=w, joint="curve")
    def txt(xy, s, f, col=DARK, anchor="mm"): d.text(xy, s, font=f, fill=col, anchor=anchor)
    label = None
    if ":" in name: name, label = name.split(":", 1)
    if name == "percent":
        ell((160, 160, 360, 360), fill=GOLD); ell((480, 480, 680, 680), fill=GOLD); line([(640, 180), (200, 660)], w=34)
    elif name == "chart":
        line([(150, 690), (700, 690)], w=22); line([(150, 690), (150, 150)], w=22)
        for i, h in enumerate([170, 260, 340, 430]):
            x = 210 + i * 120; rr((x, 690 - h, x + 85, 690), fill=RED if i == 3 else GOLD, r=8)
    elif name == "doc":
        rr((220, 120, 620, 720), r=20); txt((420, 210), label or "REDDITI", F("ss7", 54), TEAL)
        for i in range(6): line([(270, 300 + i * 60), (570 - (i % 3) * 60, 300 + i * 60)], col=GREY, w=10)
        line([(400, 660), (450, 630), (500, 655), (560, 615)], w=10)
    elif name == "scale":
        line([(420, 180), (420, 650)], w=22); line([(280, 680), (560, 680)], w=26)
        line([(180, 260), (660, 260)], w=22); ell((395, 155, 445, 205), fill=GOLD, w=12)
        for x in (220, 620):
            line([(x, 260), (x - 80, 450)], w=8); line([(x, 260), (x + 80, 450)], w=8)
            d.chord((x - 110, 380, x + 110, 520), 0, 180, fill=GOLD, outline=DARK, width=LW)
    elif name in ("steps", "stairs"):
        cols = [GOLD, GOLD, RED] if name == "steps" else [CREAM, GOLD, RED]
        for i in range(3):
            x = 170 + i * 170; h = 160 + i * 160; rr((x, 680 - h, x + 170, 680), fill=cols[i], r=6)
        if name == "stairs":
            ell((560, 140, 640, 220), fill=DARK, w=6); line([(600, 220), (600, 300)], w=16)
        line([(140, 690), (700, 690)], w=22)
    elif name == "coin":
        # coin -> "L." ; coin:5 -> due monete con "5" e "LIRE"
        if label:
            ell((250, 250, 730, 730), fill=GOLD, w=22)
            ell((110, 110, 590, 590), fill=GOLD, w=22); ell((165, 165, 535, 535), fill=GOLD, w=10)
            txt((350, 320), label, F("pf9", 190 if len(label) <= 2 else 120), DARK)
            txt((350, 450), "LIRE", F("ss7", 56), DARK)
        else:
            ell((150, 150, 690, 690), fill=GOLD, w=22); ell((215, 215, 625, 625), fill=GOLD, w=10)
            txt((420, 430), "L.", F("pf9", 210), DARK)
    elif name == "house":
        d.polygon([(420, 140), (140, 400), (700, 400)], fill=RED, outline=DARK); line([(420, 140), (140, 400), (700, 400), (420, 140)], w=LW)
        rr((200, 400, 640, 700), r=6); rr((370, 520, 470, 700), fill=GOLD, r=6); rr((240, 450, 330, 530), fill=TEAL, r=6); rr((510, 450, 600, 530), fill=TEAL, r=6)
    elif name == "wheat":
        line([(420, 720), (420, 180)], w=16)
        for side in (-1, 1):
            for k in range(5):
                y = 240 + k * 80; cx = 420 + side * 62
                d.ellipse((cx - 42, y - 62, cx + 42, y + 62), fill=GOLD, outline=DARK, width=12)
        d.ellipse((380, 120, 460, 250), fill=GOLD, outline=DARK, width=12)
    elif name == "rings":
        d.ellipse((150, 260, 490, 600), outline=DARK, width=60); d.ellipse((165, 275, 475, 585), outline=GOLD, width=30)
        d.ellipse((350, 260, 690, 600), outline=DARK, width=60); d.ellipse((365, 275, 675, 585), outline=GOLD, width=30)
        line([(560, 150), (300, 690)], col=RED, w=34)
    elif name == "boxes":
        for i in range(3):
            x = 130 + i * 210
            rr((x, 420, x + 170, 590), fill=GOLD, r=10); txt((x + 85, 505), "%", F("ss7", 90), DARK)
            if i < 2: line([(x + 180, 505), (x + 205, 505)], w=10)
        txt((420, 300), "+  +  +", F("ss7", 110), RED)
    elif name == "envelope":
        rr((150, 230, 690, 610), r=16); line([(160, 240), (420, 450), (680, 240)], w=LW)
        rr((440, 470, 700, 700), fill=GOLD, r=20); txt((570, 585), label or "-%", F("ss7", 110), DARK)
    elif name == "handshake":
        ell((170, 230, 470, 530), fill=GOLD); ell((370, 230, 670, 530), fill=CREAM)
        txt((320, 380), "TU", F("ss7", 70)); txt((520, 380), "STATO", F("ss7", 54))
        line([(220, 640), (620, 640)], col=RED, w=20)
    elif name == "receipt":
        pts = [(250, 120), (590, 120), (590, 690)]
        for k in range(8): pts.append((590 - k * 42.5, 690 if k % 2 == 0 else 655))
        pts.append((250, 690))
        d.polygon(pts, fill=CREAM, outline=DARK); d.line(pts + [pts[0]], fill=DARK, width=LW)
        txt((420, 200), label or "SCONTRINO", F("ss7", 44), TEAL)
        for i in range(4):
            line([(290, 280 + i * 60), (450, 280 + i * 60)], col=GREY, w=10); txt((550, 280 + i * 60), "0,00", F("ss6", 36), GREY, "rm")
        line([(290, 540), (550, 540)], w=8); txt((290, 590), "TOT", F("ss7", 52), RED, "lm")
    elif name == "table":
        rr((150, 470, 690, 530), fill=GOLD, r=8); line([(210, 530), (210, 700)], w=26); line([(630, 530), (630, 700)], w=26)
        rr((230, 200, 610, 380), r=16); txt((420, 290), label or "+22%", F("pf9", 120), RED)
    elif name == "people":
        for i in range(3):
            x = 220 + i * 200
            ell((x - 60, 200, x + 60, 320), fill=GOLD if i == 1 else CREAM)
            d.chord((x - 100, 340, x + 100, 620), 180, 360, fill=GOLD if i == 1 else CREAM, outline=DARK, width=LW)
            line([(x - 100, 480), (x + 100, 480)], w=LW)
        if label: txt((420, 640), label, F("pf9", 110), RED)
    elif name == "bank":
        d.polygon([(420, 120), (130, 290), (710, 290)], fill=GOLD, outline=DARK); line([(420, 120), (130, 290), (710, 290), (420, 120)], w=LW)
        for i in range(4):
            x = 190 + i * 140; rr((x, 320, x + 60, 610), r=4)
        rr((140, 620, 700, 690), fill=DARK, r=6)
    elif name == "lock":
        d.arc((260, 120, 580, 440), 180, 360, fill=DARK, width=46)
        line([(283, 280), (283, 380)], w=46); line([(557, 280), (557, 380)], w=46)
        rr((200, 360, 640, 700), fill=GOLD, r=30); ell((390, 470, 450, 530), fill=DARK, w=4); line([(420, 510), (420, 600)], w=28)
    elif name == "euro":
        ell((150, 150, 690, 690), fill=GOLD, w=22); txt((420, 430), "€", F("pf9", 300), DARK)
    elif name == "phone":
        rr((260, 110, 580, 730), fill=DARK, r=50); rr((290, 170, 550, 660), fill=CREAM, r=14, w=6)
        txt((420, 230), label or "730", F("pf9", 80), RED)
        for i in range(5): line([(320, 300 + i * 60), (520 - (i % 2) * 70, 300 + i * 60)], col=GREY, w=10)
        ell((395, 680, 445, 715), fill=GREY, w=4)
    elif name == "screen":
        rr((130, 160, 710, 560), fill=DARK, r=20); rr((160, 190, 680, 530), fill=CREAM, r=8, w=6)
        txt((420, 260), label or "FATTURA", F("ss7", 60), TEAL)
        for i in range(3): line([(200, 340 + i * 55), (560 - i * 60, 340 + i * 55)], col=GREY, w=10)
        line([(380, 560), (340, 670)], w=20); line([(460, 560), (500, 670)], w=20); line([(290, 680), (550, 680)], w=24)
    elif name == "magnifier":
        ell((150, 130, 560, 540), fill=CREAM, w=34); line([(500, 480), (700, 690)], w=60)
        txt((355, 340), label or "?", F("pf9", 240), RED)
    elif name == "gamepad":
        d.rounded_rectangle((60, 250, 780, 650), radius=190, fill=DARK, outline=DARK, width=LW)
        rr((215, 340, 265, 560), fill=CREAM, r=10, w=0); rr((130, 425, 350, 475), fill=CREAM, r=10, w=0)
        for (cx, cy, col) in [(600, 360, RED), (680, 450, GOLD), (520, 450, TEAL), (600, 540, CREAM)]:
            d.ellipse((cx - 42, cy - 42, cx + 42, cy + 42), fill=col)
        if label: txt((420, 150), label, F("pf9", 150), RED)
    elif name == "car":
        d.polygon([(250, 360), (330, 250), (530, 250), (610, 360)], fill=TEAL, outline=DARK); line([(250, 360), (330, 250), (530, 250), (610, 360)], w=LW)
        rr((110, 350, 730, 520), fill=TEAL, r=60)
        rr((350, 275, 420, 350), fill=CREAM, r=8, w=10); rr((440, 275, 520, 350), fill=CREAM, r=8, w=10)
        for cx in (250, 590):
            ell((cx - 80, 450, cx + 80, 610), fill=DARK, w=8); ell((cx - 35, 495, cx + 35, 565), fill=GREY, w=6)
    elif name == "cambiale":
        rr((120, 230, 720, 560), fill=CREAM, r=8, w=14)
        txt((160, 280), label or "CAMBIALE", F("ss7", 40), RED, "lm")
        for i, w_ in enumerate([420, 480, 360]): line([(160, 350 + i * 55), (160 + w_, 350 + i * 55)], col=GREY, w=8)
        line([(470, 520), (530, 500), (580, 515), (660, 490)], w=8)
    elif name == "cart":
        line([(110, 200), (210, 200), (290, 560), (640, 560)], w=24)
        d.polygon([(230, 260), (700, 260), (650, 470), (270, 470)], fill=GOLD, outline=DARK); line([(230, 260), (700, 260), (650, 470), (270, 470), (230, 260)], w=LW)
        for x in (330, 580): ell((x - 45, 590, x + 45, 680), fill=DARK, w=6)
        for x in (360, 450, 540): line([(x, 280), (x - 10, 450)], w=8)
    elif name == "piggy":
        ell((160, 250, 660, 620), fill=(232, 170, 160))
        d.polygon([(250, 300), (300, 180), (360, 280)], fill=(232, 170, 160), outline=DARK); line([(250, 300), (300, 180), (360, 280)], w=14)
        rr((620, 380, 720, 480), fill=(232, 170, 160), r=30, w=14)
        ell((300, 340, 340, 380), fill=DARK, w=4); rr((360, 230, 470, 260), fill=DARK, r=6, w=2)
        for x in (260, 500): rr((x, 580, x + 70, 690), fill=(232, 170, 160), r=12, w=14)
    elif name == "calendar":
        rr((150, 170, 690, 700), r=24); rr((150, 170, 690, 300), fill=RED, r=24)
        line([(270, 120), (270, 220)], w=26); line([(570, 120), (570, 220)], w=26)
        txt((420, 500), label or "1°", F("pf9", 220), DARK)
    elif name == "bottle":
        rr((340, 110, 500, 200), fill=DARK, r=10, w=8)
        d.polygon([(360, 200), (480, 200), (560, 330), (560, 720), (280, 720), (280, 330)], fill=CREAM, outline=DARK); line([(360, 200), (480, 200), (560, 330), (560, 720), (280, 720), (280, 330), (360, 200)], w=LW)
        rr((280, 420, 560, 600), fill=TEAL, r=4, w=10); txt((420, 510), label or "1 L", F("ss7", 80), CREAM)
    elif name == "card":
        rr((120, 230, 720, 610), fill=TEAL, r=40); rr((120, 310, 720, 380), fill=DARK, r=0, w=0)
        rr((180, 440, 300, 530), fill=GOLD, r=12, w=10); line([(360, 530), (640, 530)], col=CREAM, w=14)
    elif name == "factory":
        d.polygon([(110, 700), (110, 380), (290, 480), (290, 380), (470, 480), (470, 380), (650, 480), (650, 700)], fill=GOLD, outline=DARK)
        line([(110, 700), (110, 380), (290, 480), (290, 380), (470, 480), (470, 380), (650, 480), (650, 700), (110, 700)], w=LW)
        rr((560, 150, 640, 470), fill=RED, r=6);
        for i in range(3): rr((170 + i * 160, 560, 250 + i * 160, 640), fill=CREAM, r=6, w=10)
    elif name == "oldman":
        ell((330, 120, 510, 300), fill=CREAM); d.chord((240, 330, 600, 800), 180, 360, fill=GOLD, outline=DARK, width=LW)
        line([(640, 360), (640, 700)], w=22); d.arc((590, 300, 690, 400), 180, 360, fill=DARK, width=22)
        txt((420, 650), label or "", F("pf9", 90), RED)
    elif name == "tv":
        rr((140, 220, 700, 640), fill=DARK, r=40); rr((190, 270, 560, 590), fill=CREAM, r=20, w=8)
        ell((600, 300, 650, 350), fill=GOLD, w=6); ell((600, 400, 650, 450), fill=GOLD, w=6)
        line([(330, 220), (250, 110)], w=12); line([(410, 220), (490, 110)], w=12)
        if label: txt((375, 430), label, F("pf9", 110), RED)
    else:
        ell((200, 200, 640, 640), fill=GOLD)
    return im

_IC = {}
def get_icon(n, size=420):
    if (n, size) not in _IC:
        _IC[(n, size)] = icon(n).resize((size, size), Image.LANCZOS)
    return _IC[(n, size)]

# ---------- testo ----------
def fit(d, text, fname, size, maxw, minsize=40):
    f = F(fname, size)
    while d.textlength(text, font=f) > maxw and size > minsize:
        size -= 4; f = F(fname, size)
    return f

def wrap(d, text, f, maxw):
    words = text.split(); lines = []; cur = ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=f) <= maxw or not cur: cur = t
        else: lines.append(cur); cur = w_
    lines.append(cur); return lines

# ---------- tempi delle parole ----------
def norm(w): return re.sub(r"[^\w%€]", "", w.lower())

def word_times(text, words):
    """Per ogni parola del testo, l'istante (s) in cui la voce la dice."""
    toks = text.split(); times = [None] * len(toks); j = 0
    for i, t in enumerate(toks):
        nt = norm(t)
        for k in range(j, min(j + 4, len(words))):
            if norm(words[k]["w"]) == nt or (nt and norm(words[k]["w"]).startswith(nt[:4])):
                times[i] = words[k]["t"]; j = k + 1; break
    end = (words[-1]["t"] + words[-1]["d"]) if words else 0.0
    known = [(i, t) for i, t in enumerate(times) if t is not None]
    for i in range(len(times)):
        if times[i] is None:
            prev = max([k for k in known if k[0] < i], default=(0, 0.0), key=lambda k: k[0])
            nxt = min([k for k in known if k[0] > i], default=(len(toks), end), key=lambda k: k[0])
            times[i] = prev[1] + (nxt[1] - prev[1]) * (i - prev[0]) / max(1, nxt[0] - prev[0])
    return toks, times

def caption_chunks(text, words, maxlen=40, minlen=14):
    toks, times = word_times(text, words)
    chunks = []; cur = []
    for i, t in enumerate(toks):
        cur.append(i)
        txt = " ".join(toks[k] for k in cur)
        if (t[-1] in ".:;?!" and len(txt) >= minlen) or (t[-1] == "," and len(txt) > 24) or len(txt) > maxlen:
            chunks.append(cur); cur = []
    if cur: chunks.append(cur)
    return [(times[c[0]], " ".join(toks[k] for k in c)) for c in chunks]

def cue_time(text, words, cue):
    """Istante in cui la voce dice la parola 'cue' (prima occorrenza)."""
    toks, times = word_times(text, words)
    nc = norm(cue)
    for t, w in zip(times, toks):
        if norm(w).startswith(nc[:5]): return t
    return None
