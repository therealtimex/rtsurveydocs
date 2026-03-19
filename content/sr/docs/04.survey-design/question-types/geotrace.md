---
title: "Geotrace"
description: "Pitanja tipa geotrace dozvoljavaju ispitanicima da uhvate niz povezanih tačaka na mapi, stvarajući linije ili putanje kao deo ankete."
icon: "timeline"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 234
---

Tip pitanja geotrace u XLSForm-ovima i rtSurvey-u omogućava ispitanicima da uhvate niz povezanih tačaka na mapi, stvarajući linije ili putanje. Ova funkcija je posebno korisna za mapiranje ruta, granica ili linearnih karakteristika u prostornim anketama.

## Osnovna XLSForm specifikacija

| type     | name        | label                           |
|----------|-------------|--------------------------------|
| geotrace | river_path  | Pratite tok reke                |

Za više detalja o osnovnom tipu pitanja geotrace, pogledajte [XLSForm specifikaciju](https://xlsform.org/en/#question-types).

## Upotrebe

Pitanja tipa geotrace se uobičajeno koriste za:

1. Mapiranje ruta ili putanja preuzetih tokom terenskih istraživanja
2. Praćenje linearnih karakteristika kao što su putevi, reke ili granice
3. Hvatanje obima linearne infrastrukture (npr. cevovodi, dalekovodi)
4. Beleženje putnih pravaca u transportnim studijama
5. Definisanje transekata u ekološkim istraživanjima

## Najbolje prakse

1. Osigurajte da uređaj ima omogućene usluge lokacije i odobrene dozvole.
2. Pružite jasna uputstva o tome kako pratiti putanju i koje karakteristike treba uključiti.
3. Razmotrite korišćenje satelitskih snimaka ili osnovnih mapa kako biste pomogli ispitanicima da precizno prate putanje.
4. Budite svesni potencijalne složenosti tragova i njihovog uticaja na veličinu i obradu podataka.

## Primer upotrebe

Evo primera kako biste mogli koristiti pitanje tipa geotrace u anketi:

| type     | name           | label                                      | hint                                        |
|----------|----------------|--------------------------------------------|--------------------------------------------|
| geotrace | hiking_trail   | Pratite putanju planinarske staze          | Počnite od polazišta i završite na vrhu |

## rtSurvey proširenja

Dok je osnovna XLSForm specifikacija za pitanja tipa geotrace jednostavna, rtSurvey može ponuditi dodatne funkcije ili prilagođavanja:

1. Integracija sa offline mapama za udaljena područja
2. Opcije za postavljanje minimalnog i maksimalnog broja tačaka za trag
3. Mogućnost uređivanja ili preciziranja tragova nakon početnog crtanja
4. Podrška za automatsko praćenje u zadatim intervalima tokom kretanja

## Format podataka

Geotrace podaci se obično čuvaju kao string koordinatnih parova razdvojenih razmacima, slično geoshape-u ali bez zatvarajuće tačke:

```
sirina1 duzina1; sirina2 duzina2; sirina3 duzina3; ... sirinaN duzinaN
```

Na primer:
```
38.253094215699576 21.756382658677467; 38.25021274773806 21.756382658677467; 38.25007793942195 21.763892843919166; 38.25290886154963 21.763935759263404
```

## Razmatranja za analizu

Kada koristite pitanja tipa geotrace, razmotrite:

1. Kako će geografski podaci biti vizualizovani i analizirani (npr. GIS softver)
2. Potencijalnu potrebu za čišćenjem ili pojednostavljivanjem složenih tragova
3. Mere privatnosti i zaštite podataka za rukovanje detaljnim prostornim podacima
4. Integraciju sa drugim prostornim izvorima podataka za sveobuhvatnu analizu

## Ograničenja

- Praćenje preciznih putanja na malim mobilnim ekranima može biti izazovno.
- Složeni tragovi mogu zahtevati značajan kapacitet za skladištenje i obradu.
- Kontinuirano korišćenje GPS-a za automatsko praćenje može brzo isprazniti bateriju uređaja.
- Mogu postojati problemi sa privatnošću vezani za prikupljanje detaljnih podataka o putanji.
