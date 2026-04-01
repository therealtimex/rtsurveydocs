---
title: "Range"
description: "A range kérdések lehetővé teszik a válaszadók számára, hogy egy számot válasszanak egy csúszka húzásával a meghatározott minimális és maximális érték között."
icon: "sliders"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 238
---

A `range` kérdéstípus egy **csúszkát** (vagy azzal egyenértékű beviteli elemet) jelenít meg, amellyel a válaszadók egy meghatározott minimum és maximum közötti számot választhatnak. Ideális értékelések, elégedettségi pontszámok vagy bármilyen numerikus érték gyűjtéséhez, ahol vizuálisan szeretné korlátozni a tartományt szövegbevitel helyett.

## Alapvető XLSForm-specifikáció

| type | name | label | parameters |
|------|------|-------|------------|
| range | satisfaction | Mennyire elégedett a szolgáltatással? | start=1 end=5 step=1 |

A `parameters` oszlop határozza meg a csúszka határait és lépésközeit:

| Paraméter | Leírás | Alapértelmezett |
|-----------|--------|-----------------|
| `start` | Minimális érték (beleszámítva) | 0 |
| `end` | Maximális érték (beleszámítva) | 10 |
| `step` | Lépésköz az érvényes értékek között | 1 |

A standard range kérdéstípus részleteiről lásd az [XLSForm specifikációt](https://xlsform.org/en/#question-types).

## Felhasználási területek

A range kérdések általánosan használt területei:

1. Elégedettségi vagy értékelési skálák (pl. 1–5 vagy 0–10)
2. Likert-típusú numerikus skálák
3. Mérések gyűjtése, ahol csak diszkrét értékek érvényesek
4. Korcsoport- vagy pontszámtartományok, ahol a csúszka jobb felhasználói élményt nyújt, mint a szövegmező

## Példa

### Alap értékelési skála

| type | name | label | parameters |
|------|------|-------|------------|
| range | overall_rating | Általános értékelés (0–10) | start=0 end=10 step=1 |

### Tizedes lépésköz

| type | name | label | parameters |
|------|------|-------|------------|
| range | weight_kg | Testsúly (kg) | start=0 end=200 step=0.5 |

### Az érték felhasználása számításban

| type | name | label | parameters | calculation |
|------|------|-------|------------|-------------|
| range | score | Tesztpontszám (0–100) | start=0 end=100 step=5 | |
| calculate | grade | | | if(${score} >= 90, 'A', if(${score} >= 80, 'B', if(${score} >= 70, 'C', 'F'))) |
| note | grade_note | Az osztályzata: ${grade} | | |

## Megjelenés

A `range` típus alapértelmezés szerint csúszkaként jelenik meg. Az alap használathoz nem szükséges további appearance értékeket megadni. Web-formuláron a `horizontal` megjelenéssel szélesebb elrendezéssel kombinálható:

| type | name | label | parameters | appearance |
|------|------|-------|------------|------------|
| range | nps | Mennyire valószínű, hogy ajánlana minket? (0–10) | start=0 end=10 step=1 | horizontal |

## Bevált módszerek

1. Mindig adjon meg értelmes `start`, `end` és `step` értékeket – ne támaszkodjon az alapértelmezettekre.
2. Jelölje a skála végpontjait a `hint` oszlopban (pl. `hint: 0 = Nagyon elégedetlen, 10 = Nagyon elégedett`), hogy kontextust adjon a válaszadóknak.
3. 5 fokozatú Likert-skálához használjon `start=1 end=5 step=1` értéket 0–4 helyett, mivel a válaszadók elvárják, hogy az „1" a legalacsonyabbat jelölje.
4. Használjon `range`-et `integer` + korlát helyett, ha a bevitel korlátozott jellege a kérdés tervezésének részét képezi (a csúszka vizuálisan kommunikálja a skálát).

## Korlátozások

- A csúszka widget nem ideális nagyon széles tartományokhoz (pl. 0–10000) – a korláttal ellátott `integer` szövegmező ezekben az esetekben felhasználóbarátabb.
- Mobileszközökön a finom lépésközök (pl. `step=0.1`) érintőcsúszkával nehezen irányíthatók pontosan.
