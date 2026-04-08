---
title: "Mentions"
description: "Campo de texto com preenchimento automático de menções @ para marcar usuários ou entidades inline."
icon: "alternate_email"
date: "2026-04-08T00:00:00+00:00"
lastmod: "2026-04-08T00:00:00+00:00"
draft: false
toc: true
weight: 262
---

O tipo de pergunta `mentions` é uma entrada de texto que ativa um menu suspenso de preenchimento automático quando o usuário digita `@`. É usado para marcar usuários, nomes de funcionários, códigos ou qualquer entidade inline em uma resposta de texto livre.

## Especificação básica do XLSForm

| type | name | label |
|------|------|-------|
| mentions | note_text | Digite notas de observação (use @ para marcar um membro da equipe) |

## Comportamento

- A digitação normal produz texto comum.
- Digitar `@` seguido de caracteres aciona uma pesquisa de preenchimento automático em uma lista configurada ou API.
- Selecionar uma sugestão insere o token de menção no texto.
- O valor armazenado é a string de texto completa, incluindo quaisquer tokens de menção incorporados.

## Usos

1. Notas qualitativas que fazem referência a membros específicos da equipe ou entidades por nome
2. Registros de observação onde várias pessoas ou locais precisam ser marcados
3. Qualquer campo de texto livre onde referências inline controladas melhoram a análise posterior

## Suporte de plataforma

Suportado em formulários web.

## Limitações

- Não faz parte da especificação padrão do XLSForm — extensão exclusiva do rtSurvey.
- A fonte da lista de menções (estática ou orientada por API) é configurada no nível do servidor, não no XLSForm.
