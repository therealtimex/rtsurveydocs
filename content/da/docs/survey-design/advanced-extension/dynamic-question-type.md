---
title: "Dynamisk spørgsmålstype"
description: "Dynamisk spørgsmålstype giver mulighed for at bestemme et felts spørgsmålstype og widget ved kørselstid baseret på et API-svar eller en beregnet værdi."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 301
---

Funktionen **Dynamisk spørgsmålstype** giver mulighed for at bestemme et felts inputwidget og valideringsadfærd **ved kørselstid** snarere end ved formulardesigntidspunktet. Dette er en avanceret rtSurvey-udvidelse, der bruges, når typen af data, der skal indsamles, afhænger af en serversidekonfiguration, et API-svar eller en forudgående feltværdi.

Et almindeligt anvendelsestilfælde er en konfigurerbar inspektionscheckliste, hvor serveren definerer, hvilke felter der er påkrævede, hvilken type de er (tekst, heltal, valgmulighed osv.), og hvilke muligheder der er tilgængelige — uden at genopbygge formularen for hver konfiguration.

---

## Sådan fungerer det

Et felt markeret som en dynamisk spørgsmålstype bruger `callapi()` til at hente sin konfiguration fra et API. API-svaret definerer:

- Den inputtype, der skal gengives (text, integer, select_one osv.)
- De tilgængelige valgmuligheder (for select-typer)
- Valideringsregler

Feltet markeres internt med `specialFeature: isDynamicQuestionType`, som fortæller formularmotoren at bruge API-svaret til at konstruere widgetten frem for den statiske formulardefinition.

---

## Opsætning

### Trin 1: Hent feltkonfigurationen

Brug et `calculate`-felt med `callapi()` til at hente den dynamiske konfiguration:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | field_config | | callapi | `callapi('POST', 'https://api.example.com/field-config', 1, 2, 0, '$.config', 10000, 0, '', '', '{"form_id": "##form_id##", "field_id": "inspection_result"}')` |

### Trin 2: Referer til konfigurationen i det dynamiske felt

Det dynamiske felt bruger `callapi-verify()` i sin `appearance` eller `constraint` for at linke til den hentede konfiguration:

| type | name | label | appearance |
|------|------|-------|------------|
| text | inspection_result | Inspektionsresultat | `callapi-verify(dynamicParams)` |

Formularmotoren læser `field_config` og bestemmer dynamisk, om `inspection_result` skal gengives som et `text`-, `integer`- eller `select_one`-felt.

---

## API-svarformat

API'et skal returnere et JSON-objekt, der beskriver feltkonfigurationen. Et typisk svar:

```json
{
  "config": {
    "type": "select_one",
    "choices": [
      {"value": "pass", "label": "Bestået"},
      {"value": "fail", "label": "Ikke bestået"},
      {"value": "na", "label": "Ikke relevant"}
    ],
    "required": true,
    "constraint": ". != ''"
  }
}
```

---

## Eksempel: Konfigurerbar inspektionsformular

En inspektionsformular, hvor checklisteelementer og deres svartyper hentes fra en server baseret på inspektionskategorien:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| select_one inspection_type | insp_type | Inspektionstype | | |
| calculate | checklist_config | | callapi | `callapi('POST', 'https://api.example.com/checklist', 1, 2, 0, '$.items', 10000, 0, '', '', '{"type": "##insp_type##"}')` |
| text | item_1 | Element 1 | `callapi-verify(dynamicParams)` | |
| text | item_2 | Element 2 | `callapi-verify(dynamicParams)` | |
| text | item_3 | Element 3 | `callapi-verify(dynamicParams)` | |

Serveren returnerer den korrekte widgettype, label, valgmuligheder og validering for hvert element baseret på `insp_type`.

---

## Bedste praksis

1. Brug kun dynamiske spørgsmålstyper, når feltstrukturen rent faktisk varierer ved kørselstid — brug standardspørgsmålstyper til statiske formularer.
2. Sørg for, at konfigurationens API svarer hurtigt (under 2 sekunder) og er tilgængeligt på feltnetværket.
3. Definer altid en fornuftig fallback i formularen for tilfældet, hvor API'et er utilgængeligt — et almindeligt `text`-felt med en note er bedre end en defekt widget.
4. Versionér dit API-svars skema — ændringer i svarformatet vil påvirke alle aktive formularer, der bruger det pågældende endepunkt.
5. Test alle kombinationer af felttyper, som API'et kan returnere, inden udrulning.

## Begrænsninger

- Dynamiske spørgsmålstyper kræver netværksforbindelse for at hente konfigurationen.
- Det fulde udvalg af widgettyper, der er tilgængeligt dynamisk, afhænger af rtSurvey-klientversion — test din målversion.
- Dette er en avanceret rtSurvey-udvidelse uden tilsvarende i standard XLSForm-specifikationen.
- Fejlfinding er sværere at spore, da feltdefinitionen delvis befinder sig i formularen og delvis i API-svaret.
