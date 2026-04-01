---
title: "Operatoriai"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 292
---

### Palyginimo operatoriai

{{< table >}}
Operatorius | Operacija      | Pavyzdys              | Atsakymo pavyzdys
-------- | -------------- | -------------------- | --------------
`=`        | Lygus          | ${age} = 25     | tiesa arba melas
`!=`       | Nelygus        | ${age} != 25    | tiesa arba melas
`>`        | Didesnis nei   | ${age} > 25     | tiesa arba melas
`>=`       | Didesnis arba lygus | ${age} >= 25 | tiesa arba melas
`<`        | Mažesnis nei   | ${age} < 25     | tiesa arba melas
`<=`       | Mažesnis arba lygus | ${age} <= 25  | tiesa arba melas
{{< /table >}}

Aukščiau pateiktuose pavyzdžiuose ${age} atspindi dabartinio lauko reikšmę, o operatorius naudojamas jai lyginti su reikšme 25. Apribojimas bus įvertintas kaip tiesa arba melas, priklausomai nuo to, ar palyginimas patenkinamas.

### Loginiai operatoriai

Loginiai operatoriai naudojami kelioms išraiškoms apribojimuose sujungti. Čia pateikiami kai kurie dažniausiai naudojami loginiai operatoriai su jų operacijomis ir pavyzdžiais:

Operatorius | Operacija      | Pavyzdys                                           
-------- | -------------- | --------------------------------------------------
`or`       | Grąžina tiesa, jei kuri nors išraiška yra teisinga | ${age} = 3 or ${age} = 4
`and`      | Grąžina tiesa tik jei abi išraiškos yra teisingos | ${age} > 3 and ${age} < 5
`not()`    | Grąžina tiesa, jei išraiška nėra teisinga | not(${age} > 3 and ${age} < 5)

Aukščiau pateiktuose pavyzdžiuose ${age} atspindi dabartinio lauko reikšmę, o loginiai operatoriai naudojami išraiškoms sujungti. Apribojimas bus įvertintas kaip tiesa arba melas pagal nurodytas sąlygas.

1 pavyzdys:
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` grąžins `tiesa`, jei amžius yra 3 arba 4." />}}

2 pavyzdys:
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` grąžins `tiesa`, jei amžius yra nuo 3 iki 5." />}}

3 pavyzdys:
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` grąžins `tiesa`, jei amžius nėra nuo 3 iki 5." />}}
