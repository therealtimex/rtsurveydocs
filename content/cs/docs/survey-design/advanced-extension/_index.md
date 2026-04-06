---
title: "Pokročilá rozšíření"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 289
---

Sloupec `appearance` v rtSurvey vám umožňuje přizpůsobit vizuální prezentaci a chování otázek ve vašich průzkumech. Tato funkce zlepšuje uživatelský zážitek a může výrazně zlepšit efektivitu sběru dat. rtSurvey podporuje standardní atributy vzhledu XLSForm a rozšiřuje je o další možnosti.

## Rozšíření vzhledu specifická pro rtSurvey

rtSurvey rozšiřuje standardní možnosti vzhledu o následující:

### Přizpůsobení zadávání času

Pro otázky typu `text` používané pro zadávání času:

- `appearance:` — Zobrazí hodiny pro výběr hodin a minut
- `appearance: inline` — Zobrazí hodiny jako ikonu
- `appearance: inline-1line` — Zobrazí hodiny ve formátu jednoho řádku
- `appearance: inline-onlyresult` — Zobrazí ikonu hodin, po výběru zmizí
- `appearance: inline-[FORMAT]` — Přizpůsobí zobrazení formátu času (např. `[%H:%M]`, `[%h:%M:%S]`)

### Přizpůsobení barev

rtSurvey umožňuje přizpůsobení barev pro různé vzhleды:

- `appearance: inline colors("0099FF")` — Přizpůsobí barvu ikony
- `appearance: inline-1line colors("0000FF","FFFF00")` — Přizpůsobí barvy ve formátu jednoho řádku

### Mřížkové rozvržení

rtSurvey zavádí mřížkové rozvržení pro kompaktní zobrazení podobné tabulce:

- `appearance: grid` — Aplikuje se na skupiny pro vytvoření mřížkového rozvržení

### Sbalitelné skupiny

- `appearance: collapsible` — Vytváří rozbalovací/sbalitelné skupiny

## Osvědčené postupy pro použití vzhledu

1. **Konzistentnost**: Používejte atributy vzhledu konzistentně v celém průzkumu pro jednotný vzhled.
2. **Mobil vs. Web**: Zvažte, jak se vzhled zobrazí na různých zařízeních a platformách.
3. **Výkon**: Buďte opatrní s atributy vzhledu, které mohou zpomalit načítání formuláře (např. `table-list` pro velké skupiny).
4. **Uživatelský zážitek**: Vyberte vzhled, který usnadní a zintutitivní zadávání dat pro respondenty.
5. **Testování**: Vždy testujte formulář na cílových zařízeních, abyste se ujistili, že vzhled funguje správně.

## Pokročilé techniky

### Kombinování vzhledů

Některé atributy vzhledu lze kombinovat pro složitější rozvržení:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Select one: | minimal compact |
```

### Dynamické vzhled

rtSurvey umožňuje dynamické změny vzhledu na základě logiky formuláře:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Enter time: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Požadavky na mobilní aplikaci

- Některé vzhleды (např. `quick`, `signature`) jsou specifické pro mobilní zařízení.
- Testujte důkladně na Androidu i iOS pro zajištění konzistentního chování.

## Známá omezení

- Složité vzhleды nemusí být vykreslovány identicky na všech platformách.
- Některé pokročilé vzhleды rtSurvey nemusí být podporovány v offline režimu.

## Řešení problémů se vzhledem

1. **Vzhled není použit**: Zkontrolujte překlepy ve sloupci appearance.
2. **Nekonzistentní vykreslování**: Ověřte kompatibilitu s typem otázky a platformou.
3. **Problémy s výkonem**: Zvažte zjednodušení složitých vzhledů, zejména pro velké průzkumy.
