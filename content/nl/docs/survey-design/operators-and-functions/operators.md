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

### Vergelijkingsoperatoren

{{< table >}}
Operator | Bewerking      | Voorbeeld            | Voorbeeldantwoord
-------- | -------------- | -------------------- | -----------------
`=`        | Gelijk aan     | ${age} = 25     | true of false
`!=`       | Niet gelijk aan| ${age} != 25    | true of false
`>`        | Groter dan     | ${age} > 25     | true of false
`>=`       | Groter dan of gelijk aan | ${age} >= 25 | true of false
`<`        | Kleiner dan    | ${age} < 25     | true of false
`<=`       | Kleiner dan of gelijk aan | ${age} <= 25  | true of false
{{< /table >}}

In de bovenstaande voorbeelden vertegenwoordigt ${age} de waarde van het huidige veld, en wordt de operator gebruikt om deze te vergelijken met de waarde 25. De beperking evalueert tot true of false, afhankelijk van of de vergelijking voldaan is.

### Logische operatoren

Logische operatoren worden gebruikt om meerdere expressies in beperkingen te combineren. Hier zijn enkele veelgebruikte logische operatoren met hun bewerkingen en voorbeelden:

Operator | Bewerking      | Voorbeeld
-------- | -------------- | ---------
`or`       | Geeft true terug als een van de expressies waar is | ${age} = 3 or ${age} = 4
`and`      | Geeft true terug alleen als beide expressies waar zijn | ${age} > 3 and ${age} < 5
`not()`    | Geeft true terug als de expressie niet waar is | not(${age} > 3 and ${age} < 5)

In de bovenstaande voorbeelden vertegenwoordigt ${age} de waarde van het huidige veld, en worden de logische operatoren gebruikt om expressies te combineren. De beperking evalueert tot true of false op basis van de opgegeven voorwaarden.

Voorbeeld 1:
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` geeft `true` terug als de leeftijd 3 of 4 is." />}}

Voorbeeld 2:
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` geeft `true` terug als de leeftijd tussen 3 en 5 ligt." />}}

Voorbeeld 3:
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` geeft `true` terug als de leeftijd niet tussen 3 en 5 ligt." />}}
