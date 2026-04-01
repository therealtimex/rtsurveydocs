---
title: "Tipo de pregunta dinámico"
description: "El tipo de pregunta dinámico permite que el tipo de pregunta y el widget de un campo se determinen en tiempo de ejecución según una respuesta de API o un valor calculado."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 301
---

La función **Tipo de pregunta dinámico** permite que el widget de entrada y el comportamiento de validación de un campo se determinen **en tiempo de ejecución** en lugar de en el momento del diseño del formulario. Esta es una extensión avanzada de rtSurvey que se utiliza cuando el tipo de datos a recopilar depende de una configuración del servidor, una respuesta de API o el valor de un campo anterior.

Un caso de uso común es una lista de verificación de inspección configurable en la que el servidor define qué campos son necesarios, de qué tipo son (texto, entero, selección, etc.) y qué opciones están disponibles, sin necesidad de reconstruir el formulario para cada configuración.

---

## Cómo funciona

Un campo marcado como tipo de pregunta dinámico utiliza `callapi()` para obtener su configuración desde una API. La respuesta de la API define:

- El tipo de entrada a renderizar (text, integer, select_one, etc.)
- Las opciones disponibles (para tipos de selección)
- Las reglas de validación

El campo se marca internamente con `specialFeature: isDynamicQuestionType`, lo que indica al motor del formulario que use la respuesta de la API para construir el widget en lugar de la definición estática del formulario.

---

## Configuración

### Paso 1: Obtener la configuración del campo

Use un campo `calculate` con `callapi()` para recuperar la configuración dinámica:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | field_config | | callapi | `callapi('POST', 'https://api.example.com/field-config', 1, 2, 0, '$.config', 10000, 0, '', '', '{"form_id": "##form_id##", "field_id": "inspection_result"}')` |

### Paso 2: Referenciar la configuración en el campo dinámico

El campo dinámico usa `callapi-verify()` en su `appearance` o `constraint` para vincularse con la configuración obtenida:

| type | name | label | appearance |
|------|------|-------|------------|
| text | inspection_result | Resultado de la inspección | `callapi-verify(dynamicParams)` |

El motor del formulario lee `field_config` y determina dinámicamente si renderizar `inspection_result` como un campo `text`, `integer` o `select_one`.

---

## Formato de respuesta de la API

La API debe devolver un objeto JSON que describa la configuración del campo. Una respuesta típica:

```json
{
  "config": {
    "type": "select_one",
    "choices": [
      {"value": "pass", "label": "Aprobado"},
      {"value": "fail", "label": "Reprobado"},
      {"value": "na", "label": "N/A"}
    ],
    "required": true,
    "constraint": ". != ''"
  }
}
```

---

## Ejemplo: Formulario de inspección configurable

Un formulario de inspección donde los elementos de la lista de verificación y sus tipos de respuesta se obtienen de un servidor según la categoría de inspección:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| select_one inspection_type | insp_type | Tipo de inspección | | |
| calculate | checklist_config | | callapi | `callapi('POST', 'https://api.example.com/checklist', 1, 2, 0, '$.items', 10000, 0, '', '', '{"type": "##insp_type##"}')` |
| text | item_1 | Elemento 1 | `callapi-verify(dynamicParams)` | |
| text | item_2 | Elemento 2 | `callapi-verify(dynamicParams)` | |
| text | item_3 | Elemento 3 | `callapi-verify(dynamicParams)` | |

El servidor devuelve el tipo de widget correcto, la etiqueta, las opciones y la validación para cada elemento según `insp_type`.

---

## Mejores prácticas

1. Use tipos de preguntas dinámicos solo cuando la estructura del campo varíe genuinamente en tiempo de ejecución; para formularios estáticos, use tipos de preguntas estándar.
2. Asegúrese de que la API de configuración responda rápidamente (menos de 2 segundos) y esté disponible en la red del campo.
3. Siempre defina un respaldo razonable en el formulario para el caso en que la API no esté disponible: un campo `text` simple con una nota es mejor que un widget roto.
4. Versione el esquema de respuesta de su API; los cambios en el formato de respuesta afectarán todos los formularios activos que usen ese endpoint.
5. Pruebe cada combinación de tipos de campo que la API pueda devolver antes de la implementación.

## Limitaciones

- Los tipos de preguntas dinámicos requieren conectividad de red para obtener la configuración.
- La gama completa de tipos de widget disponibles dinámicamente depende de la versión del cliente rtSurvey; pruebe su versión de destino.
- Esta es una extensión avanzada de rtSurvey sin equivalente en la especificación estándar de XLSForm.
- Los errores de depuración son más difíciles de rastrear ya que la definición del campo vive en parte en el formulario y en parte en la respuesta de la API.
