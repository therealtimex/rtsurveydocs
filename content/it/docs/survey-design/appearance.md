---
title: "Aspetto (Appearance)"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

La colonna `appearance` in rtSurvey consente di personalizzare la presentazione visiva e il comportamento delle domande nei tuoi sondaggi. Questa funzionalità migliora l'esperienza utente e può migliorare significativamente l'efficienza della raccolta dati. rtSurvey supporta gli attributi di appearance XLSForm standard ed li estende con opzioni aggiuntive.

## Attributi di appearance XLSForm standard

rtSurvey supporta i seguenti attributi di appearance XLSForm standard:

| Attributo appearance | Tipi di domanda | Descrizione |
|----------------------|----------------|-------------|
| multiline | text | Crea una casella di testo multiriga (ideale per i client web) |
| minimal | select_one, select_multiple | Mostra le scelte in un menu a discesa |
| quick | select_one | Avanza automaticamente alla domanda successiva dopo la selezione (solo mobile) |
| no-calendar | date | Sopprime la visualizzazione del calendario (solo mobile) |
| month-year | date | Consente la selezione solo di mese e anno |
| year | date | Consente la selezione solo dell'anno |
| horizontal-compact | select_one, select_multiple | Mostra le scelte orizzontalmente (solo web) |
| horizontal | select_one, select_multiple | Mostra le scelte orizzontalmente in colonne (solo web) |
| likert | select_one | Presenta le scelte come scala Likert |
| compact | select_one, select_multiple | Mostra le scelte fianco a fianco con padding minimo |
| quickcompact | select_one | Combina la visualizzazione compatta con l'avanzamento automatico (solo mobile) |
| field-list | groups | Mostra l'intero gruppo su un'unica schermata (solo mobile) |
| label | select_one, select_multiple | Mostra le etichette delle scelte senza input |
| list-nolabel | select_one, select_multiple | Mostra gli input senza etichette (usare con `label`) |
| table-list | groups | Mostra le domande in formato tabella |
| signature | image | Abilita l'acquisizione della firma (solo mobile) |
| draw | image | Consente il disegno a mano libera (solo mobile) |
| map, quick map | select_one, select_one_from_file | Abilita la selezione dalle feature della mappa |

## Best practice per l'uso di Appearance

1. **Coerenza**: Usa gli attributi di appearance in modo coerente nel tuo sondaggio per un aspetto uniforme.
2. **Mobile vs. Web**: Considera come le appearance vengono renderizzate su diversi dispositivi e piattaforme.
3. **Prestazioni**: Sii cauto con gli attributi di appearance che potrebbero rallentare il caricamento del modulo (es. `table-list` per gruppi di grandi dimensioni).
4. **Esperienza utente**: Scegli appearance che rendono l'inserimento dati più facile e intuitivo per i rispondenti.
5. **Test**: Testa sempre il tuo modulo sui dispositivi di destinazione per assicurarti che le appearance funzionino come previsto.

## Tecniche avanzate

### Combinare le appearance

