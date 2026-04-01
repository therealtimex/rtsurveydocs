---
title: "Operatori"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 292
---

### Operatori poređenja

{{< table >}}
Operator | Operacija          | Primer              | Primer odgovora
-------- | ------------------ | ------------------- | ---------------
`=`      | Jednako            | ${age} = 25     | tačno ili netačno
`!=`     | Nije jednako       | ${age} != 25    | tačno ili netačno
`>`      | Veće od            | ${age} > 25     | tačno ili netačno
`>=`     | Veće ili jednako   | ${age} >= 25    | tačno ili netačno
`<`      | Manje od           | ${age} < 25     | tačno ili netačno
`<=`     | Manje ili jednako  | ${age} <= 25    | tačno ili netačno
{{< /table >}}

U gornjim primerima, ${age} predstavlja vrednost trenutnog polja, a operator se koristi za poređenje sa vrednošću 25. Ograničenje će se evaluirati kao tačno ili netačno, u zavisnosti od toga da li je poređenje zadovoljeno ili ne.

### Logički operatori

Logički operatori se koriste za kombinovanje više izraza u ograničenjima. Evo nekih uobičajeno korišćenih logičkih operatora zajedno sa njihovim operacijama i primerima:

Operator | Operacija                                                    | Primer                                           
-------- | ------------------------------------------------------------ | --------------------------------------------------
`or`     | Vraća tačno ako je bilo koji izraz tačan                     | ${age} = 3 or ${age} = 4
`and`    | Vraća tačno samo ako su oba izraza tačna                     | ${age} > 3 and ${age} < 5
`not()`  | Vraća tačno ako izraz nije tačan                             | not(${age} > 3 and ${age} < 5)

U gornjim primerima, ${age} predstavlja vrednost trenutnog polja, a logički operatori se koriste za kombinovanje izraza. Ograničenje će se evaluirati kao tačno ili netačno na osnovu navedenih uslova.

Primer 1:
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` će vratiti `tačno` ako je godine 3 ili 4." />}}

Primer 2:
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` će vratiti `tačno` ako su godine između 3 i 5." />}}

Primer 3:
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` će vratiti `tačno` ako godine nisu između 3 i 5." />}}
