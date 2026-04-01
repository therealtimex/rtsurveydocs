---
title: "Kérdések csoportosítása"
description: ""
icon: "auto_awesome"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 250
---

Az XLSForm-ban a csoportok lehetővé teszik a kapcsolódó kérdések összefogását, javítva a felmérés struktúráját és az adatelemzési lehetőségeket. Az rtSurvey teljes mértékben támogatja az XLSForm-csoportokat, és további funkciókkal egészíti ki azokat.

## Alapvető csoportszerkezet

Kérdéscsoport létrehozásához használja a `begin_group` és `end_group` szintaxist:

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | respondent | Válaszadó adatai                         |
| text         | name       | Adja meg a válaszadó nevét               |
| text         | position   | Adja meg a válaszadó beosztását          |
| end_group    |            |                                          |
```

Főbb pontok:
- A `begin_group` sorhoz szükséges a `name` és a `label`.
- Az `end_group` sorhoz nem szükséges név vagy felirat.
- A `begin_group` és `end_group` közötti kérdések a csoport részét alkotják.

## Csoportmegjelenés

Az rtSurvey különféle megjelenési lehetőségeket támogat a csoportokhoz:

1. **field-list**: Több kérdést jelenít meg ugyanazon a képernyőn.
   ```
   | type         | name       | label     | appearance |
   |--------------|------------|-----------|------------|
   | begin_group  | respondent | Válaszadó | field-list |
   | text         | name       | Név       |            |
   | text         | position   | Beosztás  |            |
   | end_group    |            |           |            |
   ```

2. **grid**: Kompakt, táblázatszerű elrendezést hoz létre a csoportokhoz (rtSurvey-specifikus).
   ```
   | type         | name       | label      | appearance |
   |--------------|------------|------------|------------|
   | begin_group  | household  | Háztartás  | grid       |
   | text         | member_name| Név        |            |
   | integer      | member_age | Kor        |            |
   | end_group    |            |            |            |
   ```

3. **collapsible**: Kinyitható/becsukható csoportokat hoz létre (rtSurvey-specifikus).
   ```
   | type         | name       | label     | appearance  |
   |--------------|------------|-----------|-------------|
   | begin_group  | details    | Részletek | collapsible |
   | text         | address    | Cím       |             |
   | text         | phone      | Telefon   |             |
   | end_group    |            |           |             |
   ```

## Beágyazott csoportok

A csoportok más csoportokon belül is elhelyezhetők összetettebb struktúrák kialakításához:

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | hospital   | Kórház adatai                            |
| text         | hosp_name  | Mi a kórház neve?                        |
| begin_group  | medication | Gyógyszerek elérhetősége                 |
| select_one y_n| hiv_meds  | Van HIV-gyógyszer ebben a kórházban?     |
| end_group    |            |                                          |
| end_group    |            |                                          |
```

**Megjegyzés**: Mindig a legutoljára nyitott csoportot zárja be először a megfelelő beágyazás megőrzéséhez.

## Ugrási logika csoportokhoz

A `relevant` oszlop segítségével ugrási logikát valósíthat meg teljes csoportokhoz:

```
| type         | name   | label                                        | relevant        |
|--------------|--------|----------------------------------------------|-----------------|
| integer      | age    | Hány éves?                                   |                 |
| begin_group  | child  | Gyermek                                      | ${age} <= 5     |
| integer      | muac   | Rögzítse a gyermek felső karkerületét        |                 |
| select_one y_n| mrdt  | Pozitív a gyermek rapid diagnosztikai tesztje?|               |
| end_group    |        |                                              |                 |
```

Ebben a példában a `child` csoport csak akkor jelenik meg, ha a válaszadó 5 éves vagy fiatalabb.

## A csoportok használatának bevált módszerei

1. Használjon értelmes neveket a csoportokhoz az adatelemzés javítása érdekében.
2. Tartsa a csoportokat kapcsolódó kérdésekre összpontosítva.
3. Mértékkel használja a beágyazott csoportokat, kerülje az túlzottan bonyolult struktúrákat.
4. Alaposan tesztelje az ugrási logikát, amikor a `relevant` beállítást csoportokra alkalmazza.
5. Fontolja meg a `field-list` megjelenés használatát rövid csoportokhoz a görgetés csökkentése érdekében.
6. Használja az rtSurvey rácsszerű elrendezését kapcsolódó információk kompakt megjelenítéséhez.
7. Hosszú űrlapokon használjon összecsukható csoportokat a navigáció javítása érdekében.

## rtSurvey-specifikus funkciók

1. **Rácsszerű elrendezés**: Táblázatszerű megjelenítéshez használja a `grid` megjelenést.
2. **Összecsukható csoportok**: Kibontható szakaszok megvalósításához alkalmazza a `collapsible` megjelenést.
3. **Egyedi stílus**: Egyedi CSS-t alkalmazzon csoportokhoz egyedi vizuális kialakításhoz.
4. **Dinamikus csoportviselkedés**: Valósítson meg összetett ugrási logikát és számításokat csoportokon belül.

## Többnyelvű támogatás

Az rtSurvey többnyelvű csoportokat is támogat. Használjon nyelvspecifikus oszlopokat a feliratokhoz:

```
| type         | name       | label::Magyar       | label::English      |
|--------------|------------|---------------------|---------------------|
| begin_group  | personal   | Személyes adatok    | Personal Info       |
| text         | name       | Név                 | Name                |
| end_group    |            |                     |                     |
```

## Mobilalkalmazás szempontjai

- A `field-list` megjelenéssel rendelkező csoportok egyetlen képernyőként jelennek meg a mobilalkalmazásban.
- Az összecsukható csoportok javíthatják a navigációt kisebb képernyőkön.
- A rácsszerű elrendezések alkalmazkodhatnak a jobb láthatósághoz mobileszközökön.

## Ismert korlátozások

- A csoportok rendkívül mély beágyazása befolyásolhatja a teljesítményt egyes eszközökön.
- Egyes haladó stílusbeállítások esetleg nem érhetők el a csoportokhoz a mobilalkalmazásban.

## Csoportok hibaelhárítása

1. Győződjön meg arról, hogy minden `begin_group`-hoz tartozik egy `end_group`.
2. Ellenőrizze, hogy a csoportneveket az űrlapon belül egyediek legyenek.
3. Ellenőrizze, hogy az ugrási logika a helyes kérdésnevekre hivatkozik.
4. Alaposan tesztelje a csoportokat web és mobil felületeken egyaránt.

Az XLSForm-csoportok hatékony használatával az rtSurvey-ben jól szervezett, hatékony felméréseket hozhat létre, amelyek javítják az adatgyűjtési élményt és az adatelemzés minőségét.
