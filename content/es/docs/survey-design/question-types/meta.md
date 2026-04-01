---
title: "Meta"
description: "Los tipos de pregunta meta capturan automáticamente información del dispositivo, del encuestador y de tiempo sin ninguna entrada del encuestado."
icon: "info"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 237
---

Los tipos de pregunta meta son campos especiales que se completan **automáticamente** — el encuestado nunca los ve. Capturan contexto sobre el envío: cuándo se recopiló, qué dispositivo se usó y quién lo recopiló. Agréguelos en la hoja de trabajo `survey` como cualquier otro tipo de pregunta; simplemente no aparecen en pantalla.

## Especificación básica de XLSForm

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| deviceid | deviceid | |

Las etiquetas son opcionales para los campos meta ya que nunca se muestran.

---

## Campos meta de tiempo

### `start`

Registra la **fecha y hora en que se abrió el formulario**. Almacenado en formato ISO 8601 (`YYYY-MM-DDTHH:MM:SS.sss+HH:MM`).

```
type    | name  | label
start   | start |
```

### `end`

Registra la **fecha y hora en que se envió el formulario**. Junto con `start`, puede calcular el tiempo empleado en completar el formulario:

```
type      | name          | calculation
calculate | duration_min  | (decimal-date-time(${end}) - decimal-date-time(${start})) * 1440
```

### `today`

Registra la **fecha actual** (sin componente de hora). Almacenado como `YYYY-MM-DD`. Útil cuando solo necesita la fecha sin la marca de tiempo completa.

```
type  | name  | label
today | today |
```

---

## Campos meta del dispositivo

### `deviceid`

Registra el **identificador único del dispositivo** usado para la recopilación de datos. En Android esto es típicamente el IMEI o el ID de Android. Útil para rastrear qué dispositivo envió cada formulario y detectar envíos duplicados desde el mismo dispositivo.

```
type      | name     | label
deviceid  | deviceid |
```

### `devicephonenum`

Registra el **número de teléfono de la tarjeta SIM** en el dispositivo (si está disponible). Puede estar vacío si el dispositivo no tiene SIM o si el número no está almacenado en la SIM.

```
type           | name          | label
devicephonenum | devicephonenum |
```

### `simserial`

Registra el **número de serie de la tarjeta SIM** (ICCID). Útil para identificar qué SIM/operador se usó.

```
type      | name      | label
simserial | simserial |
```

### `subscriberid`

Registra el **IMSI (Identidad Internacional de Suscriptor Móvil)** — el identificador único del suscriptor en la tarjeta SIM.

```
type         | name        | label
subscriberid | subscriberid |
```

---

## Campos meta del encuestador

### `username`

Registra el **nombre de usuario del encuestador conectado** (la cuenta usada en la aplicación rtSurvey). Esta es la forma más confiable de rastrear quién recopiló cada envío.

```
type     | name     | label
username | username |
```

### `email`

Registra la **dirección de correo electrónico del encuestador conectado**.

```
type  | name  | label
email | email |
```

### `phonenumber`

Registra el **número de teléfono asociado con la cuenta del encuestador** (si está configurado).

```
type        | name       | label
phonenumber | phonenumber |
```

---

## Registro de auditoría

### `audit`

El campo meta `audit` habilita el **registro detallado de auditoría** — registra un registro con marcas de tiempo de cada pregunta que visitó el encuestador, cuánto tiempo pasó en cada una y (opcionalmente) su ubicación GPS en cada paso. El registro de auditoría se guarda como un archivo `audit.csv` separado junto con cada envío.

```
type  | name  | parameters
audit | audit | location-priority=balanced location-min-interval=30 location-max-age=60
```

#### Parámetros de auditoría

| Parámetro | Descripción |
|-----------|-------------|
| `location-priority` | Nivel de precisión GPS: `no-gps`, `low-power`, `balanced`, `high-accuracy` |
| `location-min-interval` | Segundos mínimos entre capturas de ubicación |
| `location-max-age` | Edad máxima (segundos) de una ubicación en caché para aceptar |

El registro de auditoría captura:
- Nombre de la pregunta y tipo de evento (`question`, `form.start`, `form.exit`, `form.save`, `form.finalize`)
- Marcas de tiempo de inicio y fin para cada evento
- Coordenadas GPS (si `location-priority` está establecido)

{{% alert icon=" " context="warning" %}}
El campo `audit` genera un archivo separado por envío. Asegúrese de que su proceso de datos procese tanto los datos del formulario principal como el CSV de auditoría.
{{% /alert %}}

---

## Ejemplo completo

Una encuesta típica de hogar podría incluir todos los campos meta de tiempo y del encuestador:

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| today | today | |
| deviceid | deviceid | |
| username | username | |
| email | email | |
| audit | audit | |
| text | household_id | ID del hogar |
| ... | ... | ... |

---

## Mejores prácticas

1. Incluya siempre `start` y `end`; son gratuitos, automáticos e invaluables para el monitoreo de calidad.
2. Incluya siempre `username` para rastrear a los encuestadores.
3. Incluya `deviceid` cuando desee detectar envíos duplicados o rastrear dispositivos de campo.
4. Use `audit` en encuestas de alta responsabilidad donde necesite verificar que los encuestadores realmente visitaron cada pregunta.
5. Los campos relacionados con SIM (`simserial`, `subscriberid`, `devicephonenum`) solo son confiables en dispositivos Android con tarjetas SIM activas; omítalos para implementaciones solo con tabletas.

---

## Limitaciones

- Todos los campos meta son de **solo lectura**; no pueden ser referenciados ni modificados por otros cálculos.
- `username` y `email` requieren que el encuestador esté conectado; estarán vacíos para envíos anónimos.
- Los campos meta de SIM/teléfono pueden devolver valores vacíos en tabletas solo con Wi-Fi y algunas versiones de Android debido a restricciones de permisos.
