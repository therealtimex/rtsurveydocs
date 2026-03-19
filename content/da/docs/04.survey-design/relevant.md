---
title: "Spring over spørgsmål"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 280
---

Spring-logik, også kaldet forgrening eller betinget logik, giver dig mulighed for at oprette dynamiske undersøgelser, der tilpasser sig respondenternes svar. I rtSurvey implementeres spring-logik ved hjælp af kolonnen `relevant` i din XLSForm.

## Grundlæggende spring-logik

For at implementere grundlæggende spring-logik skal du bruge kolonnen `relevant` til at angive en betingelse:

```
| type           | name          | label                       | relevant            |
|----------------|---------------|-----------------------------|--------------------|
| select_one y_n | likes_pizza   | Kan du lide pizza?          |                    |
| select_multiple pizza_toppings | favorite_topping | Yndlingspålæg | ${likes_pizza} = 'yes' |
```

I dette eksempel vises spørgsmålet "Yndlingspålæg" kun, hvis respondenten svarer "ja" til at kunne lide pizza.

## Syntaks for relevant-udtryk

- Brug `${ }` til at referere til andre spørgsmålsvariable.
- Til `select_one`-spørgsmål, sammenlign direkte: `${question_name} = 'svar'`
- Til `select_multiple`-spørgsmål, brug funktionen `selected()`.

## Avanceret spring-logik

### Flere betingelser

Du kan kombinere flere betingelser ved hjælp af `and`, `or` og parenteser:

```
| type    | name  | label                   | relevant                                  |
|---------|-------|-------------------------|-------------------------------------------|
| integer | age   | Hvad er din alder?      |                                           |
| text    | school| Hvilken skole går du på?| ${age} < 18 and (${location} = 'urban' or ${location} = 'suburban') |
```

### Brug af select_multiple-spørgsmål

Til `select_multiple`-spørgsmål skal du bruge funktionen `selected()`:

```
| type           | name          | label                       | relevant                               |
|----------------|---------------|-----------------------------|-----------------------------------------|
| select_multiple pizza_toppings | favorite_topping | Yndlingspålæg |                                         |
| text           | cheese_type   | Yndlingsosttype             | selected(${favorite_topping}, 'cheese') |
```

### "Andet"-mulighed i multiple choice

Implementér en fritekstudfyldt "Andet"-mulighed ved hjælp af `relevant`:

```
| type           | name                  | label                               | relevant                               |
|----------------|----------------------|-------------------------------------|---------------------------------------|
| select_multiple pizza_toppings | favorite_toppings | Hvad er dine yndlingspizzapålæg? |                                       |
| text           | favorite_toppings_other | Hvilke andre pålæg kan du lide?   | selected(${favorite_toppings}, 'other') |
```

Husk at inkludere 'other' som en mulighed i dit choices-regneark.

## rtSurvey-specifikke funktioner

### Dynamisk relevans

rtSurvey giver mulighed for dynamisk relevans baseret på beregnede felter:

```
| type      | name       | label              | calculation                   |
|-----------|------------|--------------------|-----------------------------|
| calculate | total_score| Samlet score       | ${score1} + ${score2} + ${score3} |
| text      | feedback   | Feedback           | ${total_score} > 75             |
```

### Relevans i gentagelser

rtSurvey understøtter relevans inden for gentagelsesgrupper:

```
| type         | name         | label            | relevant               |
|--------------|--------------|------------------|------------------------|
| begin repeat | child_info   | Barneinformation |                        |
| integer      | child_age    | Barnets alder    |                        |
| text         | school_name  | Skolens navn     | ${child_age} >= 5      |
| end repeat   |              |                  |                        |
```

## Bedste praksis for spring-logik i rtSurvey

1. **Hold det enkelt**: Undgå alt for komplekse relevans-betingelser, når det er muligt.
2. **Test grundigt**: Brug rtSurveys forhåndsvisningsfunktion til at teste alle mulige stier i din undersøgelse.
3. **Overvej ydeevne**: Meget kompleks spring-logik kan påvirke undersøgelsesydeevnen, især på mobilenheder.
4. **Brug klare variabelnavne**: Det gør dine relevans-udtryk nemmere at læse og vedligeholde.
5. **Dokumentér din logik**: Tilføj noter til at forklare komplekse springmønstre, især til teamsamarbejde.
6. **Vær opmærksom på dataanalyse**: Sprungne spørgsmål vil resultere i manglende data. Planlæg din analyse i overensstemmelse hermed.

## Fejlfinding af spring-logik

- **Syntaksfejl**: Sørg for, at alle `${ }` er korrekt lukket og stavet korrekt.
- **Cirkulære referencer**: Undgå at oprette løkker, hvor spørgsmål afhænger af hinanden.
- **Versalfølsomhed**: Husk, at svarmuligheder er versalfølsomme i relevans-udtryk.
- **Numeriske sammenligninger**: Brug passende operatorer (`<`, `>`, `=`) til numeriske sammenligninger.

## Konklusion

Effektiv brug af spring-logik kan markant forbedre respondenternes oplevelse og datakvaliteten i dine rtSurvey-projekter. Ved at udnytte rtSurveys avancerede funktioner og følge bedste praksis kan du oprette dynamiske, effektive undersøgelser, der tilpasser sig hver respondents unikke situation.
