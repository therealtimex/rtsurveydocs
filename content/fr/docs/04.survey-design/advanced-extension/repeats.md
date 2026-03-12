---
title: "Répétitions (Repeats)"
description: ""
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 294
---

La recherche dynamique (Dynamic Search) est une fonctionnalité puissante de rtSurvey qui vous permet d'intégrer une fonctionnalité de recherche dynamique dans vos enquêtes, permettant la récupération de données en temps réel à partir de sources externes.

## Syntaxe

La syntaxe de base pour l'utilisation de `search-api` est :

```
search-api(method, url, post_body, value_column, display, data_path, save_path)
```

### Paramètres

- `method` : Utilisez toujours 'POST'
- `url` : L'URL pour récupérer les données
- `post_body` : Le corps de la requête. Utilisez la syntaxe searchView (voir la documentation sur les vues DataModel)
- `value_column` : Le champ de données à utiliser comme valeur
- `display` : Le champ de données à utiliser comme étiquette (label). Prend en charge une syntaxe de type modèle avec `##key##` et `@{func}` pour un formatage avancé
- `data_path` : JSONPath pour extraire les données souhaitées de la réponse (ex : `$.hits.hits.*._source`)
- `save_path` : Emplacement pour stocker les données de réponse pour une utilisation ultérieure

## Exemples d'utilisation

### Utilisation de base

```
appearance: search-api('POST', 'https://api.example.com/search', '{"query": "%__input__%"}', 'id', 'name', '$.results', 'search_results')
```

### Avec formatage d'affichage avancé

```
appearance: search-api('POST', 'https://api.example.com/search', '{"query": "%__input__%"}', 'id', '##name## (##age## ans)', '$.results', 'search_results')
```

### Avec fonction dans l'affichage

```
appearance: search-api('POST', 'https://api.example.com/search', '{"query": "%__input__%"}', 'id', '@{if_else(eq("##status##", "active"), "Actif : ##name##", "Inactif : ##name##")}', '$.results', 'search_results')
```

## Types de questions pris en charge

- `select_one`
- `select_multiple`
- `text` (pour la fonctionnalité d'autocomplétion)

## Caractéristiques supplémentaires

### API par défaut (Default API)

Utilisez `search-default-api()` après `search-api()` pour définir des valeurs par défaut :

```
appearance: search-api(...) search-default-api(...)
```

### Séparateur de sélection multiple

Pour `select_multiple`, utilisez `search-default-separator()` pour spécifier un séparateur personnalisé :

```
appearance: search-api(...) search-default-separator(' || ')
```

## Meilleures pratiques

1. Optimisez les points de terminaison de l'API pour la performance, en particulier avec de grands ensembles de données.
2. Utilisez des stratégies de mise en cache appropriées pour réduire les appels API.
3. Gérez les erreurs réseau avec élégance dans la conception de votre enquête.
4. Testez soigneusement avec divers scénarios de saisie.

## Limitations connues

- Les requêtes complexes peuvent impacter les temps de chargement de l'enquête.
- La fonctionnalité hors connexion peut être limitée selon l'implémentation.

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
