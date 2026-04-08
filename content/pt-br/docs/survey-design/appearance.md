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

A coluna `appearance` no rtSurvey permite que você personalize a apresentação visual e o comportamento das perguntas nas suas pesquisas. Este recurso melhora a experiência do usuário e pode melhorar significativamente a eficiência da coleta de dados. O rtSurvey suporta atributos de aparência padrão do XLSForm e os estende com opções adicionais.

## Atributos de aparência padrão do XLSForm

O rtSurvey suporta os seguintes atributos de aparência padrão do XLSForm:

| Atributo de aparência | Tipos de perguntas | Descrição |
|-----------------------|-------------------|-----------|
| multiline | text | Cria uma caixa de texto de várias linhas (melhor para clientes web) |
| minimal | select_one, select_multiple | Exibe opções em um menu suspenso |
| quick | select_one | Avança automaticamente para a próxima pergunta após a seleção (somente móvel) |
| no-calendar | date | Suprime a exibição do calendário (somente móvel) |
| month-year | date | Permite a seleção apenas de mês e ano |
| year | date | Permite a seleção apenas do ano |
| horizontal-compact | select_one, select_multiple | Exibe opções horizontalmente (somente web) |
| horizontal | select_one, select_multiple | Exibe opções horizontalmente em colunas (somente web) |
| likert | select_one | Apresenta opções como uma escala Likert |
| compact | select_one, select_multiple | Exibe opções lado a lado com preenchimento mínimo |
| quickcompact | select_one | Combina exibição compacta com avanço automático (somente móvel) |
| field-list | groups | Exibe o grupo inteiro em uma única tela (somente móvel) |
| label | select_one, select_multiple | Mostra rótulos de opção sem entradas |
| list-nolabel | select_one, select_multiple | Mostra entradas sem rótulos (use com `label`) |
| table-list | groups | Exibe perguntas em formato de tabela |
| signature | image | Habilita captura de assinatura (somente móvel) |
| draw | image | Permite desenho à mão livre (somente móvel) |
| map, quick map | select_one, select_one_from_file | Habilita seleção a partir de recursos do mapa |

## Práticas recomendadas para usar aparência

1. **Consistência**: Use atributos de aparência de forma consistente em toda a sua pesquisa para uma aparência uniforme.
2. **Móvel vs. web**: Considere como as aparências serão renderizadas em diferentes dispositivos e plataformas.
3. **Desempenho**: Tenha cuidado com atributos de aparência que podem diminuir o carregamento do formulário (por exemplo, `table-list` para grupos grandes).
4. **Experiência do usuário**: Escolha aparências que facilitem a entrada de dados e sejam mais intuitivas para os respondentes.
5. **Teste**: Sempre teste seu formulário nos dispositivos de destino para garantir que as aparências funcionem conforme esperado.

## Técnicas avançadas

### Combinando aparências

