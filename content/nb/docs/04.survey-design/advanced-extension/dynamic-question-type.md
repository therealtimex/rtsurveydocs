---
title: "Dynamisk spørsmålstype"
description: "Dynamisk spørsmålstype lar et felts spørsmålstype og widget bestemmes ved kjøretid basert på et API-svar eller beregnet verdi."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 301
---

Funksjonen **Dynamisk spørsmålstype** lar et felts inndatawidget og valideringsadferd bestemmes **ved kjøretid** i stedet for ved skjemadesigntidspunkt. Dette er en avansert rtSurvey-utvidelse som brukes når typen data som skal samles inn avhenger av en serversidekonfigurasjon, API-svar eller foregående feltverdi.

Et vanlig brukstilfelle er en konfigurerbar inspeksjonssjekkliste der serveren definerer hvilke felt som kreves, hvilken type de er (tekst, heltall, select, osv.) og hvilke alternativer som er tilgjengelige — uten å bygge om skjemaet for hver konfigurasjon.

---

## Slik fungerer det

Et felt merket som en dynamisk spørsmålstype bruker `callapi()` for å hente konfigurasjonen fra et API. API-svaret definerer:

- Inndatatypen som skal gjengis (text, integer, select_one, osv.)
- De tilgjengelige valgene (for select-typer)
- Valideringsregler

Feltet er merket med `specialFeature: isDynamicQuestionType` internt, som forteller skjemmotoren å bruke API-svaret til å konstruere widgeten i stedet for den statiske skjemadefinisjonen.

---

## Oppsett

### Trinn 1: Hent feltkonfigurasjonen

Bruk et `calculate`-felt med `callapi()` for å hente den dynamiske konfigurasjonen:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | field_config | | callapi | `callapi('POST', 'https://api.example.com/field-config', 1, 2, 0, '$.config', 10000, 0, '', '', '{"form_id": "##form_id##", "field_id": "inspection_result"}')` |

### Trinn 2: Referer til konfigurasjonen i det dynamiske feltet

Det dynamiske feltet bruker `callapi-verify()` i `appearance` eller `constraint` for å koble til den hentede konfigurasjonen:

| type | name | label | appearance |
|------|------|-------|------------|
| text | inspection_result | Inspeksjonsresultat | `callapi-verify(dynamicParams)` |

Skjemmotoren leser `field_config` og bestemmer dynamisk om `inspection_result` skal gjengis som et `text`-, `integer`- eller `select_one`-felt.

---

## API-svarformat

API-et bør returnere et JSON-objekt som beskriver feltkonfigurasjonen. Et typisk svar:

```json
{
  "config": {
    "type": "select_one",
    "choices": [
      {"value": "pass", "label": "Bestått"},
      {"value": "fail", "label": "Ikke bestått"},
      {"value": "na", "label": "N/A"}
    ],
    "required": true,
    "constraint": ". != ''"
  }
}
```

---

## Eksempel: Konfigurerbart inspeksjonsskjema

Et inspeksjonsskjema der sjekklisteelementene og svartypene deres hentes fra en server basert på inspeksjonskategorien:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| select_one inspection_type | insp_type | Type inspeksjon | | |
| calculate | checklist_config | | callapi | `callapi('POST', 'https://api.example.com/checklist', 1, 2, 0, '$.items', 10000, 0, '', '', '{"type": "##insp_type##"}')` |
| text | item_1 | Element 1 | `callapi-verify(dynamicParams)` | |
| text | item_2 | Element 2 | `callapi-verify(dynamicParams)` | |
| text | item_3 | Element 3 | `callapi-verify(dynamicParams)` | |

Serveren returnerer riktig widget-type, etikett, valg og validering for hvert element basert på `insp_type`.

---

## Beste praksis

1. Bruk dynamiske spørsmålstyper bare når feltstrukturen genuint varierer ved kjøretid — for statiske skjemaer, bruk standard spørsmålstyper.
2. Sørg for at konfigurasjon-API-et svarer raskt (under 2 sekunder) og er tilgjengelig på feltets nettverk.
3. Definer alltid en fornuftig fallback i skjemaet for tilfellet der API-et er utilgjengelig — et vanlig `text`-felt med en merknad er bedre enn en ødelagt widget.
4. Versjonsstyr API-svarskjemaet — endringer i svarformatet vil påvirke alle aktive skjemaer som bruker det endepunktet.
5. Test alle kombinasjoner av felttyper som API-et kan returnere før distribusjon.

## Begrensninger

- Dynamiske spørsmålstyper krever nettverkstilkobling for å hente konfigurasjonen.
- Det fulle utvalget av widget-typer som er tilgjengelig dynamisk avhenger av rtSurvey-klientversjonen — test målversjonen.
- Dette er en avansert rtSurvey-utvidelse uten tilsvarende i standard XLSForm-spesifikasjonen.
- Feilsøkingsfeil er vanskeligere å spore siden feltdefinisjonen delvis befinner seg i skjemaet og delvis i API-svaret.
