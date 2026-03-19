---
title: "Heltal"
description: "Heltalsfrågor tillåter heltalsinmatning i din undersökning."
icon: "123"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 222
---

Frågtypen integer i XLSForms och rtSurvey används för att samla in heltalssvar. Denna frågtyp är viktig för att samla in numeriska data utan decimaler, som antal, åldrar eller år.

## Grundläggande XLSForm-specifikation

| type    | name  | label                          |
|---------|-------|--------------------------------|
| integer | age   | Ange din ålder i år            |

För mer detaljer om grundläggande frågtypen integer, se [XLSForm-specifikationen](https://xlsform.org/en/#question-types).

## Användningsområden

Heltalsfrågor används vanligtvis för:

1. Åldersinmatning
2. Räkna objekt (t.ex. antal barn, hushållsmedlemmar)
3. År-inmatning (t.ex. födelseår)
4. Betyg på en numerisk skala
5. Alla heltalsdatainsamlingar

## Bästa praxis

1. Använd tydliga och kortfattade etiketter för att specificera förväntad inmatning.
2. Implementera intervallbegränsningar för att förhindra orealistiska eller felaktiga inmatningar.
3. Överväg att använda tipstext för att ge exempel eller förtydliga det förväntade formatet.
4. För stora tal, överväg att använda kommatecken eller mellanslag i etiketten för att förbättra läsbarheten.

## Begränsningar och validering

Du kan lägga till begränsningar för att säkerställa att det angivna värdet faller inom ett specifikt intervall:

| type    | name  | label                          | constraint        | constraint_message                     |
|---------|-------|--------------------------------|-------------------|----------------------------------------|
| integer | age   | Ange din ålder i år            | .>0 and .<=120    | Ålder måste vara mellan 1 och 120 år   |

## Exempelanvändning

Här är ett exempel på hur du kan använda heltalsfrågor i en hushållsundersökning:

| type    | name           | label                                      | constraint     | constraint_message                         |
|---------|----------------|--------------------------------------------|-----------------|--------------------------------------------|
| integer | household_size | Hur många personer bor i ditt hushåll?    | .>0             | Hushållets storlek måste vara minst 1      |
| integer | num_children   | Hur många barn under 18 i hushållet?      | .>=0            | Antal barn kan inte vara negativt          |
| integer | year_built     | Vilket år byggdes ditt hus?               | .>1800 and .<=2023 | År måste vara mellan 1800 och 2023      |

## Beräkning med heltalsvärden

Heltalsvärden kan användas i beräkningar. Här är ett exempel:

| type    | name           | label                                      |
|---------|----------------|---------------------------------------------|
| integer | num_adults     | Antal vuxna i hushållet                    |
| integer | num_children   | Antal barn i hushållet                     |
| calculate | total_members | | 

I beräkningsraden kan du använda:

```
calculation | ${num_adults} + ${num_children}
```

Detta summerar antalet vuxna och barn för att få det totala antalet hushållsmedlemmar.
