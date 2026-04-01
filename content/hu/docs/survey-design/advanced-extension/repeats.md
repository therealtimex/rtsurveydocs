---
title: "Haladó ismétlések"
description: "Haladó minták ismétlőcsoportokhoz: dinamikus számok, beágyazott ismétlések, ismétlési adatok összefoglalása és értékek hivatkozása ismétlések között."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 295
---

Ez az oldal haladó mintákat tárgyal az rtSurvey ismétlőcsoportjaihoz. Az ismétlőcsoport beállításának alapjairól lásd: [Csoportosítás és ismétlések](../repeats).

---

## Dinamikus ismétlésszám

Alapértelmezés szerint a kérdező dönt arról, hányszor ismételjen. Az ismétlések számát a `repeat_count` segítségével rögzítheti:

| type | name | label | repeat_count |
|------|------|-------|--------------|
| begin_repeat | household_members | Háztartástag | `${num_members}` |
| text | member_name | Tag neve | |
| integer | member_age | Kor | |
| end_repeat | | | |

Az ismétlés pontosan `${num_members}` alkalommal fut le, ahol a `num_members` értékét korábban az űrlapon gyűjtötték. A kérdező nem adhat hozzá vagy távolíthat el példányokat.

---

## Indexelt hozzáférés: `indexed-repeat()`

Egy adott ismétlési példány mezőértékének elérése az ismétlőcsoporton **kívülről** az `indexed-repeat(repeatedField, repeatGroup, index)` segítségével:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | first_name | | `indexed-repeat(${member_name}, ${household_members}, 1)` |
| calculate | second_name | | `indexed-repeat(${member_name}, ${household_members}, 2)` |

Ez hasznos összefoglaló mezők felépítéséhez vagy az ismétlés utáni "elsődleges" tag adataira való hivatkozáshoz.

---

## Aktuális példány pozíciója: `index()`

Az ismétlőcsoporton belül az `index()` az aktuális példány 1-től számozott pozícióját adja vissza. Ezzel az egyes ismétlések megcímkézhetők vagy egyedi azonosítók hozhatók létre:

| type | name | label |
|------|------|-------|
| begin_repeat | plots | Parcella |
| note | plot_label | ${index()}. parcella |
| text | plot_id | Parcella azonosítója |
| end_repeat | | |

---

## Ugyanabban a példányban lévő mezőkre való hivatkozás

Az ismétlésen belül a `${mezőnév}` segítségével hivatkozhat egy másik mezőre **ugyanabban az ismétlési példányban**. Az `indexed-repeat()` nem szükséges ugyanazon a cikluson belül:

| type | name | label | relevant |
|------|------|-------|----------|
| begin_repeat | members | Tag | |
| text | member_name | Név | |
| integer | member_age | Kor | |
| text | school_name | Iskola neve | `${member_age} < 18` |
| end_repeat | | | |

---

## Szülőmezőkre való hivatkozás ismétlésen belülről

Az ismétlőcsoporton kívül (felette) lévő mezőkre normálisan hivatkozhat a `${mezőnév}` segítségével:

| type | name | label |
|------|------|-------|
| text | village | Falu neve |
| begin_repeat | plots | Mezőgazdasági parcella |
| note | plot_context | Parcellák ${village} területén |
| end_repeat | | |

---

## Ismétlési adatok összefoglalása

Az ismétlőcsoporton **kívüli** összesítő függvények használata az összefoglaláshoz:

| Függvény | Példa | Leírás |
|----------|---------|--------|
| `count(group)` | `count(${household_members})` | Példányok száma |
| `sum(field)` | `sum(${loan_amount})` | Numerikus mező összege |
| `min(field)` | `min(${member_age})` | Minimális érték |
| `max(field)` | `max(${member_age})` | Maximális érték |
| `join(sep, field)` | `join(', ', ${member_name})` | Vesszővel elválasztott lista |
| `count-if(group, expr)` | `count-if(${members}, ${member_age} < 18)` | Feltételes számlálás |
| `sum-if(field, expr)` | `sum-if(${loan_amount}, ${loan_amount} > 500)` | Feltételes összegzés |
| `join-if(sep, field, expr)` | `join-if(', ', ${name}, ${age} >= 18)` | Feltételes összefűzés |

### Példa: Háztartás összefoglalója

| type | name | label | calculation |
|------|------|-------|-------------|
| integer | num_members | Hány tag van? | |
| begin_repeat | members | Tag | `${num_members}` |
| text | member_name | Név | |
| integer | member_age | Kor | |
| end_repeat | | | |
| calculate | total_members | | `count(${members})` |
| calculate | children_count | | `count-if(${members}, ${member_age} < 18)` |
| calculate | adult_names | | `join-if(', ', ${member_name}, ${member_age} >= 18)` |
| note | summary | ${total_members} tag; ${children_count} 18 éven aluli. Felnőttek: ${adult_names} | |

---

## Beágyazott ismétlések

Egy ismétlőcsoport tartalmazhat másik ismétlőcsoportot. Ezt óvatosan alkalmazza – a beágyazott ismétlések bonyolultabbak és zavaróak lehetnek a kérdezők számára.

| type | name | label |
|------|------|-------|
| begin_repeat | households | Háztartás |
| text | hh_id | Háztartás azonosítója |
| begin_repeat | hh_members | Tag |
| text | member_name | Tag neve |
| end_repeat | | |
| end_repeat | | |

A belső ismétlésből a külső ismétlés mezőjére való hivatkozáshoz használja a `${mezőnév}` értéket – ez a legközelebbi egyező ősre oldódik fel:

A `hh_members` ismétlésen belül a `${hh_id}` az **aktuális** háztartás azonosítóját adja vissza, nem az összes háztartásét.

---

## Rang ismétlőcsoportokban: `rank-index()`

Ha egy `rank` mező egy ismétlőcsoporton belül van, a `rank-index(instanceNumber, repeatedField)` segítségével kinyerheti egy adott példány rangját az ismétlésen kívülről:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | top_scorer | | `rank-index(1, ${score})` |

A `rank-index(1, ${score})` a legmagasabb pontszámú példány indexét adja vissza.

---

## Bevált módszerek

1. Mindig használjon `repeat_count` értéket, ha az ismétlések száma előre ismert – ez megakadályozza, hogy a kérdezők véletlenül hozzáadjanak vagy eltávolítsanak példányokat.
2. Tartsa az ismétlőcsoportokat fókuszáltan – a 20+ kérdést tartalmazó ismétlési példányok nehézek a navigáláshoz.
3. Névvezze az ismétlőcsoportokat egyértelműen (pl. `household_members`, nem `repeat1`) – a név megjelenik a függvényhívásokban és az exportált adatokban.
4. Tesztelje a maximálisan várt példányszámmal a teljesítmény ellenőrzéséhez.
5. Mobilon használja a `field-list` megjelenést az ismétlőcsoporton, hogy minden mező egy képernyőn jelenjen meg példányonként.

---

## Korlátozások

- Az `indexed-repeat()` érvényes indexet igényel (1-től a példányok számáig) – tartományon kívüli indexek üres értéket adnak vissza.
- A 2 szintnél mélyebb beágyazott ismétlések nem ajánlottak, és egyes kliensekben megjelenítési problémákat okozhatnak.
- Az összesítő függvények (`sum`, `count` stb.) a teljes ismétlőcsoporton működnek – nem lehet a példányok egy részhalmazán összesíteni a `*-if` változatok nélkül.
