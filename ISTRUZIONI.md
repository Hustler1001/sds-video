# Storia dei Soldi · istruzioni di produzione

Canale YouTube **Storia dei Soldi** (@storiadeisoldi): storia economica italiana raccontata con i numeri.
Documentari lunghi (18-25 minuti) e short verticali (25-55 secondi). Pubblico italiano, soprattutto adulto e over 55.
Obiettivo: crescere fino al Programma partner di YouTube (1.000 iscritti + ore di visione dei video lunghi).
Tutto è gratuito: voce Edge TTS, grafica in Python. Non usare strumenti a crediti.

## Regole fisse (valgono sempre)

1. **Ogni numero, data o legge** va verificato su una fonte primaria (Istat, Banca d'Italia, INPS, MEF, Dipartimento delle Finanze, Normattiva, Gazzetta Ufficiale, Agenzia delle Entrate, Corte costituzionale, Senato/Camera) con WebSearch o WebFetch. Nei documentari ogni cifra importante deve avere **due** fonti concordi; se non le trovi, non usarla. I calcoli li fai in codice con `assert` e li indichi come "Esempio calcolato".
2. Niente consigli di investimento, niente politica di parte, niente accuse a persone o aziende con nome e cognome. Si raccontano i fatti.
3. **Niente stampino.** YouTube non paga i canali con video ripetitivi. Cambia ogni volta la prima frase, l'icona, l'ordine delle scene (hero / elenco), il titolo. Non riusare la stessa formula di titolo due volte di fila.
4. **Gancio**: nei primi 2 secondi una cifra concreta (prezzo in lire o euro, percentuale, anno con una cifra). È il modello che finora rende 5-10 volte di più.
5. Domanda finale specifica (un anno, una cifra, un ricordo di famiglia), mai "cosa ne pensi?".
6. La voce è sintetica: in descrizione scrivi sempre "Voce e grafiche realizzate con strumenti di intelligenza artificiale." e su Posty `containsSyntheticMedia: yes`.
7. Non ripetere temi già in `registro.json` (salvo serie dichiarate, come "Sei nato nel 19XX?" con anni diversi).

## Preparazione (ogni sessione)

```
git clone --depth 1 https://github.com/Hustler1001/sds-video   # se non c'è già (prima add_repo Hustler1001/sds-video, push)
cd sds-video && bash setup.sh
```
Le spec nuove vanno in `spec/AAAA-MM-GG-nome.py`. I file di lavoro in `lavoro/` (non vanno su git).

## SHORT

1. **Tema**: scegli dal foglio Idee (priorità più alta, Stato "Da fare" o "In corso") o una nuova idea con cifra concreta. Controlla `registro.json` e `list_posts` di Posty (ultimi 30 giorni e prossimi 30) per non ripetere.
2. **Spec**: copia `esempi/short_esempio_1960.py`. Tipi di scena: `hero` (icona + parola grande), `list` (elenco che compare voce per voce: ogni voce ha la parola che la fa comparire), `end` (cartello scuro finale). 3-5 scene, testo parlato 25-55 secondi. Le cifre nel testo scrivile in numeri (84 lire, 1.199 lire): la didascalia le colora in giallo. Icone disponibili: lista `ICONS` in `lib/common.py`.
3. **Anteprima**: `python3 short/render_short.py spec/<file>.py lavoro/<nome> preview` e guarda i PNG con Read: niente testo tagliato o sovrapposto.
4. **Video**: `bash make_short.sh spec/<file>.py <nome>`. Controlla: durata 20-58 s, volume circa -16 LUFS, e guarda `lavoro/<nome>/controllo.png`.
5. **Short da un documentario uscito**: 2-3 fatti forti del documentario, ognuno uno short, con scena finale `end` big="Il documentario completo", sub1="è sul canale", sub2="«Titolo breve» · NN minuti". Solo dopo che il documentario è pubblico.

## DOCUMENTARIO

1. **Tema**: foglio Idee, Tipo Documentario, priorità più alta e non fatto. Preferisci temi con pubblicità ben pagata (mutui, casa, risparmio, pensioni, tasse, inflazione) e una domanda che la gente cerca.
2. **Ricerca**: 10-25 ricerche. Costruisci una cronologia con fonti. Ogni cifra: due fonti.
3. **Struttura** (copia `esempi/doc_esempio_03_tasse.py`): introduzione con due cifre che si contraddicono e una domanda; 1-2 "idee chiave" spiegate semplici; 5-7 capitoli (cartello `card=True` + 3-6 scene); finale "cosa ci insegna questa storia" che torna alla domanda iniziale. Totale 3.000-3.600 parole circa = 18-25 minuti. Frasi brevi, numeri scritti in lettere nel testo parlato (la voce li legge meglio), esempi concreti calcolati in codice.
4. Imposta `TIMELINE` (anno iniziale, 2026), `CHAPTERS`, `COVER` (line1, big, pill, sub, icon).
5. **Anteprima** di 4-5 scene: `python3 doc/render_doc.py spec/<file>.py lavoro/<nome> preview 0,3,10,20` e guardale.
6. **Video**: `bash make_doc.sh spec/<file>.py <nome>` (circa 5-10 minuti). Controlla `controllo.png`, `copertina.png`, durata, e che il file sia sotto 95 MB.
7. **Capitoli** per la descrizione: `lavoro/<nome>/capitoli.json` (secondi dall'inizio). Il primo capitolo in descrizione è sempre "00:00 Introduzione".

## CONSEGNA A POSTY

1. `bash consegna.sh lavoro/<nome>/<nome>.mp4 [lavoro/<nome>/copertina.png]` stampa `BRANCH=...` e gli `URL=...`.
2. Posty: `get_workspace_context`, `get_integration_schema` (integrationId **cmwim1wcw01qss28ftpsf8cuu**), `upload_media_from_url` con ogni URL (video e copertina).
3. Subito dopo il caricamento cancella il branch: `git push origin --delete <BRANCH>`.
4. `preview_post`, poi `create_post` con un idempotencyKey nuovo, type "schedule". Impostazioni YouTube:
   - `title` (max 100 caratteri, con le parole che la gente cerca e l'anno), `type` public, `selfDeclaredMadeForKids` no, `containsSyntheticMedia` yes;
   - documentario: anche `thumbnail` = {id, path} della copertina caricata e `tags` (8-12, come nell'esempio).
   - Testo HTML, ogni paragrafo in `<p>`: gancio con le cifre, di cosa parla, domanda per i commenti, CAPITOLI (solo documentari), FONTI, "Video a scopo informativo ed educativo...", frase sulla voce sintetica, 3-5 hashtag con #storiadeisoldi.
5. **Orari** (Europe/Rome): uno short al giorno alle 18:00; se alle 18:00 c'è un documentario, lo short va alle 12:00. Documentari il martedì alle 18:00. Massimo 3 post al giorno sul canale.
6. Verifica con `list_posts`.

## DOPO

1. Aggiungi il video a `registro.json`, salva la spec in `spec/`, poi `git add registro.json spec && git commit -m "..." && git pull --rebase origin main && git push origin HEAD:main`.
2. Foglio «Storia dei Soldi · Monetizzazione» (Claude Docs, id c01449c9-4a53-4f50-9c88-bb8e0fba7eb0): aggiungi la riga nel foglio Calendario (Data, Ora, Tipo, Tema, "In coda", postId) e, se hai usato un'idea, metti Stato "Fatto" nel foglio Idee. Prima chiama `guide` con `["topic.sheets"]`.
3. Messaggio breve a Gen: cosa è in coda, quando esce, e ogni dato che è rimasto dubbio.
