---
title: "Estilo HTML"
description: "rtSurvey admite etiquetas HTML en etiquetas e indicaciones, permitiendo formato de texto enriquecido, enlaces y temas de color dinámicos."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 297
---

rtSurvey renderiza el texto de **etiqueta** e **indicación** como HTML en formularios web. Esto significa que puede usar etiquetas HTML estándar para formatear texto, agregar saltos de línea, crear enlaces y aplicar colores. Esto es particularmente útil para campos de nota, instrucciones de sección y resúmenes dinámicos.

{{% alert icon=" " context="warning" %}}
El HTML en etiquetas se renderiza en el **formulario web** y las aplicaciones móviles rtSurvey. Es posible que no se renderice en todos los clientes compatibles con ODK. Siempre pruebe en su plataforma de destino.
{{% /alert %}}

---

## Etiquetas HTML admitidas

### Formato de texto

| Etiqueta | Resultado |
|---------|-----------|
| `<strong>texto</strong>` o `<b>texto</b>` | **Texto en negrita** |
| `<em>texto</em>` o `<i>texto</i>` | *Texto en cursiva* |
| `<u>texto</u>` | Texto subrayado |
| `<br>` | Salto de línea |
| `<span style="...">texto</span>` | Estilo en línea |

### Enlaces

```html
<a href="https://ejemplo.com" target="_blank">Haga clic aquí</a>
```

Se abre en una nueva pestaña. Úselo para documentos de referencia, directrices o recursos externos que el encuestador debe consultar.

### Colores

Use `<span>` con estilos en línea:

```html
<span style="color: red;">Advertencia: el valor está fuera de rango</span>
<span style="color: #009688;">Sección completada</span>
```

---

## Variables de tema de color

rtSurvey admite **tokens de tema de color** que se adaptan al tema configurado de la aplicación. Use la sintaxis `__COLOR_THEME_NAME__`:

```html
<span style="color: var(--color-theme-primary);">Texto en color primario</span>
```

O usando el token abreviado en el texto de la etiqueta:

```
<font color="var(--COLOR_THEME_PRIMARY)">Nota importante</font>
```

Esto se convierte automáticamente al `<span>` equivalente con una variable CSS en el momento del renderizado.

---

## Etiquetas multilingües

Envuelva el contenido en etiquetas de idioma para admitir múltiples idiomas en una sola celda de etiqueta:

```
<en>Enter the household size</en><vi>Nhập quy mô hộ gia đình</vi>
```

rtSurvey extrae el contenido que coincide con el idioma actual de la aplicación. Si no se encuentra ninguna etiqueta de idioma coincidente, se muestra la cadena completa tal cual.

---

## Ejemplos en campos de nota

### Instrucción de sección con negrita y salto de línea

| type | name | label |
|------|------|-------|
| note | section_intro | `<strong>Sección 3: Uso del suelo</strong><br>Haga todas las preguntas de esta sección solo al jefe del hogar.` |

### Resumen dinámico con referencia de cálculo

| type | name | label |
|------|------|-------|
| calculate | total | | `${adults} + ${children}` |
| note | summary | `Total de miembros del hogar: <strong>${total}</strong><br><span style="color: gray;">Adultos: ${adults} · Niños: ${children}</span>` |

### Advertencia en rojo

| type | name | label | relevant |
|------|------|-------|----------|
| note | age_warning | `<span style="color: red;"><strong>Advertencia:</strong> La edad ingresada (${age}) es inusualmente alta. Por favor verifique.</span>` | `${age} > 100` |

### Enlace a un documento de referencia

| type | name | label |
|------|------|-------|
| note | guidelines_link | `Consulte las <a href="https://docs.example.com/guidelines" target="_blank">Directrices de Campo</a> antes de comenzar esta sección.` |

---

## Etiquetas HTML especiales de rtSurvey

### `<webbox src='url' title='titulo'>...</webbox>`

Incrusta un botón que abre una URL en un modal dentro del formulario. Consulte [Webbox](webbox) para obtener detalles completos.

### `<delete-repeat-current>etiqueta</delete-repeat-current>`

Renderiza un botón dentro de un grupo de repetición que elimina la instancia de repetición actual cuando se toca.

### `<delete-repeat-last>etiqueta</delete-repeat-last>`

Renderiza un botón que elimina la última instancia de repetición.

Ejemplo de uso en un grupo de repetición:

| type | name | label |
|------|------|-------|
| note | delete_btn | `<delete-repeat-current>Eliminar este miembro</delete-repeat-current>` |

---

## Mejores prácticas

1. Use HTML con moderación; las etiquetas demasiado formateadas son más difíciles de leer, no más fáciles.
2. Prefiera `<strong>` para negrita y `<em>` para cursiva sobre los obsoletos `<b>` e `<i>`.
3. Mantenga el uso del color significativo: use rojo para advertencias, no para decoración.
4. Siempre pruebe el renderizado HTML tanto en la aplicación móvil como en el formulario web, ya que el renderizado puede diferir ligeramente.
5. Evite las etiquetas `<table>` dentro de las etiquetas; rara vez se renderizan bien en pantallas móviles.
6. No use JavaScript (`<script>`); será eliminado o causará errores.

## Limitaciones

- El HTML complejo (tablas, formularios, scripts) no es compatible y puede romper el renderizado.
- Algunos clientes móviles más antiguos pueden mostrar las etiquetas HTML como texto literal; pruebe en todos los dispositivos de destino.
- Los enlaces `<a>` se abren en un navegador o WebView; el encuestador sale del formulario, lo que puede ser disruptivo en móvil.
