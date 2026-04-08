---
title: "Text Tags"
description: "Campo de entrada de tags — os respondentes digitam e pressionam Enter para criar tokens de tag individuais."
icon: "label"
date: "2026-04-08T00:00:00+00:00"
lastmod: "2026-04-08T00:00:00+00:00"
draft: false
toc: true
weight: 264
---

O tipo de pergunta `texttags` (também com o alias `text_tags`) renderiza uma entrada onde cada valor inserido pelo usuário se torna um **token de tag** discreto. Os usuários digitam um valor, pressionam Enter ou uma tecla delimitadora, e o valor é adicionado como um chip removível. Várias tags podem ser adicionadas em uma única resposta.

## Especificação básica do XLSForm

| type | name | label |
|------|------|-------|
| texttags | keywords | Digite palavras-chave (pressione Enter após cada uma) |

## Comportamento

- Cada entrada confirmada se torna uma tag exibida como uma pílula/chip dentro do campo.
- As tags podem ser removidas individualmente clicando no × do chip.
- O valor armazenado é uma string separada por espaços de todas as tags inseridas.

## Usos

1. Coletar múltiplas palavras-chave ou códigos de texto livre sem uma lista predefinida
2. Campos de rotulagem ou categorização onde o conjunto de valores é aberto
3. Qualquer entrada de texto livre com múltiplos valores onde `select_multiple` é muito rígido

## Formato de dados

As tags são armazenadas como uma única string separada por espaços. Por exemplo, se o usuário inserir `malária`, `febre` e `tosse`, o valor armazenado será `malária febre tosse`.

## Suporte de plataforma

Suportado em formulários web.

## Limitações

- Não faz parte da especificação padrão do XLSForm — extensão exclusiva do rtSurvey.
- Como os valores são texto livre, a análise posterior requer divisão de string por espaços.
