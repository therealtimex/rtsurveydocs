---
title: "Apariencia"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

La columna `appearance` en rtSurvey le permite personalizar la presentación visual y el comportamiento de las preguntas en sus encuestas. Esta función mejora la experiencia del usuario y puede mejorar significativamente la eficiencia de la recopilación de datos. rtSurvey admite atributos de apariencia estándar de XLSForm y los amplía con opciones adicionales.

## Atributos de apariencia estándar de XLSForm

rtSurvey admite los siguientes atributos de apariencia estándar de XLSForm:

| Atributo de apariencia | Tipos de pregunta | Descripción |
|----------------------|----------------|-------------|
| multiline | text | Crea un cuadro de texto multilínea (mejor para clientes web) |
| minimal | select_one, select_multiple | Muestra las opciones en un menú desplegable |
| quick | select_one | Avanza automáticamente a la siguiente pregunta después de la selección (solo móvil) |
| no-calendar | date | Suprime la visualización del calendario (solo móvil) |
| month-year | date | Permite la selección de mes y año solamente |
| year | date | Permite la selección de año solamente |
| horizontal-compact | select_one, select_multiple | Muestra las opciones horizontalmente (solo web) |
| horizontal | select_one, select_multiple | Muestra las opciones horizontalmente en columnas (solo web) |
| likert | select_one | Presenta las opciones como una escala Likert |
| compact | select_one, select_multiple | Muestra las opciones una al lado de la otra con relleno mínimo |
| quickcompact | select_one | Combina la visualización compacta con el avance automático (solo móvil) |
| field-list | groups | Muestra todo el grupo en una pantalla (solo móvil) |
| label | select_one, select_multiple | Muestra las etiquetas de opciones sin entradas |
| list-nolabel | select_one, select_multiple | Muestra las entradas sin etiquetas (usar con `label`) |
| table-list | groups | Muestra las preguntas en formato de tabla |
| signature | image | Habilita la captura de firma (solo móvil) |
| draw | image | Permite el dibujo a mano alzada (solo móvil) |
| map, quick map | select_one, select_one_from_file | Habilita la selección desde características del mapa |

## Mejores prácticas para usar la apariencia

1. **Coherencia**: Use los atributos de apariencia de forma coherente en toda su encuesta para una apariencia uniforme.
2. **Móvil vs. Web**: Considere cómo se renderizarán las apariencias en diferentes dispositivos y plataformas.
3. **Rendimiento**: Tenga cuidado con los atributos de apariencia que podrían ralentizar la carga del formulario (p. ej., `table-list` para grupos grandes).
4. **Experiencia del usuario**: Elija apariencias que faciliten la entrada de datos y sean más intuitivas para los encuestados.
5. **Pruebas**: Pruebe siempre su formulario en los dispositivos de destino para asegurarse de que las apariencias funcionen como se espera.

## Técnicas avanzadas

### Combinar apariencias

Algunos atributos de apariencia pueden combinarse para diseños más complejos:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Seleccione uno: | minimal compact |
```

### Apariencias dinámicas

rtSurvey permite cambios dinámicos de apariencia basados en la lógica del formulario:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Ingrese la hora: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Consideraciones sobre la aplicación móvil

- Algunas apariencias (p. ej., `quick`, `signature`) son específicas para dispositivos móviles.
- Pruebe exhaustivamente tanto en Android como en iOS para garantizar un comportamiento coherente.

## Atributos de apariencia extendida de rtSurvey

Además de las apariencias estándar de XLSForm, rtSurvey admite las siguientes opciones específicas de la plataforma:

### Control de datos y visualización

| Atributo de apariencia | Tipos de pregunta | Descripción |
|----------------------|----------------|-------------|
| `invisible` | cualquiera | Oculta el campo de la vista mientras aún recopila o calcula su valor. Diferente del tipo `hidden` — el campo aún participa en la lógica. |
| `displaytitle` | cualquiera | Fuerza la visualización de la etiqueta/título del campo incluso cuando de otro modo estaría suprimido. |
| `autopull` | select_one, select_multiple | Obtiene automáticamente datos externos para llenar las opciones cuando el formulario se carga o un campo disparador cambia. |
| `floating_hint` | text, integer, decimal | Muestra el texto de sugerencia como una etiqueta flotante encima del campo de entrada en lugar de debajo. |
| `calculate-button` | calculate | Agrega un botón visible que activa el recálculo del campo a demanda, en lugar de calcularse automáticamente. |

### Diseño

| Atributo de apariencia | Tipos de pregunta | Descripción |
|----------------------|----------------|-------------|
| `1screen` | group | Fuerza a que todo el grupo se muestre en una sola pantalla independientemente del tamaño del grupo. |
| `columns(n)` | select_one, select_multiple | Muestra las opciones en `n` columnas. Ejemplo: `columns(3)` muestra tres columnas de botones de radio. |
| `gridformat<row=R col=C colspan=S align=center>` | cualquiera | Posiciona el campo en un diseño de cuadrícula CSS en la fila `R`, columna `C`, abarcando `S` columnas. Se usa con `advanced-extension/grid-layout`. |
| `ignore-simplify` | cualquiera | Instruye al renderizador de formularios a omitir la simplificación o condensación automática del diseño de este campo. |

### Widgets

| Atributo de apariencia | Tipos de pregunta | Descripción |
|----------------------|----------------|-------------|
| `likert` | select_one | Presenta las opciones como una fila de escala Likert (ya en la tabla estándar anterior; confirmado como compatible). |
| `distress` | select_one | Renderiza las opciones como el widget visual de la Escala de angustia psicológica de Kessler (K10) con iconos emocionales. |

### Integración de API

| Atributo de apariencia | Tipos de pregunta | Descripción |
|----------------------|----------------|-------------|
| `callapi` | text, integer, decimal, select_one | Habilita la integración de llamada a API para este campo. La columna de cálculo debe contener una expresión `callapi()`. Consulte [Call API](advanced-extension/call-api). |
| `callapi-verify(params)` | text, integer, decimal | Activa una llamada de verificación de API usando parámetros estáticos. El formulario bloquea el progreso hasta que la API confirme el valor. |
| `callapi-verify(dynamicParams)` | text, integer, decimal | Igual que `callapi-verify` pero con parámetros derivados de otros valores de campo en tiempo de ejecución. |

### Formato de fecha/hora en línea

Para campos `date`, `time` y `datetime`, puede especificar un formato de visualización personalizado usando una cadena de formato anexada a la apariencia:

```
inline-[%d/%m/%Y]
inline-1line-[%d/%m/%Y %H:%M]
```

Los tokens de formato son los mismos que `format-date()` y `format-date-time()`. Consulte [Funciones — Funciones de fecha y hora](operators-and-functions/functions#date-and-time-functions).

Ejemplo:

| type | name | label | appearance |
|------|------|-------|------------|
| datetime | event_time | Fecha y hora del evento | inline-[%d/%m/%Y %I:%M %p] |
| date | birth_date | Fecha de nacimiento | inline-[%d/%m/%Y] |

## Limitaciones conocidas

- Las apariencias complejas pueden no renderizarse de forma idéntica en todas las plataformas.
- Algunas apariencias avanzadas de rtSurvey pueden no estar disponibles en el modo sin conexión.

## Solución de problemas de apariencia

1. **Apariencia no aplicada**: Verifique si hay errores tipográficos en la columna de apariencia.
2. **Renderización inconsistente**: Verifique la compatibilidad con el tipo de pregunta y la plataforma.
3. **Problemas de rendimiento**: Considere simplificar las apariencias complejas, especialmente para encuestas grandes.
