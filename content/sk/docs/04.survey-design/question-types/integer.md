---
title: "Integer"
description: "Otázky typu integer umožňujú zadávanie celých čísel v prieskume."
icon: "123"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 222
---

Typ otázky integer v XLSForms a rtSurvey sa používa na zber celočíselných odpovedí. Tento typ otázky je nevyhnutný pre zber numerických dát bez desatinných miest, ako sú počty, vek alebo roky.

## Základná špecifikácia XLSForm

| type    | name  | label                   |
|---------|-------|------------------------|
| integer | age   | Zadajte svoj vek v rokoch|

Pre viac podrobností o základnom type otázky integer pozrite si [špecifikáciu XLSForm](https://xlsform.org/en/#question-types).

## Použitia

Otázky typu integer sa bežne používajú pre:

1. Zadávanie veku
2. Počítanie položiek (napr. počet detí, členov domácnosti)
3. Zadávanie rokov (napr. rok narodenia)
4. Hodnotenie na numerickej škále
5. Akýkoľvek zber celočíselných dát

## Rozšírenia rtSurvey

Hoci je základná špecifikácia XLSForm pre otázky typu integer priamočiara, rtSurvey môže ponúkať ďalšie funkcie alebo prispôsobenia:

1. Overenie rozsahu
2. Vlastné chybové hlásenia
3. Možnosti vzhľadu pre číselný vstup

## Najlepšie postupy

1. Používajte jasné a stručné popisky na určenie očakávaného vstupu.
2. Implementujte obmedzenia rozsahu na zabránenie nerealistickým alebo chybným vstupom.
3. Zvážte použitie nápovedy na poskytnutie príkladov alebo objasnenie očakávaného formátu.
4. Pre veľké čísla zvážte použitie čiarok alebo medzier v popisku na zlepšenie čitateľnosti (napr. „Zadajte počet obyvateľov (do 1 000 000)").

## Obmedzenia a overovanie

Môžete pridať obmedzenia na zabezpečenie, že zadaná hodnota spadá do konkrétneho rozsahu:

| type    | name  | label                   | constraint        | constraint_message                    |
|---------|-------|------------------------|-------------------|---------------------------------------|
| integer | age   | Zadajte svoj vek v rokoch| .>0 and .<=120    | Vek musí byť medzi 1 a 120 rokmi   |

## Príklad použitia

Tu je príklad, ako by ste mohli použiť otázky typu integer v prieskume domácnosti:

| type    | name           | label                                     | constraint | constraint_message                |
|---------|----------------|-------------------------------------------|------------|-----------------------------------|
| integer | household_size | Koľko ľudí žije vo vašej domácnosti?   | .>0        | Veľkosť domácnosti musí byť aspoň 1 |
| integer | num_children   | Koľko detí do 18 rokov je v domácnosti? | .>=0    | Počet detí nemôže byť záporný |
| integer | year_built     | V ktorom roku bol váš dom postavený?        | .>1800 and .<=2023 | Rok musí byť medzi 1800 a 2023 |

## Výpočty s hodnotami integer

Hodnoty integer možno použiť vo výpočtoch. Tu je príklad:

| type    | name           | label                                     |
|---------|----------------|-------------------------------------------|
| integer | num_adults     | Počet dospelých v domácnosti         |
| integer | num_children   | Počet detí v domácnosti       |
| calculate | total_members | | 

V riadku calculate môžete použiť:

```
calculation | ${num_adults} + ${num_children}
```

Toto sčíta počet dospelých a detí na získanie celkového počtu členov domácnosti.
