---
title: "Gestión de envíos"
description: "Revise, gestione y exporte entradas de datos brutos y envíos."
icon: "cloud"
date: "2023-05-22T00:34:57+01:00"
lastmod: "2023-05-22T00:34:57+01:00"
draft: false
weight: 317
---

El módulo **Gestión de envíos** (al que se accede a través del botón **Vista de datos** en la sección Familia de formularios) permite a los gestores de proyectos y supervisores interactuar directamente con los datos brutos entrantes. Sirve como un espacio de trabajo unificado para revisar los envíos de los encuestadores, rastrear identificadores de dispositivos y realizar operaciones de calidad de datos.

![Interfaz de gestión de envíos](/images/manage_submissions.png)

## Descripción general de datos y columnas

La cuadrícula de datos muestra dinámicamente los datos recopilados para un formulario específico. Opera en dos modos principales: **Oficial** (registros finalizados) y **Trabajo** (registros en tiempo real, no finalizados).

### Columnas de datos clave

Independientemente de las preguntas personalizadas definidas en el formulario, la cuadrícula incluye varias columnas de metadatos estándar para ayudar con la auditoría:

- **Enviado por:** Identifica la plataforma de origen del envío (p. ej., FA para aplicación de campo, WEB para formulario web, RS para sistemas remotos).
- **Detalle:** Abre una vista centrada de un solo registro (icono de búsqueda) para inspeccionar cada variable y respuesta enviada para esa instancia.
- **iNota:** Permite a los supervisores adjuntar notas laterales o comentarios internos a un registro específico sin alterar los datos recopilados (representado por un icono de lápiz).
- **Campos de fecha:** Marcas de tiempo que indican cuándo se inició, completó o sincronizó el registro.
- **Archivos adjuntos multimedia:** Enlaces de miniaturas directas a imágenes, firmas o archivos recopilados durante la encuesta.
- **Grupos repetidos:** Enlaces dedicados para acceder a tablas anidadas para preguntas repetidas dentro del formulario padre.

## Acciones de envío

Para facilitar el control activo de la calidad de los datos, la interfaz proporciona un menú desplegable de comandos accionables que se pueden ejecutar en los registros seleccionados:

- **Crear una nueva instancia:** Permite a los administradores ingresar manualmente un nuevo registro de encuesta directamente en la base de datos.
- **Devolver instancia:** Rechaza el registro enviado y encarga al encuestador que vuelva a verificar o recopilar la información.
- **Dar seguimiento a la instancia:** Marca un registro para mayor atención, generalmente enviando una alerta al equipo de campo para aclarar.
- **Exportar a archivo de comandos devueltos / paquete de comandos de seguimiento:** Genera exportaciones por lotes (archivos) que contienen conjuntos de datos marcados específicamente para devoluciones o seguimientos.
- **Convertir a XML:** Transforma el conjunto de datos estructurado de nuevo en su formato XML sin procesar para análisis de backend o integración de sistemas.
- **Reenviar instancias:** (Disponible en modo *Trabajo*) Envía datos no finalizados inmediatamente a otro dispositivo o usuario.
- **Eliminar:** Elimina permanentemente las instancias seleccionadas de la base de datos.
