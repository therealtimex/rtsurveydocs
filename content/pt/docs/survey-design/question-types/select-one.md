---
title: "Select_one"
description: "As perguntas Select_one permitem aos respondentes escolher exatamente uma opção de uma lista predefinida de escolhas."
icon: "radio_button_checked"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 224
---

O tipo de pergunta `select_one` pede ao respondente que escolha **exatamente uma opção** de uma lista predefinida. Por predefinição as escolhas são renderizadas como botões de rádio, mas está disponível uma ampla gama de opções de aparência para alterar o layout e o comportamento.

## Especificação XLSForm Básica

**folha de trabalho survey:**

| type | name | label |
|------|------|-------|
| select_one yesno | consent | O respondente deu consentimento? |

**folha de trabalho choices:**

| list_name | name | label |
|-----------|------|-------|
| yesno | yes | Sim |
| yesno | no | Não |

O `listname` em `select_one listname` deve corresponder à coluna `list_name` na folha de trabalho choices.

Para mais detalhes consulte a [especificação XLSForm](https://xlsform.org/en/#question-types).

## Utilizações

As perguntas Select_one são usadas para:

1. Perguntas de Sim/Não
2. Escolha múltipla de resposta única (por ex., nível de educação, género, estado civil)
3. Classificações categóricas (por ex., fraco / razoável / bom / excelente)
4. Seleções em cascata (encadeadas) onde as escolhas filtram com base numa resposta anterior
5. Seleção de país, região, distrito ou outra unidade administrativa

## Opções de aparência

Especifique um valor na coluna `appearance` para alterar como as escolhas são exibidas:

{{< table >}}
| Aparência | Descrição |
|------------|-----------|
| *(nenhuma)* | Botões de rádio predefinidos, um por linha |
| `minimal` | Único menu suspenso em vez de botões de rádio |
| `quick` | Avança automaticamente para a próxima pergunta imediatamente após seleção (apenas móvel) |
| `compact` | Grelha compacta de escolhas — o número de colunas ajusta-se à largura do ecrã |
| `compact-N` | Grelha compacta forçada para N colunas (por ex., `compact-3`) |
| `quickcompact` | Combina `quick` e `compact` |
| `quickcompact-N` | Combina `quick` e `compact` com N colunas forçadas |
| `horizontal` | Escolhas dispostas numa linha horizontal (web) |
| `horizontal-compact` | Horizontal, espaçamento compacto (web) |
| `likert` | Linha de escala de Likert — etiquetas acima, botões de rádio abaixo |
| `label` | Mostra apenas etiquetas de escolha sem entradas (use em par com `list-nolabel`) |
| `list-nolabel` | Mostra apenas as entradas sem etiquetas (use em par com `label`) |
| `columns(N)` | Exibir em N colunas (extensão rtSurvey, por ex., `columns(3)`) |
| `distress` | Widget de ícone emocional de Angústia Psicológica de Kessler (K10) |
| `search-api(...)` | Pesquisa dinâmica — carrega escolhas de uma API em runtime |
| `tagging` | Exibe as escolhas como chips de etiqueta clicáveis em vez de botões de rádio |
| `boxtag` | Exibe as escolhas como caixas retangulares estilizadas que o utilizador toca para selecionar |
| `boxtag -search` | Layout boxtag com entrada de pesquisa/filtro acima das caixas |
| `duolingo-style1` | Layout de cartão inspirado no Duolingo — cartões grandes e tocáveis com ícones |
| `rating_box` | Caixas de avaliação em grelha — melhor para escolhas numéricas ou de escala |
| `star_rating` | Widget de avaliação por estrelas — as escolhas renderizam como 1–N estrelas |
| `choices-noshow` | Mostra apenas as primeiras 10 escolhas inicialmente; revela o resto a pedido |
| `noshow` | Oculta a lista de escolhas completamente; o valor é definido programaticamente |
| `checkall` | Adiciona uma opção "Selecionar tudo" no topo da lista |
| `max-items(N)` | Limita o número de escolhas visíveis a N (por ex., max-items(5)) |
{{< /table >}}

### Exemplo: Escala de Likert

| type | name | label | appearance |
|------|------|-------|------------|
| select_one satisfaction | service_rating | Quão satisfeito está com o serviço? | likert |

### Exemplo: Compacto 3 colunas

| type | name | label | appearance |
|------|------|-------|------------|
| select_one regions | region | Selecione a região | compact-3 |

## Seleções em cascata

Uma seleção em cascata (encadeada) filtra as escolhas com base no valor selecionado numa pergunta anterior. Use a coluna `choice_filter` com o nome de uma coluna da sua folha de trabalho choices.

**survey:**

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one province | province | Selecione a província | |
| select_one district | district | Selecione o distrito | province_name = ${province} |

**choices:**

| list_name | name | label | province_name |
|-----------|------|-------|---------------|
| province | nairobi | Nairobi | |
| province | mombasa | Mombasa | |
| district | westlands | Westlands | nairobi |
| district | kasarani | Kasarani | nairobi |
| district | nyali | Nyali | mombasa |
| district | likoni | Likoni | mombasa |

Quando o respondente seleciona `nairobi`, apenas `Westlands` e `Kasarani` aparecem na lista de distritos.

{{% alert icon=" " context="warning" %}}
O nome de coluna usado em `choice_filter` (por ex., `province_name`) deve existir na folha de trabalho choices. O `${province}` referencia o campo do inquérito denominado `province`.
{{% /alert %}}

## Usar o valor selecionado em expressões

Referencie o **valor** selecionado (não a etiqueta) com `${fieldname}`:

```
relevant: ${consent} = 'yes'
```

Para obter a etiqueta da escolha em vez do valor, use `choice-label()`:

```
calculate: choice-label(${education_level}, ${education_level})
```

## Opção "Outro" com texto livre

Um padrão comum é incluir uma opção "outro" que revela um campo de texto:

| type | name | label | relevant |
|------|------|-------|----------|
| select_one occupation | job | Qual é a sua ocupação? | |
| text | job_other | Por favor especifique | `${job} = 'other'` |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| occupation | farmer | Agricultor |
| occupation | trader | Comerciante |
| occupation | student | Estudante |
| occupation | other | Outro (por favor especifique) |

## Melhores Práticas

1. Mantenha as listas curtas e mutuamente exclusivas — se os respondentes puderem querer mais de uma, use `select_multiple`.
2. Coloque a resposta mais comum primeiro, ou ordene alfabeticamente para listas longas.
3. Inclua sempre uma opção "Não sei" ou "Prefiro não responder" onde relevante.
4. Use `minimal` (menu suspenso) para listas com mais de 7–8 escolhas em dispositivos móveis para poupar espaço de ecrã.
5. Para seleções em cascata, adicione todas as colunas de filtro na folha de trabalho choices antes de construir o formulário.

## Limitações

- Um respondente só pode selecionar uma escolha — use `select_multiple` para perguntas de múltiplas respostas.
- A aparência `likert` funciona melhor com 5–7 escolhas que cabem numa linha.
- O avanço automático `quick` é apenas para dispositivos móveis; não tem efeito em formulários web.
