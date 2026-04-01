---
title: "Gjentatte spørsmål"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 260
---

Repeats er en kraftig funksjon i rtSurvey som lar deg samle inn det samme settet med informasjon flere ganger innenfor en enkelt spørreundersøkelse. Dette er særlig nyttig for scenarioer som husholdningsundersøkelser, der du kan trenge å samle inn data om flere husholdningsmedlemmer.

## Grunnleggende repeat-struktur

For å lage en repeat i rtSurvey, bruk `begin repeat`- og `end repeat`-konstruksjonen:

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat |                      |
| text         | name         | Barnets navn         |
| decimal      | birthweight  | Barnets fødselsvekt  |
| select_one male_female | sex | Barnets kjønn       |
| end repeat   |              |                      |
```

I dette eksemplet kan brukeren samle inn informasjon om flere barn ved å legge til nye gjentagelser i skjemaet.

## Merking av repeats

Selv om `label`-kolonnen er valgfri for `begin repeat`, kan det å legge til en etikett forbedre navigasjonen:

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat | Barneinformasjon     |
| text         | name         | Barnets navn         |
| decimal      | birthweight  | Barnets fødselsvekt  |
| select_one male_female | sex | Barnets kjønn       |
| end repeat   |              |                      |
```

rtSurvey vil vise "Barneinformasjon" som en tittel for hver gjentakelsesinstans.

## Fast antall gjentagelser

For å angi et fast antall gjentagelser, bruk `repeat_count`-kolonnen:

```
| type         | name         | label                | repeat_count |
|--------------|--------------|----------------------|--------------|
| begin repeat | child_repeat | Barneinformasjon     | 3            |
| text         | name         | Barnets navn         |              |
| decimal      | birthweight  | Barnets fødselsvekt  |              |
| end repeat   |              |                      |              |
```

Dette vil opprette nøyaktig 3 barnegjentagelser.

## Dynamisk antall gjentagelser

rtSurvey støtter dynamiske antall gjentagelser basert på tidligere svar:

```
| type     | name           | label                          | repeat_count       |
|----------|----------------|--------------------------------|--------------------|
| integer  | num_hh_members | Antall husholdningsmedlemmer?  |                    |
| begin repeat | hh_member  | Husholdningsmedlem             | ${num_hh_members}  |
| text     | name           | Navn                           |                    |
| integer  | age            | Alder                          |                    |
| end repeat |              |                                |                    |
```

## Betingede repeats

Du kan bruke `relevant`-kolonnen for å betinget vise repeats:

```
| type              | name        | label                     | relevant           |
|-------------------|-------------|---------------------------|---------------------|
| select_one yes_no | has_child   | Bor det barn her?         |                     |
| begin repeat      | child_repeat| Barneinformasjon          | ${has_child} = 'yes'|
| text              | name        | Barnets navn              |                     |
| decimal           | birthweight | Barnets fødselsvekt       |                     |
| end repeat        |             |                           |                     |
```

## rtSurvey-spesifikke funksjoner

### Repeat-sammendrag

rtSurvey gir en sammendragsvisning av repeats. For å tilpasse sammendraget, bruk en gruppe inne i repeat-en:

```
| type         | name         | label                                    |
|--------------|--------------|------------------------------------------|
| begin repeat | person_repeat|                                          |
| begin group  | person       | ${first_name} ${last_name} - ${age}      |
| text         | first_name   | Fornavn                                  |
| text         | last_name    | Etternavn                                |
| integer      | age          | Alder                                    |
| end group    |              |                                          |
| end repeat   |              |                                          |
```

### Utseendealternativer for repeat

rtSurvey tilbyr ytterligere utseendealternativer for repeats:

- `appearance: field-list` — Viser alle spørsmål i en repeat på én skjerm
- `appearance: table-list` — Presenterer repeats i tabellformat

```
| type         | name         | label            | appearance  |
|--------------|--------------|-------------------|-------------|
| begin repeat | child_repeat | Barneinformasjon  | table-list  |
| text         | name         | Navn              |             |
| integer      | age          | Alder             |             |
| end repeat   |              |                   |             |
```

### Nestede repeats

rtSurvey støtter nestede repeats for komplekse datastrukturer:

```
| type         | name           | label                |
|--------------|----------------|----------------------|
| begin repeat | household      | Hushold              |
| text         | hh_name        | Husholdningsnavn     |
| begin repeat | hh_member      | Husholdningsmedlem   |
| text         | member_name    | Medlemsnavn          |
| integer      | member_age     | Medlemsalder         |
| end repeat   |                |                      |
| end repeat   |                |                      |
```

## Beste praksis for bruk av repeats i rtSurvey

1. Bruk meningsfulle navn og etiketter for repeats for å forbedre dataanalysen.
2. Vurder å bruke dynamiske antall gjentagelser for å redusere datainntastingsfeil.
3. Test skjemaet grundig, spesielt når du bruker komplekse nestede repeats.
4. Bruk sammendragsfunksjonen for å hjelpe tellere med å navigere i lange lister med repeats.
5. Vær forsiktig med store antall repeats, da de kan påvirke skjemaytelsen.

## Hensyn til dataeksport

Når du eksporterer data fra rtSurvey, flates repeat-data vanligvis ut. Hver repeat-instans blir en separat rad i de eksporterte dataene, med overordnet skjemas data gjentatt for hver instans.

## Hensyn til mobilapp

- Repeats i rtSurvey mobilapp støtter frakoblet datainnsamling.
- Store antall repeats kan påvirke appytelsen på lavere-ends enheter.
