---
title: "Operadores e Funções"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 290
---

As expressões no rtSurvey são escritas num subconjunto de **XPath 1.0**, alargado com funções JavaRosa/ODK e funções rtSurvey personalizadas. Usa expressões nas colunas `calculate`, `constraint`, `relevant`, `required` e `default` do seu XLSForm.

## Referenciar valores de campo

Use `${fieldname}` para referenciar o valor de outro campo:

```
${age} > 18
```

Use `.` (um único ponto) para referenciar o **valor do campo atual** — frequentemente usado em expressões `constraint`:

```
. >= 0 and . <= 100
```

Use `..` para referenciar o grupo pai (uso avançado em repetições).

## Sintaxe de expressão

As expressões seguem as regras XPath padrão:

- **Cadeias de caracteres** devem ser colocadas entre aspas simples: `'yes'`
- **Números** são escritos como estão: `42`, `3.14`
- Resultados **booleanos** são usados para `relevant`, `required` e `constraint` — qualquer valor não vazio e não zero é verdadeiro
- O espaço em branco é ignorado em torno dos operadores

{{% alert icon=" " context="warning" %}}
Use sempre aspas simples direitas (`'` ou `"`) — nunca "aspas inteligentes" (aspas curvas). Os editores de texto enriquecido frequentemente convertem aspas automaticamente e quebrarão as suas expressões.
{{% /alert %}}

## Secções neste capítulo

- **[Operadores](operators)** — operadores de comparação (`=`, `!=`, `>`, `<`, `>=`, `<=`) e operadores lógicos (`and`, `or`, `not()`)
- **[Funções](functions)** — funções de cadeia de caracteres, seleção, número, data/hora, booleano, geo e utilitário
- **[Referências](references)** — como referenciar campos e valores de contexto

## Exemplos rápidos

| Caso de uso | Expressão |
|----------|------------|
| Mostrar se a idade for superior a 18 | `${age} > 18` |
| Mostrar apenas se "yes" foi selecionado | `${consent} = 'yes'` |
| Obrigatório se outro campo não estiver vazio | `${name} != ''` |
| Calcular total | `${adults} + ${children}` |
| Concatenar nome | `concat(${first_name}, ' ', ${last_name})` |
| Data de hoje | `today()` |
| Verificar se opção foi selecionada | `selected(${interests}, 'sports')` |
