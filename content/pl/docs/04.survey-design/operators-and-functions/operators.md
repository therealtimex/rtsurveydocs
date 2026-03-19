---
title: "Operatory"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 292
---

### Operatory porównania

{{< table >}}
Operator | Operacja       | Przykład             | Przykładowa odpowiedź
-------- | -------------- | -------------------- | --------------
`=`        | Równy          | ${age} = 25     | prawda lub fałsz
`!=`       | Różny          | ${age} != 25    | prawda lub fałsz
`>`        | Większy niż    | ${age} > 25     | prawda lub fałsz
`>=`       | Większy lub równy | ${age} >= 25 | prawda lub fałsz
`<`        | Mniejszy niż   | ${age} < 25     | prawda lub fałsz
`<=`       | Mniejszy lub równy | ${age} <= 25 | prawda lub fałsz
{{< /table >}}

W powyższych przykładach ${age} reprezentuje bieżącą wartość pola, a operator jest używany do jej porównania z wartością 25. Ograniczenie zostanie ocenione jako prawda lub fałsz, w zależności od tego, czy porównanie jest spełnione.

### Operatory logiczne

Operatory logiczne są używane do łączenia wielu wyrażeń w ograniczeniach. Oto niektóre powszechnie używane operatory logiczne wraz z ich operacjami i przykładami:

Operator | Operacja       | Przykład                                          
-------- | -------------- | --------------------------------------------------
`or`       | Zwraca prawdę jeśli którekolwiek wyrażenie jest prawdziwe | ${age} = 3 or ${age} = 4
`and`      | Zwraca prawdę tylko jeśli oba wyrażenia są prawdziwe | ${age} > 3 and ${age} < 5
`not()`    | Zwraca prawdę jeśli wyrażenie nie jest prawdziwe | not(${age} > 3 and ${age} < 5)

W powyższych przykładach ${age} reprezentuje bieżącą wartość pola, a operatory logiczne są używane do łączenia wyrażeń.

Przykład 1:
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` zwróci `prawdę` jeśli wiek wynosi 3 lub 4." />}}

Przykład 2:
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` zwróci `prawdę` jeśli wiek wynosi między 3 a 5." />}}

Przykład 3:
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` zwróci `prawdę` jeśli wiek nie wynosi między 3 a 5." />}}
