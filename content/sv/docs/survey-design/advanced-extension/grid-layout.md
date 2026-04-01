---
title: "Rutnätslayout"
description: "Rutnätslayout låter dig placera fält i ett CSS-rutnät inom en grupp, vilket möjliggör formulärdesign med flera kolumner."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 296
---

Funktionen **Rutnätslayout** låter dig ordna frågor i ett **flerfkolumns-rutnät** inom en grupp med hjälp av utseendetaggen `gridformat<>`. Detta är användbart för täta datainmatningsformulär där flera relaterade fält bör visas sida vid sida istället för staplade vertikalt.

---

## Hur det fungerar

Rutnätslayout tillämpas på två nivåer:

1. **Gruppen** — sätt `appearance: field-list grid(weight=N)` för att definiera hur många kolumner rutnätet har
2. **Varje fält inuti gruppen** — sätt `appearance: gridformat<row=R col=C colspan=S/>` för att positionera fältet

Rutnätet använder ett 12-kolumners Bootstrap-liknande system. `weight=N` definierar hur många logiska kolumner ditt rutnät har; varje kolumn upptar `12/N` Bootstrap-kolumner.

---

## Utseende på gruppnivå

| Utseende | Beskrivning |
|----------|-------------|
| `field-list grid(weight=2)` | 2-kolumners rutnät (varje kolumn = 6 Bootstrap-kolumner) |
| `field-list grid(weight=3)` | 3-kolumners rutnät (varje kolumn = 4 Bootstrap-kolumner) |
| `field-list grid(weight=4)` | 4-kolumners rutnät (varje kolumn = 3 Bootstrap-kolumner) |
| `field-list grid(weight=6)` | 6-kolumners rutnät (varje kolumn = 2 Bootstrap-kolumner) |

---

## `gridformat<>`-syntax på fältnivå

```
gridformat<row=R col=C colspan=S/>
gridformat<row=R col=C colspan=S backgroundcolor=COLOR/>
```

| Attribut | Beskrivning |
|----------|-------------|
| `row` | Radnummer (1-baserat) |
| `col` | Kolumnnummer (1-baserat, inom rutnätet definierat av `weight`) |
| `colspan` | Antal kolumner det här fältet spänner (standard 1) |
| `backgroundcolor` | Valfri CSS-färg för fältbakgrunden (t.ex. `#f0f0f0`, `lightblue`) |

---

## Exempel: 2-kolumners hushållsundersökningssektion

| type | name | label | appearance |
|------|------|-------|------------|
| begin_group | demographics | Demografi | `field-list grid(weight=2)` |
| text | first_name | Förnamn | `gridformat<row=1 col=1/>` |
| text | last_name | Efternamn | `gridformat<row=1 col=2/>` |
| integer | age | Ålder | `gridformat<row=2 col=1/>` |
| select_one gender | gender | Kön | `gridformat<row=2 col=2/>` |
| text | address | Fullständig adress | `gridformat<row=3 col=1 colspan=2/>` |
| end_group | | | |

Detta renderas som:

```
[ Förnamn           ] [ Efternamn          ]
[ Ålder             ] [ Kön                ]
[ Fullständig adress (sträcker sig över båda kolumnerna)  ]
```

---

## Exempel: 3-kolumners datainmatning för odlingsmark

| type | name | label | appearance |
|------|------|-------|------------|
| begin_group | plot_data | Parcellinformation | `field-list grid(weight=3)` |
| text | plot_id | Parcel-ID | `gridformat<row=1 col=1/>` |
| decimal | area_ha | Yta (ha) | `gridformat<row=1 col=2/>` |
| select_one crop_type | crop | Grödtyp | `gridformat<row=1 col=3/>` |
| decimal | yield | Skörd (kg) | `gridformat<row=2 col=1/>` |
| decimal | revenue | Intäkt | `gridformat<row=2 col=2/>` |
| text | notes | Anteckningar | `gridformat<row=2 col=3/>` |
| end_group | | | |

---

## Bakgrundsfärger

Använd `backgroundcolor` för att visuellt urskilja sektioner:

| type | name | label | appearance |
|------|------|-------|------------|
| note | section_a | Sektion A | `gridformat<row=1 col=1 colspan=2 backgroundcolor=#e8f4f8/>` |

---

## Bästa praxis

1. Använd rutnätslayout bara för **datainmatningsintensiva** skärmar där fält sida vid sida genuint minskar scrollning.
2. Håll `colspan=1`-fält korta (ID:n, koder, korta val) — breda etiketter trunkeras dåligt i smala rutnätskolumner.
3. Använd `colspan=N` för fält med långa etiketter eller flerradiga textinmatningar.
4. Testa på den minsta skärmstorlek du förväntar dig att räknare ska använda — ett 4-kolumners rutnät är trångt på en telefon.
5. Rutnätslayout fungerar bäst på webben och pekskärmsformfaktorer; på mobiltelefoner är vanligtvis en 2-kolumners layout den maximalt bekväma bredden.

## Begränsningar

- `gridformat<>` fungerar bara inuti en grupp med `grid(weight=N)`-utseende — det har ingen effekt på toppnivå.
- Rutnätslayout är ett rtSurvey webbformulär-tillägg och kanske inte renderas korrekt i andra ODK-kompatibla klienter.
- Rad- och kolumnpositionering valideras inte vid formulärbyggningstid — överlappande fält renderas båda men kan se trasiga ut.
