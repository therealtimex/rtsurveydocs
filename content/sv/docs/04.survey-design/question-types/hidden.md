---
title: "Dolt"
description: "Dolda fält lagrar värden som aldrig visas för respondenten — används för att skicka sammanhang, förifyla data eller lagra mellanresultat."
icon: "eye-slash"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 239
---

Ett `hidden`-fält lagrar ett värde som **aldrig visas för respondenten**. Till skillnad från `calculate` (som beräknar ett värde) används `hidden` för att bära ett **externt tillhandahållet värde** — till exempel ett uppgifts-ID, ett hushålls-ID skickat från ett annat system, eller en räknarkod injicerad när formuläret startas.

## Grundläggande XLSForm-specifikation

| type | name | label |
|------|------|-------|
| hidden | household_id | |

Etiketter krävs inte för dolda fält eftersom ingenting renderas på skärmen.

## Användningsområden

Dolda fält används vanligtvis för:

1. Skicka ett förtilldelat ID från undersökningshanteringssystemet (t.ex. hushålls-ID, ärendenummer, uppgiftskod)
2. Lagra formulärversionen eller driftsättningsmetadata
3. Injicera räknarspecifik konfiguration vid formulärstart
4. Bära data från ett överordnat formulär till ett underordnat formulär i länkade arbetsflöden
5. Lagra ett värde härledd från URL-parametrar när formuläret öppnas via en webblänk

## Ange ett standardvärde

Det vanligaste mönstret är att använda `hidden` med ett `default`-uttryck så att värdet ställs in när formuläret öppnas:

| type | name | default |
|------|------|---------|
| hidden | deployment_code | 'ZONE_A_2024' |
| hidden | form_version | '3.1' |

## Referera till ett dolt fält i beräkningar

Dolda värden kan refereras som vilket annat fält som helst med `${fieldname}`:

| type | name | label | calculation |
|------|------|-------|-------------|
| hidden | zone_code | | |
| calculate | label_prefix | | concat('[', ${zone_code}, '] ') |
| note | intro | ${label_prefix} Välkommen till hushållsundersökningen | |

## Använda hidden med förifyllning / URL-parametrar

När ett webbformulär startas via URL kan du skicka parametrar som fyller i dolda fält. Detta gör det möjligt att förvärladda ett hushålls-ID eller uppgiftskod utan att räknaren skriver det:

```
https://your-server.com/form/FORMID?household_id=H00123&zone_code=NORTH
```

Fältet med namnet `household_id` fylls automatiskt i med `H00123`.

## Bästa praxis

1. Använd `hidden` (inte `calculate`) när värdet **injiceras externt** och inte bör omberäknas.
2. Använd `calculate` när värdet **härleds från andra fält** i formuläret.
3. Sätt alltid ett `default` om det dolda fältet måste ha ett värde — ett dolt fält utan standard är tomt.
4. Namnge dolda fält tydligt för att skilja dem (t.ex. prefix med `_hidden_` eller använd en konsekvent namngivningskonvention).

## Begränsningar

- Dolda fält inkluderas i exporterade data precis som vilket annat fält som helst.
- De kan inte visas villkorligt — de är alltid närvarande (men osynliga).
- Om du behöver ett fält som beräknas dynamiskt, använd `calculate` istället.
