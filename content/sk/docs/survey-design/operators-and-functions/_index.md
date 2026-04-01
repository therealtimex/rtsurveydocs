---
title: "Operátory a funkcie"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 290
---

Výrazy v rtSurvey sú písané v podmnožine **XPath 1.0**, rozšírenej o funkcie JavaRosa/ODK a vlastné funkcie rtSurvey. Výrazy používate v stĺpcoch `calculate`, `constraint`, `relevant`, `required` a `default` vášho XLSForm.

## Odkazovanie hodnôt polí

Použite `${fieldname}` na odkazovanie hodnoty iného poľa:

```
${age} > 18
```

Použite `.` (jednu bodku) na odkazovanie **hodnoty aktuálneho poľa** — bežne sa používa vo výrazoch `constraint`:

```
. >= 0 and . <= 100
```

Použite `..` na odkazovanie nadradenej skupiny (pokročilé použitie v opakovaniach).

## Syntax výrazov

Výrazy sa riadia štandardnými pravidlami XPath:

- **Reťazce** musia byť uzavreté do jednoduchých úvodzoviek: `'yes'`
- **Čísla** sa píšu tak, ako sú: `42`, `3.14`
- **Boolean** výsledky sa používajú pre `relevant`, `required` a `constraint` — akákoľvek neprázdna, nenulová hodnota je pravdivá
- Whitespace sa okolo operátorov ignoruje

{{% alert icon=" " context="warning" %}}
Vždy používajte rovné úvodzovky (`'` alebo `"`) — nikdy „typografické úvodzovky" (kučeravé úvodzovky). Editory bohatého textu úvodzovky často automaticky konvertujú a tým poruší vaše výrazy.
{{% /alert %}}

## Sekcie v tejto kapitole

- **[Operátory](operators)** — porovnávacie operátory (`=`, `!=`, `>`, `<`, `>=`, `<=`) a logické operátory (`and`, `or`, `not()`)
- **[Funkcie](functions)** — funkcie reťazcov, výberu, čísel, dátumu/času, boolean, geo a utility funkcie
- **[Referencie](references)** — ako odkazovať na polia a kontextové hodnoty

## Rýchle príklady

| Prípad použitia | Výraz |
|----------|------------|
| Zobraziť ak je vek nad 18 | `${age} > 18` |
| Zobraziť iba ak bolo vybrané „yes" | `${consent} = 'yes'` |
| Vyžadovať ak iné pole nie je prázdne | `${name} != ''` |
| Vypočítať súčet | `${adults} + ${children}` |
| Spojiť meno | `concat(${first_name}, ' ', ${last_name})` |
| Dnešný dátum | `today()` |
| Skontrolovať či bola možnosť vybraná | `selected(${interests}, 'sports')` |
