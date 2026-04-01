---
title: "Geopoint"
description: "As perguntas de geopoint capturam coordenadas geográficas (latitude, longitude, altitude e precisão) como parte da pesquisa."
icon: "location_on"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 232
---

O tipo de pergunta geopoint em XLSForms e rtSurvey permite a coleta de coordenadas geográficas usando o GPS do dispositivo ou outros serviços de localização. Este recurso é particularmente útil para mapear respostas de pesquisa, rastrear atividades de campo ou associar dados a locais específicos.

## Especificação básica do XLSForm

| type     | name        | label                           |
|----------|-------------|--------------------------------|
| geopoint | location    | Registre a localização atual    |

Para mais detalhes sobre o tipo básico de pergunta geopoint, consulte a [especificação do XLSForm](https://xlsform.org/en/#question-types).

## Usos

As perguntas de geopoint são comumente usadas para:

1. Mapear respostas de pesquisa geograficamente
2. Verificar a localização das atividades de campo
3. Rastrear a rota dos entrevistadores
4. Associar dados ambientais ou sociais a locais específicos
5. Calcular distâncias ou áreas em análises geográficas

## Práticas recomendadas

1. Garanta que o dispositivo tenha os serviços de localização habilitados e as permissões concedidas.
2. Permita tempo suficiente para o GPS adquirir um sinal preciso.
3. Considere as implicações de privacidade e informe os respondentes sobre a coleta de dados de localização.
4. Use em conjunto com outros tipos de perguntas para fornecer contexto para os dados de localização.

## Exemplo de uso

Aqui está um exemplo de como você pode usar uma pergunta geopoint em uma pesquisa:

| type     | name           | label                                      | hint                                        |
|----------|----------------|--------------------------------------------|--------------------------------------------|
| geopoint | sample_location| Registre a localização da coleta de amostras | Fique em uma área aberta para melhor sinal de GPS |

## Extensões do rtSurvey

Embora a especificação básica do XLSForm para perguntas geopoint seja direta, o rtSurvey pode oferecer recursos ou personalizações adicionais:

1. Integração de mapa para confirmação visual da localização capturada
2. Configurações de limite de precisão
3. Opção para inserir coordenadas manualmente
4. Integração com mapas offline para áreas remotas

## Formato de dados

Os dados de geopoint são tipicamente armazenados como uma string de quatro valores separados por espaço:

```
latitude longitude altitude accuracy
```

Por exemplo:
```
41.40338 2.17403 30.5 10
```

## Considerações para análise

Ao usar perguntas de geopoint, considere:

1. Como os dados geográficos serão visualizados (por exemplo, software de mapeamento)
2. A precisão das coordenadas coletadas e seu impacto na análise
3. Medidas de privacidade e proteção de dados para manipulação de dados de localização
4. Potencial integração com ferramentas GIS (Sistema de Informação Geográfica)

## Limitações

- A precisão pode variar dependendo do dispositivo e das condições ambientais.
- Os sinais GPS podem ser fracos ou indisponíveis em locais internos ou áreas com obstruções.
- A coleta de dados de localização pode impactar significativamente a vida útil da bateria do dispositivo.
- Pode haver preocupações de privacidade associadas à coleta de dados de localização precisos.
