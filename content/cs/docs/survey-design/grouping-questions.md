---
title: "Seskupování otázek"
description: ""
icon: "auto_awesome"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 250
---

Skupiny v XLSForm vám umožňují organizovat související otázky dohromady, čímž se zlepšuje struktura průzkumu a zvyšují se možnosti analýzy dat. rtSurvey plně podporuje skupiny XLSForm a rozšiřuje jejich funkce o další možnosti.

## Základní struktura skupiny

Pro vytvoření skupiny otázek použijte syntaxi `begin_group` a `end_group`:

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | respondent | Informace o respondentovi                |
| text         | name       | Zadejte jméno respondenta                |
| text         | position   | Zadejte pozici respondenta               |
| end_group    |            |                                          |
```

Klíčové body:
- Řádek `begin_group` vyžaduje `name` a `label`.
- Řádek `end_group` nepotřebuje název ani popisek.
- Otázky mezi `begin_group` a `end_group` jsou součástí skupiny.

## Vzhled skupiny

rtSurvey podporuje různé možnosti vzhledu pro skupiny:

1. **field-list**: Zobrazí více otázek na stejné obrazovce.
   ```
   | type         | name       | label     | appearance |
   |--------------|------------|-----------|------------|
   | begin_group  | respondent | Respondent| field-list |
   | text         | name       | Jméno     |            |
   | text         | position   | Pozice    |            |
   | end_group    |            |           |            |
   ```

2. **grid**: Vytvoří kompaktní, tabulkové rozvržení pro skupiny (specifické pro rtSurvey).
   ```
   | type         | name       | label     | appearance |
   |--------------|------------|-----------|------------|
   | begin_group  | household  | Domácnost | grid       |
   | text         | member_name| Jméno     |            |
   | integer      | member_age | Věk       |            |
   | end_group    |            |           |            |
   ```

3. **collapsible**: Vytvoří rozbalitelné/sbalitelné skupiny (specifické pro rtSurvey).
   ```
   | type         | name       | label     | appearance  |
   |--------------|------------|-----------|-------------|
   | begin_group  | details    | Detaily   | collapsible |
   | text         | address    | Adresa    |             |
   | text         | phone      | Telefon   |             |
   | end_group    |            |           |             |
   ```

## Vnořené skupiny

Skupiny mohou být vnořeny do jiných skupin pro složitější struktury:

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | hospital   | Informace o nemocnici                    |
| text         | hosp_name  | Jaký je název této nemocnice?            |
| begin_group  | medication | Informace o léčivech                     |
| text         | med_name   | Název léčiva                             |
| end_group    |            |                                          |
| end_group    |            |                                          |
```

## Skupiny s logikou přeskočení

Skupinám lze přiřadit podmínky `relevant`, čímž zobrazíte nebo skryjete celé sekce najednou:

```
| type         | name          | label              | relevant                |
|--------------|---------------|--------------------|-------------------------|
| select_one yn| has_business  | Podnikáte?         |                         |
| begin_group  | business_info | Informace o podniku| ${has_business} = 'yes' |
| text         | bus_name      | Název podniku      |                         |
| integer      | employees     | Počet zaměstnanců  |                         |
| end_group    |               |                    |                         |
```

## Osvědčené postupy

1. Používejte skupiny pro logické uspořádání otázek pro lepší navigaci enumerátora.
2. Aplikujte `field-list` na skupiny pro mobilní průzkumy, kde se více otázek vejde na jednu obrazovku.
3. Vyhněte se příliš hlubokému vnořování skupin — dvě nebo tři úrovně jsou obvykle dostatečné.
4. Pojmenujte skupiny popisně, protože názvy skupin se objevují v exportovaných datech.
5. Testujte skupiny s logikou přeskočení důkladně, aby se zajistilo správné chování.

## Omezení

- Skupiny `field-list` mohou být pomalé na načítání s mnoha otázkami nebo složitou logikou.
- Vnořené skupiny `field-list` nemusí správně fungovat na všech klientech.
- Skupiny `grid` jsou specifické pro rtSurvey a nemusí se správně zobrazovat v jiných klientech kompatibilních s ODK.
