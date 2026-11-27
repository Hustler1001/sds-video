# Short TREND "revisione" (Google Trends Italia, 26-27/11/2026: n. 1 con 20.000+ ricerche; notizie su tariffe 2027 e proposta UE per auto oltre 10 anni).
# Fonti primarie: D.M. 2 agosto 2007 n. 161, art. 2 c. 1 (tariffa 45,00 euro); D.M. 3 agosto 2021 n. 129 (G.U. 24/9/2021 n. 229):
# tariffa 54,95 euro dal 1/11/2021 (+9,95 euro, art. 1 c. 705 L. 178/2020). Totale 79,02 euro IVA e diritti compresi nei centri privati
# (Altroconsumo 7/11/2025, alVolante 23/11/2026, La Nuova Sardegna 25/11/2026: fonti giornalistiche concordi).
# Ipotesi 2027 circa 90 euro: NON approvata (OdG accettato il 5/11/2026, decreto MIT-MEF non concluso; alVolante, newsauto).
# Istat, Il valore della moneta 1861-2025 (FOI base 1913=1): 2007 = 6.762,916; 2021 = 7.971,102; 2025 = 9.286,869.
# Esempi calcolati (assert in sessione): 45 x 9286,869/6762,916 = 61,79 euro; 45 euro = 87.132 lire; +22,1% tariffa contro +37,3% prezzi.
TITLE = "Revisione auto: quanto costa davvero?"
UNDER = "Revisione"
YEAR = 2026
TIMELINE = (1900, 2026)
VOICE = "it-IT-ElsaNeural"
RATE = "+8%"
SCENES = [
    dict(kind="hero", icon="car", big="79,02 €", sub1="La revisione in officina",
         sub2="IVA e diritti compresi · tariffa base 54,95 €", src="Fonte: D.M. 3 agosto 2021 n. 129 · Altroconsumo", year=2026,
         text="79 euro e 2 centesimi. È quanto paghi oggi la revisione dell'auto in officina, con IVA e diritti. E dal 2027 potrebbe costare di più."),
    dict(kind="list", heading="La tariffa base nel tempo", year=2021,
         items=[("2007: 45 € (87.132 lire)", "2007"), ("2021: 54,95 €, cioè +22%", "2021"),
                ("Prezzi 2007-2025: +37%", "prezzi"), ("45 € del 2007 oggi: 61,79 €", "61")],
         src="Fonti: D.M. 161/2007 e 129/2021 · Istat · Esempio calcolato",
         text="Nel 2007 la tariffa base era 45 euro, cioè 87.132 lire. Nel 2021 è salita a 54,95 euro: più 22 per cento. Ma i prezzi, dice l'Istat, sono saliti del 37 per cento. Con l'inflazione, quei 45 euro oggi sarebbero 61 euro e 79."),
    dict(kind="hero", icon="calendar", big="90 €?", sub1="L'ipotesi per il 2027",
         sub2="Non ancora approvata: manca il decreto", src="Fonte: alVolante, 23/11/2026 · ipotesi, non legge", year=2026,
         text="Per il 2027 si parla di circa 90 euro in tutto. Ma è un'ipotesi: il decreto non c'è ancora. E la revisione ogni anno per le auto con più di dieci anni? È solo una proposta europea."),
    dict(kind="end", big="E tu?", sub1="Quanto hai pagato l'ultima revisione?", sub2="Iscriviti: ogni giorno un prezzo spiegato con i numeri",
         text="E tu, quanto hai pagato l'ultima revisione? Scrivilo nei commenti, e iscriviti."),
]
PUBLISH = dict(
    title="Revisione auto: 79,02 euro oggi, 90 nel 2027? Con l'inflazione dovrebbe costare di più",
    paragraphs=[
        "Revisione auto: oggi in un centro privato costa 79,02 euro, IVA e diritti compresi. La tariffa base è 54,95 euro dal 1° novembre 2021 (D.M. 3 agosto 2021 n. 129); prima era 45 euro, fissata dal D.M. 2 agosto 2007 n. 161, cioè 87.132 lire.",
        "Dal 2007 la tariffa base è salita del 22%, mentre i prezzi al consumo sono saliti del 37% (Istat, indice FOI 2007-2025). Esempio calcolato: 45 euro del 2007 corrispondono a circa 61,79 euro del 2025.",
        "Per il 2027 si parla di un totale di circa 90 euro: è un'ipotesi, non un aumento approvato (il decreto interministeriale MIT-MEF non è ancora concluso). La revisione annuale per le auto con più di 10 anni è una proposta della Commissione europea in discussione: per ora in Italia restano la prima revisione dopo 4 anni e poi ogni 2.",
        "Quanto hai pagato la tua ultima revisione, e in che anno? Scrivilo nei commenti.",
        "Fonti: D.M. 2 agosto 2007 n. 161; D.M. 3 agosto 2021 n. 129 (G.U. n. 229 del 24/9/2021); L. 178/2020, art. 1 c. 705; Istat, «Il valore della moneta in Italia dal 1861 al 2025»; Altroconsumo (7/11/2025) e alVolante (23/11/2026) per il totale e l'ipotesi 2027. Video a scopo informativo ed educativo.",
        "Voce e grafiche realizzate con strumenti di intelligenza artificiale.",
        "#revisione #revisioneauto #auto #storiadeisoldi",
    ],
)
