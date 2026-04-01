---
title: "Dinamikus kérdéstípus"
description: "A dinamikus kérdéstípus lehetővé teszi, hogy egy mező kérdéstípusát és widgetjét futásidőben határozza meg egy API-válasz vagy számított érték alapján."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 301
---

A **Dinamikus kérdéstípus** funkció lehetővé teszi, hogy egy mező beviteli widgetjét és ellenőrzési viselkedését **futásidőben** határozza meg, nem az űrlap tervezésekor. Ez egy haladó rtSurvey-bővítmény, amelyet akkor használnak, ha a gyűjteni kívánt adatok típusa egy szerver oldali konfigurációtól, API-választól vagy előző mező értékétől függ.

Tipikus használati eset egy konfigurálható ellenőrzési ellenőrzőlista, ahol a szerver határozza meg, hogy mely mezők szükségesek, milyen típusúak (text, integer, select stb.) és milyen lehetőségek állnak rendelkezésre – anélkül, hogy minden konfigurációhoz újra kellene készíteni az űrlapot.

---

## Működési elv

A dinamikus kérdéstípusként megjelölt mező a `callapi()` segítségével lekéri konfigurációját egy API-ból. Az API-válasz meghatározza:

- A megjelenítendő beviteli típust (text, integer, select_one stb.)
- Az elérhető lehetőségeket (kiválasztós típusoknál)
- Érvényesítési szabályokat

A mezőt belsőleg a `specialFeature: isDynamicQuestionType` jelöléssel látják el, ami utasítja az űrlaprendszert, hogy az API-választ használja a widget létrehozásához a statikus űrlapdefiníció helyett.

---

## Beállítás

### 1. lépés: A mezőkonfiguráció lekérése

Használja a `callapi()` függvényt tartalmazó `calculate` mezőt a dinamikus konfiguráció lekéréséhez:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | field_config | | callapi | `callapi('POST', 'https://api.example.com/field-config', 1, 2, 0, '$.config', 10000, 0, '', '', '{"form_id": "##form_id##", "field_id": "inspection_result"}')` |

### 2. lépés: A konfiguráció hivatkozása a dinamikus mezőben

A dinamikus mező a `callapi-verify()` értéket használja `appearance` vagy `constraint` mezőjében a lekért konfigurációra való hivatkozáshoz:

| type | name | label | appearance |
|------|------|-------|------------|
| text | inspection_result | Ellenőrzés eredménye | `callapi-verify(dynamicParams)` |

Az űrlaprendszer beolvassa a `field_config` értéket, és dinamikusan meghatározza, hogy az `inspection_result` mezőt `text`, `integer` vagy `select_one` mezőként jelenítse meg.

---

## API-válasz formátuma

Az API-nak a mezőkonfigurációt leíró JSON-objektumot kell visszaadnia. Tipikus válasz:

```json
{
  "config": {
    "type": "select_one",
    "choices": [
      {"value": "pass", "label": "Megfelelt"},
      {"value": "fail", "label": "Nem felelt meg"},
      {"value": "na", "label": "Nem alkalmazható"}
    ],
    "required": true,
    "constraint": ". != ''"
  }
}
```

---

## Példa: Konfigurálható ellenőrzési űrlap

Egy ellenőrzési űrlap, ahol az ellenőrzőlista tételeit és azok választípusait a szerver a vizsgálat kategóriája alapján adja le:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| select_one inspection_type | insp_type | Ellenőrzés típusa | | |
| calculate | checklist_config | | callapi | `callapi('POST', 'https://api.example.com/checklist', 1, 2, 0, '$.items', 10000, 0, '', '', '{"type": "##insp_type##"}')` |
| text | item_1 | 1. tétel | `callapi-verify(dynamicParams)` | |
| text | item_2 | 2. tétel | `callapi-verify(dynamicParams)` | |
| text | item_3 | 3. tétel | `callapi-verify(dynamicParams)` | |

A szerver az `insp_type` alapján visszaadja a megfelelő widget típusát, feliratát, lehetőségeit és érvényesítési szabályait minden tételhez.

---

## Bevált módszerek

1. Dinamikus kérdéstípusokat csak akkor használjon, ha a mezőstruktúra valóban változik futásidőben – statikus űrlapoknál standard kérdéstípusokat alkalmazzon.
2. Győződjön meg arról, hogy a konfigurációs API gyorsan (2 másodpercen belül) válaszol és elérhető a terepi hálózaton.
3. Mindig határozzon meg megfelelő tartalék megoldást az API elérhetetlensége esetére – egy egyszerű `text` mező és megjegyzés jobb, mint egy hibás widget.
4. Verziókezelje az API-válasz sémáját – a válaszformátum változásai az összes aktív, az adott végpontot használó űrlapra hatással lesznek.
5. Az üzembe helyezés előtt tesztelje az API által visszaadható összes mezőtípust.

## Korlátozások

- A dinamikus kérdéstípusok hálózati kapcsolatot igényelnek a konfiguráció lekéréséhez.
- A dinamikusan elérhető widget típusok teljes köre az rtSurvey kliensverziójától függ – tesztelje a célverziót.
- Ez egy haladó rtSurvey-bővítmény, amely nem egyenértékű a standard XLSForm specifikációval.
- A hibák nyomkövetése nehezebb, mivel a mezőmeghatározás részben az űrlapban, részben az API-válaszban él.
