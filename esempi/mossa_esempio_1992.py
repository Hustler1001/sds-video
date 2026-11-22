# ESEMPIO DI FORMATO "Mossa per mossa" (6-9 minuti). Non è un video in coda.
# Le cifre qui sotto servono a mostrare il formato: prima di usarle in un video, verificale con due fonti.
# Copialo in spec/AAAA-MM-GG-nome.py e riscrivi tutto.
#
# Come funziona il formato:
# - EVAL = i due lati della "partita" (il primo sta in basso nella barra). La barra va da -10 a +10:
#   positivo = sta vincendo il primo lato, negativo = il secondo. Ogni scena può avere barra=<numero>.
# - Le scene con mossa=dict(n, chi, voto) mostrano il voto al posto dell'icona.
#   Voti: GENIALE (!!), OTTIMA (!), BUONA (+), IMPRECISIONE (?!), ERRORE (?), DISASTRO (??).
# - Il voto è un giudizio nostro: la voce lo dice e lo giustifica SEMPRE con una cifra ("ERRORE: costò X").
# - Struttura: gancio (cifra + "chi vince questa partita?"), la situazione con la barra a zero,
#   6-10 mosse (1-3 scene ciascuna, la barra si sposta), il risultato finale, la pagella, la domanda per i commenti.
# - 900-1.400 parole parlate = 6-9 minuti. Capitoli = le mosse.
RATE = "-2%"
VOICE = "it-IT-GiuseppeMultilingualNeural"  # voce del formato Mossa per mossa
TIMELINE = (1985, 2026)
EVAL = ("ITALIA", "MERCATI")
TITLE = "La lira contro i mercati, 1992"
CHAPTERS = {0: "", 1: "Mossa 1 · Il prelievo", 2: "Mossa 2 · I tassi al 15%"}
COVER = dict(line1="Lira 1992", big="ERRORE?", pill="Mossa per mossa",
             sub="L'Italia contro i mercati: chi ha vinto la partita", icon="coin:1000")
SCENES = [
dict(chunk=0, year=1992, icon="coin:1000", barra=0, big="1992", sub1="L'Italia contro i mercati",
     sub2="Una partita durata tre mesi", src="",
     text="Nel 1992 l'Italia gioca una partita contro i mercati. La posta è la lira. Vediamola mossa per mossa, e diamo un voto a ogni decisione."),
dict(chunk=1, year=1992, card=True, barra=-1, big="Mossa 1", sub1="Il prelievo sui conti", sub2="Luglio 1992",
     text="Mossa uno. Il prelievo sui conti."),
dict(chunk=1, year=1992, barra=-2.5, mossa=dict(n=1, chi="Governo", voto="IMPRECISIONE"),
     big="6 PER MILLE", sub1="Prelevato da tutti i conti correnti", sub2="Nella notte tra il 9 e il 10 luglio 1992",
     src="Fonte: decreto-legge 11 luglio 1992, n. 333",
     text="Nella notte tra il nove e il dieci luglio il governo preleva il sei per mille da tutti i conti correnti. Porta soldi subito, ma gli italiani perdono fiducia. Voto: imprecisione."),
dict(chunk=2, year=1992, barra=-4.5, mossa=dict(n=2, chi="Banca d'Italia", voto="ERRORE"),
     big="15%", sub1="Il tasso di sconto a settembre", sub2="Era al 13,75%: difendere la lira costa caro",
     src="Fonte: Banca d'Italia",
     text="Il quattro settembre la Banca d'Italia alza il tasso di sconto al quindici per cento. Serve a difendere la lira, ma la speculazione non si ferma. Voto: errore."),
]
