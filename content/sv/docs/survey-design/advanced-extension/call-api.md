---
title: "Anropa API"
description: "Call API låter din undersökning hämta data från en extern webbtjänst och använda svaret för att fylla i fält eller validera svar."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 294
---

Funktionen **Call API** låter ett undersökningsfält göra en HTTP-förfrågan till en extern tjänst och använda svaret för att fylla i ett beräknat värde eller validera användarinmatning. Detta möjliggör realtidsuppslag, ID-verifiering, streckkodsuppslag och alla andra serversideskontroller under datainsamling.

Det finns två funktioner:

- `callapi()` — hämtar ett värde från ett API och lagrar det i ett `calculate`- eller `text`-fält
- `callapi-verify()` — anropar ett API och blockerar framsteg om svaret inte matchar det förväntade värdet (används i `constraint`)

---

## `callapi()` — Hämta och lagra ett API-svar

### Syntax

Placera `callapi()` i **`calculation`**-kolumnen för ett `calculate`- eller `text`-fält:

```
callapi(method, url, allowed_auto, max_retry, no_overwrite, extract_expr, timeout, lifetime, response_q, call_type, post_body)
```

### Parametrar

| # | Parameter | Beskrivning |
|---|-----------|-------------|
| 1 | `method` | HTTP-metod: `'GET'` eller `'POST'` |
| 2 | `url` | API-slutpunktens URL |
| 3 | `allowed_auto` | `1` för att anropa automatiskt när fältet nås; `0` för att kräva en manuell utlösarknapp |
| 4 | `max_retry` | Maximalt antal försök vid misslyckande |
| 5 | `no_overwrite` | `1` för att behålla det befintliga värdet om fältet redan har ett; `0` för att alltid skriva över |
| 6 | `extract_expr` | JSONPath-uttryck för att extrahera det önskade värdet från svaret (t.ex. `$.data.name`) |
| 7 | `timeout` | Tidsgräns för förfrågan i millisekunder |
| 8 | `lifetime` | Hur länge (ms) det cachade svaret förblir giltigt innan det hämtas igen |
| 9 | `response_q` | Namn på ett fält för att lagra den råa HTTP-svarskoden (t.ex. `${response_status}`) |
| 10 | `call_type` | *(Valfritt)* Speciellt anropsläge: `'lazy-upload'` eller `'lazy-upload-multiple'` |
| 11 | `post_body` | *(Valfritt)* POST-kroppssträng. Referera till formulärfält med `##fieldname##` |

### Exempel: GET-förfrågan för att söka upp ett hushåll via ID

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| text | household_id | Hushålls-ID | | |
| calculate | hh_name | | callapi | `callapi('GET', concat('https://api.example.com/households/', ${household_id}), 1, 3, 0, '$.name', 10000, 0, '')` |
| note | hh_display | Hushåll: ${hh_name} | | |

### Exempel: POST-förfrågan med JSON-kropp

```
callapi('POST', 'https://api.example.com/lookup', 1, 2, 0, '$.result.value', 15000, 0, '', '', '{"id": "##household_id##"}')
```

I `post_body`, använd `##fieldname##` för att injicera det aktuella värdet av ett formulärfält.

### Utseende: `callapi`

Lägg till `callapi` i `appearance`-kolumnen för fältet för att aktivera API-anropsintegration:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | api_result | | callapi | `callapi('GET', ...)` |

När `allowed_auto` är `0` visar rtSurvey en **"Hämta"-knapp** som räknaren trycker på manuellt.

---

## `callapi-verify()` — Validera ett värde mot ett API

`callapi-verify()` blockerar inlämning av ett fält tills ett API bekräftar att det angivna värdet är giltigt. Använd det i **`constraint`**-kolumnen.

### Syntax

```
callapi-verify(method, url, extract_expr, match_expr, timeout, constraint_mode, post_body, message)
```

### Parametrar

| # | Parameter | Beskrivning |
|---|-----------|-------------|
| 1 | `method` | HTTP-metod: `'GET'` eller `'POST'` |
| 2 | `url` | Verifierings-API:ets slutpunkt |
| 3 | `extract_expr` | JSONPath för att extrahera det förväntade värdet från svaret |
| 4 | `match_expr` | Uttryck som jämför extraherat värde med fältvärdet (t.ex. `$.status = 'valid'`) |
| 5 | `timeout` | Tidsgräns för förfrågan i millisekunder |
| 6 | `constraint_mode` | `'soft'` för enbart varning; `'hard'` för att blockera framsteg |
| 7 | `post_body` | *(Valfritt)* POST-kropp med `##fieldname##`-substitutioner |
| 8 | `message` | *(Valfritt)* Felmeddelande. Stöder flera språk: `<en>Invalid!</en><vi>Không hợp lệ!</vi>` |

### Exempel: Verifiera en streckkod mot ett tillgångsregister

| type | name | label | appearance | constraint | constraint_message |
|------|------|-------|------------|------------|-------------------|
| barcode | asset_code | Skanna tillgångsstreckoden | callapi-verify | `callapi-verify('POST', 'https://api.example.com/assets/verify', '$.valid', ". = 'true'", 10000, 'hard', '{"code": "##asset_code##"}')` | Tillgången hittades inte i registret |

### Utseende: `callapi-verify(...)`

`appearance`-kolumnen på ett fält med `callapi-verify()` i constraint bör innehålla `callapi-verify(params)` eller `callapi-verify(dynamicParams)` för att signalera till rtSurvey att det här fältet använder API-verifiering.

---

## Använda App API-data tillsammans med callapi

Kombinera `callapi()` med `pulldata('app-api', 'user.token')` för att injicera den autentiserade användarens token i din API-förfrågan:

```
callapi('POST', 'https://api.example.com/data', 1, 2, 0, '$.value', 10000, 0, '', '',
  concat('{"token":"', pulldata('app-api','user.token'), '","id":"##item_id##"}'))
```

## Bästa praxis

1. Ange alltid en rimlig `timeout` (5000–15000 ms) — använd inte 0 eller mycket höga värden.
2. Sätt `allowed_auto=0` för verifieringar som räknaren bör utlösa medvetet (t.ex. ID-kontroller).
3. Sätt `no_overwrite=1` när fältet kan redigeras senare och du inte vill att ny hämtning ska skriva över manuella korrigeringar.
4. Använd `extract_expr` med ett specifikt JSONPath snarare än att förlita dig på råsvarstext.
5. Testa API-anrop i offlineläge — callapi misslyckas graciöst och visar ett fel, men formuläret bör fortfarande kunna slutföras för icke-kritiska fält.

## Begränsningar

- Kräver nätverksanslutning vid tidpunkten för anropet — anrop misslyckas när enheten är offline.
- API-svar måste vara JSON — XML- eller ren textsvar kräver ytterligare tolkning.
- Hög anropsfrekvens (t.ex. ett API-anrop per upprepningsinstans) kan sakta ned formulärnavigering.
