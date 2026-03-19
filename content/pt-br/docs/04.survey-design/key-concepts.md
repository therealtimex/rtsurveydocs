---
title: "Conceitos principais"
description: "Visão geral do design de formulários"
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 210
---

## O que é um XLSForm?
O rtSurvey usa uma versão estendida do padrão [XLSForm](https://xlsform.org/) para design de formulários, oferecendo recursos poderosos para criar pesquisas sofisticadas. Este guia apresentará os conceitos principais do design de formulários no rtSurvey, desde a estrutura básica do XLSForm até os recursos avançados específicos do rtSurvey.

Com XLSForms, você pode criar formulários em um formato legível por humanos usando a familiar ferramenta Excel, tornando-o acessível para quase todos. Este padrão facilita o compartilhamento e a colaboração na criação de formulários.

Embora os XLSForms sejam amigáveis para iniciantes, eles também permitem que usuários experientes criem formulários complexos.

O rtSurvey fornece uma maneira consistente de incorporar funcionalidades avançadas, como lógica de salto, em formulários em várias plataformas de coleta de dados web e móvel.

## Estrutura do XLSForm
Um XLSForm normalmente consiste em duas planilhas principais:

1. **survey**: Define a estrutura e o conteúdo do seu formulário.
2. **choices**: Especifica as opções de resposta para perguntas de múltipla escolha.

Uma planilha opcional **settings** pode fornecer especificações adicionais do formulário.

É importante observar que as colunas obrigatórias nas planilhas survey e choices devem estar presentes para que o formulário funcione corretamente. Colunas opcionais em ambas as planilhas fornecem mais controle sobre o comportamento de cada entrada no formulário, mas não são essenciais.

As colunas na sua pasta de trabalho Excel podem aparecer em qualquer ordem, e as colunas opcionais podem ser deixadas em branco. No entanto, é crucial usar a sintaxe e as convenções de nomenclatura precisas especificadas na documentação do XLSForm para que o formulário funcione corretamente.

### A planilha survey
A **planilha survey** é onde você define a estrutura do seu formulário e fornece o conteúdo. Cada linha na planilha survey representa uma pergunta ou elemento no seu formulário. As seguintes colunas são obrigatórias na planilha survey:

- `type`: Especifica o tipo de entrada que você espera para a pergunta.
- `name`: Especifica o nome de variável único para essa entrada. Os nomes devem começar com uma letra ou sublinhado e podem conter apenas letras, dígitos, hífens, sublinhados e pontos. Os nomes diferenciam maiúsculas de minúsculas.
- `label`: Contém o texto real que você vê para a pergunta no formulário.

| type                | name     | label                      |
| ------------------- | -------- | -------------------------- |
| today               | today    |                            |
| select_one gender   | gender   | Gênero do respondente?     |
| integer             | age      | Idade do respondente?      |

### A planilha choices
A planilha **`choices`** é usada para especificar as opções de resposta para perguntas de múltipla escolha. Cada linha representa uma opção de resposta. As seguintes colunas são obrigatórias na planilha choices:

- **`list_name`**: Agrupa um conjunto de opções de resposta relacionadas.
- **`name`**: Especifica o nome de variável único para essa opção de resposta.
- **`label`**: Mostra a opção de resposta exatamente como você quer que apareça no formulário.

| list_name           | name        | label            |
| ------------------- | ----------- | ---------------- |
| gender              | transgender | Transgênero      |
| gender              | female      | Feminino         |
| gender              | male        | Masculino        |
| gender              | other       | Outro            |

As colunas que você adiciona à sua pasta de trabalho Excel, sejam obrigatórias ou opcionais, podem aparecer em qualquer ordem. As colunas opcionais podem ser omitidas completamente. Linhas ou colunas podem ser deixadas em branco para facilitar a leitura, mas os dados após 20 colunas ou linhas em branco adjacentes em uma planilha não serão processados. Toda a formatação do arquivo .xlsx é ignorada, portanto, você pode usar linhas divisórias, sombreamento e outra formatação de fonte para tornar o formulário mais legível.

Uma coisa a ter em mente ao criar formulários no Excel é que a sintaxe que você usa deve ser precisa. Por exemplo, se você escrever **Choices** ou **choice** em vez de **choices**, o formulário não funcionará.

### A planilha settings

A planilha settings é opcional, mas permite que você especifique metadados e comportamento no nível do formulário. As colunas comuns na planilha settings incluem:

| Coluna | Descrição |
|--------|-----------|
| form_title | O título do formulário como aparece para os usuários |
| form_id | Um identificador único para o formulário, usado no gerenciamento de dados e chamadas de API |
| default_language | O código de idioma padrão para formulários multilíngues (por exemplo, 'pt' para Português) |
| version | O número de versão do formulário, útil para rastrear alterações |
| instance_name | Expressão para gerar um nome único para cada envio de formulário |
| generation | Inteiro que marca a geração do formulário. Incremente para mudanças estruturais |
| family | Identificador para agrupar formulários relacionados entre mudanças estruturais |

A planilha settings no rtSurvey também pode incluir configurações adicionais específicas das funcionalidades estendidas do rtSurvey. Consulte a documentação do rtSurvey para uma lista completa de configurações suportadas.

## Componentes principais da planilha survey

A planilha survey é o núcleo do seu design de formulário. Aqui está uma visão geral de seus componentes principais:

| Componente | Descrição |
|------------|-----------|
| [type](#question-types) | Especifica o tipo de pergunta (por exemplo, text, integer, select_one) |
| [name](#naming-conventions) | Identificador único para a pergunta |
| [label](#labels-and-translations) | O texto exibido ao respondente |
| [hint](#hints-and-help-text) | Orientação adicional para o respondente |
| [appearance](#appearance-options) | Modifica como a pergunta é exibida |
| [relevant](#relevance-and-skip-logic) | Determina quando a pergunta deve ser feita (lógica de salto) |
| [constraint](#constraints-and-validation) | Valida a resposta |
| [calculation](#calculations) | Calcula valores com base em outras respostas |
| [required](#required-fields) | Especifica se a pergunta deve ser respondida |


Cada um desses componentes desempenha um papel crucial na criação de pesquisas eficazes e eficientes.

### Tipos de perguntas
O XLSForm suporta vários tipos de perguntas. Estas são apenas algumas das opções que você pode inserir na coluna **`type`** na planilha **`survey`** do seu XLSForm:

| Tipo de pergunta          | Entrada de resposta                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| integer                   | Entrada de número inteiro (ou seja, número sem decimais).                                       |
| decimal                   | Entrada decimal.                                                                                 |
| range                     | Entrada de [intervalo](#range) (incluindo classificação)                                        |
| text                      | Resposta de texto livre.                                                                        |
| select_one [options]      | Pergunta de [múltipla escolha](#multiple-choice); apenas uma resposta pode ser selecionada.     |
| select_multiple [options] | Pergunta de [múltipla escolha](#multiple-choice); várias respostas podem ser selecionadas.      |
| select_one_from_file [file]| [Múltipla escolha a partir de arquivo](#multiple-choice-from-file); apenas uma resposta.       |
| select_multiple_from_file [file]| [Múltipla escolha a partir de arquivo](#multiple-choice-from-file); várias respostas.    |
| rank [options]            | Pergunta de [classificação](#rank); ordenar uma lista.                                          |
| note                      | Exibe uma nota na tela, sem entrada. Abreviação para type=text com readonly=true.               |
| geopoint                  | Coletar uma [coordenada GPS única](#gps).                                                       |
| geotrace                  | Registrar uma [linha de duas ou mais coordenadas GPS](#gps).                                    |
| geoshape                  | Registrar um [polígono de várias coordenadas GPS](#gps); o último ponto é igual ao primeiro.    |
| date                      | Entrada de data.                                                                                |
| time                      | Entrada de hora.                                                                                |
| dateTime                  | Aceita entrada de data e hora.                                                                  |
| image                     | Tirar uma foto ou fazer upload de um [arquivo de imagem](#image).                               |
| audio                     | Fazer uma gravação de áudio ou fazer upload de um arquivo de áudio.                             |
| background-audio          | O áudio é gravado em segundo plano enquanto o formulário é preenchido.                          |
| video                     | Fazer uma gravação de vídeo ou fazer upload de um arquivo de vídeo.                             |
| file                      | Entrada de arquivo genérica (txt, pdf, xls, xlsx, doc, docx, rtf, zip)                        |
| barcode                   | Escanear um código de barras, requer o aplicativo de scanner de código de barras instalado.    |
| calculate                 | Realizar um cálculo; consulte a seção [Cálculo](#calculation) abaixo.                         |
| acknowledge               | Prompt de confirmação que define o valor como "OK" se selecionado.                             |
| hidden                    | Um campo sem elemento de UI associado que pode ser usado para armazenar uma constante          |
| xml-external              | Adiciona uma referência a um arquivo de [dados XML externo](#external-xml-data)                |

### Rótulos

Os rótulos são o texto exibido aos respondentes para cada pergunta. Eles são cruciais para uma comunicação clara nas pesquisas.

- **Uso básico**: Na coluna `label`, insira o texto da pergunta.
- **Múltiplos idiomas**: Use colunas adicionais como `label::Português` e `label::English` para pesquisas multilíngues.
- **Formatação**: O rtSurvey suporta formatação HTML básica nos rótulos para ênfase ou estrutura.

Exemplo:
```
| type | name | label | label::French |
|------|------|-------|---------------|
| text | name | Qual é o seu nome? | Quel est votre nom? |
```

### Dicas

As dicas fornecem orientação adicional aos respondentes sem sobrecarregar o texto principal da pergunta.

- **Uso**: Adicione dicas na coluna `hint`.
- **Visibilidade**: As dicas são normalmente exibidas abaixo do texto principal da pergunta.
- **Multilíngue**: Como os rótulos, as dicas podem ser especificadas para múltiplos idiomas usando colunas `hint::Idioma`.

Exemplo:
```
| type | name | label | hint |
|------|------|-------|------|
| integer | age | Quantos anos você tem? | Por favor, insira sua idade em anos |
```

### Aparência

A coluna `appearance` no rtSurvey permite a personalização de como as perguntas são exibidas.

- **Opções padrão**: Incluem 'multiline' para texto, 'horizontal' para perguntas de seleção.
- **Extensões do rtSurvey**: 
  - Entrada de hora: Várias opções de exibição de relógio (por exemplo, `inline`, `inline-1line`)
  - Personalização de cores: Use a função `colors()` para alterar as cores dos ícones

Exemplo:
```
| type | name | label | appearance |
|------|------|-------|------------|
| text | time | Insira a hora | inline-[%H:%M] |
```

### Relevante

A coluna `relevant` implementa lógica de salto, determinando quando uma pergunta deve ser exibida.

- **Sintaxe**: Use expressões XPath para definir condições.
- **Variáveis**: Referencie outros nomes de perguntas usando `${nome_da_pergunta}`.

Exemplo:
```
| type | name | label | relevant |
|------|------|-------|----------|
| text | allergies | Liste as alergias | ${has_allergies} = 'yes' |
```

### Obrigatório

A coluna `required` especifica se uma pergunta deve ser respondida.

- **Uso básico**: Use 'yes' ou 'true' para tornar uma pergunta obrigatória.
- **Avançado**: Pode usar expressões para requisito condicional.

Exemplo:
```
| type | name | label | required |
|------|------|-------|----------|
| text | email | Endereço de e-mail | yes |
```

### Repetições

As repetições permitem que um grupo de perguntas seja respondido várias vezes.

- **Uso**: Use as linhas `begin repeat` e `end repeat` para definir um grupo repetido.
- **Nomenclatura**: Dê a cada grupo de repetição um nome único.

Exemplo:
```
| type | name | label |
|------|------|-------|
| begin repeat | household_member | Membro do domicílio |
| text | member_name | Nome |
| integer | member_age | Idade |
| end repeat | | |
```

### Mídia

O rtSurvey suporta vários tipos de mídia em pesquisas, incluindo imagens, áudio e vídeo.

- **Tipos de perguntas**: Use 'image', 'audio' ou 'video' na coluna type.
- **Mídia em rótulos**: Referencie arquivos de mídia em rótulos usando tags HTML.

Exemplo:
```
| type | name | label |
|------|------|-------|
| image | house_photo | Tire uma foto da casa |
| note | | <img src="logo.jpg" /> Bem-vindo à pesquisa |
```

### Somente leitura

Perguntas somente leitura exibem informações sem permitir entrada do usuário.

- **Uso**: Adicione 'readonly' à coluna `appearance`.
- **Cálculos**: Frequentemente usado com o tipo calculate para exibir valores calculados.

Exemplo:
```
| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | bmi | IMC | readonly | ${weight} / (${height} * ${height}) |
```

## Extensões do rtSurvey

O rtSurvey expande o padrão XLSForm suportando capacidades adicionais, como `grid layout`, `html format` e muitos novos `widgets`.

### Layout em grade
O rtSurvey permite que seu formulário imite a aparência das pesquisas em papel tradicionais, compactando várias perguntas em uma linha.

### Configurações do formulário

### Configurações de dados

### Estilo Typeform

### Extensão de pulldata()

### Extensões baseadas em aparência

### Extensões Webbox
