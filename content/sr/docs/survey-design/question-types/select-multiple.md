---
title: "Select_multiple"
description: "Pitanja tipa select_multiple dozvoljavaju ispitanicima da izaberu jednu ili više opcija sa unapred definisane liste."
icon: "check_box"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 225
---

Tip pitanja `select_multiple` prikazuje listu gde ispitanik može izabrati **jednu ili više opcija**. Podrazumevano, opcije se prikazuju kao potvrdni okviri. Sačuvana vrednost je **lista izabranih vrednosti opcija razdvojena razmacima**.

## Osnovna XLSForm specifikacija

**Radni list survey:**

| type | name | label |
|------|------|-------|
| select_multiple crops | crops_grown | Koje useve domaćinstvo gaji? |

**Radni list choices:**

| list_name | name | label |
|-----------|------|-------|
| crops | maize | Kukuruz |
| crops | beans | Pasulj |
| crops | rice | Pirinač |
| crops | vegetables | Povrće |
| crops | other | Drugo |

Za više detalja pogledajte [XLSForm specifikaciju](https://xlsform.org/en/#question-types).

## Format sačuvanih podataka

Izvezena kolona sadrži listu izabranih vrednosti razdvojenu razmacima:

```
maize beans vegetables
```

Koristite funkciju `selected()` — ne `=` — kada testirate vrednosti select_multiple u izrazima (pogledajte ispod).

## Upotrebe

Pitanja tipa select_multiple se koriste za:

1. Prikupljanje više primenljivih odgovora (npr. izvori prihoda, gajeni usevi, simptomi)
2. Stavke slaganja u stilu potvrdnih okvira (npr. "Izaberite sve što se primenjuje")
3. Inventari jezika ili veština
4. Bilo koje pitanje gde su više odgovora istovremeno valjani

## Opcije izgleda

{{< table >}}
| Izgled | Opis |
|--------|------|
| *(ništa)* | Podrazumevani potvrdni okviri, jedan po redu |
| `minimal` | Widget za višestruki izbor iz padajućeg menija |
| `compact` | Kompaktna mreža, kolone se prilagođavaju širini ekrana |
| `compact-N` | Kompaktna mreža primorana na N kolona |
| `horizontal` | Opcije raspoređene horizontalno u redu (veb) |
| `horizontal-compact` | Horizontalni, kompaktni razmaci (veb) |
| `label` | Prikazuje samo oznake, bez potvrdnih okvira (koristiti sa `list-nolabel`) |
| `list-nolabel` | Prikazuje samo potvrdne okvire, bez oznaka (koristiti sa `label`) |
| `columns(N)` | Prikazati u N kolona (rtSurvey proširenje) |
| `tagging` | Prikazuje opcije kao klikabilne čipove sa oznakama |
| `boxtag` | Prikazuje opcije kao pravougaone stilizovane kutije |
| `boxtag -search` | Raspored boxtag sa poljem za pretragu |
| `duolingo-style1` | Raspored velikih kartica inspirisan Duolingom |
| `rating_box` | Kutije za ocenjivanje na bazi mreže |
| `choices-noshow` | Prikazuje prvih 10 opcija, ostatak na zahtev |
| `checkall` | Dodaje opciju „Izaberi sve" |
| `max-items(N)` | Ograničava broj vidljivih opcija na N |
{{< /table >}}

### Primer: Kompaktni raspored sa 3 kolone

| type | name | label | appearance |
|------|------|-------|------------|
| select_multiple symptoms | symptoms | Izaberite sve primećene simptome | compact-3 |

## Korišćenje `selected()` u izrazima

Pošto je sačuvana vrednost string razdvojen razmacima, **morate** koristiti `selected()` da biste testirali da li je određena opcija izabrana. Korišćenje `=` neće ispravno funkcionisati.

### U `relevant`

Prikažite pitanje za praćenje samo ako je izabrano "drugo":

| type | name | label | relevant |
|------|------|-------|----------|
| select_multiple crops | crops_grown | Koji usevi se gaje? | |
| text | crops_other | Molimo navedite druge useve | `selected(${crops_grown}, 'other')` |

### U `constraint`

Zahtevajte najmanje 2 izbora:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple issues | issues | `count-selected(.) >= 2` | Izaberite najmanje 2 problema |

Ograničite na maksimalno 3:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple priorities | priorities | `count-selected(.) <= 3` | Izaberite ne više od 3 prioriteta |

### U `calculate` — spajanje izabranih oznaka

Kombinirajte `selected-at()`, `count-selected()` i `choice-label()` za izgradnju čitljivog rezimea:

| type | name | calculation |
|------|------|-------------|
| calculate | crops_summary | join(', ', ${crops_grown}) |

## Opcija "Nijedno od navedenog" / ekskluzivna opcija

Uobičajeni obrazac je da se jedna opcija učini međusobno isključivom sa svim ostalim. Koristite `constraint` da je primenite:

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| select_multiple issues | issues | Izaberite sve prisutne probleme | `not(selected(., 'none') and count-selected(.) > 1)` | "Nijedno" ne može biti izabrano sa drugim opcijama |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| issues | water | Nestašica vode |
| issues | roads | Loši putevi |
| issues | health | Nedostatak zdravstvenih usluga |
| issues | none | Nijedno od navedenog |

## Brojanje i sumiranje izbora

| Funkcija | Primer | Rezultat |
|----------|--------|---------|
| `count-selected(field)` | `count-selected(${crops_grown})` | Broj izabranih opcija |
| `selected(field, value)` | `selected(${crops_grown}, 'maize')` | tačno/netačno |
| `selected-at(field, index)` | `selected-at(${crops_grown}, 0)` | Prva izabrana vrednost |
| `choice-label(field, value)` | `choice-label(${crops_grown}, 'maize')` | Oznaka za vrednost |

## Najbolje prakse

1. Uvek koristite `selected()` u `relevant`, `constraint` i `calculate` — nikada `=` ili `!=`.
2. Dodajte ograničenje za ograničavanje maksimalnog broja izbora ako dizajn pitanja to zahteva.
3. Uključite opciju "Nijedno" ili "Nije primenljivo" kada je nula izbora valjan odgovor.
4. Za dugačke liste (15+ opcija), koristite `minimal` (višestruki izbor iz padajućeg menija) da izbegnete prekomerno skrolovanje.
5. Izvozite podatke i koristite razdvajanje stringova u vašem alatu za analizu — format razdvojen razmacima zahteva razdvajanje pre pivotiranja.

## Ograničenja

- Vrednosti select_multiple se ne mogu direktno porediti sa `=`. Uvek koristite `selected()`.
- Kompaktni izgled možda neće dobro prikazivati veoma dugačke oznake opcija.
- Kada filtrirate opcije sa `choice_filter`, filtriranje se primenjuje na sve prikazane opcije, isto kao i kod `select_one`.
