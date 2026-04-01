---
title: "Gestión de calidad"
description: "Monitoree el progreso de la recopilación de datos, vea mapas de entrevistas y analice el rendimiento de los encuestadores."
icon: "cloud"
date: "2023-05-22T00:34:57+01:00"
lastmod: "2023-05-22T00:34:57+01:00"
draft: false
weight: 316
---

El módulo **Gestión de calidad** (accesible a través del panel) proporciona análisis en tiempo real y visualizaciones espaciales para monitorear el progreso de la recopilación de datos y el rendimiento de los encuestadores. Ofrece a los gestores de proyectos una interfaz de vista dividida para cambiar rápidamente entre cuestionarios individuales e informes analíticos personalizados.

![Panel de gestión de calidad](/images/manage_quality.png)

## Descripción general del panel

El panel de gestión de calidad se divide en dos pestañas de navegación principales: **Formularios** e **Informes**. Este menú lateral permite a los usuarios buscar y seleccionar de manera eficiente el conjunto de datos o informe específico que desean analizar.

### Análisis de formularios

Al seleccionar un formulario específico de la lista, el panel proporciona múltiples herramientas de visualización integradas para rastrear la calidad y frecuencia de los envíos:

- **Recuento por hora de inicio:** Un gráfico de barras que visualiza la frecuencia de las entrevistas iniciadas a lo largo del tiempo.
- **Recuento por hora de finalización:** Un gráfico de barras que visualiza cuándo se completaron las entrevistas.
- **Recuento por fecha de envío:** Rastrea el volumen diario de datos sincronizados con el servidor.
- **Recuento por nombre de usuario:** Un gráfico de barras que identifica a los encuestadores de mayor rendimiento según sus recuentos totales de envíos.
- **Mapa de entrevistas:** Un diagrama de dispersión geográfico (impulsado por Leaflet) que muestra las coordenadas GPS de dónde se realizó cada envío, lo que permite a los gestores verificar las ubicaciones del trabajo de campo.

### Informes personalizados

La pestaña **Informes** da acceso a diseños analíticos preconfigurados de R Markdown y otras estadísticas personalizadas. Una vez seleccionado un informe, el área de vista principal carga dinámicamente el análisis generado a través de un visor integrado, lo que permite una verificación estadística más profunda de los datos recopilados.

## Búsqueda y filtrado

Una barra de búsqueda rápida está disponible sobre la lista de la barra lateral, lo que permite a los usuarios encontrar rápidamente formularios o informes específicos por nombre.
