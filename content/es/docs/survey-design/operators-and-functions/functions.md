---
title: "Funciones"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 293
---

### Funciones de cadena

{{% alert icon=" " context="warning" %}}
Al trabajar con cadenas dentro de expresiones, es importante usar comillas simples ('') para encerrar cadenas literales. Sin embargo, surge una excepción cuando se quieren incluir comillas simples dentro de una cadena literal. En tales casos, puede usar comillas dobles ("") para encerrar toda la cadena.

Por ejemplo:
- Correcto: if(${yesno} = 1, "a string with 'single quotes' in it", "no single quotes here")
- Incorrecto: if(${yesno} = 1, 'a string with 'single quotes' in it', 'no single quotes here')

Con respecto a las comillas tipográficas, es fundamental ser consciente de su presencia, ya que pueden causar problemas en las expresiones. Muchos editores de texto enriquecido convierten automáticamente las comillas rectas ("" o '') en comillas tipográficas o curvas ("" o ''), lo que puede resultar en errores de sintaxis o comportamiento inesperado. Para evitar esto, asegúrese de usar consistentemente comillas rectas ('') en sus expresiones.
{{% /alert %}}

rtSurvey admite varias funciones, incluyendo:

1. `string(field)`: Convierte un campo a cadena.
   - Ejemplo: `string(34.8)` se convertirá en `'34.8'`.

2. `string-length(field)`: Devuelve la longitud de un campo de cadena.
   - Ejemplo: `string-length(.) > 3 and string-length(.) < 10` puede usarse para garantizar que el campo actual tenga entre 3 y 10 caracteres.

3. `substr(fieldorstring, startindex, endindex)`: Devuelve una subcadena que comienza en `startindex` y termina justo antes de `endindex`. Los índices comienzan en 0 para el primer carácter de la cadena.
   - Ejemplo: `substr(${phone}, 0, 3)` devolverá los primeros tres dígitos de un número de teléfono.

4. `concat(a, b, c, ...)`: Concatena campos (y/o cadenas) juntos.
   - Ejemplo: `concat(${firstname}, ' ', ${lastname})` devolverá un nombre completo combinando los valores en los campos `firstname` y `lastname`.

5. `linebreak()`: Devuelve un carácter de salto de línea.
   - Ejemplo: `concat(${field1}, linebreak(), ${field2}, linebreak(), ${field3})` devolverá una lista de tres valores de campo con saltos de línea entre ellos.

6. `lower()`: Convierte una cadena a todos los caracteres en minúsculas.
   - Ejemplo: `lower('Street Name')` devolverá "street name".

7. `upper()`: Convierte una cadena a todos los caracteres en mayúsculas.
   - Ejemplo: `upper('Street Name')` devolverá "STREET NAME".

### Funciones de select_one y select_multiple

1. `count-selected(field)`: Devuelve el número de elementos seleccionados en un campo select_multiple.
   - Ejemplo: `count-selected(.) = 3` puede usarse como expresión de restricción para garantizar que se seleccionen exactamente tres opciones.

2. `selected(field, value)`: Devuelve verdadero o falso dependiendo de si el valor especificado fue seleccionado en el campo select_one o select_multiple.
   - Ejemplo: `selected(${color}, 'Blue')` puede usarse como expresión de relevancia para mostrar un grupo o campo solo si el encuestado seleccionó "Azul" como su color favorito.
   - Nota: El segundo parámetro siempre debe especificar el valor de la opción, no la etiqueta de la opción. Use el valor de la columna de valor en la hoja de cálculo de opciones de la definición del formulario.

3. `selected-at(field, number)`: Devuelve el elemento seleccionado en la posición especificada en un campo select_multiple. Cuando el número pasado es 0, devuelve el primer elemento seleccionado; cuando el número es 1, devuelve el segundo elemento seleccionado, y así sucesivamente.
   - Ejemplo: `selected-at(${fruits}, 0) = 'Apple'` puede usarse como expresión de relevancia para mostrar un grupo o campo solo si la primera opción seleccionada es "Apple".
   - Nota: El valor devuelto será el valor de la opción, no la etiqueta de la opción.

