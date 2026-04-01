---
title: "Operatorët"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 292
---

### Operatorët e krahasimit

{{< table >}}
Operatori | Operacioni      | Shembulli              | Përgjigja e Shembullit
-------- | -------------- | -------------------- | --------------
`=`        | E barabartë          | ${age} = 25     | e vërtetë ose e rreme
`!=`       | Jo e barabartë      | ${age} != 25    | e vërtetë ose e rreme
`>`        | Më e madhe se   | ${age} > 25     | e vërtetë ose e rreme
`>=`       | Më e madhe ose e barabartë | ${age} >= 25 | e vërtetë ose e rreme
`<`        | Më e vogël se      | ${age} < 25     | e vërtetë ose e rreme
`<=`       | Më e vogël ose e barabartë | ${age} <= 25  | e vërtetë ose e rreme
{{< /table >}}

Në shembujt e mësipërm, ${age} përfaqëson vlerën e fushës aktuale, dhe operatori përdoret për të krahasuar me vlerën 25. Kufizimi do të vlerësohet si i vërtetë ose i rremë, varësisht nga nëse krahasimi plotësohet ose jo.

### Operatorët logjikë

Operatorët logjikë përdoren për të kombinuar shprehje të shumëfishta në kufizime. Ja disa operatorë logjikë të përdorur zakonisht bashkë me operacionet dhe shembujt e tyre:

Operatori | Operacioni      | Shembulli                                           
-------- | -------------- | --------------------------------------------------
`or`       | Kthen të vërtetën nëse njëra shprehje është e vërtetë | ${age} = 3 or ${age} = 4
`and`      | Kthen të vërtetën vetëm nëse të dyja shprehjet janë të vërteta | ${age} > 3 and ${age} < 5
`not()`    | Kthen të vërtetën nëse shprehja nuk është e vërtetë | not(${age} > 3 and ${age} < 5)

Në shembujt e mësipërm, ${age} përfaqëson vlerën e fushës aktuale, dhe operatorët logjikë përdoren për të kombinuar shprehjet. Kufizimi do të vlerësohet si i vërtetë ose i rremë bazuar në kushtet e specifikuara.

Shembulli 1:
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` do të kthejë `e vërtetë` nëse mosha është ose 3 ose 4." />}}

Shembulli 2:
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` do të kthejë `e vërtetë` nëse mosha është midis 3 dhe 5." />}}

Shembulli 3:
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` do të kthejë `e vërtetë` nëse mosha nuk është midis 3 dhe 5." />}}
