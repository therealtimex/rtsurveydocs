---
title: "Operatorer"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 292
---

### Jämförelseoperatorer

{{< table >}}
Operator | Åtgärd         | Exempel              | Exempelsvar
-------- | -------------- | -------------------- | --------------
`=`        | Lika med       | ${age} = 25     | true eller false
`!=`       | Inte lika med  | ${age} != 25    | true eller false
`>`        | Större än      | ${age} > 25     | true eller false
`>=`       | Större än eller lika med | ${age} >= 25 | true eller false
`<`        | Mindre än      | ${age} < 25     | true eller false
`<=`       | Mindre än eller lika med | ${age} <= 25  | true eller false
{{< /table >}}

I exemplen ovan representerar ${age} det aktuella fältets värde, och operatorn används för att jämföra det med värdet 25. Begränsningen utvärderas till antingen true eller false, beroende på om jämförelsen uppfylls eller inte.

### Logiska operatorer

Logiska operatorer används för att kombinera flera uttryck i begränsningar. Här är några vanliga logiska operatorer tillsammans med deras åtgärder och exempel:

Operator | Åtgärd         | Exempel                                           
-------- | -------------- | --------------------------------------------------
`or`       | Returnerar true om något av uttrycken är true   | ${age} = 3 or ${age} = 4
`and`      | Returnerar true bara om båda uttrycken är true  | ${age} > 3 and ${age} < 5
`not()`    | Returnerar true om uttrycket inte är true       | not(${age} > 3 and ${age} < 5)

I exemplen ovan representerar ${age} det aktuella fältets värde, och de logiska operatorerna används för att kombinera uttryck. Begränsningen utvärderas till true eller false baserat på de angivna villkoren.

Exempel 1:
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` returnerar `true` om åldern är antingen 3 eller 4." />}}

Exempel 2:
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` returnerar `true` om åldern är mellan 3 och 5." />}}

Exempel 3:
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` returnerar `true` om åldern inte är mellan 3 och 5." />}}