4. `choice-label(field, value)`: Devuelve la etiqueta de una opción de campo select_one o select_multiple, según se define en la hoja de cálculo de opciones de la definición del formulario.
   - Ejemplo 1: `choice-label(${country}, ${country})` devolverá la etiqueta de la opción de la opción actualmente seleccionada en el campo llamado `country`.
   - Ejemplo 2: `choice-label(${languages}, selected-at(${languages}, 0))` devolverá la etiqueta de la primera opción seleccionada en el campo llamado `languages`.
   - Nota: Esta función recupera la etiqueta de la opción, no el valor.

### Funciones de campos repetidos

En rtSurvey, si desea hacer la(s) misma(s) pregunta(s) varias veces, puede colocar un campo dentro de un grupo de repetición. Esto da como resultado múltiples instancias del mismo campo. Las siguientes funciones pueden ayudarle a trabajar con estos campos repetidos y los datos repetidos que producen.

1. `join(string, repeatedfield)`: Para un campo dentro de un grupo de repetición, genera una lista separada por cadena de valores. El primer parámetro especifica el delimitador a usar para separar los valores.
   - Ejemplo: `join(', ', ${member_name})` generará una lista única separada por comas de todos los nombres ingresados.

2. `join-if(string, repeatedfield, expression)`: Funciona exactamente como `join()`, excepto que verifica cada instancia en el grupo de repetición usando la expresión suministrada. Si la expresión se evalúa como falsa, el elemento se omitirá de la salida.
   - Ejemplo: `join-if(', ', ${member_name}, ${age} >= 18)` generará una lista separada por comas de nombres solo de miembros adultos (aquellos con edades de 18 años o más).

3. `count(repeatgroup)`: Devuelve el número actual de veces que un grupo de repetición se ha repetido.
   - Ejemplo: `count(${groupname})` devolverá el número de instancias del grupo.

4. `count-if(repeatgroup, expression)`: Funciona exactamente como `count()`, excepto que verifica cada instancia en el grupo de repetición usando la expresión suministrada.
   - Ejemplo: `count-if(${members}, ${age} >= 18)` devolverá el conteo de miembros adultos según el campo de edad dentro del grupo de repetición "members".

5. `sum(repeatedfield)`: Para un campo dentro de un grupo de repetición, calcula la suma de todos los valores.
   - Ejemplo: `sum(${loan_amount})` devolverá el valor total de todos los préstamos.

6. `sum-if(repeatedfield, expression)`: Funciona exactamente como `sum()`, excepto que verifica cada instancia usando la expresión suministrada.
   - Ejemplo: `sum-if(${loan_amount}, ${loan_amount} > 500)` devolverá el valor total de todos los préstamos superiores a 500.

7. `min(repeatedfield)`: Para un campo dentro de un grupo de repetición, calcula el mínimo de todos los valores.
   - Ejemplo: `min(${member_age})` devolverá la edad del miembro más joven del grupo.

8. `min-if(repeatedfield, expression)`: Funciona exactamente como `min()`, excepto que verifica cada instancia usando la expresión suministrada.
   - Ejemplo: `min-if(${member_age}, ${member_age} >= 18)` devolverá la edad del adulto más joven del grupo.

9. `max(repeatedfield)`: Para un campo dentro de un grupo de repetición, calcula el máximo de todos los valores.
   - Ejemplo: `max(${member_age})` devolverá la edad del miembro más viejo del grupo.

10. `max-if(repeatedfield, expression)`: Funciona exactamente como `max()`, excepto que verifica cada instancia usando la expresión suministrada.
    - Ejemplo: `max-if(${member_age}, ${member_age} >= 18)` devolverá la edad del adulto más viejo del grupo.

11. `index()`: Llamado dentro de un grupo de repetición, devuelve el número de índice para el grupo o instancia actual.
    - Ejemplo: `index()` cuando se usa dentro de un grupo de repetición devolverá 1 para la primera instancia, 2 para la segunda, y así sucesivamente.

12. `indexed-repeat(repeatedfield, repeatgroup, index)`: Referencia un campo o grupo que está dentro de un grupo de repetición desde fuera de ese grupo de repetición.
    - Ejemplo 1: `indexed-repeat(${name}, ${names}, 1)` devolverá el primer nombre disponible cuando el campo de nombre está dentro de un grupo de repetición anterior llamado "names".
    - Ejemplo 2: `indexed-repeat(${name}, ${names}, index())` obtendrá el nombre correspondiente al número de instancia del grupo de repetición actual.

