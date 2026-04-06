---
title: "Dynamisk sökning"
description: "Dynamisk sökning laddar alternativ från ett fjärr-API i realtid när räknaren skriver, vilket möjliggör stora eller ofta uppdaterade datamängder."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 293
---

**Dynamisk sökning** (kallas även Sök-API) låter ett `select_one`-, `select_multiple`- eller `text`-fält ladda sina alternativ från en fjärrwebbtjänst **vid körning** när räknaren skriver. Det här är rätt tillvägagångssätt när din alternativlista är för stor för att paketeras i en CSV-fil, uppdateras ofta eller kommer från en levande databas.

---

## `search-api()` utseende

Den dynamiska sökningen konfigureras via `appearance`-kolumnen med funktionen `search-api()`:

```
search-api(method, url, post_body, value_column, display, data_path, save_path)
```

### Parametrar

| Parameter | Beskrivning |
|-----------|-------------|
| `method` | Använd alltid `'POST'` |
| `url` | API-slutpunkten att fråga |
| `post_body` | JSON-kropp som skickas till API:et. Använd `%__input__%` som platshållare för räknarens aktuella söktext |
| `value_column` | Nyckeln i svarsobjektet som används som lagrat **värde** |
| `display` | Nyckeln (eller mallen) som används som **etikett** i rullgardinsmenyn. Stöder `##key##`-platshållare och `@{func}`-uttryck |
| `data_path` | JSONPath till arrayen av resultatobjekt i svaret (t.ex. `$.data`, `$.hits.hits.*._source`) |
| `save_path` | Ett namn under vilket råsvaret sparas för användning av andra fält |

---

## Grundläggande exempel

En sökning efter hälsoinrättningar där räknaren skriver en del av inrättningens namn:

| type | name | label | appearance |
|------|------|-------|------------|
| select_one | facility | Välj hälsoinrättning | `search-api('POST', 'https://api.example.com/facilities/search', '{"query": "%__input__%"}', 'id', 'name', '$.results', 'facility_data')` |

API:et tar emot `{"query": "nair"}` när räknaren skriver "nair" och returnerar:

```json
{
  "results": [
    {"id": "HF001", "name": "Nairobi Central Clinic"},
    {"id": "HF002", "name": "Nairobi West Hospital"}
  ]
}
```

Rullgardinsmenyn visar `Nairobi Central Clinic` och `Nairobi West Hospital`; det lagrade värdet är `HF001` eller `HF002`.

---

## Avancerad visningsformatering

### Använda `##key##`-mallar

Visa flera fält i etiketten:

```
search-api('POST', 'https://api.example.com/search', '{"q": "%__input__%"}', 'id', '##name## (##district##)', '$.data', 'res')
```

Visas som: `Nairobi Central Clinic (Nairobi)`.

### Använda `@{func}`-uttryck

Tillämpa villkorlig logik i visningsetiketten:

```
search-api('POST', 'https://api.example.com/search', '{"q": "%__input__%"}', 'id',
  '@{if_else(eq("##status##", "active"), "✓ ##name##", "✗ ##name##")}',
  '$.data', 'res')
```

Aktiva resultat visar `✓ Kliniknamn`; inaktiva visar `✗ Kliniknamn`.

---

## Ange ett standardvärde: `search-default-api()`

Använd `search-default-api()` efter `search-api()` för att förifyla fältet med ett standardval laddat från ett separat API-anrop (t.ex. när en befintlig post redigeras):

```
appearance: search-api(...) search-default-api('POST', 'https://api.example.com/get', '{"id": "##saved_id##"}', 'id', 'name', '$.item')
```

---

## Anpassad separator för select_multiple: `search-default-separator()`

För `select_multiple`-fält, ange hur flera valda värden kopplas samman i den lagrade strängen:

```
appearance: search-api(...) search-default-separator(' || ')
```

Standardseparatorn är ett mellanslag.

---

## Stödda frågtyper

| Frågtyp | Användningsfall |
|---------|-----------------|
| `select_one` | Enkelt val från sökresultat |
| `select_multiple` | Flera val från sökresultat |
| `text` | Autokomplettering — räknaren skriver fritt men kan välja ett förslag |

---

## Använda sparad svarsdata

`save_path` lagrar det fullständiga API-svarsobjektet under det angivna namnet. Andra fält kan referera till det med `pulldata()`:

| type | name | label | calculation |
|------|------|-------|-------------|
| select_one | facility | Välj inrättning | `search-api(..., 'facility_data')` |
| calculate | facility_district | | `pulldata('facility_data', 'district')` |
| calculate | facility_type | | `pulldata('facility_data', 'type')` |

---

## Bästa praxis

1. Se till att din API-slutpunkt svarar inom 1–2 sekunder — långsamma API:er gör sökningen opåsvarlig.
2. Använd `%__input__%` i `post_body` så att API:et bara returnerar matchande resultat, inte hela datamängden.
3. Indexera sökfältet på serversidan (t.ex. Elasticsearch, fulltext-index i databasen) för snabba svar.
4. Begränsa resultaten till 20–50 objekt per fråga — att returnera tusentals resultat motverkar syftet med sökning.
5. Inkludera ett krav på minsta inmatningslängd i API:et för att undvika breda frågor vid enskilda tecken.

## Begränsningar

- Dynamisk sökning kräver nätverksanslutning — den fungerar inte offline.
- `%__input__%`-platshållaren injiceras som den är; sanera indata på serversidan för att förhindra injektionsattacker.
- Komplexa `@{func}`-visningsuttryck kan ha begränsat stöd i alla rtSurvey-klientversioner.
