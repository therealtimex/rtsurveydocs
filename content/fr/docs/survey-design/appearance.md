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

La colonne `appearance` dans rtSurvey vous permet de personnaliser la présentation visuelle et le comportement des questions dans vos enquêtes. Cette fonctionnalité améliore l'expérience utilisateur et peut considérablement améliorer l'efficacité de la collecte de données. rtSurvey prend en charge les attributs d'apparence standard de XLSForm et les étend avec des options supplémentaires.

## Attributs d'apparence standard XLSForm

rtSurvey prend en charge les attributs d'apparence standard XLSForm suivants :

| Attribut d'apparence | Types de questions | Description |
|----------------------|----------------|-------------|
| multiline | text | Crée une zone de texte multi-lignes (idéale pour les clients web) |
| minimal | select_one, select_multiple | Affiche les choix dans un menu déroulant |
| quick | select_one | Passe automatiquement à la question suivante après sélection (mobile uniquement) |
| no-calendar | date | Supprime l'affichage du calendrier (mobile uniquement) |
| month-year | date | Permet la sélection du mois et de l'année uniquement |
| year | date | Permet la sélection de l'année uniquement |
| horizontal-compact | select_one, select_multiple | Affiche les choix horizontalement (web uniquement) |
| horizontal | select_one, select_multiple | Affiche les choix horizontalement en colonnes (web uniquement) |
| likert | select_one | Présente les choix sous forme d'échelle de Likert |
| compact | select_one, select_multiple | Affiche les choix côte à côte avec espacement minimal |
| quickcompact | select_one | Combine l'affichage compact avec l'avance automatique (mobile uniquement) |
| field-list | groups | Affiche tout le groupe sur un seul écran (mobile uniquement) |
| label | select_one, select_multiple | Affiche les étiquettes de choix sans les saisies |
| list-nolabel | select_one, select_multiple | Affiche les saisies sans étiquettes (à utiliser avec `label`) |
| table-list | groups | Affiche les questions sous forme de tableau |
| signature | image | Active la capture de signature (mobile uniquement) |
| draw | image | Permet le dessin à main levée (mobile uniquement) |
| map, quick map | select_one, select_one_from_file | Active la sélection à partir d'entités sur une carte |

## Bonnes pratiques pour l'utilisation de l'apparence

1. **Cohérence** : Utilisez les attributs d'apparence de manière cohérente dans toute votre enquête pour un aspect uniforme.
2. **Mobile vs. web** : Considérez comment les apparences s'afficheront sur différents appareils et plateformes.
3. **Performance** : Soyez prudent avec les attributs d'apparence qui pourraient ralentir le chargement du formulaire (ex. : `table-list` pour de grands groupes).
4. **Expérience utilisateur** : Choisissez des apparences qui rendent la saisie de données plus facile et plus intuitive pour les répondants.
5. **Tests** : Testez toujours votre formulaire sur les appareils cibles pour vous assurer que les apparences fonctionnent comme prévu.

## Techniques avancées

### Combiner des apparences

