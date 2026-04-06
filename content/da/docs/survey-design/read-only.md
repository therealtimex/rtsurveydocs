---
title: "Skrivebeskyttet"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 287
---

Skrivebeskyttede felter i rtSurvey giver dig mulighed for at vise information, som ikke kan redigeres af respondenten. Denne funktion er særligt nyttig til visning af forudfyldte data, beregnede resultater eller information, der skal forblive konstant under hele undersøgelsen.

## Grundlæggende brug

For at gøre et felt skrivebeskyttet skal du bruge kolonnen `read_only` i din XLSForm:

```
| type    | name | label                 | read_only | default |
|---------|------|----------------------|-----------|---------|
| integer | num  | Patientnummeret er:   | yes       | 5       |
```

I dette eksempel er patientnummeret sat til 5 og kan ikke ændres af respondenten.

## Kombination af skrivebeskyttet med standardværdier

Skrivebeskyttede felter bruges ofte i kombination med standardværdier til at vise forudbestemt eller beregnet information:

```
| type    | name     | label               | read_only | default        |
|---------|----------|---------------------|-----------|----------------|
| text    | username | Logget ind som:     | yes       | ${current_user}|
| date    | today    | Dags dato:          | yes       | today()        |
```

## rtSurvey-specifikke funktioner

### Betinget skrivebeskyttet

rtSurvey udvider skrivebeskyttet-funktionaliteten med betinget logik:

```
| type    | name     | label           | read_only                |
|---------|----------|-----------------|--------------------------|
| integer | age      | Alder:          | ${role} = 'viewer'       |
| text    | comments | Kommentarer:    | selected(${status}, 'closed') |
```

### Avancerede teknikker

#### Beregnede skrivebeskyttede felter

Brug skrivebeskyttede felter til at vise beregninger baseret på andre svar:

```
| type      | name     | label           | read_only | calculation            |
|-----------|----------|-----------------|-----------|------------------------|
| calculate | bmi      | BMI:            | yes       | ${weight} / (${height} * ${height}) |
```

## Bedste praksis for skrivebeskyttede felter

1. **Klarhed**: Angiv tydeligt, hvilke felter der er skrivebeskyttede, via visuelle signaler eller labels.
2. **Konsistens**: Brug skrivebeskyttede felter konsekvent i hele din undersøgelse.
3. **Validering**: Selvom skrivebeskyttede felter ikke kan redigeres, bør du inkludere dem i din datavalideringsproces.
4. **Ydeevne**: Vær forsigtig med komplekse beregninger i skrivebeskyttede felter, da de kan påvirke formularindlæsningstiden.
5. **Tilgængelighed**: Sørg for, at skrivebeskyttede felter er korrekt markeret til skærmlæsere.

## Kendte begrænsninger

- Visse komplekse dynamiske skrivebeskyttede betingelser kan have en let ydeevneindvirkning på lavklassede enheder.
- Skrivebeskyttede felter forhindrer muligvis ikke alle former for datamanipulation i eksporterede datafiler, så validering på serversiden anbefales til kritiske data.
