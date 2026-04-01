---
title: "Rozloženie mriežky"
description: "Rozloženie mriežky umožňuje umiestniť polia do CSS mriežky vo vnútri skupiny, umožňujúc viacstĺpcové dizajny formulárov."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 296
---

Funkcia **Rozloženie mriežky** umožňuje usporiadať otázky v **viacstĺpcovej mriežke** vo vnútri skupiny pomocou tagu vzhľadu `gridformat<>`. Je to užitočné pre formuláre so zadávaním hustých dát, kde by sa viaceré súvisiace polia mali objavovať vedľa seba namiesto vertikálneho stohovania.

---

## Ako to funguje

Rozloženie mriežky sa aplikuje na dvoch úrovniach:

1. **Skupina** — nastavte `appearance: field-list grid(weight=N)` na definovanie počtu stĺpcov mriežky
2. **Každé pole vo vnútri skupiny** — nastavte `appearance: gridformat<row=R col=C colspan=S/>` na umiestnenie poľa

Mriežka používa 12-stĺpcový systém v štýle Bootstrap. `weight=N` definuje, koľko logických stĺpcov má vaša mriežka; každý stĺpec zaberá `12/N` Bootstrap stĺpcov.

---

## Vzhľad na úrovni skupiny

| Vzhľad | Popis |
|------------|-------------|
| `field-list grid(weight=2)` | 2-stĺpcová mriežka (každý stĺpec = 6 Bootstrap stĺpcov) |
| `field-list grid(weight=3)` | 3-stĺpcová mriežka (každý stĺpec = 4 Bootstrap stĺpce) |
| `field-list grid(weight=4)` | 4-stĺpcová mriežka (každý stĺpec = 3 Bootstrap stĺpce) |
| `field-list grid(weight=6)` | 6-stĺpcová mriežka (každý stĺpec = 2 Bootstrap stĺpce) |

---

## Syntax `gridformat<>` na úrovni poľa

```
gridformat<row=R col=C colspan=S/>
gridformat<row=R col=C colspan=S backgroundcolor=COLOR/>
```

| Atribút | Popis |
|-----------|-------------|
| `row` | Číslo riadka (začína od 1) |
| `col` | Číslo stĺpca (začína od 1, v rámci mriežky definovanej `weight`) |
| `colspan` | Počet stĺpcov, ktoré toto pole presahuje (predvolené 1) |
| `backgroundcolor` | Voliteľná CSS farba pre pozadie poľa (napr. `#f0f0f0`, `lightblue`) |

---

## Príklad: 2-stĺpcová sekcia prieskumu domácnosti

| type | name | label | appearance |
|------|------|-------|------------|
| begin_group | demographics | Demografické údaje | `field-list grid(weight=2)` |
| text | first_name | Krstné meno | `gridformat<row=1 col=1/>` |
| text | last_name | Priezvisko | `gridformat<row=1 col=2/>` |
| integer | age | Vek | `gridformat<row=2 col=1/>` |
| select_one gender | gender | Pohlavie | `gridformat<row=2 col=2/>` |
| text | address | Celá adresa | `gridformat<row=3 col=1 colspan=2/>` |
| end_group | | | |

Toto sa renderuje ako:

```
[ Krstné meno        ] [ Priezvisko          ]
[ Vek               ] [ Pohlavie             ]
[ Celá adresa (presahuje oba stĺpce)        ]
```

---

## Príklad: 3-stĺpcové zadávanie dát o parcele

| type | name | label | appearance |
|------|------|-------|------------|
| begin_group | plot_data | Podrobnosti parcely | `field-list grid(weight=3)` |
| text | plot_id | ID parcely | `gridformat<row=1 col=1/>` |
| decimal | area_ha | Plocha (ha) | `gridformat<row=1 col=2/>` |
| select_one crop_type | crop | Typ plodiny | `gridformat<row=1 col=3/>` |
| decimal | yield | Výnos (kg) | `gridformat<row=2 col=1/>` |
| decimal | revenue | Príjem | `gridformat<row=2 col=2/>` |
| text | notes | Poznámky | `gridformat<row=2 col=3/>` |
| end_group | | | |

---

## Farby pozadia

Použite `backgroundcolor` na vizuálne odlíšenie sekcií:

| type | name | label | appearance |
|------|------|-------|------------|
| note | section_a | Sekcia A | `gridformat<row=1 col=1 colspan=2 backgroundcolor=#e8f4f8/>` |

---

## Najlepšie postupy

1. Používajte rozloženie mriežky iba pre **intenzívne zadávanie dát**, kde polia vedľa seba skutočne znižujú rolovanie.
2. Udržujte polia s `colspan=1` krátke (ID, kódy, krátke výbery) — široké popisky sa zle skracujú v úzkych stĺpcoch mriežky.
3. Používajte `colspan=N` pre polia s dlhými popiskami alebo viacriadkovými textovými vstupmi.
4. Testujte na najmenšej veľkosti obrazovky, ktorú očakávate, že budú anketári používať — 4-stĺpcová mriežka je stiesnená na telefóne.
5. Rozloženie mriežky funguje najlepšie na webových formulároch a tabletoch; na mobilných telefónoch je 2-stĺpcové rozloženie zvyčajne maximálna pohodlná šírka.

## Obmedzenia

- `gridformat<>` funguje iba vo vnútri skupiny so vzhľadom `grid(weight=N)` — na najvyššej úrovni nemá žiadny efekt.
- Rozloženie mriežky je rozšírenie webového formulára rtSurvey a nemusí sa správne renderovať v iných klientoch kompatibilných s ODK.
- Pozičné umiestnenie riadkov a stĺpcov nie je overené v čase zostavenia formulára — prekrývajúce sa polia sa oba renderujú, ale môžu vyzerať chybne.
