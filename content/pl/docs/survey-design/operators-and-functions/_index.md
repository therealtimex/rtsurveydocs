---
title: "Operatory i funkcje"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 290
---

Wyrażenia w rtSurvey są pisane w podzbiorze **XPath 1.0**, rozszerzonym o funkcje JavaRosa/ODK i niestandardowe funkcje rtSurvey. Wyrażenia są używane w kolumnach `calculate`, `constraint`, `relevant`, `required` i `default` XLSForm.

## Odwoływanie się do wartości pól

Użyj `${nazwa_pola}`, aby odwołać się do wartości innego pola:

```
${age} > 18
```

Użyj `.` (pojedynczej kropki), aby odwołać się do **wartości bieżącego pola** — często używane w wyrażeniach `constraint`:

```
. >= 0 and . <= 100
```

Użyj `..`, aby odwołać się do grupy nadrzędnej (zaawansowane użycie w powtórzeniach).

## Składnia wyrażeń

Wyrażenia przestrzegają standardowych reguł XPath:

- **Ciągi znaków** muszą być ujęte w pojedyncze cudzysłowy: `'yes'`
- **Liczby** są pisane bezpośrednio: `42`, `3.14`
- **Boolean** wyniki są używane dla `relevant`, `required` i `constraint` — każda niepusta, niezerowa wartość jest prawdziwa
- Białe znaki są ignorowane wokół operatorów

{{% alert icon=" " context="warning" %}}
Zawsze używaj prostych cudzysłowów (`'` lub `"`) — nigdy „inteligentnych cudzysłowów" (cudzysłowów kręconych). Edytory tekstu sformatowanego często automatycznie konwertują cudzysłowy, co spowoduje błędy w wyrażeniach.
{{% /alert %}}

## Sekcje w tym rozdziale

- **[Operatory](operators)** — operatory porównania (`=`, `!=`, `>`, `<`, `>=`, `<=`) i operatory logiczne (`and`, `or`, `not()`)
- **[Funkcje](functions)** — funkcje ciągów znaków, wyboru, liczbowe, daty/czasu, boolean, geo i narzędziowe
- **[Odwołania](references)** — jak odwoływać się do pól i wartości kontekstowych

## Szybkie przykłady

| Przypadek użycia | Wyrażenie |
|----------|------------|
| Pokaż jeśli wiek przekracza 18 | `${age} > 18` |
| Pokaż tylko jeśli wybrano „tak" | `${consent} = 'yes'` |
| Wymagaj jeśli inne pole nie jest puste | `${name} != ''` |
| Oblicz sumę | `${adults} + ${children}` |
| Połącz imię | `concat(${first_name}, ' ', ${last_name})` |
| Dzisiejsza data | `today()` |
| Sprawdź czy opcja była wybrana | `selected(${interests}, 'sports')` |
