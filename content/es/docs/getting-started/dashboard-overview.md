---
weight: 10
date: "2026-03-04T00:00:00+00:00"
draft: false
title: "Descripción general del panel"
icon: "home"
toc: true
description: "Comprensión del panel del sistema RT-CPMS y las herramientas de supervisión de proyectos."
tags: ["Panel", "Descripción general", "Monitoreo"]
---

# El panel del sistema

El panel (`/cpms/cpmsDashBoard/indexNew`) sirve como centro de comando administrativo y página de inicio principal de la plataforma de Encuesta en Tiempo Real (RT-CPMS).

![Vista previa del panel del sistema](/images/dashboard_overview.png)

Está diseñado para ofrecer a los gestores de encuestas una visión general inmediata de los proyectos activos, accesos directos a las herramientas esenciales y un centro centralizado para navegar por todos los módulos principales de la plataforma.

## Características principales

### 1. Selección de proyecto y formulario
El panel izquierdo contiene el navegador de **Formularios e Informes**. Esta área lista todas las encuestas activas en su espacio de trabajo.
* Al seleccionar una encuesta específica (p. ej., *RTA - SURVEY 02*), se dirige el panel para enfocar el monitoreo y las métricas exclusivamente en ese proyecto.

### 2. Filtros de visualización y métricas
Encima de la lista de proyectos, puede alternar entre varias perspectivas de datos críticos para monitorear el progreso del trabajo de campo en tiempo real:
* **Recuento por hora de inicio / hora de finalización**: Rastree cuándo los encuestadores están comenzando y completando sus sesiones de encuesta.
* **Recuento por fecha de envío**: Monitoree el volumen diario general de datos que llegan al servidor.
* **Recuento por nombre de usuario**: Evalúe la productividad y el rendimiento individual de los encuestadores.
* **Mapa de entrevistas**: Vea una distribución geográfica (GIS) de dónde se están recopilando las respuestas de la encuesta para garantizar que se cumplan los requisitos de cobertura espacial.

### 3. Portales de aplicaciones
El centro del panel proporciona acceso instantáneo a las interfaces de recopilación de datos. Según el hardware de sus encuestadores, puede iniciar o dirigirlos a:
* **Aplicación web**: Para la recopilación de datos basada en navegador.
* **Aplicación Android**: Enlace a Google Play Store o APK.
* **Aplicación iOS**: Enlace a Apple App Store.

### 4. Accesos directos a módulos principales
Tres botones de acción prominentes permiten una transición rápida a los módulos operativos más utilizados:
* **Entrada de formularios y datos**: Acceda directamente a la gestión manual de los datos recopilados.
* **Análisis e informes**: Abra la suite de Inteligencia de Negocios (BI) para cruzar y graficar las respuestas de la encuesta.
* **Configuración de permisos**: Ajuste quién tiene acceso a la encuesta activa y qué roles tienen.

### 5. Barra lateral de navegación global
La barra lateral izquierda plegable proporciona acceso al ecosistema completo de módulos de back-end de RT-CPMS. Desde aquí, puede acceder en profundidad a:
* **Configuración**: Gestión del personal y los dispositivos activos.
* **Gestión del trabajo de campo**: Seguimiento de la actividad diaria de los encuestadores.
* **Garantía de calidad**: Implementación y revisión de reglas y marcadores de control de calidad.
* **Entregables finales**: Exportación de conjuntos de datos depurados a CSV, PDF o Stata.
