# Short TREND "vortice polare" (freddo e neve in arrivo, Google Trends Italia 23/11/2026) -> quanto costa scaldare casa col gas.
# Fonte primaria: ARERA, nota stampa 3/11/2026 "Nota CMEM vulnerabili gas ottobre 2026"
# (https://www.arera.it/fileadmin/allegati/com_stampa/26/26.11.03_Nota_CMEM_vulnerabili_gas_ottobre_2026.pdf):
# prezzo di riferimento per il nuovo cliente tipo (tutela della vulnerabilità) 176,80 centesimi/metro cubo (+9,1% su settembre);
# materia gas 97,06 + vendita 5,83; trasporto e contatore 27,25; oneri 4,98; imposte 41,68 (23,57%). Famiglia tipo: 1.100 m3/anno.
# Esempi calcolati (assert in sessione): 176,80 x 1.100 = 1.944,80 euro/anno; imposte 41,68 x 1.100 = 458,48 euro;
# in lire 1,768 x 1.936,27 = 3.423 lire al metro cubo.
TITLE = "Vortice polare: quanto costa il gas?"
UNDER = "gas?"
YEAR = 2026
TIMELINE = (1900, 2026)
VOICE = "it-IT-ElsaNeural"
RATE = "+6%"
SCENES = [
    dict(kind="hero", icon="house", big="1,77 €", sub1="Un metro cubo di gas",
         sub2="Tasse comprese · ottobre 2026, famiglia tipo", src="Fonte: ARERA, nota del 3 novembre 2026",
         text="1 euro e 77. Con il vortice polare arriva il freddo, e questo è il prezzo di un metro cubo di gas per la famiglia tipo, tasse comprese. Dati ARERA: più 9,1% in un mese."),
    dict(kind="list", heading="Dove va il tuo euro e 77",
         items=[("Il gas: 1,03 €", "gas"), ("Tasse: 42 centesimi", "tasse"),
                ("Trasporto e contatore: 27 centesimi", "trasporto"), ("Oneri di sistema: 5 centesimi", "oneri")],
         src="Fonte: ARERA · cifre per metro cubo, ottobre 2026",
         text="Dove vanno? Il gas, con la vendita, costa 1 euro e 3 centesimi. Poi ci sono le tasse, 42 centesimi: quasi un quarto della bolletta. Il trasporto e il contatore, 27 centesimi. E gli oneri di sistema, 5 centesimi."),
    dict(kind="hero", icon="receipt", big="1.945 €", sub1="1.100 metri cubi in un anno",
         sub2="Di cui 458 € di tasse · in lire, 3.423 al metro cubo", src="Esempio calcolato su dati ARERA, prezzo di ottobre",
         text="La famiglia tipo consuma 1.100 metri cubi all'anno. Se il prezzo restasse quello di ottobre, sarebbero circa 1.945 euro. Di questi, 458 sono tasse. In lire, ogni metro cubo costerebbe 3.423 lire."),
    dict(kind="end", big="E tu?", sub1="Quanto hai pagato l'ultima bolletta?", sub2="Iscriviti: ogni giorno i soldi spiegati con i numeri",
         text="E tu, quanto hai pagato l'ultima bolletta del gas d'inverno? Scrivi la cifra nei commenti, e iscriviti."),
]
PUBLISH = dict(
    title="Vortice polare: quanto costa scaldare casa? Il gas a 1,77 euro al metro cubo",
    paragraphs=[
        "Vortice polare e freddo in arrivo: quanto costa scaldarsi con il gas? Secondo l'ARERA, a ottobre 2026 il prezzo di riferimento per la famiglia tipo nel servizio di tutela della vulnerabilità è di 176,80 centesimi di euro per metro cubo, tasse comprese: +9,1% rispetto a settembre.",
        "Per ogni metro cubo: 97,06 centesimi per il gas e 5,83 per la vendita, 27,25 per trasporto e contatore, 4,98 di oneri di sistema e 41,68 di imposte (il 23,57% della bolletta). Esempio calcolato: con i 1.100 metri cubi all'anno della famiglia tipo e il prezzo di ottobre fermo per 12 mesi, la spesa sarebbe di circa 1.945 euro, di cui 458 di imposte. Il prezzo cambia ogni mese e varia con le offerte del mercato libero.",
        "Quanto hai pagato l'ultima bolletta del gas d'inverno? Scrivi la cifra e la tua regione nei commenti.",
        "Fonte: ARERA, nota stampa del 3 novembre 2026 sul servizio di tutela della vulnerabilità gas (ottobre 2026). Video a scopo informativo ed educativo, non è consulenza.",
        "Voce e grafiche realizzate con strumenti di intelligenza artificiale.",
        "#vorticepolare #bollette #gas #storiadeisoldi",
    ],
)
