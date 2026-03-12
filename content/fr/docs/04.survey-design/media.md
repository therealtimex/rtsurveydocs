---
title: "Médias"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 286
---

rtSurvey prend en charge l'intégration de médias riches dans les enquêtes, vous permettant d'améliorer vos questionnaires avec des images, de l'audio et de la vidéo. Cette fonctionnalité peut considérablement améliorer l'expérience du répondant et la qualité des données collectées.

## Types de Médias Pris en Charge

rtSurvey prend en charge les types de médias suivants :
- Images (jpg, png, gif)
- Audio (mp3, wav)
- Vidéo (mp4, webm)

## Ajouter des Médias à votre Enquête

Pour inclure des médias dans votre formulaire rtSurvey, utilisez les colonnes suivantes dans votre XLSForm :

- `image` : Pour afficher des images
- `audio` : Pour lire des fichiers audio
- `video` : Pour lire des fichiers vidéo

Exemple :

```
| type | name          | label         | image        | audio       | video       |
|------|---------------|---------------|--------------|-------------|-------------|
| note | media_example | Exemple média | example.jpg  | sound.mp3   | clip.mp4    |
```

## Gestion des Fichiers Multimédias

### Enquêtes en ligne (Web)
Pour les enquêtes sur le web, rtSurvey fournit une interface de gestion des médias où vous pouvez télécharger et organiser vos fichiers multimédias. Ces fichiers sont ensuite automatiquement disponibles pour être utilisés dans vos enquêtes.

### Application mobile
Lors de l'utilisation de l'application mobile rtSurvey :
1. Placez vos fichiers multimédias dans le dossier `/rtSurvey/forms/[nom-du-formulaire]-media/` sur votre appareil.
2. Référencez le nom exact du fichier dans votre XLSForm.

## Fonctionnalités Spécifiques à rtSurvey

### Chargement Dynamique de Médias
rtSurvey prend en charge le chargement dynamique de médias en fonction des réponses à l'enquête :

```
| type         | name      | label              | image                    |
|--------------|-----------|--------------------|--------------------------| 
| select_one species | animal | Sélectionner un animal | ${animal}.jpg            |
```

### Médias dans les Options de Choix
rtSurvey vous permet d'utiliser des médias dans les options de choix pour les questions de sélection :

```
| type                | name    | label           | media::image |
|---------------------|---------|-----------------|--------------|
| select_one_from_file animals | Choisir un animal |              |
```

Dans la feuille choices :
```
| list_name | name  | label | media::image |
|-----------|-------|-------|--------------|
| animals   | dog   | Chien | dog.jpg      |
| animals   | cat   | Chat  | cat.jpg      |
```

### Capture de Médias
rtSurvey étend XLSForm avec des capacités de capture de médias :

```
| type  | name        | label               |
|-------|-------------|---------------------|
| image | photo       | Prendre une photo   |
| audio | voice_note  | Enregistrer une note vocale |
| video | video_clip  | Enregistrer une vidéo |
```

## Meilleures Pratiques pour l'Utilisation des Médias

1. **Optimiser la taille des fichiers** : Les fichiers multimédias volumineux peuvent ralentir le chargement et la soumission de l'enquête.
2. **Utiliser des formats appropriés** : Privilégiez les formats largement pris en charge (jpg pour les images, mp3 pour l'audio, mp4 pour la vidéo).
3. **Fournir des alternatives** : Incluez toujours des alternatives textuelles pour l'accessibilité.
4. **Tester soigneusement** : Assurez-vous que les médias s'affichent correctement sur tous les appareils cibles.
5. **Envisager l'utilisation hors ligne** : Pour les enquêtes menées hors ligne, assurez-vous que tous les médias sont disponibles localement.

## Support Multilingue des Médias

rtSurvey prend en charge les médias spécifiques à la langue. Utilisez le suffixe `::langue` :

```
| type | name  | label      | image::English | image::French |
|------|-------|------------|----------------|---------------|
| note | intro | Bienvenue  | welcome_en.jpg | welcome_fr.jpg|
```

## Médias dans l'Exportation des Données

Lors de l'exportation des données de rtSurvey :
- Pour les enquêtes web, les URLs des médias sont incluses dans l'export.
- Pour les enquêtes sur application mobile, les chemins de fichiers sont inclus.

## Considérations pour l'Application Mobile

- Assurez-vous de disposer d'un espace de stockage suffisant sur les appareils pour les enquêtes riches en médias.
- L'application mobile rtSurvey prend en charge la lecture et la capture de médias hors ligne.
- Les fichiers multimédias volumineux peuvent avoir un impact sur les performances de l'application sur les appareils bas de gamme.

## Limitations Connues

- Certains navigateurs plus anciens peuvent ne pas prendre en charge tous les formats de médias.
- Les fichiers vidéo très volumineux peuvent causer des problèmes dans des situations de faible bande passante.

## Dépannage des Problèmes de Médias

1. **Le média ne s'affiche pas** : Vérifiez l'exactitude des chemins et des noms de fichiers.
2. **Problèmes de lecture** : Assurez-vous que le format de média est pris en charge par les appareils cibles.
3. **Chargement lent** : Envisagez d'optimiser la taille des fichiers ou de précharger les médias.

## Fonctionnalités Multimédias Avancées

### Géomarquage (Geotagging)
rtSurvey peut géomarquer automatiquement les médias capturés lors des enquêtes :

```
| type  | name        | label        | appearance |
|-------|-------------|--------------|------------|
| image | photo       | Prendre une photo | geotag     |
```

### Annotations de Médias
Permettre aux répondants d'annoter des images :

```
| type  | name        | label        | appearance |
|-------|-------------|--------------|------------|
| image | photo       | Annoter l'image | annotate |
```

En utilisant efficacement les médias dans vos formulaires rtSurvey, vous pouvez créer des enquêtes plus attrayantes, informatives et précises. N'oubliez pas de trouver un équilibre entre les avantages de l'inclusion de médias et les considérations de performance, en particulier pour les enquêtes déployées dans des zones à connectivité internet limitée ou sur des appareils bas de gamme.