Alcuni attributi di appearance possono essere combinati per layout più complessi:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Seleziona uno: | minimal compact |
```

### Appearance dinamiche

rtSurvey consente modifiche dinamiche dell'appearance basate sulla logica del modulo:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Inserisci l'orario: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Considerazioni sull'app mobile

- Alcune appearance (es. `quick`, `signature`) sono specifiche per i dispositivi mobili.
- Testa approfonditamente sia su Android che su iOS per garantire un comportamento coerente.

## Attributi di appearance estesi di rtSurvey

Oltre alle appearance XLSForm standard, rtSurvey supporta le seguenti opzioni specifiche per la piattaforma:

### Controllo dati e visualizzazione

| Attributo appearance | Tipi di domanda | Descrizione |
|----------------------|----------------|-------------|
| `invisible` | qualsiasi | Nasconde il campo dalla vista pur raccogliendo o calcolando il suo valore. Diverso dal tipo `hidden` — il campo partecipa ancora alla logica. |
| `displaytitle` | qualsiasi | Forza la visualizzazione dell'etichetta/titolo del campo anche quando sarebbe altrimenti soppressa. |
| `autopull` | select_one, select_multiple | Recupera automaticamente dati esterni per popolare le scelte quando il modulo si carica o quando un campo trigger cambia. |
| `floating_hint` | text, integer, decimal | Mostra il testo del suggerimento come etichetta flottante sopra il campo di input invece che sotto. |
| `calculate-button` | calculate | Aggiunge un pulsante visibile che attiva il ricalcolo del campo su richiesta, piuttosto che calcolare automaticamente. |

### Layout

| Attributo appearance | Tipi di domanda | Descrizione |
|----------------------|----------------|-------------|
| `1screen` | group | Forza l'intero gruppo a essere visualizzato su un'unica schermata indipendentemente dalla dimensione del gruppo. |
| `columns(n)` | select_one, select_multiple | Mostra le scelte in `n` colonne. Esempio: `columns(3)` mostra tre colonne di pulsanti radio. |
| `gridformat<row=R col=C colspan=S align=center>` | qualsiasi | Posiziona il campo in un layout CSS-grid alla riga `R`, colonna `C`, coprendo `S` colonne. Usato con `advanced-extension/grid-layout`. |
| `ignore-simplify` | qualsiasi | Istruisce il renderer del modulo a saltare la semplificazione automatica o la condensazione del layout di questo campo. |
| `required-but-simplify` | qualsiasi | Il campo è obbligatorio ma il layout viene comunque semplificato |
| `embed` | qualsiasi | Visualizza il campo in modalità incorporata/inline |
| `popup` | select_one, select_multiple | Visualizza l'elenco delle scelte in un overlay popup/modale |
| `auto-hide-empty` | boxtag, select | Nasconde il widget quando l'elenco delle scelte è vuoto |
| `text-nolabel` | select_one, select_multiple | Nasconde l'etichetta testuale per ogni scelta |

### Widget

| Attributo appearance | Tipi di domanda | Descrizione |
|----------------------|----------------|-------------|
| `likert` | select_one | Presenta le scelte come riga della scala Likert (già nella tabella standard sopra; confermato supportato). |
| `distress` | select_one | Renderizza le scelte come widget visivo della scala di disagio psicologico di Kessler (K10) con icone emotive. |

### Widget visivi per la selezione

| Attributo appearance | Tipi di domanda | Descrizione |
|----------------------|----------------|-------------|
| `tagging` | select_one, select_multiple | Mostra le scelte come chip di tag cliccabili invece di pulsanti radio o caselle di controllo |
| `boxtag` | select_one, select_multiple | Mostra le scelte come riquadri rettangolari stilizzati che l'utente tocca per selezionare |
| `boxtag -search` | select_one, select_multiple | Layout boxtag con un campo di ricerca/filtro sopra i riquadri |
| `duolingo-style1` | select_one, select_multiple | Layout a schede ispirato a Duolingo — grandi schede toccabili con icone |
| `rating_box` | select_one | Riquadri di valutazione a griglia — ideale per scelte numeriche o a scala |
| `star_rating` | select_one | Widget di valutazione a stelle — le scelte vengono visualizzate come 1–N stelle |
| `choices-noshow` | select_one, select_multiple | Mostra inizialmente solo le prime 10 scelte; rivela le restanti su richiesta |
| `noshow` | select_one | Nasconde completamente l'elenco delle scelte; il valore viene impostato programmaticamente |
| `checkall` | select_multiple | Aggiunge un'opzione "Seleziona tutto" in cima all'elenco |
| `max-items(N)` | select_one, select_multiple | Limita il numero di scelte visibili a N (es. max-items(5)) |

### Widget visivi per il testo

| Attributo appearance | Tipi di domanda | Descrizione |
|----------------------|----------------|-------------|
| `richtext` | text | Editor di testo ricco — barra degli strumenti con grassetto, corsivo, elenchi e link |
| `typingtest` | text | Interfaccia di test di digitazione — presenta un brano e misura velocità e precisione di digitazione |

### Estensioni media

| Attributo appearance | Tipi di domanda | Descrizione |
|----------------------|----------------|-------------|
| `watermark("expr")` | image | Sovrappone una filigrana di testo alla foto acquisita; l'argomento è un'espressione XPath valutata al momento dell'acquisizione |
| `editable` | image | Consente al rispondente di annotare o disegnare sulla foto acquisita |

### Configurazione del display inline

Usa `display{}` per controllare come viene visualizzato il valore di un campo all'interno di un'etichetta o di una nota. Usa `results{}` per controllare il riepilogo dei risultati visualizzato dopo l'invio.

| Sintassi | Tipi di domanda | Descrizione |
|----------|----------------|-------------|
| `display{format="..."}` | qualsiasi | Formatta il valore del campo quando viene inserito inline in un'etichetta tramite `${fieldname}` |
| `results{show="true"}` | qualsiasi | Mostra il valore del campo nel riepilogo dei risultati post-invio |

### Integrazione API

| Attributo appearance | Tipi di domanda | Descrizione |
|----------------------|----------------|-------------|
| `callapi` | text, integer, decimal, select_one | Abilita l'integrazione della chiamata API per questo campo. La colonna calculation dovrebbe contenere un'espressione `callapi()`. Vedi [Call API](advanced-extension/call-api). |
| `callapi-verify(params)` | text, integer, decimal | Attiva una chiamata di verifica API usando parametri statici. Il modulo blocca l'avanzamento finché l'API non conferma il valore. |
| `callapi-verify(dynamicParams)` | text, integer, decimal | Come `callapi-verify` ma con parametri derivati dai valori di altri campi in fase di esecuzione. |

### Formato data/ora inline

Per i campi `date`, `time` e `datetime`, puoi specificare un formato di visualizzazione personalizzato usando una stringa di formato aggiunta all'appearance:

```
inline-[%d/%m/%Y]
inline-1line-[%d/%m/%Y %H:%M]
```

I token di formato sono gli stessi di `format-date()` e `format-date-time()`. Vedi [Funzioni — Funzioni data e ora](operators-and-functions/functions#date-and-time-functions).

Esempio:

| type | name | label | appearance |
|------|------|-------|------------|
| datetime | event_time | Data e ora dell'evento | inline-[%d/%m/%Y %I:%M %p] |
| date | birth_date | Data di nascita | inline-[%d/%m/%Y] |

## Limitazioni note

- Le appearance complesse potrebbero non essere renderizzate in modo identico su tutte le piattaforme.
- Alcune appearance avanzate di rtSurvey potrebbero non essere supportate in modalità offline.

## Risoluzione dei problemi di appearance

1. **Appearance non applicata**: Controlla la presenza di errori di battitura nella colonna appearance.
2. **Rendering inconsistente**: Verifica la compatibilità con il tipo di domanda e la piattaforma.
3. **Problemi di prestazioni**: Considera la semplificazione delle appearance complesse, specialmente per sondaggi di grandi dimensioni.
