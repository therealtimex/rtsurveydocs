---
title: "Sola lettura"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 287
---

I campi di sola lettura in rtSurvey ti consentono di visualizzare informazioni che non possono essere modificate dal rispondente. Questa funzionalità è particolarmente utile per mostrare dati pre-compilati, risultati calcolati, o informazioni che devono rimanere costanti per tutta la durata del sondaggio.

## Utilizzo di base

Per rendere un campo di sola lettura, usa la colonna `read_only` nel tuo XLSForm:

```
| type    | name | label                 | read_only | default |
|---------|------|----------------------|-----------|---------|
| integer | num  | Il numero del paziente è:    | yes       | 5       |
```

In questo esempio, il numero del paziente è impostato a 5 e non può essere modificato dal rispondente.

## Combinazione della sola lettura con i valori predefiniti

I campi di sola lettura vengono spesso usati insieme ai valori predefiniti per visualizzare informazioni predeterminate o calcolate:

```
| type    | name     | label               | read_only | default        |
|---------|----------|---------------------|-----------|----------------|
| text    | username | Utente connesso:     | yes       | ${current_user}|
| date    | today    | Data odierna:       | yes       | today()        |
```

Qui, il nome utente e la data corrente vengono visualizzati ma non possono essere modificati.

## Funzionalità specifiche di rtSurvey

### Sola lettura condizionale

rtSurvey estende la funzionalità di sola lettura con la logica condizionale:

```
| type    | name     | label           | read_only                |
|---------|----------|-----------------|--------------------------|
| integer | age      | Età:            | ${role} = 'viewer'       |
| text    | comments | Commenti:       | selected(${status}, 'closed') |
```

In questi esempi:
- Il campo 'age' è di sola lettura solo se il ruolo dell'utente è 'viewer'.
- Il campo 'comments' diventa di sola lettura se lo stato è 'closed'.

### Stato di sola lettura dinamico

rtSurvey ti consente di cambiare dinamicamente lo stato di sola lettura:

```
| type      | name     | label    | read_only              |
|-----------|----------|----------| ----------------------|
| text      | address  | Indirizzo: | ${edit_mode} = 'false' |
```

Questo ti consente di passare tra le modalità modificabile e di sola lettura in base a determinate condizioni o azioni dell'utente.

## Best practice per l'utilizzo dei campi di sola lettura

1. **Chiarezza**: Indica chiaramente quali campi sono di sola lettura attraverso segnali visivi o etichette.
2. **Coerenza**: Usa i campi di sola lettura in modo coerente in tutto il tuo sondaggio.
3. **Validazione**: Anche se i campi di sola lettura non possono essere modificati, includili nel tuo processo di validazione dei dati.
4. **Prestazioni**: Sii cauto con i calcoli complessi nei campi di sola lettura, poiché possono influire sul tempo di caricamento del modulo.
5. **Accessibilità**: Assicurati che i campi di sola lettura siano correttamente contrassegnati per i lettori di schermo.

## Tecniche avanzate

### Campi di sola lettura calcolati

Usa i campi di sola lettura per visualizzare i calcoli basati su altre risposte:

```
| type      | name     | label           | read_only | calculation            |
|-----------|----------|-----------------|-----------|------------------------|
| calculate | bmi      | BMI:            | yes       | ${weight} / (${height} * ${height}) |
```

### Visualizzazione di dati storici

I campi di sola lettura possono visualizzare dati da sondaggi precedenti o fonti esterne:

```
| type    | name           | label                  | read_only | default                    |
|---------|----------------|------------------------|-----------|----------------------------|
| text    | last_visit_date| Data dell'ultima visita:    | yes       | ${pulldata('visits', 'date', 'id', ${patient_id})} |
```

## Considerazioni sulla gestione dei dati

- I campi di sola lettura sono inclusi nelle esportazioni dei dati, tipicamente con un flag che indica il loro stato di sola lettura.
- Quando si aggiornano i record esistenti, i campi di sola lettura preservano i loro valori originali a meno che non vengano esplicitamente sovrascritti tramite il backend.

## Comportamento nell'app mobile

- L'app mobile di rtSurvey rispetta le impostazioni di sola lettura, inclusa la logica di sola lettura condizionale.
- La modalità offline supporta pienamente la funzionalità di sola lettura, inclusi i campi di sola lettura dinamici e calcolati.

## Limitazioni note

- Alcune condizioni di sola lettura dinamiche complesse possono avere un leggero impatto sulle prestazioni sui dispositivi di fascia bassa.
- I campi di sola lettura potrebbero non impedire tutte le forme di manipolazione dei dati nei file di dati esportati, quindi è consigliabile la validazione lato server per i dati critici.

## Risoluzione dei problemi con i campi di sola lettura

1. **Campo inaspettatamente modificabile**: Controlla la presenza di errori di sintassi nella colonna `read_only` o nella logica condizionale.
2. **Valori calcolati non aggiornati**: Verifica la logica di calcolo e assicurati che tutti i campi referenziati siano denominati correttamente.
3. **Problemi di prestazioni**: Ottimizza i calcoli complessi o considera approcci alternativi per la visualizzazione dei dati di sola lettura.
