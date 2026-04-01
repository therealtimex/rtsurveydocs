---
title: "Image"
description: "Le domande image permettono ai rispondenti di acquisire e inviare foto come parte del sondaggio."
icon: "image"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 227
---

Il tipo di domanda image negli XLSForm e in rtSurvey consente ai rispondenti di acquisire e inviare foto come parte delle loro risposte al sondaggio. Questa funzionalità è particolarmente utile per raccogliere dati visivi, documentare osservazioni, o fornire prove nei sondaggi sul campo.

## Specifica XLSForm di base

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| image | photo       | Scatta una foto del luogo    |

Per ulteriori dettagli sul tipo di domanda image di base, vedere la [specifica XLSForm](https://xlsform.org/en/#question-types).

## Utilizzi

Le domande image sono comunemente usate per:

1. Documentare le condizioni o le osservazioni sul campo
2. Acquisire prove visive negli studi di ricerca
3. Raccogliere foto prima e dopo nelle valutazioni d'impatto
4. Verificare il completamento dei compiti o la presenza nelle posizioni
5. Raccogliere dati visivi per l'analisi remota

## Best practice

1. Fornire istruzioni chiare su cosa dovrebbe essere fotografato.
2. Considerare le implicazioni sulla privacy e informare i rispondenti su come verranno utilizzate le loro foto.
3. Essere consapevoli delle dimensioni dei file e dei limiti di archiviazione, specialmente per i sondaggi in aree con connettività internet limitata.
4. Assicurarsi che il dispositivo abbia spazio di archiviazione sufficiente e i permessi della fotocamera siano concessi.

## Esempio di utilizzo

Ecco un esempio di come potresti usare una domanda image in un sondaggio:

| type  | name           | label                                      | hint                                        |
|-------|----------------|--------------------------------------------|--------------------------------------------|
| image | storefront     | Scatta una foto dell'ingresso del negozio       | Assicurati che il nome del negozio sia chiaramente visibile    |

## Estensioni rtSurvey

Mentre la specifica XLSForm di base per le domande image è semplice, rtSurvey può offrire funzionalità o personalizzazioni aggiuntive:

1. Impostazioni della qualità dell'immagine (es. bassa, media, alta risoluzione)
2. Opzione per aggiungere didascalie o tag alle immagini
3. Acquisizione di più immagini per una singola domanda
4. Integrazione con l'app fotocamera nativa del dispositivo o la galleria

## Gestione dei dati

Le immagini raccolte tramite questo tipo di domanda sono tipicamente:

1. Salvate in un formato immagine comune (es. JPG, PNG)
2. Memorizzate insieme agli altri dati del sondaggio, spesso in una cartella media separata
3. Accessibili per la visualizzazione e l'analisi tramite la piattaforma di gestione dei sondaggi

## Considerazioni per l'analisi

Quando usi le domande image, considera:

1. Come le immagini verranno analizzate (es. revisione manuale, analisi automatizzata delle immagini)
2. Lo spazio di archiviazione aggiuntivo richiesto per i file di immagine
3. Misure di privacy e protezione dei dati per l'archiviazione e la gestione delle foto
4. La potenziale necessità di strumenti di modifica o organizzazione delle immagini nella fase di analisi

## Limitazioni

- I file di immagine possono essere grandi, il che può influire sul trasferimento e sull'archiviazione dei dati.
- Non tutti i dispositivi potrebbero avere fotocamere di alta qualità o spazio di archiviazione sufficiente.
- L'analisi di un gran numero di immagini può richiedere molto tempo.
- Potrebbero esserci preoccupazioni sulla privacy durante l'acquisizione di immagini, specialmente negli spazi pubblici.
