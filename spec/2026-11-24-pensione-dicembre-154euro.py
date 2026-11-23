# Short TREND "pensione di dicembre / tredicesima" (24/11/2026).
# Fonti: INPS scheda "Importo aggiuntivo delle pensioni" (agg. 16/04/2026): 154,94 euro, art. 70 L. 388/2000, d'ufficio a dicembre;
# limiti 2026 (su tasso previsionale 1,4%): pensione annua tra 7.954,05 e 8.108,99 euro, reddito personale fino a 11.931,08, coniugi 23.862,15.
# INPS circolare 69 del 21/3/2001: "importo aggiuntivo di lire 300.000 ex articolo 70, comma 7, legge n. 388/2000", con la tredicesima 2001.
# INPS notizia 15/12/2025: "Oltre 400mila pensionati" lo hanno ricevuto nel 2025.
# Calcolo: 300.000 / 1.936,27 = 154,94 euro. Istat FOI (Nota "Il valore della moneta 1861-2025"): indice 2001 = 5.987,782, 2025 = 9.286,869
# -> coefficiente 1,551 -> 300.000 lire 2001 = 240,30 euro del 2025; perdita di potere d'acquisto 35,5% (assert nel calcolo di sessione).
TITLE = "Pensione di dicembre: perché 154,94 euro?"
UNDER = "154,94"
YEAR = 2001
TIMELINE = (1900, 2026)
VOICE = "it-IT-ElsaNeural"
RATE = "+4%"
SCENES = [
    dict(kind="hero", icon="envelope", big="154,94 €", sub1="L'extra di dicembre in pensione",
         sub2="Una cifra strana. Da dove viene?", src="Fonte: INPS, importo aggiuntivo delle pensioni", year=2026,
         text="154 euro e 94 centesimi. È l'extra che a dicembre arriva insieme alla pensione, a chi prende il minimo. Ma perché proprio questa cifra così strana?"),
    dict(kind="list", heading="La risposta è in lire", year=2001,
         items=[("Legge finanziaria 2001: 300.000 lire", "300.000"), ("300.000 ÷ 1.936,27 = 154,94 €", "diviso"),
                ("Da allora: mai cambiato", "cambiato")],
         src="Fonte: INPS, circolare 69/2001 · art. 70 legge 388/2000",
         text="La risposta è in lire. La legge finanziaria del 2001 lo fissò a 300.000 lire. Diviso 1.936,27, il cambio dell'euro, fa esattamente 154,94. E da allora non è mai cambiato."),
    dict(kind="hero", icon="chart", big="240 €", sub1="300.000 lire del 2001, oggi",
         sub2="Il bonus ha perso il 35% del suo valore", src="Istat, coefficienti di rivalutazione · Esempio calcolato", year=2025,
         text="Ma con l'inflazione, 300.000 lire del 2001 oggi valgono circa 240 euro, secondo i coefficienti Istat. Il bonus è rimasto fermo, e ha perso più di un terzo del suo valore."),
    dict(kind="end", big="Nel 2001?", sub1="Quante lire di pensione?", sub2="Iscriviti: ogni giorno i soldi spiegati con i numeri",
         text="Nel 2001 la pensione dei tuoi genitori quante lire era? Scrivilo nei commenti, e iscriviti."),
]
PUBLISH = dict(
    title="Pensione di dicembre: perché il bonus è 154,94 euro? Erano 300.000 lire",
    paragraphs=[
        "Pensione di dicembre: con la tredicesima, chi prende una pensione vicina al minimo riceve un importo aggiuntivo di 154,94 euro. Una cifra strana, che viene dalle lire: la legge finanziaria 2001 (art. 70 della legge 388/2000) lo fissò a 300.000 lire, cioè 154,94 euro al cambio di 1.936,27. Da allora non è mai cambiato.",
        "Esempio calcolato con i coefficienti Istat: 300.000 lire del 2001 valgono oggi circa 240 euro. Il bonus ha perso circa il 35% del suo valore. Nel 2026 spetta, secondo l'INPS, con pensione annua tra 7.954,05 e 8.108,99 euro e reddito fino a 11.931,08 euro (23.862,15 in coppia); limiti calcolati dall'INPS su un tasso previsionale. Nel 2025 lo hanno ricevuto oltre 400.000 pensionati.",
        "Nel 2001 la pensione dei tuoi genitori quante lire era? Scrivi la cifra nei commenti.",
        "Fonti: INPS, scheda «Importo aggiuntivo delle pensioni»; INPS, circolare n. 69 del 21 marzo 2001; INPS, notizia del 15 dicembre 2025; Istat, «Il valore della moneta in Italia dal 1861 al 2025». Video a scopo informativo, non è consulenza previdenziale: per la tua situazione rivolgiti all'INPS o a un patronato.",
        "Voce e grafiche realizzate con strumenti di intelligenza artificiale.",
        "#pensioni #tredicesima #lira #storiadeisoldi",
    ],
)
