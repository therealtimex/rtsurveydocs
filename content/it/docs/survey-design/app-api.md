---
title: "App API"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 300
---

L'AppAPI consente agli utenti di caricare metadati di sistema dall'app usando diversi metodi nel FormEngine e nel DMView. Fornisce accesso a varie chiavi di dati per recuperare informazioni specifiche dall'app.

Nell'XLSForm, puoi usare la funzione `pulldata()` con la seguente sintassi:


{{< alert context="light" text="pulldata('app-api', 'data-key')" />}}

- `'app-api'`: Questa parola chiave informa il FormEngine di caricare i dati dall'App API.
- `'data-key'`: Questa è la chiave dei dati che vuoi caricare dall'App API.
- Se la chiave dati non è valida o non è supportata, il calcolo restituirà "n/a".

Ecco le chiavi dati supportate che puoi usare con l'App-API:

`osPlatform`: Restituisce il nome del sistema operativo corrente (Android o iOS) e la versione del sistema operativo. Le piattaforme web restituiranno un valore vuoto.

`appPlatform`: Restituisce il nome della piattaforma dell'app, che è `rtSurvey`.

`appVersion`: Restituisce il nome della versione dell'app.

`getDisplayWidth`: Restituisce la larghezza dello schermo del dispositivo in pixel.

`getDisplayHeight`: Restituisce l'altezza dello schermo del dispositivo in pixel.

`getScreenSize`: Restituisce la dimensione dello schermo del dispositivo in pollici.

`projectCode`: Restituisce il codice del progetto corrente del sito a cui l'utente ha effettuato l'accesso.

`projectURL`: Restituisce l'URL del progetto corrente del sito a cui l'utente ha effettuato l'accesso. Il valore predefinito/fallback è testo vuoto ("").

`startingPoint`: Restituisce il percorso del punto che avvia il modulo. Per ulteriori dettagli, vedi "Punto di partenza del modulo".

`serverTime`: Restituisce la migliore approssimazione disponibile della data e dell'ora sul server.

`user.[attribute]`: Restituisce gli attributi dell'utente corrente in base alla chiave attributo specificata. Per le chiavi attributo disponibili, vedi la tabella "Attributi utente".

Combina le chiavi attributo seguenti con "user." nei parametri di `pulldata()` per recuperare le informazioni sull'utente corrente. Ad esempio, usa `user.username`, `user.email`, ecc.

| Chiave attributo     | Descrizione                                  |
|----------------------|----------------------------------------------|
| username             | Nome utente dell'utente                       |
| name                 | Nome completo dell'utente                    |
| staffCode            | Codice personale dell'utente                 |
| phone                | Numero di telefono dell'utente               |
| email                | Indirizzo email dell'utente                  |
| description          | Testo di descrizione nelle informazioni utente|
| organization_id      | ID dell'organizzazione a cui appartiene l'utente|
| organization_name    | Nome dell'organizzazione a cui appartiene l'utente|
| team_id              | ID del team a cui appartiene l'utente        |
| supervisor_id        | ID del supervisore dell'utente               |
| is_supervisor        | 1 se l'utente è un supervisore, 0 altrimenti |

`instancePath`: Restituisce il percorso della cartella dell'istanza corrente.

`appLanguage`: Restituisce la lingua dell'app corrente impostata nelle impostazioni dell'app (es. vi, en).

`openArgs.[attribute]`: Restituisce l'argomento di apertura modulo passato dall'ActionButton (act_fill_form, act_get_instance). Il valore predefinito/fallback è testo vuoto ("").

`primaryAppColor`: Recupera il colore primario dell'app.

---

## Esempi di utilizzo

### Memorizza il nome utente e l'organizzazione dell'intervistatore

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | enumerator_name | | `pulldata('app-api', 'user.name')` |
| calculate | enumerator_org | | `pulldata('app-api', 'user.organization_name')` |
| calculate | enumerator_email | | `pulldata('app-api', 'user.email')` |

Usali nelle etichette note per scopi di audit:
```
note | interviewer_info | Intervistatore: ${enumerator_name} (${enumerator_org})
```

### Informazioni sul dispositivo e sullo schermo

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | device_platform | | `pulldata('app-api', 'osPlatform')` |
| calculate | app_ver | | `pulldata('app-api', 'appVersion')` |
| calculate | screen_w | | `pulldata('app-api', 'getDisplayWidth')` |

Utile per la risoluzione dei problemi: esporta `device_platform` e `app_ver` insieme ai tuoi dati per identificare quale versione del dispositivo è stata usata per ogni invio.

### Ora del server invece dell'ora del dispositivo

Gli orologi dei dispositivi possono essere sbagliati. Usa `serverTime` per un timestamp più affidabile:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | server_ts | | `pulldata('app-api', 'serverTime')` |

### Logica condizionale basata sul ruolo dell'utente

Mostra una sezione solo per supervisori ai supervisori:

| type | name | label | relevant |
|------|------|-------|----------|
| calculate | is_supervisor | | `pulldata('app-api', 'user.is_supervisor')` |
| begin_group | supervisor_section | Revisione supervisore | `${is_supervisor} = '1'` |
| text | supervisor_notes | Note del supervisore | |
| end_group | | | |

### Passa argomenti da un pulsante di azione

Quando il modulo viene avviato da un pulsante di azione `act_fill_form` con argomenti personalizzati:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | passed_hh_id | | `pulldata('app-api', 'openArgs.household_id')` |
| calculate | passed_task | | `pulldata('app-api', 'openArgs.task_code')` |

Il pulsante di azione deve passare gli argomenti con chiavi corrispondenti (es. `household_id`, `task_code`).

### Utilizzo delle informazioni sul progetto

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | project | | `pulldata('app-api', 'projectCode')` |
| calculate | project_url | | `pulldata('app-api', 'projectURL')` |

---

## Note

- Tutte le chiamate `pulldata('app-api', ...)` vengono valutate quando il modulo viene aperto e non vengono rivalutate dinamicamente durante la sessione (eccetto `serverTime` e `now()`).
- Se una chiave non è supportata o il dato non è disponibile, la funzione restituisce `'n/a'` (non stringa vuota — testa con `!= 'n/a'` piuttosto che `!= ''`).
- I valori di `openArgs` sono disponibili solo quando il modulo viene avviato da un pulsante di azione; altrimenti restituiscono stringa vuota.
