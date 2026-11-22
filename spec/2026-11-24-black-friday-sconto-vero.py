# Short TREND Black Friday (27/11/2026). 4,3 miliardi = stima Codacons (14/11/2026, ANSA), non un dato ufficiale.
# Regola: art. 17-bis Codice del consumo (introdotto dal D.Lgs. 7 marzo 2023 n. 26): prezzo precedente = il più basso dei 30 giorni prima.
# Esempio calcolato: 100 -> 130 -> "-30%" = 91,00 €; sconto vero sul prezzo di 30 giorni prima = 9% (assert nel controllo).
TITLE = "Black Friday: lo sconto è vero?"
UNDER = "vero?"
YEAR = 2026
TIMELINE = (1900, 2026)
VOICE = "it-IT-ElsaNeural"
RATE = "+4%"
SCENES = [
    dict(kind="hero", icon="cart", big="4,3 miliardi", sub1="Spesa stimata per il Black Friday",
         sub2="+7% sul 2025, venerdì 27 novembre", src="Stima Codacons, non un dato ufficiale", year=2026,
         text="4,3 miliardi di euro. È quanto spenderemo per il Black Friday, secondo una stima del Codacons. Ma quegli sconti sono veri? C'è una legge che lo dice."),
    dict(kind="list", heading="La regola dei 30 giorni", year=2023,
         items=[("Dal 2023 è legge (Codice del consumo)", "2023"),
                ("Lo sconto si calcola sul prezzo", "calcola"),
                ("più basso degli ultimi 30 giorni", "basso")],
         src="Fonte: art. 17-bis Codice del consumo, D.Lgs. 26/2023",
         text="Dal 2023 c'è una regola nel Codice del consumo. Quando un negozio annuncia uno sconto, lo deve calcolare sul prezzo più basso che ha fatto negli ultimi 30 giorni."),
    dict(kind="list", heading="Un esempio fatto i conti", year=2026,
         items=[("1° novembre: 100 €", "novembre"), ("20 novembre: sale a 130 €", "sale"),
                ("Black Friday: «-30%», 91 €", "scontato"), ("Sconto vero: solo 9%", "vero")],
         src="Esempio calcolato",
         text="Un esempio. Il primo novembre un prodotto costa 100 euro. Il 20 novembre sale a 130. Il giorno del Black Friday lo trovi scontato del 30 per cento, a 91 euro. "
              "Ma rispetto ai 100 euro di inizio mese lo sconto vero è solo del 9 per cento. E per legge il prezzo di partenza da mostrare è 100, non 130."),
    dict(kind="end", big="Quanto spendi?", sub1="Scrivi la cifra", sub2="Iscriviti: ogni giorno i soldi spiegati con i numeri",
         text="E tu, quanto pensi di spendere quest'anno al Black Friday? Scrivi la cifra nei commenti. E iscriviti: ogni giorno i soldi spiegati con i numeri."),
]
PUBLISH = dict(
    title="Black Friday 2026: lo sconto è vero? La regola dei 30 giorni",
    paragraphs=[
        "Per il Black Friday 2026 (venerdì 27 novembre) il Codacons stima una spesa di circa 4,3 miliardi di euro, +7% sul 2025. È una stima, non un dato ufficiale.",
        "Dal 2023 il Codice del consumo dice che uno sconto va calcolato sul prezzo più basso applicato negli ultimi 30 giorni. Esempio calcolato: un prodotto a 100 euro il 1° novembre, alzato a 130 il 20 novembre e venduto a 91 euro «-30%» il giorno del Black Friday: lo sconto vero è del 9%, e il prezzo precedente da indicare è 100 euro.",
        "Quanto pensi di spendere quest'anno al Black Friday? Scrivi la cifra nei commenti.",
        "Fonti: art. 17-bis del Codice del consumo (D.Lgs. 206/2005), introdotto dal D.Lgs. 7 marzo 2023, n. 26 (Normattiva); stima Codacons del 14 novembre 2026 (ANSA). Video a scopo informativo, non è consulenza legale.",
        "Voce e grafiche realizzate con strumenti di intelligenza artificiale.",
        "#blackfriday #sconti #risparmio #storiadeisoldi",
    ],
)
