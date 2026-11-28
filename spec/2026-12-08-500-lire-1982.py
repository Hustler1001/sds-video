# Short serie "Quanto valgono oggi X lire?": la moneta da 500 lire del 1982 (acmonital e bronzital, autore Laura Cretara:
# Museo della Zecca di Roma, IPZS, scheda moneta 891). Istat FOI 1913=1 (nota 30/7/2026): 1982 = 2.233,849; 2025 = 9.286,869.
# Cambio fisso 1 euro = 1.936,27 lire. Claim "prima bimetallica al mondo" NON usato (non verificato su fonte primaria).
L = 1936.27
I82, I25 = 2233.849, 9286.869
assert round(500 / L, 2) == 0.26
assert round(500 * I25 / I82) == 2079
assert round(500 * I25 / I82 / L, 2) == 1.07
TITLE = "Le 500 lire del 1982, oggi"
UNDER = "500 lire"
YEAR = 1982
TIMELINE = (1900, 2026)
VOICE = "it-IT-ElsaNeural"
RATE = "+4%"
SCENES = [
    dict(kind="hero", icon="coin:500", big="26 centesimi?", sub1="Le 500 lire al cambio dell'euro",
         sub2="1 euro = 1.936,27 lire", src="Cambio fisso lira-euro", year=2002,
         text="26 centesimi. Tanto valevano le 500 lire quando sono arrivati gli euro. Ma la moneta da 500 lire del 1982 oggi varrebbe molto di più."),
    dict(kind="list", heading="La moneta del 1982", year=1982,
         items=[("Due metalli: acmonital e bronzital", "metalli"), ("Disegnata da Laura Cretara", "Cretara"),
                ("Peso: 6,73 grammi", "grammi")],
         src="Fonte: Museo della Zecca di Roma, IPZS",
         text="Era la moneta a due colori: dentro acmonital, fuori bronzital, due metalli. L'aveva disegnata Laura Cretara, e pesava 6,73 grammi."),
    dict(kind="hero", icon="chart", big="1,07 €", sub1="Le 500 lire del 1982 con l'inflazione",
         sub2="Cioè 2.079 lire di oggi", src="Fonte: Istat, indice FOI · Esempio calcolato", year=2025,
         text="Con l'inflazione misurata dall'Istat, 500 lire del 1982 oggi sono 2.079 lire: un euro e 7 centesimi. Il caffè al bar, più o meno."),
    dict(kind="end", big="Cosa compravi?", sub1="Con 500 lire nel 1982", sub2="Scrivilo nei commenti",
         text="E tu, con una moneta da 500 lire nel 1982, cosa compravi? Scrivilo nei commenti."),
]
PUBLISH = dict(
    title="La moneta da 500 lire del 1982: quanto vale oggi con l'inflazione?",
    paragraphs=[
        "Al cambio dell'euro 500 lire valevano 26 centesimi. Ma la moneta da 500 lire del 1982, quella a due colori in acmonital e bronzital disegnata da Laura Cretara, con l'inflazione oggi varrebbe circa 1,07 euro, cioè 2.079 lire.",
        "Esempio calcolato con gli indici Istat dei prezzi (FOI): 500 × 9.286,869 ÷ 2.233,849 = 2.079 lire del 2025, diviso 1.936,27 = 1,07 euro.",
        "Cosa compravi con una moneta da 500 lire nel 1982? Scrivilo nei commenti.",
        "Fonti: Museo della Zecca di Roma (IPZS), scheda della moneta da 500 lire 1982; Istat, «Il valore della moneta in Italia dal 1861 al 2025» (nota del 30 luglio 2026). Coefficienti per l'analisi storica, non valori ufficiali per rivalutazioni legali. Video a scopo informativo ed educativo.",
        "Voce e grafiche realizzate con strumenti di intelligenza artificiale.",
        "#500lire #lira #inflazione #storiadeisoldi",
    ],
)
