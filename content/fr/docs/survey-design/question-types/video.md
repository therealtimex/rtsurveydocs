---
title: "Video"
description: "Les questions vidéo permettent aux répondants d'enregistrer et de soumettre des fichiers vidéo dans le cadre de l'enquête."
icon: "videocam"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 229
---

Le type de question `video` permet aux répondants d'**enregistrer une vidéo** ou de téléverser un fichier vidéo existant dans leur réponse à l'enquête. Il est utile pour capturer des preuves visuelles, des démonstrations, des conditions environnementales ou toute information qui bénéficie du mouvement et du son ensemble.

## Spécification XLSForm de base

| type  | name        | label                              |
|-------|-------------|-------------------------------------|
| video | demo_video  | Veuillez enregistrer une courte démonstration |

Pour plus de détails sur le type de question vidéo standard, consultez la [spécification XLSForm](https://xlsform.org/en/#question-types).

## Utilisations

Les questions vidéo sont couramment utilisées pour :

1. Documenter les conditions de terrain — dommages routiers, état des infrastructures, santé des cultures
2. Enregistrer des démonstrations de produits ou des vérifications de conformité procédurale
3. Collecter des témoignages vidéo auprès des répondants
4. Capturer des preuves nécessitant un contexte spatial (ex. : taille et étendue d'une zone problématique)
5. Documentation avant/après pour les enquêtes de suivi et d'évaluation

## Format des données

Les fichiers vidéo sont stockés comme pièces jointes binaires :

- **Format :** MP4 ou MOV (enregistrement mobile)
- **Nommage :** `{instanceID}-{fieldname}.mp4` (ou équivalent)
- **Stockage :** Téléversé dans le dossier média du serveur et lié à l'enregistrement de soumission
- **Accès :** Lisible et téléchargeable depuis l'interface de gestion des soumissions

## Extensions rtSurvey

### Durée maximale

Utilisez la colonne `parameters` pour limiter la durée d'enregistrement :

| type | name | label | parameters |
|------|------|-------|------------|
| video | site_visit | Enregistrer les conditions du site | `max-duration=60` |

`max-duration` est en secondes. L'enregistrement s'arrête automatiquement à la limite.

### Qualité / résolution

Contrôlez la résolution d'enregistrement via `parameters` :

| type | name | label | parameters |
|------|------|-------|------------|
| video | evidence | Enregistrer une preuve vidéo | `quality=low` |

Valeurs supportées : `low` (téléversement plus rapide), `normal` (par défaut), `high`. Utilisez `low` dans les zones à connectivité limitée.

### Téléverser une vidéo existante

Sur mobile, le répondant peut choisir de **téléverser une vidéo existante** depuis la galerie de l'appareil plutôt que d'en enregistrer une nouvelle. Cette option est activée par défaut dans l'intégration native appareil-photo/galerie.

### Lecture avant soumission

Sur mobile, le clip enregistré peut être revu avant de continuer. Aucune configuration supplémentaire n'est nécessaire.

## Exemple d'utilisation

### Vidéo d'inspection de site avec limite

| type | name | label | hint | parameters |
|------|------|-------|------|------------|
| video | site_video | Enregistrer le point d'eau | Faites le tour de toute l'installation. Maximum 90 secondes. | `max-duration=90 quality=normal` |

### Vidéo conditionnelle — uniquement si des dommages sont signalés

| type | name | label | relevant | required |
|------|------|-------|----------|----------|
| select_one yesno | damage_found | Des dommages ont-ils été constatés ? | | |
| video | damage_video | Enregistrer une vidéo des dommages | `${damage_found} = 'yes'` | `${damage_found} = 'yes'` |

## Bonnes pratiques

1. Définissez `max-duration` — les enregistrements vidéo sans restriction peuvent facilement dépasser 100 Mo et échouer au téléversement sur des connexions faibles.
2. Utilisez `quality=low` pour les enquêtes de suivi où une preuve visuelle est requise mais le détail fin n'est pas nécessaire — cela réduit considérablement la taille du fichier.
3. Rédigez des instructions d'enregistrement spécifiques dans la colonne `hint` (ex. : "Faites le tour du bâtiment entier, tenez l'appareil photo stable").
4. Demandez-vous si la vidéo est nécessaire — une photo (`image`) est généralement suffisante pour les preuves statiques et produit des fichiers beaucoup plus petits.
5. Testez les performances de téléversement sur le réseau terrain réel avant le déploiement.

## Limitations

- Les fichiers vidéo sont très volumineux — une vidéo d'1 minute en qualité normale représente généralement 20-60 Mo selon l'appareil.
- Le téléversement de fichiers vidéo volumineux nécessite une bonne connexion réseau ; envisagez d'exiger une synchronisation Wi-Fi pour les formulaires à forte densité vidéo.
- Tous les navigateurs web ne supportent pas l'enregistrement vidéo via MediaRecorder — Chrome est le plus fiable.
- L'analyse des réponses vidéo est manuelle et chronophage ; utilisez-les avec parcimonie et uniquement lorsque le contenu vidéo apporte une valeur unique.
