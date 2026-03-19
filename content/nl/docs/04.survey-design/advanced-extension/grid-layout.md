---
title: "Rasterindeling"
description: "Rasterindeling laat u velden positioneren in een CSS-raster binnen een groep, waardoor meerkoloms formulierontwerpen mogelijk zijn."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 296
---

De functie **Rasterindeling** laat u vragen arrangeren in een **meerkoloms raster** binnen een groep, met behulp van de weergavetag `gridformat<>`. Dit is nuttig voor gegevensinvoerschermen met hoge dichtheid waarbij meerdere gerelateerde velden naast elkaar moeten verschijnen in plaats van verticaal gestapeld.

---

## Hoe het werkt

Rasterindeling wordt op twee niveaus toegepast:

1. **De groep** — stel `appearance: field-list grid(weight=N)` in om te definiëren hoeveel kolommen het raster heeft
2. **Elk veld binnen de groep** — stel `appearance: gridformat<row=R col=C colspan=S/>` in om het veld te positioneren

Het raster gebruikt een 12-koloms Bootstrap-stijl systeem. `weight=N` definieert hoeveel logische kolommen uw raster heeft; elke kolom beslaat `12/N` Bootstrap-kolommen.

---

## Weergave op groepsniveau

| Weergave | Beschrijving |
|----------|-------------|
| `field-list grid(weight=2)` | 2-koloms raster (elke kolom = 6 Bootstrap-kolommen) |
| `field-list grid(weight=3)` | 3-koloms raster (elke kolom = 4 Bootstrap-kolommen) |
| `field-list grid(weight=4)` | 4-koloms raster (elke kolom = 3 Bootstrap-kolommen) |
| `field-list grid(weight=6)` | 6-koloms raster (elke kolom = 2 Bootstrap-kolommen) |

---

## `gridformat<>`-syntaxis op veldniveau

```
gridformat<row=R col=C colspan=S/>
gridformat<row=R col=C colspan=S backgroundcolor=KLEUR/>
```

| Attribuut | Beschrijving |
|-----------|-------------|
| `row` | Rijnummer (1-gebaseerd) |
| `col` | Kolomnummer (1-gebaseerd, binnen het raster gedefinieerd door `weight`) |
| `colspan` | Aantal kolommen dat dit veld beslaat (standaard 1) |
| `backgroundcolor` | Optionele CSS-kleur voor de veldachtergrond (bijv. `#f0f0f0`, `lightblue`) |

---

## Voorbeeld: 2-koloms sectie huishoudenenquête

| type | name | label | appearance |
|------|------|-------|------------|
| begin_group | demographics | Demografische gegevens | `field-list grid(weight=2)` |
| text | first_name | Voornaam | `gridformat<row=1 col=1/>` |
| text | last_name | Achternaam | `gridformat<row=1 col=2/>` |
| integer | age | Leeftijd | `gridformat<row=2 col=1/>` |
| select_one gender | gender | Geslacht | `gridformat<row=2 col=2/>` |
| text | address | Volledig adres | `gridformat<row=3 col=1 colspan=2/>` |
| end_group | | | |

Dit wordt weergegeven als:

```
[ Voornaam          ] [ Achternaam         ]
[ Leeftijd          ] [ Geslacht           ]
[ Volledig adres (beslaat beide kolommen)  ]
```

---

## Voorbeeld: 3-koloms perceelinvoer

| type | name | label | appearance |
|------|------|-------|------------|
| begin_group | plot_data | Perceeldetails | `field-list grid(weight=3)` |
| text | plot_id | Perceel-ID | `gridformat<row=1 col=1/>` |
| decimal | area_ha | Oppervlakte (ha) | `gridformat<row=1 col=2/>` |
| select_one crop_type | crop | Gewastype | `gridformat<row=1 col=3/>` |
| decimal | yield | Opbrengst (kg) | `gridformat<row=2 col=1/>` |
| decimal | revenue | Opbrengst | `gridformat<row=2 col=2/>` |
| text | notes | Notities | `gridformat<row=2 col=3/>` |
| end_group | | | |

---

## Achtergrondkleuren

Gebruik `backgroundcolor` om secties visueel te onderscheiden:

| type | name | label | appearance |
|------|------|-------|------------|
| note | section_a | Sectie A | `gridformat<row=1 col=1 colspan=2 backgroundcolor=#e8f4f8/>` |

---

## Aanbevolen werkwijzen

1. Gebruik rasterindeling alleen voor **gegevensinvoer-intensieve** schermen waarbij naast-elkaar-velden het scrollen daadwerkelijk verminderen.
2. Houd `colspan=1`-velden kort (ID's, codes, korte selecties) — brede labels worden slecht afgebroken in smalle rasterkolommen.
3. Gebruik `colspan=N` voor velden met lange labels of meerregelige tekstinvoer.
4. Test op het kleinste schermformaat dat u verwacht dat enumeratoren gebruiken — een 4-koloms raster is krap op een telefoon.
5. Rasterindeling werkt het beste op web- en tabletformfactoren; op mobiele telefoons is een 2-koloms indeling meestal de maximale comfortabele breedte.

## Beperkingen

- `gridformat<>` werkt alleen binnen een groep met `grid(weight=N)`-weergave — het heeft geen effect op het hoogste niveau.
- Rasterindeling is een rtSurvey-webformulieruitbreiding en wordt mogelijk niet correct weergegeven in andere ODK-compatibele clients.
- Rij- en kolompositionering wordt niet gevalideerd bij het bouwen van formulieren — overlappende velden worden beide weergegeven maar kunnen er beschadigd uitzien.
