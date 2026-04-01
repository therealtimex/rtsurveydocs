---
title: "Barcode"
description: "Otázky typu barcode umožňujú skenovanie a zachytávanie dát čiarových kódov v prieskume."
icon: "qr_code_scanner"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 231
---

Typ otázky barcode v XLSForms a rtSurvey umožňuje používateľom skenovať a zachytávať dáta čiarových kódov priamo v prieskume. Táto funkcia je obzvlášť užitočná pre správu zásob, sledovanie produktov alebo akýkoľvek scenár, kde je potrebné rýchle a presné zadávanie kódovaných informácií.

## Základná špecifikácia XLSForm

| type    | name          | label                   |
|---------|---------------|-------------------------|
| barcode | product_code  | Naskenujte čiarový kód produktu|

Pre viac podrobností o základnom type otázky barcode pozrite si [špecifikáciu XLSForm](https://xlsform.org/en/#question-types).

## Použitia

Otázky typu barcode sa bežne používajú pre:

1. Identifikáciu produktov v prieskumoch zásob
2. Sledovanie majetku v terénnych operáciách
3. Overenie vstupeniek alebo ID na podujatiach
4. Rýchle zadávanie kódovaných informácií

## Rozšírenia rtSurvey

Hoci je základná špecifikácia XLSForm pre otázky barcode priamočiara, rtSurvey môže ponúkať ďalšie funkcie alebo prispôsobenia:

1. Podpora pre viacero formátov čiarových kódov (napr. QR kódy, UPC, EAN)
2. Integrácia s fotoaparátom zariadenia pre skenovanie čiarových kódov
3. Možnosť manuálneho zadávania v prípade, že čiarový kód je poškodený alebo ho nemožno naskenovať

## Najlepšie postupy

1. Zabezpečte správne osvetlenie pre presné skenovanie čiarových kódov.
2. Poskytnite používateľom jasné pokyny, ako umiestniť zariadenie pri skenovaní.
3. Zahrňte možnosť manuálneho zadávania ako zálohu v prípade ťažkostí so skenovaním.
4. Pred nasadením prieskumu testujte funkciu skenovania čiarových kódov s rôznymi zariadeniami a typmi čiarových kódov.

## Obmedzenia

- Presnosť skenovania čiarových kódov sa môže líšiť v závislosti od kvality fotoaparátu zariadenia a environmentálnych podmienok.
- Niektoré staršie alebo zariadenia nižšej triedy nemusia podporovať skenovanie čiarových kódov.
- Určité typy čiarových kódov nemusia byť podporované v závislosti od implementácie.

## Príklad použitia

Tu je príklad, ako by ste mohli použiť otázku barcode v prieskume zásob:

| type    | name          | label                   | hint                                      |
|---------|---------------|-------------------------|-------------------------------------------|
| barcode | product_code  | Naskenujte čiarový kód produktu| Umiestnite čiarový kód do rámca     |
| integer | quantity      | Zadajte množstvo produktu  |                                           |
| note    | confirmation  | Naskenovaný produkt: ${product_code}. Množstvo: ${quantity} |           |

V tomto príklade prieskum zachytáva čiarový kód produktu, pýta sa na množstvo a potom zobrazí potvrdzujúcu poznámku so skenovanými informáciami.