13. `rank-index(index, repeatedfield)`: Esta función calcula el rango ordinal de la instancia especificada de un campo repetido para su uso fuera del grupo de repetición. El rango de 1 se asigna a la instancia con el valor más alto.
    - Ejemplo: `rank-index(1, ${random_draw})` calcula el rango de la primera instancia según el valor de su campo `random_draw` en comparación con los valores de otras instancias.

14. `rank-index-if(index, repeatedfield, expression)`: Esta función funciona de manera similar a `rank-index()`, pero verifica cada instancia en el grupo de repetición del campo repetido usando la expresión suministrada.
    - Ejemplo: `rank-index-if(1, ${age}, ${age} >= 18)` calcula el rango de edad dentro del conjunto de adultos, considerando solo instancias donde la edad sea mayor o igual a 18.

### Funciones numéricas

{{< table >}}
| Operador | Operación | Ejemplo | Respuesta de ejemplo |
|----------|-----------|---------|----------------------|
| `+` | Suma | 1 + 1 | 2 |
| `-` | Resta | 3 - 2 | 1 |
| `*` | Multiplicación | 3 * 2 | 6 |
| `div` | División | 10 div 2 | 5 |
| `mod` | Módulo | 9 mod 2 | 1 |
{{< /table >}}

rtSurvey admite funciones numéricas, incluyendo:
- `number(field)`: Convierte el valor del campo a un número.
  - Ejemplo: `number('34.8')` = 34.8

- `int(field)`: Convierte el valor del campo a un entero.
  - Ejemplo: `int('39.2')` = 39

- `min(field1, ..., fieldx)`: Devuelve el valor mínimo entre los campos pasados.
  - Ejemplo: `min(${father_age}, ${mother_age})` devolverá la edad del padre o la madre, la que sea menor.

- `max(field1, ..., fieldx)`: Devuelve el valor máximo entre los campos pasados.
  - Ejemplo: `max(${father_age}, ${mother_age})` devolverá la edad del padre o la madre, la que sea mayor.

- `format-number(field)`: Formatea el valor de un campo entero o decimal según la configuración regional del usuario.
  - Ejemplo: `format-number(${income})` podría formatear "120000" como "120,000".

- `round(field, digits)`: Redondea el valor del campo numérico al número especificado de dígitos después del punto decimal.
  - Ejemplo: `round(${interest_rate}, 2)`

- `abs(number)`: Devuelve el valor absoluto de un número.

- `pow(base, exponent)`: Devuelve el valor del primer parámetro elevado a la potencia del segundo parámetro.

- `log10(fieldorvalue)`: Devuelve el logaritmo en base diez del campo o valor pasado.

- `sin(fieldorvalue)`: Devuelve el seno del campo o valor pasado, expresado en radianes.

- `cos(fieldorvalue)`: Devuelve el coseno del campo o valor pasado, expresado en radianes.

- `tan(fieldorvalue)`: Devuelve la tangente del campo o valor pasado, expresado en radianes.

- `asin(fieldorvalue)`: Devuelve el arcoseno del campo o valor pasado, expresado en radianes.

- `acos(fieldorvalue)`: Devuelve el arcocoseno del campo o valor pasado, expresado en radianes.

- `atan(fieldorvalue)`: Devuelve la arcotangente del campo o valor pasado, expresado en radianes.

- `atan2(x, y)`: Devuelve el ángulo en radianes subtendido en el origen por el punto con coordenadas (x, y) y el eje x positivo.

- `sqrt(fieldorvalue)`: Devuelve la raíz cuadrada no negativa del campo o valor pasado.

- `exp(x)`: Devuelve el valor de e^x.

- `pi()`: Devuelve el valor de pi.

### Funciones de fecha y hora

{{% alert icon=" " context="warning" %}}
Los valores de fecha en rtSurvey se almacenan como cadenas en formato `YYYY-MM-DD`. Los valores de fecha y hora se almacenan como cadenas ISO 8601 (`YYYY-MM-DDTHH:MM:SS`). Use `decimal-date-time()` para convertir a un número para aritmética (p. ej., cálculo de duraciones).
{{% /alert %}}

1. `today()`: Devuelve la fecha de hoy como cadena en formato `YYYY-MM-DD`. Se evalúa una vez cuando se abre el formulario.
   - Ejemplo: `today()` → `'2024-03-15'`
   - Uso común: columna `default` para prellenar la fecha de hoy, o en `relevant`/`constraint` para comparar con un campo de fecha.

