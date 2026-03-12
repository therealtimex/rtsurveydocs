---
title: "Audio"
description: "Les questions audio permettent aux répondants d'enregistrer et de soumettre des fichiers audio dans le cadre de l'enquête."
icon: "mic"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 228
---

Le type de question audio dans XLSForms et rtSurvey permet aux répondants d'enregistrer et de soumettre des fichiers audio dans le cadre de leurs réponses à l'enquête. Cette fonctionnalité est particulièrement utile pour capturer des réponses verbales, des témoignages ou des sons environnementaux pertinents pour l'enquête.

## Spécification XLSForm de Base

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| audio | voice_note  | Veuillez enregistrer vos commentaires |

Pour plus de détails sur le type de question audio de base, consultez la [spécification XLSForm](https://xlsform.org/en/#question-types).

## Utilisations

Les questions audio sont couramment utilisées pour :

1. Capturer des réponses verbales à des questions ouvertes
2. Enregistrer des témoignages ou des histoires personnelles
3. Documenter des sons environnementaux ou des niveaux de bruit
4. Collecter des échantillons de voix à des fins de recherche
5. Permettre aux répondants de fournir des explications détaillées

## Meilleures Pratiques

1. Fournissez des instructions claires sur ce qu'il faut enregistrer et pendant combien de temps.
2. Tenez compte des implications en matière de confidentialité et informez les répondants de la manière dont leur audio sera utilisé.
3. Soyez attentif à la taille des fichiers et aux limitations de stockage, en particulier pour les enquêtes dans des zones où la connectivité Internet est limitée.
4. Testez la fonction d'enregistrement audio sur divers appareils pour garantir la compatibilité.

## Exemple d'Utilisation

Voici un exemple de la manière dont vous pourriez utiliser une question audio dans une enquête :

| type  | name           | label                                                | hint                                    |
|-------|----------------|------------------------------------------------------|----------------------------------------|
| audio | feedback_audio | Veuillez enregistrer votre avis sur le produit       | Parlez clairement jusqu'à 60 secondes  |

## Extensions rtSurvey

Bien que la spécification XLSForm de base pour les questions audio soit simple, rtSurvey peut proposer des fonctionnalités ou des personnalisations supplémentaires :

1. Réglage de la durée maximale d'enregistrement
2. Options de qualité audio (ex : basse, moyenne, haute)
3. Fonctionnalité de lecture pour révision avant soumission
4. Intégration avec l'application d'enregistrement audio native de l'appareil

(Note : Les extensions spécifiques disponibles dans rtSurvey pour les questions audio devront être confirmées et détaillées ici.)

## Limitations

- Les fichiers audio peuvent être volumineux, ce qui peut avoir un impact sur le transfert et le stockage des données.
- Tous les appareils ne prennent pas forcément en charge les capacités d'enregistrement audio.
- La transcription des réponses audio peut être nécessaire pour l'analyse, ce qui peut prendre du temps.
- Des préoccupations en matière de confidentialité peuvent survenir lors de la collecte de données vocales.

## Manipulation des Données

Les fichiers audio collectés via ce type de question sont typiquement :

1. Enregistrés dans un format audio courant (ex : MP3, WAV)
2. Stockés aux côtés des autres données d'enquête
3. Accessibles pour lecture et analyse via la plateforme de gestion d'enquête

## Considérations pour l'Analyse

Lors de l'utilisation de questions audio, tenez compte de :

1. La manière dont les données audio seront analysées (ex : transcription manuelle, reconnaissance vocale automatisée)
2. Le temps et les ressources supplémentaires nécessaires au traitement des réponses audio
3. Les mesures de confidentialité et de protection des données pour le stockage et la manipulation des enregistrements vocaux
