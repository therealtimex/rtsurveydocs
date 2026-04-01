---
title: "File"
description: "Les questions de type fichier permettent aux répondants de téléverser des documents et autres fichiers dans le cadre de leurs réponses à l'enquête."
icon: "upload_file"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 230
---

Le type de question `file` permet aux répondants de **téléverser n'importe quel fichier** depuis leur appareil — documents, tableurs, PDF ou autres types de fichiers. Contrairement à `image`, `audio` et `video` qui lancent des outils de capture spécifiques, `file` ouvre un sélecteur de fichiers polyvalent.

## Spécification XLSForm de base

| type | name      | label                        |
|------|-----------|------------------------------|
| file | document  | Veuillez téléverser votre document  |

Pour plus de détails sur le type de question fichier standard, consultez la [spécification XLSForm](https://xlsform.org/en/#question-types).

## Utilisations

Les questions de type fichier sont couramment utilisées pour :

1. Collecter des documents justificatifs (reçus, certificats, contrats, rapports)
2. Téléverser des formulaires papier scannés
3. Rassembler des tableurs ou des exports de données d'autres systèmes
4. Tout type de fichier numérique non couvert par image/audio/vidéo

## Format des données

Les fichiers téléversés sont stockés comme pièces jointes binaires :

- **Format :** Conservé dans le format d'origine (PDF, XLSX, DOCX, etc.)
- **Nommage :** `{instanceID}-{fieldname}.{extension}`
- **Stockage :** Téléversé dans le dossier média du serveur avec la soumission
- **Accès :** Téléchargeable depuis l'interface de gestion des soumissions

## Extensions rtSurvey

### Types de fichiers acceptés

Utilisez la colonne `parameters` pour restreindre les types de fichiers pouvant être sélectionnés :

| type | name | label | parameters |
|------|------|-------|------------|
| file | report | Téléverser le rapport d'inspection | `accept=.pdf` |
| file | spreadsheet | Téléverser le fichier de données | `accept=.xlsx,.csv` |

Le paramètre `accept` utilise la syntaxe d'extension de fichier standard (séparée par des virgules).

### Guide sur la taille des fichiers

rtSurvey n'impose pas de limite stricte de taille de fichier au niveau de la question, mais la limite de téléversement du serveur s'applique. Utilisez `hint` pour communiquer les attentes à l'enquêteur :

| type | name | label | hint |
|------|------|-------|------|
| file | receipt | Téléverser le reçu de paiement | Accepté : PDF ou image. Taille maximale : 5 Mo |

### Intégration avec le système de fichiers de l'appareil et le stockage cloud

Sur Android et iOS, la question `file` ouvre le sélecteur de fichiers natif de l'appareil, qui peut inclure l'accès à :
- Le stockage local de l'appareil
- La carte SD (Android)
- iCloud Drive (iOS)
- Google Drive, Dropbox (si installés)

Sur le web, il ouvre la boîte de dialogue standard de téléversement de fichiers du navigateur.

## Exemple d'utilisation

### Téléversement de PDF obligatoire

| type | name | label | hint | required | required_message |
|------|------|-------|------|----------|-----------------|
| file | signed_consent | Téléverser le formulaire de consentement signé | PDF uniquement, max 2 Mo | yes | Un formulaire de consentement est obligatoire |

### Téléversement de document conditionnel

| type | name | label | relevant |
|------|------|-------|----------|
| select_one yesno | has_land_title | Le ménage possède-t-il un titre foncier ? | |
| file | land_title_doc | Téléverser une photo ou un scan du titre foncier | `${has_land_title} = 'yes'` |

## Bonnes pratiques

1. Utilisez `accept` pour restreindre les types de fichiers — cela évite aux enquêteurs de téléverser accidentellement de mauvais fichiers.
2. Incluez toujours des indications sur la taille et le format dans la colonne `hint`.
3. Pour les photos et images, utilisez le type `image` à la place — il offre une meilleure compression et une gestion de format cohérente.
4. Pour les grandes enquêtes avec des pièces jointes, planifiez en conséquence votre stockage de données et la bande passante de téléchargement.
5. Testez le sélecteur de fichiers sur le type d'appareil cible (Android vs iOS vs web) avant le déploiement — l'accès aux drives cloud varie.

## Considérations sur la gestion des données

- Les fichiers sont stockés dans leur format d'origine ; ils ne sont pas convertis ou compressés par rtSurvey.
- Analysez les fichiers après téléchargement — rtSurvey n'extrait pas et n'indexe pas le contenu des fichiers.
- Les pièces jointes de grande taille augmentent considérablement le temps nécessaire pour télécharger un jeu de données complet.

## Limitations

- Les questions fichier ne valident pas le contenu des fichiers — seule la vérification de l'extension via `accept` est appliquée au niveau de l'interface.
- Les fichiers très volumineux (100 Mo+) peuvent expirer lors du téléversement dans les environnements à faible connectivité.
- Les enquêteurs hors ligne peuvent joindre des fichiers mais ceux-ci ne seront pas téléversés avant le rétablissement de la connexion.
- Certaines configurations d'appareils restreignent l'accès à certains emplacements de stockage (ex. : politiques MDM d'entreprise).
