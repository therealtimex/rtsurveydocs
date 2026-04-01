---
title: "Kérdések kihagyása"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 280
---

Az ugrási logika – más néven elágazás vagy feltételes logika – lehetővé teszi dinamikus felmérések létrehozását, amelyek alkalmazkodnak a válaszadók válaszaihoz. Az rtSurvey-ben az ugrási logika a `relevant` oszlop segítségével valósítható meg az XLSForm-ban.

## Alapvető ugrási logika

Az alapvető ugrási logika megvalósításához használja a `relevant` oszlopot egy feltétel megadásához:

```
| type           | name          | label                       | relevant            |
|----------------|---------------|-----------------------------|---------------------|
| select_one y_n | likes_pizza   | Szereti a pizzát?           |                     |
| select_multiple pizza_toppings | favorite_topping | Kedvenc feltétek | ${likes_pizza} = 'yes' |
```

Ebben a példában a "Kedvenc feltétek" kérdés csak akkor jelenik meg, ha a válaszadó "igen"-t válaszol a pizza szeretésére vonatkozó kérdésre.

## A relevant kifejezések szintaxisa

- A `${ }` jelöléssel hivatkozhat más kérdési változókra.
- `select_one` kérdéseknél közvetlen összehasonlítást használjon: `${question_name} = 'answer'`
- `select_multiple` kérdéseknél használja a `selected()` függvényt.

## Haladó ugrási logika

### Több feltétel

Több feltételt kombinálhat az `and`, `or` operátorokkal és zárójelekkel:

```
| type    | name  | label                   | relevant                                  |
|---------|-------|-------------------------|-------------------------------------------|
| integer | age   | Hány éves?              |                                           |
| text    | school| Melyik iskolába jár?    | ${age} < 18 and (${location} = 'urban' or ${location} = 'suburban') |
```

### select_multiple kérdések használata

A `select_multiple` kérdéseknél használja a `selected()` függvényt:

```
| type           | name          | label                       | relevant                               |
|----------------|---------------|-----------------------------|-----------------------------------------|
| select_multiple pizza_toppings | favorite_topping | Kedvenc feltétek |                                         |
| text           | cheese_type   | Kedvenc sajtféleség         | selected(${favorite_topping}, 'cheese') |
```

### "Egyéb" lehetőség a feleletválasztásnál

Valósítson meg szabad szöveges "Egyéb" lehetőséget a `relevant` segítségével:

```
| type           | name                  | label                               | relevant                               |
|----------------|----------------------|-------------------------------------|---------------------------------------|
| select_multiple pizza_toppings | favorite_toppings | Milyen feltéteket szeret a legjobban? |                                    |
| text           | favorite_toppings_other | Milyen egyéb feltéteket szeret?   | selected(${favorite_toppings}, 'other') |
```

Ne felejtse el az 'other' lehetőséget felvenni a choices munkalapba.

## rtSurvey-specifikus funkciók

### Dinamikus relevancia

Az rtSurvey lehetővé teszi a számított mezőkön alapuló dinamikus relevanciát:

```
| type      | name       | label              | calculation                   |
|-----------|------------|--------------------|-----------------------------|
| calculate | total_score| Összpontszám       | ${score1} + ${score2} + ${score3} |
| text      | feedback   | Visszajelzés       | ${total_score} > 75             |
```

### Relevancia ismétlésekben

Az rtSurvey támogatja a relevanciát ismétlőcsoportokon belül:

```
| type         | name         | label            | relevant               |
|--------------|--------------|------------------|------------------------|
| begin repeat | child_info   | Gyermek adatai   |                        |
| integer      | child_age    | Gyermek kora     |                        |
| text         | school_name  | Iskola neve      | ${child_age} >= 5      |
| end repeat   |              |                  |                        |
```

### Kaszkádos relevancia

Az rtSurvey hatékonyan kezeli a kaszkádos relevanciát, ahol az egyik kérdés relevanciája egy másiktól függ, amely viszont egy harmadiktól:

```
| type           | name        | label                  | relevant               |
|----------------|-------------|------------------------|------------------------|
| select_one y_n | has_car     | Van autója?            |                        |
| select_one car_type | car_type | Milyen típusú autója van? | ${has_car} = 'yes' |
| text           | model       | Pontos modell          | ${car_type} = 'sedan'  |
```

## Az ugrási logika bevált módszerei az rtSurvey-ben

1. **Tartsa egyszerűen**: Ahol lehetséges, kerülje a túlzottan összetett relevanciafeltételeket.
2. **Alaposan tesztelje**: Az rtSurvey előnézeti funkciójával tesztelje a felmérés összes lehetséges útját.
3. **Vegye figyelembe a teljesítményt**: A nagyon összetett ugrási logika befolyásolhatja a felmérés teljesítményét, különösen mobileszközökön.
4. **Használjon egyértelmű változóneveket**: Ez megkönnyíti a relevanciakifejezések olvashatóságát és karbantarthatóságát.
5. **Dokumentálja a logikát**: Adjon megjegyzéseket az összetett ugrási minták magyarázatához, különösen csapatmunka esetén.
6. **Legyen tudatában az adatelemzési következményeknek**: A kihagyott kérdések hiányzó adatokat eredményeznek. Tervezze meg az elemzést ennek megfelelően.

## Az ugrási logika hibaelhárítása

- **Szintaktikai hibák**: Győződjön meg arról, hogy az összes `${ }` megfelelően zárt és helyesen van írva.
- **Körkörös hivatkozások**: Kerülje az egymástól függő kérdések köreit.
- **Betűk érzékenysége**: Ne feledje, hogy a válaszlehetőségek megkülönböztetik a kis- és nagybetűket a relevanciakifejezésekben.
- **Numerikus összehasonlítások**: Numerikus összehasonlításoknál használja a megfelelő operátorokat (`<`, `>`, `=`).

## Összefoglalás

Az ugrási logika hatékony alkalmazása jelentősen javíthatja a válaszadói élményt és az adatminőséget az rtSurvey projektjeiben. Az rtSurvey haladó funkcióinak kihasználásával és a bevált módszerek követésével dinamikus, hatékony felméréseket hozhat létre, amelyek alkalmazkodnak az egyes válaszadók egyedi helyzetéhez.
