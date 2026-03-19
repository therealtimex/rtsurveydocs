---
title: "Dinamikus keresés"
description: "A dinamikus keresés valós időben tölt be lehetőségeket egy távoli API-ból a kérdező gépelése közben, lehetővé téve nagy vagy sűrűn frissített adathalmazok kezelését."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 293
---

A **Dinamikus keresés** (más néven Search API) lehetővé teszi, hogy egy `select_one`, `select_multiple` vagy `text` mező **futásidőben** töltsön be lehetőségeket egy távoli webszolgáltatásból, ahogy a kérdező gépel. Ez a megfelelő megközelítés akkor, ha a lehetőségek listája túl nagy ahhoz, hogy CSV-fájlban legyen csomagolva, sűrűn frissül, vagy egy élő adatbázisból származik.

---

## `search-api()` megjelenés

A dinamikus keresés az `appearance` oszlopon keresztül konfigurálható a `search-api()` függvény segítségével:

```
search-api(method, url, post_body, value_column, display, data_path, save_path)
```

### Paraméterek

| Paraméter | Leírás |
|-----------|--------|
| `method` | Mindig `'POST'` |
| `url` | Az API-végpont a lekérdezéshez |
| `post_body` | Az API-nak küldött JSON törzs. Használja a `%__input__%` helyőrzőt a kérdező aktuális keresési szövegéhez |
| `value_column` | A válaszobjektumban tárolt **értékként** használandó kulcs |
| `display` | A legördülő menüben megjelenő **feliratként** használandó kulcs (vagy sablon). Támogatja a `##kulcs##` helyőrzőket és a `@{func}` kifejezéseket |
| `data_path` | JSONPath az eredményobjektumok tömbjéhez a válaszban (pl. `$.data`, `$.hits.hits.*._source`) |
| `save_path` | Név, amely alatt a nyers válasz el van mentve más mezők általi felhasználáshoz |

---

## Alapvető példa

Egészségügyi intézmény keresése, ahol a kérdező az intézmény nevének egy részét gépeli:

| type | name | label | appearance |
|------|------|-------|------------|
| select_one | facility | Válasszon egészségügyi intézményt | `search-api('POST', 'https://api.example.com/facilities/search', '{"query": "%__input__%"}', 'id', 'name', '$.results', 'facility_data')` |

Az API `{"query": "nair"}` értéket kap, amikor a kérdező "nair"-t gépel, és visszaadja:

```json
{
  "results": [
    {"id": "HF001", "name": "Nairobi Central Clinic"},
    {"id": "HF002", "name": "Nairobi West Hospital"}
  ]
}
```

A legördülő menüben megjelenik a `Nairobi Central Clinic` és a `Nairobi West Hospital`; a tárolt érték `HF001` vagy `HF002`.

---

## Haladó megjelenítési formázás

### `##kulcs##` sablonok használata

Több mező megjelenítése a feliratban:

```
search-api('POST', 'https://api.example.com/search', '{"q": "%__input__%"}', 'id', '##name## (##district##)', '$.data', 'res')
```

Megjelenítés: `Nairobi Central Clinic (Nairobi)`.

### `@{func}` kifejezések használata

Feltételes logika alkalmazása a megjelenítési feliratban:

```
search-api('POST', 'https://api.example.com/search', '{"q": "%__input__%"}', 'id',
  '@{if_else(eq("##status##", "active"), "✓ ##name##", "✗ ##name##")}',
  '$.data', 'res')
```

Az aktív eredmények `✓ Klinika neve` formátumban jelennek meg; az inaktívak `✗ Klinika neve` formátumban.

---

## Alapértelmezett érték beállítása: `search-default-api()`

A `search-default-api()` értéket a `search-api()` után használja, hogy a mezőt egy külön API-hívásból betöltött alapértelmezett lehetőséggel töltse fel előre (pl. meglévő rekord szerkesztésekor):

```
appearance: search-api(...) search-default-api('POST', 'https://api.example.com/get', '{"id": "##saved_id##"}', 'id', 'name', '$.item')
```

---

## Egyedi elválasztó a select_multiple esetén: `search-default-separator()`

`select_multiple` mezőknél adja meg, hogyan kötődjön össze a tárolt karakterláncban a több kiválasztott érték:

```
appearance: search-api(...) search-default-separator(' || ')
```

Az alapértelmezett elválasztó szóköz.

---

## Támogatott kérdéstípusok

| Kérdéstípus | Felhasználási mód |
|-------------|-------------------|
| `select_one` | Egyetlen kiválasztás a keresési eredményekből |
| `select_multiple` | Több kiválasztás a keresési eredményekből |
| `text` | Automatikus kiegészítés – a kérdező szabadon gépel, de kiválaszthat javaslatot |

---

## Mentett válasz adatok felhasználása

A `save_path` az API teljes válaszobjektumát tárolja a megadott név alatt. Más mezők hivatkozhatnak rá a `pulldata()` függvénnyel:

| type | name | label | calculation |
|------|------|-------|-------------|
| select_one | facility | Intézmény kiválasztása | `search-api(..., 'facility_data')` |
| calculate | facility_district | | `pulldata('facility_data', 'district')` |
| calculate | facility_type | | `pulldata('facility_data', 'type')` |

---

## Bevált módszerek

1. Győződjön meg arról, hogy az API-végpont 1–2 másodpercen belül válaszol – a lassú API-k reagálatlanná teszik a keresést.
2. Használja a `%__input__%` értéket a `post_body`-ban, hogy az API csak az egyező eredményeket adja vissza, nem az összes adatot.
3. Indexelje a keresési mezőt szerver oldalon (pl. Elasticsearch, adatbázis teljes szöveges index) a gyors válaszadáshoz.
4. Korlátozza az eredményeket lekérésenként 20–50 elemre – több ezer eredmény visszaadása nem éri el a keresés célját.
5. Illesszen be minimális beviteli hossz követelményt az API-ba, hogy elkerülje az egykarakteres bemeneteken induló átfogó lekérdezéseket.

## Korlátozások

- A dinamikus keresés hálózati kapcsolatot igényel – offline módban nem működik.
- A `%__input__%` helyőrző pontosan van beillesztve; szerver oldalon szanitizálja a bemeneteket az injekciós támadások megelőzéséhez.
- Az összetett `@{func}` megjelenítési kifejezések esetleg korlátozott támogatással rendelkeznek az rtSurvey kliensverzióiban.
