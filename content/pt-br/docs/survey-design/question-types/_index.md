---
title: "Tipos de perguntas"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 220
---

O rtSurvey suporta todos os tipos de perguntas XLSForm padrão, além de várias extensões. Cada tipo de pergunta controla que tipo de dados são coletados e como o widget de entrada é renderizado no dispositivo.

Para definir o tipo de pergunta, insira o nome do tipo na coluna `type` da planilha **survey** no seu XLSForm.

## Entrada de texto

| Tipo | Descrição |
|------|-----------|
| [text](text) | Resposta de texto livre — qualquer caractere é permitido |
| [integer](integer) | Número inteiro (sem decimais) |
| [decimal](decimal) | Número com casas decimais |
| [range](range) | Número selecionado de um controle deslizante dentro de um intervalo mín/máx definido |

## Seleção

| Tipo | Descrição |
|------|-----------|
| [select_one listname](select-one) | Escolha exatamente uma opção de uma lista |
| [select_multiple listname](select-multiple) | Escolha uma ou mais opções de uma lista |
| [rank listname](rank) | Ordene as opções por preferência ou prioridade |

## Data e hora

| Tipo | Descrição |
|------|-----------|
| [date](date) | Data do calendário (ano, mês, dia) |
| [time](time) | Hora do dia (horas, minutos) |
| [datetime](datetime-date-time) | Data e hora combinadas |

## Localização

| Tipo | Descrição |
|------|-----------|
| [geopoint](geopoint) | Coordenada GPS única (latitude, longitude, altitude, precisão) |
| [geotrace](geotrace) | Um caminho — série de pontos GPS formando uma linha |
| [geoshape](geoshape) | Uma área — polígono fechado de pontos GPS |

## Mídia

| Tipo | Descrição |
|------|-----------|
| [image](image) | Captura de foto ou upload de imagem |
| [audio](audio) | Gravação de áudio |
| [video](video) | Gravação de vídeo |
| [file](file) | Upload de arquivo geral (PDF, documento, etc.) |

## Outros

| Tipo | Descrição |
|------|-----------|
| [barcode](barcode) | Escanear um código de barras ou QR code |
| [note](note) | Texto de exibição somente leitura — mostra instruções ou resumos calculados |
| [calculate](calculate) | Campo oculto que armazena um valor calculado |
| [hidden](hidden) | Campo oculto que armazena um valor estático ou pré-preenchido |
| [trigger / acknowledge](trigger) | Uma caixa de seleção que o entrevistador deve marcar para confirmar que leu uma declaração |
| [meta](meta) | Metadados automáticos: carimbos de tempo, ID do dispositivo, informações do entrevistador |

## Extensões rtSurvey

Esses tipos são específicos do rtSurvey e não fazem parte da especificação XLSForm padrão.

| Tipo | Descrição |
|------|-----------|
| [search-autocomplete](search-autocomplete) | Entrada de texto com sugestões de preenchimento automático em tempo real via API |
| [mentions](mentions) | Campo de texto com preenchimento automático de menções `@` para marcar entidades inline |
| [texttags](texttags) | Entrada de tags — cada entrada se torna um chip removível; armazenado como string separada por espaços |

Para grupos de repetição, consulte [Repeats](../advanced-extension/repeats)

## Como tipo e aparência funcionam juntos

O `type` determina **que dados são coletados**. A coluna `appearance` controla **como o widget parece**. Muitos tipos suportam múltiplas aparências — por exemplo, `select_one` pode aparecer como botões de opção, um menu suspenso, uma escala Likert ou uma grade compacta.

Consulte [Aparência](../appearance) para a lista completa de opções.
