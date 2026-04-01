---
title: "Classificação"
description: "As perguntas de classificação permitem que os respondentes ordenem um conjunto de opções por preferência ou prioridade."
icon: "list-ol"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 242
---

O tipo de pergunta `rank` apresenta uma lista de opções que o respondente deve **arrastar para ordenar** (ou de outra forma classificar do primeiro ao último). Ele armazena o resultado como uma lista separada por espaço de valores de opções na ordem selecionada, com a opção de maior prioridade primeiro.

## Especificação básica do XLSForm

| type | name | label |
|------|------|-------|
| rank priorities | main_priority | Classifique estas necessidades da comunidade da mais para a menos importante |

As opções são definidas na planilha **choices** assim como `select_one`:

**survey:**

| type | name | label |
|------|------|-------|
| rank priorities | main_priority | Classifique estas necessidades da mais para a menos importante |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| priorities | water | Água limpa |
| priorities | health | Saúde |
| priorities | education | Educação |
| priorities | roads | Estradas |
| priorities | electricity | Eletricidade |

## Formato do valor armazenado

O valor armazenado é uma **lista separada por espaço** de valores de opções em ordem de classificação (primeiro = maior prioridade):

```
water education health roads electricity
```

## Extraindo posições classificadas

Use `selected-at()` para obter a opção em uma classificação específica:

| type | name | label | calculation |
|------|------|-------|-------------|
| rank priorities | main_priority | Classificar necessidades da comunidade | |
| calculate | top_priority | | selected-at(${main_priority}, 0) |
| calculate | second_priority | | selected-at(${main_priority}, 1) |

`selected-at(${main_priority}, 0)` retorna o valor colocado **primeiro** (índice 0 = classificação mais alta).

## Usando `rank-index()` com grupos de repetição

Quando `rank` é usado dentro de um grupo de repetição, `rank-index()` permite referenciar a classificação ordinal de fora da repetição:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | first_ranked | | rank-index(1, ${score}) |

Consulte [Funções — Funções de campo repetido](../operators-and-functions/functions#repeated-field-functions) para detalhes completos sobre `rank-index()` e `rank-index-if()`.

## Usos

As perguntas de classificação são comumente usadas para:

1. **Classificação de prioridades** — pedir às comunidades que classifiquem necessidades de desenvolvimento
2. **Ordenação de preferências** — classificar recursos de produtos, atributos de serviço ou opções de política
3. **Ordenação de itens de exame** — organizar etapas em um processo
4. **Seleção dos N principais** — combinado com `selected-at()` para extrair apenas as 1, 2 ou 3 principais opções

## Práticas recomendadas

1. Mantenha a lista curta (3 a 7 itens) — classificar torna-se cognitivamente exigente além de 7 a 8 opções.
2. Use rótulos de opção claros e mutuamente exclusivos para evitar confusão sobre o que "primeiro" significa.
3. Adicione texto de dica explicando a direção da classificação (por exemplo, "Arraste para ordenar: primeiro = mais importante").
4. Valide usando `count-selected(.) = x` se você precisa garantir que todas as opções estejam classificadas.

## Limitações

- O widget de arrastar para classificar requer uma tela de toque ou mouse — pode não funcionar bem em ambientes apenas com teclado.
- Em alguns clientes móveis mais antigos, o widget de classificação pode voltar para uma interface de entrada numerada.
- Você não pode classificar parcialmente (ou seja, classificar apenas algumas opções) — todas as opções devem ser ordenadas.
