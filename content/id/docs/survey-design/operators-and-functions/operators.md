---
title: "Operator"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 292
---

### Operator perbandingan

{{< table >}}
Operator | Operasi      | Contoh              | Jawaban Contoh
-------- | -------------- | -------------------- | --------------
`=`        | Sama dengan          | ${age} = 25     | true atau false
`!=`       | Tidak sama dengan      | ${age} != 25    | true atau false
`>`        | Lebih besar dari   | ${age} > 25     | true atau false
`>=`       | Lebih besar dari atau sama dengan | ${age} >= 25 | true atau false
`<`        | Lebih kecil dari      | ${age} < 25     | true atau false
`<=`       | Lebih kecil dari atau sama dengan | ${age} <= 25  | true atau false
{{< /table >}}

Dalam contoh di atas, ${age} mewakili nilai bidang saat ini, dan operator digunakan untuk membandingkannya dengan nilai 25. Batasan akan dievaluasi menjadi true atau false, tergantung pada apakah perbandingan terpenuhi atau tidak.

### Operator logika

Operator logika digunakan untuk menggabungkan beberapa ekspresi dalam batasan. Berikut adalah beberapa operator logika yang umum digunakan beserta operasi dan contohnya:

Operator | Operasi      | Contoh                                           
-------- | -------------- | --------------------------------------------------
`or`       | Mengembalikan true jika salah satu ekspresi benar          | ${age} = 3 or ${age} = 4
`and`      | Mengembalikan true hanya jika kedua ekspresi benar    | ${age} > 3 and ${age} < 5
`not()`    | Mengembalikan true jika ekspresi tidak benar        | not(${age} > 3 and ${age} < 5)

Dalam contoh di atas, ${age} mewakili nilai bidang saat ini, dan operator logika digunakan untuk menggabungkan ekspresi. Batasan akan dievaluasi menjadi true atau false berdasarkan kondisi yang ditentukan.

Contoh 1:
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` akan mengembalikan `true` jika usia adalah 3 atau 4." />}}

Contoh 2:
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` akan mengembalikan `true` jika usia antara 3 dan 5." />}}

Contoh 3:
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` akan mengembalikan `true` jika usia tidak antara 3 dan 5." />}}
