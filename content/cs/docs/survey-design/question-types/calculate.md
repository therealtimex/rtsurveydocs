---
title: "Calculate"
description: ""
icon: "calculate"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 235
---

Otázky calculate v XLSForms a rtSurvey se používají pro provádění výpočtů na základě jiných polí nebo hodnot ve formuláři. Tyto otázky se uživateli nezobrazují, ale místo toho běží na pozadí a ukládají výsledky pro pozdější použití nebo odeslání.

## Syntaxe

V XLSForm je otázka calculate definována takto:

| type      | name     | label | calculation |
|-----------|----------|-------|-------------|
| calculate | calc_q1  |       | ${q1} + ${q2} |

- **type**: Vždy „calculate" pro tento typ otázky.
- **name**: Jedinečný název pro otázku calculate.
- **label**: Obvykle ponecháno prázdné, protože otázky calculate se uživatelům nezobrazují.
- **calculation**: Vzorec, který má být vyhodnocen.

## Použití

Otázky calculate se běžně používají pro:

1. Provádění aritmetických operací
2. Zřetězení řetězců
3. Aplikaci složité logiky nebo funkcí
4. Ukládání mezivýsledků pro pozdější použití

## Příklady

### Základní aritmetika

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | total    | ${price} * ${quantity} |
```

### Zřetězení řetězců

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | full_name| concat(${first_name}, ' ', ${last_name}) |
```

### Použití funkcí

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | age      | int((today() - ${date_of_birth}) / 365.25) |
```

## Pokročilé použití v rtSurvey

### Funkce pulldata()

rtSurvey podporuje funkci `pulldata()` v polích calculate, což umožňuje načítání dat z externích CSV souborů:

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | city     | pulldata('cities', 'city_name', 'zip_code', ${zip_input}) |
```

#### Syntaxe

Základní syntaxe pro pulldata() je:

```
pulldata('csv_filename', 'column_to_return', 'key_column', ${matching_value})
```

- `'csv_filename'`: Název CSV souboru (bez přípony .csv)
- `'column_to_return'`: Název sloupce obsahujícího data, která chcete načíst
- `'key_column'`: Název sloupce pro porovnání
- `${matching_value}`: Hodnota pro vyhledání v klíčovém sloupci (často proměnná z formuláře)

#### Důležité poznámky

1. CSV soubor musí být nahrán spolu s vaším XLSForm při nasazení průzkumu.
2. V CSV souboru používejte čárky jako oddělovače, nikoli středníky.
3. Vyhněte se čárkám uvnitř datových polí CSV, protože mohou způsobit problémy s parsováním.
4. pulldata() podporuje pouze relace 1:1. Pokud je nalezeno více shod, vrátí pouze první.
5. Mohou existovat omezení délky textu, který lze načíst (přibližně 76 znaků).
6. pulldata() můžete použít v omezeních pro validaci záznamů oproti datům CSV.

### Podmíněné výpočty

Můžete použít příkazy if() pro podmíněné výpočty:

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | discount | if(${total} > 1000, ${total} * 0.1, 0) |
```

## Osvědčené postupy

1. Používejte smysluplné názvy pro pole calculate pro zlepšení čitelnosti formuláře.
2. Vyhněte se příliš složitým výpočtům v jediném poli; v případě potřeby je rozdělte.
3. Důkladně testujte výpočty, zejména při použití složitých vzorců nebo externích dat.
4. Pamatujte, že pole calculate se spouštějí při každém vyhodnocení formuláře, což může ovlivnit výkon u velmi složitých nebo početných výpočtů.
5. Při použití pulldata() zajistěte správné formátování CSV souborů a důkladně testujte s konkrétními daty a strukturou formuláře.

## Omezení

- Pole calculate nejsou přímo editovatelná uživateli.
- Výsledek pole calculate není okamžitě viditelný, pokud není odkazován v poli zobrazení nebo použit v logice formuláře.