2. `now()`: Devuelve la fecha y hora actuales como cadena ISO 8601. Se evalúa cada vez que se calcula la expresión.
   - Ejemplo: `now()` → `'2024-03-15T14:32:00.000+03:00'`
   - Uso común: registrar la marca de tiempo exacta de un evento específico durante la encuesta.

3. `date(value)`: Convierte un valor (cadena o número) a una cadena de fecha.
   - Ejemplo: `date('2024-03-15')` → `'2024-03-15'`

4. `date-time(value)`: Convierte un valor a una cadena de fecha y hora.
   - Ejemplo: `date-time(${event_timestamp})`

5. `decimal-date-time(value)`: Convierte una cadena de fecha o fecha y hora a un número decimal que representa milisegundos desde la época Unix dividido por 86400000 (días fraccionarios desde 1970-01-01). Úselo para realizar aritmética en fechas.
   - Ejemplo — Duración en días entre dos fechas:
     `decimal-date-time(${end_date}) - decimal-date-time(${start_date})`
   - Ejemplo — Duración en minutos entre dos fechas y horas:
     `(decimal-date-time(${end_time}) - decimal-date-time(${start_time})) * 1440`

6. `format-date(date, format)`: Formatea un valor de fecha usando una cadena de patrón.
   - Tokens de formato: `%Y` (año de 4 dígitos), `%y` (año de 2 dígitos), `%m` (mes 01–12), `%d` (día 01–31), `%a` (día de la semana abreviado), `%b` (nombre del mes abreviado)
   - Ejemplo: `format-date(today(), '%d/%m/%Y')` → `'15/03/2024'`

7. `format-date-time(datetime, format)`: Formatea un valor de fecha y hora usando una cadena de patrón. Acepta todos los tokens de `format-date` más:
   - `%H` (hora 00–23), `%h` (hora 01–12), `%M` (minutos 00–59), `%S` (segundos 00–59), `%3` (milisegundos), `%P` (AM/PM)
   - Ejemplo: `format-date-time(now(), '%d/%m/%Y %H:%M')` → `'15/03/2024 14:32'`

---

### Funciones booleanas

1. `boolean(value)`: Convierte cualquier valor a booleano. Devuelve `true` para cadenas no vacías, números distintos de cero y `true`; devuelve `false` para cadenas vacías, `0` y `false`.

2. `boolean-from-string(string)`: Devuelve `true` si la cadena es `'1'` o `'true'` (sin distinción de mayúsculas); devuelve `false` en caso contrario.

3. `true()`: Devuelve el valor booleano `true`.
   - Ejemplo: En la columna `required`, `true()` es equivalente a `yes`.

4. `false()`: Devuelve el valor booleano `false`.
   - Ejemplo: `if(${skip_section} = 'yes', false(), true())` — establecer dinámicamente como requerido.

5. `not(expression)`: Devuelve la negación lógica de la expresión.
   - Ejemplo: `not(${consent} = 'yes')` — muestra una advertencia cuando NO se dio consentimiento.
   - Ejemplo: `not(selected(${issues}, 'none'))` — requiere detalles solo si no se seleccionó "ninguno".

---

### Funciones de cadena adicionales

1. `starts-with(string, prefix)`: Devuelve `true` si `string` comienza con `prefix`.
   - Ejemplo: `starts-with(${phone}, '+254')` verifica si el número de teléfono comienza con el código de país de Kenia.

2. `contains(string, substring)`: Devuelve `true` si `string` contiene `substring`.
   - Ejemplo: `contains(${email}, '@')` verifica que una dirección de correo tenga un signo `@`.

3. `substring-before(string, needle)`: Devuelve la parte de `string` que aparece antes de la primera ocurrencia de `needle`.
   - Ejemplo: `substring-before(${full_name}, ' ')` extrae la primera palabra (nombre de pila).

4. `substring-after(string, needle)`: Devuelve la parte de `string` que aparece después de la primera ocurrencia de `needle`.
   - Ejemplo: `substring-after(${email}, '@')` extrae la parte de dominio de una dirección de correo.

5. `normalize-space(string)`: Elimina el espacio en blanco al inicio y al final, y colapsa todas las secuencias de espacio en blanco internas en un solo espacio.

6. `translate(string, search_chars, replace_chars)`: Reemplaza cada carácter en `string` que aparece en `search_chars` con el carácter correspondiente en `replace_chars`.
   - Ejemplo: `translate(${phone}, ' -()', '')` elimina espacios, guiones y paréntesis de un número de teléfono.

