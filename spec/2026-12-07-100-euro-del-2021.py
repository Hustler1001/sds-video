# Short: "100 euro del 2021 oggi" (inflazione recente, serie "Quanto valgono oggi").
# Istat, «Il valore della moneta in Italia dal 1861 al 2025» (nota 30/7/2026), Prospetto 1, FOI 1913=1:
# 2021 = 7.971,102; 2022 = 8.613,686; 2023 = 9.080,324; 2024 = 9.156,822; 2025 = 9.286,869 (medie annue).
I = {2021: 7971.102, 2022: 8613.686, 2023: 9080.324, 2024: 9156.822, 2025: 9286.869}
assert round(100 * I[2021] / I[2025], 2) == 85.83
assert round((I[2025] / I[2021] - 1) * 100, 1) == 16.5
assert [round((I[y] / I[y - 1] - 1) * 100, 1) for y in (2022, 2023, 2024, 2025)] == [8.1, 5.4, 0.8, 1.4]
TITLE = "100 euro del 2021, oggi"
UNDER = "2021"
YEAR = 2021
TIMELINE = (1900, 2026)
VOICE = "it-IT-ElsaNeural"
RATE = "+4%"
SCENES = [
    dict(kind="hero", icon="piggy", big="85,83 €", sub1="Il valore oggi di 100 € del 2021",
         sub2="I prezzi sono saliti del 16,5% in 4 anni", src="Fonte: Istat, indice FOI · Esempio calcolato", year=2021,
         text="85 euro e 83. È quello che comprano oggi 100 euro del 2021. In quattro anni, secondo l'Istat, i prezzi sono saliti del 16 e mezzo per cento."),
    dict(kind="list", heading="Anno per anno, i prezzi", year=2025,
         items=[("2022: +8,1%", "2022"), ("2023: +5,4%", "2023"), ("2024: +0,8%", "2024"), ("2025: +1,4%", "2025")],
         src="Fonte: Istat, indice FOI, medie annue",
         text="Nel 2022 più 8,1 per cento, il colpo più forte. Nel 2023 più 5,4. Poi la frenata: nel 2024 più 0,8, e nel 2025 più 1,4. Ma i prezzi saliti non tornano indietro."),
    dict(kind="hero", icon="receipt", big="1.165 €", sub1="Uno stipendio di 1.000 € del 2021",
         sub2="Dovrebbe essere così oggi, solo per restare pari", src="Esempio calcolato con l'indice Istat FOI", year=2025,
         text="Per comprare le stesse cose, uno stipendio di 1.000 euro del 2021 oggi dovrebbe essere di 1.165 euro."),
    dict(kind="end", big="E il tuo?", sub1="Di quanto è salito il tuo stipendio dal 2021?", sub2="Scrivi la percentuale nei commenti",
         text="E il tuo stipendio, o la tua pensione, di quanto è salito dal 2021? Scrivi la percentuale nei commenti."),
]
PUBLISH = dict(
    title="100 euro del 2021 oggi valgono 85,83 euro: l'inflazione anno per anno",
    paragraphs=[
        "100 euro del 2021 oggi comprano quanto 85,83 euro di allora. Secondo l'indice dei prezzi Istat per le famiglie di operai e impiegati (FOI), dal 2021 al 2025 i prezzi sono saliti del 16,5%.",
        "Anno per anno: +8,1% nel 2022, +5,4% nel 2023, +0,8% nel 2024, +1,4% nel 2025 (medie annue). Esempio calcolato: per restare pari, uno stipendio di 1.000 euro del 2021 dovrebbe essere oggi di circa 1.165 euro.",
        "Di quanto è salito il tuo stipendio, o la tua pensione, dal 2021? Scrivi la percentuale nei commenti.",
        "Fonte: Istat, «Il valore della moneta in Italia dal 1861 al 2025» (nota informativa del 30 luglio 2026), indici FOI. Sono valori per l'analisi storica, non coefficienti ufficiali per rivalutazioni legali. Video a scopo informativo ed educativo.",
        "Voce e grafiche realizzate con strumenti di intelligenza artificiale.",
        "#inflazione #prezzi #stipendi #storiadeisoldi",
    ],
)
