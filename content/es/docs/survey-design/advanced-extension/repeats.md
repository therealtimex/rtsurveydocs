---
title: "Repeticiones avanzadas"
description: "Patrones avanzados para grupos de repetición: conteos dinámicos, repeticiones anidadas, resumen de datos de repetición y referencia de valores entre repeticiones."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 295
---

Esta página cubre patrones avanzados para trabajar con grupos de repetición en rtSurvey. Para los conceptos básicos sobre cómo configurar un grupo de repetición, consulte [Agrupación y repeticiones](../repeats).

---

## Conteo dinámico de repeticiones

De forma predeterminada, el encuestador decide cuántas veces repetir. Puede fijar el número de repeticiones usando `repeat_count`:

| type | name | label | repeat_count |
|------|------|-------|--------------|
| begin_repeat | household_members | Miembro del hogar | `${num_members}` |
| text | member_name | Nombre del miembro | |
| integer | member_age | Edad | |
| end_repeat | | | |

La repetición se ejecuta exactamente `${num_members}` veces, donde `num_members` se recopiló anteriormente en el formulario. El encuestador no puede agregar ni eliminar instancias.

---

## Acceso indexado: `indexed-repeat()`

Acceda al valor del campo de una instancia de repetición específica desde **fuera** del grupo de repetición usando `indexed-repeat(repeatedField, repeatGroup, index)`:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | first_name | | `indexed-repeat(${member_name}, ${household_members}, 1)` |
| calculate | second_name | | `indexed-repeat(${member_name}, ${household_members}, 2)` |

Esto es útil para construir campos de resumen o referenciar los datos del miembro "principal" después de la repetición.

---

## Posición de la instancia actual: `index()`

Dentro de un grupo de repetición, `index()` devuelve la posición basada en 1 de la instancia actual. Úselo para etiquetar cada repetición o crear identificadores únicos:

| type | name | label |
|------|------|-------|
| begin_repeat | plots | Parcela |
| note | plot_label | Número de parcela ${index()} |
| text | plot_id | ID de parcela |
| end_repeat | | |

---

## Referenciar campos en la misma instancia

Dentro de una repetición, use `${fieldname}` para referenciar otro campo **en la misma instancia de repetición**. No es necesario usar `indexed-repeat()` dentro del mismo bucle:

| type | name | label | relevant |
|------|------|-------|----------|
| begin_repeat | members | Miembro | |
| text | member_name | Nombre | |
| integer | member_age | Edad | |
| text | school_name | Nombre de la escuela | `${member_age} < 18` |
| end_repeat | | | |

---

## Referenciar campos padre desde dentro de una repetición

Los campos fuera (por encima) del grupo de repetición se pueden referenciar normalmente con `${fieldname}`:

| type | name | label |
|------|------|-------|
| text | village | Nombre del pueblo |
| begin_repeat | plots | Parcela agrícola |
| note | plot_context | Parcelas en ${village} |
| end_repeat | | |

---

## Resumen de datos de repetición

Use funciones de agregado de repetición **fuera** del grupo de repetición para resumir:

| Función | Ejemplo | Descripción |
|---------|---------|-------------|
| `count(group)` | `count(${household_members})` | Número de instancias |
| `sum(field)` | `sum(${loan_amount})` | Suma de un campo numérico |
| `min(field)` | `min(${member_age})` | Valor mínimo |
| `max(field)` | `max(${member_age})` | Valor máximo |
| `join(sep, field)` | `join(', ', ${member_name})` | Lista separada por comas |
| `count-if(group, expr)` | `count-if(${members}, ${member_age} < 18)` | Conteo condicional |
| `sum-if(field, expr)` | `sum-if(${loan_amount}, ${loan_amount} > 500)` | Suma condicional |
| `join-if(sep, field, expr)` | `join-if(', ', ${name}, ${age} >= 18)` | Unión condicional |

### Ejemplo: Resumen del hogar

| type | name | label | calculation |
|------|------|-------|-------------|
| integer | num_members | ¿Cuántos miembros? | |
| begin_repeat | members | Miembro | `${num_members}` |
| text | member_name | Nombre | |
| integer | member_age | Edad | |
| end_repeat | | | |
| calculate | total_members | | `count(${members})` |
| calculate | children_count | | `count-if(${members}, ${member_age} < 18)` |
| calculate | adult_names | | `join-if(', ', ${member_name}, ${member_age} >= 18)` |
| note | summary | ${total_members} miembros; ${children_count} menores de 18. Adultos: ${adult_names} | |

---

## Repeticiones anidadas

Un grupo de repetición puede contener otro grupo de repetición. Úselo con cuidado; las repeticiones anidadas agregan complejidad y pueden ser confusas para los encuestadores.

| type | name | label |
|------|------|-------|
| begin_repeat | households | Hogar |
| text | hh_id | ID del hogar |
| begin_repeat | hh_members | Miembro |
| text | member_name | Nombre del miembro |
| end_repeat | | |
| end_repeat | | |

Para referenciar un campo en una repetición exterior desde la repetición interior, use `${fieldname}`; se resuelve al ancestro coincidente más cercano:

Dentro de la repetición `hh_members`, `${hh_id}` devuelve el ID del hogar **actual**, no todos los hogares.

---

## Rango dentro de grupos de repetición: `rank-index()`

Cuando existe un campo `rank` dentro de una repetición, use `rank-index(instanceNumber, repeatedField)` desde fuera para obtener el rango ordinal de una instancia específica:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | top_scorer | | `rank-index(1, ${score})` |

`rank-index(1, ${score})` devuelve el índice de instancia de la puntuación más alta.

---

## Mejores prácticas

1. Siempre use `repeat_count` cuando el número de repeticiones se conozca de antemano; evita que los encuestadores agreguen o eliminen instancias accidentalmente.
2. Mantenga los grupos de repetición enfocados; una repetición con más de 20 preguntas por instancia es difícil de navegar.
3. Nombre los grupos de repetición de forma clara (p. ej., `household_members`, no `repeat1`); el nombre aparece en las llamadas de función y los datos exportados.
4. Pruebe con el número máximo esperado de instancias para verificar el rendimiento.
5. Use la apariencia `field-list` en el grupo de repetición para mostrar todos los campos en una pantalla por instancia (móvil).

---

## Limitaciones

- `indexed-repeat()` requiere un índice válido (1 al conteo de instancias); los índices fuera de rango devuelven vacío.
- Las repeticiones anidadas más allá de 2 niveles no se recomiendan y pueden causar problemas de visualización en algunos clientes.
- Las funciones de agregado (`sum`, `count`, etc.) operan sobre todo el grupo de repetición; no puede agregar un subconjunto de instancias sin las variantes `*-if`.
