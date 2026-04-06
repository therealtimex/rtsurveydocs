---
title: "Klíčové koncepty"
description: "Přehled návrhu formulářů"
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 210
---

## Co je XLSForm?
rtSurvey používá rozšířenou verzi standardu [XLSForm](https://xlsform.org/) pro návrh formulářů a nabízí výkonné funkce pro vytváření sofistikovaných průzkumů. Tento průvodce vás seznámí s klíčovými koncepty návrhu formulářů v rtSurvey, od základní struktury XLSForm po pokročilé funkce specifické pro rtSurvey.

S XLSForms můžete vytvářet formuláře ve čitelném formátu pomocí známého nástroje Excel, čímž jsou přístupné téměř každému. Tento standard umožňuje snadné sdílení a spolupráci při vytváření formulářů.

Ačkoliv jsou XLSForms přátelské pro začátečníky, umožňují zkušeným uživatelům také vytvářet složité formuláře.

rtSurvey poskytuje konzistentní způsob, jak zahrnout pokročilé funkce jako logiku přeskočení do formulářů napříč různými webovými a mobilními platformami pro sběr dat.

## Struktura XLSForm
XLSForm typicky sestává ze dvou hlavních listů:

1. **survey**: Definuje strukturu a obsah formuláře.
2. **choices**: Specifikuje možnosti odpovědí pro otázky s výběrem odpovědi.

Volitelný list **settings** může poskytnout další specifikace formuláře.

Je důležité poznamenat, že povinné sloupce v listech survey a choices musí být přítomny, aby formulář fungoval správně. Volitelné sloupce v obou listech poskytují další kontrolu nad chováním každého záznamu ve formuláři, ale nejsou nezbytné.

Sloupce v excelovém sešitu mohou být v libovolném pořadí a volitelné sloupce mohou být ponechány prázdné. Nicméně je klíčové používat přesnou syntaxi a konvence pojmenování specifikované v dokumentaci XLSForm, aby formulář fungoval správně.

### List survey
**List survey** je místo, kde definujete strukturu formuláře a poskytujete obsah. Každý řádek v listu survey představuje otázku nebo prvek ve formuláři. Následující sloupce jsou povinné v listu survey:

- `type`: Určuje typ záznamu, který očekáváte pro otázku.
- `name`: Určuje jedinečný název proměnné pro daný záznam. Názvy musí začínat písmenem nebo podtržítkem a mohou obsahovat pouze písmena, číslice, pomlčky, podtržítka a tečky. Názvy jsou citlivé na velikost písmen.
- `label`: Obsahuje skutečný text, který vidíte pro otázku ve formuláři.

| type                | name     | label                |
| ------------------- | -------- | -------------------- |
| today               | today    |                      |
| select_one gender   | gender   | Pohlaví respondenta? |
| integer             | age      | Věk respondenta?     |

### List choices
**List `choices`** se používá pro specifikaci možností odpovědí pro otázky s výběrem odpovědi. Každý řádek představuje možnost odpovědi. Následující sloupce jsou povinné v listu choices:

- **`list_name`**: Seskupuje sadu souvisejících možností odpovědí.
- **`name`**: Jedinečný identifikátor pro každou možnost odpovědi.
- **`label`**: Textový popis, který se zobrazí respondentovi.

| list_name | name   | label  |
|-----------|--------|--------|
| gender    | male   | Muž    |
| gender    | female | Žena   |
| gender    | other  | Jiné   |

### Nastavení formuláře (volitelné)
Volitelný list **settings** vám umožňuje poskytnout metadata formuláře jako název formuláře, verzi nebo výchozí jazyk.

## Odkaz na klíčové koncepty XLSForm

### Typy otázek
rtSurvey podporuje všechny standardní typy otázek XLSForm a navíc několik rozšíření. Viz [Typy otázek](question-types) pro kompletní přehled.

### Logika přeskočení (relevance)
Sloupec `relevant` umožňuje podmíněné zobrazení otázek. Viz [Přeskakování otázek](relevant).

### Omezení a validace
Sloupec `constraint` definuje pravidla validace. Viz [Validace odpovědí](constraint).

### Výchozí hodnoty
Sloupec `default` předvyplňuje otázky počátečními hodnotami. Viz [Výchozí hodnoty](default).

### Opakování
Skupiny `begin_repeat`/`end_repeat` umožňují sběr opakujících se dat. Viz [Opakování otázek](repeats).

### Skupiny
Skupiny `begin_group`/`end_group` organizují otázky. Viz [Seskupování otázek](grouping-questions).
