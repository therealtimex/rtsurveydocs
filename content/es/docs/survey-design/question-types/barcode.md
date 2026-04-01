---
title: "Código de barras"
description: "Las preguntas de código de barras permiten escanear y capturar datos de códigos de barras en su encuesta."
icon: "qr_code_scanner"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 231
---

El tipo de pregunta de código de barras en XLSForms y rtSurvey permite a los usuarios escanear y capturar datos de códigos de barras directamente dentro de la encuesta. Esta función es particularmente útil para la gestión de inventarios, el seguimiento de productos o cualquier escenario donde se requiera una entrada de datos rápida y precisa de información codificada.

## Especificación básica de XLSForm

| type    | name          | label                        |
|---------|---------------|------------------------------|
| barcode | product_code  | Escanee el código de barras del producto |

Para obtener más detalles sobre el tipo de pregunta de código de barras básico, consulte la [especificación de XLSForm](https://xlsform.org/en/#question-types).

## Usos

Las preguntas de código de barras se usan comúnmente para:

1. Identificación de productos en encuestas de inventario
2. Seguimiento de activos en operaciones de campo
3. Verificación de entradas o ID en eventos
4. Entrada rápida de datos de información codificada

## Extensiones de rtSurvey

Si bien la especificación básica de XLSForm para preguntas de código de barras es sencilla, rtSurvey puede ofrecer características o personalizaciones adicionales:

1. Soporte para múltiples formatos de código de barras (p. ej., códigos QR, UPC, EAN)
2. Integración con la cámara del dispositivo para escanear códigos de barras
3. Opción de entrada manual en caso de que el código de barras esté dañado o no pueda escanearse

## Mejores prácticas

1. Asegure condiciones de iluminación adecuadas para un escaneo preciso de códigos de barras.
2. Proporcione instrucciones claras a los usuarios sobre cómo posicionar el dispositivo para escanear.
3. Incluya una opción de entrada manual como respaldo en caso de dificultades de escaneo.
4. Pruebe la función de escaneo de códigos de barras con varios dispositivos y tipos de códigos de barras antes de implementar la encuesta.

## Limitaciones

- La precisión del escaneo de códigos de barras puede variar dependiendo de la calidad de la cámara del dispositivo y las condiciones ambientales.
- Algunos dispositivos más antiguos o de gama baja pueden no admitir el escaneo de códigos de barras.
- Es posible que ciertos tipos de códigos de barras no sean admitidos, dependiendo de la implementación.

## Ejemplo de uso

He aquí un ejemplo de cómo podría usar una pregunta de código de barras en una encuesta de inventario:

| type    | name          | label                        | hint                                          |
|---------|---------------|------------------------------|-----------------------------------------------|
| barcode | product_code  | Escanee el código de barras del producto | Coloque el código de barras dentro del marco |
| integer | quantity      | Ingrese la cantidad del producto |                                           |
| note    | confirmation  | Producto escaneado: ${product_code}. Cantidad: ${quantity} |               |

En este ejemplo, la encuesta captura el código de barras de un producto, solicita la cantidad y luego muestra una nota de confirmación con la información escaneada.
