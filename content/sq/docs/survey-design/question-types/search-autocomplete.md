---
title: "Search Autocomplete"
description: "Fushë teksti me plotësim automatik që kërkon opsione nga një API i largët gjatë shtypjes."
icon: "search"
date: "2026-04-08T00:00:00+00:00"
lastmod: "2026-04-08T00:00:00+00:00"
draft: false
toc: true
weight: 260
---

Lloji i pyetjes `search-autocomplete` renderueson një hyrje teksti që kërkon një API të largët ndërsa përdoruesi shtype dhe paraqet rezultate të përputhura si listë rënëse. Vlera e zgjedhur ruhet si varg teksti. Ndryshe nga `select_one` me `search-api()`, `search-autocomplete` e trajton rezultatin si tekst i thjeshtë — nuk ka listë zgjedhjesh fikse në XLSForm.

## Specifikimi bazë XLSForm

| type | name | label | appearance |
|------|------|-------|------------|
| search-autocomplete | facility_name | Kërkoni për institucionin | `searchApi("/api/facilities", "name")` |

Shprehja `searchApi()` vendoset në kolonën `appearance` dhe kontrollon cilin pikë fundore API kërkohet dhe cili fushë nga përgjigja përdoret si vlerë shfaqjeje.

## Sintaksa e `searchApi()`

```
searchApi("url", "display_field")
searchApi("url", "display_field", "value_field")
```

| Parametri | I detyrueshëm | Përshkrimi |
|-----------|---------------|------------|
| `url` | Po | URL e pikës fundore. Shtoni parametra kërkimi me `?q=##QUERY##` — `##QUERY##` zëvendësohet me tekstin e shtypur gjatë ekzekutimit |
| `display_field` | Po | Emri i fushës JSON nga përgjigja API për t'u treguar në listën rënëse |
| `value_field` | Jo | Emri i fushës JSON për t'u ruajtur si vlerë e përgjigjes (parazgjedhja është `display_field`) |

### Shembull: Kërko institucione, ruaj ID-in e institucionit

| type | name | label | appearance |
|------|------|-------|------------|
| search-autocomplete | facility | Emri i institucionit | `searchApi("/api/facilities?q=##QUERY##", "name", "id")` |

## Varianti: `search-autocomplete-noedit`

Varianti `search-autocomplete-noedit` parandalon përdoruesin të dorëzojë një vlerë që nuk u zgjodh nga rezultatet e plotësimit automatik. Përdoruesi duhet të zgjedhë nga lista.

| type | name | label | appearance |
|------|------|-------|------------|
| search-autocomplete | patient_id | ID e pacientit | `search-autocomplete-noedit searchApi("/api/patients?q=##QUERY##", "full_name", "patient_id")` |

## Përdorimet

1. Kërkimi i grupeve të mëdha të të dhënave referuese (institucione, staf, produkte) pa ngulitur të gjitha zgjedhjet në XLSForm
2. Fushat e tekstit të lirë me sugjerime opsionale (kur `search-autocomplete-noedit` nuk përdoret)
3. Kërkime të lidhura ku vlera e zgjedhur populllon fusha të tjera nëpërmjet `calculate`

## Formati i të dhënave

Vlera e ruajtur është një varg i thjeshtë — ose vlera e kthyer nga `value_field` ose teksti i shfaqjes nëse nuk specifikohet `value_field`.

## Mbështetja e platformës

Mbështetet në formularët web. Mbështetja mobile varet nga lidhshmëria e rrjetit me pikën fundore API.

## Kufizimet

- Kërkon një pikë fundore API të arritshme nga rrjeti gjatë mbledhjes së të dhënave.
- Nuk është pjesë e specifikimit standard XLSForm — vetëm zgjerim rtSurvey.
- Nuk mbështet ruajtjen e zgjedhjeve offline; përdorni `select_one` me `search-api()` nëse nevojitet rezervë offline.
