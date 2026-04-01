---
title: "Grid-oppsett"
description: "Grid-oppsett lar deg plassere felt i et CSS-grid innenfor en gruppe, noe som muliggjør flerkolonnes skjemadesign."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 296
---

**Grid-oppsett**-funksjonen lar deg arrangere spørsmål i et **flerkolonnet grid** innenfor en gruppe ved hjelp av `gridformat<>`-utseendetegnet. Dette er nyttig for tettere datainntastingsskjemaer der flere relaterte felt bør vises side om side i stedet for stablede vertikalt.

---

## Slik fungerer det

Grid-oppsett brukes på to nivåer:

1. **Gruppen** — sett `appearance: field-list grid(weight=N)` for å definere hvor mange kolonner gridet har
2. **Hvert felt inne i gruppen** — sett `appearance: gridformat<row=R col=C colspan=S/>` for å plassere feltet

Gridet bruker et 12-kolonne Bootstrap-stil system. `weight=N` definerer hvor mange logiske kolonner gridet ditt har; hver kolonne opptar `12/N` Bootstrap-kolonner.

---

## Utseende på gruppenivå

| Utseende | Beskrivelse |
|----------|-------------|
| `field-list grid(weight=2)` | 2-kolonne grid (hver kolonne = 6 Bootstrap-kol) |
| `field-list grid(weight=3)` | 3-kolonne grid (hver kolonne = 4 Bootstrap-kol) |
| `field-list grid(weight=4)` | 4-kolonne grid (hver kolonne = 3 Bootstrap-kol) |
| `field-list grid(weight=6)` | 6-kolonne grid (hver kolonne = 2 Bootstrap-kol) |

---

## `gridformat<>`-syntaks på feltnivå

```
gridformat<row=R col=C colspan=S/>
gridformat<row=R col=C colspan=S backgroundcolor=FARGE/>
```

| Attributt | Beskrivelse |
|-----------|-------------|
| `row` | Radnummer (1-basert) |
| `col` | Kolonnenummer (1-basert, innenfor gridet definert av `weight`) |
| `colspan` | Antall kolonner dette feltet strekker seg over (standard 1) |
| `backgroundcolor` | Valgfri CSS-farge for feltbakgrunnen (f.eks. `#f0f0f0`, `lightblue`) |

---

## Eksempel: 2-kolonne husholdningsundersøkelsesseksjon

| type | name | label | appearance |
|------|------|-------|------------|
| begin_group | demographics | Demografi | `field-list grid(weight=2)` |
| text | first_name | Fornavn | `gridformat<row=1 col=1/>` |
| text | last_name | Etternavn | `gridformat<row=1 col=2/>` |
| integer | age | Alder | `gridformat<row=2 col=1/>` |
| select_one gender | gender | Kjønn | `gridformat<row=2 col=2/>` |
| text | address | Full adresse | `gridformat<row=3 col=1 colspan=2/>` |
| end_group | | | |

Dette gjengis som:

```
[ Fornavn           ] [ Etternavn          ]
[ Alder             ] [ Kjønn              ]
[ Full adresse (strekker seg over begge kolonner) ]
```

---

## Eksempel: 3-kolonne plotdatainntasting

| type | name | label | appearance |
|------|------|-------|------------|
| begin_group | plot_data | Plotdetaljer | `field-list grid(weight=3)` |
| text | plot_id | Plot-ID | `gridformat<row=1 col=1/>` |
| decimal | area_ha | Areal (ha) | `gridformat<row=1 col=2/>` |
| select_one crop_type | crop | Avlingstype | `gridformat<row=1 col=3/>` |
| decimal | yield | Avling (kg) | `gridformat<row=2 col=1/>` |
| decimal | revenue | Inntekt | `gridformat<row=2 col=2/>` |
| text | notes | Notater | `gridformat<row=2 col=3/>` |
| end_group | | | |

---

## Bakgrunnsfarger

Bruk `backgroundcolor` for å visuelt skille seksjoner:

| type | name | label | appearance |
|------|------|-------|------------|
| note | section_a | Seksjon A | `gridformat<row=1 col=1 colspan=2 backgroundcolor=#e8f4f8/>` |

---

## Beste praksis

1. Bruk grid-oppsett bare for **datainntastingsintensive** skjermer der felt side om side genuint reduserer rulling.
2. Hold `colspan=1`-felt korte (ID-er, koder, korte select-er) — brede etiketter kuttes dårlig i smale gridkolonner.
3. Bruk `colspan=N` for felt med lange etiketter eller flerlinjet tekstinput.
4. Test på den minste skjermstørrelsen du forventer at tellere bruker — et 4-kolonne grid er trangt på en telefon.
5. Grid-oppsett fungerer best på web- og nettbrettformer; på mobiltelefoner er vanligvis et 2-kolonne oppsett den maksimale komfortable bredden.

## Begrensninger

- `gridformat<>` fungerer bare inne i en gruppe med `grid(weight=N)`-utseende — det har ingen effekt på toppnivå.
- Grid-oppsett er en rtSurvey webskjema-utvidelse og gjengis kanskje ikke riktig i andre ODK-kompatible klienter.
- Rad- og kolonneposisjonering valideres ikke ved skjemabyggetidspunkt — overlappende felt vil begge gjengis, men kan se ødelagt ut.
