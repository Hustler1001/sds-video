# Serie "Quanto valgono oggi X lire?" (foglio Idee, In corso). Diversa dai video "mille lire" (1960-2001).
# Fonte: Istat, «Il valore della moneta in Italia dal 1861 al 2025» (nota 30/7/2026), Prospetto 1, FOI base 1913=1:
# 1955 = 259,472; 2001 = 5.987,782; 2025 = 9.286,869. Cambio fisso 1 euro = 1.936,27 lire.
# Esempi calcolati (assert in sessione): 9.286,869 / 1.936,27 = 4,796 euro -> 4,80 euro; 2001->2025 x1,551.
TITLE = "Una lira del 1913, oggi"
UNDER = "1913"
YEAR = 1913
TIMELINE = (1900, 2026)
VOICE = "it-IT-ElsaNeural"
RATE = "+4%"
SCENES = [
    dict(kind="hero", icon="coin", big="4,80 €", sub1="Quanto vale oggi una lira del 1913",
         sub2="Con l'inflazione misurata dall'Istat", src="Fonte: Istat, il valore della moneta 1861-2025 · Esempio calcolato", year=1913,
         text="4 euro e 80. È quanto vale oggi una sola lira del 1913, l'ultimo anno prima della Grande Guerra. Lo dicono gli indici dei prezzi dell'Istat."),
    dict(kind="list", heading="Ciò che costava 1 lira nel 1913", year=2025,
         items=[("Nel 1955: 259 lire", "1955"), ("Nel 2001: 5.988 lire", "2001"),
                ("Nel 2025: 9.287 lire", "2025"), ("Cioè 4,80 euro", "euro")],
         src="Fonte: Istat, indice dei prezzi FOI, 1913 = 1",
         text="Quello che nel 1913 costava una lira, nel 1955 costava 259 lire. Nel 2001, l'ultimo anno della lira, 5.988 lire. E nel 2025, 9.287 lire: cioè 4 euro e 80."),
    dict(kind="hero", icon="chart", big="+55%", sub1="I prezzi dal 2001 al 2025",
         sub2="La lira è sparita, l'inflazione no", src="Fonte: Istat · Esempio calcolato", year=2025,
         text="E solo dall'addio alla lira, nel 2001, al 2025, i prezzi sono saliti del 55 per cento. La moneta è cambiata, l'inflazione è rimasta."),
    dict(kind="end", big="Il prezzo più vecchio", sub1="che ti ricordi in lire?", sub2="Iscriviti: ogni giorno un prezzo di una volta",
         text="Qual è il prezzo più vecchio che ti ricordi in lire? Scrivi la cosa, l'anno e il prezzo nei commenti. E iscriviti: ogni giorno un prezzo di una volta."),
]
PUBLISH = dict(
    title="Quanto vale oggi una lira del 1913? 4,80 euro: i conti con l'inflazione Istat",
    paragraphs=[
        "Una lira del 1913 oggi vale circa 4,80 euro. Secondo gli indici dei prezzi dell'Istat (FOI, base 1913 = 1), quello che nel 1913 costava una lira nel 1955 costava 259 lire, nel 2001 5.988 lire e nel 2025 9.287 lire.",
        "Esempio calcolato: 9.287 lire diviso 1.936,27 (il cambio fisso lira-euro) fa 4,80 euro. E dal 2001 al 2025 i prezzi sono saliti di circa il 55%. Sono coefficienti per l'analisi storica, non valori ufficiali per rivalutazioni legali.",
        "Qual è il prezzo più vecchio che ti ricordi in lire? Scrivi la cosa, l'anno e il prezzo nei commenti.",
        "Fonte: Istat, «Il valore della moneta in Italia dal 1861 al 2025», nota informativa del 30 luglio 2026. Video a scopo informativo ed educativo.",
        "Voce e grafiche realizzate con strumenti di intelligenza artificiale.",
        "#lira #inflazione #storiadeisoldi",
    ],
)
