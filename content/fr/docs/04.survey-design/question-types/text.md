---
title: "Texte (Text)"
description: "Type de question de réponse textuelle libre dans rtSurvey"
icon: "text_fields"
date: "2024-07-01T12:00:00+01:00"
lastmod: "2024-07-01T12:00:00+01:00"
draft: false
toc: true
weight: 221
---

## Présentation

Le type de question `text` dans rtSurvey permet des réponses textuelles libres, offrant une flexibilité pour collecter divers types de données textuelles. Il est basé sur la spécification XLSForm standard mais inclut des extensions spécifiques à rtSurvey pour des fonctionnalités améliorées.

## Spécification XLSForm

Dans XLSForm, le type de question texte est spécifié comme suit :

```
type: text
```

Pour plus de détails sur la syntaxe XLSForm standard, reportez-vous à la [documentation officielle de XLSForm](https://xlsform.org/en/#question-types).

## Extensions spécifiques à rtSurvey

rtSurvey étend les fonctionnalités du type de question `text` via diverses options d'apparence, particulièrement pour la saisie de l'heure :

### Extensions pour la saisie de l'heure

- `appearance:` - Affiche une horloge pour sélectionner les heures et les minutes
- `appearance: inline` - Affiche l'horloge sous forme d'icône
- `appearance: inline colors("0099FF")` - Affiche l'horloge sous forme d'icône avec une couleur personnalisable
- `appearance: inline-1line` - Affiche l'horloge pour la sélection dans un format à une seule ligne
- `appearance: inline-1line-0000FF` - Format sur une seule ligne avec une couleur personnalisable
- `appearance: inline-1line colors("0000FF","FFFF00")` - Format sur une seule ligne avec plusieurs options de couleur
- `appearance: inline-onlyresult` - Affiche l'horloge sous forme d'icône à la fin de la ligne, disparaissant après la sélection
- `appearance: inline-onlyresult colors("0099FF")` - Identique au cas précédent, avec une couleur d'icône personnalisable

### Extensions pour le format de l'heure

- `appearance: inline-[%3]` - Affiche les millisecondes
- `appearance: inline-[%S]` - Affiche les secondes
- `appearance: inline-[%M]` - Affiche les minutes
- `appearance: inline-[%h]` - Affiche les heures (format 12 heures)
- `appearance: inline-[%H]` - Affiche les heures (format 24 heures)
- `appearance: inline-[%H-%M-%S]` - Affiche l'heure au format HH-MM-SS
- `appearance: inline-[%H:%M:%3]` - Affiche l'heure au format HH:MM:millisecondes
- `appearance: inline-[%h:%M:%S]` - Affiche l'heure au format 12 heures avec les secondes
- `appearance: inline-[%H:%M]` - Affiche l'heure au format 24 heures
- `appearance: inline-[%h:%M]` - Affiche l'heure au format 12 heures
- `appearance: inline-[%M:%S]` - Affiche les minutes et les secondes
- `appearance: inline-[%M:%3]` - Affiche les minutes et les millisecondes

## Format des Données

Les données textuelles sont stockées et exportées sous forme de texte. Pour les saisies basées sur l'heure, les données sont stockées dans un format de date/heure basé sur le texte.

## Considérations sur l'Appli Mobile

Le type de question `text`, y compris toutes ses variantes et apparences, est entièrement pris en charge sur les plateformes iOS, Android et Web.

## Types de Questions Connexes

- Entiers (Integers)
- Date et heure (Datetime)

## Meilleures Pratiques

- Utilisez des étiquettes claires et concises pour les questions textuelles afin de guider les répondants.
- Envisagez d'utiliser des contraintes ou des règles de validation pour garantir la qualité des données.
- Pour les saisies d'heure, choisissez l'option d'apparence appropriée en fonction du niveau de précision requis pour votre enquête.

## Limitations Connues

Actuellement, il n'y a pas de limitations connues pour le type de question `text` dans rtSurvey.

## Captures d'écran

[Note : Inclure des captures d'écran pertinentes pour illustrer les différentes apparences et variantes du type de question texte.]
