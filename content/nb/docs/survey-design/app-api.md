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

AppAPI lar brukere laste inn systemmetadata fra appen ved hjelp av ulike metoder i FormEngine og DMView. Den gir tilgang til ulike datanøkler for å hente spesifikk informasjon fra appen.

I xlsform kan du bruke `pulldata()`-funksjonen med følgende syntaks:


{{< alert context="light" text="pulldata('app-api', 'data-key')" />}}

- `'app-api'`: Dette nøkkelordet informerer FormEngine om å laste data fra App API.
- `'data-key'`: Dette er nøkkelen til dataene du ønsker å laste fra App API.
- Hvis datanøkkelen er ugyldig eller ikke støttes, vil beregningen returnere "n/a".

Her er de støttede datanøklene du kan bruke med App-API:

`osPlatform`: Returnerer det gjeldende OS-navnet (Android eller iOS) og OS-versjonen. Webplattformer returnerer en tom verdi.

`appPlatform`: Returnerer appens plattformnavn, som er `rtSurvey`.

`appVersion`: Returnerer appens versjonsnavn.

`getDisplayWidth`: Returnerer enhetsskjermens bredde i piksler.

`getDisplayHeight`: Returnerer enhetsskjermens høyde i piksler.

`getScreenSize`: Returnerer enhetsskjermens størrelse i tommer.

`projectCode`: Returnerer den gjeldende prosjektkoden til nettstedet brukeren logger inn på.

`projectURL`: Returnerer den gjeldende prosjekt-URL-en til nettstedet brukeren logger inn på. Standard/tilbakefallsverdi er tom tekst ("").

`startingPoint`: Returnerer stien til punktet som starter skjemaet. Se "Skjemastartpunkt" for mer informasjon.

`serverTime`: Returnerer den best tilgjengelige tilnærmingen av dato og tid på serveren.

`user.[attributt]`: Returnerer gjeldende brukerattributter basert på den angitte attributtnøkkelen. Se "Brukerattributter"-tabellen for tilgjengelige attributtnøkler.

Kombiner attributtnøklene nedenfor med "user." i `pulldata()`-parametrene for å hente gjeldende brukerinformasjon. For eksempel, bruk `user.username`, `user.email`, osv.

| Attributtnøkkel      | Beskrivelse                          |
|----------------------|--------------------------------------|
| username             | Brukernavn til brukeren              |
| name                 | Fullt navn til brukeren              |
| staffCode            | Brukerens stab-kode                  |
| phone                | Telefonnummer til brukeren           |
| email                | E-postadresse til brukeren           |
| description          | Beskrivelsestekst i brukerinformasjon|
| organization_id      | Organisasjons-ID brukeren tilhører   |
| organization_name    | Organisasjonsnavn brukeren tilhører  |
| team_id              | Team-ID brukeren tilhører            |
| supervisor_id        | ID til brukerens overordnede         |
| is_supervisor        | 1 hvis brukeren er overordnet, 0 hvis ikke|

`instancePath`: Returnerer den gjeldende instansmappestien.

`appLanguage`: Returnerer gjeldende appspråk angitt i appens innstillinger (f.eks. vi, en).

`openArgs.[attributt]`: Returnerer det åpne-skjema-argumentet som sendes fra ActionButton (act_fill_form, act_get_instance). Standard/tilbakefallsverdi er tom tekst ("").

`primaryAppColor`: Henter appens primærfarge.

---

## Brukseksempler

### Lagre tellerens brukernavn og organisasjon

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | enumerator_name | | `pulldata('app-api', 'user.name')` |
| calculate | enumerator_org | | `pulldata('app-api', 'user.organization_name')` |
| calculate | enumerator_email | | `pulldata('app-api', 'user.email')` |

Bruk disse i note-etiketter for revisjonsformål:
```
note | interviewer_info | Intervjuer: ${enumerator_name} (${enumerator_org})
```

### Enhets- og skjerminformasjon

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | device_platform | | `pulldata('app-api', 'osPlatform')` |
| calculate | app_ver | | `pulldata('app-api', 'appVersion')` |
| calculate | screen_w | | `pulldata('app-api', 'getDisplayWidth')` |

Nyttig for feilsøking: eksporter `device_platform` og `app_ver` sammen med dataene for å identifisere hvilken enhetsversjon som ble brukt for hvert innsend.

### Servertid i stedet for enhetstid

Enheters klokker kan være feil. Bruk `serverTime` for et mer pålitelig tidsstempel:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | server_ts | | `pulldata('app-api', 'serverTime')` |

### Betinget logikk basert på brukerrolle

Vis en overordnet-kun seksjon bare til overordnede:

| type | name | label | relevant |
|------|------|-------|----------|
| calculate | is_supervisor | | `pulldata('app-api', 'user.is_supervisor')` |
| begin_group | supervisor_section | Overordnet gjennomgang | `${is_supervisor} = '1'` |
| text | supervisor_notes | Overordnets notater | |
| end_group | | | |

### Send argumenter fra en handlingsknapp

Når skjemaet startes fra en `act_fill_form`-handlingsknapp med tilpassede argumenter:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | passed_hh_id | | `pulldata('app-api', 'openArgs.household_id')` |
| calculate | passed_task | | `pulldata('app-api', 'openArgs.task_code')` |

Handlingsknappen må sende argumentene med samsvarende nøkler (f.eks. `household_id`, `task_code`).

### Bruke prosjektinformasjon

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | project | | `pulldata('app-api', 'projectCode')` |
| calculate | project_url | | `pulldata('app-api', 'projectURL')` |

---

## Notater

- Alle `pulldata('app-api', ...)`-kall evalueres når skjemaet åpnes og evalueres ikke dynamisk på nytt i løpet av sesjonen (bortsett fra `serverTime` og `now()`).
- Hvis en nøkkel ikke støttes eller dataene er utilgjengelige, returnerer funksjonen `'n/a'` (ikke tom streng — test med `!= 'n/a'` i stedet for `!= ''`).
- `openArgs`-verdier er bare tilgjengelige når skjemaet startes fra en handlingsknapp; de returnerer ellers en tom streng.
