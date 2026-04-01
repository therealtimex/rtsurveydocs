---
title: "Geotrace"
description: "As perguntas de geotrace permitem que os respondentes capturem uma série de pontos conectados em um mapa, criando linhas ou caminhos como parte da pesquisa."
icon: "timeline"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 234
---

O tipo de pergunta geotrace em XLSForms e rtSurvey permite que os respondentes capturem uma série de pontos conectados em um mapa, criando linhas ou caminhos. Este recurso é particularmente útil para mapear rotas, limites ou características lineares em pesquisas espaciais.

## Especificação básica do XLSForm

| type     | name        | label                           |
|----------|-------------|--------------------------------|
| geotrace | river_path  | Trace o caminho do rio          |

Para mais detalhes sobre o tipo básico de pergunta geotrace, consulte a [especificação do XLSForm](https://xlsform.org/en/#question-types).

## Usos

As perguntas de geotrace são comumente usadas para:

1. Mapeamento de rotas ou caminhos percorridos durante pesquisas de campo
2. Rastreamento de características lineares como estradas, rios ou limites
3. Captura da extensão de infraestrutura linear (por exemplo, oleodutos, linhas de energia)
4. Registro de caminhos de viagem em estudos de transporte
5. Definição de transectos em pesquisas ecológicas

## Práticas recomendadas

1. Garanta que o dispositivo tenha os serviços de localização habilitados e as permissões concedidas.
2. Forneça instruções claras sobre como traçar o caminho e quais características devem ser incluídas.
3. Considere usar imagens de satélite ou mapas base para ajudar os respondentes a traçar caminhos com precisão.
4. Esteja ciente da complexidade potencial dos traços e seu impacto no tamanho e processamento dos dados.

## Exemplo de uso

Aqui está um exemplo de como você pode usar uma pergunta geotrace em uma pesquisa:

| type     | name           | label                                      | hint                                        |
|----------|----------------|--------------------------------------------|--------------------------------------------|
| geotrace | hiking_trail   | Trace o caminho da trilha de caminhada      | Comece na entrada da trilha e termine no cume |

## Extensões do rtSurvey

Embora a especificação básica do XLSForm para perguntas geotrace seja direta, o rtSurvey pode oferecer recursos ou personalizações adicionais:

1. Integração com mapas offline para áreas remotas
2. Opções para definir número mínimo e máximo de pontos para o traço
3. Capacidade de editar ou refinar traços após o desenho inicial
4. Suporte para rastreamento automático em intervalos definidos durante o movimento

## Formato de dados

Os dados de geotrace são tipicamente armazenados como uma string de pares de coordenadas separados por espaço, semelhante ao geoshape, mas sem o ponto de fechamento:

```
lat1 lon1; lat2 lon2; lat3 lon3; ... latN lonN
```

Por exemplo:
```
38.253094215699576 21.756382658677467; 38.25021274773806 21.756382658677467; 38.25007793942195 21.763892843919166; 38.25290886154963 21.763935759263404
```

## Considerações para análise

Ao usar perguntas de geotrace, considere:

1. Como os dados geográficos serão visualizados e analisados (por exemplo, software GIS)
2. A possível necessidade de limpeza ou simplificação de dados de traços complexos
3. Medidas de privacidade e proteção de dados para manipulação de dados espaciais detalhados
4. Integração com outras fontes de dados espaciais para análise abrangente

## Limitações

- Traçar caminhos precisos em telas de celulares pequenas pode ser desafiador.
- Traços complexos podem requerer capacidade significativa de armazenamento e processamento.
- O uso contínuo do GPS para rastreamento automático pode rapidamente drenar as baterias dos dispositivos.
- Pode haver preocupações de privacidade associadas à coleta de dados detalhados de caminho.
