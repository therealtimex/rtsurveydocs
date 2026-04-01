---
title: "Text"
description: "Tipo di domanda a risposta testuale libera in rtSurvey"
icon: "text_fields"
date: "2024-07-01T12:00:00+01:00"
lastmod: "2024-07-01T12:00:00+01:00"
draft: false
toc: true
weight: 221
---

Il tipo di domanda `text` raccoglie una risposta a testo libero — qualsiasi stringa di caratteri. È il tipo di input più flessibile e viene usato per nomi, indirizzi, descrizioni, codici, e tutto ciò che non si adatta a un tipo più specifico.

rtSurvey estende anche `text` con **widget di input temporale** che consentono l'inserimento preciso dell'ora con un selettore dell'orologio.

## Specifica XLSForm di base

| type | name | label |
|------|------|-------|
| text | respondent_name | Nome completo del rispondente |
| text | address | Indirizzo di residenza |

Per ulteriori dettagli sul tipo text standard di XLSForm, vedere la [specifica XLSForm](https://xlsform.org/en/#question-types).

## Utilizzi

Le domande text vengono usate per:

1. Nomi, indirizzi, descrizioni libere
2. Commenti o feedback a risposta aperta
3. Codici, ID o numeri di riferimento che non si adattano a integer/decimal
4. Raccolta di valori temporali con le estensioni di input temporale di rtSurvey
5. Campi di testo con completamento automatico (tramite `search-autocomplete-noedit-v2()`)

## Opzioni di appearance standard

| Appearance | Descrizione |
|------------|-------------|
| *(nessuna)* | Input di testo a riga singola |
| `multiline` | Area di testo a più righe — ideale per testo libero più lungo sul web |

## Estensioni di input temporale di rtSurvey

rtSurvey estende `text` con un **widget selettore dell'orologio** per raccogliere valori temporali. Queste opzioni di appearance visualizzano un'icona dell'orologio che l'enumeratore può toccare per selezionare ore, minuti, secondi o millisecondi.

### Varianti di appearance

| Appearance | Descrizione |
|------------|-------------|
| `inline` | Icona dell'orologio visualizzata accanto al campo |
| `inline colors("RRGGBB")` | Icona dell'orologio con colore esadecimale personalizzato |
| `inline-1line` | Orologio visualizzato in formato a riga singola compatto |
| `inline-1line-RRGGBB` | A riga singola con colore personalizzato dell'icona (esadecimale, senza `#`) |
| `inline-1line colors("RRGGBB","RRGGBB")` | A riga singola con due colori |
| `inline-onlyresult` | L'icona dell'orologio scompare dopo la selezione; viene mostrato solo il valore |
| `inline-onlyresult colors("RRGGBB")` | Come sopra, con colore personalizzato dell'icona |

### Token di formato temporale

Aggiungi una stringa di formato tra parentesi per controllare quali componenti temporali vengono mostrati:

| Stringa di formato | Visualizza |
|---------------|----------|
| `inline-[%H:%M]` | Ore e minuti (24 ore) |
| `inline-[%h:%M]` | Ore e minuti (12 ore) |
| `inline-[%H:%M:%S]` | Ore, minuti, secondi (24 ore) |
| `inline-[%h:%M:%S]` | Ore, minuti, secondi (12 ore) |
| `inline-[%H:%M:%3]` | Ore, minuti, millisecondi |
| `inline-[%M:%S]` | Solo minuti e secondi |
| `inline-[%M:%3]` | Solo minuti e millisecondi |
| `inline-[%S]` | Solo secondi |
| `inline-[%3]` | Solo millisecondi |
| `inline-[%H]` | Solo ore (24 ore) |
| `inline-[%h]` | Solo ore (12 ore) |

### Esempio: Registra la durata di un'attività in minuti e secondi

| type | name | label | appearance |
|------|------|-------|------------|
| text | task_duration | Tempo impiegato per completare l'attività | `inline-[%M:%S]` |

### Esempio: Registra l'ora di un evento in formato 24 ore con colore personalizzato

| type | name | label | appearance |
|------|------|-------|------------|
| text | event_time | Ora dell'evento | `inline-1line colors("0099FF")` |

## Formato dei dati

I dati text vengono memorizzati ed esportati come stringa semplice. Per gli input temporali che usano il widget di orologio inline, il valore viene memorizzato nel formato corrispondente alla stringa di formato scelta (es. `14:32` per `%H:%M`).

## Vincoli e validazione

Applica vincoli per imporre formato, lunghezza o pattern:

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| text | name | Nome completo | `string-length(.) >= 2` | Il nome deve avere almeno 2 caratteri |
| text | code | Codice di riferimento | `regex(., '^[A-Z]{2}[0-9]{4}$')` | Inserisci 2 lettere maiuscole seguite da 4 cifre |
| text | phone | Numero di telefono | `regex(., '^[0-9]{9,15}$')` | Inserisci un numero di telefono valido |

## Best practice

1. Usa tipi più specifici (`integer`, `decimal`, `date`) quando i dati hanno una struttura nota — questo previene voci non valide e semplifica l'analisi.
2. Aggiungi `constraint` con `string-length()` o `regex()` per validare codici o ID.
3. Usa l'appearance `multiline` per le domande a risposta aperta in cui i rispondenti potrebbero scrivere diverse frasi.
4. Per la raccolta di orari, scegli i token di formato temporale che corrispondono alla precisione richiesta dalla tua analisi — raccogliere i millisecondi quando hai bisogno solo dei minuti spreca lo sforzo degli enumeratori.

## Supporto della piattaforma

Il tipo di domanda text e tutte le appearance di input temporale sono supportati su piattaforme iOS, Android e web.

## Limitazioni

- Le risposte testuali sono in formato libero — non è disponibile alcun controllo ortografico o vincolo di vocabolario integrato oltre ai pattern regex.
- Il widget di orologio inline è un'estensione di rtSurvey e non fa parte della specifica XLSForm standard.
