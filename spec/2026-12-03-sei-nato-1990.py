# Short serie "Sei nato nel 19XX?" (3/12/2026), anno 1990, prodotti diversi dagli short 1960/1970/1980 dove possibile.
# Fonte: Istat, Sommario di statistiche storiche, cap. 21 Prezzi, Tavola 21.3 "Prezzi medi al consumo di alcuni prodotti del comparto
# alimentare - Anni 1861-2010", euro correnti (controllo: 1960 latte 0,04338 x 1.936,27 = 84 lire, burro 1.199, caffè 2.104: coincidono).
# 1990 (euro): pane kg 1,18837 -> 2.301 lire; pasta kg 1,13104 -> 2.190; carne bovina kg 8,49675 -> 16.452; caffè tostato kg 7,19063 -> 13.923;
# olio extra vergine litro 3,29345 -> 6.377. Coefficiente Istat 1990 in valori 2025: 2,285 -> carne 19,42 euro di oggi.
TITLE = "Sei nato nel 1990? Ecco i prezzi"
UNDER = "1990?"
YEAR = 1990
TIMELINE = (1900, 2026)
VOICE = "it-IT-ElsaNeural"
RATE = "+4%"
SCENES = [
    dict(kind="list", heading="La spesa del 1990, in lire", year=1990,
         items=[("Pane, 1 chilo: 2.301 lire", "pane"), ("Pasta, 1 chilo: 2.190 lire", "pasta"),
                ("Olio extravergine, 1 litro: 6.377 lire", "olio"), ("Caffè, 1 chilo: 13.923 lire", "caffè")],
         src="Fonte: Istat, prezzi medi al consumo (serie storiche)",
         text="2.301 lire per un chilo di pane. Era il 1990, l'anno dei Mondiali in Italia. Un chilo di pasta costava 2.190 lire, un litro di olio extravergine 6.377, e un chilo di caffè 13.923 lire."),
    dict(kind="hero", icon="cart", big="16.452 lire", sub1="Un chilo di carne di manzo nel 1990",
         sub2="Con l'inflazione: 19,42 € di oggi", src="Istat · Esempio calcolato con i coefficienti di rivalutazione", year=1990,
         text="E la carne di manzo? 16.452 lire al chilo. Con l'inflazione, secondo i coefficienti Istat, sono 19 euro e 42 di oggi."),
    dict(kind="end", big="Sei del 1990?", sub1="Cosa costava di più?", sub2="Scrivi il tuo anno: faccio il prossimo",
         text="Sei del 1990? Scrivi nei commenti cosa ti ricordi che costava di più. E il tuo anno di nascita: il prossimo video lo faccio su quello."),
]
PUBLISH = dict(
    title="1990: il pane a 2.301 lire al chilo. Sei nato quell'anno?",
    paragraphs=[
        "Nel 1990, l'anno dei Mondiali in Italia, un chilo di pane costava in media 2.301 lire, un chilo di pasta 2.190, un litro di olio extravergine 6.377, un chilo di caffè 13.923 e un chilo di carne di manzo 16.452 lire.",
        "Esempio calcolato con i coefficienti di rivalutazione Istat: le 16.452 lire della carne valgono circa 19,42 euro di oggi.",
        "Sei del 1990? Cosa ti ricordi che costava di più? Scrivi nei commenti anche il tuo anno di nascita: il prossimo video lo faccio su quello.",
        "Fonti: Istat, Sommario di statistiche storiche, cap. 21 Prezzi (prezzi medi al consumo, convertiti in lire a 1.936,27); Istat, «Il valore della moneta in Italia dal 1861 al 2025».",
        "Voce e grafiche realizzate con strumenti di intelligenza artificiale.",
        "#1990 #lira #prezzi #storiadeisoldi",
    ],
)
