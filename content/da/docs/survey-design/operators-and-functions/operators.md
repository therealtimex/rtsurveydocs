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

### Sammenligningsoperatorer

{{< table >}}
Operator | Operation      | Eksempel              | Eksempelsvar
-------- | -------------- | -------------------- | --------------
`=`        | Lig med          | ${age} = 25     | sand eller falsk
`!=`       | Ikke lig med      | ${age} != 25    | sand eller falsk
`>`        | Større end   | ${age} > 25     | sand eller falsk
`>=`       | Større end eller lig med | ${age} >= 25 | sand eller falsk
`<`        | Mindre end      | ${age} < 25     | sand eller falsk
`<=`       | Mindre end eller lig med | ${age} <= 25  | sand eller falsk
{{< /table >}}

I eksemplerne ovenfor repræsenterer ${age} det aktuelle felts værdi, og operatoren bruges til at sammenligne den med værdien 25. Betingelsen vil evalueres til enten sand eller falsk, afhængigt af om sammenligningen er opfyldt eller ej.

### Logiske operatorer

Logiske operatorer bruges til at kombinere flere udtryk i betingelser. Her er nogle almindeligt brugte logiske operatorer med deres operationer og eksempler:

Operator | Operation      | Eksempel                                           
-------- | -------------- | --------------------------------------------------
`or`       | Returnerer sand, hvis ét af udtrykkene er sandt          | ${age} = 3 or ${age} = 4
`and`      | Returnerer sand kun, hvis begge udtryk er sande    | ${age} > 3 and ${age} < 5
`not()`    | Returnerer sand, hvis udtrykket ikke er sandt        | not(${age} > 3 and ${age} < 5)

I eksemplerne ovenfor repræsenterer ${age} det aktuelle felts værdi, og de logiske operatorer bruges til at kombinere udtryk. Betingelsen evalueres til sand eller falsk baseret på de angivne betingelser.

Eksempel 1:
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` returnerer `sand`, hvis alderen er enten 3 eller 4." />}}

Eksempel 2:
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` returnerer `sand`, hvis alderen er mellem 3 og 5." />}}

Eksempel 3:
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` returnerer `sand`, hvis alderen ikke er mellem 3 og 5." />}}
