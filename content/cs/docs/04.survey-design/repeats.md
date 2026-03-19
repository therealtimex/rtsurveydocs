---
title: "Opakování otázek"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 260
---

Opakování jsou výkonnou funkcí v rtSurvey, která vám umožňuje shromažďovat stejnou sadu informací vícekrát v rámci jednoho průzkumu. To je zvláště užitečné pro scénáře jako průzkumy domácností, kde může být nutné shromáždit data o více členech domácnosti.

## Základní struktura opakování

Pro vytvoření opakování v rtSurvey použijte konstrukt `begin repeat` a `end repeat`:

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat | Dítě                 |
| text         | child_name   | Jméno dítěte         |
| integer      | child_age    | Věk dítěte           |
| end repeat   |              |                      |
```

## Nastavení počtu opakování

Ve výchozím nastavení enumerátor rozhoduje, kolikrát opakovat. Počet opakování lze pevně nastavit pomocí `repeat_count`:

```
| type         | name     | label             | repeat_count    |
|--------------|----------|-------------------|-----------------|
| integer      | num_kids | Počet dětí?       |                 |
| begin repeat | children | Dítě              | ${num_kids}     |
| text         | child_name| Jméno dítěte     |                 |
| end repeat   |          |                   |                 |
```

## Označení opakování

Použijte `jr:count` nebo přidejte pole `index()` pro označení každého opakování:

```
| type         | name       | label          |
|--------------|------------|----------------|
| begin repeat | members    | Člen           |
| note         | member_num | Člen č. ${index()} |
| text         | member_name| Jméno          |
| end repeat   |            |                |
```

## Shrnování dat opakování

Použijte agregační funkce pro shrnutí dat z opakování mimo skupinu opakování:

```
| type         | name         | label          | calculation              |
|--------------|--------------|----------------|--------------------------|
| begin repeat | loans        | Půjčka         |                          |
| decimal      | loan_amount  | Výše půjčky    |                          |
| end repeat   |              |                |                          |
| calculate    | total_loans  |                | sum(${loan_amount})      |
| note         | summary      | Celkem půjček: ${total_loans} | |
```

## Osvědčené postupy

1. Vždy používejte `repeat_count`, pokud je počet opakování předem znám.
2. Skupiny opakování udržujte zaměřené — opakování s více než 20 otázkami na instanci je obtížné navigovat.
3. Jasně pojmenujte skupiny opakování (např. `household_members`, ne `repeat1`).
4. Testujte s maximálním očekávaným počtem instancí pro ověření výkonu.
5. Použijte vzhled `field-list` na skupinu opakování pro zobrazení všech polí na jedné obrazovce na instanci (mobilní).

## Omezení

- `indexed-repeat()` vyžaduje platný index (1 až počet instancí) — indexy mimo rozsah vrátí prázdnou hodnotu.
- Vnořená opakování nad 2 úrovně se nedoporučují a mohou způsobit problémy se zobrazením na některých klientech.
- Agregační funkce (`sum`, `count` atd.) pracují na celé skupině opakování — nelze agregovat podmnožinu instancí bez variant `*-if`.
