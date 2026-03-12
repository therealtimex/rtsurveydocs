---
title: "Apparence"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

La colonne `appearance` dans rtSurvey vous permet de personnaliser la présentation visuelle et le comportement des questions dans vos enquêtes. Cette fonctionnalité améliore l'expérience utilisateur et peut augmenter considérablement l'efficacité de la collecte de données. rtSurvey prend en charge les attributs d'apparence standard de XLSForm et les étend avec des options supplémentaires.

## Attributs d'Apparence Standard XLSForm

rtSurvey prend en charge les attributs d'apparence standard XLSForm suivants :

| Attribut d'apparence | Types de questions | Description |
|----------------------|--------------------|-------------|
| multiline | text | Crée une boîte de texte multiligne (mieux pour les clients web) |
| minimal | select_one, select_multiple | Affiche les choix dans un menu déroulant |
| quick | select_one | Avance automatiquement à la question suivante après la sélection (mobile uniquement) |
| no-calendar | date | Supprime l'affichage du calendrier (mobile uniquement) |
| month-year | date | Permet la sélection du mois et de l'année uniquement |
| year | date | Permet la sélection de l'année uniquement |
| horizontal-compact | select_one, select_multiple | Affiche les choix horizontalement (web uniquement) |
| horizontal | select_one, select_multiple | Affiche les choix horizontalement en colonnes (web uniquement) |
| likert | select_one | Présente les choix sous forme d'échelle de Likert |
| compact | select_one, select_multiple | Affiche les choix côte à côte avec un espacement minimal |
| quickcompact | select_one | Combine l'affichage compact avec l'avance automatique (mobile uniquement) |
| field-list | groups | Affiche tout le groupe sur un seul écran (mobile uniquement) |
| label | select_one, select_multiple | Affiche les étiquettes de choix sans les entrées |
| list-nolabel | select_one, select_multiple | Affiche les entrées sans étiquettes (à utiliser avec `label`) |
| table-list | groups | Affiche les questions sous forme de tableau |
| signature | image | Permet la capture de signature (mobile uniquement) |
| draw | image | Permet le dessin à main levée (mobile uniquement) |
| map, quick map | select_one, select_one_from_file | Permet la sélection à partir d'entités sur une carte |

## Meilleures Pratiques pour l'Utilisation de l'Apparence

1. **Cohérence** : Utilisez les attributs d'apparence de manière cohérente dans toute votre enquête pour un aspect uniforme.
2. **Mobile vs. Web** : Considérez comment les apparences s'afficheront sur différents appareils et plateformes.
3. **Performance** : Soyez prudent avec les attributs d'apparence qui pourraient ralentir le chargement du formulaire (ex: `table-list` pour de grands groupes).
4. **Expérience Utilisateur** : Choisissez des apparences qui rendent la saisie des données plus facile et plus intuitive pour les répondants.
5. **Tests** : Testez toujours votre formulaire sur les appareils cibles pour vous assurer que les apparences fonctionnent comme prévu.

## Techniques Avancées

### Combinaison d'Apparences

Certains attributs d'apparence peuvent être combinés pour des mises en page plus complexes :

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Sélectionner : | minimal compact |
```

### Apparences Dynamiques

rtSurvey permet des changements d'apparence dynamiques basés sur la logique du formulaire :

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Entrer l'heure : | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Considérations pour l'Application Mobile

- Certaines apparences (ex: `quick`, `signature`) sont spécifiques aux appareils mobiles.
- Testez soigneusement sur Android et iOS pour garantir un comportement cohérent.

## Limitations Connues

- Les apparences complexes peuvent ne pas s'afficher de manière identique sur toutes les plateformes.
- Certaines apparences avancées de rtSurvey peuvent ne pas être prises en charge en mode hors ligne.

## Dépannage des Problèmes d'Apparence

1. **Apparence non appliquée** : Vérifiez les fautes de frappe dans la colonne appearance.
2. **Rendu incohérent** : Vérifiez la compatibilité avec le type de question et la plateforme.
3. **Problèmes de performance** : Envisagez de simplifier les apparences complexes, surtout pour les enquêtes volumineuses.
