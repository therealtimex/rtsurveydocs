---
title: "Fichier (File)"
description: "Les questions de type fichier permettent aux répondants de télécharger des fichiers dans le cadre de leurs réponses à l'enquête."
icon: "upload_file"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 230
---

Le type de question `file` dans XLSForms et rtSurvey permet aux répondants de télécharger des fichiers dans le cadre de leurs réponses à l'enquête. Cette fonctionnalité est particulièrement utile pour collecter des documents, des images ou d'autres types de fichiers pertinents pour l'enquête.

## Spécification XLSForm de Base

| type | name      | label                       |
|------|-----------|----------------------------|
| file | document  | Veuillez télécharger votre document |

Pour plus de détails sur le type de question `file` de base, consultez la [spécification XLSForm](https://xlsform.org/en/#question-types).

## Utilisations

Les questions de type fichier sont couramment utilisées pour :

1. Collecter des documents justificatifs (ex : reçus, certificats)
2. Rassembler des preuves visuelles (ex : photos des conditions sur le terrain)
3. Télécharger des formulaires ou des feuilles de calcul complétés
4. Collecter tout type de fichier numérique pertinent pour l'enquête

## Meilleures Pratiques

1. Fournissez des instructions claires sur le type de fichier à télécharger et sur les limitations de taille éventuelles.
2. Tenez compte des implications en matière de confidentialité et informez les répondants de la manière dont leurs fichiers seront utilisés et stockés.
3. Soyez attentif à la taille des fichiers et aux limitations de stockage, en particulier pour les enquêtes dans des zones où la connectivité Internet est limitée.
4. Spécifiez les formats de fichiers acceptés si nécessaire.

## Exemple d'Utilisation

Voici un exemple de la manière dont vous pourriez utiliser une question de type fichier dans une enquête :

| type | name           | label                                      | hint                                        |
|------|----------------|--------------------------------------------|--------------------------------------------|
| file | receipt_upload | Veuillez télécharger une photo de votre reçu | Formats acceptés : JPG, PNG. Taille max : 5 Mo |

## Extensions rtSurvey

Bien que la spécification XLSForm de base pour les questions de type fichier soit simple, rtSurvey peut proposer des fonctionnalités ou des personnalisations supplémentaires :

1. Restrictions sur le type de fichier (ex : uniquement des images, uniquement des PDF)
2. Limitations sur la taille des fichiers
3. Possibilité de télécharger plusieurs fichiers
4. Intégration avec le système de fichiers de l'appareil ou les services de stockage en nuage (cloud)

(Note : Les extensions spécifiques disponibles dans rtSurvey pour les questions de type fichier devront être confirmées et détaillées ici.)

## Manipulation des Données

Les fichiers collectés via ce type de question sont typiquement :

1. Enregistrés dans leur format d'origine
2. Stockés aux côtés des autres données d'enquête, souvent dans un dossier média séparé
3. Accessibles pour téléchargement et analyse via la plateforme de gestion d'enquête

## Considérations pour l'Analyse

Lors de l'utilisation de questions de type fichier, tenez compte de :

1. La manière dont les fichiers téléchargés seront traités et analysés
2. L'espace de stockage supplémentaire requis pour les fichiers joints
3. Les mesures de confidentialité et de protection des données pour le stockage et la manipulation des fichiers téléchargés
4. Le besoin potentiel de logiciels spécialisés pour ouvrir ou analyser certains types de fichiers

## Limitations

- Les fichiers volumineux peuvent avoir un impact significatif sur le transfert de données et les exigences de stockage.
- Tous les appareils ne permettent pas forcément un accès facile aux fichiers pour le téléchargement.
- L'analyse des fichiers joints peut prendre plus de temps que les réponses textuelles.
- Il peut y avoir des problèmes de compatibilité avec certains types de fichiers entre différents systèmes.
