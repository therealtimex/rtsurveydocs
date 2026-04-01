---
title: "Přeskakování otázek"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 280
---

Logika přeskočení, také známá jako větvení nebo podmíněná logika, vám umožňuje vytvářet dynamické průzkumy přizpůsobující se odpovědím respondentů. V rtSurvey je logika přeskočení implementována pomocí sloupce `relevant` ve vašem XLSForm.

## Základní logika přeskočení

Pro implementaci základní logiky přeskočení použijte sloupec `relevant` k specifikaci podmínky:

```
| type           | name          | label                       | relevant            |
|----------------|---------------|-----------------------------|--------------------|
| select_one y_n | likes_pizza   | Máte rádi pizzu?            |                     |
| text           | favorite_pizza| Jaký je váš oblíbený druh pizzy? | ${likes_pizza} = 'yes' |
```

Otázka `favorite_pizza` se zobrazí pouze tehdy, když respondent odpověděl „ano" na `likes_pizza`.

## Složitá logika přeskočení

Kombinujte více podmínek pomocí `and`, `or` a `not()`:

```
| type    | name      | label              | relevant                                    |
|---------|-----------|--------------------|---------------------------------------------|
| integer | age       | Váš věk?           |                                             |
| text    | job       | Vaše zaměstnání?   | ${age} >= 18 and ${age} <= 65               |
| note    | minor_note| Jste nezletilí.    | ${age} < 18                                 |
| note    | senior_note| Jste senioři.     | ${age} > 65                                 |
```

## Skupiny s logice přeskočení

Logiku přeskočení lze použít na celé skupiny, čímž zobrazíte nebo skryjete více otázek najednou:

```
| type         | name          | label                    | relevant            |
|--------------|---------------|--------------------------|---------------------|
| select_one yn| has_children  | Máte děti?               |                     |
| begin_group  | children_info | Informace o dětech       | ${has_children} = 'yes' |
| integer      | num_children  | Kolik dětí máte?         |                     |
| integer      | youngest_age  | Věk nejmladšího dítěte?  |                     |
| end_group    |               |                          |                     |
```

## Odkaz na výpočty ve výrazech relevant

Vypočtená pole lze použít ve výrazech relevant:

```
| type      | name        | label                | calculation                |
|-----------|-------------|----------------------|----------------------------|
| calculate | adult       |                      | if(${age} >= 18, 'yes', 'no') |
| text      | job_details | Podrobnosti práce    |                            |
```

```
| type | name        | relevant         |
|------|-------------|-----------------|
| text | job_details | ${adult} = 'yes' |
```

## Osvědčené postupy

1. Testujte všechny větve logiky přeskočení před nasazením.
2. Používejte jasné a popisné názvy polí pro srozumitelnější výrazy relevant.
3. Zvažte výkon při použití složitých výrazů relevant na velké formuláře.
4. Dokumentujte zamýšlenou logiku přeskočení pro ostatní členy týmu.
5. Vyhněte se kruhové závislosti v podmínkách relevant.

## Omezení

- Výrazy relevant jsou vyhodnocovány v reálném čase při zadávání dat — složité výrazy mohou zpomalit výkon formuláře.
- Pole skrytá pomocí relevant jsou stále součástí dat formuláře, ale jejich hodnoty jsou prázdné.
