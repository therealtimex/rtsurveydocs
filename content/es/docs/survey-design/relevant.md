---
title: "Omisión de preguntas"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 280
---

La lógica de salto, también conocida como ramificación o lógica condicional, le permite crear encuestas dinámicas que se adaptan a las respuestas de los encuestados. En rtSurvey, la lógica de salto se implementa usando la columna `relevant` en su XLSForm.

## Lógica de salto básica

Para implementar la lógica de salto básica, use la columna `relevant` para especificar una condición:

```
| type           | name          | label                       | relevant            |
|----------------|---------------|-----------------------------|--------------------|
| select_one y_n | likes_pizza   | ¿Le gusta la pizza?         |                    |
| select_multiple pizza_toppings | favorite_topping | Ingredientes favoritos | ${likes_pizza} = 'yes' |
```

En este ejemplo, la pregunta "Ingredientes favoritos" solo aparece si el encuestado responde "sí" a que le gusta la pizza.

## Sintaxis para expresiones relevantes

- Use `${ }` para hacer referencia a otras variables de pregunta.
- Para preguntas `select_one`, compare directamente: `${question_name} = 'answer'`
- Para preguntas `select_multiple`, use la función `selected()`.

## Lógica de salto avanzada

### Condiciones múltiples

Puede combinar múltiples condiciones usando `and`, `or` y paréntesis:

```
| type    | name  | label                   | relevant                                  |
|---------|-------|-------------------------|-------------------------------------------|
| integer | age   | ¿Cuántos años tiene?    |                                           |
| text    | school| ¿A qué escuela asiste?  | ${age} < 18 and (${location} = 'urban' or ${location} = 'suburban') |
```

### Uso de preguntas select_multiple

Para preguntas `select_multiple`, use la función `selected()`:

```
| type           | name          | label                       | relevant                               |
|----------------|---------------|-----------------------------|-----------------------------------------|
| select_multiple pizza_toppings | favorite_topping | Ingredientes favoritos |                                         |
| text           | cheese_type   | Tipo de queso favorito      | selected(${favorite_topping}, 'cheese') |
```

### Opción "Otro" en opción múltiple

Implemente una opción "Otro" de texto libre usando `relevant`:

```
| type           | name                  | label                               | relevant                               |
|----------------|----------------------|-------------------------------------|---------------------------------------|
| select_multiple pizza_toppings | favorite_toppings | ¿Cuáles son sus ingredientes de pizza favoritos? |                                       |
| text           | favorite_toppings_other | ¿Qué otros ingredientes le gustan? | selected(${favorite_toppings}, 'other') |
```

Recuerde incluir 'other' como opción en la hoja de trabajo choices.

## Características específicas de rtSurvey

### Relevancia dinámica

rtSurvey permite la relevancia dinámica basada en campos calculados:

```
| type      | name       | label              | calculation                   |
|-----------|------------|--------------------|-----------------------------|
| calculate | total_score| Puntuación total   | ${score1} + ${score2} + ${score3} |
| text      | feedback   | Comentarios        | ${total_score} > 75             |
```

### Relevancia en repeticiones

rtSurvey admite la relevancia dentro de grupos repetitivos:

```
| type         | name         | label            | relevant               |
|--------------|--------------|------------------|------------------------|
| begin repeat | child_info   | Información del niño |                    |
| integer      | child_age    | Edad del niño    |                        |
| text         | school_name  | Nombre de la escuela | ${child_age} >= 5  |
| end repeat   |              |                  |                        |
```

### Relevancia en cascada

rtSurvey maneja eficientemente la relevancia en cascada, donde la relevancia de una pregunta depende de otra, que a su vez depende de una tercera:

```
| type           | name        | label                  | relevant               |
|----------------|-------------|------------------------|------------------------|
| select_one y_n | has_car     | ¿Tiene un automóvil?   |                        |
| select_one car_type | car_type | ¿Qué tipo de automóvil? | ${has_car} = 'yes'  |
| text           | model       | Modelo específico      | ${car_type} = 'sedan'  |
```

## Mejores prácticas para la lógica de salto en rtSurvey

1. **Mantenga la simplicidad**: Evite condiciones de relevancia demasiado complejas cuando sea posible.
2. **Pruebe exhaustivamente**: Use la función de vista previa de rtSurvey para probar todos los posibles caminos a través de su encuesta.
3. **Considere el rendimiento**: La lógica de salto muy compleja puede afectar el rendimiento de la encuesta, especialmente en dispositivos móviles.
4. **Use nombres de variables claros**: Esto hace que sus expresiones de relevancia sean más fáciles de leer y mantener.
5. **Documente su lógica**: Agregue notas para explicar patrones de salto complejos, especialmente para la colaboración en equipo.
6. **Sea consciente del análisis de datos**: Las preguntas omitidas resultarán en datos faltantes. Planifique su análisis en consecuencia.

## Solución de problemas de lógica de salto

- **Errores de sintaxis**: Asegúrese de que todos los `${ }` estén correctamente cerrados y escritos correctamente.
- **Referencias circulares**: Evite crear bucles donde las preguntas dependen entre sí.
- **Distinción entre mayúsculas y minúsculas**: Recuerde que las opciones de respuesta distinguen entre mayúsculas y minúsculas en las expresiones de relevancia.
- **Comparaciones numéricas**: Use los operadores apropiados (`<`, `>`, `=`) para las comparaciones numéricas.

## Conclusión

El uso efectivo de la lógica de salto puede mejorar significativamente la experiencia del encuestado y la calidad de los datos en sus proyectos de rtSurvey. Al aprovechar las funciones avanzadas de rtSurvey y seguir las mejores prácticas, puede crear encuestas dinámicas y eficientes que se adapten a la situación única de cada encuestado.
