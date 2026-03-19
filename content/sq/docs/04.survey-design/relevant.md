---
title: "Kapërcimi i pyetjeve"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 280
---

Logjika e kapërcimit, e njohur edhe si degëzim ose logjikë e kushtëzuar, ju lejon të krijoni sondazhe dinamike që përshtaten me përgjigjet e të anketuarve. Në rtSurvey, logjika e kapërcimit implementohet duke përdorur kolonën `relevant` në XLSForm tuaj.

## Logjika Bazë e Kapërcimit

Për të implementuar logjikën bazë të kapërcimit, përdorni kolonën `relevant` për të specifikuar një kusht:

```
| type           | name          | label                       | relevant            |
|----------------|---------------|-----------------------------|--------------------|
| select_one y_n | likes_pizza   | A ju pëlqen pica?           |                    |
| select_multiple pizza_toppings | favorite_topping | Shtojcat e preferuara | ${likes_pizza} = 'yes' |
```

Në këtë shembull, pyetja "Shtojcat e preferuara" shfaqet vetëm nëse i anketuari përgjigjet "po" në pyetjen nëse i pëlqen pica.

## Sintaksa për Shprehjet Relevant

- Përdorni `${ }` për të referuar variablat e tjera të pyetjeve.
- Për pyetjet `select_one`, krahasoni direkt: `${emri_pyetjes} = 'përgjigja'`
- Për pyetjet `select_multiple`, përdorni funksionin `selected()`.

## Logjika e Avancuar e Kapërcimit

### Kushte të Shumëfishta

Mund të kombinoni kushte të shumëfishta duke përdorur `and`, `or` dhe kllapa:

```
| type    | name  | label                   | relevant                                  |
|---------|-------|-------------------------|-------------------------------------------|
| integer | age   | Cila është mosha juaj?  |                                           |
| text    | school| Cilën shkollë ndiqni?   | ${age} < 18 and (${location} = 'urban' or ${location} = 'suburban') |
```

### Përdorimi i Pyetjeve select_multiple

Për pyetjet `select_multiple`, përdorni funksionin `selected()`:

```
| type           | name          | label                       | relevant                               |
|----------------|---------------|-----------------------------|-----------------------------------------|
| select_multiple pizza_toppings | favorite_topping | Shtojcat e preferuara |                                         |
| text           | cheese_type   | Lloji i preferuar i djathit | selected(${favorite_topping}, 'cheese') |
```

### Opsioni "Tjetër" në Zgjedhje të Shumëfishta

Implementoni një opsion "Tjetër" me tekst të lirë duke përdorur `relevant`:

```
| type           | name                  | label                               | relevant                               |
|----------------|----------------------|-------------------------------------|---------------------------------------|
| select_multiple pizza_toppings | favorite_toppings | Cilat janë shtojcat tuaja të preferuara të picës? |                                       |
| text           | favorite_toppings_other | Cilat shtojca të tjera ju pëlqejnë?   | selected(${favorite_toppings}, 'other') |
```

Mos harroni të përfshini 'other' si opsion në fletën e punës choices.

## Veçoritë Specifike rtSurvey

### Relevant-i Dinamik

rtSurvey lejon relevant-in dinamik bazuar në fushat e llogaritura:

```
| type      | name       | label              | calculation                   |
|-----------|------------|--------------------|-----------------------------|
| calculate | total_score| Rezultati Total    | ${score1} + ${score2} + ${score3} |
| text      | feedback   | Reagimi            | ${total_score} > 75             |
```

### Relevant-i në Përsëritjet

rtSurvey mbështet relevant-in brenda grupeve të përsëritjeve:

```
| type         | name         | label            | relevant               |
|--------------|--------------|------------------|------------------------|
| begin repeat | child_info   | Informacioni i Fëmijës |                  |
| integer      | child_age    | Mosha e Fëmijës  |                        |
| text         | school_name  | Emri i Shkollës  | ${child_age} >= 5      |
| end repeat   |              |                  |                        |
```

### Relevant-i me Kaskadë

rtSurvey trajton me efikasitet relevant-in me kaskadë, ku relevant-i i një pyetjeje varet nga një tjetër, e cila nga ana e saj varet nga e treta:

```
| type           | name        | label                  | relevant               |
|----------------|-------------|------------------------|------------------------|
| select_one y_n | has_car     | Keni makinë?           |                        |
| select_one car_type | car_type | Çfarë tipi makine?  | ${has_car} = 'yes'     |
| text           | model       | Modeli specifik        | ${car_type} = 'sedan'  |
```

## Praktikat Më të Mira për Logjikën e Kapërcimit në rtSurvey

1. **Mbajeni të Thjeshtë**: Shmangni kushtet tepër komplekse relevant kur është e mundur.
2. **Testoni Tërësisht**: Përdorni veçorinë e pamjes paraprake të rtSurvey për të testuar të gjitha rrugët e mundshme nëpërmjet sondazhit tuaj.
3. **Konsideroni Performancën**: Logjika shumë komplekse e kapërcimit mund të ndikojë në performancën e sondazhit, veçanërisht në pajisjet celulare.
4. **Përdorni Emra Variablash të Qartë**: Kjo i bën shprehjet tuaja relevant më të lehta për t'u lexuar dhe mirëmbajtur.
5. **Dokumentoni Logjikën tuaj**: Shtoni shënime për të shpjeguar modelet komplekse të kapërcimit, veçanërisht për bashkëpunimin e ekipeve.
6. **Kini Parasysh Analizën e të Dhënave**: Pyetjet e kapërcyera do të rezultojnë në të dhëna të munguar. Planifikoni analizën tuaj në përputhje me rrethanat.

## Zgjidhja e Problemeve me Logjikën e Kapërcimit

- **Gabimet Sintaksore**: Sigurohuni që të gjitha `${ }` të jenë mbyllur siç duhet dhe shkruar saktë.
- **Referencat Qarkulluese**: Shmangni krijimin e laqeve ku pyetjet varen nga njëra-tjetra.
- **Ndjeshmëria ndaj Shkronjave**: Mos harroni se zgjedhjet e përgjigjeve janë të ndjeshme ndaj shkronjave në shprehjet relevant.
- **Krahasimet Numerike**: Përdorni operatorët e duhur (`<`, `>`, `=`) për krahasimet numerike.

## Përfundim

Përdorimi efektiv i logjikës së kapërcimit mund të përmirësojë ndjeshëm eksperiencën e të anketuarit dhe cilësinë e të dhënave në projektet tuaja rtSurvey. Duke shfrytëzuar veçoritë e avancuara të rtSurvey dhe duke ndjekur praktikat më të mira, mund të krijoni sondazhe dinamike, efikase që përshtaten me situatën unike të çdo të anketuari.
