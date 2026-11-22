# ESEMPIO di spec per uno short (ricostruisce lo short "Nato nel 1960? Ecco i prezzi", già pubblicato).
# Copialo in spec/AAAA-MM-GG-nome.py e cambia testi e dati. Ogni cifra va verificata su fonte primaria.
TITLE = "Nato nel 1960? Ecco i prezzi"   # titolo in alto (max 2 righe)
UNDER = "1960?"                          # parola del titolo sottolineata in rosso ("" per nessuna)
YEAR = 1960                              # anno sulla linea del tempo (ogni scena può avere year=...)
TIMELINE = (1900, 2026)
RATE = "+4%"                             # velocità della voce (short: da +0% a +8%)

SCENES = [
    # kind="hero": icona + parola grande rossa + due righe + fonte
    dict(kind="hero", icon="coin:5", big="1960", sub1="Quanto costava la spesa",
         sub2="Prezzi medi in Italia, in lire", src="Fonte: Istat, serie storiche dei prezzi",
         text="Sei nato nel 1960? Ecco quanto costava la spesa quell'anno. In lire."),
    # kind="list": titoletto + elenco numerato; ogni voce compare quando la voce dice la parola indicata
    dict(kind="list", heading="La spesa del 1960",
         items=[("Latte, 1 litro: 84 lire", "latte"), ("Vino, 1 litro: 123 lire", "vino"),
                ("Zucchero, 1 chilo: 233 lire", "zucchero"), ("Burro, 1 chilo: 1.199 lire", "burro"),
                ("Caffè, 1 chilo: 2.104 lire", "caffè")],
         text="Un litro di latte costava 84 lire. Un litro di vino, 123 lire. Un chilo di zucchero, 233 lire. "
              "Un chilo di burro, 1.199 lire. E un chilo di caffè, 2.104 lire."),
    # kind="end": cartello scuro finale con la domanda per i commenti
    dict(kind="end", big="Sei del 1960?", sub1="Metti like", sub2="Scrivi il tuo anno: faccio il prossimo",
         text="Sei del 1960? Metti like, e scrivi nei commenti il tuo anno di nascita: il prossimo video lo faccio su quello."),
]

# Testo per Posty (YouTube). Ogni paragrafo diventa un <p>.
PUBLISH = dict(
    title="Nato nel 1960? Ecco quanto costava la spesa in lire",
    paragraphs=[
        "Sei nato nel 1960? Quell'anno un litro di latte costava 84 lire, un litro di vino 123, un chilo di zucchero 233, un chilo di burro 1.199 e un chilo di caffè 2.104 lire.",
        "Sei del 1960? Metti like. E scrivi nei commenti il tuo anno di nascita: il prossimo video lo faccio su quello.",
        "Fonte: Istat, serie storiche dei prezzi (prezzi medi al consumo). Voce e grafiche realizzate con strumenti di intelligenza artificiale.",
        "#1960 #lira #storiadeisoldi",
    ],
)
