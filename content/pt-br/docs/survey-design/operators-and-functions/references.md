---
title: "Referenciando valores"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 291
---

A sintaxe `${fieldname}` é usada para se referir ao valor atual de um campo diferente no seu formulário. Ela pode representar o valor inserido, selecionado ou calculado, e será exibida exatamente como aparece nos dados enviados.

Exemplo:
Se você tiver um campo chamado "age" e quiser recuperar o valor exato inserido nesse campo, pode usar `${age}`.

Quando se trata de restrições, o símbolo "." é usado para se referir à entrada ou seleção proposta pelo usuário para o campo atual. Ele permite aplicar condições ou limites com base no valor que o usuário está inserindo ou selecionando naquele momento.

Exemplo:
Se você quiser verificar se o valor proposto para o campo atual é menor que 3, pode usar a restrição `. < 3`.

---

## `..` — Referência ao grupo pai

Dentro de um grupo ou grupo de repetição, `..` se refere ao **contexto pai**. Isso raramente é necessário na prática, mas é usado em expressões XPath avançadas para navegar pela hierarquia do formulário.

---

## Onde as referências são usadas

| Coluna | Tipo de referência | Exemplo |
|--------|-------------------|---------|
| `relevant` | `${fieldname}` | `${consent} = 'yes'` |
| `constraint` | `.` para o campo atual, `${fieldname}` para outros | `. > 0 and . <= ${max_value}` |
| `calculation` | `${fieldname}` | `${adults} + ${children}` |
| `required` | `${fieldname}` | `${has_income} = 'yes'` |
| `default` | `${fieldname}` | `${previous_answer}` |
| `label` | `${fieldname}` no texto | `"Sua idade é ${age} anos"` |
| `choice_filter` | Nome da coluna (sem `${}`) | `district = ${district}` |

{{% alert icon=" " context="warning" %}}
Na coluna `choice_filter`, referencie **nomes de colunas de escolha** diretamente (sem `${}`), e referencie **campos do formulário** com `${}`. Misturar esses é uma fonte comum de erros.
{{% /alert %}}

---

## Referenciando valores dentro de grupos de repetição

Dentro de uma repetição, `${fieldname}` se refere ao campo na **mesma instância** da repetição:

```
relevant: ${member_age} < 18
```

Isso usa o valor de `member_age` para a instância de repetição atual, não todas as instâncias.

Para referenciar um campo em uma instância de repetição **específica** de fora da repetição, use `indexed-repeat()`:

```
indexed-repeat(${member_name}, ${household_members}, 1)
```

Veja [Funções — Funções de campo repetido](functions#repeated-field-functions) para detalhes completos.

---

## Verificações de valor vazio

Teste se um campo foi respondido:

```
${fieldname} != ''       (campo não está vazio)
${fieldname} = ''        (campo está vazio)
```

Para números, também verifique:
```
${age} > 0               (age tem um valor positivo — implicitamente não vazio em contexto numérico)
```

---

## Coerção de tipo em referências

Quando você usa `${fieldname}` em um contexto numérico (por exemplo, `${age} + 1`), o rtSurvey automaticamente converte o valor string para um número. Um campo vazio é convertido para `0` ou `NaN` dependendo da operação — use `coalesce(${field}, 0)` para definir com segurança um campo numérico vazio como zero.
