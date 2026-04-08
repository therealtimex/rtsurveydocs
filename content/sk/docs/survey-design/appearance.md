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
| `required-but-simplify` | akýkoľvek | Pole je povinné, ale jeho rozloženie je stále zjednodušené rendererom (prepíše predvolené správanie, kde povinné polia sú vylúčené zo zjednodušenia). |
| `embed` | akýkoľvek | Renderuje pole vo vloženom/inline režime zobrazenia, potlačí jeho vonkajší obal a kontajner popisku — používa sa, keď je otázka vnorená do vlastného HTML. |
| `popup` | select_one, select_multiple | Renderuje zoznam volieb v vyskakovacom/modálnom okne namiesto inline. |
| `auto-hide-empty` | boxtag, select | Skryje celý widget otázky, keď je zoznam volieb prázdny (napr. API nevrátilo žiadne výsledky). |
| `text-nolabel` | select_one, select_multiple | Skryje textový popisok každej voľby, zobrazuje iba vstupný ovládací prvok. Podobné `list-nolabel`, ale aplikované pre každú voľbu, nie ako rozdelenie stĺpcov. |

### Widgety

| Atribút vzhľadu | Typy otázok | Popis |
|----------------------|----------------|-------------|
| `likert` | select_one | Prezentuje voľby ako rad Likertovej škály (potvrdené ako podporované). |
| `distress` | select_one | Renderuje voľby ako vizuálny widget Kesslerovej škály psychologickej tiesne (K10) s emocionálnymi ikonami. |

### Vizuálne widgety pre výber

Tieto vzhľady menia celé renderovanie zoznamov volieb pre výber.

| Atribút vzhľadu | Typy otázok | Popis |
|----------------------|----------------|-------------|
| `tagging` | select_one, select_multiple | Voľby sa renderujú ako klikateľné tagové čipy v tvare piluliek. |
| `boxtag` | select_one, select_multiple | Voľby sa renderujú ako obdĺžnikové štylizované boxy, na ktoré používateľ klepne. |
| `boxtag -search` | select_one, select_multiple | Rozloženie boxtag s živým vyhľadávacím/filtrovacím poľom nad boxmi. |
| `duolingo-style1` | select_one, select_multiple | Rozloženie veľkých kariet inšpirované Duolingom — vhodné pre krátke zoznamy s ikonami. |
| `rating_box` | select_one, select_multiple | Mriežka klepateľných číslovaných boxov — vhodná pre škálové alebo NPS otázky. |
| `star_rating` | select_one | Voľby sa renderujú ako hviezdičky; počet hviezdičiek zodpovedá počtu volieb. |
| `choices-noshow` | select_one, select_multiple | Spočiatku zobrazuje iba prvých 10 volieb s ovládacím prvkom „Zobraziť viac". |
| `noshow` | select_one, select_multiple | Skryje zoznam volieb úplne; hodnota sa nastavuje programovo cez `calculate` alebo API. |
| `checkall` | select_multiple | Pridá skratku „Vybrať všetko" na vrchol zoznamu volieb. |
| `max-items(N)` | select_one, select_multiple | Obmedzí viditeľný zoznam volieb na N položiek. Príklad: `max-items(5)`. |

### Vizuálne widgety pre text

| Atribút vzhľadu | Typy otázok | Popis |
|----------------------|----------------|-------------|
| `richtext` | text | Nahradí prosté textové pole editorom formátovaného textu (tučné, kurzíva, zoznamy, odkazy). Ukladá HTML. |
| `typingtest` | text | Widget testu písania — text popisku je pasáž; widget zaznamenáva zadanú odpoveď a časovanie. |

### Mediálne rozšírenia

| Atribút vzhľadu | Typy otázok | Popis |
|----------------------|----------------|-------------|
| `watermark("výraz")` | image | Prekryje textový vodoznak na zachytených fotografiách. Argument je výraz XPath vyhodnotený v čase zachytenia. Príklad: `watermark("${id} ${today()}")`. |
| `editable` | image | Umožní anotáciu/kreslenie cez zachytenú fotografiu pred uložením. |

### Konfigurácia inline zobrazenia

Modifikátory `display{}` a `results{}` možno pripojiť k `inline` vzhľadom pre riadenie zarovnania ikon a zobrazenia výsledkov. Používajú sa spolu s rozšírením inline časového vstupu na poliach `text` a s widgetmi na zachytenie médií.

#### Parametre `display{}`

```
inline display{left}
inline display{right,small}
inline display{top,large,inline-icon}
```

| Parameter | Hodnoty | Popis |
|-----------|--------|-------------|
| Zarovnanie | `left`, `right`, `top`, `bottom`, `center` | Pozícia ikony relatívne k vstupnému poľu |
| Veľkosť | `small`, `medium`, `large` | Veľkosť ikony (zodpovedá 2,5 rem, 5 rem, 8 rem) |
| Režim | `inline-icon` | Renderuje spúšťač iba ako ikonu (bez okraja tlačidla) |
| Režim | `inline-button` | Renderuje spúšťač ako celé tlačidlo |

#### Parametre `results{}`

```
inline results{right}
inline results{left,hide(seconds)}
```

| Parameter | Hodnoty | Popis |
|-----------|--------|-------------|
| Zarovnanie | `left`, `right`, `top`, `bottom`, `center` | Pozícia zobrazenia výslednej hodnoty |
| `hide(pole)` | ľubovoľný názov čiastkového poľa | Skryje konkrétnu komponentu výsledku (napr. `hide(seconds)`) |

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
