---
title: "Repeats"
description: ""
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 294
---

Dynamic Search is a powerful feature in rtSurvey that allows you to integrate dynamic search functionality into your surveys, enabling real-time data retrieval from external sources.

## Syntax

The basic syntax for using Search-API is:

```
search-api(method, url, post_body, value_column, display, data_path, save_path)
```

### Parameters

- `method`: Always use 'POST'
- `url`: The URL to fetch data from
- `post_body`: The request body. Use searchView syntax (see DataModel Views documentation)
- `value_column`: The data field to use as the value
- `display`: The data field to use as the label. Supports template-like syntax with `##key##` and `@{func}` for advanced formatting
- `data_path`: JSONPath to extract the desired data from the response (e.g., `$.hits.hits.*._source`)
- `save_path`: Location to store the response data for later use

## Usage Examples

### Basic Usage

```
appearance: search-api('POST', 'https://api.example.com/search', '{"query": "%__input__%"}', 'id', 'name', '$.results', 'search_results')
```

### With Advanced Display Formatting

```
appearance: search-api('POST', 'https://api.example.com/search', '{"query": "%__input__%"}', 'id', '##name## (##age## years old)', '$.results', 'search_results')
```

### With Function in Display

```
appearance: search-api('POST', 'https://api.example.com/search', '{"query": "%__input__%"}', 'id', '@{if_else(eq("##status##", "active"), "Active: ##name##", "Inactive: ##name##")}', '$.results', 'search_results')
```

## Supported Question Types

- `select_one`
- `select_multiple`
- `text` (for autocomplete functionality)

## Additional Features

### Default API

Use `search-default-api()` after `search-api()` to set default values:

```
appearance: search-api(...) search-default-api(...)
```

### Multiple Selection Separator

For `select_multiple`, use `search-default-separator()` to specify a custom separator:

```
appearance: search-api(...) search-default-separator(' || ')
```

## Best Practices

1. Optimize API endpoints for performance, especially with large datasets.
2. Use appropriate caching strategies to reduce API calls.
3. Handle network errors gracefully in your survey design.
4. Test thoroughly with various input scenarios.

## Known Limitations

- Complex queries may impact survey loading times.
- Offline functionality may be limited depending on the implementation.

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