---

### Funciones matemáticas adicionales

1. `floor(number)`: Devuelve el mayor entero menor o igual que `number`.
   - Ejemplo: `floor(4.9)` = 4, `floor(-2.1)` = -3

2. `ceiling(number)`: Devuelve el menor entero mayor o igual que `number`.
   - Ejemplo: `ceiling(4.1)` = 5, `ceiling(-2.9)` = -2

3. `random()`: Devuelve un número decimal aleatorio entre 0.0 (inclusive) y 1.0 (exclusivo).
   - Ejemplo: `int(random() * 6) + 1` → número aleatorio del 1 al 6 (lanzamiento de dados)

4. `coalesce(a, b)`: Devuelve `a` si `a` no está vacío; de lo contrario devuelve `b`. Útil como respaldo cuando un campo podría estar vacío.
   - Ejemplo: `coalesce(${preferred_name}, ${full_name})` — usa el nombre preferido si está establecido, de lo contrario usa el nombre completo.

5. `once(value)`: Evalúa `value` y lo almacena, pero solo si el campo actual está **vacío**. Si el campo ya tiene un valor, `once()` devuelve el valor existente sin cambios.
   - Ejemplo: `once(today())` en la columna `default` establece la fecha de hoy una vez y no se actualiza si el encuestador vuelve a abrir el formulario.
   - Ejemplo: `once(uuid())` genera un UUID una vez y lo mantiene estable entre reediciones.

---

### Funciones geográficas

1. `area(geoshape_value)`: Calcula el **área en metros cuadrados** encerrada por un valor de geoshape (polígono).
   - Ejemplo: `area(${field_boundary})` — calcula el área de un campo encuestado en m².
   - Ejemplo: `round(area(${field_boundary}) div 10000, 2)` — convertir a hectáreas.

2. `distance(coordinates)`: Calcula la **longitud total del trayecto en metros** de un geotrace (línea), o la distancia entre dos geopoints.
   - Para un geotrace: `distance(${route})` devuelve la longitud total del trayecto en metros.
   - Para dos geopoints: `distance(concat(${point_a}, ' ', ${point_b}))` devuelve la distancia entre ellos.

---

### Funciones de validación

1. `regex(value, pattern)`: Devuelve `true` si `value` coincide con la expresión regular `pattern`. Úselo en la columna `constraint` para validación basada en patrones.
   - Ejemplo: `regex(., '^[0-9]{10}$')` — validar un número de 10 dígitos.
   - Ejemplo: `regex(., '^[A-Z]{2}[0-9]{6}$')` — validar un formato de número de pasaporte.
   - Ejemplo: `regex(., '^[^@]+@[^@]+\.[^@]{2,}$')` — verificación básica del formato de correo electrónico.

2. `checklist(min, max, v1, v2, ...)`: Evalúa una lista de expresiones booleanas y devuelve `true` si el número de valores `true` está entre `min` y `max` (inclusive).
   - Ejemplo: `checklist(2, 3, ${q1} = 'yes', ${q2} = 'yes', ${q3} = 'yes')` — pasa si exactamente 2 o 3 de las tres condiciones son verdaderas.

3. `weighted-checklist(min, max, v1, w1, v2, w2, ...)`: Como `checklist()`, pero cada valor tiene un peso. La suma de pesos de los valores verdaderos debe estar entre `min` y `max`.

---

### Funciones de utilidad

1. `uuid()`: Genera un UUID aleatorio (formato RFC 4122 v4) como cadena.
   - Normalmente se usa con `once()` para generar un ID único estable: `once(uuid())`

2. `version()`: Devuelve el valor del atributo `version` del formulario según se establece en la hoja de trabajo de configuración.

3. `position()`: Cuando se llama dentro de un **grupo de repetición**, devuelve el índice basado en 1 de la instancia de repetición actual.

4. `thousandsep(length, separator, value)`: Formatea un número con un separador de miles.
   - Ejemplo: `thousandsep(0, ',', 1234567)` → `'1,234,567'`

5. `substr-jsonpath(value, jsonpath)`: Extrae una subcadena de una cadena JSON usando una expresión JSONPath.
   - Ejemplo: `substr-jsonpath(${api_response}, '$.data.name')` — extrae el campo `name` de una cadena JSON almacenada en `api_response`.
