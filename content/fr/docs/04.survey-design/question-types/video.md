---
title: "Vidéo (Video)"
description: "Les questions de type vidéo permettent aux répondants d'enregistrer et de soumettre des fichiers vidéo dans le cadre de l'enquête."
icon: "videocam"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 229
---

Le type de question `video` dans XLSForms et rtSurvey permet aux répondants d'enregistrer et de soumettre des fichiers vidéo dans le cadre de leurs réponses à l'enquête. Cette fonctionnalité est particulièrement utile pour capturer des preuves visuelles, des démonstrations ou des témoignages pertinents pour l'enquête.

## Spécification XLSForm de Base

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| video | demo_video  | Veuillez enregistrer une courte vidéo de démonstration |

Pour plus de détails sur le type de question `video` de base, consultez la [spécification XLSForm](https://xlsform.org/en/#question-types).

## Utilisations

Les questions vidéo sont couramment utilisées pour :

1. Capturer des preuves visuelles lors d'enquêtes sur le terrain
2. Enregistrer des démonstrations de produits ou des scénarios d'utilisation
3. Collecter des témoignages vidéo
4. Documenter des processus ou des procédures
5. Permettre aux répondants de fournir des explications visuelles détaillées

## Meilleures Pratiques

1. Fournissez des instructions claires sur ce qu'il faut enregistrer et pendant combien de temps.
2. Tenez compte des implications en matière de confidentialité et informez les répondants de la manière dont leur vidéo sera utilisée.
3. Soyez attentif à la taille des fichiers et aux limitations de stockage, en particulier pour les enquêtes dans des zones où la connectivité Internet est limitée.
4. Testez la fonction d'enregistrement vidéo sur différents appareils pour garantir la compatibilité.
5. Pensez à préciser la qualité ou la résolution vidéo souhaitée dans les instructions.

## Exemple d'Utilisation

Voici un exemple de la manière dont vous pourriez utiliser une question vidéo dans une enquête :

| type  | name           | label                                                | hint                                    |
|-------|----------------|------------------------------------------------------|----------------------------------------|
| video | product_demo   | Veuillez enregistrer une courte démo de l'utilisation du produit | Enregistrez pendant 30 à 60 secondes, en montrant les fonctionnalités clés |

## Extensions rtSurvey

Bien que la spécification XLSForm de base pour les questions vidéo soit simple, rtSurvey peut proposer des fonctionnalités ou des personnalisations supplémentaires :

1. Réglage de la durée maximale d'enregistrement
2. Options de qualité vidéo (ex : basse, moyenne, haute)
3. Fonction de lecture pour révision avant soumission
4. Intégration avec l'application d'enregistrement vidéo native de l'appareil
5. Option de téléchargement de fichiers vidéo existants au lieu d'en enregistrer de nouveaux

(Note : Les extensions spécifiques disponibles dans rtSurvey pour les questions vidéo devront être confirmées et détaillées ici.)

## Limitations

- Les fichiers vidéo peuvent être très volumineux, ce qui peut avoir un impact significatif sur le transfert et le stockage des données.
- Tous les appareils ne prennent pas forcément en charge les capacités d'enregistrement vidéo ou peuvent avoir un stockage limité.
- L'analyse des réponses vidéo peut prendre beaucoup de temps et nécessiter des logiciels spécialisés.
- Les préoccupations en matière de confidentialité peuvent être plus prononcées avec la collecte de données vidéo.

## Manipulation des Données

Les fichiers vidéo collectés via ce type de question sont typiquement :

1. Enregistrés dans un format vidéo courant (ex : MP4, MOV)
2. Stockés aux côtés des autres données d'enquête, souvent dans un dossier média séparé
3. Accessibles pour lecture et analyse via la plateforme de gestion d'enquête

## Considérations pour l'Analyse

Lors de l'utilisation de questions vidéo, tenez compte de :

1. La manière dont les données vidéo seront analysées (ex : examen manuel, analyse vidéo automatisée)
2. Le temps et les ressources supplémentaires nécessaires pour traiter les réponses vidéo
3. Les mesures de confidentialité et de protection des données pour le stockage et la manipulation des enregistrements vidéo
4. Le besoin potentiel d'outils de montage ou de compilation vidéo lors de la phase d'analyse
