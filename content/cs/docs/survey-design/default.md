---
title: "Výchozí hodnoty"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 287
---

Výchozí hodnoty v rtSurvey vám umožňují předvyplnit otázky odpověďmi, když se s nimi respondent poprvé setká. Tato funkce může výrazně zvýšit efektivitu průzkumu a kvalitu dat poskytnutím počátečních hodnot, které jsou buď běžně vybrány nebo slouží jako příklady očekávaného vstupu.

## Základní použití

Pro nastavení výchozí hodnoty použijte sloupec `default` ve vašem XLSForm:

```
| type    | name        | label                         | default    |
|---------|-------------|-------------------------------|------------|
| date    | survey_date | Datum průzkumu                | 2024-07-04 |
| decimal | weight      | Váha respondenta? (v kg)      | 51.3       |
```

V tomto příkladu bude datum průzkumu předvyplněno 4. července 2024 a pole váhy začne hodnotou 51,3 kg.

## Dynamické výchozí hodnoty

rtSurvey podporuje dynamické výchozí hodnoty pomocí funkcí:

```
| type | name | label                              | default  |
|------|------|------------------------------------| ---------|
| date | d    | Zadejte datum, kdy událost nastala? | today()  |
```

Funkce `today()` automaticky nastaví výchozí hodnotu na aktuální datum.

## Funkce specifické pro rtSurvey

### Výchozí hodnoty s vědomím kontextu

rtSurvey rozšiřuje funkci výchozích hodnot o výchozí hodnoty s vědomím kontextu:

```
| type    | name     | label           | default            |
|---------|----------|-----------------|---------------------|
| text    | location | Aktuální poloha | ${current_location} |
```

Tato proměnná `${current_location}` rtSurvey předvyplňuje polohu na základě GPS zařízení.

### Kaskádové výchozí hodnoty

rtSurvey umožňuje výchozí hodnoty na základě předchozích odpovědí:

```
| type    | name     | label           | default         |
|---------|----------|-----------------|-----------------|
| text    | city     | Město           |                 |
| text    | district | Okres           | ${city}-district|
```

Pole okresu je předvyplněno na základě zadaného města.

### Výchozí hodnoty v opakováních

Pro otázky uvnitř skupiny opakování se výchozí hodnota vypočítá při přidání opakování:

```
| type         | name      | label        | default                |
|--------------|-----------|--------------|------------------------|
| begin repeat | visits    | Návštěvy kliniky |                   |
| date         | visit_date| Datum návštěvy | ${previous_visit_date} |
| end repeat   |           |              |                        |
```

Toto nastaví výchozí datum návštěvy na datum předchozí návštěvy.

## Osvědčené postupy pro použití výchozích hodnot

1. **Používejte střídmě**: Používejte výchozí hodnoty pouze tam, kde výrazně zlepšují efektivitu nebo kvalitu dat.
2. **Zajistěte přesnost**: Pravidelně kontrolujte a aktualizujte statické výchozí hodnoty.
3. **Důkladně testujte**: Zejména při použití dynamických nebo vypočtených výchozích hodnot.
4. **Zvažte uživatelský zážitek**: Zajistěte, aby výchozí hodnoty neuváděly respondenty v omyl nebo nezaváděly zkreslení.
5. **Jasně dokumentujte**: Ujistěte se, že všichni členové týmu chápou zdůvodnění výchozích hodnot.

## Pokročilé techniky výchozích hodnot

### Náhodné výchozí hodnoty

rtSurvey podporuje náhodné výchozí hodnoty pro určité typy otázek:

```
| type              | name    | label        | default           |
|-------------------|---------|--------------|-------------------|
| select_one options| choice  | Vyberte jednu: | random(options) |
```

Toto náhodně vybere výchozí možnost ze seznamu „options".

### Podmíněné výchozí hodnoty

Použijte relevanci pro nastavení podmíněných výchozích hodnot:

```
| type    | name     | label    | default | relevant        |
|---------|----------|----------|---------|-----------------|
| text    | other    | Specifikujte | N/A  | ${q1} = 'other' |
```

Zde je „N/A" výchozí hodnotou pouze tehdy, když je v předchozí otázce vybráno „other".

## Omezení

- Složité vypočtené výchozí hodnoty mohou ovlivnit dobu načítání formuláře, zejména na zařízeních nižší třídy.
- Některé dynamické výchozí hodnoty nemusí fungovat podle očekávání v režimu náhledu.

## Řešení problémů s výchozími hodnotami

1. **Výchozí hodnota se nezobrazuje**: Zkontrolujte syntaktické chyby ve výrazu výchozí hodnoty.
2. **Neočekávané hodnoty**: Ověřte logiku výpočtu a testujte s různými scénáři.
3. **Problémy s výkonem**: Optimalizujte složité výpočty výchozích hodnot nebo zvažte alternativní přístupy.
