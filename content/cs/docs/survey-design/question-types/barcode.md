---
title: "Barcode"
description: "Otázky barcode umožňují skenování a zachycení dat čárových kódů v průzkumu."
icon: "qr_code_scanner"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 231
---

Typ otázky barcode v XLSForms a rtSurvey umožňuje uživatelům skenovat a zachycovat data čárových kódů přímo v průzkumu. Tato funkce je zvláště užitečná pro správu zásob, sledování produktů nebo jakýkoli scénář, kde je vyžadováno rychlé a přesné zadávání kódovaných informací.

## Základní specifikace XLSForm

| type    | name          | label                   |
|---------|---------------|-------------------------|
| barcode | product_code  | Naskenujte čárový kód produktu |

## Použití

Otázky barcode se běžně používají pro:

1. Identifikaci produktů v inventárních průzkumech
2. Sledování majetku při terénních operacích
3. Ověřování lístků nebo ID na akcích
4. Rychlé zadávání kódovaných informací

## Osvědčené postupy

1. Zajistěte správné osvětlení pro přesné skenování čárových kódů.
2. Poskytněte uživatelům jasné pokyny, jak umístit zařízení pro skenování.
3. Zahrňte možnost ručního zadání jako zálohu v případě potíží se skenováním.
4. Testujte funkci skenování čárových kódů s různými zařízeními a typy čárových kódů před nasazením průzkumu.

## Omezení

- Přesnost skenování čárových kódů se může lišit v závislosti na kvalitě kamery zařízení a podmínkách prostředí.
- Některá starší nebo levná zařízení nemusí podporovat skenování čárových kódů.
- Určité typy čárových kódů nemusí být podporovány v závislosti na implementaci.

## Příklad použití

Příklad použití otázky barcode v inventárním průzkumu:

| type    | name          | label                   | hint                                      |
|---------|---------------|-------------------------|-------------------------------------------|
| barcode | product_code  | Naskenujte čárový kód produktu | Umístěte čárový kód do rámečku     |
| integer | quantity      | Zadejte množství produktu  |                                           |
| note    | confirmation  | Naskenovaný produkt: ${product_code}. Množství: ${quantity} |           |

V tomto příkladu průzkum zachycuje čárový kód produktu, ptá se na množství a poté zobrazí potvrzovací poznámku s naskenovanými informacemi.
