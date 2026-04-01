---
title: "Extensions avancées"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 289
---

La colonne `appearance` dans rtSurvey vous permet de personnaliser la présentation visuelle et le comportement des questions dans vos enquêtes. Cette fonctionnalité améliore l'expérience utilisateur et peut augmenter considérablement l'efficacité de la collecte des données. rtSurvey prend en charge les attributs d'apparence standard de XLSForm et les étend avec des options supplémentaires.

## Extensions d'apparence spécifiques à rtSurvey

rtSurvey étend les options d'apparence standard avec les éléments suivants :

### Personnalisation de la saisie de l'heure

Pour les questions de type `text` utilisées pour la saisie de l'heure :

- `appearance:` - Affiche une horloge pour sélectionner les heures et les minutes
- `appearance: inline` - Affiche l'horloge sous forme d'icône
- `appearance: inline-1line` - Affiche l'horloge dans un format à une seule ligne
- `appearance: inline-onlyresult` - Affiche l'icône de l'horloge, disparaît après la sélection
- `appearance: inline-[FORMAT]` - Personnalise l'affichage du format de l'heure (ex : `[%H:%M]`, `[%h:%M:%S]`)

### Personnalisation des couleurs

rtSurvey permet de personnaliser les couleurs pour diverses apparences :

- `appearance: inline colors("0099FF")` - Personnalise la couleur de l'icône
- `appearance: inline-1line colors("0000FF","FFFF00")` - Personnalise les couleurs dans le format à une seule ligne

### Mise en page en grille (Grid Layout)

rtSurvey introduit une mise en page en grille pour les affichages compacts de type tableau :

- `appearance: grid` - S'applique aux groupes pour créer une mise en page en grille

### Groupes compressibles (Collapsible Groups)

- `appearance: collapsible` - Crée des groupes extensibles/compressibles

## Meilleures pratiques pour l'utilisation de l'apparence

1. **Cohérence** : Utilisez les attributs d'apparence de manière cohérente dans toute votre enquête pour un aspect uniforme.
2. **Mobile vs Web** : Réfléchissez au rendu des apparences sur différents appareils et plateformes.
3. **Performance** : Soyez prudent avec les attributs d'apparence qui pourraient ralentir le chargement du formulaire (ex : `table-list` pour les grands groupes).
4. **Expérience Utilisateur** : Choisissez des apparences qui facilitent la saisie des données et la rendent plus intuitive pour les répondants.
5. **Tests** : Testez toujours votre formulaire sur les appareils cibles pour vous assurer que les apparences fonctionnent comme prévu.

## Techniques avancées

### Combinaison d'apparences

Certains attributs d'apparence peuvent être combinés pour des mises en page plus complexes :

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Sélectionnez-en un : | minimal compact |
```

### Apparences dynamiques

rtSurvey permet des changements d'apparence dynamiques basés sur la logique du formulaire :

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Entrez l'heure : | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Considérations sur l'Appli Mobile

- Certaines apparences (ex : `quick`, `signature`) sont spécifiques aux appareils mobiles.
- Testez soigneusement sur Android et iOS pour garantir un comportement cohérent.

## Limitations connues

- Les apparences complexes peuvent ne pas s'afficher de manière identique sur toutes les plateformes.
- Certaines apparences avancées de rtSurvey peuvent ne pas être prises en charge en mode hors connexion.

## Dépannage des problèmes d'apparence

1. **Apparence non appliquée** : Vérifiez les fautes de frappe dans la colonne `appearance`.
2. **Rendu incohérent** : Vérifiez la compatibilité avec le type de question et la plateforme.
3. **Problèmes de performance** : Envisagez de simplifier les apparences complexes, en particulier pour les grandes enquêtes.