Certains attributs d'apparence peuvent être combinés pour des mises en page plus complexes :

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Sélectionner un : | minimal compact |
```

### Apparences dynamiques

rtSurvey permet des changements d'apparence dynamiques basés sur la logique du formulaire :

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Saisir l'heure : | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Considérations pour l'application mobile

- Certaines apparences (ex. : `quick`, `signature`) sont spécifiques aux appareils mobiles.
- Testez soigneusement sur Android et iOS pour garantir un comportement cohérent.

## Attributs d'apparence étendus rtSurvey

En plus des apparences standard XLSForm, rtSurvey prend en charge les options spécifiques à la plateforme suivantes :

### Contrôle des données et de l'affichage

| Attribut d'apparence | Types de questions | Description |
|----------------------|----------------|-------------|
| `invisible` | tout | Masque le champ de la vue tout en collectant ou calculant sa valeur. Différent du type `hidden` — le champ participe toujours à la logique. |
| `displaytitle` | tout | Force l'affichage de l'étiquette/titre du champ même lorsqu'il serait normalement supprimé. |
| `autopull` | select_one, select_multiple | Récupère automatiquement des données externes pour peupler les choix au chargement du formulaire ou lorsqu'un champ déclencheur change. |
| `floating_hint` | text, integer, decimal | Affiche le texte d'aide comme une étiquette flottante au-dessus du champ de saisie plutôt qu'en dessous. |
| `calculate-button` | calculate | Ajoute un bouton visible qui déclenche le recalcul du champ à la demande, plutôt qu'automatiquement. |

### Mise en page

| Attribut d'apparence | Types de questions | Description |
|----------------------|----------------|-------------|
| `1screen` | group | Force l'affichage de tout le groupe sur un seul écran quelle que soit la taille du groupe. |
| `columns(n)` | select_one, select_multiple | Affiche les choix en `n` colonnes. Exemple : `columns(3)` affiche trois colonnes de boutons radio. |
| `gridformat<row=R col=C colspan=S align=center>` | tout | Positionne le champ dans une mise en page CSS grid à la ligne `R`, colonne `C`, en s'étendant sur `S` colonnes. Utilisé avec `advanced-extension/grid-layout`. |
| `ignore-simplify` | tout | Indique au moteur de rendu de formulaire d'ignorer la simplification ou la condensation automatique de la mise en page de ce champ. |

### Widgets

| Attribut d'apparence | Types de questions | Description |
|----------------------|----------------|-------------|
| `likert` | select_one | Présente les choix sous forme d'une ligne d'échelle de Likert (déjà dans le tableau standard ci-dessus ; confirmé comme pris en charge). |
| `distress` | select_one | Affiche les choix sous forme du widget visuel de l'échelle de détresse psychologique de Kessler (K10) avec des icônes émotionnelles. |

### Intégration API

| Attribut d'apparence | Types de questions | Description |
|----------------------|----------------|-------------|
| `callapi` | text, integer, decimal, select_one | Active l'intégration d'appel API pour ce champ. La colonne calculation doit contenir une expression `callapi()`. Voir [Call API](advanced-extension/call-api). |
| `callapi-verify(params)` | text, integer, decimal | Déclenche un appel de vérification API avec des paramètres statiques. Le formulaire bloque la progression jusqu'à ce que l'API confirme la valeur. |
| `callapi-verify(dynamicParams)` | text, integer, decimal | Identique à `callapi-verify` mais avec des paramètres dérivés des valeurs d'autres champs au moment de l'exécution. |

### Format de date/heure inline

Pour les champs `date`, `time` et `datetime`, vous pouvez spécifier un format d'affichage personnalisé en utilisant une chaîne de format ajoutée à l'apparence :

```
inline-[%d/%m/%Y]
inline-1line-[%d/%m/%Y %H:%M]
```

Les jetons de format sont les mêmes que pour `format-date()` et `format-date-time()`. Voir [Fonctions — Fonctions de date et heure](operators-and-functions/functions#date-and-time-functions).

Exemple :

| type | name | label | appearance |
|------|------|-------|------------|
| datetime | event_time | Date et heure de l'événement | inline-[%d/%m/%Y %I:%M %p] |
| date | birth_date | Date de naissance | inline-[%d/%m/%Y] |

## Limitations connues

- Les apparences complexes peuvent ne pas s'afficher de manière identique sur toutes les plateformes.
- Certaines apparences avancées rtSurvey peuvent ne pas être prises en charge en mode hors ligne.

## Résolution des problèmes d'apparence

1. **Apparence non appliquée** : Vérifiez les fautes de frappe dans la colonne appearance.
2. **Rendu incohérent** : Vérifiez la compatibilité avec le type de question et la plateforme.
3. **Problèmes de performance** : Envisagez de simplifier les apparences complexes, surtout pour les grandes enquêtes.
