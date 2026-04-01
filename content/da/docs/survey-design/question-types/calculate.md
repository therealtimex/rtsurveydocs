---
title: "Beregning"
description: ""
icon: "calculate"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 235
---

Beregningsspørgsmål i XLSForms og rtSurvey bruges til at udføre beregninger baseret på andre felter eller værdier i din formular. Disse spørgsmål vises ikke for brugeren, men kører i baggrunden og gemmer deres resultater til senere brug eller indsendelse.

## Syntaks

I XLSForm defineres et beregningsspørgsmål som følger:

| type      | name     | label | calculation |
|-----------|----------|-------|-------------|
| calculate | calc_q1  |       | ${q1} + ${q2} |

- **type**: Altid "calculate" for denne spørgsmålstype.
- **name**: Et unikt navn til beregningsspørgsmålet.
- **label**: Efterlades normalt tomt, da beregningsspørgsmål ikke vises for brugerne.
- **calculation**: Formlen der skal evalueres.

## Anvendelser

Beregningsspørgsmål bruges typisk til:

1. At udføre aritmetiske operationer
2. At sammensætte strenge
3. At anvende kompleks logik eller funktioner
4. At gemme mellemresultater til senere brug

## Eksempler

### Grundlæggende aritmetik

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | total    | ${price} * ${quantity} |
```

### Strengsammensætning

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | full_name| concat(${first_name}, ' ', ${last_name}) |
```

### Brug af funktioner

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | age      | int((today() - ${date_of_birth}) / 365.25) |
```

## Avanceret brug i rtSurvey

### `pulldata()`-funktionen

rtSurvey understøtter funktionen `pulldata()` i beregningsfelter, som giver dig mulighed for at hente data fra eksterne CSV-filer:

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | city     | pulldata('cities', 'city_name', 'zip_code', ${zip_input}) |
```

#### Syntaks

Den grundlæggende syntaks for pulldata() er:

```
pulldata('csv_filnavn', 'kolonne_der_returneres', 'nøglekolonne', ${matchende_værdi})
```

- 'csv_filnavn': Navn på CSV-filen (uden .csv-filtypenavn)
- 'kolonne_der_returneres': Kolonnenavn, der indeholder de data, du vil hente
- 'nøglekolonne': Kolonnenavn, der matches mod
- ${matchende_værdi}: Værdien der slås op i nøglekolonnen (ofte en variabel fra formularen)

#### Vigtige noter

1. CSV-filen skal uploades sammen med din XLSForm ved udrulning af undersøgelsen.
2. Brug kommaer som separatorer i din CSV-fil, ikke semikoloner.
3. Undgå kommaer inden for datafeltene i din CSV, da de kan forårsage parseproblemer.
4. pulldata() understøtter kun 1-til-1-relationer. Hvis der findes flere matches, returneres kun det første.
5. Der kan være begrænsninger på tekstlængde, der kan hentes (ca. 76 tegn).
6. Du kan bruge pulldata() i betingelser til at validere poster mod CSV-dataene.

### Betingede beregninger

Du kan bruge if()-sætninger til betingede beregninger:

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | discount | if(${total} > 1000, ${total} * 0.1, 0) |
```

## Bedste praksis

1. Brug meningsfulde navne til beregningsfelter for at forbedre formularens læsbarhed.
2. Undgå alt for komplekse beregninger i et enkelt felt; opdel dem om nødvendigt.
3. Test dine beregninger grundigt, især ved brug af komplekse formler eller eksterne data.
4. Husk at beregningsfelter kører, hver gang formularen evalueres, hvilket kan påvirke ydeevnen ved meget komplekse eller mange beregninger.
5. Når du bruger pulldata(), skal du sikre, at dine CSV-filer er korrekt formateret, og teste grundigt med dine specifikke data og formularstruktur.

## Begrænsninger

- Beregningsfelter kan ikke redigeres direkte af brugere.
- Resultatet af et beregningsfelt er ikke umiddelbart synligt, medmindre det refereres i et visningsfelt eller bruges i formularlogik.
