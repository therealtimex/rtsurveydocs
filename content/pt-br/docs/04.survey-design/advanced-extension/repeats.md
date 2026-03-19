---
title: "Repetições avançadas"
description: "Padrões avançados para grupos de repetição: contagens dinâmicas, repetições aninhadas, resumo de dados de repetição e referenciação de valores entre repetições."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 295
---

Esta página cobre padrões avançados para trabalhar com grupos de repetição no rtSurvey. Para os conceitos básicos de configuração de um grupo de repetição, consulte [Agrupando e repetindo](../repeats).

---

## Contagem dinâmica de repetições

Por padrão, o entrevistador decide quantas vezes repetir. Você pode fixar o número de repetições usando `repeat_count`:

| type | name | label | repeat_count |
|------|------|-------|--------------|
| begin_repeat | household_members | Membro do domicílio | `${num_members}` |
| text | member_name | Nome do membro | |
| integer | member_age | Idade | |
| end_repeat | | | |

A repetição é executada exatamente `${num_members}` vezes, onde `num_members` foi coletado anteriormente no formulário. O entrevistador não pode adicionar ou remover instâncias.

---

## Acesso indexado: `indexed-repeat()`

Acesse o valor de campo de uma instância de repetição específica de **fora** do grupo de repetição usando `indexed-repeat(repeatedField, repeatGroup, index)`:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | first_name | | `indexed-repeat(${member_name}, ${household_members}, 1)` |
| calculate | second_name | | `indexed-repeat(${member_name}, ${household_members}, 2)` |

Isso é útil para construir campos de resumo ou referenciar os dados do membro "principal" após a repetição.

---

## Posição atual da instância: `index()`

Dentro de um grupo de repetição, `index()` retorna a posição (base 1) da instância atual. Use-o para rotular cada repetição ou criar identificadores únicos:

| type | name | label |
|------|------|-------|
| begin_repeat | plots | Lote |
| note | plot_label | Lote número ${index()} |
| text | plot_id | ID do lote |
| end_repeat | | |

---

## Referenciando campos na mesma instância

Dentro de uma repetição, use `${fieldname}` para referenciar outro campo **na mesma instância de repetição**. Não é necessário usar `indexed-repeat()` dentro do mesmo loop:

| type | name | label | relevant |
|------|------|-------|----------|
| begin_repeat | members | Membro | |
| text | member_name | Nome | |
| integer | member_age | Idade | |
| text | school_name | Nome da escola | `${member_age} < 18` |
| end_repeat | | | |

---

## Referenciando campos pai de dentro de uma repetição

Os campos fora (acima) do grupo de repetição podem ser referenciados normalmente com `${fieldname}`:

| type | name | label |
|------|------|-------|
| text | village | Nome da aldeia |
| begin_repeat | plots | Lote agrícola |
| note | plot_context | Lotes em ${village} |
| end_repeat | | |

---

## Resumindo dados de repetição

Use funções de agregação de repetição **fora** do grupo de repetição para resumir:

| Função | Exemplo | Descrição |
|--------|---------|-----------|
| `count(group)` | `count(${household_members})` | Número de instâncias |
| `sum(field)` | `sum(${loan_amount})` | Soma de um campo numérico |
| `min(field)` | `min(${member_age})` | Valor mínimo |
| `max(field)` | `max(${member_age})` | Valor máximo |
| `join(sep, field)` | `join(', ', ${member_name})` | Lista separada por vírgulas |
| `count-if(group, expr)` | `count-if(${members}, ${member_age} < 18)` | Contagem condicional |
| `sum-if(field, expr)` | `sum-if(${loan_amount}, ${loan_amount} > 500)` | Soma condicional |
| `join-if(sep, field, expr)` | `join-if(', ', ${name}, ${age} >= 18)` | Junção condicional |

### Exemplo: Resumo do domicílio

| type | name | label | calculation |
|------|------|-------|-------------|
| integer | num_members | Quantos membros? | |
| begin_repeat | members | Membro | `${num_members}` |
| text | member_name | Nome | |
| integer | member_age | Idade | |
| end_repeat | | | |
| calculate | total_members | | `count(${members})` |
| calculate | children_count | | `count-if(${members}, ${member_age} < 18)` |
| calculate | adult_names | | `join-if(', ', ${member_name}, ${member_age} >= 18)` |
| note | summary | ${total_members} membros; ${children_count} com menos de 18. Adultos: ${adult_names} | |

---

## Repetições aninhadas

Um grupo de repetição pode conter outro grupo de repetição. Use isso com cuidado — repetições aninhadas adicionam complexidade e podem ser confusas para os entrevistadores.

| type | name | label |
|------|------|-------|
| begin_repeat | households | Domicílio |
| text | hh_id | ID do domicílio |
| begin_repeat | hh_members | Membro |
| text | member_name | Nome do membro |
| end_repeat | | |
| end_repeat | | |

Para referenciar um campo em uma repetição externa a partir da repetição interna, use `${fieldname}` — ele resolve para o ancestral correspondente mais próximo:

Dentro da repetição `hh_members`, `${hh_id}` retorna o ID do domicílio **atual**, não de todos os domicílios.

---

## Classificação dentro de grupos de repetição: `rank-index()`

Quando um campo `rank` existe dentro de uma repetição, use `rank-index(instanceNumber, repeatedField)` de fora para obter a classificação ordinal de uma instância específica:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | top_scorer | | `rank-index(1, ${score})` |

`rank-index(1, ${score})` retorna o índice de instância da pontuação mais alta.

---

## Práticas recomendadas

1. Sempre use `repeat_count` quando o número de repetições for conhecido antecipadamente — isso evita que os entrevistadores adicionem ou removam instâncias acidentalmente.
2. Mantenha os grupos de repetição focados — uma repetição com mais de 20 perguntas por instância é difícil de navegar.
3. Nomeie os grupos de repetição claramente (por exemplo, `household_members`, não `repeat1`) — o nome aparece nas chamadas de função e nos dados exportados.
4. Teste com o número máximo esperado de instâncias para verificar o desempenho.
5. Use a aparência `field-list` no grupo de repetição para mostrar todos os campos em uma tela por instância (mobile).

---

## Limitações

- `indexed-repeat()` requer um índice válido (de 1 ao número de instâncias) — índices fora do intervalo retornam vazio.
- Repetições aninhadas além de 2 níveis não são recomendadas e podem causar problemas de exibição em alguns clientes.
- Funções de agregação (`sum`, `count`, etc.) operam em todo o grupo de repetição — você não pode agregar um subconjunto de instâncias sem variantes `*-if`.
