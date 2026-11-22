# Short serie "Quanto valgono oggi X lire?". Istat, coefficienti annuali FOI 1861-2025 (valori del 2025), diviso 1936,27.
# 1960: 31,225 -> 16,13 €; 1970: 21,338 -> 11,02 €; 1980: 5,741 -> 2,96 €; 1990: 2,285 -> 1,18 €; 2001: 1,551 -> 0,80 €.
TITLE = "Quanto valgono 1.000 lire?"
UNDER = "1.000 lire"
YEAR = 1960
TIMELINE = (1900, 2026)
VOICE = "it-IT-ElsaNeural"
RATE = "+4%"
SCENES = [
    dict(kind="list", heading="1.000 lire, in euro di oggi", year=1960,
         items=[("1960: 16,13 €", "1960"), ("1970: 11,02 €", "1970"), ("1980: 2,96 €", "1980"),
                ("1990: 1,18 €", "1990"), ("2001: 0,80 €", "2001")],
         src="Fonte: Istat, coefficienti di rivalutazione (valori 2025)",
         text="Mille lire del 1960 valgono oggi 16 euro e 13 centesimi. Mille lire del 1970, 11 euro. Mille lire del 1980, appena 2,96. "
              "Mille lire del 1990, 1 euro e 18. E le mille lire del 2001, l'ultimo anno della lira, 80 centesimi."),
    dict(kind="hero", icon="coin:1000", big="-73%", sub1="Il valore perso tra il 1970 e il 1980",
         sub2="Inflazione a due cifre per anni", src="Esempio calcolato su dati Istat", year=1980,
         text="Il colpo più duro arrivò negli anni Settanta. Tra il 1970 e il 1980 mille lire persero il 73 per cento del loro valore: per gran parte del decennio l'inflazione fu a due cifre."),
    dict(kind="end", big="Il tuo primo stipendio?", sub1="Quante lire?", sub2="Scrivi anno e cifra: te lo converto in euro di oggi",
         text="E il tuo primo stipendio, quante lire era? Scrivi l'anno e la cifra nei commenti: te lo converto in euro di oggi."),
]
PUBLISH = dict(
    title="Quanto valgono oggi 1.000 lire? Dal 1960 al 2001, in euro",
    paragraphs=[
        "Mille lire del 1960 valgono oggi circa 16,13 euro. Quelle del 1970 11,02 euro, del 1980 2,96 euro, del 1990 1,18 euro e quelle del 2001 appena 0,80 euro.",
        "Il colpo più duro negli anni Settanta: tra il 1970 e il 1980 mille lire hanno perso il 73% del loro potere d'acquisto.",
        "Il tuo primo stipendio quante lire era? Scrivi anno e cifra nei commenti: te lo convertiamo in euro di oggi.",
        "Fonte: Istat, «Il valore della moneta in Italia dal 1861 al 2025», coefficienti annuali FOI per tradurre valori del passato in valori del 2025. Calcolo: 1.000 lire × coefficiente ÷ 1.936,27.",
        "Voce e grafiche realizzate con strumenti di intelligenza artificiale.",
        "#lira #inflazione #storiadeisoldi",
    ],
)
