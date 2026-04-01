---
title: "Geotrace"
description: "Otázky typu geotrace umožňujú respondentom zachytiť sériu prepojených bodov na mape, vytvárajúc čiary alebo trasy ako súčasť prieskumu."
icon: "timeline"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 234
---

Typ otázky geotrace v XLSForms a rtSurvey umožňuje respondentom zachytiť sériu prepojených bodov na mape, vytvárajúc čiary alebo trasy. Táto funkcia je obzvlášť užitočná na mapovanie trás, hraníc alebo lineárnych prvkov v priestorových prieskumoch.

## Základná špecifikácia XLSForm

| type     | name        | label                           |
|----------|-------------|--------------------------------|
| geotrace | river_path  | Sledujte tok rieky     |

Pre viac podrobností o základnom type otázky geotrace pozrite si [špecifikáciu XLSForm](https://xlsform.org/en/#question-types).

## Použitia

Otázky typu geotrace sa bežne používajú pre:

1. Mapovanie trás alebo chodníkov počas terénnych prieskumov
2. Sledovanie lineárnych prvkov ako cesty, rieky alebo hranice
3. Zachytávanie rozsahu lineárnej infraštruktúry (napr. potrubia, elektrické vedenia)
4. Zaznamenávanie cestovných trás v dopravných štúdiách
5. Definovanie transekcií v ekologických prieskumoch

## Najlepšie postupy

1. Uistite sa, že zariadenie má povolené lokalizačné služby a udelené oprávnenia.
2. Poskytnite jasné pokyny, ako sledovať trasu a aké prvky by mali byť zahrnuté.
3. Zvážte použitie satelitných snímok alebo podkladových máp, aby respondenti mohli presne sledovať trasy.
4. Buďte pozorní na potenciálnu zložitosť trás a ich vplyv na veľkosť a spracovanie dát.

## Príklad použitia

Tu je príklad, ako by ste mohli použiť otázku geotrace v prieskume:

| type     | name           | label                                      | hint                                        |
|----------|----------------|--------------------------------------------|--------------------------------------------|
| geotrace | hiking_trail   | Sledujte trasu turistického chodníka         | Začnite pri vstupe na chodník a skončite na vrchole |

## Rozšírenia rtSurvey

Hoci je základná špecifikácia XLSForm pre otázky geotrace priamočiara, rtSurvey môže ponúkať ďalšie funkcie alebo prispôsobenia:

1. Integrácia s offline mapami pre vzdialené oblasti
2. Možnosti nastavenia minimálneho a maximálneho počtu bodov pre trasu
3. Možnosť úpravy alebo spresnenia trás po počiatočnom kreslení
4. Podpora pre automatické sledovanie v nastavených intervaloch počas pohybu

## Formát dát

Dáta geotrace sú typicky ukladané ako reťazec súradnicových párov oddelených medzerami, podobne ako geoshape, ale bez uzatváracieho bodu:

```
lat1 lon1; lat2 lon2; lat3 lon3; ... latN lonN
```

Napríklad:
```
38.253094215699576 21.756382658677467; 38.25021274773806 21.756382658677467; 38.25007793942195 21.763892843919166; 38.25290886154963 21.763935759263404
```

## Úvahy pre analýzu

Pri používaní otázok geotrace zvážte:

1. Ako budú geografické dáta vizualizované a analyzované (napr. GIS softvér)
2. Potenciálnu potrebu čistenia dát alebo zjednodušenia komplexných trás
3. Opatrenia na ochranu súkromia a dát pri manipulácii s podrobnými priestorovými dátami
4. Integráciu s inými priestorovými zdrojmi dát pre komplexnú analýzu

## Obmedzenia

- Sledovanie presných trás na malých mobilných obrazovkách môže byť náročné.
- Komplexné trasy môžu vyžadovať značnú úložnú a procesorovú kapacitu.
- Nepretržité používanie GPS pri automatickom sledovaní môže rýchlo vybiť batériu zariadenia.
- So zberom podrobných dát o trasách môžu byť spojené obavy o súkromie.
