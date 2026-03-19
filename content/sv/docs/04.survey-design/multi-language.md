---
title: "Flerspråksstöd"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 285
---

rtSurvey tillhandahåller robust flerspråksstöd, vilket låter dig skapa undersökningar på flera språk. Denna funktion är avgörande för att bedriva forskning i olika språkliga populationer eller i flerspråkiga miljöer.

## Konfigurera flerspråkiga undersökningar

För att skapa en flerspråkig undersökning i rtSurvey behöver du lägga till språkspecifika kolumner i ditt XLSForm. Så här gör du:

1. **Etikettöversättningar**: Lägg till kolumner för varje språk med formatet `label::Language (code)`.
2. **Tipsöversättningar**: Använd `hint::Language (code)` för att översätta tips.
3. **Mediefilöversättningar**: För språkspecifika medier, använd `media::Language (code)`.

Exempel:

```
| type    | name | label::Swedish (sv) | label::English (en) | hint::Swedish (sv)  | hint::English (en)  |
|---------|------|---------------------|---------------------|---------------------|---------------------|
| integer | age  | Hur gammal är du?   | How old are you?    | Ange din ålder      | Enter your age      |
```

## Språkkoder

Det rekommenderas att använda de officiella 2-teckenspråkkoderna (undertaggar) efter språknamnet. Du kan hitta de officiella koderna [här](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry).

## Ange ett standardspråk

För att ange ett standardspråk för datainsamling, använd kalkylbladet `settings` i ditt XLSForm:

```
| form_id   | version | default_language |
|-----------|---------|-------------------|
| test_form | 101     | Swedish (sv)      |
```

## rtSurvey-specifika funktioner

### Dynamisk språkväxling

rtSurvey tillåter användare att växla språk dynamiskt under datainsamling:

- I webbgränssnittet, använd språkrullgardinsmenyn i det övre navigeringsfältet.
- I mobilappen, öppna språkalternativ via inställningsmenyn.

### Språkspecifika valideringsmeddelanden

rtSurvey utökar flerspråksstödet till valideringsmeddelanden:

```
| type    | name | constraint | constraint_message::Swedish (sv) | constraint_message::English (en) |
|---------|------|------------|----------------------------------|----------------------------------|
| integer | age  | . <= 150   | Ålder måste vara 150 eller lägre | Age must be 150 or less          |
```

### RTL-språkstöd

För höger-till-vänster (RTL) språk som arabiska eller hebreiska justerar rtSurvey automatiskt layouten.

## Bästa praxis för flerspråkiga undersökningar

1. **Konsekvent namngivning**: Använd konsekventa språkkoder i hela ditt formulär.
2. **Professionell översättning**: Anlita professionella översättare som är bekanta med undersökningskontexten.
3. **Kontextanteckningar**: Tillhandahåll kontextanteckningar för översättare för att säkerställa korrekta översättningar.
4. **Testning**: Testa ditt formulär på alla språk innan driftsättning.
5. **Unicode-stöd**: Se till att dina datainsamlingsenheter stöder Unicode för icke-latinska skrifter.
6. **Språkspecifika medier**: Använd kulturellt lämpliga bilder eller ljud för varje språk.
7. **Undvik text i bilder**: Om du använder bilder med text, skapa separata bilder för varje språk.

## Exportera flerspråkiga data

När du exporterar data från rtSurvey:

- Välj att exportera på ett specifikt språk eller inkludera alla språkversioner.
- Språkmetadata inkluderas i exporten, vilket anger vilket språk som användes för varje svar.

## Kända begränsningar

- Vissa avancerade funktioner kanske inte är tillgängliga på alla språk.
- Extremt långa översättningar kan påverka layouten på mindre skärmar.
