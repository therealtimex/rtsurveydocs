---
title: "Typy otázek"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 220
---

rtSurvey podporuje všechny standardní typy otázek XLSForm a několik rozšíření. Každý typ otázky určuje, jaký druh dat se sbírá a jak je vstupní widget zobrazen na zařízení.

Pro nastavení typu otázky zadejte název typu do sloupce `type` listu **survey** ve vašem XLSForm.

## Textový vstup

| Typ | Popis |
|-----|-------|
| [text](text) | Volná textová odpověď — povoleny jsou jakékoliv znaky |
| [integer](integer) | Celé číslo (bez desetinných míst) |
| [decimal](decimal) | Číslo s desetinnými místy |
| [range](range) | Číslo vybrané pomocí posuvníku v definovaném rozsahu min/max |

## Výběr

| Typ | Popis |
|-----|-------|
| [select_one listname](select-one) | Výběr přesně jedné možnosti ze seznamu |
| [select_multiple listname](select-multiple) | Výběr jedné nebo více možností ze seznamu |
| [rank listname](rank) | Seřazení voleb podle preference nebo priority |

## Datum a čas

| Typ | Popis |
|-----|-------|
| [date](date) | Datum v kalendáři (rok, měsíc, den) |
| [time](time) | Čas dne (hodiny, minuty) |
| [datetime](datetime-date-time) | Kombinace data a času |

## Poloha

| Typ | Popis |
|-----|-------|
| [geopoint](geopoint) | Jediná GPS souřadnice (zeměpisná šířka, délka, nadmořská výška, přesnost) |
| [geotrace](geotrace) | Cesta — série GPS bodů tvořících linii |
| [geoshape](geoshape) | Oblast — uzavřený polygon GPS bodů |

## Média

| Typ | Popis |
|-----|-------|
| [image](image) | Zachycení fotografie nebo nahrání obrázku |
| [audio](audio) | Zvukový záznam |
| [video](video) | Video záznam |
| [file](file) | Obecné nahrání souboru (PDF, dokument atd.) |

## Ostatní

| Typ | Popis |
|-----|-------|
| [barcode](barcode) | Naskenování čárového kódu nebo QR kódu |
| [note](note) | Zobrazení textu jen pro čtení — zobrazuje instrukce nebo vypočítané souhrny |
| [calculate](calculate) | Skryté pole ukládající vypočítanou hodnotu |
| [hidden](hidden) | Skryté pole ukládající statickou nebo předvyplněnou hodnotu |
| [trigger / acknowledge](trigger) | Zaškrtávací políčko, které musí enumerátor zaškrtnout pro potvrzení přečtení prohlášení |
| [meta](meta) | Automatická metadata: časová razítka, ID zařízení, informace o enumerátorovi |

## Rozšíření rtSurvey

Tyto typy jsou specifické pro rtSurvey a nejsou součástí standardní specifikace XLSForm.

| Typ | Popis |
|-----|-------|
| [search-autocomplete](search-autocomplete) | Textový vstup s návrhy automatického doplňování na základě API v reálném čase |
| [mentions](mentions) | Textové pole s automatickým doplňováním `@`-zmínek pro označování entit inline |
| [texttags](texttags) | Pole pro zadávání tagů — každý záznam se stane odstraňovacím čipem; uloženo jako řetězec oddělený mezerami |

Pro skupiny opakování viz [Repeats](../advanced-extension/repeats)

## Jak typ a vzhled spolupracují

`type` určuje **jaká data se sbírají**. Sloupec `appearance` řídí **jak widget vypadá**. Mnoho typů podporuje více vzhledů — například `select_one` může vypadat jako přepínače, rozbalovací nabídka, Likertova škála nebo kompaktní mřížka.

Viz [Vzhled](../appearance) pro úplný seznam možností.
