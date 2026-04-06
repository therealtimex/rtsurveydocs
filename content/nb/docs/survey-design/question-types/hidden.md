---
title: "Skjult"
description: "Skjulte felt lagrer verdier som aldri vises for respondenten — brukes til å sende kontekst, forhåndsutfylle data eller lagre mellomliggende resultater."
icon: "eye-slash"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 239
---

Et `hidden`-felt lagrer en verdi som **aldri vises for respondenten**. I motsetning til `calculate` (som beregner en verdi) brukes `hidden` til å overføre en **eksternt gitt verdi** — for eksempel en oppgave-ID, en hushold-ID sendt fra et annet system, eller en tellererkode injisert når skjemaet startes.

## Grunnleggende XLSForm-spesifikasjon

| type | name | label |
|------|------|-------|
| hidden | household_id | |

Etiketter er ikke nødvendige for skjulte felt siden ingenting gjengis på skjermen.

## Brukstilfeller

Skjulte felt brukes vanligvis for:

1. Sende en forhåndsoppgitt ID fra spørreundersøkelsesskjemaet (f.eks. hushold-ID, saksnummer, oppgavekode)
2. Lagre skjemaversjonen eller distribusjonens metadata
3. Injisere tellersspesifikk konfigurasjon ved skjemaoppstart
4. Overføre data fra et overordnet skjema til et underordnet skjema i koblede arbeidsflyter
5. Lagre en verdi avledet fra URL-parametere når skjemaet åpnes via en nettlenke

## Angi en standardverdi

Det vanligste mønsteret er å bruke `hidden` med et `default`-uttrykk slik at verdien settes når skjemaet åpnes:

| type | name | default |
|------|------|---------|
| hidden | deployment_code | 'ZONE_A_2024' |
| hidden | form_version | '3.1' |

## Referere til et skjult felt i beregninger

Skjulte verdier kan refereres til som ethvert annet felt ved hjelp av `${feltnavn}`:

| type | name | label | calculation |
|------|------|-------|-------------|
| hidden | zone_code | | |
| calculate | label_prefix | | concat('[', ${zone_code}, '] ') |
| note | intro | ${label_prefix} Velkommen til husholdningsundersøkelsen | |

## Bruke hidden med forhåndsutfylling / URL-parametere

Når du starter et webskjema via URL, kan du sende parametere som fyller ut skjulte felt. Dette lar deg forhåndslaste en hushold-ID eller oppgavekode uten at telleren skriver det inn:

```
https://your-server.com/form/FORMID?household_id=H00123&zone_code=NORTH
```

Feltet kalt `household_id` vil automatisk fylles ut med `H00123`.

## Beste praksis

1. Bruk `hidden` (ikke `calculate`) når verdien er **injisert eksternt** og ikke skal omberegnes.
2. Bruk `calculate` når verdien er **avledet fra andre felt** i skjemaet.
3. Angi alltid en `default` hvis det skjulte feltet må ha en verdi — et skjult felt uten standard vil være tomt.
4. Navngi skjulte felt tydelig for å skille dem (f.eks. prefiks med `_hidden_` eller bruk en konsekvent navnekonvensjon).

## Begrensninger

- Skjulte felt er inkludert i de eksporterte dataene som ethvert annet felt.
- De kan ikke vises betinget — de er alltid til stede (men usynlige).
- Hvis du trenger et felt som beregnes dynamisk, bruk `calculate` i stedet.
