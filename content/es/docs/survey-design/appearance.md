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
| `required-but-simplify` | cualquiera | El campo es obligatorio pero su diseño aún es simplificado por el renderizador |
| `embed` | cualquiera | Renderiza el campo en modo de visualización integrado/inline, suprimiendo su envoltorio externo y el contenedor de etiquetas |
| `popup` | select_one, select_multiple | Renderiza la lista de opciones en una superposición popup/modal en lugar de inline |
| `auto-hide-empty` | boxtag, select | Oculta todo el widget de pregunta cuando la lista de opciones está vacía |
| `text-nolabel` | select_one, select_multiple | Oculta la etiqueta de texto para cada opción, mostrando solo el control de entrada |

### Widgets

| Atributo de apariencia | Tipos de pregunta | Descripción |
|----------------------|----------------|-------------|
| `likert` | select_one | Presenta las opciones como una fila de escala Likert (ya en la tabla estándar anterior; confirmado como compatible). |
| `distress` | select_one | Renderiza las opciones como el widget visual de la Escala de angustia psicológica de Kessler (K10) con iconos emocionales. |

### Widgets visuales de selección

Estas apariencias cambian toda la renderización de las listas de opciones de selección.

| Apariencia | Tipos de pregunta | Descripción |
|-----------|------------------|-------------|
| `tagging` | select_one, select_multiple | Las opciones se renderizan como chips de etiqueta clicables con forma de píldora. |
| `boxtag` | select_one, select_multiple | Las opciones se renderizan como cuadros rectangulares con estilo que el usuario toca. |
| `boxtag -search` | select_one, select_multiple | Diseño boxtag con entrada de búsqueda/filtro en vivo sobre los cuadros. |
| `duolingo-style1` | select_one, select_multiple | Diseño de tarjetas grande inspirado en Duolingo — adecuado para listas cortas con iconos. |
| `rating_box` | select_one, select_multiple | Cuadrícula de cuadros numéricos tocables — adecuado para preguntas de escala o NPS. |
| `star_rating` | select_one | Las opciones se renderizan como estrellas; el número de estrellas es igual al número de opciones. |
| `choices-noshow` | select_one, select_multiple | Muestra inicialmente solo las primeras 10 opciones con un control "Mostrar más". |
| `noshow` | select_one, select_multiple | Oculta la lista de opciones completamente; el valor se establece programáticamente via calculate o API. |
| `checkall` | select_multiple | Agrega un acceso directo "Seleccionar todo" al principio de la lista de opciones. |
| `max-items(N)` | select_one, select_multiple | Limita la lista de opciones visible a N elementos. Ejemplo: max-items(5). |

### Widgets visuales de texto

| Apariencia | Tipos de pregunta | Descripción |
|-----------|------------------|-------------|
| `richtext` | text | Reemplaza el cuadro de texto simple con un editor de texto enriquecido (negrita, cursiva, listas, enlaces). Almacena HTML. |
| `typingtest` | text | Widget de prueba de escritura — el texto de la etiqueta es el pasaje; el widget registra la respuesta escrita y el tiempo. |

### Extensiones de medios

| Apariencia | Tipos de pregunta | Descripción |
|-----------|------------------|-------------|
| `watermark("expression")` | image | Superpone una marca de agua de texto en las fotos capturadas. El argumento es una expresión XPath evaluada en el momento de la captura. |
| `editable` | image | Habilita la anotación/dibujo sobre la foto capturada antes de guardar. |

### Configuración de visualización inline

Los modificadores `display{}` y `results{}` controlan la alineación de iconos y la visualización de resultados para widgets inline.

#### Parámetros de `display{}`

| Parámetro | Valores | Descripción |
|-----------|---------|-------------|
| Alineación | `left`, `right`, `top`, `bottom`, `center` | Posición del icono relativa al campo de entrada |
| Tamaño | `small`, `medium`, `large` | Tamaño del icono |
| Modo | `inline-icon` | Renderiza el disparador solo como icono |
| Modo | `inline-button` | Renderiza el disparador como botón completo |

#### Parámetros de `results{}`

| Parámetro | Valores | Descripción |
|-----------|---------|-------------|
| Alineación | `left`, `right`, `top`, `bottom`, `center` | Posición de la visualización del valor del resultado |
| `hide(field)` | cualquier nombre de sub-campo | Oculta un componente específico del resultado |

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
