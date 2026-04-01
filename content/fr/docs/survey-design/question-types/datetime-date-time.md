---
title: "Datetime, date, time (Date et heure)"
description: "Les questions de type datetime permettent aux répondants de saisir à la fois la date et l'heure dans un seul champ."
icon: "event"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 226
---

Le type de question `datetime` dans XLSForms et rtSurvey permet aux répondants de saisir à la fois la date et l'heure dans un seul champ. Ce type de question est utile lorsque vous devez capturer un moment précis dans le temps, incluant à la fois la date et l'heure exacte.

## Spécification XLSForm de Base

| type     | name           | label                           |
|----------|----------------|--------------------------------|
| datetime | event_datetime | Quand l'événement s'est-il produit ? |

Pour plus de détails sur le type de question `datetime` de base, consultez la [spécification XLSForm](https://xlsform.org/en/#question-types).

## Utilisations

Les questions `datetime` sont couramment utilisées pour :

1. Enregistrer l'horodatage d'événements ou d'observations
2. Planifier des rendez-vous ou des réunions
3. Journaliser les heures de début et de fin d'activités
4. Capturer des moments précis pour la collecte de données sensibles au temps

## Extensions rtSurvey

rtSurvey étend les fonctionnalités des questions `datetime` avec diverses apparences et options de personnalisation :

### Options d'Apparence

- `(par défaut)` : Affiche le calendrier et l'horloge pour sélectionner la date et l'heure
- `inline` : Affiche le calendrier et l'horloge sous forme d'icônes
- `inline-1line` : Affiche le calendrier et l'horloge pour la sélection dans un format à une seule ligne
- `inline-onlyresult` : Affiche le calendrier et l'horloge sous forme d'icônes en fin de ligne ; les icônes disparaissent après la sélection

### Personnalisation des Couleurs

Vous pouvez personnaliser la couleur des icônes du calendrier et de l'horloge en utilisant la fonction `colors()` :

- `inline colors("0099FF")` : Affiche les icônes avec une couleur personnalisée
- `inline-1line-0000FF` : Affiche le format sur une seule ligne avec une couleur personnalisée
- `inline-1line colors("0000FF","FFFF00")` : Affiche le format sur une seule ligne avec plusieurs couleurs personnalisées
- `inline-onlyresult colors("0099FF")` : Affiche des icônes qui disparaissent après sélection, avec une couleur personnalisée

### Formats de Date et d'Heure Personnalisés

rtSurvey permet des formats de date et d'heure personnalisés en utilisant une syntaxe spéciale :

- `inline-[%Y-%m-%d %H:%M:%S]` : Exemple de format personnalisé (Année-Mois-Jour Heure:Minute:Seconde)
- `inline-[%d/%m/%Y %I:%M %p]` : Exemple de format personnalisé (Jour/Mois/Année Heure:Minute AM/PM)

## Exemple d'Utilisation

Voici un exemple de la manière dont vous pourriez utiliser une question `datetime` dans une enquête :

| type     | name           | label                                      | appearance                    |
|----------|----------------|--------------------------------------------|-----------------------------|
| datetime | incident_time  | Quand l'incident s'est-il produit ?        | inline-[%d/%m/%Y %I:%M %p]  |

## Meilleures Pratiques

1. Fournissez des instructions claires sur le format de date et d'heure attendu.
2. Envisagez d'utiliser l'apparence `inline` pour un affichage plus compact.
3. Utilisez des formats personnalisés lorsque vous avez besoin de composants de date et d'heure ou d'un formatage spécifiques.
4. Soyez attentif aux fuseaux horaires lors de la collecte de données `datetime` dans différentes régions.

## Limitations

- Certaines apparences ou certains formats personnalisés peuvent ne pas être pris en charge sur tous les appareils ou plateformes.
- Les utilisateurs peuvent avoir besoin d'aide pour saisir correctement la date et l'heure, en particulier avec des formats personnalisés.
- Les différences de fuseau horaire peuvent compliquer l'analyse des données si elles ne sont pas correctement prises en compte.
