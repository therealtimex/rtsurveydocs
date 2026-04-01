---
title: "Select from file"
description: "select_one_from_file a select_multiple_from_file načítavajú voľby dynamicky z externého CSV alebo XML súboru priloženého k formuláru."
icon: "file-earmark-spreadsheet"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 241
---

`select_one_from_file` a `select_multiple_from_file` fungujú ako `select_one` a `select_multiple`, ale namiesto definovania volieb v **hárku choices** sa voľby načítavajú z **externého CSV alebo XML súboru** priloženého k formuláru. To je užitočné, keď je váš zoznam volieb veľmi dlhý, mení sa často alebo je potrebné ho aktualizovať bez prestavby celého formulára.

## Základná špecifikácia XLSForm

| type | name | label |
|------|------|-------|
| select_one_from_file health_facilities.csv | facility | Vyberte zdravotnícke zariadenie |
| select_multiple_from_file crops.csv | crops | Aké plodiny pestuje domácnosť? |

Názov súboru za názvom typu musí zodpovedať názvu súboru, ktorý prikladáte pri nahrávaní formulára.

## Formát CSV súboru

Váš CSV súbor musí mať aspoň dva stĺpce: `name` (uložená hodnota) a `label` (zobrazený text). Môžete pridať ľubovoľný počet ďalších stĺpcov na filtrovanie.

**health_facilities.csv:**

```
name,label,district,type
HF001,Klinika Centrum,Bratislava,clinic
HF002,Zdravotné centrum Západ,Bratislava,health_centre
HF003,Nemocnica Košice,Košice,hospital
```

## Filtrovanie volieb

Použite stĺpec `choice_filter` na zobrazenie iba volieb zodpovedajúcich aktuálnemu kontextu. Odkazujte na stĺpce CSV priamo ich názvom (bez `${}`):

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one districts.csv | district | Vyberte okres | |
| select_one_from_file health_facilities.csv | facility | Vyberte zariadenie | district = ${district} |

V tomto príklade sa zobrazia iba zariadenia vo vybranom okrese. `district` v `choice_filter` odkazuje na stĺpec `district` v CSV súbore; `${district}` odkazuje na pole formulára s názvom `district`.

## Použitia

Otázky select-from-file sa bežne používajú pre:

1. **Dlhé zoznamy volieb** — zdravotnícke zariadenia, školy, dediny, zoznamy druhov (stovky alebo tisíce položiek)
2. **Frequently updated lists** — keď sa hlavný zoznam mení medzi kolami prieskumu, aktualizujte iba CSV bez prestavby formulára
3. **Zdieľané referenčné dáta** — jeden CSV súbor používaný naprieč viacerými formulármi
4. **Filtrované kaskádové výbery** — načítajte všetky regióny/okresy/dediny v jednom súbore, potom filtrujte podľa nadriadeného výberu

## Prikladanie súboru

Keď nahráte váš formulár do rtSurvey, priložte CSV súbor ako **mediálnu prílohu**. Názov súboru v definícii formulára musí presne zodpovedať názvu súboru prílohy.

{{% alert icon=" " context="warning" %}}
Názvy súborov rozlišujú veľké a malé písmená. `Health_Facilities.csv` a `health_facilities.csv` sa považujú za rôzne súbory.
{{% /alert %}}

## Použitie `choice-label()` so súbormi

Na zobrazenie popisku vybranej voľby v poznámke alebo poli calculate:

| type | name | label | calculation |
|------|------|-------|-------------|
| select_one_from_file health_facilities.csv | facility | Vyberte zariadenie | |
| calculate | facility_label | | choice-label(${facility}, ${facility}) |
| note | summary | Vybrané zariadenie: ${facility_label} | |

## Najlepšie postupy

1. Udržujte vaše CSV súbory pod 5 000 riadkov pre dobrý výkon na mobilných zariadeniach.
2. Vždy zahrňte stĺpce `name` a `label` — ďalšie stĺpce sú voliteľné.
3. Pre kaskádové výbery použite jeden CSV s nadriadeným stĺpcom a filtrujte pomocou `choice_filter`.
4. Verzujte názvy CSV súborov (napr. `facilities_v3.csv`) pri vykonávaní zlomových zmien v štruktúre stĺpcov.
5. Dôkladne testujte filtrovacie výrazy — preklep v `choice_filter` potichu nezobrazí žiadne voľby.

## Obmedzenia

- Veľmi veľké CSV súbory (10 000+ riadkov) môžu spomaliť načítavanie formulára, najmä na zariadeniach nižšej triedy.
- CSV súbory musia byť nahrané spolu s formulárom — nemôžu byť za behu načítané z URL (pre dynamické vyhľadávania použite `search()` alebo `pulldata()`).
- `select_multiple_from_file` je menej bežne podporovaný naprieč klientmi — pred použitím overte kompatibilitu.

## Porovnanie s `search()`

| | `select_one_from_file` | Vzhľad `search()` |
|--|----------------------|----------------------|
| Zdroj volieb | Priložený CSV/XML súbor | Serverový databázový dopyt |
| Funguje offline | Áno (súbor je súčasťou balíka) | Vyžaduje konektivitu |
| Počet volieb | Obmedzený pamäťou zariadenia | Neobmedzený (stránkovaný) |
| Dáta v reálnom čase | Nie | Áno |

Pre veľké, často sa meniace alebo serverové datasety pozrite si [Dynamické vyhľadávanie](../advanced-extension/dynamic-search).
