---
title: "Gruppera frågor"
description: ""
icon: "auto_awesome"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 250
---

Grupper i XLSForm låter dig organisera relaterade frågor tillsammans, vilket förbättrar strukturen i din undersökning och förbättrar dataanalyskapabiliteterna. rtSurvey stöder fullt ut XLSForm-grupper och utökar deras funktionalitet med ytterligare funktioner.

## Grundläggande gruppstruktur

För att skapa en grupp med frågor, använd syntaxen `begin_group` och `end_group`:

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | respondent | Respondentinformation                    |
| text         | name       | Ange respondentens namn                  |
| text         | position   | Ange respondentens befattning            |
| end_group    |            |                                          |
```

Viktiga punkter:
- Raden `begin_group` kräver ett `name` och `label`.
- Raden `end_group` behöver inget namn eller etikett.
- Frågor mellan `begin_group` och `end_group` är en del av gruppen.

## Gruppens utseende

rtSurvey stöder olika utseendealternativ för grupper:

1. **field-list**: Visar flera frågor på samma skärm.
2. **grid**: Skapar en kompakt, tabellliknande layout för grupper (rtSurvey-specifikt).
3. **collapsible**: Skapar expanderbara/hopfällbara grupper (rtSurvey-specifikt).

## Kapslade grupper

Grupper kan kapslas i andra grupper för mer komplexa strukturer:

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | hospital   | Sjukshusinformation                      |
| text         | hosp_name  | Vad heter det här sjukhuset?             |
| begin_group  | medication | Läkemedelstillgänglighet                 |
| select_one y_n| hiv_meds  | Har sjukhuset HIV-medicin?               |
| end_group    |            |                                          |
| end_group    |            |                                          |
```

**Obs!**: Avsluta alltid den senast startade gruppen först för att upprätthålla korrekt kapslingsordning.

## Hopplogik för grupper

Använd kolumnen `relevant` för att implementera hopplogik för hela grupper:

```
| type         | name   | label                                        | relevant        |
|--------------|--------|----------------------------------------------|-----------------|
| integer      | age    | Hur gammal är du?                            |                 |
| begin_group  | child  | Barn                                         | ${age} <= 5     |
| integer      | muac   | Registrera barnets överarmsomkrets           |                 |
| select_one y_n| mrdt  | Är barnets snabba diagnostiska test positivt?|                |
| end_group    |        |                                              |                 |
```

I det här exemplet visas gruppen `child` bara om respondentens ålder är 5 eller yngre.

## Bästa praxis för att använda grupper

1. Använd meningsfulla namn för grupper för att förbättra dataanalysen.
2. Håll grupper fokuserade på relaterade frågor.
3. Använd kapslade grupper varsamt för att undvika alltför komplexa strukturer.
4. Testa hopplogiken noggrant när du använder `relevant` på grupper.
5. Överväg att använda `field-list`-utseende för korta grupper för att minska scrollning.
6. Använd rtSurveys rutnätslayout för kompakt visning av relaterad information.
7. Använd hopfällbara grupper för långa formulär för att förbättra navigeringen.

## rtSurvey-specifika funktioner

1. **Rutnätslayout**: Använd `grid`-utseendet för tabellliknande visningar.
2. **Hopfällbara grupper**: Implementera `collapsible`-utseende för expanderbara avsnitt.
3. **Anpassad stilsättning**: Tillämpa anpassad CSS på grupper för unika visuella designer.
4. **Dynamiskt gruppbeteende**: Implementera komplex hopplogik och beräkningar inom grupper.

## Flerspråksstöd

rtSurvey stöder flerspråkiga grupper. Använd språkspecifika kolumner för etiketter:

```
| type         | name       | label::Swedish | label::English |
|--------------|------------|----------------|----------------|
| begin_group  | personal   | Personlig info | Personal Info  |
| text         | name       | Namn           | Name           |
| end_group    |            |                |                |
```

## Kända begränsningar

- Extremt djup kapslingsordning av grupper kan påverka prestandan på vissa enheter.
- Vissa avancerade stilsättningsalternativ kanske inte är tillgängliga för grupper i mobilappen.

## Felsökning av grupper

1. Se till att varje `begin_group` har en motsvarande `end_group`.
2. Kontrollera att gruppnamn är unika inom formuläret.
3. Verifiera att hopplogiken refererar till korrekta frågensnamn.
4. Testa grupper noggrant på både webb- och mobilgränssnitt.
