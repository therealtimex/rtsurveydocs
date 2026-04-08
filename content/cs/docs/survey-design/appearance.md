---
title: "Vzhled"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

Sloupec `appearance` v rtSurvey vám umožňuje přizpůsobit vizuální prezentaci a chování otázek ve vašich průzkumech. Tato funkce zlepšuje uživatelský zážitek a může výrazně zvýšit efektivitu sběru dat. rtSurvey podporuje standardní atributy vzhledu XLSForm a rozšiřuje je o další možnosti.

## Standardní atributy vzhledu XLSForm

rtSurvey podporuje následující standardní atributy vzhledu XLSForm:

| Atribut vzhledu | Typy otázek | Popis |
|----------------------|----------------|-------------|
| multiline | text | Vytvoří víceřádkové textové pole (nejlepší pro webové klienty) |
| minimal | select_one, select_multiple | Zobrazí možnosti v rozevíracím menu |
| quick | select_one | Automaticky přejde na další otázku po výběru (pouze mobilní) |
| no-calendar | date | Potlačí zobrazení kalendáře (pouze mobilní) |
| month-year | date | Umožní výběr pouze měsíce a roku |
| year | date | Umožní výběr pouze roku |
| horizontal-compact | select_one, select_multiple | Zobrazí možnosti horizontálně (pouze web) |
| horizontal | select_one, select_multiple | Zobrazí možnosti horizontálně ve sloupcích (pouze web) |
| likert | select_one | Prezentuje možnosti jako Likertovu škálu |
| compact | select_one, select_multiple | Zobrazí možnosti vedle sebe s minimálním odsazením |
| quickcompact | select_one | Kombinuje kompaktní zobrazení s automatickým přechodem (pouze mobilní) |
| field-list | skupiny | Zobrazí celou skupinu na jedné obrazovce (pouze mobilní) |
| label | select_one, select_multiple | Zobrazí popisky možností bez vstupů |
| list-nolabel | select_one, select_multiple | Zobrazí vstupy bez popisků (použijte s `label`) |
| table-list | skupiny | Zobrazí otázky ve formátu tabulky |
| signature | image | Povolí zachycení podpisu (pouze mobilní) |
| draw | image | Umožní volné kreslení (pouze mobilní) |
| map, quick map | select_one, select_one_from_file | Umožní výběr z mapových prvků |

## Osvědčené postupy pro používání vzhledu

1. **Konzistence**: Používejte atributy vzhledu konzistentně napříč průzkumem pro jednotný vzhled.
2. **Mobilní vs. web**: Zvažte, jak se vzhled bude vykreslovat na různých zařízeních a platformách.
3. **Výkon**: Buďte opatrní s atributy vzhledu, které by mohly zpomalit načítání formuláře (např. `table-list` pro velké skupiny).
4. **Uživatelský zážitek**: Vybírejte vzhled, který usnadní zadávání dat a bude intuitivnější pro respondenty.
5. **Testování**: Vždy testujte formulář na cílových zařízeních, abyste se ujistili, že se vzhled zobrazuje správně.

## Pokročilé techniky

### Kombinování vzhledů

