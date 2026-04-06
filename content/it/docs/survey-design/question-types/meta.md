---
title: "Meta"
description: "I tipi di domanda meta acquisiscono automaticamente informazioni sul dispositivo, sull'enumeratore e sui tempi senza alcun input dal rispondente."
icon: "info"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 237
---

I tipi di domanda meta sono campi speciali che vengono compilati **automaticamente** — il rispondente non li vede mai. Acquisiscono il contesto dell'invio: quando è stato raccolto, quale dispositivo è stato usato e chi lo ha raccolto. Aggiungili nel foglio di lavoro `survey` come qualsiasi altro tipo di domanda; semplicemente non appaiono sullo schermo.

## Specifica XLSForm di base

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| deviceid | deviceid | |

Le etichette sono opzionali per i campi meta poiché non vengono mai visualizzate.

---

## Campi meta di temporizzazione

### `start`

Registra la **data e l'ora in cui il modulo è stato aperto**. Memorizzato in formato ISO 8601 (`YYYY-MM-DDTHH:MM:SS.sss+HH:MM`).

```
type    | name  | label
start   | start |
```

### `end`

Registra la **data e l'ora in cui il modulo è stato inviato**. Insieme a `start`, puoi calcolare il tempo trascorso a compilare il modulo:

```
type      | name          | calculation
calculate | duration_min  | (decimal-date-time(${end}) - decimal-date-time(${start})) * 1440
```

### `today`

Registra la **data corrente** (senza componente oraria). Memorizzato come `YYYY-MM-DD`. Utile quando hai bisogno solo della data senza il timestamp completo.

```
type  | name  | label
today | today |
```

---

## Campi meta del dispositivo

### `deviceid`

Registra l'**identificatore univoco del dispositivo** usato per la raccolta dati. Su Android questo è tipicamente l'IMEI o l'Android ID. Utile per tracciare quale dispositivo ha inviato ciascun modulo e rilevare invii duplicati dallo stesso dispositivo.

```
type      | name     | label
deviceid  | deviceid |
```

### `devicephonenum`

Registra il **numero di telefono della scheda SIM** nel dispositivo (se disponibile). Potrebbe essere vuoto se il dispositivo non ha una SIM o se il numero non è memorizzato sulla SIM.

```
type           | name          | label
devicephonenum | devicephonenum |
```

### `simserial`

Registra il **numero di serie della scheda SIM** (ICCID). Utile per identificare quale SIM/operatore è stato usato.

```
type      | name      | label
simserial | simserial |
```

### `subscriberid`

Registra l'**IMSI (International Mobile Subscriber Identity)** — l'identificatore univoco dell'abbonato sulla scheda SIM.

```
type         | name        | label
subscriberid | subscriberid |
```

---

## Campi meta dell'enumeratore

### `username`

Registra il **nome utente dell'enumeratore connesso** (l'account usato nell'app rtSurvey). Questo è il modo più affidabile per tracciare chi ha raccolto ciascun invio.

```
type     | name     | label
username | username |
```

### `email`

Registra l'**indirizzo email dell'enumeratore connesso**.

```
type  | name  | label
email | email |
```

### `phonenumber`

Registra il **numero di telefono associato all'account dell'enumeratore** (se configurato).

```
type        | name       | label
phonenumber | phonenumber |
```

---

## Registro di audit

### `audit`

Il campo meta `audit` abilita la **registrazione di audit dettagliata** — registra un log con timestamp di ogni domanda visitata dall'enumeratore, quanto tempo hanno trascorso su ciascuna, e (opzionalmente) la loro posizione GPS a ogni passaggio. Il log di audit viene salvato come file `audit.csv` separato accanto a ciascun invio.

```
type  | name  | parameters
audit | audit | location-priority=balanced location-min-interval=30 location-max-age=60
```

#### Parametri di audit

| Parametro | Descrizione |
|-----------|-------------|
| `location-priority` | Livello di precisione GPS: `no-gps`, `low-power`, `balanced`, `high-accuracy` |
| `location-min-interval` | Secondi minimi tra le acquisizioni di posizione |
| `location-max-age` | Età massima (secondi) di una posizione memorizzata nella cache da accettare |

Il log di audit acquisisce:
- Nome della domanda e tipo di evento (`question`, `form.start`, `form.exit`, `form.save`, `form.finalize`)
- Timestamp di inizio e fine per ogni evento
- Coordinate GPS (se `location-priority` è impostato)

{{% alert icon=" " context="warning" %}}
Il campo `audit` genera un file separato per invio. Assicurati che la tua pipeline di dati elabori sia i dati principali del modulo che il CSV di audit.
{{% /alert %}}

---

## Esempio completo

Un tipico sondaggio familiare potrebbe includere tutti i campi meta di temporizzazione ed enumeratore:

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| today | today | |
| deviceid | deviceid | |
| username | username | |
| email | email | |
| audit | audit | |
| text | household_id | ID famiglia |
| ... | ... | ... |

---

## Best practice

1. Includi sempre `start` e `end` — sono gratuiti, automatici e preziosi per il monitoraggio della qualità.
2. Includi sempre `username` per tracciare gli enumeratori.
3. Includi `deviceid` quando vuoi rilevare invii duplicati o tracciare i dispositivi sul campo.
4. Usa `audit` nei sondaggi ad alta responsabilità dove devi verificare che gli enumeratori abbiano effettivamente visitato ogni domanda.
5. I campi relativi alla SIM (`simserial`, `subscriberid`, `devicephonenum`) sono affidabili solo su dispositivi Android con schede SIM attive — saltali per i deployment solo su tablet.

---

## Limitazioni

- Tutti i campi meta sono **di sola lettura** — non possono essere referenziati o modificati da altri calcoli.
- `username` e `email` richiedono che l'enumeratore sia connesso; saranno vuoti per gli invii anonimi.
- I campi meta SIM/telefono possono restituire valori vuoti su tablet solo Wi-Fi e alcune versioni di Android a causa di restrizioni sui permessi.
