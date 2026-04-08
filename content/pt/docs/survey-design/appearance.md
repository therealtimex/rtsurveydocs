---
title: "Aparência"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

A coluna `appearance` no rtSurvey permite-lhe personalizar a apresentação visual e o comportamento das perguntas nos seus inquéritos. Esta funcionalidade melhora a experiência do utilizador e pode melhorar significativamente a eficiência da recolha de dados. O rtSurvey suporta atributos de aparência XLSForm padrão e alarga-os com opções adicionais.

## Atributos de Aparência XLSForm Padrão

O rtSurvey suporta os seguintes atributos de aparência XLSForm padrão:

| Atributo de Aparência | Tipos de Pergunta | Descrição |
|----------------------|----------------|-----------|
| multiline | text | Cria uma caixa de texto multilinhas (melhor para clientes web) |
| minimal | select_one, select_multiple | Exibe escolhas num menu suspenso |
| quick | select_one | Avança automaticamente para a próxima pergunta após seleção (apenas móvel) |
| no-calendar | date | Suprime a exibição do calendário (apenas móvel) |
| month-year | date | Permite seleção apenas de mês e ano |
| year | date | Permite seleção apenas de ano |
| horizontal-compact | select_one, select_multiple | Exibe escolhas horizontalmente (apenas web) |
| horizontal | select_one, select_multiple | Exibe escolhas horizontalmente em colunas (apenas web) |
| likert | select_one | Apresenta escolhas como uma escala de Likert |
| compact | select_one, select_multiple | Exibe escolhas lado a lado com preenchimento mínimo |
| quickcompact | select_one | Combina exibição compacta com avanço automático (apenas móvel) |
| field-list | groups | Exibe o grupo inteiro num único ecrã (apenas móvel) |
| label | select_one, select_multiple | Mostra etiquetas de escolha sem entradas |
| list-nolabel | select_one, select_multiple | Mostra entradas sem etiquetas (use com `label`) |
| table-list | groups | Exibe perguntas em formato de tabela |
| signature | image | Ativa a captura de assinatura (apenas móvel) |
| draw | image | Permite desenho à mão livre (apenas móvel) |
| map, quick map | select_one, select_one_from_file | Ativa seleção a partir de funcionalidades de mapa |

## Melhores Práticas para Usar Aparência

1. **Consistência**: Use atributos de aparência de forma consistente ao longo do seu inquérito para um aspeto uniforme.
2. **Móvel vs. Web**: Considere como as aparências serão renderizadas em diferentes dispositivos e plataformas.
3. **Desempenho**: Seja cauteloso com atributos de aparência que podem atrasar o carregamento do formulário (por ex., `table-list` para grupos grandes).
4. **Experiência do Utilizador**: Escolha aparências que tornem a entrada de dados mais fácil e intuitiva para os respondentes.
5. **Teste**: Teste sempre o seu formulário nos dispositivos alvo para garantir que as aparências funcionam como esperado.

## Técnicas Avançadas

### Combinar Aparências

