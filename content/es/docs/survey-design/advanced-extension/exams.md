---
title: "Exámenes"
description: "La función de examen agrega un modo de cuestionario cronometrado a una encuesta, con retroalimentación de audio opcional para respuestas correctas e incorrectas."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 298
---

La función **Examen** convierte una encuesta en un cuestionario cronometrado. Se muestra una cuenta regresiva al encuestado y la encuesta registra cuánto tiempo queda cuando termina. Opcionalmente, se pueden reproducir sonidos de audio para respuestas correctas e incorrectas.

Esto es útil para evaluaciones de conocimiento, pruebas de alfabetización, verificaciones de competencia del personal de campo y cualquier encuesta en la que el tiempo empleado sea un dato significativo.

---

## Función `check-exam()`

Configure el examen usando `check-exam()` en la columna **`calculation`** de un campo `calculate` colocado al inicio del formulario:

```
check-exam(examTime, questionToStoreRemainingTime)
check-exam(examTime, questionToStoreRemainingTime, rightSound, wrongSound, excludeQuestion)
```

### Parámetros

| # | Parámetro | Descripción |
|---|-----------|-------------|
| 1 | `examTime` | Duración total del examen en segundos |
| 2 | `questionToStoreRemainingTime` | El `name` de un campo `calculate` o `integer` que almacenará el tiempo restante cuando finalice el examen |
| 3 | `rightSound` | *(Opcional)* Nombre de archivo del audio a reproducir cuando se da una respuesta correcta (adjunte al formulario como archivo multimedia) |
| 4 | `wrongSound` | *(Opcional)* Nombre de archivo del audio a reproducir cuando se da una respuesta incorrecta |
| 5 | `excludeQuestion` | *(Opcional)* Lista separada por comas de nombres de campos a excluir del temporizador del examen (p. ej., `'intro_note,consent'`) |

---

## Configuración básica

### Paso 1: Agregar campos de examen

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | exam_config | | `check-exam(600, 'remaining_time')` |
| calculate | remaining_time | | |

`exam_config` activa el temporizador de 600 segundos (10 minutos). `remaining_time` se completa automáticamente cuando el encuestado termina.

### Paso 2: Agregar sus preguntas

El temporizador del examen cubre todas las preguntas del formulario excepto las listadas en `excludeQuestion`.

| type | name | label |
|------|------|-------|
| select_one yesno | q1 | La capital de Kenia es Nairobi. ¿Verdadero o falso? |
| select_one choices | q2 | ¿Qué órgano bombea la sangre por el cuerpo? |
| select_one choices | q3 | El agua hierve a 100°C al nivel del mar. ¿Verdadero o falso? |

### Paso 3: Almacenar el tiempo restante

El campo nombrado en el parámetro 2 (`remaining_time`) se establece automáticamente con el número de segundos restantes cuando el encuestado envía. Un valor de `0` significa que se agotó el tiempo; un valor alto significa que terminó rápidamente.

---

## Con retroalimentación de audio

Adjunte archivos de sonido al formulario (como archivos adjuntos multimedia) y luego referenciarlos:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | exam_config | | `check-exam(300, 'remaining_time', 'correct.mp3', 'wrong.mp3')` |

- `correct.mp3` se reproduce cuando el encuestado selecciona la respuesta correcta
- `wrong.mp3` se reproduce cuando el encuestado selecciona una respuesta incorrecta

{{% alert icon=" " context="warning" %}}
Los archivos de sonido deben adjuntarse al formulario como archivos multimedia y el nombre del archivo debe coincidir exactamente (distingue mayúsculas de minúsculas), incluida la extensión.
{{% /alert %}}

---

## Excluir preguntas del temporizador

Pase una lista separada por comas de nombres de campos para excluirlos del examen (p. ej., notas introductorias o preguntas de consentimiento):

```
check-exam(300, 'remaining_time', '', '', 'intro_note,consent_ack,section_header')
```

Deje `rightSound` y `wrongSound` como cadenas vacías `''` si no necesita audio pero sí necesita exclusiones.

---

## Ejemplo completo

| type | name | label | calculation |
|------|------|-------|-------------|
| note | intro | Bienvenido a la evaluación de conocimientos de salud. Tiene 5 minutos para responder todas las preguntas. | |
| trigger | start_ack | Toque OK cuando esté listo para comenzar. | |
| calculate | exam_config | | `check-exam(300, 'remaining_time', 'correct.mp3', 'wrong.mp3', 'intro,start_ack')` |
| calculate | remaining_time | | |
| select_one yesno | q1 | Lavarse las manos previene la propagación de enfermedades. | |
| select_one yesno | q2 | Debe beber al menos 2 litros de agua por día. | |
| select_one yesno | q3 | La malaria es causada por un virus. | |

---

## Mejores prácticas

1. Siempre informe a los encuestados sobre el límite de tiempo antes de comenzar; use una `note` o `trigger` antes del campo `check-exam()`.
2. Excluya las notas introductorias y las preguntas de consentimiento del temporizador usando el parámetro `excludeQuestion`.
3. Use `remaining_time` en un cálculo de seguimiento para detectar tiempos agotados: `if(${remaining_time} = 0, 'Tiempo agotado', 'Completado')`.
4. Mantenga el número de preguntas proporcional al tiempo permitido; 2–3 minutos por pregunta es una línea base razonable para la mayoría de las evaluaciones de conocimiento.
5. Pruebe con archivos de audio en el dispositivo real antes de la implementación; la reproducción de audio varía según las versiones de Android y los navegadores.

## Limitaciones

- El temporizador es solo de visualización; el formulario no se envía automáticamente cuando se agota el tiempo; el encuestado debe enviar manualmente.
- La retroalimentación de audio requiere que el volumen del dispositivo esté activado y no silenciado.
- La función de examen es una extensión de rtSurvey y no forma parte de la especificación estándar de XLSForm.
