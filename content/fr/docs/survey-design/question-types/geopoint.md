---
title: "Geopoint"
description: "Les questions de type geopoint capturent les coordonnées géographiques (latitude, longitude, altitude et précision) dans le cadre de l'enquête."
icon: "location_on"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 232
---

Le type de question `geopoint` dans XLSForms et rtSurvey permet la collecte de coordonnées géographiques à l'aide du GPS de l'appareil ou d'autres services de localisation. Cette fonctionnalité est particulièrement utile pour cartographier les réponses à l'enquête, suivre les activités sur le terrain ou associer des données à des emplacements spécifiques.

## Spécification XLSForm de Base

| type     | name        | label                           |
|----------|-------------|--------------------------------|
| geopoint | location    | Enregistrer l'emplacement actuel |

Pour plus de détails sur le type de question `geopoint` de base, consultez la [spécification XLSForm](https://xlsform.org/en/#question-types).

## Utilisations

Les questions `geopoint` sont couramment utilisées pour :

1. Cartographier géographiquement les réponses à l'enquête
2. Vérifier l'emplacement des activités sur le terrain
3. Suivre l'itinéraire des enquêteurs
4. Associer des données environnementales ou sociales à des emplacements spécifiques
5. Calculer des distances ou des zones dans le cadre d'analyses géographiques

## Meilleures Pratiques

1. Assurez-vous que l'appareil a activé les services de localisation et que les autorisations sont accordées.
2. Laissez suffisamment de temps au GPS pour obtenir une position précise.
3. Tenez compte des implications en matière de confidentialité et informez les répondants de la collecte de données de localisation.
4. Utilisez en conjonction avec d'autres types de questions pour fournir un contexte aux données de localisation.

## Exemple d'Utilisation

Voici un exemple de la manière dont vous pourriez utiliser une question `geopoint` dans une enquête :

| type     | name           | label                                      | hint                                        |
|----------|----------------|--------------------------------------------|--------------------------------------------|
| geopoint | sample_location| Enregistrer l'emplacement du prélèvement    | Tenez-vous dans une zone dégagée pour un meilleur signal GPS |

## Extensions rtSurvey

Bien que la spécification XLSForm de base pour les questions `geopoint` soit simple, rtSurvey peut proposer des fonctionnalités ou des personnalisations supplémentaires :

1. Intégration de cartes pour une confirmation visuelle de l'emplacement capturé
2. Paramètres de seuil de précision
3. Option de saisie manuelle des coordonnées
4. Intégration de cartes hors ligne pour les zones reculées

(Note : Les extensions spécifiques disponibles dans rtSurvey pour les questions `geopoint` devront être confirmées et détaillées ici.)

## Format des Données

Les données `geopoint` sont généralement stockées sous forme d'une chaîne de quatre valeurs séparées par des espaces :

```
latitude longitude altitude précision
```

Par exemple :
```
41.40338 2.17403 30.5 10
```

## Considérations pour l'Analyse

Lors de l'utilisation de questions `geopoint`, tenez compte de :

1. La manière dont les données géographiques seront visualisées (ex : logiciel de cartographie)
2. La précision des coordonnées collectées et son impact sur l'analyse
3. Les mesures de confidentialité et de protection des données pour la manipulation des données de localisation
4. L'intégration potentielle avec des outils SIG (Système d'Information Géographique)

## Limitations

- La précision peut varier en fonction de l'appareil et des conditions environnementales.
- Les signaux GPS peuvent être faibles ou indisponibles à l'intérieur des bâtiments ou dans les zones présentant des obstructions.
- La collecte de données de localisation peut avoir un impact significatif sur la durée de vie de la batterie de l'appareil.
- Des préoccupations en matière de confidentialité peuvent être associées à la collecte de données de localisation précises.
