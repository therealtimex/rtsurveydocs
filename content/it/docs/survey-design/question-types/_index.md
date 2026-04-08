---
title: "Tipi di domanda"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 220
---

rtSurvey supporta tutti i tipi di domanda standard XLSForm, oltre a diverse estensioni. Ogni tipo di domanda controlla il tipo di dati raccolti e come viene visualizzato il widget di input sul dispositivo.

Per impostare il tipo di domanda, inserisci il nome del tipo nella colonna `type` del foglio di lavoro **survey** nel tuo XLSForm.

## Input di testo

| Tipo | Descrizione |
|------|-------------|
| [text](text) | Risposta a testo libero — qualsiasi carattere consentito |
| [integer](integer) | Numero intero (senza decimali) |
| [decimal](decimal) | Numero con cifre decimali |
| [range](range) | Numero selezionato tramite uno slider in un intervallo min/max definito |

## Selezione

| Tipo | Descrizione |
|------|-------------|
| [select_one listname](select-one) | Scegli esattamente un'opzione da un elenco |
| [select_multiple listname](select-multiple) | Scegli una o più opzioni da un elenco |
| [rank listname](rank) | Ordina le scelte per preferenza o priorità |

## Data e ora

| Tipo | Descrizione |
|------|-------------|
| [date](date) | Data del calendario (anno, mese, giorno) |
| [time](time) | Ora del giorno (ore, minuti) |
| [datetime](datetime-date-time) | Data e ora combinate |

## Posizione

| Tipo | Descrizione |
|------|-------------|
| [geopoint](geopoint) | Singola coordinata GPS (latitudine, longitudine, altitudine, precisione) |
| [geotrace](geotrace) | Un percorso — serie di punti GPS che formano una linea |
| [geoshape](geoshape) | Un'area — poligono chiuso di punti GPS |

## Media

| Tipo | Descrizione |
|------|-------------|
| [image](image) | Acquisizione di foto o caricamento di immagini |
| [audio](audio) | Registrazione audio |
| [video](video) | Registrazione video |
| [file](file) | Caricamento di file generico (PDF, documenti, ecc.) |

## Altro

| Tipo | Descrizione |
|------|-------------|
| [barcode](barcode) | Scansione di un codice a barre o codice QR |
| [note](note) | Testo di sola lettura — mostra istruzioni o riepiloghi calcolati |
| [calculate](calculate) | Campo nascosto che memorizza un valore calcolato |
| [hidden](hidden) | Campo nascosto che memorizza un valore statico o pre-compilato |
| [trigger / acknowledge](trigger) | Una casella di controllo che l'enumeratore deve spuntare per confermare di aver letto una dichiarazione |
| [meta](meta) | Metadati automatici: timestamp, ID dispositivo, informazioni sull'enumeratore |

## Estensioni rtSurvey

Questi tipi sono specifici di rtSurvey e non fanno parte della specifica XLSForm standard.

| Tipo | Descrizione |
|------|-------------|
| [search-autocomplete](search-autocomplete) | Inserimento testo con suggerimenti di completamento automatico basati su API in tempo reale |
| [mentions](mentions) | Campo di testo con completamento automatico delle menzioni `@` per taggare entità inline |
| [texttags](texttags) | Inserimento tag — ogni voce diventa un chip rimovibile; memorizzato come stringa separata da spazi |

Per i gruppi di ripetizione, vedere [Repeats](../advanced-extension/repeats)

## Come tipo e appearance lavorano insieme

Il `type` determina **quali dati vengono raccolti**. La colonna `appearance` controlla **come appare il widget**. Molti tipi supportano più appearance — ad esempio `select_one` può apparire come pulsanti radio, un menu a discesa, una scala Likert o una griglia compatta.

Vedi [Appearance](../appearance) per l'elenco completo delle opzioni.
