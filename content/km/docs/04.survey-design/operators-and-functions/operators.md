---
title: "Operators"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 292
---

### Comparison operators

{{< table >}}
Operator | Operation      | Example              | Example Answer
-------- | -------------- | -------------------- | --------------
`=`        | ស្មើ          | ${age} = 25     | true ឬ false
`!=`       | មិន ស្មើ      | ${age} != 25    | true ឬ false
`>`        | ធំ ជ ាង         | ${age} > 25     | true ឬ false
`>=`       | ធំ ជ ា ង ឬ ស ្ ម ើ | ${age} >= 25 | true ឬ false
`<`        | តូ ច ជ ា ង      | ${age} < 25     | true ឬ false
`<=`       | តូ ច ជ ា ង ឬ ស ្ ម ើ | ${age} <= 25  | true ឬ false
{{< /table >}}

ក ្ ន ុ ង ឧ ទ ា ហ រ ណ ៍ ខ ា ង ល ើ, ${age} តំ ណ ា ង ឱ ្ យ value ន ៃ field current, ហ ើ យ operator ប ្ រ ើ ស ម ្ រ ា ប ់ compare ជ ា ម ួ យ value 25 ។

### Logical operators

Logical operators ប ្ រ ើ ដើ ម ្ ប ី combine expressions ច ្ រ ើ ន ។

Operator | Operation      | Example                                           
-------- | -------------- | --------------------------------------------------
`or`       | Return true ប ្ រ ស ិ ន ប ើ expression ណ ា ម ួ យ true     | ${age} = 3 or ${age} = 4
`and`      | Return true ត ែ ប ្ រ ស ិ ន ប ើ expressions ទ ា ំ ង ប ី true | ${age} > 3 and ${age} < 5
`not()`    | Return true ប ្ រ ស ិ ន ប ើ expression ម ិ ន true        | not(${age} > 3 and ${age} < 5)

ឧទាហរណ៍ ១:
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` ត ្ រ ឡ ប ់ `true` ប ្ រ ស ិ ន ប ើ age ជ ា 3 ឬ 4 ។" />}}

ឧទាហរណ៍ ២:
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` ត ្ រ ឡ ប ់ `true` ប ្ រ ស ិ ន ប ើ age ន ៅ ចន ្ ល ោ ះ 3 ហ ើ យ 5 ។" />}}

ឧទាហរណ៍ ៣:
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` ត ្ រ ឡ ប ់ `true` ប ្ រ ស ិ ន ប ើ age ន ៅ ក ្ រ ោ យ range ។" />}}
