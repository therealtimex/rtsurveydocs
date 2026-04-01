---
title: "Operatoren"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 292
---

### Vergleichsoperatoren

{{< table >}}
Operator | Operation      | Beispiel              | Beispielantwort
-------- | -------------- | -------------------- | --------------
`=`        | Gleich          | ${age} = 25     | wahr oder falsch
`!=`       | Ungleich      | ${age} != 25    | wahr oder falsch
`>`        | Größer als   | ${age} > 25     | wahr oder falsch
`>=`       | Größer als oder gleich | ${age} >= 25 | wahr oder falsch
`<`        | Kleiner als      | ${age} < 25     | wahr oder falsch
`<=`       | Kleiner als oder gleich | ${age} <= 25  | wahr oder falsch
{{< /table >}}

In den obigen Beispielen steht ${age} für den Wert des aktuellen Feldes, und der Operator wird verwendet, um ihn mit dem Wert 25 zu vergleichen. Die Einschränkung wird zu wahr oder falsch ausgewertet, abhängig davon, ob der Vergleich erfüllt ist oder nicht.

### Logische Operatoren

Logische Operatoren werden verwendet, um mehrere Ausdrücke in Einschränkungen zu kombinieren. Hier sind einige häufig verwendete logische Operatoren mit ihren Operationen und Beispielen:

Operator | Operation      | Beispiel
-------- | -------------- | --------------------------------------------------
`or`       | Gibt wahr zurück, wenn einer der Ausdrücke wahr ist          | ${age} = 3 or ${age} = 4
`and`      | Gibt nur wahr zurück, wenn beide Ausdrücke wahr sind    | ${age} > 3 and ${age} < 5
`not()`    | Gibt wahr zurück, wenn der Ausdruck nicht wahr ist        | not(${age} > 3 and ${age} < 5)

In den obigen Beispielen steht ${age} für den Wert des aktuellen Feldes, und die logischen Operatoren werden verwendet, um Ausdrücke zu kombinieren. Die Einschränkung wird basierend auf den angegebenen Bedingungen zu wahr oder falsch ausgewertet.

Beispiel 1:
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` gibt `wahr` zurück, wenn das Alter entweder 3 oder 4 ist." />}}

Beispiel 2:
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` gibt `wahr` zurück, wenn das Alter zwischen 3 und 5 liegt." />}}

Beispiel 3:
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` gibt `wahr` zurück, wenn das Alter nicht zwischen 3 und 5 liegt." />}}
