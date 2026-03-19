---
title: "Operátorok"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 292
---

### Összehasonlítási operátorok

{{< table >}}
Operátor | Művelet        | Példa                | Példa válasz
-------- | -------------- | -------------------- | --------------
`=`        | Egyenlő          | ${age} = 25     | igaz vagy hamis
`!=`       | Nem egyenlő      | ${age} != 25    | igaz vagy hamis
`>`        | Nagyobb          | ${age} > 25     | igaz vagy hamis
`>=`       | Nagyobb vagy egyenlő | ${age} >= 25 | igaz vagy hamis
`<`        | Kisebb           | ${age} < 25     | igaz vagy hamis
`<=`       | Kisebb vagy egyenlő | ${age} <= 25  | igaz vagy hamis
{{< /table >}}

A fenti példákban a ${age} az aktuális mező értékét jelöli, az operátor pedig a 25-ös értékkel való összehasonlításhoz használatos. A korlát igaz vagy hamis értékre értékelődik ki, attól függően, hogy az összehasonlítás teljesül-e vagy sem.

### Logikai operátorok

A logikai operátorok több kifejezés kombinálására szolgálnak a korlátokban. Az alábbiakban néhány általánosan használt logikai operátor, azok műveletei és példái:

Operátor | Művelet      | Példa                                           
-------- | -------------- | --------------------------------------------------
`or`       | Igaz, ha valamelyik kifejezés igaz   | ${age} = 3 or ${age} = 4
`and`      | Csak akkor igaz, ha mindkét kifejezés igaz | ${age} > 3 and ${age} < 5
`not()`    | Igaz, ha a kifejezés nem igaz        | not(${age} > 3 and ${age} < 5)

A fenti példákban a ${age} az aktuális mező értékét jelöli, a logikai operátorok pedig a kifejezések kombinálásához használatosak. A korlát igaz vagy hamis értékre értékelődik ki a megadott feltételek alapján.

1. példa:
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` akkor ad vissza `igaz` értéket, ha a kor 3 vagy 4." />}}

2. példa:
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` akkor ad vissza `igaz` értéket, ha a kor 3 és 5 közé esik." />}}

3. példa:
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` akkor ad vissza `igaz` értéket, ha a kor NEM esik 3 és 5 közé." />}}
