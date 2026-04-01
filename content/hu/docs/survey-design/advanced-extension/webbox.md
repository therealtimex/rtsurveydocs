---
title: "Webbox"
description: "A Webbox beágyaz egy külső weblapot a felmérésbe modális iframeként, lehetővé téve a kérdezők számára, hogy megtekinthessék a hivatkozásokat vagy interakcióba léphessenek külső eszközökkel anélkül, hogy elhagynák az űrlapot."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 299
---

A **Webbox** egy külső weblapot ágyaz be a felmérésbe **modális előugró ablakként** (iframe). A kérdező megnyom egy gombot a feliratban vagy megjegyzésmezőben, az oldal teljes képernyős előugró ablakban nyílik meg az űrlapon belül, és bezáráskor pontosan oda tér vissza, ahol járt. Így megjeleníthet hivatkozási anyagot, térképeket, irányítópultokat vagy egyedi eszközöket anélkül, hogy külön böngészőlapot nyitna.

---

## Szintaxis

Illesszen be egy `<webbox>` HTML-taget közvetlenül egy `label` vagy `note` felirat oszlopba:

```html
<webbox src='https://example.com/reference' title='Hivatkozási útmutató'>Hivatkozási útmutató megnyitása</webbox>
```

| Attribútum | Leírás |
|-----------|--------|
| `src` | Az iframebe betöltendő URL. Egyszerű és kettős idézőjeleket is elfogad. |
| `title` | A modális fejlécsávban megjelenített szöveg. Sima szöveget támogat. |
| *(tartalom)* | A felmérési mezőben megjelenő kattintható gomb felirata |

---

## Alapvető példa

| type | name | label |
|------|------|-------|
| note | ref_guide | `<webbox src='https://docs.example.com/field-guide' title='Terepi útmutató'>📖 Terepi útmutató megnyitása</webbox>` |

Ez egy "📖 Terepi útmutató megnyitása" feliratú gombot jelenít meg. Megnyomáskor egy modális ablak nyílik meg, amely a terepi útmutató weboldalát jeleníti meg.

---

## Térkép beágyazása

| type | name | label |
|------|------|-------|
| note | area_map | `<webbox src='https://maps.example.com/survey-area' title='Felmérési terület térképe'>🗺 Térkép megtekintése</webbox>` |

---

## Űrlapértékek átadása a beágyazott oldalnak

Az URL-hez fűzze hozzá az űrlapmező értékeit a `concat()` segítségével a `calculation` oszlopban, és hivatkozzon az eredményre a feliratban:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | webbox_url | | `concat('https://dashboard.example.com/household?id=', ${household_id})` |
| note | hh_dash | `<webbox src='${webbox_url}' title='Háztartás irányítópultja'>Irányítópult megnyitása</webbox>` |

{{% alert icon=" " context="warning" %}}
A `<webbox>` tag `src` attribútuma a `calculate` mezőből számított felirat esetén támogatja a `${mezőnév}` hivatkozásokat. Hozza létre a teljes URL-t egy `calculate` mezőben, és hivatkozzon rá.
{{% /alert %}}

---

## Ismétlési interakció: törlő gombok

A Webbox az ismétlőcsoportok kezeléséhez is támogat speciális akciótagokat a feliratokban:

```html
<delete-repeat-current>Ez a sor törlése</delete-repeat-current>
<delete-repeat-last>Utolsó sor törlése</delete-repeat-last>
```

Ezek olyan gombokként jelennek meg, amelyek megnyomáskor törlik az ismétlési példányokat. Helyezze el őket egy `note` mezőben az ismétlőcsoport belsejében (vagy közvetlenül utána):

| type | name | label |
|------|------|-------|
| begin_repeat | items | Elem |
| text | item_name | Elem neve |
| note | delete_btn | `<delete-repeat-current>✕ Ez az elem törlése</delete-repeat-current>` |
| end_repeat | | |

---

## Kommunikáció a beágyazott oldallal (postMessage)

A webbox iframe és a szülő űrlap kommunikálhat a böngésző `postMessage` API segítségével. A szülő egy `init` üzenetet küld az iframebe megnyitáskor. A beágyazott oldal a következőkkel válaszolhat:

- `delete-repeat-current` — elindítja az aktuális ismétlési példány törlését
- `delete-repeat-last` — elindítja az utolsó ismétlési példány törlését

Ez lehetővé teszi, hogy egyedi webes eszközök (pl. rajzoló eszközök, interaktív térképek) azután indítsanak el űrlapműveleteket, hogy a felhasználó megerősít egy műveletet az iframeben.

---

## Bevált módszerek

1. A Webboxot **hivatkozási anyagokhoz** (irányelvek, keresési táblázatok, térképek) használja – ne az űrlapban szereplő adatgyűjtéshez.
2. Győződjön meg arról, hogy a beágyazott URL elérhető az eszköz hálózatáról – a webbox kapcsolatot igényel.
3. Tartsa a beágyazott oldalt mobilbarátan – a modális ablak maximálisan 800 px széles és a viewport magasságának 80%-a.
4. Használjon leíró gombtextet (pl. "Falutérkép megtekintése"), ahelyett általános feliratot ("Kattintson ide").
5. Tájékoztassa a kérdezőket, hogy a modális ablak bezárása visszaviszi őket a felméréshez – néhány felhasználó esetleg nem tudja, hogyan zárja be az iframe előugró ablakot.

## Korlátozások

- A Webbox hálózati kapcsolatot igényel a beágyazott URL betöltéséhez.
- Egyes külső oldalak az `X-Frame-Options` vagy `Content-Security-Policy` fejlécekkel blokkolják az iframebe való beágyazást – ezeket az oldalakat nem lehet a webboxszal használni.
- A modális ablak bezárul, ha a kérdező elhagyja a kérdést – az iframeben lévő el nem mentett állapot elveszik.
- A Webbox rtSurvey webes bővítmény, és esetleg nem működik más ODK-kompatibilis kliensekben.
