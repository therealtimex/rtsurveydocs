---
title: "Decimal"
description: "As perguntas decimais permitem entradas numéricas com partes fracionárias na sua pesquisa."
icon: "calculate"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 223
---

O tipo de pergunta decimal em XLSForms e rtSurvey é usado para coletar respostas numéricas que podem incluir partes fracionárias. Este tipo de pergunta é essencial para reunir dados numéricos precisos, como medidas, preços ou percentuais.

## Especificação básica do XLSForm

| type    | name   | label                    |
|---------|--------|--------------------------|
| decimal | weight | Digite seu peso em kg    |

Para mais detalhes sobre o tipo básico de pergunta decimal, consulte a [especificação do XLSForm](https://xlsform.org/en/#question-types).

## Usos

As perguntas decimais são comumente usadas para:

1. Medidas (por exemplo, peso, altura, distância)
2. Dados financeiros (por exemplo, preços, salários)
3. Percentuais
4. Coleta de dados científicos
5. Quaisquer dados numéricos que requeiram precisão além de números inteiros

## Práticas recomendadas

1. Use rótulos claros e concisos para especificar a entrada esperada e a unidade de medida.
2. Implemente restrições de intervalo para evitar entradas não realistas ou errôneas.
3. Considere usar texto de dica para fornecer exemplos ou esclarecer o formato esperado.
4. Especifique o número desejado de casas decimais no rótulo ou dica se a precisão for importante.

## Restrições e validação

Você pode adicionar restrições para garantir que o valor inserido esteja dentro de um intervalo específico:

| type    | name   | label                    | constraint        | constraint_message                    |
|---------|--------|--------------------------|-------------------|---------------------------------------|
| decimal | height | Digite sua altura em metros | .>0 and .<=3    | A altura deve estar entre 0 e 3 metros |

## Exemplo de uso

Aqui está um exemplo de como você pode usar perguntas decimais em uma pesquisa de saúde:

| type    | name           | label                                     | constraint | constraint_message                |
|---------|----------------|-------------------------------------------|------------|-----------------------------------|
| decimal | weight         | Digite seu peso em kg                     | .>0 and .<=500 | O peso deve estar entre 0 e 500 kg |
| decimal | height         | Digite sua altura em metros               | .>0 and .<=3 | A altura deve estar entre 0 e 3 metros |
| decimal | body_temp      | Digite sua temperatura corporal em Celsius | .>=35 and .<=42 | A temperatura deve estar entre 35°C e 42°C |
| calculate | bmi          |                                           |            |                                   |

Na linha de cálculo para IMC, você pode usar:

```
calculation | ${weight} / (${height} * ${height})
```

Isso calculará o IMC usando o peso e a altura inseridos.

## Extensões do rtSurvey

Embora a especificação básica do XLSForm para perguntas decimais seja direta, o rtSurvey pode oferecer recursos ou personalizações adicionais:

1. Controle de precisão (número de casas decimais)
2. Formatos de entrada personalizados (por exemplo, percentual, moeda)
3. Regras de validação avançadas

## Limitações

- A precisão de números decimais pode ser limitada pelo sistema ou banco de dados subjacente.
- Os usuários podem precisar de orientação sobre o separador decimal esperado (ponto ou vírgula) dependendo de sua localidade.
- Números decimais grandes podem ser difíceis de ler ou inserir com precisão em dispositivos móveis.
