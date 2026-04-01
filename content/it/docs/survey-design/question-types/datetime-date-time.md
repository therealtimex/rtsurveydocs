---
title: "Datetime, data, ora"
description: "Le domande datetime permettono ai rispondenti di inserire sia la data che l'ora in un singolo campo."
icon: "event"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 226
---

Il tipo di domanda datetime negli XLSForm e in rtSurvey consente ai rispondenti di inserire sia la data che l'ora in un singolo campo. Questo tipo di domanda è utile quando è necessario acquisire un momento specifico nel tempo, inclusa sia la data che l'ora esatta.

## Specifica XLSForm di base

| type     | name           | label                           |
|----------|----------------|--------------------------------|
| datetime | event_datetime | Quando si è verificato l'evento?       |

Per ulteriori dettagli sul tipo di domanda datetime di base, vedere la [specifica XLSForm](https://xlsform.org/en/#question-types).

## Utilizzi

Le domande datetime sono comunemente usate per:

1. Registrare timestamp di eventi o osservazioni
2. Pianificare appuntamenti o riunioni
3. Registrare orari di inizio e fine delle attività
4. Acquisire momenti precisi per la raccolta di dati sensibili al tempo

## Estensioni rtSurvey

rtSurvey estende la funzionalità delle domande datetime con varie appearance e opzioni di personalizzazione:

### Opzioni di appearance

- `(predefinito)`: Visualizza il calendario e l'orologio per la selezione di data e ora
- `inline`: Visualizza il calendario e l'orologio come icone
- `inline-1line`: Visualizza il calendario e l'orologio per la selezione in formato a riga singola
- `inline-onlyresult`: Visualizza il calendario e l'orologio come icone alla fine della riga; le icone scompaiono dopo la selezione

### Personalizzazione dei colori

Puoi personalizzare il colore delle icone del calendario e dell'orologio usando la funzione `colors()`:

- `inline colors("0099FF")`: Visualizza le icone con colore personalizzato
- `inline-1line-0000FF`: Visualizza in formato a riga singola con colore personalizzato
- `inline-1line colors("0000FF","FFFF00")`: Visualizza in formato a riga singola con più colori personalizzati
- `inline-onlyresult colors("0099FF")`: Visualizza le icone che scompaiono dopo la selezione, con colore personalizzato

### Formati personalizzati di data e ora

rtSurvey consente formati personalizzati di data e ora usando una sintassi speciale:

- `inline-[%Y-%m-%d %H:%M:%S]`: Esempio di formato personalizzato (Anno-Mese-Giorno Ora:Minuto:Secondo)
- `inline-[%d/%m/%Y %I:%M %p]`: Esempio di formato personalizzato (Giorno/Mese/Anno Ora:Minuto AM/PM)

## Esempio di utilizzo

Ecco un esempio di come potresti usare una domanda datetime in un sondaggio:

| type     | name           | label                                      | appearance                    |
|----------|----------------|--------------------------------------------|-----------------------------|
| datetime | incident_time  | Quando si è verificato l'incidente?               | inline-[%d/%m/%Y %I:%M %p]  |

## Best practice

1. Fornire istruzioni chiare sul formato di data e ora previsto.
2. Considerare l'utilizzo dell'appearance `inline` per una visualizzazione più compatta.
3. Usare formati personalizzati quando si ha bisogno di componenti specifici di data e ora o formattazione.
4. Essere consapevoli dei fusi orari quando si raccolgono dati datetime in diverse regioni.

## Limitazioni

- Alcune appearance o formati personalizzati potrebbero non essere supportati su tutti i dispositivi o piattaforme.
- Gli utenti potrebbero aver bisogno di indicazioni per inserire correttamente data e ora, specialmente con formati personalizzati.
- Le differenze di fuso orario possono complicare l'analisi dei dati se non adeguatamente considerate.
