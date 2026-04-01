---
title: "Operadores"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 292
---

### Operadores de comparación

{{< table >}}
Operador | Operación      | Ejemplo              | Respuesta de ejemplo
-------- | -------------- | -------------------- | ---------------------
`=`        | Igual          | ${age} = 25     | verdadero o falso
`!=`       | No igual       | ${age} != 25    | verdadero o falso
`>`        | Mayor que      | ${age} > 25     | verdadero o falso
`>=`       | Mayor o igual que | ${age} >= 25 | verdadero o falso
`<`        | Menor que      | ${age} < 25     | verdadero o falso
`<=`       | Menor o igual que | ${age} <= 25  | verdadero o falso
{{< /table >}}

En los ejemplos anteriores, ${age} representa el valor del campo actual, y el operador se usa para compararlo con el valor 25. La restricción se evaluará como verdadera o falsa, dependiendo de si la comparación se satisface o no.

### Operadores lógicos

Los operadores lógicos se utilizan para combinar múltiples expresiones en restricciones. Aquí hay algunos operadores lógicos de uso común junto con sus operaciones y ejemplos:

Operador | Operación      | Ejemplo
-------- | -------------- | -------
`or`       | Devuelve verdadero si cualquiera de las expresiones es verdadera | ${age} = 3 or ${age} = 4
`and`      | Devuelve verdadero solo si ambas expresiones son verdaderas    | ${age} > 3 and ${age} < 5
`not()`    | Devuelve verdadero si la expresión no es verdadera        | not(${age} > 3 and ${age} < 5)

En los ejemplos anteriores, ${age} representa el valor del campo actual, y los operadores lógicos se usan para combinar expresiones. La restricción se evaluará como verdadera o falsa según las condiciones especificadas.

Ejemplo 1:
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` devolverá `true` si la edad es 3 o 4." />}}

Ejemplo 2:
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` devolverá `true` si la edad está entre 3 y 5." />}}

Ejemplo 3:
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` devolverá `true` si la edad no está entre 3 y 5." />}}
