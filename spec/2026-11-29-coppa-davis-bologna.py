# Short TREND "Coppa Davis" (Google Trends Italia 27-28/11/2026: "tennis coppa davis" 100K+, "mensik", "supertennis streaming").
# Fatti: Italia-Repubblica Ceca 2-1 al doppio decisivo il 27/11/2026 a Bologna (Sky Sport, RTL 102.5): quarta finale di fila, domenica 29/11
# contro Spagna o Gran Bretagna. Titoli: 1976, 2023, 2024, 2025 (sportefinanza, money.it).
# Impatto economico edizione 2025 a Bologna: 143,8 milioni di euro STIMATI (Federtennis FITP, conferenza stampa di A. Binaghi 23/11/2025, LaPresse):
# 64,8 diretti + 55,2 indiretti + 23,8 indotti. E' una stima della federazione: lo diciamo a voce e a schermo.
# Montepremi 2026 (1,5 milioni $ al vincitore secondo la stampa) NON usato: nessuna fonte ITF primaria letta.
L = 1936.27
assert round(64.8 + 55.2 + 23.8, 1) == 143.8
assert round(143.8e6 * L / 1e9, 1) == 278.4   # miliardi di lire, cambio fisso
TITLE = "Coppa Davis: quanto vale per Bologna?"
UNDER = "Coppa Davis"
YEAR = 2025
TIMELINE = (1900, 2026)
VOICE = "it-IT-ElsaNeural"
RATE = "+6%"
SCENES = [
    dict(kind="hero", icon="chart", big="143,8 mln €", sub1="L'effetto della Davis 2025 a Bologna",
         sub2="Stima della Federtennis, non un conto ufficiale", src="Fonte: FITP, conferenza stampa 23/11/2025 · stima", year=2025,
         text="143 milioni e 800 mila euro. È quanto avrebbe portato a Bologna la Coppa Davis dell'anno scorso, secondo una stima della Federtennis. Oggi l'Italia gioca la quarta finale di fila."),
    dict(kind="list", heading="Da dove arrivano i 143,8 milioni", year=2025,
         items=[("Spesa diretta: 64,8 milioni", "diretta"), ("Effetto sui fornitori: 55,2 milioni", "fornitori"),
                ("Stipendi spesi in città: 23,8 milioni", "stipendi"), ("In lire: 278 miliardi", "lire")],
         src="Fonte: stima FITP · in lire: esempio calcolato al cambio 1.936,27",
         text="64,8 milioni di spesa diretta: biglietti, alberghi, ristoranti. 55,2 milioni di effetto sui fornitori. E 23,8 milioni di stipendi spesi in città. In lire, sarebbero 278 miliardi."),
    dict(kind="hero", icon="calendar", big="1976", sub1="La prima Coppa Davis dell'Italia",
         sub2="Poi 2023, 2024, 2025: oggi si gioca per la quinta", src="Italia-Repubblica Ceca 2-1 · semifinale del 27/11/2026", year=1976,
         text="La prima Coppa Davis l'Italia l'ha vinta nel 1976. Poi ne sono arrivate tre di fila: 2023, 2024 e 2025. Venerdì la Repubblica Ceca è caduta 2 a 1, al doppio decisivo."),
    dict(kind="end", big="2-0 o 2-1?", sub1="Scrivi il tuo pronostico per la finale", sub2="Iscriviti: ogni giorno una notizia spiegata con i numeri",
         text="E tu come la vedi la finale: 2 a 0 o 2 a 1? Scrivi il tuo pronostico nei commenti, e iscriviti."),
]
PUBLISH = dict(
    title="Coppa Davis 2026: quanto vale la finale per Bologna? 143,8 milioni (stima)",
    paragraphs=[
        "Coppa Davis: secondo una stima della Federtennis, l'edizione 2025 delle Finals ha portato a Bologna un impatto economico di 143,8 milioni di euro: 64,8 milioni di spesa diretta, 55,2 di effetto indiretto sui fornitori e 23,8 di effetto indotto. Al cambio fisso sono circa 278 miliardi di lire (esempio calcolato).",
        "Oggi, domenica 29 novembre 2026, l'Italia gioca a Bologna la quarta finale consecutiva, dopo il 2-1 alla Repubblica Ceca deciso dal doppio. In bacheca ci sono le Coppe del 1976, 2023, 2024 e 2025.",
        "Il tuo pronostico per la finale: 2-0 o 2-1? Scrivilo nei commenti.",
        "Fonti: FITP, conferenza stampa del presidente Angelo Binaghi del 23/11/2025 (stima dell'impatto economico, riportata da LaPresse); Sky Sport e RTL 102.5 per la semifinale del 27/11/2026. La cifra di 143,8 milioni è una stima della federazione, non un dato ufficiale di contabilità pubblica. Video a scopo informativo ed educativo.",
        "Voce e grafiche realizzate con strumenti di intelligenza artificiale.",
        "#coppadavis #tennis #bologna #storiadeisoldi",
    ],
)
