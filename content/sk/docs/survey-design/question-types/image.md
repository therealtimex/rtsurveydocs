---
title: "Image"
description: "Otázky typu image umožňujú respondentom zachytiť a odoslať fotografie ako súčasť prieskumu."
icon: "image"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 227
---

Typ otázky image v XLSForms a rtSurvey umožňuje respondentom zachytiť a odoslať fotografie ako súčasť ich odpovedí v prieskume. Táto funkcia je obzvlášť užitočná na zber vizuálnych dát, dokumentovanie pozorovaní alebo poskytovanie dôkazov v terénnych prieskumoch.

## Základná špecifikácia XLSForm

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| image | photo       | Odfotografujte miesto    |

Pre viac podrobností o základnom type otázky image pozrite si [špecifikáciu XLSForm](https://xlsform.org/en/#question-types).

## Použitia

Otázky typu image sa bežne používajú pre:

1. Dokumentovanie terénnych podmienok alebo pozorovaní
2. Zachytávanie vizuálnych dôkazov vo výskumných štúdiách
3. Zber fotografií pred a po v hodnoteniach dopadov
4. Overenie dokončenia úloh alebo prítomnosti na miestach
5. Zber vizuálnych dát pre vzdialenú analýzu

## Najlepšie postupy

1. Poskytnite jasné pokyny, čo má byť vyfotografované.
2. Zvážte dôsledky pre súkromie a informujte respondentov o tom, ako budú ich fotografie použité.
3. Buďte pozorní na veľkosti súborov a obmedzenia úložiska, najmä pre prieskumy v oblastiach s obmedzenou konektivitou.
4. Uistite sa, že zariadenie má dostatočné úložisko a udelené oprávnenia pre fotoaparát.

## Príklad použitia

Tu je príklad, ako by ste mohli použiť otázku image v prieskume:

| type  | name           | label                                      | hint                                        |
|-------|----------------|--------------------------------------------|--------------------------------------------|
| image | storefront     | Odfotografujte vchod do predajne       | Uistite sa, že názov predajne je jasne viditeľný    |

## Rozšírenia rtSurvey

Hoci je základná špecifikácia XLSForm pre otázky image priamočiara, rtSurvey môže ponúkať ďalšie funkcie alebo prispôsobenia:

1. Nastavenia kvality obrázka (napr. nízke, stredné, vysoké rozlíšenie)
2. Možnosť pridávať popisy alebo tagy k obrázkom
3. Zachytenie viacerých obrázkov pre jednu otázku
4. Integrácia s natívnou aplikáciou fotoaparátu alebo galériou zariadenia

## Manipulácia s dátami

Obrázky zozbierané prostredníctvom tohto typu otázky sú typicky:

1. Uložené v bežnom formáte obrázka (napr. JPG, PNG)
2. Uložené spolu s ostatnými dátami prieskumu, často v samostatnom mediálnom priečinku
3. Dostupné na zobrazenie a analýzu prostredníctvom platformy na správu prieskumov

## Úvahy pre analýzu

Pri používaní otázok image zvážte:

1. Ako budú obrázky analyzované (napr. manuálna kontrola, automatizovaná analýza obrázkov)
2. Dodatočné úložné miesto potrebné pre obrázkové súbory
3. Opatrenia na ochranu súkromia a dát pri ukladaní a manipulácii s fotografiami
4. Potenciálna potreba nástrojov na úpravu alebo organizáciu obrázkov vo fáze analýzy

## Obmedzenia

- Obrázkové súbory môžu byť veľké, čo môže ovplyvniť prenos a ukladanie dát.
- Nie všetky zariadenia môžu mať vysokokvalitné fotoaparáty alebo dostatok úložného priestoru.
- Analýza veľkého počtu obrázkov môže byť časovo náročná.
- So zachytávaním obrázkov, najmä na verejných miestach, môžu byť spojené obavy o súkromie.