Alguns atributos de aparência podem ser combinados para layouts mais complexos:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Selecione um: | minimal compact |
```

### Aparências dinâmicas

O rtSurvey permite alterações dinâmicas de aparência com base na lógica do formulário:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Insira a hora: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Considerações sobre aplicativo móvel

- Algumas aparências (por exemplo, `quick`, `signature`) são específicas para dispositivos móveis.
- Teste minuciosamente no Android e iOS para garantir comportamento consistente.

## Atributos de aparência estendidos do rtSurvey

Além das aparências padrão do XLSForm, o rtSurvey suporta as seguintes opções específicas da plataforma:

### Controle de dados e exibição

| Atributo de aparência | Tipos de perguntas | Descrição |
|-----------------------|-------------------|-----------|
| `invisible` | qualquer | Oculta o campo da visualização enquanto ainda coleta ou calcula seu valor. Diferente do tipo `hidden` — o campo ainda participa da lógica. |
| `displaytitle` | qualquer | Força a exibição do rótulo/título do campo mesmo quando seria suprimido. |
| `autopull` | select_one, select_multiple | Busca automaticamente dados externos para preencher opções quando o formulário carrega ou um campo de gatilho muda. |
| `floating_hint` | text, integer, decimal | Mostra o texto de dica como um rótulo flutuante acima do campo de entrada em vez de abaixo. |
| `calculate-button` | calculate | Adiciona um botão visível que aciona o recálculo do campo sob demanda, em vez de calcular automaticamente. |

### Layout

| Atributo de aparência | Tipos de perguntas | Descrição |
|-----------------------|-------------------|-----------|
| `1screen` | group | Força o grupo inteiro a ser exibido em uma única tela, independentemente do tamanho do grupo. |
| `columns(n)` | select_one, select_multiple | Exibe opções em `n` colunas. Exemplo: `columns(3)` mostra três colunas de botões de rádio. |
| `gridformat<row=R col=C colspan=S align=center>` | qualquer | Posiciona o campo em um layout CSS-grid na linha `R`, coluna `C`, abrangendo `S` colunas. Usado com `advanced-extension/grid-layout`. |
| `ignore-simplify` | qualquer | Instrui o renderizador de formulário a pular a simplificação ou condensação automática do layout deste campo. |
| `required-but-simplify` | qualquer | O campo é obrigatório, mas seu layout ainda é simplificado pelo renderizador (substitui o comportamento padrão onde campos obrigatórios são excluídos da simplificação). |
| `embed` | qualquer | Renderiza o campo no modo de exibição incorporado/inline, suprimindo seu contêiner externo e de rótulo — usado quando uma pergunta está aninhada dentro de HTML personalizado. |
| `popup` | select_one, select_multiple | Renderiza a lista de opções em uma sobreposição popup/modal em vez de inline. |
| `auto-hide-empty` | boxtag, select | Oculta todo o widget de pergunta quando a lista de opções está vazia (por exemplo, nenhum resultado de API retornado). |
| `text-nolabel` | select_one, select_multiple | Oculta o rótulo de texto para cada opção, mostrando apenas o controle de entrada. Semelhante a `list-nolabel`, mas aplicado por opção em vez de como uma divisão de coluna. |

### Widgets

| Atributo de aparência | Tipos de perguntas | Descrição |
|-----------------------|-------------------|-----------|
| `likert` | select_one | Apresenta opções como uma linha de escala Likert (já na tabela padrão acima; confirmado como suportado). |
| `distress` | select_one | Renderiza opções como o widget visual da Escala de Sofrimento Psicológico de Kessler (K10) com ícones emocionais. |

### Widgets visuais de seleção

Essas aparências mudam toda a renderização das listas de opções de seleção.

| Atributo de aparência | Tipos de perguntas | Descrição |
|-----------------------|-------------------|-----------|
| `tagging` | select_one, select_multiple | As opções são renderizadas como chips de tag clicáveis em formato de pílula. |
| `boxtag` | select_one, select_multiple | As opções são renderizadas como caixas retangulares estilizadas que o usuário toca. |
| `boxtag -search` | select_one, select_multiple | Layout boxtag com uma entrada de pesquisa/filtro ao vivo acima das caixas. |
| `duolingo-style1` | select_one, select_multiple | Layout de cartão inspirado no Duolingo — adequado para listas curtas com ícones. |
| `rating_box` | select_one, select_multiple | Grade de caixas numeradas tocáveis — adequado para perguntas de escala ou NPS. |
| `star_rating` | select_one | As opções são renderizadas como estrelas; o número de estrelas é igual ao número de opções. |
| `choices-noshow` | select_one, select_multiple | Mostra inicialmente apenas as primeiras 10 opções com um controle "Mostrar mais". |
| `noshow` | select_one, select_multiple | Oculta completamente a lista de opções; o valor é definido programaticamente via `calculate` ou API. |
| `checkall` | select_multiple | Adiciona um atalho "Selecionar tudo" no topo da lista de opções. |
| `max-items(N)` | select_one, select_multiple | Limita a lista de opções visível a N itens. Exemplo: `max-items(5)`. |

### Widgets visuais de texto

| Atributo de aparência | Tipos de perguntas | Descrição |
|-----------------------|-------------------|-----------|
| `richtext` | text | Substitui a caixa de texto simples por um editor de texto rico (negrito, itálico, listas, links). Armazena HTML. |
| `typingtest` | text | Widget de teste de digitação — o texto do rótulo é a passagem; o widget registra a resposta digitada e o tempo. |

### Extensões de mídia

| Atributo de aparência | Tipos de perguntas | Descrição |
|-----------------------|-------------------|-----------|
| `watermark("expression")` | image | Sobrepõe uma marca d'água de texto nas fotos capturadas. O argumento é uma expressão XPath avaliada no momento da captura. Exemplo: `watermark("${id} ${today()}")`. |
| `editable` | image | Habilita anotação/desenho sobre a foto capturada antes de salvar. |

### Configuração de exibição inline

Os modificadores `display{}` e `results{}` podem ser anexados às aparências `inline` para controlar o alinhamento de ícones e a exibição de resultados.

#### Parâmetros de `display{}`

```
inline display{left}
inline display{right,small}
inline display{top,large,inline-icon}
```

| Parâmetro | Valores | Descrição |
|-----------|---------|-----------|
| Alinhamento | `left`, `right`, `top`, `bottom`, `center` | Posição do ícone em relação ao campo de entrada |
| Tamanho | `small`, `medium`, `large` | Tamanho do ícone (2,5 rem, 5 rem, 8 rem respectivamente) |
| Modo | `inline-icon` | Renderiza o gatilho apenas como ícone (sem borda de botão) |
| Modo | `inline-button` | Renderiza o gatilho como um botão completo |

#### Parâmetros de `results{}`

```
inline results{right}
inline results{left,hide(seconds)}
```

| Parâmetro | Valores | Descrição |
|-----------|---------|-----------|
| Alinhamento | `left`, `right`, `top`, `bottom`, `center` | Posição da exibição do valor do resultado |
| `hide(field)` | qualquer nome de subcampo | Oculta um componente específico do resultado (por exemplo, `hide(seconds)`) |

### Integração de API

| Atributo de aparência | Tipos de perguntas | Descrição |
|-----------------------|-------------------|-----------|
| `callapi` | text, integer, decimal, select_one | Habilita integração de chamada de API para este campo. A coluna de cálculo deve conter uma expressão `callapi()`. Consulte [Call API](advanced-extension/call-api). |
| `callapi-verify(params)` | text, integer, decimal | Aciona uma chamada de verificação de API usando parâmetros estáticos. O formulário bloqueia o progresso até que a API confirme o valor. |
| `callapi-verify(dynamicParams)` | text, integer, decimal | Igual a `callapi-verify`, mas com parâmetros derivados de outros valores de campo em tempo de execução. |

### Formato de data/hora inline

Para campos `date`, `time` e `datetime`, você pode especificar um formato de exibição personalizado usando uma string de formato anexada à aparência:

```
inline-[%d/%m/%Y]
inline-1line-[%d/%m/%Y %H:%M]
```

Os tokens de formato são os mesmos de `format-date()` e `format-date-time()`. Consulte [Funções — Funções de data e hora](operators-and-functions/functions#date-and-time-functions).

Exemplo:

| type | name | label | appearance |
|------|------|-------|------------|
| datetime | event_time | Data e hora do evento | inline-[%d/%m/%Y %I:%M %p] |
| date | birth_date | Data de nascimento | inline-[%d/%m/%Y] |

## Limitações conhecidas

- Aparências complexas podem não renderizar de forma idêntica em todas as plataformas.
- Algumas aparências avançadas do rtSurvey podem não ser suportadas no modo off-line.

## Solução de problemas de aparência

1. **Aparência não aplicada**: Verifique erros de digitação na coluna de aparência.
2. **Renderização inconsistente**: Verifique a compatibilidade com o tipo de pergunta e a plataforma.
3. **Problemas de desempenho**: Considere simplificar aparências complexas, especialmente para pesquisas grandes.
