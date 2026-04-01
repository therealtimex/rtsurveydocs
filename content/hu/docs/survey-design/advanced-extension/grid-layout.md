---
title: "Rácsszerű elrendezés"
description: "A rácsszerű elrendezés lehetővé teszi a mezők CSS-rácsban való elhelyezését egy csoporton belül, így többoszlopos űrlapkialakítást tesz lehetővé."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 296
---

A **Rácsszerű elrendezés** funkció lehetővé teszi a kérdések **többoszlopos rácsban** való elrendezését egy csoporton belül, a `gridformat<>` megjelenési tag segítségével. Ez hasznos sűrű adatbeviteli űrlapoknál, ahol több kapcsolódó mezőt egymás mellé kell helyezni, ahelyett hogy egymás alatt lennének.

---

## Működési elv

A rácsszerű elrendezés két szinten alkalmazható:

1. **A csoport** — állítsa be az `appearance: field-list grid(weight=N)` értéket a rács oszlopainak számának meghatározásához
2. **Minden egyes mező a csoporton belül** — állítsa be az `appearance: gridformat<row=R col=C colspan=S/>` értéket a mező elhelyezéséhez

A rács 12 oszlopos Bootstrap-stílusú rendszert használ. A `weight=N` meghatározza a logikai oszlopok számát; minden oszlop `12/N` Bootstrap-oszlopot foglal el.

---

## Csoportszintű megjelenés

| Megjelenés | Leírás |
|------------|--------|
| `field-list grid(weight=2)` | 2 oszlopos rács (minden oszlop = 6 Bootstrap-oszlop) |
| `field-list grid(weight=3)` | 3 oszlopos rács (minden oszlop = 4 Bootstrap-oszlop) |
| `field-list grid(weight=4)` | 4 oszlopos rács (minden oszlop = 3 Bootstrap-oszlop) |
| `field-list grid(weight=6)` | 6 oszlopos rács (minden oszlop = 2 Bootstrap-oszlop) |

---

## Mezőszintű `gridformat<>` szintaxis

```
gridformat<row=R col=C colspan=S/>
gridformat<row=R col=C colspan=S backgroundcolor=SZÍN/>
```

| Attribútum | Leírás |
|-----------|--------|
| `row` | Sor száma (1-től számozva) |
| `col` | Oszlop száma (1-től számozva, a `weight` által meghatározott rácson belül) |
| `colspan` | Hány oszlopot foglal el ez a mező (alapértelmezett: 1) |
| `backgroundcolor` | Opcionális CSS-szín a mező hátteréhez (pl. `#f0f0f0`, `lightblue`) |

---

## Példa: 2 oszlopos háztartásfelmérési szakasz

| type | name | label | appearance |
|------|------|-------|------------|
| begin_group | demographics | Demográfiai adatok | `field-list grid(weight=2)` |
| text | first_name | Utónév | `gridformat<row=1 col=1/>` |
| text | last_name | Vezetéknév | `gridformat<row=1 col=2/>` |
| integer | age | Kor | `gridformat<row=2 col=1/>` |
| select_one gender | gender | Nem | `gridformat<row=2 col=2/>` |
| text | address | Teljes cím | `gridformat<row=3 col=1 colspan=2/>` |
| end_group | | | |

Ez a következő megjelenítést eredményezi:

```
[ Utónév             ] [ Vezetéknév          ]
[ Kor                ] [ Nem                 ]
[ Teljes cím (mindkét oszlopot lefedi)       ]
```

---

## Példa: 3 oszlopos terülti adatbevitel

| type | name | label | appearance |
|------|------|-------|------------|
| begin_group | plot_data | Parcella adatai | `field-list grid(weight=3)` |
| text | plot_id | Parcella azonosítója | `gridformat<row=1 col=1/>` |
| decimal | area_ha | Terület (ha) | `gridformat<row=1 col=2/>` |
| select_one crop_type | crop | Növénytípus | `gridformat<row=1 col=3/>` |
| decimal | yield | Termés (kg) | `gridformat<row=2 col=1/>` |
| decimal | revenue | Bevétel | `gridformat<row=2 col=2/>` |
| text | notes | Megjegyzések | `gridformat<row=2 col=3/>` |
| end_group | | | |

---

## Háttérszínek

A `backgroundcolor` segítségével vizuálisan megkülönböztetheti a szakaszokat:

| type | name | label | appearance |
|------|------|-------|------------|
| note | section_a | A szakasz | `gridformat<row=1 col=1 colspan=2 backgroundcolor=#e8f4f8/>` |

---

## Bevált módszerek

1. Rácsszerű elrendezést csak **adatintenzív** képernyőknél használjon, ahol az egymás mellé rendezett mezők valóban csökkentik a görgetést.
2. Tartsa a `colspan=1` mezőket rövidnek (azonosítók, kódok, rövid kiválasztók) – a széles feliratok rosszul csonkulnak a keskeny rácsoszlopokban.
3. Használjon `colspan=N` értéket hosszú feliratú vagy többsoros szövegbeviteli mezőkhöz.
4. Tesztelje a legkisebb várt képernyőméreten – a 4 oszlopos rács szűk mobiltelefon-kijelzőn.
5. A rácsszerű elrendezés a webes és táblagépes formátumoknál működik a legjobban; mobiltelefonnál általában legfeljebb 2 oszlopos elrendezés kényelmes.

## Korlátozások

- A `gridformat<>` csak `grid(weight=N)` megjelenéssel rendelkező csoporton belül működik – a legfelső szinten nincs hatása.
- A rácsszerű elrendezés rtSurvey webes bővítmény, és esetleg nem jelenik meg megfelelően más ODK-kompatibilis kliensekben.
- A sor és oszlop elhelyezése az űrlap felépítéskor nem kerül ellenőrzésre – az átfedő mezők mindkettő megjelenik, de töröttnek tűnhet.
