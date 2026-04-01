---
title: "Számítás"
description: ""
icon: "calculate"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 235
---

A számítás kérdések az XLSForm-ban és az rtSurvey-ben az űrlap más mezőin vagy értékein alapuló számítások elvégzésére szolgálnak. Ezek a kérdések nem jelennek meg a felhasználónak, hanem a háttérben futnak, és eredményeiket tárolják a későbbi felhasználáshoz vagy beküldéshez.

## Szintaxis

Az XLSForm-ban a számítás kérdés a következőképpen definiálható:

| type      | name     | label | calculation |
|-----------|----------|-------|-------------|
| calculate | calc_q1  |       | ${q1} + ${q2} |

- **type**: Mindig "calculate" ennél a kérdéstípusnál.
- **name**: A számítás kérdés egyedi neve.
- **label**: Általában üresen marad, mivel a számítás kérdések nem jelennek meg a felhasználóknak.
- **calculation**: A kiértékelendő képlet.

## Felhasználási területek

A számítás kérdések általánosan használt területei:

1. Aritmetikai műveletek elvégzése
2. Karakterláncok összefűzése
3. Összetett logika vagy függvények alkalmazása
4. Közbenső eredmények tárolása a későbbi felhasználáshoz

## Példák

### Alapvető aritmetika

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | total    | ${price} * ${quantity} |
```

### Karakterlánc összefűzése

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | full_name| concat(${first_name}, ' ', ${last_name}) |
```

### Függvények használata

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | age      | int((today() - ${date_of_birth}) / 365.25) |
```

## Haladó használat az rtSurvey-ben

### pulldata() függvény

Az rtSurvey támogatja a `pulldata()` függvényt a számítás mezőkben, lehetővé téve adatok lekérését külső CSV-fájlokból:

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | city     | pulldata('cities', 'city_name', 'zip_code', ${zip_input}) |
```

#### Szintaxis

A pulldata() alapvető szintaxisa:

```
pulldata('csv_fájlnév', 'visszaadandó_oszlop', 'kulcs_oszlop', ${egyező_érték})
```

- 'csv_fájlnév': A CSV-fájl neve (.csv kiterjesztés nélkül)
- 'visszaadandó_oszlop': A lekérendő adatot tartalmazó oszlopnév
- 'kulcs_oszlop': Az egyeztetendő oszlopnév
- ${egyező_érték}: A kulcsoszlopban keresendő érték (általában egy változó az űrlapból)

#### Fontos megjegyzések

1. A CSV-fájlt az XLSForm feltöltésekor csatolni kell a felmérés telepítésekor.
2. Vesszőket használjon elválasztóként a CSV-fájlban, ne pontosvesszőket.
3. Kerülje a vesszőket a CSV adatmezőkön belül, mivel ezek elemzési problémákat okozhatnak.
4. A pulldata() csak 1:1 arányú kapcsolatokat támogat. Több egyezés esetén csak az elsőt adja vissza.
5. Korlátok lehetnek a kihúzható szöveg hosszán (kb. 76 karakter körül).
6. Használhatja a pulldata() függvényt korlátokban a CSV-adatokkal való bejegyzések ellenőrzéséhez.

### Feltételes számítások

Az if() utasításokat feltételes számításokhoz használhatja:

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | discount | if(${total} > 1000, ${total} * 0.1, 0) |
```

## Bevált módszerek

1. Használjon értelmes neveket a számítás mezőknek az űrlap olvashatóságának javítása érdekében.
2. Kerülje a túlzottan összetett számításokat egyetlen mezőben; szükség esetén bontsa szét azokat.
3. Alaposan tesztelje a számításokat, különösen összetett képletek vagy külső adatok használatakor.
4. Ne feledje, hogy a számítás mezők az űrlap minden kiértékelésekor lefutnak, ami teljesítményre hatással lehet nagyon összetett vagy számos számítás esetén.
5. A pulldata() használatakor győződjön meg arról, hogy a CSV-fájlok helyesen vannak formázva, és alaposan tesztelje az adott adatokkal és az űrlap struktúrájával.

## Korlátozások

- A számítás mezők nem szerkeszthetők közvetlenül a felhasználók által.
- Egy számítás mező eredménye nem látható azonnal, hacsak nem egy megjelenítési mezőben hivatkoznak rá, vagy az űrlap logikájában nem használják.
