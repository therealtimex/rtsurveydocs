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
| `required-but-simplify` | tout | Le champ est obligatoire mais sa mise en page est toujours simplifiée par le moteur de rendu |
| `embed` | tout | Affiche le champ en mode intégré/inline, supprimant son conteneur externe et le conteneur d'étiquettes |
| `popup` | select_one, select_multiple | Affiche la liste des choix dans une superposition popup/modal au lieu d'être inline |
| `auto-hide-empty` | boxtag, select | Masque tout le widget de question quand la liste de choix est vide |
| `text-nolabel` | select_one, select_multiple | Masque l'étiquette de texte pour chaque choix, n'affichant que le contrôle de saisie |

### Widgets

| Attribut d'apparence | Types de questions | Description |
|----------------------|----------------|-------------|
| `likert` | select_one | Présente les choix sous forme d'une ligne d'échelle de Likert (déjà dans le tableau standard ci-dessus ; confirmé comme pris en charge). |
| `distress` | select_one | Affiche les choix sous forme du widget visuel de l'échelle de détresse psychologique de Kessler (K10) avec des icônes émotionnelles. |

### Widgets visuels de sélection

Ces apparences modifient entièrement le rendu des listes de choix de sélection.

| Apparence | Types de questions | Description |
|-----------|-------------------|-------------|
| `tagging` | select_one, select_multiple | Les choix s'affichent sous forme de chips de tags cliquables en forme de pilule. |
| `boxtag` | select_one, select_multiple | Les choix s'affichent sous forme de boîtes rectangulaires stylisées que l'utilisateur tape. |
| `boxtag -search` | select_one, select_multiple | Mise en page boxtag avec une saisie de recherche/filtre en direct au-dessus des boîtes. |
| `duolingo-style1` | select_one, select_multiple | Grand layout de cartes inspiré de Duolingo — adapté aux listes courtes avec icônes. |
| `rating_box` | select_one, select_multiple | Grille de boîtes numérotées tapables — adaptée aux questions d'échelle ou NPS. |
| `star_rating` | select_one | Les choix s'affichent sous forme d'étoiles ; le nombre d'étoiles est égal au nombre de choix. |
| `choices-noshow` | select_one, select_multiple | Affiche initialement seulement les 10 premiers choix avec un contrôle "Afficher plus". |
| `noshow` | select_one, select_multiple | Masque entièrement la liste des choix ; la valeur est définie programmatiquement via calculate ou API. |
| `checkall` | select_multiple | Ajoute un raccourci "Tout sélectionner" en haut de la liste des choix. |
| `max-items(N)` | select_one, select_multiple | Limite la liste de choix visible à N éléments. Exemple : max-items(5). |

### Widgets visuels de texte

| Apparence | Types de questions | Description |
|-----------|-------------------|-------------|
| `richtext` | text | Remplace la zone de texte simple par un éditeur de texte riche (gras, italique, listes, liens). Stocke du HTML. |
| `typingtest` | text | Widget de test de frappe — l'étiquette est le passage ; le widget enregistre la réponse saisie et le timing. |

### Extensions médias

| Apparence | Types de questions | Description |
|-----------|-------------------|-------------|
| `watermark("expression")` | image | Superpose un filigrane textuel sur les photos capturées. L'argument est une expression XPath évaluée au moment de la capture. |
| `editable` | image | Active l'annotation/le dessin sur la photo capturée avant l'enregistrement. |

### Configuration de l'affichage inline

Les modificateurs `display{}` et `results{}` contrôlent l'alignement des icônes et l'affichage des résultats pour les widgets inline.

#### Paramètres de `display{}`

| Paramètre | Valeurs | Description |
|-----------|---------|-------------|
| Alignement | `left`, `right`, `top`, `bottom`, `center` | Position de l'icône par rapport au champ de saisie |
| Taille | `small`, `medium`, `large` | Taille de l'icône |
| Mode | `inline-icon` | Rend le déclencheur sous forme d'icône uniquement |
| Mode | `inline-button` | Rend le déclencheur sous forme de bouton complet |

#### Paramètres de `results{}`

| Paramètre | Valeurs | Description |
|-----------|---------|-------------|
| Alignement | `left`, `right`, `top`, `bottom`, `center` | Position de l'affichage de la valeur résultat |
| `hide(field)` | tout nom de sous-champ | Masque un composant spécifique du résultat |

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
