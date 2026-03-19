---
title: "Geopoint"
description: "A geopoint kérdések az eszköz GPS-ének vagy más helymeghatározó szolgáltatásainak segítségével rögzítik a földrajzi koordinátákat."
icon: "location_on"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 232
---

Az XLSForm és az rtSurvey geopoint kérdéstípusa lehetővé teszi az eszköz GPS-ét vagy más helymeghatározó szolgáltatásait felhasználva a földrajzi koordináták összegyűjtését. Ez a funkció különösen hasznos a felmérési válaszok térképezéséhez, a terepi tevékenységek nyomon követéséhez vagy az adatok konkrét helyszínekhez való kötéséhez.

## Alapvető XLSForm-specifikáció

| type     | name        | label                           |
|----------|-------------|--------------------------------|
| geopoint | location    | Rögzítse az aktuális helyszínt  |

A geopoint kérdéstípus alapvető részleteiről lásd az [XLSForm specifikációt](https://xlsform.org/en/#question-types).

## Felhasználási területek

A geopoint kérdések általánosan használt területei:

1. Felmérési válaszok földrajzi térképezése
2. Terepi tevékenységek helyszínének ellenőrzése
3. Kérdezők útvonalának követése
4. Környezeti vagy szociális adatok konkrét helyszínekhez kötése
5. Távolságok vagy területek kiszámítása földrajzi elemzésekben

## Bevált módszerek

1. Győződjön meg arról, hogy az eszközön engedélyezve van a helymeghatározó szolgáltatás és megvannak az engedélyek.
2. Hagyjon elegendő időt a GPS-nek a pontos koordináta megszerzéséhez.
3. Vegye figyelembe az adatvédelmi következményeket, és tájékoztassa a válaszadókat a helyszín adatok gyűjtéséről.
4. Más kérdéstípusokkal együtt használja a helyszín adatok kontextusának biztosításához.

## Példa

Íme egy példa arra, hogyan lehet geopoint kérdést felhasználni egy felmérésben:

| type     | name           | label                                      | hint                                        |
|----------|----------------|--------------------------------------------|--------------------------------------------|
| geopoint | sample_location| Rögzítse a mintavétel helyszínét | Álljon nyílt területen a jobb GPS-jel érdekében |

## rtSurvey-bővítések

Bár az alapvető XLSForm-specifikáció egyszerű a geopoint kérdéseknél, az rtSurvey további funkciókat kínálhat:

1. Térkép integráció a rögzített helyszín vizuális megerősítéséhez
2. Pontossági küszöbérték beállítások
3. Koordináták manuális bevitelének lehetősége
4. Integráció offline térképekkel távoli területeken

## Adatformátum

A geopoint adatok általában négy szóközzel elválasztott értékből álló karakterláncként kerülnek tárolásra:

```
szélességi_fok hosszúsági_fok tengerszint_feletti_magasság pontosság
```

Például:
```
41.40338 2.17403 30.5 10
```

## Elemzési szempontok

A geopoint kérdések használatakor vegye figyelembe:

1. A földrajzi adatok vizualizálásának módját (pl. térképező szoftver)
2. Az összegyűjtött koordináták pontosságát és annak hatását az elemzésre
3. Az adatvédelmi és adatbiztonsági intézkedéseket a helyszínadatok kezeléséhez
4. A lehetséges integrációt GIS-eszközökkel (Geographic Information System)

## Korlátozások

- A pontosság az eszköztől és a környezeti feltételektől függően változhat.
- Beltéren vagy akadályok által körülvett területeken a GPS-jel gyenge vagy nem elérhető.
- A helyszínadatok gyűjtése jelentősen merítheti az eszköz akkumulátorát.
- A pontos helyszínadatok gyűjtésével adatvédelmi aggályok merülhetnek fel.
