---
title: "Rank"
description: "Otázky typu rank umožňujú respondentom zoradiť sadu volieb podľa preferencie alebo priority."
icon: "list-ol"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 242
---

Typ otázky `rank` prezentuje zoznam volieb, ktoré respondent musí **pretiahnuť do poradia** (alebo inak zoradiť od prvého po posledné). Ukladá výsledok ako zoznam hodnôt volieb oddelený medzerami v poradí, v ktorom boli vybrané, pričom voľba s najvyššou prioritou je na prvom mieste.

## Základná špecifikácia XLSForm

| type | name | label |
|------|------|-------|
| rank priorities | main_priority | Zoraďte tieto komunitné potreby od najdôležitejšej po najmenej dôležitú |

Voľby sú definované v **hárku choices** rovnako ako pri `select_one`:

**survey:**

| type | name | label |
|------|------|-------|
| rank priorities | main_priority | Zoraďte tieto potreby od najdôležitejšej po najmenej dôležitú |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| priorities | water | Čistá voda |
| priorities | health | Zdravotná starostlivosť |
| priorities | education | Vzdelávanie |
| priorities | roads | Cesty |
| priorities | electricity | Elektrina |

## Formát uloženej hodnoty

Uložená hodnota je **zoznam hodnôt volieb oddelený medzerami** v poradí (prvá = najvyššia priorita):

```
water education health roads electricity
```

## Extrahovanie poradových pozícií

Použite `selected-at()` na získanie voľby na konkrétnom poradí:

| type | name | label | calculation |
|------|------|-------|-------------|
| rank priorities | main_priority | Zoraďte komunitné potreby | |
| calculate | top_priority | | selected-at(${main_priority}, 0) |
| calculate | second_priority | | selected-at(${main_priority}, 1) |

`selected-at(${main_priority}, 0)` vracia hodnotu umiestnenú **na prvom mieste** (index 0 = najvyššia priorita).

## Použitie `rank-index()` s opakujúcimi sa skupinami

Keď je `rank` použitý vo vnútri opakujúcej sa skupiny, `rank-index()` umožňuje odkazovať na poradové miesto zvonka opakovania:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | first_ranked | | rank-index(1, ${score}) |

Pozrite si [Funkcie — Funkcie opakujúcich sa polí](../operators-and-functions/functions#repeated-field-functions) pre úplné podrobnosti o `rank-index()` a `rank-index-if()`.

## Použitia

Otázky typu rank sa bežne používajú pre:

1. **Poradie priorít** — požiadanie komunít o zoradenie rozvojových potrieb
2. **Poradie preferencií** — zoradenie funkcií produktu, atribútov služby alebo politických možností
3. **Zoraďovanie krokov skúšky** — usporiadanie krokov v procese
4. **Výber Top-N** — kombinovaný s `selected-at()` na extrahovanie iba 1, 2 alebo 3 najlepších volieb

## Najlepšie postupy

1. Udržujte zoznam krátky (3–7 položiek) — zoraďovanie sa stáva kognitívne náročným nad 7–8 volieb.
2. Používajte jasné, vzájomne sa vylučujúce popisky volieb, aby ste predišli zmätku ohľadom toho, čo „prvé" znamená.
3. Pridajte nápovedu vysvetľujúcu smer zoraďovania (napr. „Pretiahnite do poradia: prvé = najdôležitejšie").
4. Overujte pomocou `count-selected(.) = x`, ak potrebujete zabezpečiť, že všetky voľby sú zoradené.

## Obmedzenia

- Widget ťahania na zoraďovanie vyžaduje dotykovú obrazovku alebo myš — nemusí dobre fungovať v prostrediach iba s klávesnicou.
- Na niektorých starších mobilných klientoch môže widget rank prejsť na číslicové rozhranie.
- Nemôžete čiastočne zoradiť (t.j. zoradiť iba niektoré voľby) — všetky voľby musia byť usporiadané.
