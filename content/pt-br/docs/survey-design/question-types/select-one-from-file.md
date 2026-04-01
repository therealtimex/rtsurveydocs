---
title: "Selecionar de arquivo"
description: "select_one_from_file e select_multiple_from_file carregam opções dinamicamente de um arquivo CSV ou XML externo anexado ao formulário."
icon: "file-earmark-spreadsheet"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 241
---

`select_one_from_file` e `select_multiple_from_file` funcionam como `select_one` e `select_multiple`, mas em vez de definir opções na planilha **choices**, as opções são carregadas de um **arquivo CSV ou XML externo** anexado ao formulário. Isso é útil quando sua lista de opções é muito longa, muda frequentemente ou precisa ser atualizada sem reconstruir todo o formulário.

## Especificação básica do XLSForm

| type | name | label |
|------|------|-------|
| select_one_from_file health_facilities.csv | facility | Selecione o estabelecimento de saúde |
| select_multiple_from_file crops.csv | crops | Quais culturas o domicílio cultiva? |

O nome do arquivo após o nome do tipo deve corresponder ao nome do arquivo que você anexa ao fazer upload do formulário.

## Formato do arquivo CSV

Seu arquivo CSV deve ter pelo menos duas colunas: `name` (o valor armazenado) e `label` (o texto exibido). Você pode adicionar qualquer número de colunas extras para filtragem.

**health_facilities.csv:**

```
name,label,district,type
HF001,Clínica Central de Nairóbi,Nairóbi,clinica
HF002,Centro de Saúde Westlands,Nairóbi,centro_saude
HF003,Hospital Distrital de Kisumu,Kisumu,hospital
```

## Filtrando opções

Use a coluna `choice_filter` para mostrar apenas as opções que correspondem ao contexto atual. Referencie colunas CSV pelo nome da coluna diretamente (sem `${}`):

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one districts.csv | district | Selecione o distrito | |
| select_one_from_file health_facilities.csv | facility | Selecione o estabelecimento | district = ${district} |

Neste exemplo, apenas os estabelecimentos do distrito selecionado são mostrados. O `district` em `choice_filter` refere-se à coluna `district` no arquivo CSV; `${district}` refere-se ao campo do formulário chamado `district`.

## Usos

As perguntas de seleção a partir de arquivo são comumente usadas para:

1. **Listas de opções longas** — estabelecimentos de saúde, escolas, aldeias, listas de espécies (centenas ou milhares de itens)
2. **Listas atualizadas com frequência** — quando a lista mestre muda entre rodadas de pesquisa, atualize apenas o CSV sem reconstruir o formulário
3. **Dados de referência compartilhados** — um arquivo CSV usado em múltiplos formulários
4. **Seleções cascata filtradas** — carregue todas as regiões/distritos/aldeias em um arquivo, depois filtre pela seleção pai

## Anexando o arquivo

Ao fazer upload do seu formulário para o rtSurvey, anexe o arquivo CSV como um **anexo de mídia**. O nome do arquivo na definição do formulário deve corresponder exatamente ao nome do arquivo do anexo.

{{% alert icon=" " context="warning" %}}
Os nomes de arquivo são sensíveis a maiúsculas e minúsculas. `Health_Facilities.csv` e `health_facilities.csv` são tratados como arquivos diferentes.
{{% /alert %}}

## Usando `choice-label()` com from-file

Para exibir o rótulo de uma opção selecionada em um campo de nota ou cálculo:

| type | name | label | calculation |
|------|------|-------|-------------|
| select_one_from_file health_facilities.csv | facility | Selecione o estabelecimento | |
| calculate | facility_label | | choice-label(${facility}, ${facility}) |
| note | summary | Estabelecimento selecionado: ${facility_label} | |

## Práticas recomendadas

1. Mantenha seus arquivos CSV abaixo de 5.000 linhas para bom desempenho em dispositivos móveis.
2. Sempre inclua uma coluna `name` e `label` — colunas adicionais são opcionais.
3. Para seleções cascata, use um único CSV com uma coluna pai e filtre com `choice_filter`.
4. Versione seus nomes de arquivo CSV (por exemplo, `facilities_v3.csv`) ao fazer mudanças significativas na estrutura das colunas.
5. Teste as expressões de filtragem cuidadosamente — um erro de digitação em `choice_filter` silenciosamente não mostrará opções.

## Limitações

- Arquivos CSV muito grandes (10.000+ linhas) podem desacelerar o carregamento do formulário, especialmente em dispositivos de baixo desempenho.
- Os arquivos CSV devem ser enviados junto com o formulário — eles não podem ser buscados de uma URL em tempo de execução (use `search()` ou `pulldata()` para buscas dinâmicas).
- `select_multiple_from_file` é menos comumente suportado em todos os clientes — verifique a compatibilidade antes de usar.

## Comparação com `search()`

| | `select_one_from_file` | aparência `search()` |
|--|----------------------|----------------------|
| Fonte das opções | Arquivo CSV/XML anexado | Consulta de banco de dados no lado do servidor |
| Funciona offline | Sim (arquivo está incluído) | Requer conectividade |
| Contagem de opções | Limitada pela memória do dispositivo | Ilimitada (paginada) |
| Dados em tempo real | Não | Sim |

Para conjuntos de dados grandes, que mudam com frequência ou do lado do servidor, consulte [Busca dinâmica](../advanced-extension/dynamic-search).
