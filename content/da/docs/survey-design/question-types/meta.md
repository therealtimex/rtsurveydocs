---
title: "Meta"
description: "Meta-spørgsmålstyper fanger automatisk enheds-, interviewer- og tidsinformation uden input fra respondenten."
icon: "info"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 237
---

Meta-spørgsmålstyper er specielle felter, der udfyldes **automatisk** — respondenten ser dem aldrig. De fanger kontekst om indsendelsen: hvornår den blev indsamlet, hvilken enhed der blev brugt, og hvem der indsamlede den. Tilføj dem i regnearket `survey` ligesom enhver anden spørgsmålstype; de vises simpelthen ikke på skærmen.

## Grundlæggende XLSForm-specifikation

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| deviceid | deviceid | |

Labels er valgfrie for metafelter, da de aldrig vises.

---

## Tidsmeta-felter

### `start`

Registrerer **dato og tid, da formularen blev åbnet**. Gemmes i ISO 8601-format (`YYYY-MM-DDTHH:MM:SS.sss+HH:MM`).

```
type    | name  | label
start   | start |
```

### `end`

Registrerer **dato og tid, da formularen blev indsendt**. Sammen med `start` kan du beregne den tid, der bruges på at udfylde formularen:

```
type      | name          | calculation
calculate | duration_min  | (decimal-date-time(${end}) - decimal-date-time(${start})) * 1440
```

### `today`

Registrerer **den aktuelle dato** (ingen tidskomponent). Gemmes som `YYYY-MM-DD`. Nyttigt, når du kun har brug for datoen uden det fulde tidsstempel.

```
type  | name  | label
today | today |
```

---

## Enhedsmetafelter

### `deviceid`

Registrerer den **unikke identifikator for enheden**, der bruges til dataindsamling. På Android er dette typisk IMEI eller Android ID. Nyttigt til sporing af, hvilken enhed der indsendte hver formular og til opdagelse af duplikatindsendelser fra den samme enhed.

```
type      | name     | label
deviceid  | deviceid |
```

### `devicephonenum`

Registrerer **telefonnummeret på SIM-kortet** i enheden (hvis tilgængeligt). Kan være tomt, hvis enheden ikke har SIM-kort, eller hvis nummeret ikke er gemt på SIM-kortet.

```
type           | name          | label
devicephonenum | devicephonenum |
```

### `simserial`

Registrerer **serienummeret på SIM-kortet** (ICCID). Nyttigt til identifikation af, hvilken SIM/mobilselskab der blev brugt.

```
type      | name      | label
simserial | simserial |
```

### `subscriberid`

Registrerer **IMSI (International Mobile Subscriber Identity)** — den unikke abonnentidentifikator på SIM-kortet.

```
type         | name        | label
subscriberid | subscriberid |
```

---

## Interviewermetafelter

### `username`

Registrerer **brugernavnet på den indloggede interviewer** (kontoen der bruges i rtSurvey-appen). Dette er den mest pålidelige måde at spore, hvem der indsamlede hver indsendelse.

```
type     | name     | label
username | username |
```

### `email`

Registrerer **e-mailadressen på den indloggede interviewer**.

```
type  | name  | label
email | email |
```

### `phonenumber`

Registrerer **telefonnummeret tilknyttet interviewerens konto** (hvis konfigureret).

```
type        | name       | label
phonenumber | phonenumber |
```

---

## Revisionslog

### `audit`

Metafeltet `audit` muliggør **detaljeret revisionslogning** — det registrerer en tidsstemplet log over hvert spørgsmål, intervieweren besøgte, hvor lang tid de brugte på hvert, og (valgfrit) deres GPS-placering på hvert trin. Revisionsloggen gemmes som en separat `audit.csv`-fil ved siden af hver indsendelse.

```
type  | name  | parameters
audit | audit | location-priority=balanced location-min-interval=30 location-max-age=60
```

#### Revisionsparametre

| Parameter | Beskrivelse |
|-----------|-------------|
| `location-priority` | GPS-nøjagtighedsniveau: `no-gps`, `low-power`, `balanced`, `high-accuracy` |
| `location-min-interval` | Minimale sekunder mellem placeringsregistreringer |
| `location-max-age` | Maksimal alder (sekunder) af en cachet placering, der accepteres |

Revisionsloggen fanger:
- Spørgsmålsnavn og hændelsestype (`question`, `form.start`, `form.exit`, `form.save`, `form.finalize`)
- Start- og sluttidsstempler for hver hændelse
- GPS-koordinater (hvis `location-priority` er angivet)

{{% alert icon=" " context="warning" %}}
Feltet `audit` genererer en separat fil pr. indsendelse. Sørg for, at din datapipeline behandler både de primære formulardata og revisions-CSV-filen.
{{% /alert %}}

---

## Komplet eksempel

En typisk husholdningsundersøgelse kan inkludere alle tids- og interviewermetafelter:

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| today | today | |
| deviceid | deviceid | |
| username | username | |
| email | email | |
| audit | audit | |
| text | household_id | Husholdnings-ID |
| ... | ... | ... |

---

## Bedste praksis

1. Inkluder altid `start` og `end` — de er gratis, automatiske og uvurderlige til kvalitetsovervågning.
2. Inkluder altid `username` til sporing af interviewere.
3. Inkluder `deviceid`, når du vil opdage duplikatindsendelser eller spore feltenheder.
4. Brug `audit` i undersøgelser med høj ansvarlighed, hvor du skal verificere, at interviewere rent faktisk besøgte hvert spørgsmål.
5. SIM-relaterede felter (`simserial`, `subscriberid`, `devicephonenum`) er kun pålidelige på Android-enheder med aktive SIM-kort — undlad dem til tablet-kun udrulninger.

---

## Begrænsninger

- Alle metafelter er **skrivebeskyttede** — de kan ikke refereres til eller ændres af andre beregninger.
- `username` og `email` kræver, at intervieweren er logget ind; de vil være tomme ved anonyme indsendelser.
- SIM/telefon-metafelter kan returnere tomme værdier på Wi-Fi-kun tablets og nogle Android-versioner på grund af tilladelsesrestriktioner.
