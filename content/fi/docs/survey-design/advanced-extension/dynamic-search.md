---
title: "Dynaaminen haku"
description: "Dynaaminen haku lataa valinnat etäpalvelimelta API:n kautta reaaliaikaisesti luetteloijan kirjoittaessa, mahdollistaen suuret tai usein päivittyvät tietoaineistot."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 293
---

**Dynaaminen haku** (tunnetaan myös nimellä Search API) mahdollistaa `select_one`-, `select_multiple`- tai `text`-kentän valintojen lataamisen etäpalvelulta **suorituksenaikaisesti** luetteloijan kirjoittaessa. Tämä on oikea lähestymistapa, kun valintalista on liian suuri sisällytettäväksi CSV-tiedostoon, päivittyy usein tai tulee live-tietokannasta.

---

## `search-api()`-ulkoasu

Dynaaminen haku konfiguroidaan `appearance`-sarakkeessa käyttämällä `search-api()`-funktiota:

```
search-api(method, url, post_body, value_column, display, data_path, save_path)
```

### Parametrit

| Parametri | Kuvaus |
|-----------|--------|
| `method` | Käytä aina `'POST'` |
| `url` | Kyselyyn käytettävä API-päätepiste |
| `post_body` | API:lle lähetetty JSON-runko. Käytä `%__input__%` paikkamerkkinä luetteloijan nykyiselle hakutekstille |
| `value_column` | Avain vastausobjektissa, jota käytetään tallennetuksi **arvoksi** |
| `display` | Avain (tai malli) pudotusvalikossa näytettäväksi **otsikoksi**. Tukee `##key##`-paikkamerkkejä ja `@{func}`-lausekkeita |
| `data_path` | JSONPath tulosobjektien taulukkoon vastauksessa (esim. `$.data`, `$.hits.hits.*._source`) |
| `save_path` | Nimi, jonka alle raaka vastaus tallennetaan muiden kenttien käyttöön |

---

## Perusesimerkki

Terveydenhuollon toimipaikan haku, jossa luetteloija kirjoittaa osan toimipaikan nimestä:

| type | name | label | appearance |
|------|------|-------|------------|
| select_one | facility | Valitse terveydenhuollon toimipaikka | `search-api('POST', 'https://api.example.com/facilities/search', '{"query": "%__input__%"}', 'id', 'name', '$.results', 'facility_data')` |

API vastaanottaa `{"query": "nair"}`, kun luetteloija kirjoittaa "nair" ja palauttaa:

```json
{
  "results": [
    {"id": "HF001", "name": "Nairobi Central Clinic"},
    {"id": "HF002", "name": "Nairobi West Hospital"}
  ]
}
```

Pudotusvalikko näyttää `Nairobi Central Clinic` ja `Nairobi West Hospital`; tallennettu arvo on `HF001` tai `HF002`.

---

## Edistynyt näyttömuotoilu

### `##key##`-mallien käyttö

Näytä useita kenttiä otsikossa:

```
search-api('POST', 'https://api.example.com/search', '{"q": "%__input__%"}', 'id', '##name## (##district##)', '$.data', 'res')
```

Näytetään muodossa: `Nairobi Central Clinic (Nairobi)`.

### `@{func}`-lausekkeiden käyttö

Sovella ehdollista logiikkaa näyttöotsikossa:

```
search-api('POST', 'https://api.example.com/search', '{"q": "%__input__%"}', 'id',
  '@{if_else(eq("##status##", "active"), "✓ ##name##", "✗ ##name##")}',
  '$.data', 'res')
```

Aktiiviset tulokset näyttävät `✓ Klinikan nimi`; passiiviset näyttävät `✗ Klinikan nimi`.

---

## Oletusarvon asettaminen: `search-default-api()`

Käytä `search-default-api()`:tä `search-api()`:n jälkeen esitäyttääksesi kenttä oletusvalinnalla, joka ladataan erillisestä API-kutsusta (esim. olemassa olevan tietueen muokkaamisen yhteydessä):

```
appearance: search-api(...) search-default-api('POST', 'https://api.example.com/get', '{"id": "##saved_id##"}', 'id', 'name', '$.item')
```

---

## Mukautettu erotin select_multiple:lle: `search-default-separator()`

`select_multiple`-kentille määritä, miten useita valittuja arvoja yhdistetään tallennetussa merkkijonossa:

```
appearance: search-api(...) search-default-separator(' || ')
```

Oletuserotin on välilyönti.

---

## Tuetut kysymystyypit

| Kysymystyyppi | Käyttötapaus |
|---------------|--------------|
| `select_one` | Yksittäinen valinta hakutuloksista |
| `select_multiple` | Useita valintoja hakutuloksista |
| `text` | Automaattinen täydennys — luetteloija kirjoittaa vapaasti mutta voi valita ehdotuksen |

---

## Tallennetun vastausdatan käyttö

`save_path` tallentaa täyden API-vastausobjektin annetun nimen alle. Muut kentät voivat viitata siihen `pulldata()`:llä:

| type | name | label | calculation |
|------|------|-------|-------------|
| select_one | facility | Valitse toimipaikka | `search-api(..., 'facility_data')` |
| calculate | facility_district | | `pulldata('facility_data', 'district')` |
| calculate | facility_type | | `pulldata('facility_data', 'type')` |

---

## Parhaat käytännöt

1. Varmista, että API-päätepiste vastaa 1–2 sekunnin sisällä — hitaat API:t tekevät hausta epämiellyttävää.
2. Käytä `%__input__%` `post_body`-kohdassa niin, että API palauttaa vain vastaavat tulokset eikä koko tietoaineistoa.
3. Indeksoi hakukenttä palvelinpuolella (esim. Elasticsearch, tietokannan kokotekstihakemisto) nopeita vastauksia varten.
4. Rajoita tulokset 20–50 kohteeseen per kysely — tuhansien tulosten palauttaminen vie haun tarkoituksen.
5. Sisällytä API:iin minimikirjoitusmäärän vaatimus välttääksesi laajojen kyselyjen käynnistämistä yksittäisillä merkillä.

## Rajoitukset

- Dynaaminen haku vaatii verkkoyhteyden — se ei toimi offline-tilassa.
- `%__input__%`-paikkamerkki injektoidaan sellaisenaan; suorita palvelinpuolella syötteiden puhdistus injection-hyökkäysten estämiseksi.
- Monimutkaisilla `@{func}`-näyttölausekkeilla saattaa olla rajoitettu tuki kaikissa rtSurvey-asiakasversioissa.
