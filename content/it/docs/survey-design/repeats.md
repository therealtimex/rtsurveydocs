---
title: "Domande ripetute"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 260
---

I repeat sono una potente funzionalità in rtSurvey che ti consente di raccogliere lo stesso insieme di informazioni più volte all'interno di un singolo sondaggio. Questo è particolarmente utile per scenari come i sondaggi familiari, in cui potresti dover raccogliere dati su più membri della famiglia.

## Struttura di base del repeat

Per creare un repeat in rtSurvey, usa il costrutto `begin repeat` e `end repeat`:

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat |                      |
| text         | name         | Nome del bambino         |
| decimal      | birthweight  | Peso alla nascita del bambino  |
| select_one male_female | sex | Sesso del bambino         |
| end repeat   |              |                      |
```

In questo esempio, l'utente può raccogliere informazioni su più bambini aggiungendo nuovi repeat nel modulo.

## Etichettatura dei repeat

Mentre la colonna `label` è opzionale per `begin repeat`, aggiungere un'etichetta può migliorare la navigazione:

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat | Informazioni sul bambino    |
| text         | name         | Nome del bambino         |
| decimal      | birthweight  | Peso alla nascita del bambino  |
| select_one male_female | sex | Sesso del bambino         |
| end repeat   |              |                      |
```

rtSurvey visualizzerà "Informazioni sul bambino" come titolo per ogni istanza del repeat.

## Conteggi fissi dei repeat

Per specificare un numero fisso di repeat, usa la colonna `repeat_count`:

```
| type         | name         | label                | repeat_count |
|--------------|--------------|----------------------|--------------|
| begin repeat | child_repeat | Informazioni sul bambino    | 3            |
| text         | name         | Nome del bambino         |              |
| decimal      | birthweight  | Peso alla nascita del bambino  |              |
| end repeat   |              |                      |              |
```

Questo creerà esattamente 3 repeat per i bambini.

## Conteggi dinamici dei repeat

rtSurvey supporta conteggi dinamici dei repeat basati sulle risposte precedenti:

```
| type     | name           | label                          | repeat_count       |
|----------|----------------|--------------------------------|--------------------|
| integer  | num_hh_members | Numero di membri della famiglia?   |                    |
| begin repeat | hh_member  | Membro della famiglia               | ${num_hh_members}  |
| text     | name           | Nome                           |                    |
| integer  | age            | Età                            |                    |
| end repeat |              |                                |                    |
```

## Repeat condizionali

Puoi usare la colonna `relevant` per visualizzare condizionalmente i repeat:

```
| type              | name        | label                     | relevant           |
|-------------------|-------------|---------------------------|---------------------|
| select_one yes_no | has_child   | Ci sono bambini qui?|                     |
| begin repeat      | child_repeat| Informazioni sul bambino         | ${has_child} = 'yes'|
| text              | name        | Nome del bambino              |                     |
| decimal           | birthweight | Peso alla nascita del bambino       |                     |
| end repeat        |             |                           |                     |
```

## Funzionalità specifiche di rtSurvey

### Riepilogo del repeat

rtSurvey fornisce una vista riepilogativa dei repeat. Per personalizzare il riepilogo, usa un gruppo all'interno del repeat:

```
| type         | name         | label                                    |
|--------------|--------------|------------------------------------------|
| begin repeat | person_repeat|                                          |
| begin group  | person       | ${first_name} ${last_name} - ${age}      |
| text         | first_name   | Nome                               |
| text         | last_name    | Cognome                                |
| integer      | age          | Età                                      |
| end group    |              |                                          |
| end repeat   |              |                                          |
```

### Opzioni di appearance per i repeat

rtSurvey offre opzioni di appearance aggiuntive per i repeat:

- `appearance: field-list` - Visualizza tutte le domande in un repeat su una schermata
- `appearance: table-list` - Presenta i repeat in formato tabulare

```
| type         | name         | label            | appearance  |
|--------------|--------------|-------------------|-------------|
| begin repeat | child_repeat | Informazioni sul bambino | table-list  |
| text         | name         | Nome              |             |
| integer      | age          | Età               |             |
| end repeat   |              |                   |             |
```

### Repeat annidati

rtSurvey supporta i repeat annidati per strutture di dati complesse:

```
| type         | name           | label                |
|--------------|----------------|----------------------|
| begin repeat | household      | Famiglia            |
| text         | hh_name        | Nome della famiglia       |
| begin repeat | hh_member      | Membro della famiglia     |
| text         | member_name    | Nome del membro          |
| integer      | member_age     | Età del membro           |
| end repeat   |                |                      |
| end repeat   |                |                      |
```

## Best practice per l'utilizzo dei repeat in rtSurvey

1. Usa nomi ed etichette significativi per i repeat per migliorare l'analisi dei dati.
2. Considera l'utilizzo di conteggi dinamici dei repeat per ridurre gli errori di immissione dati.
3. Testa il tuo modulo approfonditamente, specialmente quando usi repeat annidati complessi.
4. Usa la funzione di riepilogo per aiutare gli enumeratori a navigare in lunghi elenchi di repeat.
5. Sii cauto con un gran numero di repeat, poiché possono influire sulle prestazioni del modulo.

## Gestione degli zero repeat

Per rappresentare zero repeat in rtSurvey:

1. Addestra gli enumeratori a eliminare il primo repeat se non necessario.
2. Usa conteggi dinamici dei repeat quando il numero esatto è noto.
3. Usa `relevant` per visualizzare condizionalmente i repeat.

## Considerazioni sull'esportazione dei dati

Quando si esportano dati da rtSurvey, i dati dei repeat vengono tipicamente appiattiti. Ogni istanza del repeat diventa una riga separata nei dati esportati, con i dati del modulo padre ripetuti per ogni istanza.

## Considerazioni sull'app mobile

- I repeat nell'app mobile di rtSurvey supportano la raccolta dati offline.
- Un gran numero di repeat può influire sulle prestazioni dell'app sui dispositivi di fascia bassa.

Usando efficacemente i repeat in rtSurvey, puoi creare sondaggi flessibili e potenti in grado di acquisire strutture dati complesse e gerarchiche, mantenendo un'interfaccia facile da usare per gli enumeratori.
