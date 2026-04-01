---
title: "Meta"
description: "Meta-spørsmålstyper registrerer automatisk enhets-, teller- og tidinformasjon uten noen inndata fra respondenten."
icon: "info"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 237
---

Meta-spørsmålstyper er spesielle felt som fylles inn **automatisk** — respondenten ser dem aldri. De registrerer kontekst om innsendingen: når den ble samlet inn, hvilken enhet som ble brukt og hvem som samlet den inn. Legg dem til i `survey`-regnearket som enhver annen spørsmålstype; de vises rett og slett ikke på skjermen.

## Grunnleggende XLSForm-spesifikasjon

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| deviceid | deviceid | |

Etiketter er valgfrie for meta-felt siden de aldri vises.

---

## Tids-meta-felt

### `start`

Registrerer **datoen og klokkeslettet da skjemaet ble åpnet**. Lagret i ISO 8601-format (`YYYY-MM-DDTHH:MM:SS.sss+HH:MM`).

```
type    | name  | label
start   | start |
```

### `end`

Registrerer **datoen og klokkeslettet da skjemaet ble sendt inn**. Sammen med `start` kan du beregne tiden brukt på å fylle ut skjemaet:

```
type      | name          | calculation
calculate | duration_min  | (decimal-date-time(${end}) - decimal-date-time(${start})) * 1440
```

### `today`

Registrerer **gjeldende dato** (ingen tidskomponent). Lagret som `YYYY-MM-DD`. Nyttig når du bare trenger datoen uten det fulle tidsstempelet.

```
type  | name  | label
today | today |
```

---

## Enhets-meta-felt

### `deviceid`

Registrerer **den unike identifikatoren til enheten** brukt til datainnsamling. På Android er dette vanligvis IMEI eller Android ID. Nyttig for å spore hvilken enhet som sendte inn hvert skjema og oppdage dupliserte innsendinger fra samme enhet.

### `devicephonenum`

Registrerer **telefonnummeret til SIM-kortet** i enheten (hvis tilgjengelig). Kan være tomt hvis enheten ikke har SIM-kort eller hvis nummeret ikke er lagret på SIM-kortet.

### `simserial`

Registrerer **serienummeret til SIM-kortet** (ICCID). Nyttig for å identifisere hvilket SIM/operatør som ble brukt.

### `subscriberid`

Registrerer **IMSI (International Mobile Subscriber Identity)** — den unike abonnentidentifikatoren på SIM-kortet.

---

## Teller-meta-felt

### `username`

Registrerer **brukernavnet til den innloggede telleren** (kontoen brukt i rtSurvey-appen). Dette er den mest pålitelige måten å spore hvem som samlet inn hver innsending.

### `email`

Registrerer **e-postadressen til den innloggede telleren**.

### `phonenumber`

Registrerer **telefonnummeret knyttet til tellerens konto** (hvis konfigurert).

---

## Revisjonslogg

### `audit`

`audit`-meta-feltet aktiverer **detaljert revisjonslogging** — det registrerer en tidsstemplet logg over hvert spørsmål telleren besøkte, hvor lenge de brukte på hvert, og (valgfritt) GPS-posisjonen på hvert trinn. Revisjonsloggen lagres som en separat `audit.csv`-fil ved siden av hver innsending.

```
type  | name  | parameters
audit | audit | location-priority=balanced location-min-interval=30 location-max-age=60
```

#### Revisjonsparametere

| Parameter | Beskrivelse |
|-----------|-------------|
| `location-priority` | GPS-nøyaktighetsnivå: `no-gps`, `low-power`, `balanced`, `high-accuracy` |
| `location-min-interval` | Minimum sekunder mellom plasseringsregistreringer |
| `location-max-age` | Maksimal alder (sekunder) for en bufret plassering å akseptere |

Revisjonsloggen registrerer:
- Spørsmålsnavn og hendelsestype (`question`, `form.start`, `form.exit`, `form.save`, `form.finalize`)
- Start- og slutttidsstempler for hver hendelse
- GPS-koordinater (hvis `location-priority` er satt)

{{% alert icon=" " context="warning" %}}
`audit`-feltet genererer en separat fil per innsending. Sørg for at datapipelinen din behandler både hoved-skjemadataene og revisjons-CSV-en.
{{% /alert %}}

---

## Komplett eksempel

En typisk husholdningsundersøkelse kan inkludere alle tids- og teller-meta-felt:

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| today | today | |
| deviceid | deviceid | |
| username | username | |
| email | email | |
| audit | audit | |
| text | household_id | Hushold-ID |
| ... | ... | ... |

---

## Beste praksis

1. Inkluder alltid `start` og `end` — de er gratis, automatiske og uvurderlige for kvalitetsovervåking.
2. Inkluder alltid `username` for å spore tellere.
3. Inkluder `deviceid` når du ønsker å oppdage dupliserte innsendinger eller spore feltenheter.
4. Bruk `audit` i høyansvarligsundersøkelser der du trenger å verifisere at tellere faktisk besøkte hvert spørsmål.
5. SIM-relaterte felt (`simserial`, `subscriberid`, `devicephonenum`) er bare pålitelige på Android-enheter med aktive SIM-kort — hopp over dem for nettbrett-kun distribusjoner.

---

## Begrensninger

- Alle meta-felt er **skrivebeskyttede** — de kan ikke refereres til eller endres av andre beregninger.
- `username` og `email` krever at telleren er logget inn; de vil være tomme for anonyme innsendinger.
- SIM/telefon-meta-felt kan returnere tomme verdier på Wi-Fi-kun nettbrett og noen Android-versjoner på grunn av tillatelsesrestriksjoner.
