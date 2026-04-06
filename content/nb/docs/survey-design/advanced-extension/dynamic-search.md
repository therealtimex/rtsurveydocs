---
title: "Dynamisk søk"
description: "Dynamisk søk laster alternativer fra et eksternt API i sanntid mens telleren skriver, noe som muliggjør store eller hyppig oppdaterte datasett."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 293
---

**Dynamisk søk** (også kalt Search API) lar et `select_one`-, `select_multiple`- eller `text`-felt laste inn sine alternativer fra en ekstern webtjeneste **ved kjøretid** mens telleren skriver. Dette er riktig tilnærming når valglisten er for stor til å inkludere i en CSV-fil, oppdateres hyppig, eller kommer fra en live database.

---

## `search-api()`-utseende

Det dynamiske søket konfigureres gjennom `appearance`-kolonnen ved hjelp av `search-api()`-funksjonen:

```
search-api(method, url, post_body, value_column, display, data_path, save_path)
```

### Parametere

| Parameter | Beskrivelse |
|-----------|-------------|
| `method` | Bruk alltid `'POST'` |
| `url` | API-endepunktet som skal spørres |
| `post_body` | JSON-body sendt til API-et. Bruk `%__input__%` som plassholder for tellerens nåværende søketekst |
| `value_column` | Nøkkelen i svarobjektet som skal brukes som den lagrede **verdien** |
| `display` | Nøkkelen (eller malen) som skal brukes som **etiketten** vist i nedtrekkmenyen. Støtter `##nøkkel##`-plassholdere og `@{func}`-uttrykk |
| `data_path` | JSONPath til matrisen av resultatobjekter i svaret (f.eks. `$.data`, `$.hits.hits.*._source`) |
| `save_path` | Et navn som det rå svaret lagres under for bruk av andre felt |

---

## Grunnleggende eksempel

Et helseinstitusjonsoppslag der telleren skriver inn deler av institusjonsnavnet:

| type | name | label | appearance |
|------|------|-------|------------|
| select_one | facility | Velg helseinstitusjon | `search-api('POST', 'https://api.example.com/facilities/search', '{"query": "%__input__%"}', 'id', 'name', '$.results', 'facility_data')` |

API-et mottar `{"query": "nair"}` når telleren skriver "nair" og returnerer:

```json
{
  "results": [
    {"id": "HF001", "name": "Nairobi Central Clinic"},
    {"id": "HF002", "name": "Nairobi West Hospital"}
  ]
}
```

Nedtrekkmenyen viser `Nairobi Central Clinic` og `Nairobi West Hospital`; den lagrede verdien er `HF001` eller `HF002`.

---

## Avansert visningsformatering

### Bruke `##nøkkel##`-maler

Vis flere felt i etiketten:

```
search-api('POST', 'https://api.example.com/search', '{"q": "%__input__%"}', 'id', '##name## (##district##)', '$.data', 'res')
```

Vises som: `Nairobi Central Clinic (Nairobi)`.

### Bruke `@{func}`-uttrykk

Bruk betinget logikk i visningsetiketten:

```
search-api('POST', 'https://api.example.com/search', '{"q": "%__input__%"}', 'id',
  '@{if_else(eq("##status##", "active"), "✓ ##name##", "✗ ##name##")}',
  '$.data', 'res')
```

Aktive resultater viser `✓ Klinikkens navn`; inaktive viser `✗ Klinikkens navn`.

---

## Angi en standardverdi: `search-default-api()`

Bruk `search-default-api()` etter `search-api()` for å forhåndsutfylle feltet med et standardvalg lastet fra et separat API-kall (f.eks. ved redigering av en eksisterende post):

```
appearance: search-api(...) search-default-api('POST', 'https://api.example.com/get', '{"id": "##saved_id##"}', 'id', 'name', '$.item')
```

---

## Tilpasset separator for select_multiple: `search-default-separator()`

For `select_multiple`-felt, angi hvordan flere valgte verdier kobles sammen i den lagrede strengen:

```
appearance: search-api(...) search-default-separator(' || ')
```

Standard separator er et mellomrom.

---

## Støttede spørsmålstyper

| Spørsmålstype | Brukstilfelle |
|---------------|---------------|
| `select_one` | Enkeltvalg fra søkeresultater |
| `select_multiple` | Flervalg fra søkeresultater |
| `text` | Autofullføring — telleren skriver fritt, men kan velge et forslag |

---

## Bruke lagrede svardata

`save_path` lagrer det fullstendige API-svaret under det gitte navnet. Andre felt kan referere til det med `pulldata()`:

| type | name | label | calculation |
|------|------|-------|-------------|
| select_one | facility | Velg institusjon | `search-api(..., 'facility_data')` |
| calculate | facility_district | | `pulldata('facility_data', 'district')` |
| calculate | facility_type | | `pulldata('facility_data', 'type')` |

---

## Beste praksis

1. Sørg for at API-endepunktet svarer innen 1–2 sekunder — trege API-er gjør søket følges tregt.
2. Bruk `%__input__%` i `post_body` slik at API-et bare returnerer samsvarende resultater, ikke hele datasettet.
3. Indekser søkefeltet på serversiden (f.eks. Elasticsearch, database fulltekstindeks) for raske svar.
4. Begrens resultatene til 20–50 elementer per spørring — å returnere tusenvis av resultater motvirker hensikten med søk.
5. Inkluder et krav om minimumsinputlengde i API-et for å unngå å utløse brede spørringer ved enkeltbokstavsinput.

## Begrensninger

- Dynamisk søk krever nettverkstilkobling — det fungerer ikke frakoblet.
- `%__input__%`-plassholderen settes inn som den er; skaff innsatser på serversiden for å forhindre injeksjonsangrep.
- Komplekse `@{func}`-visningsuttrykk kan ha begrenset støtte på tvers av alle rtSurvey-klientversjoner.