Alguns atributos de aparência podem ser combinados para layouts mais complexos:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Selecione um: | minimal compact |
```

### Aparências Dinâmicas

O rtSurvey permite alterações de aparência dinâmicas baseadas na lógica do formulário:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Introduza a hora: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Considerações para a Aplicação Móvel

- Algumas aparências (por ex., `quick`, `signature`) são específicas para dispositivos móveis.
- Teste cuidadosamente tanto no Android como no iOS para garantir comportamento consistente.

## Atributos de Aparência Alargados do rtSurvey

Além das aparências XLSForm padrão, o rtSurvey suporta as seguintes opções específicas da plataforma:

### Controlo de dados e exibição

| Atributo de Aparência | Tipos de Pergunta | Descrição |
|----------------------|----------------|-----------|
| `invisible` | qualquer | Oculta o campo da vista enquanto ainda recolhe ou calcula o seu valor. Diferente do tipo `hidden` — o campo ainda participa na lógica. |
| `displaytitle` | qualquer | Força a exibição da etiqueta/título do campo mesmo quando seria suprimida de outra forma. |
| `autopull` | select_one, select_multiple | Obtém automaticamente dados externos para preencher escolhas quando o formulário carrega ou um campo de gatilho muda. |
| `floating_hint` | text, integer, decimal | Mostra o texto de dica como uma etiqueta flutuante acima do campo de entrada em vez de abaixo dele. |
| `calculate-button` | calculate | Adiciona um botão visível que despoleta o recálculo do campo a pedido, em vez de calcular automaticamente. |

### Layout

| Atributo de Aparência | Tipos de Pergunta | Descrição |
|----------------------|----------------|-----------|
| `1screen` | group | Força o grupo inteiro a ser exibido num único ecrã independentemente do tamanho do grupo. |
| `columns(n)` | select_one, select_multiple | Exibe escolhas em `n` colunas. Exemplo: `columns(3)` mostra três colunas de botões de rádio. |
| `gridformat<row=R col=C colspan=S align=center>` | qualquer | Posiciona o campo num layout CSS-grid na linha `R`, coluna `C`, ocupando `S` colunas. Usado com `advanced-extension/grid-layout`. |
| `ignore-simplify` | qualquer | Instrui o renderizador do formulário a ignorar a simplificação ou condensação automática do layout deste campo. |
| `required-but-simplify` | qualquer | O campo é obrigatório mas o seu layout é ainda simplificado pelo renderizador |
| `embed` | qualquer | Renderiza o campo em modo de exibição embutido/inline, suprimindo o seu wrapper externo e o container de etiqueta |
| `popup` | select_one, select_multiple | Renderiza a lista de escolhas numa sobreposição popup/modal em vez de inline |
| `auto-hide-empty` | boxtag, select | Oculta todo o widget de pergunta quando a lista de escolhas está vazia |
| `text-nolabel` | select_one, select_multiple | Oculta a etiqueta de texto para cada escolha, mostrando apenas o controlo de entrada |

### Widgets

| Atributo de Aparência | Tipos de Pergunta | Descrição |
|----------------------|----------------|-----------|
| `likert` | select_one | Apresenta escolhas como uma linha de escala de Likert (já na tabela padrão acima; confirmado suportado). |
| `distress` | select_one | Renderiza escolhas como o widget visual da Escala de Angústia Psicológica de Kessler (K10) com ícones emocionais. |

### Widgets visuais de seleção

Estas aparências alteram toda a renderização das listas de escolha de seleção.

| Aparência | Tipos de Pergunta | Descrição |
|-----------|------------------|-----------|
| `tagging` | select_one, select_multiple | As escolhas renderizam como chips de etiqueta clicáveis em forma de pílula. |
| `boxtag` | select_one, select_multiple | As escolhas renderizam como caixas retangulares estilizadas que o utilizador toca. |
| `boxtag -search` | select_one, select_multiple | Layout boxtag com entrada de pesquisa/filtro ao vivo acima das caixas. |
| `duolingo-style1` | select_one, select_multiple | Layout de cartão grande inspirado no Duolingo — adequado para listas curtas com ícones. |
| `rating_box` | select_one, select_multiple | Grelha de caixas numeradas tocáveis — adequada para perguntas de escala ou NPS. |
| `star_rating` | select_one | As escolhas renderizam como estrelas; o número de estrelas é igual ao número de escolhas. |
| `choices-noshow` | select_one, select_multiple | Mostra inicialmente apenas as primeiras 10 escolhas com um controlo "Mostrar mais". |
| `noshow` | select_one, select_multiple | Oculta a lista de escolhas completamente; o valor é definido programaticamente via calculate ou API. |
| `checkall` | select_multiple | Adiciona um atalho "Selecionar tudo" no topo da lista de escolhas. |
| `max-items(N)` | select_one, select_multiple | Limita a lista de escolhas visível a N itens. Exemplo: max-items(5). |

### Widgets visuais de texto

| Aparência | Tipos de Pergunta | Descrição |
|-----------|------------------|-----------|
| `richtext` | text | Substitui a caixa de texto simples por um editor de texto rico (negrito, itálico, listas, links). Armazena HTML. |
| `typingtest` | text | Widget de teste de digitação — o texto da etiqueta é a passagem; o widget regista a resposta digitada e o tempo. |

### Extensões de multimédia

| Aparência | Tipos de Pergunta | Descrição |
|-----------|------------------|-----------|
| `watermark("expression")` | image | Sobrepõe uma marca d'água de texto em fotos capturadas. O argumento é uma expressão XPath avaliada no momento da captura. |
| `editable` | image | Ativa anotação/desenho sobre a foto capturada antes de guardar. |

### Configuração de exibição inline

Os modificadores `display{}` e `results{}` controlam o alinhamento de ícones e a exibição de resultados para widgets inline.

#### Parâmetros de `display{}`

| Parâmetro | Valores | Descrição |
|-----------|---------|-----------|
| Alinhamento | `left`, `right`, `top`, `bottom`, `center` | Posição do ícone em relação ao campo de entrada |
| Tamanho | `small`, `medium`, `large` | Tamanho do ícone |
| Modo | `inline-icon` | Renderiza o gatilho apenas como ícone |
| Modo | `inline-button` | Renderiza o gatilho como botão completo |

#### Parâmetros de `results{}`

| Parâmetro | Valores | Descrição |
|-----------|---------|-----------|
| Alinhamento | `left`, `right`, `top`, `bottom`, `center` | Posição da exibição do valor do resultado |
| `hide(field)` | qualquer nome de sub-campo | Oculta um componente específico do resultado |

### Integração de API

| Atributo de Aparência | Tipos de Pergunta | Descrição |
|----------------------|----------------|-----------|
| `callapi` | text, integer, decimal, select_one | Ativa a integração de chamada de API para este campo. A coluna de cálculo deve conter uma expressão `callapi()`. Consulte [Chamar API](advanced-extension/call-api). |
| `callapi-verify(params)` | text, integer, decimal | Despoleta uma chamada de verificação de API usando parâmetros estáticos. O formulário bloqueia o progresso até que a API confirme o valor. |
| `callapi-verify(dynamicParams)` | text, integer, decimal | Igual a `callapi-verify` mas com parâmetros derivados de outros valores de campo em runtime. |

### Formato de data/hora em linha

Para campos `date`, `time` e `datetime`, pode especificar um formato de exibição personalizado usando uma cadeia de formato anexada à aparência:

```
inline-[%d/%m/%Y]
inline-1line-[%d/%m/%Y %H:%M]
```

Os tokens de formato são os mesmos que `format-date()` e `format-date-time()`. Consulte [Funções — Funções de data e hora](operators-and-functions/functions#date-and-time-functions).

Exemplo:

| type | name | label | appearance |
|------|------|-------|------------|
| datetime | event_time | Data e hora do evento | inline-[%d/%m/%Y %I:%M %p] |
| date | birth_date | Data de nascimento | inline-[%d/%m/%Y] |

## Limitações Conhecidas

- As aparências complexas podem não renderizar de forma idêntica em todas as plataformas.
- Algumas aparências avançadas do rtSurvey podem não ser suportadas no modo offline.

## Resolução de Problemas de Aparência

1. **Aparência Não Aplicada**: Verifique erros tipográficos na coluna de aparência.
2. **Renderização Inconsistente**: Verifique a compatibilidade com o tipo de pergunta e plataforma.
3. **Problemas de Desempenho**: Considere simplificar aparências complexas, especialmente para inquéritos grandes.
