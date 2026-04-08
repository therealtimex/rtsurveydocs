---
title: "Select_one"
description: "Las preguntas select_one permiten a los encuestados elegir exactamente una opción de una lista predefinida de opciones."
icon: "radio_button_checked"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 224
---

El tipo de pregunta `select_one` solicita al encuestado que elija **exactamente una opción** de una lista predefinida. De forma predeterminada, las opciones se renderizan como botones de radio, pero hay una amplia gama de opciones de apariencia disponibles para cambiar el diseño y el comportamiento.

## Especificación básica de XLSForm

**Hoja de trabajo survey:**

| type | name | label |
|------|------|-------|
| select_one yesno | consent | ¿El encuestado dio su consentimiento? |

**Hoja de trabajo choices:**

| list_name | name | label |
|-----------|------|-------|
| yesno | yes | Sí |
| yesno | no | No |

El `listname` en `select_one listname` debe coincidir con la columna `list_name` en la hoja de trabajo choices.

Para obtener más detalles, consulte la [especificación de XLSForm](https://xlsform.org/en/#question-types).

## Usos

Las preguntas select_one se usan para:

1. Preguntas de Sí/No
2. Opción múltiple de respuesta única (p. ej., nivel educativo, género, estado civil)
3. Calificaciones categóricas (p. ej., deficiente / regular / bueno / excelente)
4. Selecciones en cascada (vinculadas) donde las opciones se filtran según una respuesta anterior
5. Selección de país, región, distrito u otra unidad administrativa

## Opciones de apariencia

Especifique un valor en la columna `appearance` para cambiar cómo se muestran las opciones:

{{< table >}}
| Apariencia | Descripción |
|------------|-------------|
| *(ninguna)* | Botones de radio predeterminados, uno por línea |
| `minimal` | Menú desplegable/spinner único en lugar de botones de radio |
| `quick` | Avanza automáticamente a la siguiente pregunta inmediatamente después de la selección (solo móvil) |
| `compact` | Cuadrícula compacta de opciones — el número de columnas se ajusta al ancho de la pantalla |
| `compact-N` | Cuadrícula compacta forzada a N columnas (p. ej., `compact-3`) |
| `quickcompact` | Combina `quick` y `compact` |
| `quickcompact-N` | Combina `quick` y `compact` con N columnas forzadas |
| `horizontal` | Opciones organizadas en una fila horizontal (web) |
| `horizontal-compact` | Horizontal, espaciado compacto (web) |
| `likert` | Fila de escala Likert — etiquetas arriba, botones de radio abajo |
| `label` | Muestra solo etiquetas de opciones sin entradas (use en par con `list-nolabel`) |
| `list-nolabel` | Muestra solo las entradas sin etiquetas (use en par con `label`) |
| `columns(N)` | Mostrar en N columnas (extensión de rtSurvey, p. ej., `columns(3)`) |
| `distress` | Widget de iconos emocionales de angustia psicológica de Kessler (K10) |
| `search-api(...)` | Búsqueda dinámica — carga opciones desde una API en tiempo de ejecución |
| `tagging` | Muestra las opciones como chips de etiqueta clicables en lugar de botones de radio |
| `boxtag` | Muestra las opciones como cuadros rectangulares con estilo que el usuario toca para seleccionar |
| `boxtag -search` | Diseño boxtag con entrada de búsqueda/filtro sobre los cuadros |
| `duolingo-style1` | Diseño de tarjetas inspirado en Duolingo — tarjetas grandes tocables con iconos |
| `rating_box` | Cuadros de valoración en cuadrícula — mejor para opciones numéricas o de escala |
| `star_rating` | Widget de valoración por estrellas — las opciones se renderizan como 1–N estrellas |
| `choices-noshow` | Muestra solo las primeras 10 opciones inicialmente; revela el resto a demanda |
| `noshow` | Oculta la lista de opciones completamente; el valor se establece programáticamente |
| `checkall` | Agrega una opción "Seleccionar todo" al principio de la lista |
| `max-items(N)` | Limita el número de opciones visibles a N (p. ej., max-items(5)) |
{{< /table >}}

### Ejemplo: Escala Likert

| type | name | label | appearance |
|------|------|-------|------------|
| select_one satisfaction | service_rating | ¿Qué tan satisfecho está con el servicio? | likert |

### Ejemplo: Compacto en 3 columnas

| type | name | label | appearance |
|------|------|-------|------------|
| select_one regions | region | Seleccionar región | compact-3 |

## Selecciones en cascada

Una selección en cascada (vinculada) filtra las opciones según el valor seleccionado en una pregunta anterior. Use la columna `choice_filter` con el nombre de una columna de su hoja de trabajo choices.

**survey:**

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one province | province | Seleccionar provincia | |
| select_one district | district | Seleccionar distrito | province_name = ${province} |

**choices:**

| list_name | name | label | province_name |
|-----------|------|-------|---------------|
| province | nairobi | Nairobi | |
| province | mombasa | Mombasa | |
| district | westlands | Westlands | nairobi |
| district | kasarani | Kasarani | nairobi |
| district | nyali | Nyali | mombasa |
| district | likoni | Likoni | mombasa |

Cuando el encuestado selecciona `nairobi`, solo `Westlands` y `Kasarani` aparecen en la lista de distritos.

{{% alert icon=" " context="warning" %}}
El nombre de columna usado en `choice_filter` (p. ej., `province_name`) debe existir en la hoja de trabajo choices. El `${province}` referencia el campo de encuesta llamado `province`.
{{% /alert %}}

## Uso del valor seleccionado en expresiones

Referencie el **valor** seleccionado (no la etiqueta) con `${fieldname}`:

```
relevant: ${consent} = 'yes'
```

Para obtener la etiqueta de la opción en lugar del valor, use `choice-label()`:

```
calculate: choice-label(${education_level}, ${education_level})
```

## Opción "Otro" con texto libre

Un patrón común es incluir una opción "otro" que revela un campo de texto:

| type | name | label | relevant |
|------|------|-------|----------|
| select_one occupation | job | ¿Cuál es su ocupación? | |
| text | job_other | Por favor especifique | `${job} = 'other'` |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| occupation | farmer | Agricultor |
| occupation | trader | Comerciante |
| occupation | student | Estudiante |
| occupation | other | Otro (por favor especifique) |

## Mejores prácticas

1. Mantenga las listas cortas y mutuamente excluyentes; si los encuestados pueden querer más de una, use `select_multiple`.
2. Ponga la respuesta más común primero, u ordene alfabéticamente para listas largas.
3. Incluya siempre una opción "No sé" o "Prefiero no responder" donde sea relevante.
4. Use `minimal` (desplegable) para listas con más de 7–8 opciones en móvil para ahorrar espacio en pantalla.
5. Para selecciones en cascada, agregue todas las columnas de filtro en la hoja de trabajo choices antes de construir el formulario.

## Limitaciones

- Un encuestado solo puede seleccionar una opción; use `select_multiple` para preguntas de múltiples respuestas.
- La apariencia `likert` funciona mejor con 5–7 opciones que caben en una línea.
- El avance automático `quick` es solo para móvil; no tiene efecto en formularios web.
