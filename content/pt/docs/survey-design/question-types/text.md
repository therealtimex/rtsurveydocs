---
title: "Texto"
description: "Tipo de pergunta de resposta de texto livre no rtSurvey"
icon: "text_fields"
date: "2024-07-01T12:00:00+01:00"
lastmod: "2024-07-01T12:00:00+01:00"
draft: false
toc: true
weight: 221
---

O tipo de pergunta `text` recolhe uma resposta de texto livre — qualquer cadeia de caracteres. É o tipo de entrada mais flexível e é usado para nomes, endereços, descrições, códigos e qualquer coisa que não se encaixe num tipo mais específico.

O rtSurvey também alarga `text` com **widgets de entrada de hora** que permitem a entrada precisa de hora com um selecionador de relógio.

## Especificação XLSForm Básica

| type | name | label |
|------|------|-------|
| text | respondent_name | Nome completo do respondente |
| text | address | Endereço de casa |

Para mais detalhes sobre o tipo de texto XLSForm padrão, consulte a [especificação XLSForm](https://xlsform.org/en/#question-types).

## Utilizações

As perguntas de texto são usadas para:

1. Nomes, endereços, descrições livres
2. Comentários ou feedback de resposta aberta
3. Códigos, IDs ou números de referência que não se encaixam em integer/decimal
4. Recolher valores de hora com as extensões de entrada de hora do rtSurvey
5. Campos de texto de preenchimento automático (via `search-autocomplete-noedit-v2()`)

## Opções de aparência padrão

| Aparência | Descrição |
|------------|-----------|
| *(nenhuma)* | Entrada de texto de uma única linha |
| `multiline` | Área de texto de múltiplas linhas — melhor para texto livre mais longo na web |
| `richtext` | Editor de texto rico — barra de ferramentas com negrito, itálico, listas e links |
| `typingtest` | Interface de teste de digitação — apresenta uma passagem e mede velocidade e precisão de digitação |

## Extensões de entrada de hora do rtSurvey

O rtSurvey alarga `text` com um **widget de selecionador de relógio** para recolher valores de hora. Estas opções de aparência exibem um ícone de relógio que o enumerador pode tocar para selecionar horas, minutos, segundos ou milissegundos.

### Variantes de aparência

| Aparência | Descrição |
|------------|-----------|
| `inline` | Ícone de relógio exibido ao lado do campo |
| `inline colors("RRGGBB")` | Ícone de relógio com cor hexadecimal personalizada |
| `inline-1line` | Relógio exibido em formato compacto de uma linha |
| `inline-1line-RRGGBB` | Uma linha com cor de ícone personalizada (hex, sem `#`) |
| `inline-1line colors("RRGGBB","RRGGBB")` | Uma linha com duas cores |
| `inline-onlyresult` | O ícone de relógio desaparece após seleção; apenas o valor é mostrado |
| `inline-onlyresult colors("RRGGBB")` | Igual, com cor de ícone personalizada |

### Tokens de formato de hora

Acrescente uma cadeia de formato entre parênteses para controlar quais componentes de hora são mostrados:

| Cadeia de formato | Exibe |
|---------------|----------|
| `inline-[%H:%M]` | Horas e minutos (24 horas) |
| `inline-[%h:%M]` | Horas e minutos (12 horas) |
| `inline-[%H:%M:%S]` | Horas, minutos, segundos (24 horas) |
| `inline-[%h:%M:%S]` | Horas, minutos, segundos (12 horas) |
| `inline-[%H:%M:%3]` | Horas, minutos, milissegundos |
| `inline-[%M:%S]` | Apenas minutos e segundos |
| `inline-[%M:%3]` | Apenas minutos e milissegundos |
| `inline-[%S]` | Apenas segundos |
| `inline-[%3]` | Apenas milissegundos |
| `inline-[%H]` | Apenas horas (24 horas) |
| `inline-[%h]` | Apenas horas (12 horas) |

### Exemplo: Registar a duração de uma tarefa em minutos e segundos

| type | name | label | appearance |
|------|------|-------|------------|
| text | task_duration | Tempo necessário para concluir a tarefa | `inline-[%M:%S]` |

### Exemplo: Registar a hora de um evento em formato 24 horas com cor personalizada

| type | name | label | appearance |
|------|------|-------|------------|
| text | event_time | Hora do evento | `inline-1line colors("0099FF")` |

## Formato de dados

Os dados de texto são armazenados e exportados como uma cadeia simples. Para entradas baseadas em hora usando o widget de relógio inline, o valor é armazenado no formato correspondente à cadeia de formato escolhida (por ex., `14:32` para `%H:%M`).

## Restrições e validação

Aplique restrições para impor formato, comprimento ou padrão:

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| text | name | Nome completo | `string-length(.) >= 2` | O nome deve ter pelo menos 2 caracteres |
| text | code | Código de referência | `regex(., '^[A-Z]{2}[0-9]{4}$')` | Introduza 2 letras maiúsculas seguidas de 4 dígitos |
| text | phone | Número de telefone | `regex(., '^[0-9]{9,15}$')` | Introduza um número de telefone válido |

## Melhores Práticas

1. Use tipos mais específicos (`integer`, `decimal`, `date`) sempre que os dados tiverem uma estrutura conhecida — isto previne entradas inválidas e simplifica a análise.
2. Adicione `constraint` com `string-length()` ou `regex()` para validar códigos ou IDs.
3. Use a aparência `multiline` para perguntas de resposta aberta onde os respondentes possam escrever várias frases.
4. Para recolha de hora, escolha os tokens de formato de hora que correspondem à precisão que a sua análise requer.

## Suporte de plataforma

O tipo de pergunta de texto e todas as aparências de entrada de hora são suportados nas plataformas iOS, Android e web.

## Limitações

- As respostas de texto são de forma livre — não há verificação ortográfica incorporada ou restrição de vocabulário além dos padrões regex.
- O widget de hora inline é uma extensão do rtSurvey e não faz parte da especificação XLSForm padrão.
