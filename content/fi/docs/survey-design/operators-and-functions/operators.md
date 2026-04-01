---
title: "Operaattorit"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 292
---

### Vertailuoperaattorit

{{< table >}}
Operaattori | Toiminta      | Esimerkki              | Esimerkkivastaus
-------- | -------------- | -------------------- | --------------
`=`        | Yhtä suuri          | ${age} = 25     | tosi tai epätosi
`!=`       | Eri suuri      | ${age} != 25    | tosi tai epätosi
`>`        | Suurempi kuin   | ${age} > 25     | tosi tai epätosi
`>=`       | Suurempi tai yhtä suuri | ${age} >= 25 | tosi tai epätosi
`<`        | Pienempi kuin      | ${age} < 25     | tosi tai epätosi
`<=`       | Pienempi tai yhtä suuri | ${age} <= 25  | tosi tai epätosi
{{< /table >}}

Yllä olevissa esimerkeissä ${age} edustaa nykyisen kentän arvoa, ja operaattoria käytetään vertaamaan sitä arvoon 25. Rajoite arvioidaan joko todeksi tai epätodeksi riippuen siitä, täyttyykö ehto vai ei.

### Loogiset operaattorit

Loogisia operaattoreita käytetään yhdistämään useita lausekkeita rajoitteissa. Tässä joitakin yleisesti käytettyjä loogisia operaattoreita sekä niiden toiminnot ja esimerkit:

Operaattori | Toiminta      | Esimerkki                                           
-------- | -------------- | --------------------------------------------------
`or`       | Palauttaa tosi, jos jompi kumpi lauseke on tosi | ${age} = 3 or ${age} = 4
`and`      | Palauttaa tosi vain jos molemmat lausekkeet ovat tosia | ${age} > 3 and ${age} < 5
`not()`    | Palauttaa tosi, jos lauseke ei ole tosi | not(${age} > 3 and ${age} < 5)

Yllä olevissa esimerkeissä ${age} edustaa nykyisen kentän arvoa, ja loogisia operaattoreita käytetään yhdistämään lausekkeita. Rajoite arvioidaan todeksi tai epätodeksi määriteltyjen ehtojen perusteella.

Esimerkki 1:
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` palauttaa `tosi`, jos ikä on joko 3 tai 4." />}}

Esimerkki 2:
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` palauttaa `tosi`, jos ikä on välillä 3 ja 5." />}}

Esimerkki 3:
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` palauttaa `tosi`, jos ikä ei ole välillä 3 ja 5." />}}
