---
title: "Code-barres"
description: "Les questions de type code-barres permettent de scanner et de capturer des données de codes-barres dans votre enquête."
icon: "qr_code_scanner"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 231
---

Le type de question code-barres dans XLSForms et rtSurvey permet aux utilisateurs de scanner et de capturer des données de codes-barres directement dans l'enquête. Cette fonctionnalité est particulièrement utile pour la gestion des stocks, le suivi des produits ou tout scénario nécessitant une saisie de données rapide et précise d'informations codées.

## Spécification XLSForm de Base

| type    | name          | label                   |
|---------|---------------|-------------------------|
| barcode | product_code  | Scannez le code-barres du produit |

Pour plus de détails sur le type de question code-barres de base, consultez la [spécification XLSForm](https://xlsform.org/en/#question-types).

## Utilisations

Les questions de type code-barres sont couramment utilisées pour :

1. L'identification de produits dans les enquêtes d'inventaire
2. Le suivi des actifs dans les opérations sur le terrain
3. La vérification de billets ou d'identités lors d'événements
4. La saisie rapide de données pour des informations codées

## Extensions rtSurvey

Bien que la spécification XLSForm de base pour les questions de type code-barres soit simple, rtSurvey peut proposer des fonctionnalités ou des personnalisations supplémentaires. Celles-ci pourraient inclure :

1. La prise en charge de plusieurs formats de codes-barres (ex : codes QR, UPC, EAN)
2. L'intégration avec la caméra de l'appareil pour le balayage des codes-barres
3. Une option de saisie manuelle au cas où le code-barres serait endommagé ou ne pourrait pas être scanné

(Note : Les extensions spécifiques disponibles dans rtSurvey pour les questions de type code-barres devront être confirmées et détaillées ici.)

## Meilleures Pratiques

1. Assurez de bonnes conditions d'éclairage pour un balayage précis des codes-barres.
2. Fournissez des instructions claires aux utilisateurs sur la manière de positionner l'appareil pour le balayage.
3. Incluez une option de saisie manuelle comme solution de secours en cas de difficultés de balayage.
4. Testez la fonction de balayage de codes-barres avec divers appareils et types de codes-barres avant de déployer l'enquête.

## Limitations

- La précision du balayage des codes-barres peut varier en fonction de la qualité de la caméra de l'appareil et des conditions environnementales.
- Certains appareils anciens ou d'entrée de gamme peuvent ne pas prendre en charge le balayage des codes-barres.
- Certains types de codes-barres peuvent ne pas être pris en charge, selon l'implémentation.

## Exemple d'Utilisation

Voici un exemple de la manière dont vous pourriez utiliser une question de type code-barres dans une enquête d'inventaire :

| type    | name          | label                   | hint                                      |
|---------|---------------|-------------------------|-------------------------------------------|
| barcode | product_code  | Scannez le code-barres du produit | Positionnez le code-barres dans le cadre |
| integer | quantity      | Entrez la quantité du produit |                                           |
| note    | confirmation  | Produit scanné : ${product_code}. Quantité : ${quantity} |           |

Dans cet exemple, l'enquête capture le code-barres d'un produit, demande la quantité, puis affiche une note de confirmation avec les informations scannées.
