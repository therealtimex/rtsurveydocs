---
title: "Standardvärde"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 287
---

Standardvärden i rtSurvey låter dig förifyll frågor med svar när en respondent första gången stöter på dem. Denna funktion kan avsevärt förbättra undersökningseffektiviteten och datakvaliteten genom att tillhandahålla initiala värden som antingen vanligtvis väljs eller fungerar som exempel på förväntad inmatning.

## Grundläggande användning

För att ange ett standardvärde, använd kolumnen `default` i ditt XLSForm:

```
| type    | name        | label                         | default    |
|---------|-------------|-------------------------------|------------|
| date    | survey_date | Undersökningsdatum            | 2024-07-04 |
| decimal | weight      | Respondentens vikt? (i kg)    | 51.3       |
```

I det här exemplet förifylls undersökningsdatumet med 4 juli 2024, och viktfältet börjar med 51,3 kg.

## Dynamiska standardvärden

rtSurvey stöder dynamiska standardvärden med hjälp av funktioner:

```
| type | name | label                              | default  |
|------|------|------------------------------------| ---------|
| date | d    | Ange datumet då händelsen inträffade? | today()  |
```

Här anger funktionen `today()` automatiskt standardvärdet till det aktuella datumet.

## rtSurvey-specifika funktioner

### Kontextmedvetna standardvärden

rtSurvey utökar standardfunktionaliteten med kontextmedvetna standardvärden:

```
| type    | name     | label           | default            |
|---------|----------|-----------------|---------------------|
| text    | location | Aktuell plats   | ${current_location} |
```

### Kaskadande standardvärden

rtSurvey tillåter standardvärden baserade på tidigare svar:

```
| type    | name     | label           | default         |
|---------|----------|-----------------|-----------------|
| text    | city     | Stad            |                 |
| text    | district | Distrikt        | ${city}-distrikt|
```

## Bästa praxis för att använda standardvärden

1. **Använd sparsamt**: Använd bara standardvärden där de avsevärt förbättrar effektivitet eller datakvalitet.
2. **Säkerställ noggrannhet**: Granska och uppdatera statiska standardvärden regelbundet.
3. **Testa noggrant**: Särskilt när du använder dynamiska eller beräknade standardvärden.
4. **Tänk på användarupplevelsen**: Se till att standardvärden inte vilseleder respondenter eller introducerar bias.
5. **Dokumentera tydligt**: Se till att alla teammedlemmar förstår logiken bakom standardvärden.

## Kända begränsningar

- Komplexa beräknade standardvärden kan påverka formulärladdningstiden, särskilt på lägre enklare enheter.
- Vissa dynamiska standardvärden kanske inte fungerar som förväntat i förhandsgranskningsläge.

## Felsökning av standardvärden

1. **Standardvärde visas inte**: Kontrollera om det finns syntaxfel i standarduttrycket.
2. **Oväntade värden**: Verifiera beräkningslogiken och testa med olika scenarier.
3. **Prestandaproblem**: Optimera komplexa standardberäkningar eller överväg alternativa tillvägagångssätt.
