---
title: "Select_one"
description: "Otázky select_one umožňují respondentům vybrat přesně jednu možnost z předdefinovaného seznamu voleb."
icon: "radio_button_checked"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 224
---

Typ otázky `select_one` vyzve respondenta k výběru **přesně jedné možnosti** z předdefinovaného seznamu. Ve výchozím nastavení se volby zobrazují jako přepínače, ale je k dispozici široká škála možností vzhledu pro změnu rozvržení a chování.

## Základní specifikace XLSForm

**list survey:**

| type | name | label |
|------|------|-------|
| select_one yesno | consent | Dal respondent souhlas? |

**list choices:**

| list_name | name | label |
|-----------|------|-------|
| yesno | yes | Ano |
| yesno | no | Ne |

`listname` v `select_one listname` musí odpovídat sloupci `list_name` v listu choices.

## Použití

Otázky select_one se používají pro:

1. Otázky Ano/Ne
2. Výběr jedné odpovědi s více možnostmi (např. úroveň vzdělání, pohlaví, rodinný stav)
3. Kategorická hodnocení (např. špatné / uspokojivé / dobré / výborné)
4. Kaskádové (propojené) výběry, kde se volby filtrují na základě předchozí odpovědi
5. Výběr země, regionu, okresu nebo jiné administrativní jednotky

## Možnosti vzhledu

Zadejte hodnotu do sloupce `appearance` pro změnu zobrazení voleb:

{{< table >}}
| Vzhled | Popis |
|--------|-------|
| *(žádný)* | Výchozí přepínače, jeden na řádek |
| `minimal` | Jednoduchá rozbalovací nabídka místo přepínačů |
| `quick` | Automaticky přejde na další otázku ihned po výběru (pouze mobil) |
| `compact` | Kompaktní mřížka voleb — počet sloupců se přizpůsobuje šířce obrazovky |
| `compact-N` | Kompaktní mřížka vynucená na N sloupců (např. `compact-3`) |
| `quickcompact` | Kombinuje `quick` a `compact` |
| `quickcompact-N` | Kombinuje `quick` a `compact` s N vynucenými sloupci |
| `horizontal` | Volby uspořádané horizontálně v řadě (web) |
| `horizontal-compact` | Horizontální, kompaktní mezery (web) |
| `likert` | Řádek Likertovy škály — popisky nahoře, přepínače dole |
| `label` | Zobrazuje pouze popisky voleb bez vstupů (použijte spárovaně s `list-nolabel`) |
| `list-nolabel` | Zobrazuje pouze vstupy bez popisků (použijte spárovaně s `label`) |
| `columns(N)` | Zobrazení v N sloupcích (rozšíření rtSurvey, např. `columns(3)`) |
| `distress` | Widget emočních ikon Kesslerovy psychologické tísně (K10) |
| `search-api(...)` | Dynamické vyhledávání — načítá volby z API za běhu |
{{< /table >}}

### Příklad: Likertova škála

| type | name | label | appearance |
|------|------|-------|------------|
| select_one satisfaction | service_rating | Jak jste spokojeni se službou? | likert |

### Příklad: Kompaktní 3 sloupce

| type | name | label | appearance |
|------|------|-------|------------|
| select_one regions | region | Vyberte region | compact-3 |

## Kaskádové výběry

Kaskádový (propojený) výběr filtruje volby na základě hodnoty vybrané v předchozí otázce. Použijte sloupec `choice_filter` s názvem sloupce z listu choices.

**survey:**

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one province | province | Vyberte provincii | |
| select_one district | district | Vyberte okres | province_name = ${province} |

**choices:**

| list_name | name | label | province_name |
|-----------|------|-------|---------------|
| province | nairobi | Nairobi | |
| province | mombasa | Mombasa | |
| district | westlands | Westlands | nairobi |
| district | kasarani | Kasarani | nairobi |
| district | nyali | Nyali | mombasa |
| district | likoni | Likoni | mombasa |

Když respondent vybere `nairobi`, v seznamu okresů se zobrazí pouze `Westlands` a `Kasarani`.

{{% alert icon=" " context="warning" %}}
Název sloupce použitý v `choice_filter` (např. `province_name`) musí existovat v listu choices. `${province}` odkazuje na pole průzkumu pojmenované `province`.
{{% /alert %}}

## Použití vybrané hodnoty ve výrazech

Odkazujte na vybranou **hodnotu** (nikoli popisek) pomocí `${fieldname}`:

```
relevant: ${consent} = 'yes'
```

Pro získání popisku volby místo hodnoty použijte `choice-label()`:

```
calculate: choice-label(${education_level}, ${education_level})
```

## Možnost „Jiné" s volným textem

Běžný vzor je zahrnout možnost „jiné", která odhalí textové pole:

| type | name | label | relevant |
|------|------|-------|----------|
| select_one occupation | job | Jaké je vaše povolání? | |
| text | job_other | Prosím upřesněte | `${job} = 'other'` |

## Osvědčené postupy

1. Udržujte seznamy krátké a vzájemně se vylučující — pokud by respondenti mohli chtít více než jednu, použijte místo toho `select_multiple`.
2. Umístěte nejčastější odpověď na první místo nebo seřaďte abecedně pro dlouhé seznamy.
3. Vždy zahrňte možnost „Nevím" nebo „Nechci odpovídat", kde je to relevantní.
4. Používejte `minimal` (rozbalovací nabídka) pro seznamy s více než 7–8 volbami na mobilu pro úsporu místa na obrazovce.
5. Pro kaskádové výběry přidejte všechny sloupce filtru v listu choices před sestavením formuláře.

## Omezení

- Respondent může vybrat pouze jednu volbu — pro otázky s více odpověďmi použijte `select_multiple`.
- Vzhled `likert` nejlépe funguje s 5–7 volbami, které se vejdou na jeden řádek.
- Automatický postup `quick` je pouze pro mobil; na webových formulářích nemá žádný efekt.
