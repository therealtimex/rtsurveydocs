---
title: "Appearance"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

Stĺpec `appearance` v rtSurvey umožňuje prispôsobiť vizuálnu prezentáciu a správanie otázok vo vašich prieskumoch. Táto funkcia zlepšuje používateľský zážitok a môže výrazne zlepšiť efektivitu zberu dát. rtSurvey podporuje štandardné atribúty vzhľadu XLSForm a rozširuje ich o ďalšie možnosti.

## Štandardné atribúty vzhľadu XLSForm

rtSurvey podporuje nasledujúce štandardné atribúty vzhľadu XLSForm:

| Atribút vzhľadu | Typy otázok | Popis |
|----------------------|----------------|-------------|
| multiline | text | Vytvorí viacriadkové textové pole (najlepšie pre webových klientov) |
| minimal | select_one, select_multiple | Zobrazí voľby v rozbaľovacom menu |
| quick | select_one | Automaticky postúpi na ďalšiu otázku po výbere (len mobilné) |
| no-calendar | date | Potlačí zobrazenie kalendára (len mobilné) |
| month-year | date | Umožní výber iba mesiaca a roka |
| year | date | Umožní výber iba roka |
| horizontal-compact | select_one, select_multiple | Zobrazí voľby horizontálne (len web) |
| horizontal | select_one, select_multiple | Zobrazí voľby horizontálne v stĺpcoch (len web) |
| likert | select_one | Prezentuje voľby ako Likertovu škálu |
| compact | select_one, select_multiple | Zobrazí voľby vedľa seba s minimálnym okrajom |
| quickcompact | select_one | Kombinuje kompaktné zobrazenie s automatickým postupom (len mobilné) |
| field-list | groups | Zobrazí celú skupinu na jednej obrazovke (len mobilné) |
| label | select_one, select_multiple | Zobrazí popisky volieb bez vstupov |
| list-nolabel | select_one, select_multiple | Zobrazí vstupy bez popiskov (použite s `label`) |
| table-list | groups | Zobrazí otázky v tabuľkovom formáte |
| signature | image | Umožní zachytenie podpisu (len mobilné) |
| draw | image | Umožní voľnoručné kreslenie (len mobilné) |
| map, quick map | select_one, select_one_from_file | Umožní výber z prvkov mapy |

## Najlepšie postupy pre používanie vzhľadu

1. **Konzistentnosť**: Používajte atribúty vzhľadu konzistentne v celom prieskume pre jednotný vzhľad.
2. **Mobilné vs. web**: Zvážte, ako sa vzhľady budú renderovať na rôznych zariadeniach a platformách.
3. **Výkon**: Buďte opatrní s atribútmi vzhľadu, ktoré môžu spomaliť načítavanie formulára (napr. `table-list` pre veľké skupiny).
4. **Používateľský zážitok**: Vyberte vzhľady, ktoré uľahčujú zadávanie dát a sú intuitívnejšie pre respondentov.
5. **Testovanie**: Vždy testujte váš formulár na cieľových zariadeniach, aby ste sa uistili, že vzhľady fungujú podľa očakávaní.

## Pokročilé techniky

### Kombinácia vzhľadov

