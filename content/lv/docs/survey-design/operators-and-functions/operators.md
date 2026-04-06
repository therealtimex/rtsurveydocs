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

### Salīdzināšanas operatori

{{< table >}}
Operators | Darbība      | Piemērs              | Piemēra atbilde
-------- | -------------- | -------------------- | --------------
`=`        | Vienāds          | ${age} = 25     | true vai false
`!=`       | Nav vienāds      | ${age} != 25    | true vai false
`>`        | Lielāks par   | ${age} > 25     | true vai false
`>=`       | Lielāks par vai vienāds | ${age} >= 25 | true vai false
`<`        | Mazāks par      | ${age} < 25     | true vai false
`<=`       | Mazāks par vai vienāds | ${age} <= 25  | true vai false
{{< /table >}}

Augstāk minētajos piemēros ${age} apzīmē pašreizējā lauka vērtību, un operators tiek izmantots, lai salīdzinātu to ar vērtību 25. Ierobežojums tiks novērtēts kā true vai false atkarībā no tā, vai salīdzinājums ir izpildīts.

### Loģiskie operatori

Loģiskie operatori tiek izmantoti, lai apvienotu vairākas izteiksmes ierobežojumos. Lūk, daži biežāk izmantotie loģiskie operatori ar to darbībām un piemēriem:

Operators | Darbība      | Piemērs                                           
-------- | -------------- | --------------------------------------------------
`or`       | Atgriež true, ja kāda izteiksme ir patiesa          | ${age} = 3 or ${age} = 4
`and`      | Atgriež true tikai tad, ja abas izteiksmes ir patiesas    | ${age} > 3 and ${age} < 5
`not()`    | Atgriež true, ja izteiksme nav patiesa        | not(${age} > 3 and ${age} < 5)

Augstāk minētajos piemēros ${age} apzīmē pašreizējā lauka vērtību, un loģiskie operatori tiek izmantoti, lai apvienotu izteiksmes. Ierobežojums tiks novērtēts kā true vai false, pamatojoties uz norādītajiem nosacījumiem.

1. piemērs:
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` atgriezīs `true`, ja vecums ir 3 vai 4." />}}

2. piemērs:
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` atgriezīs `true`, ja vecums ir starp 3 un 5." />}}

3. piemērs:
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` atgriezīs `true`, ja vecums nav starp 3 un 5." />}}
