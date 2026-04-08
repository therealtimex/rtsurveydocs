---
title: "Search Autocomplete"
description: "Teksto laukas su automatiniu papildymu, kuris ieško parinkčių iš nuotolinio API rašant."
icon: "search"
date: "2026-04-08T00:00:00+00:00"
lastmod: "2026-04-08T00:00:00+00:00"
draft: false
toc: true
weight: 260
---

Klausimo tipas `search-autocomplete` renderuoja teksto įvesties lauką, kuris vartotojui rašant vaicina nuotolinį API ir pateikia atitinkamus rezultatus kaip išskleidžiamąjį sąrašą. Pasirinkta reikšmė saugoma kaip teksto eilutė. Skirtingai nuo `select_one` su `search-api()`, `search-autocomplete` traktuoja rezultatą kaip paprastą tekstą — XLSForm nėra fiksuoto pasirinkimų sąrašo.

## Pagrindinė XLSForm specifikacija

| type | name | label | appearance |
|------|------|-------|------------|
| search-autocomplete | facility_name | Ieškoti įstaigos | `searchApi("/api/facilities", "name")` |

`searchApi()` išraiška įterpiama į stulpelį `appearance` ir kontroliuoja, kuris API galapunktas yra vaicijamas ir kuris atsakymo laukas naudojamas kaip rodoma reikšmė.

## `searchApi()` sintaksė

```
searchApi("url", "display_field")
searchApi("url", "display_field", "value_field")
```

| Parametras | Privalomas | Aprašymas |
|------------|------------|-----------|
| `url` | Taip | Galapunkto URL. Pridėkite užklausos parametrus su `?q=##QUERY##` — `##QUERY##` pakeičiamas įvestu tekstu vykdymo metu |
| `display_field` | Taip | JSON lauko pavadinimas iš API atsakymo, rodomas išskleidžiamajame sąraše |
| `value_field` | Ne | JSON lauko pavadinimas, saugomas kaip atsakymo reikšmė (numatytasis — `display_field`) |

### Pavyzdys: ieškoti įstaigų, saugoti įstaigos ID

| type | name | label | appearance |
|------|------|-------|------------|
| search-autocomplete | facility | Įstaigos pavadinimas | `searchApi("/api/facilities?q=##QUERY##", "name", "id")` |

## Variantas: `search-autocomplete-noedit`

Variantas `search-autocomplete-noedit` neleidžia vartotojui pateikti reikšmės, kuri nebuvo pasirinkta iš automatinio papildymo rezultatų. Vartotojas turi pasirinkti iš sąrašo.

| type | name | label | appearance |
|------|------|-------|------------|
| search-autocomplete | patient_id | Paciento ID | `search-autocomplete-noedit searchApi("/api/patients?q=##QUERY##", "full_name", "patient_id")` |

## Naudojimo atvejai

1. Didelių atskaitos duomenų rinkinių paieška (įstaigos, darbuotojai, produktai) neįterpiant visų pasirinkimų į XLSForm
2. Laisvo teksto laukai su pasirinktiniais pasiūlymais (kai `search-autocomplete-noedit` nenaudojamas)
3. Susietos peržvalgos, kur pasirinkta reikšmė užpildo kitus laukus naudojant `calculate`

## Duomenų formatas

Saugoma reikšmė yra paprasta eilutė — arba `value_field` grąžinta reikšmė, arba rodomas tekstas, jei `value_field` nenurodytas.

## Platformos palaikymas

Palaikoma žiniatinklio formose. Mobilusis palaikymas priklauso nuo tinklo ryšio su API galapunktu.

## Apribojimai

- Duomenų rinkimo metu reikalingas tinkle prieinamas API galapunktas.
- Nėra standartinės XLSForm specifikacijos dalis — tik rtSurvey plėtinys.
- Nepalaiko neprisijungusio pasirinkimų talpinimo; naudokite `select_one` su `search-api()`, jei reikalinga neprisijungusi atsarga.
