---
title: "Rangering"
description: "Rangeringsspørsmål lar respondenter sortere et sett med valg etter preferanse eller prioritet."
icon: "list-ol"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 242
---

`rank`-spørsmålstypen presenterer en liste med valg som respondenten må **dra til en rekkefølge** (eller på annen måte rangere fra første til siste). Den lagrer resultatet som en mellomrom-separert liste over valgte verdier i den valgte rekkefølgen, med det høyest prioriterte valget først.

## Grunnleggende XLSForm-spesifikasjon

| type | name | label |
|------|------|-------|
| rank priorities | main_priority | Ranger disse samfunnsbehovene fra mest til minst viktig |

Valgene er definert i **choices-regnearket** akkurat som `select_one`:

**survey:**

| type | name | label |
|------|------|-------|
| rank priorities | main_priority | Ranger disse behovene fra mest til minst viktig |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| priorities | water | Rent vann |
| priorities | health | Helsetjenester |
| priorities | education | Utdanning |
| priorities | roads | Veier |
| priorities | electricity | Elektrisitet |

## Lagret verdiformat

Den lagrede verdien er en **mellomrom-separert liste** over valgte verdier i rangert rekkefølge (første = høyest prioritet):

```
water education health roads electricity
```

## Hente rangerte posisjoner

Bruk `selected-at()` for å få alternativet på en spesifikk rangering:

| type | name | label | calculation |
|------|------|-------|-------------|
| rank priorities | main_priority | Ranger samfunnsbehov | |
| calculate | top_priority | | selected-at(${main_priority}, 0) |
| calculate | second_priority | | selected-at(${main_priority}, 1) |

`selected-at(${main_priority}, 0)` returnerer verdien plassert **først** (indeks 0 = topprangering).

## Bruke `rank-index()` med repeat-grupper

Når `rank` brukes inne i en repeat-gruppe, lar `rank-index()` deg referere til den ordinale rangeringen fra utenfor repeat-en:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | first_ranked | | rank-index(1, ${score}) |

Se [Funksjoner — Repeterte feltfunksjoner](../operators-and-functions/functions#repeterte-feltfunksjoner) for fullstendige detaljer om `rank-index()` og `rank-index-if()`.

## Brukstilfeller

Rangeringsspørsmål brukes vanligvis for:

1. **Prioritetsrangering** — be samfunn om å rangere utviklingsbehov
2. **Preferanseordering** — rangere produktfunksjoner, tjenesteattributter eller politikkalternativer
3. **Eksamenelementer** — arrangere trinn i en prosess
4. **Topp-N valg** — kombinert med `selected-at()` for å hente bare de øverste 1, 2 eller 3 valgene

## Beste praksis

1. Hold listen kort (3–7 elementer) — rangering blir kognitivt belastende utover 7–8 valg.
2. Bruk klare, gjensidig utelukkende valgetiketter for å unngå forvirring om hva "første" betyr.
3. Legg til hinttekst som forklarer rangeringsretningen (f.eks. "Dra til rekkefølge: første = viktigst").
4. Valider med `count-selected(.) = x` hvis du trenger å sikre at alle valg er rangert.

## Begrensninger

- Dra-for-å-rangere-widgeten krever en berøringsskjerm eller mus — den fungerer kanskje ikke bra i tastaturbaserte miljøer.
- På noen eldre mobilklienter kan rangerings-widgeten falle tilbake til et nummerert inndatagrensesnitt.
- Du kan ikke delvis rangere (dvs. rangere bare noen valg) — alle valg må ordeneres.
