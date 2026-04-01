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
Operator | Operasjon      | Eksempel              | Eksempelsvar
-------- | -------------- | -------------------- | --------------
`=`        | Lik          | ${age} = 25     | sant eller usant
`!=`       | Ikke lik      | ${age} != 25    | sant eller usant
`>`        | Større enn   | ${age} > 25     | sant eller usant
`>=`       | Større enn eller lik | ${age} >= 25 | sant eller usant
`<`        | Mindre enn      | ${age} < 25     | sant eller usant
`<=`       | Mindre enn eller lik | ${age} <= 25  | sant eller usant
{{< /table >}}

I eksemplene ovenfor representerer ${age} gjeldende felts verdi, og operatoren brukes til å sammenligne den med verdien 25. Begrensningen vil evaluere til enten sant eller usant, avhengig av om sammenligningen er oppfylt eller ikke.

### Logiske operatorer

Logiske operatorer brukes til å kombinere flere uttrykk i begrensninger. Her er noen vanlig brukte logiske operatorer sammen med deres operasjoner og eksempler:

Operator | Operasjon      | Eksempel                                           
-------- | -------------- | --------------------------------------------------
`or`       | Returnerer sant hvis ett av uttrykkene er sant          | ${age} = 3 or ${age} = 4
`and`      | Returnerer sant bare hvis begge uttrykkene er sanne    | ${age} > 3 and ${age} < 5
`not()`    | Returnerer sant hvis uttrykket ikke er sant        | not(${age} > 3 and ${age} < 5)

I eksemplene ovenfor representerer ${age} gjeldende felts verdi, og de logiske operatorene brukes til å kombinere uttrykk. Begrensningen vil evaluere til sant eller usant basert på betingelsene som er angitt.

Eksempel 1:
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` returnerer `sant` hvis alderen er enten 3 eller 4." />}}

Eksempel 2:
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` returnerer `sant` hvis alderen er mellom 3 og 5." />}}

Eksempel 3:
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` returnerer `sant` hvis alderen ikke er mellom 3 og 5." />}}
