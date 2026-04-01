---
title: "Fecha y hora, fecha, hora"
description: "Las preguntas de fecha y hora permiten a los encuestados ingresar tanto la fecha como la hora en un solo campo."
icon: "event"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 226
---

El tipo de pregunta datetime en XLSForms y rtSurvey permite a los encuestados ingresar tanto la fecha como la hora en un solo campo. Este tipo de pregunta es útil cuando necesita capturar un momento específico en el tiempo, incluyendo tanto la fecha como la hora exacta.

## Especificación básica de XLSForm

| type     | name           | label                        |
|----------|----------------|------------------------------|
| datetime | event_datetime | ¿Cuándo ocurrió el evento?   |

Para obtener más detalles sobre el tipo de pregunta datetime básico, consulte la [especificación de XLSForm](https://xlsform.org/en/#question-types).

## Usos

Las preguntas de fecha y hora se usan comúnmente para:

1. Registrar marcas de tiempo de eventos u observaciones
2. Programar citas o reuniones
3. Registrar tiempos de inicio y fin de actividades
4. Capturar momentos precisos para recopilación de datos sensibles al tiempo

## Extensiones de rtSurvey

rtSurvey extiende la funcionalidad de las preguntas de fecha y hora con varias apariencias y opciones de personalización:

### Opciones de apariencia

- `(predeterminado)`: Muestra el calendario y el reloj para seleccionar fecha y hora
- `inline`: Muestra el calendario y el reloj como iconos
- `inline-1line`: Muestra el calendario y el reloj para selección en formato de una sola fila
- `inline-onlyresult`: Muestra el calendario y el reloj como iconos al final de la línea; los iconos desaparecen después de la selección

### Personalización de color

Puede personalizar el color de los iconos de calendario y reloj usando la función `colors()`:

- `inline colors("0099FF")`: Mostrar iconos con color personalizado
- `inline-1line-0000FF`: Mostrar en formato de fila única con color personalizado
- `inline-1line colors("0000FF","FFFF00")`: Mostrar en formato de fila única con múltiples colores personalizados
- `inline-onlyresult colors("0099FF")`: Mostrar iconos que desaparecen después de la selección, con color personalizado

### Formatos personalizados de fecha y hora

rtSurvey permite formatos personalizados de fecha y hora usando sintaxis especial:

- `inline-[%Y-%m-%d %H:%M:%S]`: Ejemplo de formato personalizado (Año-Mes-Día Hora:Minuto:Segundo)
- `inline-[%d/%m/%Y %I:%M %p]`: Ejemplo de formato personalizado (Día/Mes/Año Hora:Minuto AM/PM)

## Ejemplo de uso

He aquí un ejemplo de cómo podría usar una pregunta de fecha y hora en una encuesta:

| type     | name           | label                                    | appearance                    |
|----------|----------------|------------------------------------------|-----------------------------|
| datetime | incident_time  | ¿Cuándo ocurrió el incidente?            | inline-[%d/%m/%Y %I:%M %p]  |

## Mejores prácticas

1. Proporcione instrucciones claras sobre el formato de fecha y hora esperado.
2. Considere usar la apariencia `inline` para una visualización más compacta.
3. Use formatos personalizados cuando necesite componentes o formateo específico de fecha y hora.
4. Sea consciente de las zonas horarias al recopilar datos de fecha y hora en diferentes regiones.

## Limitaciones

- Algunas apariencias o formatos personalizados pueden no ser compatibles con todos los dispositivos o plataformas.
- Los usuarios pueden necesitar orientación sobre cómo ingresar la fecha y la hora correctamente, especialmente con formatos personalizados.
- Las diferencias de zona horaria pueden complicar el análisis de datos si no se tienen en cuenta adecuadamente.
