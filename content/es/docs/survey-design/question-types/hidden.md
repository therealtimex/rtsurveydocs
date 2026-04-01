---
title: "Oculto"
description: "Los campos ocultos almacenan valores que nunca se muestran al encuestado — se usan para pasar contexto, precargar datos o almacenar resultados intermedios."
icon: "eye-slash"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 239
---

Un campo `hidden` almacena un valor que **nunca se muestra al encuestado**. A diferencia de `calculate` (que calcula un valor), `hidden` se usa para llevar un **valor proporcionado externamente** — por ejemplo, un ID de tarea, un ID de hogar pasado desde otro sistema, o un código del encuestador inyectado cuando se lanza el formulario.

## Especificación básica de XLSForm

| type | name | label |
|------|------|-------|
| hidden | household_id | |

Las etiquetas no son necesarias para los campos ocultos ya que nada se renderiza en pantalla.

## Usos

Los campos ocultos se usan comúnmente para:

1. Pasar un ID preasignado desde el sistema de gestión de encuestas (p. ej., ID de hogar, número de caso, código de tarea)
2. Almacenar la versión del formulario o metadatos de implementación
3. Inyectar configuración específica del encuestador al lanzar el formulario
4. Llevar datos de un formulario padre a un formulario hijo en flujos de trabajo vinculados
5. Almacenar un valor derivado de los parámetros URL cuando el formulario se abre mediante un enlace web

## Establecer un valor predeterminado

El patrón más común es usar `hidden` con una expresión `default` para que el valor se establezca cuando se abre el formulario:

| type | name | default |
|------|------|---------|
| hidden | deployment_code | 'ZONE_A_2024' |
| hidden | form_version | '3.1' |

## Referenciar un campo oculto en cálculos

Los valores ocultos se pueden referenciar como cualquier otro campo usando `${fieldname}`:

| type | name | label | calculation |
|------|------|-------|-------------|
| hidden | zone_code | | |
| calculate | label_prefix | | concat('[', ${zone_code}, '] ') |
| note | intro | ${label_prefix} Bienvenido a la encuesta de hogar | |

## Uso de hidden con precarga / parámetros URL

Al lanzar un formulario web mediante URL, puede pasar parámetros que completen campos ocultos. Esto le permite precargar un ID de hogar o código de tarea sin que el encuestador lo escriba:

```
https://your-server.com/form/FORMID?household_id=H00123&zone_code=NORTH
```

El campo llamado `household_id` se completará automáticamente con `H00123`.

## Mejores prácticas

1. Use `hidden` (no `calculate`) cuando el valor sea **inyectado externamente** y no deba recalcularse.
2. Use `calculate` cuando el valor sea **derivado de otros campos** del formulario.
3. Siempre establezca un `default` si el campo oculto debe tener un valor; un campo oculto sin predeterminado estará vacío.
4. Nombre los campos ocultos claramente para distinguirlos (p. ej., con prefijo `_hidden_` o use una convención de nomenclatura consistente).

## Limitaciones

- Los campos ocultos se incluyen en los datos exportados como cualquier otro campo.
- No se pueden mostrar condicionalmente; siempre están presentes (pero invisibles).
- Si necesita un campo que calcule dinámicamente, use `calculate` en su lugar.
