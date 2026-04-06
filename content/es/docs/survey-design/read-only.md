---
title: "Solo lectura"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 287
---

Los campos de solo lectura en rtSurvey le permiten mostrar información que el encuestado no puede editar. Esta función es particularmente útil para mostrar datos pre-llenados, resultados calculados o información que debe permanecer constante durante la encuesta.

## Uso básico

Para hacer que un campo sea de solo lectura, use la columna `read_only` en su XLSForm:

```
| type    | name | label                 | read_only | default |
|---------|------|----------------------|-----------|---------|
| integer | num  | El número del paciente es: | yes  | 5       |
```

En este ejemplo, el número del paciente se establece en 5 y el encuestado no puede cambiarlo.

## Combinación de solo lectura con valores predeterminados

Los campos de solo lectura a menudo se usan junto con valores predeterminados para mostrar información predeterminada o calculada:

```
| type    | name     | label               | read_only | default        |
|---------|----------|---------------------|-----------|----------------|
| text    | username | Usuario conectado:  | yes       | ${current_user}|
| date    | today    | Fecha de hoy:       | yes       | today()        |
```

Aquí, el nombre de usuario y la fecha actual se muestran pero no se pueden editar.

## Características específicas de rtSurvey

### Solo lectura condicional

rtSurvey amplía la funcionalidad de solo lectura con lógica condicional:

```
| type    | name     | label           | read_only                |
|---------|----------|-----------------|--------------------------|
| integer | age      | Edad:           | ${role} = 'viewer'       |
| text    | comments | Comentarios:    | selected(${status}, 'closed') |
```

En estos ejemplos:
- El campo 'age' es de solo lectura solo si el rol del usuario es 'viewer'.
- El campo 'comments' se vuelve de solo lectura si el estado es 'closed'.

### Estado de solo lectura dinámico

rtSurvey le permite cambiar el estado de solo lectura dinámicamente:

```
| type      | name     | label    | read_only              |
|-----------|----------|----------| ----------------------|
| text      | address  | Dirección: | ${edit_mode} = 'false' |
```

Esto le permite cambiar entre modos editables y de solo lectura según ciertas condiciones o acciones del usuario.

## Mejores prácticas para usar campos de solo lectura

1. **Claridad**: Indique claramente qué campos son de solo lectura a través de señales visuales o etiquetas.
2. **Coherencia**: Use campos de solo lectura de forma coherente en toda su encuesta.
3. **Validación**: Aunque los campos de solo lectura no se pueden editar, inclúyalos en su proceso de validación de datos.
4. **Rendimiento**: Tenga cuidado con los cálculos complejos en campos de solo lectura, ya que pueden afectar el tiempo de carga del formulario.
5. **Accesibilidad**: Asegúrese de que los campos de solo lectura estén correctamente marcados para los lectores de pantalla.

## Técnicas avanzadas

### Campos de solo lectura calculados

Use campos de solo lectura para mostrar cálculos basados en otras respuestas:

```
| type      | name     | label           | read_only | calculation            |
|-----------|----------|-----------------|-----------|------------------------|
| calculate | bmi      | IMC:            | yes       | ${weight} / (${height} * ${height}) |
```

### Visualización de datos históricos

Los campos de solo lectura pueden mostrar datos de encuestas anteriores o fuentes externas:

```
| type    | name           | label                  | read_only | default                    |
|---------|----------------|------------------------|-----------|----------------------------|
| text    | last_visit_date| Fecha de la última visita: | yes  | ${pulldata('visits', 'date', 'id', ${patient_id})} |
```

## Consideraciones de gestión de datos

- Los campos de solo lectura se incluyen en las exportaciones de datos, generalmente con una bandera que indica su estado de solo lectura.
- Al actualizar registros existentes, los campos de solo lectura conservan sus valores originales a menos que se sobrescriban explícitamente a través del backend.

## Comportamiento de la aplicación móvil

- La aplicación móvil rtSurvey respeta la configuración de solo lectura, incluida la lógica de solo lectura condicional.
- El modo sin conexión admite completamente la funcionalidad de solo lectura, incluidos los campos dinámicos y calculados de solo lectura.

## Limitaciones conocidas

- Algunas condiciones dinámicas de solo lectura complejas pueden tener un ligero impacto en el rendimiento en dispositivos de gama baja.
- Los campos de solo lectura pueden no prevenir todas las formas de manipulación de datos en los archivos de datos exportados, por lo que se recomienda la validación del lado del servidor para datos críticos.

## Solución de problemas de campos de solo lectura

1. **Campo inesperadamente editable**: Verifique si hay errores de sintaxis en la columna `read_only` o en la lógica condicional.
2. **Valores calculados que no se actualizan**: Verifique la lógica de cálculo y asegúrese de que todos los campos referenciados estén nombrados correctamente.
3. **Problemas de rendimiento**: Optimice los cálculos complejos o considere enfoques alternativos para mostrar datos de solo lectura.
