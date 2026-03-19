---
title: "Hoppa över frågor"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 280
---

Hopplogik, även känd som förgrening eller villkorlig logik, låter dig skapa dynamiska undersökningar som anpassar sig efter respondenternas svar. I rtSurvey implementeras hopplogik med kolumnen `relevant` i ditt XLSForm.

## Grundläggande hopplogik

För att implementera grundläggande hopplogik, använd kolumnen `relevant` för att ange ett villkor:

```
| type           | name          | label                       | relevant            |
|----------------|---------------|-----------------------------|--------------------|
| select_one y_n | likes_pizza   | Gillar du pizza?            |                    |
| select_multiple pizza_toppings | favorite_topping | Favoritpålägg | ${likes_pizza} = 'yes' |
```

I det här exemplet visas frågan "Favoritpålägg" bara om respondenten svarar "yes" på om de gillar pizza.

## Syntax för relevant-uttryck

- Använd `${ }` för att referera till andra frågors variabler.
- För `select_one`-frågor, jämför direkt: `${question_name} = 'answer'`
- För `select_multiple`-frågor, använd funktionen `selected()`.

## Avancerad hopplogik

### Flera villkor

Du kan kombinera flera villkor med `and`, `or` och parenteser:

```
| type    | name  | label                   | relevant                                  |
|---------|-------|-------------------------|-------------------------------------------|
| integer | age   | Hur gammal är du?       |                                           |
| text    | school| Vilken skola går du på? | ${age} < 18 and (${location} = 'urban' or ${location} = 'suburban') |
```

### Använda select_multiple-frågor

För `select_multiple`-frågor, använd funktionen `selected()`:

```
| type           | name          | label                       | relevant                               |
|----------------|---------------|-----------------------------|-----------------------------------------|
| select_multiple pizza_toppings | favorite_topping | Favoritpålägg |                                         |
| text           | cheese_type   | Favoritosttyp               | selected(${favorite_topping}, 'cheese') |
```

### "Övrigt"-alternativ i flervalsfrågor

Implementera ett fritextalternativ "Övrigt" med `relevant`:

```
| type           | name                  | label                               | relevant                               |
|----------------|----------------------|-------------------------------------|---------------------------------------|
| select_multiple pizza_toppings | favorite_toppings | Vilka är dina favoritpålägg på pizza? |                                       |
| text           | favorite_toppings_other | Vilket annat pålägg gillar du?   | selected(${favorite_toppings}, 'other') |
```

Kom ihåg att inkludera 'other' som ett alternativ i ditt choices-kalkylblad.

## rtSurvey-specifika funktioner

### Dynamisk relevans

rtSurvey tillåter dynamisk relevans baserad på beräknade fält:

```
| type      | name       | label              | calculation                   |
|-----------|------------|--------------------|-----------------------------|
| calculate | total_score| Totalpoäng         | ${score1} + ${score2} + ${score3} |
| text      | feedback   | Återkoppling       | ${total_score} > 75             |
```

### Relevans i upprepningar

rtSurvey stöder relevans inom upprepningsgrupper:

```
| type         | name         | label            | relevant               |
|--------------|--------------|------------------|------------------------|
| begin repeat | child_info   | Barnuppgifter    |                        |
| integer      | child_age    | Barnets ålder    |                        |
| text         | school_name  | Skolans namn     | ${child_age} >= 5      |
| end repeat   |              |                  |                        |
```

### Kaskaderande relevans

rtSurvey hanterar effektivt kaskaderande relevans, där relevansen för en fråga beror på en annan, som i sin tur beror på en tredje:

```
| type           | name        | label                  | relevant               |
|----------------|-------------|------------------------|------------------------|
| select_one y_n | has_car     | Äger du en bil?        |                        |
| select_one car_type | car_type | Vilken typ av bil?   | ${has_car} = 'yes'     |
| text           | model       | Specifik modell        | ${car_type} = 'sedan'  |
```

## Bästa praxis för hopplogik i rtSurvey

1. **Håll det enkelt**: Undvik alltför komplexa relevansvillkor när det är möjligt.
2. **Testa noggrant**: Använd rtSurves förhandsgranskningsfunktion för att testa alla möjliga vägar genom din undersökning.
3. **Tänk på prestanda**: Mycket komplex hopplogik kan påverka undersökningens prestanda, särskilt på mobila enheter.
4. **Använd tydliga variabelnamn**: Detta gör dina relevansuttryck lättare att läsa och underhålla.
5. **Dokumentera din logik**: Lägg till anteckningar för att förklara komplexa hoppmönster, särskilt för teamsamarbete.
6. **Var medveten om dataanalysen**: Hoppade frågor resulterar i saknade data. Planera din analys i enlighet med detta.

## Felsökning av hopplogik

- **Syntaxfel**: Se till att alla `${ }` är korrekt avslutade och korrekt stavade.
- **Cirkelreferenser**: Undvik att skapa loopar där frågor beror på varandra.
- **Skiftlägeskänslighet**: Kom ihåg att svarsalternativ är skiftlägeskänsliga i relevansuttryck.
- **Numeriska jämförelser**: Använd lämpliga operatorer (`<`, `>`, `=`) för numeriska jämförelser.

## Sammanfattning

Effektiv användning av hopplogik kan avsevärt förbättra respondentupplevelsen och datakvaliteten i dina rtSurvey-projekt. Genom att utnyttja rtSurves avancerade funktioner och följa bästa praxis kan du skapa dynamiska, effektiva undersökningar som anpassar sig efter varje respondents unika situation.
