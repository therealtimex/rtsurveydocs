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

### Porovnávacie operátory

{{< table >}}
Operátor | Operácia      | Príklad              | Príklad výsledku
-------- | -------------- | -------------------- | --------------
`=`        | Rovná sa          | ${age} = 25     | true alebo false
`!=`       | Nerovná sa      | ${age} != 25    | true alebo false
`>`        | Väčší ako   | ${age} > 25     | true alebo false
`>=`       | Väčší alebo rovný | ${age} >= 25 | true alebo false
`<`        | Menší ako      | ${age} < 25     | true alebo false
`<=`       | Menší alebo rovný | ${age} <= 25  | true alebo false
{{< /table >}}

V príkladoch vyššie ${age} predstavuje hodnotu aktuálneho poľa a operátor sa používa na jej porovnanie s hodnotou 25. Obmedzenie sa vyhodnotí na true alebo false v závislosti od toho, či je porovnanie splnené alebo nie.

### Logické operátory

Logické operátory sa používajú na kombinovanie viacerých výrazov v obmedzeniach. Tu sú niektoré bežne používané logické operátory spolu s ich operáciami a príkladmi:

Operátor | Operácia      | Príklad                                           
-------- | -------------- | --------------------------------------------------
`or`       | Vráti true ak je niektorý výraz pravdivý          | ${age} = 3 or ${age} = 4
`and`      | Vráti true iba ak sú oba výrazy pravdivé    | ${age} > 3 and ${age} < 5
`not()`    | Vráti true ak výraz nie je pravdivý        | not(${age} > 3 and ${age} < 5)

V príkladoch vyššie ${age} predstavuje hodnotu aktuálneho poľa a logické operátory sa používajú na kombinovanie výrazov. Obmedzenie sa vyhodnotí na true alebo false na základe zadaných podmienok.

Príklad 1:
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` vráti `true` ak je vek buď 3 alebo 4." />}}

Príklad 2:
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` vráti `true` ak je vek medzi 3 a 5." />}}

Príklad 3:
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` vráti `true` ak vek nie je medzi 3 a 5." />}}
