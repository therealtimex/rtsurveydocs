---
title: "Wiederholungen (Repeats)"
description: ""
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 294
---

Die dynamische Suche (Dynamic Search) ist eine leistungsstarke Funktion in rtSurvey, mit der Sie dynamische Suchfunktionen in Ihre Umfragen integrieren können, um Daten in Echtzeit aus externen Quellen abzurufen.

## Syntax

Die grundlegende Syntax für die Verwendung der `search-api` lautet:

```
search-api(method, url, post_body, value_column, display, data_path, save_path)
```

### Parameter

- `method`: Verwenden Sie immer 'POST'
- `url`: Die URL zum Abrufen der Daten
- `post_body`: Der Anfragetext. Verwenden Sie die searchView-Syntax (siehe Dokumentation zu DataModel-Ansichten)
- `value_column`: Das Datenfeld, das als Wert verwendet werden soll
- `display`: Das Datenfeld, das als Label verwendet werden soll. Unterstützt eine Vorlagen-Syntax mit `##key##` und `@{func}` für erweiterte Formatierung
- `data_path`: JSONPath, um die gewünschten Daten aus der Antwort zu extrahieren (z. B. `$.hits.hits.*._source`)
- `save_path`: Ort zum Speichern der Antwortdaten für die spätere Verwendung

## Anwendungsbeispiele

### Grundlegende Verwendung

```
appearance: search-api('POST', 'https://api.example.com/search', '{"query": "%__input__%"}', 'id', 'name', '$.results', 'search_results')
```

### Mit erweiterter Anzeigeformatierung

```
appearance: search-api('POST', 'https://api.example.com/search', '{"query": "%__input__%"}', 'id', '##name## (##age## Jahre alt)', '$.results', 'search_results')
```

### Mit Funktion in der Anzeige

```
appearance: search-api('POST', 'https://api.example.com/search', '{"query": "%__input__%"}', 'id', '@{if_else(eq("##status##", "active"), "Aktiv: ##name##", "Inaktiv: ##name##")}', '$.results', 'search_results')
```

## Unterstützte Fragetypen

- `select_one`
- `select_multiple`
- `text` (für Autocomplete-Funktionalität)

## Zusätzliche Funktionen

### Standard-API (Default API)

Verwenden Sie `search-default-api()` nach `search-api()`, um Standardwerte festzulegen:

```
appearance: search-api(...) search-default-api(...)
```

### Trennzeichen für Mehrfachauswahl

Verwenden Sie für `select_multiple` `search-default-separator()`, um ein benutzerdefiniertes Trennzeichen anzugeben:

```
appearance: search-api(...) search-default-separator(' || ')
```

## Best Practices

1. Optimieren Sie API-Endpunkte für die Leistung, insbesondere bei großen Datensätzen.
2. Verwenden Sie geeignete Caching-Strategien, um API-Aufrufe zu reduzieren.
3. Gehen Sie in Ihrem Umfragedesign elegant mit Netzwerkfehlern um.
4. Testen Sie gründlich mit verschiedenen Eingabeszenarien.

## Bekannte Einschränkungen

- Komplexe Abfragen können die Ladezeiten der Umfrage beeinflussen.
- Die Offline-Funktionalität kann je nach Implementierung eingeschränkt sein.

```mermaid
    graph TD
    %% Define styles for nodes
    classDef light fill:#cce5ff,stroke:#0066cc,stroke-width:2px,color:#003366
    classDef dark fill:#2e3b4e,stroke:#a6b1c2,stroke-width:2px,color:#e1e1e1
    classDef submit fill:#ffcc99,stroke:#cc6600,stroke-width:2px,color:#663300
    classDef link fill:#ccffcc,stroke:#009933,stroke-width:2px,color:#003300
    classDef storage fill:#ffffcc,stroke:#999900,stroke-width:2px,color:#333300
    
    %% Define shapes for nodes
    A[<span class="iconify" data-icon="mdi:file-document-multiple" data-inline="false" data-width="18" data-height="18"></span> Receipts in PDF, PNG, HEIC, JPEG, Excel] --> B{<span class="iconify" data-icon="mdi:send" data-inline="false" data-width="18" data-height="18"></span> Submit the Receipts}
    B --> C1([<a href="mailto:keep@keepy.us?subject=Keep%20my%20receipts" style="color:#003300;"><span class="iconify" data-icon="mdi:email" data-inline="false" data-width="18" data-height="18"></span> Email: keep@keepy.us</a>])
    B --> C2([<a href="sms:+16504173562" style="color:#003300;"><span class="iconify" data-icon="mdi:message-text" data-inline="false" data-width="18" data-height="18"></span> SMS: 650-417-3562</a>])
    B --> C3([<a href="https://m.me/keepy.us" target="_blank" style="color:#003300;"><span class="iconify" data-icon="mdi:facebook-messenger" data-inline="false" data-width="18" data-height="18"></span> Messenger: m.me/keepy.us</a>])
    C1 --> D[[<span class="iconify" data-icon="mdi:database" data-inline="false" data-width="18" data-height="18"></span> <b>Receipt Data Stored in Google Sheet</b><br> - Automatic Text Recognition<br> - Human-Verified for Accuracy<br> - Data and Digital Receipt Copies]]
    C2 --> D
    C3 --> D
    
    %% Apply classes to nodes
    class A light
    class B submit
    class C1 link
    class C2 link
    class C3 link
    class D storage
    
    %% Adjust arrow styles for better visibility
    linkStyle default stroke:#666,stroke-width:3px
```
