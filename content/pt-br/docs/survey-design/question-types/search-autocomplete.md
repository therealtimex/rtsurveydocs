---
title: "Search Autocomplete"
description: "Campo de texto com preenchimento automático que pesquisa opções a partir de uma API remota enquanto o usuário digita."
icon: "search"
date: "2026-04-08T00:00:00+00:00"
lastmod: "2026-04-08T00:00:00+00:00"
draft: false
toc: true
weight: 260
---

O tipo de pergunta `search-autocomplete` renderiza uma entrada de texto que consulta uma API remota enquanto o usuário digita e apresenta os resultados correspondentes como um menu suspenso. O valor selecionado é armazenado como uma string de texto. Ao contrário de `select_one` com `search-api()`, o `search-autocomplete` trata o resultado como texto simples — não há lista de opções fixa no XLSForm.

## Especificação básica do XLSForm

| type | name | label | appearance |
|------|------|-------|------------|
| search-autocomplete | facility_name | Pesquisar estabelecimento | `searchApi("/api/facilities", "name")` |

A expressão `searchApi()` é colocada na coluna `appearance` e controla qual endpoint de API é consultado e qual campo da resposta é usado como valor de exibição.

## Sintaxe do `searchApi()`

```
searchApi("url", "display_field")
searchApi("url", "display_field", "value_field")
```

| Parâmetro | Obrigatório | Descrição |
|-----------|-------------|-----------|
| `url` | Sim | URL do endpoint. Adicione parâmetros de consulta com `?q=##QUERY##` — `##QUERY##` é substituído pelo texto digitado em tempo de execução |
| `display_field` | Sim | Nome do campo JSON da resposta da API para mostrar no menu suspenso |
| `value_field` | Não | Nome do campo JSON para armazenar como valor da resposta (padrão é `display_field`) |

### Exemplo: pesquisar estabelecimentos, armazenar o ID do estabelecimento

| type | name | label | appearance |
|------|------|-------|------------|
| search-autocomplete | facility | Nome do estabelecimento | `searchApi("/api/facilities?q=##QUERY##", "name", "id")` |

## Variante: `search-autocomplete-noedit`

A variante `search-autocomplete-noedit` impede o usuário de enviar um valor que não foi selecionado nos resultados de preenchimento automático. O usuário deve escolher da lista.

| type | name | label | appearance |
|------|------|-------|------------|
| search-autocomplete | patient_id | ID do paciente | `search-autocomplete-noedit searchApi("/api/patients?q=##QUERY##", "full_name", "patient_id")` |

## Usos

1. Pesquisar grandes conjuntos de dados de referência (estabelecimentos, funcionários, produtos) sem incorporar todas as opções no XLSForm
2. Campos de texto livre com sugestões opcionais (quando `search-autocomplete-noedit` não é usado)
3. Pesquisas vinculadas onde o valor selecionado preenche outros campos via `calculate`

## Formato de dados

O valor armazenado é uma string simples — o valor retornado por `value_field` ou o texto de exibição se nenhum `value_field` for especificado.

## Suporte de plataforma

Suportado em formulários web. O suporte móvel depende da conectividade de rede com o endpoint da API.

## Limitações

- Requer um endpoint de API acessível pela rede no momento da coleta de dados.
- Não faz parte da especificação padrão do XLSForm — extensão exclusiva do rtSurvey.
- Não suporta cache de opções offline; use `select_one` com `search-api()` se um fallback offline for necessário.
