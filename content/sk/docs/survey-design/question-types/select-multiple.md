---
title: "Select_multiple"
description: "Otázky typu select_multiple umožňujú respondentom vybrať jednu alebo viacero možností z preddefinovaného zoznamu."
icon: "check_box"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 225
---

Typ otázky `select_multiple` zobrazuje zoznam, kde respondent môže vybrať **jednu alebo viacero možností**. Predvolene sa voľby renderujú ako zaškrtávacie políčka. Uložená hodnota je **zoznam oddelený medzerami** zo všetkých vybraných hodnôt volieb.

## Základná špecifikácia XLSForm

**Hárok survey:**

| type | name | label |
|------|------|-------|
| select_multiple crops | crops_grown | Aké plodiny pestuje domácnosť? |

**Hárok choices:**

| list_name | name | label |
|-----------|------|-------|
| crops | maize | Kukurica |
| crops | beans | Fazuľa |
| crops | rice | Ryža |
| crops | vegetables | Zelenina |
| crops | other | Iné |

Pre viac podrobností pozrite si [špecifikáciu XLSForm](https://xlsform.org/en/#question-types).

## Formát uložených dát

Exportovaný stĺpec obsahuje zoznam vybraných hodnôt oddelených medzerami:

```
maize beans vegetables
```

Pri testovaní hodnôt select_multiple vo výrazoch používajte funkciu `selected()` — nie `=` (pozri nižšie).

## Použitia

Otázky select_multiple sa používajú pre:

1. Zber viacerých platných odpovedí (napr. zdroje príjmu, pestované plodiny, príznaky)
2. Položky so zaškrtávacím políčkom (napr. „Vyberte všetky, ktoré platia")
3. Inventáre jazykov alebo zručností
4. Akúkoľvek otázku, kde je súčasne platných viac odpovedí

## Možnosti vzhľadu

{{< table >}}
| Vzhľad | Popis |
|------------|-------------|
| *(žiadny)* | Predvolené zaškrtávacie políčka, jedno na riadok |
| `minimal` | Widget viacnásobného výberu z rozbaľovacieho zoznamu |
| `compact` | Kompaktná mriežka, stĺpce sa prispôsobujú šírke obrazovky |
| `compact-N` | Kompaktná mriežka nútená do N stĺpcov |
| `horizontal` | Voľby usporiadané horizontálne v rade (web) |
| `horizontal-compact` | Horizontálne, kompaktné rozostupy (web) |
| `label` | Zobrazuje iba popisky, žiadne zaškrtávacie políčka (použite s `list-nolabel`) |
| `list-nolabel` | Zobrazuje iba zaškrtávacie políčka, žiadne popisky (použite s `label`) |
| `columns(N)` | Zobrazenie v N stĺpcoch (rozšírenie rtSurvey) |
{{< /table >}}

### Príklad: Kompaktné rozloženie s 3 stĺpcami

| type | name | label | appearance |
|------|------|-------|------------|
| select_multiple symptoms | symptoms | Vyberte všetky pozorované príznaky | compact-3 |

## Použitie `selected()` vo výrazoch

Keďže uložená hodnota je reťazec oddelený medzerami, **musíte** použiť `selected()` na testovanie, či bola konkrétna voľba vybraná. Použitie `=` nebude fungovať správne.

### V `relevant`

Zobrazenie následnej otázky iba ak bolo vybrané „iné":

| type | name | label | relevant |
|------|------|-------|----------|
| select_multiple crops | crops_grown | Aké plodiny sa pestujú? | |
| text | crops_other | Prosím uveďte iné plodiny | `selected(${crops_grown}, 'other')` |

### V `constraint`

Vyžadovanie aspoň 2 volieb:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple issues | issues | `count-selected(.) >= 2` | Vyberte aspoň 2 problémy |

Obmedzenie na maximum 3:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple priorities | priorities | `count-selected(.) <= 3` | Vyberte najviac 3 priority |

### V `calculate` — spájanie vybraných popiskov

Kombinujte `selected-at()`, `count-selected()` a `choice-label()` na zostavenie čitateľného súhrnu:

| type | name | calculation |
|------|------|-------------|
| calculate | crops_summary | join(', ', ${crops_grown}) |

## Možnosť „Žiadne z vyššie uvedených" / exkluzívna možnosť

Bežným vzorom je urobiť jednu možnosť vzájomne exkluzívnou so všetkými ostatnými. Použite `constraint` na jej vynútenie:

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| select_multiple issues | issues | Vyberte všetky prítomné problémy | `not(selected(., 'none') and count-selected(.) > 1)` | „Žiadne" nie je možné vybrať spolu s inými možnosťami |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| issues | water | Nedostatok vody |
| issues | roads | Zlé cesty |
| issues | health | Nedostatok zdravotných služieb |
| issues | none | Žiadne z vyššie uvedených |

## Počítanie a sumarizovanie výberov

| Funkcia | Príklad | Výsledok |
|----------|---------|--------|
| `count-selected(field)` | `count-selected(${crops_grown})` | Počet vybraných volieb |
| `selected(field, value)` | `selected(${crops_grown}, 'maize')` | true/false |
| `selected-at(field, index)` | `selected-at(${crops_grown}, 0)` | Prvá vybraná hodnota |
| `choice-label(field, value)` | `choice-label(${crops_grown}, 'maize')` | Popisok pre hodnotu |

## Najlepšie postupy

1. Vždy používajte `selected()` v `relevant`, `constraint` a `calculate` — nikdy `=` alebo `!=`.
2. Pridajte obmedzenie na obmedzenie maximálneho počtu výberov, ak to dizajn otázky vyžaduje.
3. Zahrňte možnosť „Žiadne" alebo „Nie je použiteľné", keď je platnou odpoveďou nula výberov.
4. Pre dlhé zoznamy (15+ volieb) použite `minimal` (rozbaľovací zoznam s viacnásobným výberom), aby ste sa vyhli nadmernému rolovaniu.
5. Exportujte dáta a pri analýze použite rozdelenie reťazca — formát oddelený medzerami vyžaduje rozdelenie pred otočením.

## Obmedzenia

- Hodnoty select_multiple nemôžu byť priamo porovnávané pomocou `=`. Vždy používajte `selected()`.
- Kompaktný vzhľad sa nemusí dobre renderovať pri veľmi dlhých popisoch volieb.
- Pri filtrovaní volieb pomocou `choice_filter` sa filtrovanie vzťahuje na všetky zobrazené voľby, rovnako ako pri `select_one`.
