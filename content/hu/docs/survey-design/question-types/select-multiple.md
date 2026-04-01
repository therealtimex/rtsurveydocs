---
title: "Select_multiple"
description: "A select_multiple kérdések lehetővé teszik a válaszadók számára, hogy egy vagy több lehetőséget válasszanak egy előre meghatározott listából."
icon: "check_box"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 225
---

A `select_multiple` kérdéstípus olyan listát jelenít meg, amelyből a válaszadó **egy vagy több lehetőséget** választhat. Alapértelmezés szerint a lehetőségek jelölőnégyzetekként jelennek meg. A tárolt érték az összes kiválasztott lehetőség értékéből álló **szóközzel elválasztott lista**.

## Alapvető XLSForm-specifikáció

**survey munkalap:**

| type | name | label |
|------|------|-------|
| select_multiple crops | crops_grown | Milyen növényeket termeszt a háztartás? |

**choices munkalap:**

| list_name | name | label |
|-----------|------|-------|
| crops | maize | Kukorica |
| crops | beans | Bab |
| crops | rice | Rizs |
| crops | vegetables | Zöldségek |
| crops | other | Egyéb |

További részletekért lásd az [XLSForm specifikációt](https://xlsform.org/en/#question-types).

## Tárolt adatformátum

Az exportált oszlop a kiválasztott értékek szóközzel elválasztott listáját tartalmazza:

```
maize beans vegetables
```

Használja a `selected()` függvényt – ne az `=` operátort – a select_multiple értékek kifejezésekben való tesztelésekor (lásd lent).

## Felhasználási területek

A select_multiple kérdések a következőkre használhatók:

1. Több alkalmazható válasz gyűjtése (pl. jövedelemforrások, termesztett növények, tünetek)
2. Jelölőnégyzet típusú beleegyezési elemek (pl. „Jelöljön meg mindent, ami vonatkozik")
3. Nyelvi vagy készségkészletek
4. Bármely kérdés, ahol több válasz egyidejűleg érvényes

## Megjelenési lehetőségek

{{< table >}}
| Megjelenés | Leírás |
|------------|--------|
| *(nincs)* | Alapértelmezett jelölőnégyzetek, soronként egy |
| `minimal` | Legördülő lista több kiválasztással |
| `compact` | Kompakt rács, az oszlopok száma az képernyő szélességéhez igazodik |
| `compact-N` | Kompakt rács, N oszlopra kényszerítve |
| `horizontal` | Vízszintesen elrendezett lehetőségek egy sorban (web) |
| `horizontal-compact` | Vízszintes, kompakt elrendezés (web) |
| `label` | Csak feliratokat jelenít meg, jelölőnégyzetek nélkül (használja a `list-nolabel` mellé) |
| `list-nolabel` | Csak jelölőnégyzeteket jelenít meg, feliratok nélkül (használja a `label` mellé) |
| `columns(N)` | Megjelenítés N oszlopban (rtSurvey-bővítés) |
{{< /table >}}

### Példa: 3 oszlopos kompakt elrendezés

| type | name | label | appearance |
|------|------|-------|------------|
| select_multiple symptoms | symptoms | Jelöljön meg minden megfigyelt tünetet | compact-3 |

## A `selected()` használata kifejezésekben

Mivel a tárolt érték szóközzel elválasztott karakterlánc, a `selected()` függvényt **kötelező** használni egy adott lehetőség kiválasztásának teszteléséhez. Az `=` nem fog helyesen működni.

### `relevant` esetén

Utókérdés megjelenítése csak akkor, ha az „egyéb" ki lett választva:

| type | name | label | relevant |
|------|------|-------|----------|
| select_multiple crops | crops_grown | Milyen növényeket termesztenek? | |
| text | crops_other | Kérjük, adja meg a többi növényt | `selected(${crops_grown}, 'other')` |

### `constraint` esetén

Legalább 2 lehetőség kiválasztásának megkövetelése:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple issues | issues | `count-selected(.) >= 2` | Válasszon legalább 2 problémát |

Maximum 3-ra korlátozás:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple priorities | priorities | `count-selected(.) <= 3` | Legfeljebb 3 prioritást válasszon |

### `calculate` esetén – kiválasztott feliratok összefűzése

A `selected-at()`, `count-selected()` és `choice-label()` kombinálásával olvasható összefoglaló állítható össze:

| type | name | calculation |
|------|------|-------------|
| calculate | crops_summary | join(', ', ${crops_grown}) |

## „Egyik sem" / kizárólagos lehetőség

Általános minta, hogy egy lehetőséget kölcsönösen kizáróvá tesznek az összes többivel szemben. Kényszerítse ki `constraint` segítségével:

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| select_multiple issues | issues | Jelöljön meg minden jelenlévő problémát | `not(selected(., 'none') and count-selected(.) > 1)` | Az „Egyik sem" nem választható más lehetőségekkel együtt |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| issues | water | Vízhiány |
| issues | roads | Rossz utak |
| issues | health | Egészségügyi ellátás hiánya |
| issues | none | Egyik sem |

## Kiválasztások számlálása és összesítése

| Függvény | Példa | Eredmény |
|----------|-------|----------|
| `count-selected(field)` | `count-selected(${crops_grown})` | Kiválasztott lehetőségek száma |
| `selected(field, value)` | `selected(${crops_grown}, 'maize')` | igaz/hamis |
| `selected-at(field, index)` | `selected-at(${crops_grown}, 0)` | Első kiválasztott érték |
| `choice-label(field, value)` | `choice-label(${crops_grown}, 'maize')` | Egy érték felirata |

## Bevált módszerek

1. Mindig használjon `selected()` függvényt a `relevant`, `constraint` és `calculate` esetén – soha ne `=` vagy `!=` operátort.
2. Adjon hozzá korlátot a kiválasztások maximális számának korlátozásához, ha a kérdés tervezése megkívánja.
3. Foglalja bele a „Egyik sem" vagy „Nem alkalmazható" lehetőséget, ha nulla kiválasztás érvényes válasz.
4. Hosszú listáknál (15+ lehetőség) használjon `minimal` (legördülő lista) megjelenítést a túlzott görgetés elkerüléséhez.
5. Exportálja az adatokat és az elemzőeszközben végezzen szöveg-szétbontást – a szóközzel elválasztott formátumhoz felosztás szükséges a pivot előtt.

## Korlátozások

- A select_multiple értékek nem hasonlíthatók közvetlenül `=` operátorral össze. Mindig használja a `selected()` függvényt.
- A kompakt megjelenítés nagyon hosszú lehetőség-feliratoknál nem feltétlenül jól jelenik meg.
- Lehetőségek szűrésekor a `choice_filter` az összes megjelenített lehetőségre vonatkozik, ugyanúgy mint a `select_one` esetén.
