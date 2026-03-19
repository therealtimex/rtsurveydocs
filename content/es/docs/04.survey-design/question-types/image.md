---
title: "Imagen"
description: "Las preguntas de imagen permiten a los encuestados capturar y enviar fotos como parte de la encuesta."
icon: "image"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 227
---

El tipo de pregunta de imagen en XLSForms y rtSurvey permite a los encuestados capturar y enviar fotos como parte de sus respuestas a la encuesta. Esta función es particularmente útil para recopilar datos visuales, documentar observaciones o proporcionar evidencia en encuestas de campo.

## Especificación básica de XLSForm

| type  | name        | label                           |
|-------|-------------|----------------------------------|
| image | photo       | Tome una foto de la ubicación    |

Para obtener más detalles sobre el tipo de pregunta de imagen básico, consulte la [especificación de XLSForm](https://xlsform.org/en/#question-types).

## Usos

Las preguntas de imagen se usan comúnmente para:

1. Documentar condiciones o observaciones de campo
2. Capturar evidencia visual en estudios de investigación
3. Recopilar fotos de antes y después en evaluaciones de impacto
4. Verificar la finalización de tareas o la presencia en ubicaciones
5. Recopilar datos visuales para análisis remoto

## Mejores prácticas

1. Proporcione instrucciones claras sobre qué debe fotografiarse.
2. Considere las implicaciones de privacidad e informe a los encuestados sobre cómo se usarán sus fotos.
3. Sea consciente del tamaño de los archivos y las limitaciones de almacenamiento, especialmente para encuestas en áreas con conectividad a internet limitada.
4. Asegúrese de que el dispositivo tenga suficiente espacio de almacenamiento y que los permisos de cámara estén otorgados.

## Ejemplo de uso

He aquí un ejemplo de cómo podría usar una pregunta de imagen en una encuesta:

| type  | name           | label                                      | hint                                               |
|-------|----------------|--------------------------------------------|----------------------------------------------------|
| image | storefront     | Tome una foto de la entrada de la tienda   | Asegúrese de que el nombre de la tienda sea claramente visible |

## Extensiones de rtSurvey

Si bien la especificación básica de XLSForm para preguntas de imagen es sencilla, rtSurvey puede ofrecer características o personalizaciones adicionales:

1. Configuración de calidad de imagen (p. ej., resolución baja, media, alta)
2. Opción para agregar leyendas o etiquetas a las imágenes
3. Captura de múltiples imágenes para una sola pregunta
4. Integración con la aplicación de cámara nativa del dispositivo o la galería

## Manejo de datos

Las imágenes recopiladas a través de este tipo de pregunta típicamente se:

1. Guardan en un formato de imagen común (p. ej., JPG, PNG)
2. Almacenan junto con otros datos de la encuesta, a menudo en una carpeta de medios separada
3. Pueden ver y analizar a través de la plataforma de gestión de encuestas

## Consideraciones para el análisis

Al usar preguntas de imagen, considere:

1. Cómo se analizarán las imágenes (p. ej., revisión manual, análisis de imagen automatizado)
2. El espacio de almacenamiento adicional requerido para archivos de imagen
3. Medidas de privacidad y protección de datos para almacenar y manejar fotos
4. Posible necesidad de herramientas de edición u organización de imágenes en la fase de análisis

## Limitaciones

- Los archivos de imagen pueden ser grandes, lo que puede impactar la transferencia de datos y el almacenamiento.
- No todos los dispositivos pueden tener cámaras de alta calidad o suficiente espacio de almacenamiento.
- Analizar grandes cantidades de imágenes puede ser llevar mucho tiempo.
- Puede haber preocupaciones de privacidad al capturar imágenes, especialmente en espacios públicos.
