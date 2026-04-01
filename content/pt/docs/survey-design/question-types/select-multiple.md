---
title: "Select_multiple"
description: "As perguntas Select_multiple permitem aos respondentes escolher uma ou mais opções de uma lista predefinida."
icon: "check_box"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 225
---

O tipo de pergunta `select_multiple` exibe uma lista onde o respondente pode selecionar **uma ou mais opções**. Por predefinição as escolhas são renderizadas como caixas de verificação. O valor armazenado é uma **lista separada por espaços** de todos os valores de escolha selecionados.

## Especificação XLSForm Básica

**folha de trabalho survey:**

| type | name | label |
|------|------|-------|
| select_multiple crops | crops_grown | Que culturas o agregado familiar cultiva? |

**folha de trabalho choices:**

| list_name | name | label |
|-----------|------|-------|
| crops | maize | Milho |
| crops | beans | Feijão |
| crops | rice | Arroz |
| crops | vegetables | Legumes |
| crops | other | Outro |

Para mais detalhes consulte a [especificação XLSForm](https://xlsform.org/en/#question-types).

## Formato de dados armazenados

A coluna exportada contém uma lista separada por espaços de valores selecionados:

```
maize beans vegetables
```

Use a função `selected()` — não `=` — ao testar valores de select_multiple em expressões (veja abaixo).

## Utilizações

As perguntas select_multiple são usadas para:

1. Recolher múltiplas respostas aplicáveis (por ex., fontes de rendimento, culturas cultivadas, sintomas)
2. Itens de concordância em estilo de caixa de verificação (por ex., "Selecione todos que se aplicam")
3. Inventários de idiomas ou competências
4. Qualquer pergunta onde múltiplas respostas são simultaneamente válidas

## Opções de aparência

{{< table >}}
| Aparência | Descrição |
|------------|-----------|
| *(nenhuma)* | Caixas de verificação predefinidas, uma por linha |
| `minimal` | Widget de seleção múltipla em menu suspenso |
| `compact` | Grelha compacta, colunas ajustam-se à largura do ecrã |
| `compact-N` | Grelha compacta forçada para N colunas |
| `horizontal` | Escolhas dispostas horizontalmente numa linha (web) |
| `horizontal-compact` | Horizontal, espaçamento compacto (web) |
| `label` | Mostra apenas etiquetas, sem caixas de verificação (use com `list-nolabel`) |
| `list-nolabel` | Mostra apenas caixas de verificação, sem etiquetas (use com `label`) |
| `columns(N)` | Exibir em N colunas (extensão rtSurvey) |
{{< /table >}}

### Exemplo: Layout compacto de 3 colunas

| type | name | label | appearance |
|------|------|-------|------------|
| select_multiple symptoms | symptoms | Selecione todos os sintomas observados | compact-3 |

## Usar `selected()` em expressões

Como o valor armazenado é uma cadeia separada por espaços, **deve** usar `selected()` para testar se uma escolha específica foi selecionada. Usar `=` não funcionará corretamente.

### Em `relevant`

Mostrar uma pergunta de seguimento apenas se "outro" foi selecionado:

| type | name | label | relevant |
|------|------|-------|----------|
| select_multiple crops | crops_grown | Que culturas são cultivadas? | |
| text | crops_other | Por favor especifique outras culturas | `selected(${crops_grown}, 'other')` |

### Em `constraint`

Exigir pelo menos 2 escolhas:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple issues | issues | `count-selected(.) >= 2` | Selecione pelo menos 2 problemas |

Limitar a um máximo de 3:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple priorities | priorities | `count-selected(.) <= 3` | Selecione no máximo 3 prioridades |

## Opção "Nenhum dos anteriores" / opção exclusiva

Um padrão comum é tornar uma opção mutuamente exclusiva com todas as outras. Use um `constraint` para impô-lo:

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| select_multiple issues | issues | Selecione todos os problemas presentes | `not(selected(., 'none') and count-selected(.) > 1)` | "Nenhum" não pode ser selecionado com outras opções |

## Contar e resumir seleções

| Função | Exemplo | Resultado |
|----------|---------|--------|
| `count-selected(field)` | `count-selected(${crops_grown})` | Número de escolhas selecionadas |
| `selected(field, value)` | `selected(${crops_grown}, 'maize')` | verdadeiro/falso |
| `selected-at(field, index)` | `selected-at(${crops_grown}, 0)` | Primeiro valor selecionado |
| `choice-label(field, value)` | `choice-label(${crops_grown}, 'maize')` | Etiqueta para um valor |

## Melhores Práticas

1. Use sempre `selected()` em `relevant`, `constraint` e `calculate` — nunca `=` ou `!=`.
2. Adicione uma restrição para limitar o número máximo de seleções se o design da pergunta o exigir.
3. Inclua uma opção "Nenhum" ou "Não aplicável" quando zero seleções é uma resposta válida.
4. Para listas longas (15+ escolhas), use `minimal` (menu suspenso de seleção múltipla) para evitar rolagem excessiva.
5. Exporte dados e use divisão de cadeia de caracteres na sua ferramenta de análise — o formato separado por espaços requer divisão antes de pivotar.

## Limitações

- Os valores de select_multiple não podem ser comparados diretamente com `=`. Use sempre `selected()`.
- A aparência compacta pode não renderizar bem para etiquetas de escolha muito longas.
- Ao filtrar escolhas com `choice_filter`, a filtragem aplica-se a todas as escolhas exibidas, tal como em `select_one`.