Niektoré atribúty vzhľadu môžu byť kombinované pre zložitejšie rozloženia:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Vyberte jednu: | minimal compact |
```

### Dynamické vzhľady

rtSurvey umožňuje dynamické zmeny vzhľadu na základe logiky formulára:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Zadajte čas: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Úvahy pre mobilnú aplikáciu

- Niektoré vzhľady (napr. `quick`, `signature`) sú špecifické pre mobilné zariadenia.
- Dôkladne testujte na Androide aj iOS pre konzistentné správanie.

## Rozšírené atribúty vzhľadu rtSurvey

Okrem štandardných vzhľadov XLSForm rtSurvey podporuje nasledujúce možnosti špecifické pre platformu:

### Kontrola dát a zobrazenia

| Atribút vzhľadu | Typy otázok | Popis |
|----------------------|----------------|-------------|
| `invisible` | akýkoľvek | Skryje pole pred zobrazením pri súčasnom zbere alebo výpočte jeho hodnoty. Odlišné od typu `hidden` — pole sa stále zúčastňuje logiky. |
| `displaytitle` | akýkoľvek | Vynúti zobrazenie popisku/názvu poľa, aj keď by inak bol potlačený. |
| `autopull` | select_one, select_multiple | Automaticky načíta externé dáta na vyplnenie volieb pri načítaní formulára alebo zmene spúšťacieho poľa. |
| `floating_hint` | text, integer, decimal | Zobrazí text nápovedy ako plávajúci popisok nad vstupným poľom namiesto pod ním. |
| `calculate-button` | calculate | Pridá viditeľné tlačidlo, ktoré spustí prepočítanie poľa na požiadanie, namiesto automatického výpočtu. |

### Rozloženie

| Atribút vzhľadu | Typy otázok | Popis |
|----------------------|----------------|-------------|
| `1screen` | group | Vynúti zobrazenie celej skupiny na jednej obrazovke bez ohľadu na veľkosť skupiny. |
| `columns(n)` | select_one, select_multiple | Zobrazí voľby v `n` stĺpcoch. Príklad: `columns(3)` zobrazí tri stĺpce prepínačov. |
| `gridformat<row=R col=C colspan=S align=center>` | akýkoľvek | Umiestni pole v rozložení CSS mriežky na riadku `R`, stĺpci `C`, presahujúci `S` stĺpcov. Používa sa s `advanced-extension/grid-layout`. |
| `ignore-simplify` | akýkoľvek | Inštruuje renderer formulára, aby preskočil automatické zjednodušenie alebo kondenzáciu rozloženia tohto poľa. |

### Widgety

| Atribút vzhľadu | Typy otázok | Popis |
|----------------------|----------------|-------------|
| `likert` | select_one | Prezentuje voľby ako rad Likertovej škály (potvrdené ako podporované). |
| `distress` | select_one | Renderuje voľby ako vizuálny widget Kesslerovej škály psychologickej tiesne (K10) s emocionálnymi ikonami. |

### Integrácia API

| Atribút vzhľadu | Typy otázok | Popis |
|----------------------|----------------|-------------|
| `callapi` | text, integer, decimal, select_one | Umožňuje integráciu API volania pre toto pole. Stĺpec calculation by mal obsahovať výraz `callapi()`. Pozrite si [Volanie API](advanced-extension/call-api). |
| `callapi-verify(params)` | text, integer, decimal | Spustí overovací hovor API pomocou statických parametrov. Formulár blokuje postup, kým API nepotvrdí hodnotu. |
| `callapi-verify(dynamicParams)` | text, integer, decimal | Rovnaké ako `callapi-verify`, ale s parametrami odvodenými od hodnôt iných polí za behu. |

### Inline formát dátumu/času

Pre polia `date`, `time` a `datetime` môžete zadať vlastný formát zobrazenia pomocou reťazca formátu pripojeného k vzhľadu:

```
inline-[%d/%m/%Y]
inline-1line-[%d/%m/%Y %H:%M]
```

Tokeny formátu sú rovnaké ako pre `format-date()` a `format-date-time()`. Pozrite si [Funkcie — Funkcie dátumu a času](operators-and-functions/functions#date-and-time-functions).

Príklad:

| type | name | label | appearance |
|------|------|-------|------------|
| datetime | event_time | Dátum a čas udalosti | inline-[%d/%m/%Y %I:%M %p] |
| date | birth_date | Dátum narodenia | inline-[%d/%m/%Y] |

## Známe obmedzenia

- Komplexné vzhľady sa nemusia renderovať identicky naprieč všetkými platformami.
- Niektoré pokročilé vzhľady rtSurvey nemusia byť podporované v offline režime.

## Riešenie problémov so vzhľadom

1. **Vzhľad nie je aplikovaný**: Skontrolujte preklepy v stĺpci appearance.
2. **Nekonzistentné renderovanie**: Overte kompatibilitu s typom otázky a platformou.
3. **Problémy s výkonom**: Zvážte zjednodušenie komplexných vzhľadov, najmä pre veľké prieskumy.
