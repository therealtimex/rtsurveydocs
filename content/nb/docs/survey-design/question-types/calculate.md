---
title: "Calculate"
description: ""
icon: "calculate"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 235
---

Calculate-spørsmål i XLSForm og rtSurvey brukes til å utføre beregninger basert på andre felt eller verdier i skjemaet. Disse spørsmålene vises ikke for brukeren, men kjører i bakgrunnen og lagrer resultatene for senere bruk eller innsending.

## Syntaks

I XLSForm defineres et calculate-spørsmål som følger:

| type      | name     | label | calculation |
|-----------|----------|-------|-------------|
| calculate | calc_q1  |       | ${q1} + ${q2} |

- **type**: Alltid "calculate" for denne spørsmålstypen.
- **name**: Et unikt navn for calculate-spørsmålet.
- **label**: Vanligvis tom siden calculate-spørsmål ikke vises for brukere.
- **calculation**: Formelen som skal evalueres.

## Brukstilfeller

Calculate-spørsmål brukes vanligvis for:

1. Utføre aritmetiske operasjoner
2. Slå sammen strenger
3. Bruke kompleks logikk eller funksjoner
4. Lagre mellomliggende resultater for senere bruk

## Eksempler

### Grunnleggende aritmetikk

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | total    | ${price} * ${quantity} |
```

### Strengsammenslåing

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | full_name| concat(${first_name}, ' ', ${last_name}) |
```

### Bruke funksjoner

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | age      | int((today() - ${date_of_birth}) / 365.25) |
```

## Avansert bruk i rtSurvey

### pulldata()-funksjonen

rtSurvey støtter `pulldata()`-funksjonen i calculate-felt, som lar deg hente data fra eksterne CSV-filer:

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | city     | pulldata('cities', 'city_name', 'zip_code', ${zip_input}) |
```

#### Syntaks

Den grunnleggende syntaksen for pulldata() er:

```
pulldata('csv_filnavn', 'kolonne_å_returnere', 'nøkkelkolonne', ${samsvarende_verdi})
```

- 'csv_filnavn': Navn på CSV-filen (uten .csv-endelse)
- 'kolonne_å_returnere': Kolonnenavn som inneholder dataene du vil hente
- 'nøkkelkolonne': Kolonnenavn som skal sammenlignes mot
- ${samsvarende_verdi}: Verdi å slå opp i nøkkelkolonnen

#### Viktige notater

1. CSV-filen må lastes opp sammen med XLSForm ved distribusjon av spørreundersøkelsen.
2. Bruk komma som separatorer i CSV-filen, ikke semikolon.
3. Unngå komma innenfor datafeltene i CSV-en, da de kan forårsake analysefeil.
4. pulldata() støtter bare 1-til-1-relasjoner. Hvis flere treff finnes, returneres bare det første.
5. Det kan være begrensninger på tekstlengden som kan hentes (rundt 76 tegn).

### Betingede beregninger

Du kan bruke if()-setninger for betingede beregninger:

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | discount | if(${total} > 1000, ${total} * 0.1, 0) |
```

## Beste praksis

1. Bruk meningsfulle navn for calculate-felt for å forbedre skjemaets lesbarhet.
2. Unngå altfor komplekse beregninger i ett enkelt felt; bryt dem ned om nødvendig.
3. Test beregningene grundig, spesielt når du bruker komplekse formler eller eksterne data.
4. Husk at calculate-felt kjøres hver gang skjemaet evalueres, noe som kan påvirke ytelsen for svært komplekse eller tallrike beregninger.
5. Når du bruker pulldata(), sørg for at CSV-filene er riktig formatert og test grundig med dine spesifikke data og skjemastruktur.

## Begrensninger

- Calculate-felt kan ikke redigeres direkte av brukere.
- Resultatet av et calculate-felt er ikke umiddelbart synlig med mindre det refereres til i et visningsfelt eller brukes i skjemalogikk.
