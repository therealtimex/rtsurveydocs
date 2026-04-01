---
title: "Dynamické vyhledávání"
description: "Dynamické vyhledávání načítá volby ze vzdáleného API v reálném čase při psaní enumerátora, umožňující velké nebo často aktualizované datové sady."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 293
---

**Dynamické vyhledávání** (také nazývané Search API) umožňuje poli `select_one`, `select_multiple` nebo `text` načítat volby ze vzdálené webové služby **za běhu** při psaní enumerátora. To je správný přístup, když je váš seznam voleb příliš velký pro zahrnutí do CSV souboru, je často aktualizován nebo pochází z živé databáze.

---

## Vzhled `search-api()`

Dynamické vyhledávání je konfigurováno přes sloupec `appearance` pomocí funkce `search-api()`:

```
search-api(method, url, post_body, value_column, display, data_path, save_path)
```

### Parametry

| Parametr | Popis |
|----------|-------|
| `method` | Vždy použijte `'POST'` |
| `url` | Koncový bod API pro dotazování |
| `post_body` | Tělo JSON odeslané do API. Použijte `%__input__%` jako zástupný symbol pro aktuální text vyhledávání enumerátora |
| `value_column` | Klíč v objektu odpovědi použitý jako uložená **hodnota** |
| `display` | Klíč (nebo šablona) použitý jako **popisek** zobrazený v rozbalovacím menu. Podporuje zástupné symboly `##key##` a výrazy `@{func}` |
| `data_path` | JSONPath k poli výsledných objektů v odpovědi (např. `$.data`, `$.hits.hits.*._source`) |
| `save_path` | Název, pod kterým je uložena nezpracovaná odpověď pro použití jinými poli |

---

## Základní příklad

Vyhledávání zdravotnického zařízení, kde enumerátor zadá část názvu zařízení:

| type | name | label | appearance |
|------|------|-------|------------|
| select_one | facility | Vyberte zdravotnické zařízení | `search-api('POST', 'https://api.example.com/facilities/search', '{"query": "%__input__%"}', 'id', 'name', '$.results', 'facility_data')` |

API přijme `{"query": "nair"}`, když enumerátor zadá „nair" a vrátí:

```json
{
  "results": [
    {"id": "HF001", "name": "Nairobi Central Clinic"},
    {"id": "HF002", "name": "Nairobi West Hospital"}
  ]
}
```

Rozbalovací menu zobrazí `Nairobi Central Clinic` a `Nairobi West Hospital`; uložená hodnota je `HF001` nebo `HF002`.

---

## Pokročilé formátování zobrazení

### Používání šablon `##key##`

Zobrazení více polí v popisku:

```
search-api('POST', 'https://api.example.com/search', '{"q": "%__input__%"}', 'id', '##name## (##district##)', '$.data', 'res')
```

Zobrazí se jako: `Nairobi Central Clinic (Nairobi)`.

### Používání výrazů `@{func}`

Aplikace podmíněné logiky v popisku zobrazení:

```
search-api('POST', 'https://api.example.com/search', '{"q": "%__input__%"}', 'id',
  '@{if_else(eq("##status##", "active"), "✓ ##name##", "✗ ##name##")}',
  '$.data', 'res')
```

Aktivní výsledky zobrazí `✓ Název kliniky`; neaktivní zobrazí `✗ Název kliniky`.

---

## Nastavení výchozí hodnoty: `search-default-api()`

Použijte `search-default-api()` po `search-api()` pro předvyplnění pole výchozí volbou načtenou ze samostatného volání API (např. při editaci existujícího záznamu):

```
appearance: search-api(...) search-default-api('POST', 'https://api.example.com/get', '{"id": "##saved_id##"}', 'id', 'name', '$.item')
```

---

## Vlastní oddělovač pro select_multiple: `search-default-separator()`

Pro pole `select_multiple` určete, jak jsou více vybraných hodnot spojeny v uloženém řetězci:

```
appearance: search-api(...) search-default-separator(' || ')
```

Výchozí oddělovač je mezera.

---

## Podporované typy otázek

| Typ otázky | Případ použití |
|------------|----------------|
| `select_one` | Jeden výběr z výsledků vyhledávání |
| `select_multiple` | Více výběrů z výsledků vyhledávání |
| `text` | Automatické doplňování — enumerátor píše volně, ale může vybrat návrh |

---

## Používání uložených dat odpovědi

`save_path` uloží celý objekt odpovědi API pod daným názvem. Jiná pole na něj mohou odkazovat pomocí `pulldata()`:

| type | name | label | calculation |
|------|------|-------|-------------|
| select_one | facility | Vyberte zařízení | `search-api(..., 'facility_data')` |
| calculate | facility_district | | `pulldata('facility_data', 'district')` |
| calculate | facility_type | | `pulldata('facility_data', 'type')` |

---

## Osvědčené postupy

1. Zajistěte, aby váš koncový bod API odpovídal do 1–2 sekund — pomalá API způsobují, že vyhledávání působí neodpovídavě.
2. Použijte `%__input__%` v `post_body`, aby API vracelo pouze odpovídající výsledky, nikoli celou datovou sadu.
3. Indexujte vyhledávací pole na straně serveru (např. Elasticsearch, databázový full-textový index) pro rychlé odpovědi.
4. Omezte výsledky na 20–50 položek na dotaz — vrácení tisíců výsledků poráží účel vyhledávání.
5. Zahrňte požadavek na minimální délku vstupu v API pro zamezení spouštění širokých dotazů na vstupy s jedním znakem.

## Omezení

- Dynamické vyhledávání vyžaduje připojení k síti — v offline režimu nefunguje.
- Zástupný symbol `%__input__%` je vložen tak, jak je; sanitizujte vstupy na straně serveru pro prevenci injection útoků.
- Komplexní výrazy `@{func}` v zobrazení mohou mít omezenou podporu napříč všemi verzemi klientů rtSurvey.
