---
title: "Operatörler"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 292
---

### Karşılaştırma operatörleri

{{< table >}}
Operatör | İşlem      | Örnek              | Örnek Cevap
-------- | -------------- | -------------------- | --------------
`=`        | Eşit          | ${age} = 25     | doğru veya yanlış
`!=`       | Eşit değil      | ${age} != 25    | doğru veya yanlış
`>`        | Büyüktür   | ${age} > 25     | doğru veya yanlış
`>=`       | Büyük eşittir | ${age} >= 25 | doğru veya yanlış
`<`        | Küçüktür      | ${age} < 25     | doğru veya yanlış
`<=`       | Küçük eşittir | ${age} <= 25  | doğru veya yanlış
{{< /table >}}

Yukarıdaki örneklerde ${age} geçerli alanın değerini temsil eder ve operatör bunu 25 değeriyle karşılaştırmak için kullanılır. Kısıtlama, karşılaştırmanın sağlanıp sağlanmadığına bağlı olarak doğru veya yanlış olarak değerlendirilecektir.

### Mantıksal operatörler

Mantıksal operatörler, kısıtlamalardaki birden fazla ifadeyi birleştirmek için kullanılır. İşte bazı yaygın olarak kullanılan mantıksal operatörler ve işlemleri ve örnekleri:

Operatör | İşlem      | Örnek                                           
-------- | -------------- | --------------------------------------------------
`or`       | İfadelerden herhangi biri doğruysa doğru döndürür          | ${age} = 3 or ${age} = 4
`and`      | Her iki ifade de doğruysa doğru döndürür    | ${age} > 3 and ${age} < 5
`not()`    | İfade doğru değilse doğru döndürür        | not(${age} > 3 and ${age} < 5)

Yukarıdaki örneklerde ${age} geçerli alanın değerini temsil eder ve mantıksal operatörler ifadeleri birleştirmek için kullanılır. Kısıtlama, belirtilen koşullara göre doğru veya yanlış olarak değerlendirilecektir.

Örnek 1:
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` yaş 3 veya 4 ise `true` döndürür." />}}

Örnek 2:
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` yaş 3 ile 5 arasındaysa `true` döndürür." />}}

Örnek 3:
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` yaş 3 ile 5 arasında değilse `true` döndürür." />}}
