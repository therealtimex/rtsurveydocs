---
title: "Geopoint"
description: "Otázky typu geopoint zachytávajú geografické súradnice (zemepisná šírka, zemepisná dĺžka, nadmorská výška a presnosť) ako súčasť prieskumu."
icon: "location_on"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 232
---

Typ otázky geopoint v XLSForms a rtSurvey umožňuje zber geografických súradníc pomocou GPS zariadenia alebo iných lokalizačných služieb. Táto funkcia je obzvlášť užitočná na mapovanie odpovedí prieskumu, sledovanie terénnych aktivít alebo priradenie dát ku konkrétnym miestam.

## Základná špecifikácia XLSForm

| type     | name        | label                           |
|----------|-------------|--------------------------------|
| geopoint | location    | Zaznamenajte aktuálnu polohu     |

Pre viac podrobností o základnom type otázky geopoint pozrite si [špecifikáciu XLSForm](https://xlsform.org/en/#question-types).

## Použitia

Otázky typu geopoint sa bežne používajú pre:

1. Geografické mapovanie odpovedí prieskumu
2. Overenie polohy terénnych aktivít
3. Sledovanie trasy anketárov
4. Priradenie environmentálnych alebo sociálnych dát ku konkrétnym miestam
5. Výpočet vzdialeností alebo plôch v geografických analýzach

## Najlepšie postupy

1. Uistite sa, že zariadenie má povolené lokalizačné služby a udelené oprávnenia.
2. Poskytnite dostatok času na získanie presnej GPS polohy.
3. Zvážte dôsledky pre súkromie a informujte respondentov o zbere údajov o polohe.
4. Používajte v kombinácii s inými typmi otázok na poskytnutie kontextu pre dáta o polohe.

## Príklad použitia

Tu je príklad, ako by ste mohli použiť otázku geopoint v prieskume:

| type     | name           | label                                      | hint                                        |
|----------|----------------|--------------------------------------------|--------------------------------------------|
| geopoint | sample_location| Zaznamenajte miesto odberu vzorky | Stojte na otvorenom priestranstve pre lepší GPS signál |

## Rozšírenia rtSurvey

Hoci je základná špecifikácia XLSForm pre otázky geopoint priamočiara, rtSurvey môže ponúkať ďalšie funkcie alebo prispôsobenia:

1. Integrácia mapy pre vizuálne potvrdenie zachytenej polohy
2. Nastavenia prahov presnosti
3. Možnosť manuálneho zadávania súradníc
4. Integrácia s offline mapami pre vzdialené oblasti

## Formát dát

Dáta geopoint sú typicky ukladané ako reťazec štyroch hodnôt oddelených medzerami:

```
latitude longitude altitude accuracy
```

Napríklad:
```
41.40338 2.17403 30.5 10
```

## Úvahy pre analýzu

Pri používaní otázok geopoint zvážte:

1. Ako budú geografické dáta vizualizované (napr. mapovací softvér)
2. Presnosť zozbieraných súradníc a jej vplyv na analýzu
3. Opatrenia na ochranu súkromia a dát pri manipulácii s dátami o polohe
4. Potenciálna integrácia s nástrojmi GIS (Geografický informačný systém)

## Obmedzenia

- Presnosť sa môže líšiť v závislosti od zariadenia a environmentálnych podmienok.
- GPS signály môžu byť slabé alebo nedostupné vo vnútorných priestoroch alebo oblastiach s prekážkami.
- Zber údajov o polohe môže výrazne ovplyvniť výdrž batérie zariadenia.
- So zberom presných údajov o polohe môžu byť spojené obavy o súkromie.
