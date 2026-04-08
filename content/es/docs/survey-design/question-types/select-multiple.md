---
title: "Select_multiple"
description: "Las preguntas select_multiple permiten a los encuestados elegir una o más opciones de una lista predefinida."
icon: "check_box"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 225
---

El tipo de pregunta `select_multiple` muestra una lista donde el encuestado puede seleccionar **una o más opciones**. De forma predeterminada, las opciones se renderizan como casillas de verificación. El valor almacenado es una **lista separada por espacios** de todos los valores de opciones seleccionadas.

## Especificación básica de XLSForm

**Hoja de trabajo survey:**

| type | name | label |
|------|------|-------|
| select_multiple crops | crops_grown | ¿Qué cultivos produce el hogar? |

**Hoja de trabajo choices:**

| list_name | name | label |
|-----------|------|-------|
| crops | maize | Maíz |
| crops | beans | Frijoles |
| crops | rice | Arroz |
| crops | vegetables | Verduras |
| crops | other | Otro |

Para obtener más detalles, consulte la [especificación de XLSForm](https://xlsform.org/en/#question-types).

## Formato de datos almacenados

La columna exportada contiene una lista de valores seleccionados separados por espacios:

```
maize beans vegetables
```

Use la función `selected()` — no `=` — al probar los valores de select_multiple en expresiones (consulte a continuación).

## Usos

Las preguntas select_multiple se usan para:

1. Recopilar múltiples respuestas aplicables (p. ej., fuentes de ingresos, cultivos, síntomas)
2. Elementos de acuerdo tipo casilla de verificación (p. ej., "Seleccione todos los que apliquen")
3. Inventarios de idiomas o habilidades
4. Cualquier pregunta donde múltiples respuestas sean simultáneamente válidas

## Opciones de apariencia

{{< table >}}
| Apariencia | Descripción |
|------------|-------------|
| *(ninguna)* | Casillas de verificación predeterminadas, una por línea |
| `minimal` | Widget de selección múltiple desplegable |
| `compact` | Cuadrícula compacta, columnas se ajustan al ancho de pantalla |
| `compact-N` | Cuadrícula compacta forzada a N columnas |
| `horizontal` | Opciones dispuestas horizontalmente en una fila (web) |
| `horizontal-compact` | Horizontal, espaciado compacto (web) |
| `label` | Muestra solo etiquetas, sin casillas de verificación (use con `list-nolabel`) |
| `list-nolabel` | Muestra solo casillas de verificación, sin etiquetas (use con `label`) |
| `columns(N)` | Mostrar en N columnas (extensión de rtSurvey) |
| `tagging` | Las opciones se renderizan como chips de etiqueta con forma de píldora |
| `boxtag` | Las opciones se renderizan como cuadros rectangulares con estilo |
| `boxtag -search` | Diseño boxtag con entrada de búsqueda/filtro sobre los cuadros |
| `duolingo-style1` | Diseño de tarjetas grande — mejor para listas de opciones cortas |
| `rating_box` | Cuadros de valoración en cuadrícula |
| `choices-noshow` | Muestra las primeras 10 opciones inicialmente; revela el resto a demanda |
| `checkall` | Agrega una opción "Seleccionar todo" al principio de la lista |
| `max-items(N)` | Limita el número de opciones visibles a N |
{{< /table >}}

### Ejemplo: Diseño compacto de 3 columnas

| type | name | label | appearance |
|------|------|-------|------------|
| select_multiple symptoms | symptoms | Seleccione todos los síntomas observados | compact-3 |

## Uso de `selected()` en expresiones

Debido a que el valor almacenado es una cadena separada por espacios, **debe** usar `selected()` para probar si se eligió una opción específica. Usar `=` no funcionará correctamente.

### En `relevant`

Mostrar una pregunta de seguimiento solo si se seleccionó "otro":

| type | name | label | relevant |
|------|------|-------|----------|
| select_multiple crops | crops_grown | ¿Qué cultivos se producen? | |
| text | crops_other | Por favor especifique otros cultivos | `selected(${crops_grown}, 'other')` |

### En `constraint`

Requerir al menos 2 opciones:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple issues | issues | `count-selected(.) >= 2` | Seleccione al menos 2 problemas |

Limitar a un máximo de 3:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple priorities | priorities | `count-selected(.) <= 3` | Seleccione no más de 3 prioridades |

### En `calculate` — unir etiquetas seleccionadas

Combine `selected-at()`, `count-selected()` y `choice-label()` para construir un resumen legible:

| type | name | calculation |
|------|------|-------------|
| calculate | crops_summary | join(', ', ${crops_grown}) |

## Opción "Ninguna de las anteriores" / opción exclusiva

Un patrón común es hacer que una opción sea mutuamente excluyente con todas las demás. Use una `constraint` para hacerlo cumplir:

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| select_multiple issues | issues | Seleccione todos los problemas presentes | `not(selected(., 'none') and count-selected(.) > 1)` | "Ninguno" no puede seleccionarse junto con otras opciones |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| issues | water | Escasez de agua |
| issues | roads | Carreteras deficientes |
| issues | health | Falta de servicios de salud |
| issues | none | Ninguno de los anteriores |

## Conteo y resumen de selecciones

| Función | Ejemplo | Resultado |
|---------|---------|-----------|
| `count-selected(field)` | `count-selected(${crops_grown})` | Número de opciones seleccionadas |
| `selected(field, value)` | `selected(${crops_grown}, 'maize')` | verdadero/falso |
| `selected-at(field, index)` | `selected-at(${crops_grown}, 0)` | Primer valor seleccionado |
| `choice-label(field, value)` | `choice-label(${crops_grown}, 'maize')` | Etiqueta de un valor |

## Mejores prácticas

1. Siempre use `selected()` en `relevant`, `constraint` y `calculate` — nunca `=` o `!=`.
2. Agregue una restricción para limitar el número máximo de selecciones si el diseño de la pregunta lo requiere.
3. Incluya una opción "Ninguno" o "No aplica" cuando cero selecciones sea una respuesta válida.
4. Para listas largas (15+ opciones), use `minimal` (desplegable de selección múltiple) para evitar el desplazamiento excesivo.
5. Exporte datos y use la división de cadenas en su herramienta de análisis; el formato separado por espacios requiere dividir antes de pivotar.

## Limitaciones

- Los valores de select_multiple no se pueden comparar directamente con `=`. Siempre use `selected()`.
- La apariencia compacta puede no renderizarse bien para etiquetas de opciones muy largas.
- Al filtrar opciones con `choice_filter`, el filtrado se aplica a todas las opciones mostradas, igual que con `select_one`.
