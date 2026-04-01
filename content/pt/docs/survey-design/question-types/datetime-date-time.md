---
title: "Datetime, date, time"
description: "As perguntas Datetime permitem aos respondentes introduzir data e hora num único campo."
icon: "event"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 226
---

O tipo de pergunta datetime em XLSForms e rtSurvey permite aos respondentes introduzir data e hora num único campo. Este tipo de pergunta é útil quando precisa de capturar um momento específico no tempo, incluindo tanto a data como a hora exata.

## Especificação XLSForm Básica

| type     | name           | label                           |
|----------|----------------|--------------------------------|
| datetime | event_datetime | Quando ocorreu o evento?        |

Para mais detalhes sobre o tipo de pergunta datetime básico, consulte a [especificação XLSForm](https://xlsform.org/en/#question-types).

## Utilizações

As perguntas datetime são comummente usadas para:

1. Registar marcas temporais de eventos ou observações
2. Agendar compromissos ou reuniões
3. Registar horas de início e fim de atividades
4. Capturar momentos precisos para recolha de dados sensíveis ao tempo

## Extensões rtSurvey

O rtSurvey estende a funcionalidade das perguntas datetime com várias opções de aparência e personalização:

### Opções de Aparência

- `(predefinição)`: Exibir o calendário e relógio para selecionar data e hora
- `inline`: Exibir o calendário e relógio como ícones
- `inline-1line`: Exibir o calendário e relógio para seleção num formato de linha única
- `inline-onlyresult`: Exibir o calendário e relógio como ícones no fim da linha; os ícones desaparecem após a seleção

### Personalização de Cores

Pode personalizar a cor dos ícones de calendário e relógio usando a função `colors()`:

- `inline colors("0099FF")`: Exibir ícones com cor personalizada
- `inline-1line-0000FF`: Exibir em formato de linha única com cor personalizada
- `inline-1line colors("0000FF","FFFF00")`: Exibir em formato de linha única com múltiplas cores personalizadas
- `inline-onlyresult colors("0099FF")`: Exibir ícones que desaparecem após a seleção, com cor personalizada

### Formatos de Data e Hora Personalizados

O rtSurvey permite formatos de data e hora personalizados usando sintaxe especial:

- `inline-[%Y-%m-%d %H:%M:%S]`: Exemplo de formato personalizado (Ano-Mês-Dia Hora:Minuto:Segundo)
- `inline-[%d/%m/%Y %I:%M %p]`: Exemplo de formato personalizado (Dia/Mês/Ano Hora:Minuto AM/PM)

## Exemplo de Utilização

Aqui está um exemplo de como pode usar uma pergunta datetime num inquérito:

| type     | name           | label                                      | appearance                    |
|----------|----------------|--------------------------------------------|-----------------------------|
| datetime | incident_time  | Quando ocorreu o incidente?                | inline-[%d/%m/%Y %I:%M %p]  |

## Melhores Práticas

1. Forneça instruções claras sobre o formato esperado de data e hora.
2. Considere usar a aparência `inline` para uma exibição mais compacta.
3. Use formatos personalizados quando precisar de componentes ou formatação específicos de data e hora.
4. Seja cuidadoso com fusos horários ao recolher dados datetime em diferentes regiões.

## Limitações

- Algumas aparências ou formatos personalizados podem não ser suportados em todos os dispositivos ou plataformas.
- Os utilizadores podem precisar de orientação para introduzir data e hora corretamente, especialmente com formatos personalizados.
- As diferenças de fuso horário podem complicar a análise de dados se não forem devidamente consideradas.
