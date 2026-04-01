---
title: "Geotrace"
description: "As perguntas geotrace permitem aos respondentes capturar uma série de pontos conectados num mapa, criando linhas ou percursos como parte do inquérito."
icon: "timeline"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 234
---

O tipo de pergunta geotrace em XLSForms e rtSurvey permite aos respondentes capturar uma série de pontos conectados num mapa, criando linhas ou percursos. Esta funcionalidade é particularmente útil para mapear rotas, fronteiras ou características lineares em inquéritos espaciais.

## Especificação XLSForm Básica

| type     | name        | label                           |
|----------|-------------|--------------------------------|
| geotrace | river_path  | Trace o percurso do rio         |

Para mais detalhes sobre o tipo de pergunta geotrace básico, consulte a [especificação XLSForm](https://xlsform.org/en/#question-types).

## Utilizações

As perguntas geotrace são comummente usadas para:

1. Mapear rotas ou percursos tomados durante inquéritos de campo
2. Traçar características lineares como estradas, rios ou fronteiras
3. Capturar a extensão de infraestrutura linear (por ex., oleodutos, linhas de energia)
4. Registar percursos de viagem em estudos de transporte
5. Definir transectos em inquéritos ecológicos

## Melhores Práticas

1. Certifique-se de que o dispositivo tem os serviços de localização ativados e as permissões concedidas.
2. Forneça instruções claras sobre como traçar o percurso e que características devem ser incluídas.
3. Considere usar imagens de satélite ou mapas base para ajudar os respondentes a traçar percursos com precisão.
4. Esteja ciente da potencial complexidade dos traçados e do seu impacto no tamanho e processamento de dados.

## Exemplo de Utilização

Aqui está um exemplo de como pode usar uma pergunta geotrace num inquérito:

| type     | name           | label                                          | hint                                               |
|----------|----------------|------------------------------------------------|----------------------------------------------------|
| geotrace | hiking_trail   | Trace o percurso da trilha de caminhada        | Comece na entrada da trilha e termine no cume      |

## Extensões rtSurvey

Embora a especificação XLSForm básica para perguntas geotrace seja direta, o rtSurvey pode oferecer funcionalidades ou personalizações adicionais:

1. Integração com mapas offline para áreas remotas
2. Opções para definir o número mínimo e máximo de pontos para o traçado
3. Capacidade de editar ou refinar traçados após o desenho inicial
4. Suporte para traçado automático a intervalos definidos durante o movimento

(Nota: As extensões específicas disponíveis no rtSurvey para perguntas geotrace precisariam de ser confirmadas e detalhadas aqui.)

## Formato de Dados

Os dados de geotrace são tipicamente armazenados como uma cadeia de pares de coordenadas separados por espaços, semelhante ao geoshape mas sem o ponto de fecho:

```
lat1 lon1; lat2 lon2; lat3 lon3; ... latN lonN
```

Por exemplo:
```
38.253094215699576 21.756382658677467; 38.25021274773806 21.756382658677467; 38.25007793942195 21.763892843919166; 38.25290886154963 21.763935759263404
```

## Considerações para Análise

Ao usar perguntas geotrace, considere:

1. Como os dados geográficos serão visualizados e analisados (por ex., software SIG)
2. A potencial necessidade de limpeza ou simplificação de dados de traçados complexos
3. Medidas de privacidade e proteção de dados para o tratamento de dados espaciais detalhados
4. Integração com outras fontes de dados espaciais para análise abrangente

## Limitações

- Traçar percursos precisos em pequenos ecrãs móveis pode ser desafiante.
- Traçados complexos podem requerer capacidade significativa de armazenamento e processamento.
- O uso contínuo de GPS para traçado automático pode esgotar rapidamente a bateria do dispositivo.
- Pode haver preocupações de privacidade associadas à recolha de dados de percursos detalhados.
