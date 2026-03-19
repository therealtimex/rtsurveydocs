---
title: "Operátory"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 292
---

### Operátory porovnání

{{< table >}}
Operátor | Operace        | Příklad              | Příklad výsledku
-------- | -------------- | -------------------- | ----------------
`=`        | Rovná se       | ${age} = 25     | true nebo false
`!=`       | Nerovná se     | ${age} != 25    | true nebo false
`>`        | Větší než      | ${age} > 25     | true nebo false
`>=`       | Větší nebo rovno | ${age} >= 25  | true nebo false
`<`        | Menší než      | ${age} < 25     | true nebo false
`<=`       | Menší nebo rovno | ${age} <= 25  | true nebo false
{{< /table >}}

Ve výše uvedených příkladech ${age} představuje hodnotu aktuálního pole a operátor se používá pro porovnání s hodnotou 25. Omezení se vyhodnotí na true nebo false v závislosti na tom, zda je porovnání splněno nebo ne.

### Logické operátory

Logické operátory se používají pro kombinování více výrazů v omezeních. Zde jsou běžně používané logické operátory spolu s jejich operacemi a příklady:

Operátor | Operace        | Příklad                                           
-------- | -------------- | --------------------------------------------------
`or`       | Vrátí true, pokud je pravdivý alespoň jeden výraz | ${age} = 3 or ${age} = 4
`and`      | Vrátí true pouze pokud jsou oba výrazy pravdivé   | ${age} > 3 and ${age} < 5
`not()`    | Neguje logický výraz                               | not(${age} = 25)
