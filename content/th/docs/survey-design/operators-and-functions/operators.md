---
title: "ตัวดำเนินการ"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 292
---

### ตัวดำเนินการเปรียบเทียบ

{{< table >}}
Operator | Operation      | Example              | Example Answer
-------- | -------------- | -------------------- | --------------
`=`        | Equal          | ${age} = 25     | true or false
`!=`       | Not equal      | ${age} != 25    | true or false
`>`        | Greater-than   | ${age} > 25     | true or false
`>=`       | Greater-than or equal | ${age} >= 25 | true or false
`<`        | Less-than      | ${age} < 25     | true or false
`<=`       | Less-than or equal | ${age} <= 25  | true or false
{{< /table >}}

ในตัวอย่างข้างต้น ${age} แทนค่าของฟิลด์ปัจจุบัน และตัวดำเนินการใช้เปรียบเทียบกับค่า 25 constraint จะประเมินเป็น true หรือ false ขึ้นอยู่กับว่าการเปรียบเทียบตรงตามเงื่อนไขหรือไม่

### ตัวดำเนินการเชิงตรรกะ

ตัวดำเนินการเชิงตรรกะใช้รวมนิพจน์หลายอันใน constraints:

Operator | Operation      | Example                                           
-------- | -------------- | --------------------------------------------------
`or`       | ส่งคืน true ถ้านิพจน์ใดนิพจน์หนึ่งเป็น true | ${age} = 3 or ${age} = 4
`and`      | ส่งคืน true เฉพาะเมื่อทั้งสองนิพจน์เป็น true | ${age} > 3 and ${age} < 5
`not()`    | ส่งคืน true ถ้านิพจน์ไม่เป็น true | not(${age} > 3 and ${age} < 5)

ตัวอย่าง 1:
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` จะส่งคืน `true` ถ้าอายุเป็น 3 หรือ 4" />}}

ตัวอย่าง 2:
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` จะส่งคืน `true` ถ้าอายุอยู่ระหว่าง 3 ถึง 5" />}}

ตัวอย่าง 3:
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` จะส่งคืน `true` ถ้าอายุไม่ได้อยู่ระหว่าง 3 ถึง 5" />}}