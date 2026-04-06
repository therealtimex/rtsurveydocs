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

O rtSurvey suporta todos os tipos de perguntas XLSForm padrão, além de várias extensões. Cada tipo de pergunta controla que tipo de dados é recolhido e como o widget de entrada é renderizado no dispositivo.

Para definir o tipo de pergunta, introduza o nome do tipo na coluna `type` da folha de trabalho **survey** no seu XLSForm.

## Entrada de texto

| Tipo | Descrição |
|------|-----------|
| [text](text) | Resposta de texto livre — qualquer carácter permitido |
| [integer](integer) | Número inteiro (sem decimais) |
| [decimal](decimal) | Número com casas decimais |
| [range](range) | Número selecionado a partir de um deslizador dentro de um intervalo mín/máx definido |

## Seleção

| Tipo | Descrição |
|------|-----------|
| [select_one listname](select-one) | Escolher exatamente uma opção de uma lista |
| [select_multiple listname](select-multiple) | Escolher uma ou mais opções de uma lista |
| [select_one_from_file filename](select-one-from-file) | Escolher uma opção carregada a partir de um ficheiro CSV externo |
| [rank listname](rank) | Ordenar escolhas por preferência ou prioridade |

## Data e Hora

| Tipo | Descrição |
|------|-----------|
| [date](date) | Data do calendário (ano, mês, dia) |
| [time](time) | Hora do dia (horas, minutos) |
| [datetime](datetime-date-time) | Data e hora combinadas |

## Localização

| Tipo | Descrição |
|------|-----------|
| [geopoint](geopoint) | Única coordenada GPS (latitude, longitude, altitude, precisão) |
| [geotrace](geotrace) | Um percurso — série de pontos GPS formando uma linha |
| [geoshape](geoshape) | Uma área — polígono fechado de pontos GPS |

## Multimédia

| Tipo | Descrição |
|------|-----------|
| [image](image) | Captura de fotografia ou carregamento de imagem |
| [audio](audio) | Gravação de áudio |
| [video](video) | Gravação de vídeo |
| [file](file) | Carregamento geral de ficheiros (PDF, documento, etc.) |

## Outros

| Tipo | Descrição |
|------|-----------|
| [barcode](barcode) | Digitalizar um código de barras ou código QR |
| [note](note) | Texto de exibição apenas leitura — mostra instruções ou resumos calculados |
| [calculate](calculate) | Campo oculto que armazena um valor calculado |
| [hidden](hidden) | Campo oculto que armazena um valor estático ou pré-preenchido |
| [trigger / acknowledge](trigger) | Uma caixa de verificação que o enumerador deve marcar para confirmar que leu uma declaração |
| [meta](meta) | Metadados automáticos: timestamps, ID do dispositivo, informação do enumerador |

## Como type e appearance funcionam em conjunto

O `type` determina **que dados são recolhidos**. A coluna `appearance` controla **como o widget parece**. Muitos tipos suportam múltiplas aparências — por exemplo `select_one` pode aparecer como botões de rádio, um menu suspenso, uma escala de Likert ou uma grelha compacta.

Consulte [Aparência](../appearance) para a lista completa de opções.
