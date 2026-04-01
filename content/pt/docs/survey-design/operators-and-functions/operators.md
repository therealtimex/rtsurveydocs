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

### Operadores de comparação

{{< table >}}
Operador | Operação      | Exemplo              | Resposta de Exemplo
-------- | -------------- | -------------------- | --------------
`=`        | Igual          | ${age} = 25     | verdadeiro ou falso
`!=`       | Diferente      | ${age} != 25    | verdadeiro ou falso
`>`        | Maior que   | ${age} > 25     | verdadeiro ou falso
`>=`       | Maior ou igual | ${age} >= 25 | verdadeiro ou falso
`<`        | Menor que      | ${age} < 25     | verdadeiro ou falso
`<=`       | Menor ou igual | ${age} <= 25  | verdadeiro ou falso
{{< /table >}}

Nos exemplos acima, ${age} representa o valor do campo atual, e o operador é usado para compará-lo com o valor 25. A restrição será avaliada como verdadeira ou falsa, dependendo de a comparação ser satisfeita ou não.

### Operadores lógicos

Os operadores lógicos são usados para combinar múltiplas expressões em restrições. Aqui estão alguns operadores lógicos frequentemente usados juntamente com as suas operações e exemplos:

Operador | Operação      | Exemplo                                           
-------- | -------------- | --------------------------------------------------
`or`       | Retorna verdadeiro se qualquer expressão for verdadeira          | ${age} = 3 or ${age} = 4
`and`      | Retorna verdadeiro apenas se ambas as expressões forem verdadeiras    | ${age} > 3 and ${age} < 5
`not()`    | Retorna verdadeiro se a expressão não for verdadeira        | not(${age} > 3 and ${age} < 5)

Nos exemplos acima, ${age} representa o valor do campo atual, e os operadores lógicos são usados para combinar expressões. A restrição será avaliada como verdadeira ou falsa com base nas condições especificadas.

Exemplo 1:
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` retornará `true` se a idade for 3 ou 4." />}}

Exemplo 2:
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` retornará `true` se a idade estiver entre 3 e 5." />}}

Exemplo 3:
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` retornará `true` se a idade não estiver entre 3 e 5." />}}