Některé atributy vzhledu lze kombinovat pro složitější rozvržení:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Vyberte jednu: | minimal compact |
```

### Dynamický vzhled

rtSurvey umožňuje dynamické změny vzhledu na základě logiky formuláře:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Zadejte čas: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Rozšířené atributy vzhledu rtSurvey

Kromě standardních vzhledů XLSForm rtSurvey podporuje následující možnosti specifické pro platformu:

### Kontrola dat a zobrazení

| Atribut vzhledu | Typy otázek | Popis |
|----------------------|----------------|-------------|
| `invisible` | libovolné | Skryje pole ze zobrazení při zachování sběru nebo výpočtu hodnoty. Liší se od typu `hidden` — pole se stále účastní logiky. |
| `displaytitle` | libovolné | Vynutí zobrazení popisku/názvu pole, i když by byl jinak potlačen. |
| `autopull` | select_one, select_multiple | Automaticky načte externí data pro naplnění možností při načtení formuláře nebo změně spouštěcího pole. |
| `floating_hint` | text, integer, decimal | Zobrazí text nápovědy jako plovoucí popisek nad vstupním polem místo pod ním. |
| `calculate-button` | calculate | Přidá viditelné tlačítko, které spustí přepočítání pole na vyžádání, místo automatického výpočtu. |

### Rozvržení

| Atribut vzhledu | Typy otázek | Popis |
|----------------------|----------------|-------------|
| `1screen` | skupina | Vynutí zobrazení celé skupiny na jedné obrazovce bez ohledu na velikost skupiny. |
| `columns(n)` | select_one, select_multiple | Zobrazí možnosti v `n` sloupcích. Příklad: `columns(3)` zobrazí tři sloupce přepínacích tlačítek. |
| `gridformat<row=R col=C colspan=S align=center>` | libovolné | Umístí pole do rozvržení CSS-grid na řádku `R`, sloupci `C`, pokrývající `S` sloupců. Použijte s `advanced-extension/grid-layout`. |
| `ignore-simplify` | libovolné | Instruuje vykreslovač formuláře, aby přeskočil automatické zjednodušení nebo kondenzaci rozvržení tohoto pole. |
| `required-but-simplify` | libovolné | Pole je povinné, ale jeho rozvržení je stále zjednodušeno vykreslovačem (přepíše výchozí chování, kde povinná pole jsou vyloučena ze zjednodušení). |
| `embed` | libovolné | Vykreslí pole ve vloženém/inline režimu zobrazení, potlačí jeho vnější obal a kontejner popisku — používá se, když je otázka vnořena do vlastního HTML. |
| `popup` | select_one, select_multiple | Vykreslí seznam voleb v překryvném/modálním okně místo inline. |
| `auto-hide-empty` | boxtag, select | Skryje celý widget otázky, když je seznam voleb prázdný (např. API nevrátilo žádné výsledky). |
| `text-nolabel` | select_one, select_multiple | Skryje textový popisek každé volby, zobrazuje pouze vstupní ovládací prvek. Podobné `list-nolabel`, ale aplikováno pro každou volbu, nikoli jako rozdělení sloupců. |

### Widgety

| Atribut vzhledu | Typy otázek | Popis |
|----------------------|----------------|-------------|
| `likert` | select_one | Prezentuje možnosti jako řádek Likertovy škály. |
| `distress` | select_one | Vykreslí možnosti jako vizuální widget Kesslera pro psychologický distres (K10) s emočními ikonami. |

### Vizuální widgety pro výběr

Tyto vzhled mění celé vykreslování seznamů voleb pro výběr.

| Atribut vzhledu | Typy otázek | Popis |
|----------------------|----------------|-------------|
| `tagging` | select_one, select_multiple | Volby se zobrazují jako klikatelné tagové čipy ve tvaru pilulek. |
| `boxtag` | select_one, select_multiple | Volby se zobrazují jako obdélníkové stylizované boxy, na které uživatel klepne. |
| `boxtag -search` | select_one, select_multiple | Rozvržení boxtag s živým vyhledávacím/filtrovacím polem nad boxy. |
| `duolingo-style1` | select_one, select_multiple | Rozvržení velkých karet inspirované Duolingem — vhodné pro krátké seznamy s ikonami. |
| `rating_box` | select_one, select_multiple | Mřížka klepatelných číslovaných boxů — vhodná pro škálové nebo NPS otázky. |
| `star_rating` | select_one | Volby se zobrazují jako hvězdičky; počet hvězdičky odpovídá počtu voleb. |
| `choices-noshow` | select_one, select_multiple | Zpočátku zobrazuje pouze prvních 10 voleb s ovládacím prvkem „Zobrazit více". |
| `noshow` | select_one, select_multiple | Skryje seznam voleb úplně; hodnota se nastavuje programově přes `calculate` nebo API. |
| `checkall` | select_multiple | Přidá zkratku „Vybrat vše" na vrchol seznamu voleb. |
| `max-items(N)` | select_one, select_multiple | Omezí viditelný seznam voleb na N položek. Příklad: `max-items(5)`. |

### Vizuální widgety pro text

| Atribut vzhledu | Typy otázek | Popis |
|----------------------|----------------|-------------|
| `richtext` | text | Nahradí prosté textové pole editorem formátovaného textu (tučné, kurzíva, seznamy, odkazy). Ukládá HTML. |
| `typingtest` | text | Widget testu psaní — text popisku je pasáž; widget zaznamenává zadanou odpověď a časování. |

### Mediální rozšíření

| Atribut vzhledu | Typy otázek | Popis |
|----------------------|----------------|-------------|
| `watermark("výraz")` | image | Překryje textový vodoznak na zachycených fotografiích. Argument je výraz XPath vyhodnocený v době zachycení. Příklad: `watermark("${id} ${today()}")`. |
| `editable` | image | Umožní anotaci/kreslení přes zachycenou fotografii před uložením. |

### Konfigurace inline zobrazení

Modifikátory `display{}` a `results{}` lze připojit k `inline` vzhledům pro řízení zarovnání ikon a zobrazení výsledků. Používají se společně s rozšířením inline časového vstupu na polích `text` a s widgety pro zachycení médií.

#### Parametry `display{}`

```
inline display{left}
inline display{right,small}
inline display{top,large,inline-icon}
```

| Parametr | Hodnoty | Popis |
|-----------|--------|-------------|
| Zarovnání | `left`, `right`, `top`, `bottom`, `center` | Pozice ikony relativně k vstupnímu poli |
| Velikost | `small`, `medium`, `large` | Velikost ikony (odpovídá 2,5 rem, 5 rem, 8 rem) |
| Režim | `inline-icon` | Vykreslí spouštěč jako pouze ikonu (bez okraje tlačítka) |
| Režim | `inline-button` | Vykreslí spouštěč jako celé tlačítko |

#### Parametry `results{}`

```
inline results{right}
inline results{left,hide(seconds)}
```

| Parametr | Hodnoty | Popis |
|-----------|--------|-------------|
| Zarovnání | `left`, `right`, `top`, `bottom`, `center` | Pozice zobrazení výsledné hodnoty |
| `hide(pole)` | libovolný název dílčího pole | Skryje konkrétní komponentu výsledku (např. `hide(seconds)`) |

### Integrace API

| Atribut vzhledu | Typy otázek | Popis |
|----------------------|----------------|-------------|
| `callapi` | text, integer, decimal, select_one | Povolí integraci volání API pro toto pole. Sloupec calculation by měl obsahovat výraz `callapi()`. Viz [Volání API](advanced-extension/call-api). |
| `callapi-verify(params)` | text, integer, decimal | Spustí volání API pro ověření pomocí statických parametrů. Formulář zablokuje průchod, dokud API nepotvrdí hodnotu. |
| `callapi-verify(dynamicParams)` | text, integer, decimal | Stejné jako `callapi-verify`, ale s parametry odvozenými z hodnot jiných polí za běhu. |

### Formát data/času inline

Pro pole `date`, `time` a `datetime` můžete zadat vlastní formát zobrazení pomocí formátovacího řetězce přidaného k vzhledu:

```
inline-[%d/%m/%Y]
inline-1line-[%d/%m/%Y %H:%M]
```

Formátovací tokeny jsou stejné jako u `format-date()` a `format-date-time()`. Viz [Funkce — Funkce data a času](operators-and-functions/functions#date-and-time-functions).

## Omezení

- Složité vzhled se nemusí identicky vykreslovat na všech platformách.
- Některé pokročilé vzhled rtSurvey nemusí být podporovány v offline režimu.

## Řešení problémů se vzhledem

1. **Vzhled není použit**: Zkontrolujte překlepy ve sloupci appearance.
2. **Nekonzistentní vykreslování**: Ověřte kompatibilitu s typem otázky a platformou.
3. **Problémy s výkonem**: Zvažte zjednodušení složitých vzhledů, zejména pro velké průzkumy.
