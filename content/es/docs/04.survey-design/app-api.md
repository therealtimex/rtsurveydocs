---
title: "API de la aplicación"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 300
---

La AppAPI permite a los usuarios cargar metadatos del sistema desde la aplicación usando diferentes métodos en FormEngine y DMView. Proporciona acceso a varias claves de datos para recuperar información específica de la aplicación.

En el xlsform, puede usar la función `pulldata()` con la siguiente sintaxis:


{{< alert context="light" text="pulldata('app-api', 'data-key')" />}}

- `'app-api'`: Esta palabra clave informa al FormEngine que cargue los datos desde la API de la aplicación.
- `'data-key'`: Esta es la clave de los datos que desea cargar desde la API de la aplicación.
- Si la clave de datos no es válida o no está admitida, el cálculo devolverá "n/a".

Aquí están las claves de datos admitidas que puede usar con la App-API:

`osPlatform`: Devuelve el nombre del SO actual (Android o iOS) y la versión del SO. Las plataformas web devolverán un valor vacío.

`appPlatform`: Devuelve el nombre de la plataforma de la aplicación, que es `rtSurvey`.

`appVersion`: Devuelve el nombre de versión de la aplicación.

`getDisplayWidth`: Devuelve el ancho de la pantalla del dispositivo en píxeles.

`getDisplayHeight`: Devuelve la altura de la pantalla del dispositivo en píxeles.

`getScreenSize`: Devuelve el tamaño de la pantalla del dispositivo en pulgadas.

`projectCode`: Devuelve el código de proyecto actual del sitio al que el usuario está iniciando sesión.

`projectURL`: Devuelve la URL del proyecto actual del sitio al que el usuario está iniciando sesión. El valor predeterminado/alternativo es un texto vacío ("").

`startingPoint`: Devuelve la ruta del punto que inicia el formulario. Consulte el "Punto de inicio del formulario" para obtener más detalles.

`serverTime`: Devuelve la mejor aproximación disponible de la fecha y hora en el servidor.

`user.[attribute]`: Devuelve los atributos del usuario actual basados en la clave de atributo especificada. Consulte la tabla de "Atributos de usuario" para ver las claves de atributo disponibles.

Combine las claves de atributo a continuación con "user." en los parámetros de `pulldata()` para recuperar la información del usuario actual. Por ejemplo, use `user.username`, `user.email`, etc.

| Clave de atributo    | Descripción                          |
|----------------------|--------------------------------------|
| username             | Nombre de usuario del usuario        |
| name                 | Nombre completo del usuario          |
| staffCode            | Código de personal del usuario       |
| phone                | Número de teléfono del usuario       |
| email                | Dirección de correo electrónico del usuario |
| description          | Texto de descripción en la información del usuario |
| organization_id      | ID de la organización a la que pertenece el usuario |
| organization_name    | Nombre de la organización a la que pertenece el usuario |
| team_id              | ID del equipo al que pertenece el usuario |
| supervisor_id        | ID del supervisor del usuario        |
| is_supervisor        | 1 si el usuario es supervisor, 0 si no |

`instancePath`: Devuelve la ruta de la carpeta de instancia actual.

`appLanguage`: Devuelve el idioma actual de la aplicación configurado en la configuración de la aplicación (p. ej., vi, en).

`openArgs.[attribute]`: Devuelve el argumento de formulario abierto pasado desde el ActionButton (act_fill_form, act_get_instance). El valor predeterminado/alternativo es un texto vacío ("").

`primaryAppColor`: Recupera el color principal de la aplicación.

---

## Ejemplos de uso

### Almacenar el nombre de usuario y la organización del encuestador

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | enumerator_name | | `pulldata('app-api', 'user.name')` |
| calculate | enumerator_org | | `pulldata('app-api', 'user.organization_name')` |
| calculate | enumerator_email | | `pulldata('app-api', 'user.email')` |

Use estos en etiquetas de notas para propósitos de auditoría:
```
note | interviewer_info | Entrevistador: ${enumerator_name} (${enumerator_org})
```

### Información del dispositivo y la pantalla

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | device_platform | | `pulldata('app-api', 'osPlatform')` |
| calculate | app_ver | | `pulldata('app-api', 'appVersion')` |
| calculate | screen_w | | `pulldata('app-api', 'getDisplayWidth')` |

Útil para la solución de problemas: exporte `device_platform` y `app_ver` junto con sus datos para identificar qué versión del dispositivo se usó para cada envío.

### Hora del servidor en lugar de la hora del dispositivo

Los relojes de los dispositivos pueden estar mal configurados. Use `serverTime` para una marca de tiempo más confiable:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | server_ts | | `pulldata('app-api', 'serverTime')` |

### Lógica condicional basada en el rol del usuario

Muestre una sección solo para supervisores:

| type | name | label | relevant |
|------|------|-------|----------|
| calculate | is_supervisor | | `pulldata('app-api', 'user.is_supervisor')` |
| begin_group | supervisor_section | Revisión del supervisor | `${is_supervisor} = '1'` |
| text | supervisor_notes | Notas del supervisor | |
| end_group | | | |

### Pasar argumentos desde un botón de acción

Cuando el formulario se inicia desde un botón de acción `act_fill_form` con argumentos personalizados:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | passed_hh_id | | `pulldata('app-api', 'openArgs.household_id')` |
| calculate | passed_task | | `pulldata('app-api', 'openArgs.task_code')` |

El botón de acción debe pasar los argumentos con claves coincidentes (p. ej., `household_id`, `task_code`).

### Uso de información del proyecto

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | project | | `pulldata('app-api', 'projectCode')` |
| calculate | project_url | | `pulldata('app-api', 'projectURL')` |

---

## Notas

- Todas las llamadas `pulldata('app-api', ...)` se evalúan cuando se abre el formulario y no se reevalúan dinámicamente durante la sesión (excepto `serverTime` y `now()`).
- Si una clave no está admitida o los datos no están disponibles, la función devuelve `'n/a'` (no una cadena vacía — pruebe con `!= 'n/a'` en lugar de `!= ''`).
- Los valores de `openArgs` solo están disponibles cuando el formulario se inicia desde un botón de acción; de lo contrario devuelven una cadena vacía.
