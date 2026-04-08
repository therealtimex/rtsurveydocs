---
title: "Select_one"
description: "Les questions select_one permettent aux répondants de choisir exactement une option dans une liste prédéfinie."
icon: "radio_button_checked"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 224
---

Le type de question `select_one` invite le répondant à choisir **exactement une option** dans une liste prédéfinie. Par défaut, les choix s'affichent sous forme de boutons radio, mais de nombreuses options d'apparence sont disponibles pour modifier la mise en page et le comportement.

## Spécification XLSForm de base

**Feuille survey :**

| type | name | label |
|------|------|-------|
| select_one yesno | consent | Le répondant a-t-il donné son consentement ? |

**Feuille choices :**

| list_name | name | label |
|-----------|------|-------|
| yesno | yes | Oui |
| yesno | no | Non |

Le `listname` dans `select_one listname` doit correspondre à la colonne `list_name` de la feuille choices.

Pour plus de détails, consultez la [spécification XLSForm](https://xlsform.org/en/#question-types).

## Utilisations

Les questions select_one sont utilisées pour :

1. Les questions Oui/Non
2. Les choix multiples à réponse unique (ex. : niveau d'études, genre, situation matrimoniale)
3. Les évaluations catégorielles (ex. : mauvais / passable / bon / excellent)
4. Les sélections en cascade (liées) où les choix sont filtrés selon une réponse précédente
5. La sélection d'un pays, d'une région, d'un district ou d'une autre unité administrative

## Options d'apparence

Spécifiez une valeur dans la colonne `appearance` pour modifier l'affichage des choix :

{{< table >}}
| Appearance | Description |
|------------|-------------|
| *(aucune)* | Boutons radio par défaut, un par ligne |
| `minimal` | Liste déroulante unique au lieu de boutons radio |
| `quick` | Passe automatiquement à la question suivante après sélection (mobile uniquement) |
| `compact` | Grille compacte de choix — le nombre de colonnes s'adapte à la largeur de l'écran |
| `compact-N` | Grille compacte forcée à N colonnes (ex. : `compact-3`) |
| `quickcompact` | Combine `quick` et `compact` |
| `quickcompact-N` | Combine `quick` et `compact` avec N colonnes forcées |
| `horizontal` | Choix disposés en ligne horizontale (web) |
| `horizontal-compact` | Horizontal, espacement compact (web) |
| `likert` | Ligne d'échelle de Likert — étiquettes en haut, boutons radio en bas |
| `label` | Affiche uniquement les étiquettes sans saisie (à utiliser avec `list-nolabel`) |
| `list-nolabel` | Affiche uniquement les saisies sans étiquettes (à utiliser avec `label`) |
| `columns(N)` | Affichage en N colonnes (extension rtSurvey, ex. : `columns(3)`) |
| `distress` | Widget d'icônes émotionnelles de l'échelle de détresse psychologique de Kessler (K10) |
| `search-api(...)` | Recherche dynamique — charge les choix depuis une API au moment de l'exécution |
| `tagging` | Affiche les choix sous forme de chips de tags cliquables au lieu de boutons radio |
| `boxtag` | Affiche les choix sous forme de boîtes rectangulaires stylisées que l'utilisateur tape pour sélectionner |
| `boxtag -search` | Mise en page boxtag avec une saisie de recherche/filtre au-dessus des boîtes |
| `duolingo-style1` | Mise en page de cartes inspirée de Duolingo — grandes cartes tapables avec icônes |
| `rating_box` | Boîtes de notation en grille — idéales pour les choix numériques ou d'échelle |
| `star_rating` | Widget de notation par étoiles — les choix s'affichent sous forme de 1 à N étoiles |
| `choices-noshow` | Affiche uniquement les 10 premiers choix initialement ; révèle le reste à la demande |
| `noshow` | Masque entièrement la liste des choix ; la valeur est définie de manière programmatique |
| `checkall` | Ajoute une option "Tout sélectionner" en haut de la liste |
| `max-items(N)` | Limite le nombre de choix visibles à N (ex. : max-items(5)) |
{{< /table >}}

### Exemple : Échelle de Likert

| type | name | label | appearance |
|------|------|-------|------------|
| select_one satisfaction | service_rating | Dans quelle mesure êtes-vous satisfait du service ? | likert |

### Exemple : Grille compacte 3 colonnes

| type | name | label | appearance |
|------|------|-------|------------|
| select_one regions | region | Sélectionner la région | compact-3 |

## Sélections en cascade

Une sélection en cascade (liée) filtre les choix en fonction de la valeur sélectionnée dans une question précédente. Utilisez la colonne `choice_filter` avec le nom d'une colonne de votre feuille choices.

**survey :**

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one province | province | Sélectionner la province | |
| select_one district | district | Sélectionner le district | province_name = ${province} |

**choices :**

| list_name | name | label | province_name |
|-----------|------|-------|---------------|
| province | nairobi | Nairobi | |
| province | mombasa | Mombasa | |
| district | westlands | Westlands | nairobi |
| district | kasarani | Kasarani | nairobi |
| district | nyali | Nyali | mombasa |
| district | likoni | Likoni | mombasa |

Lorsque le répondant sélectionne `nairobi`, seuls `Westlands` et `Kasarani` apparaissent dans la liste des districts.

{{% alert icon=" " context="warning" %}}
Le nom de colonne utilisé dans `choice_filter` (ex. : `province_name`) doit exister dans la feuille choices. `${province}` fait référence au champ du formulaire nommé `province`.
{{% /alert %}}

## Utiliser la valeur sélectionnée dans des expressions

Référencez la **valeur** sélectionnée (pas l'étiquette) avec `${fieldname}` :

```
relevant: ${consent} = 'yes'
```

Pour obtenir l'étiquette du choix plutôt que la valeur, utilisez `choice-label()` :

```
calculate: choice-label(${education_level}, ${education_level})
```

## Option "Autre" avec texte libre

Un schéma courant consiste à inclure une option "Autre" qui révèle un champ texte :

| type | name | label | relevant |
|------|------|-------|----------|
| select_one occupation | job | Quelle est votre profession ? | |
| text | job_other | Veuillez préciser | `${job} = 'other'` |

**choices :**

| list_name | name | label |
|-----------|------|-------|
| occupation | farmer | Agriculteur |
| occupation | trader | Commerçant |
| occupation | student | Étudiant |
| occupation | other | Autre (veuillez préciser) |

## Bonnes pratiques

1. Gardez des listes courtes et mutuellement exclusives — si les répondants pourraient vouloir plus d'un choix, utilisez `select_multiple` à la place.
2. Mettez la réponse la plus fréquente en premier, ou classez par ordre alphabétique pour les longues listes.
3. Incluez toujours une option "Je ne sais pas" ou "Préfère ne pas répondre" lorsque c'est pertinent.
4. Utilisez `minimal` (liste déroulante) pour les listes de plus de 7-8 choix sur mobile afin d'économiser l'espace à l'écran.
5. Pour les sélections en cascade, ajoutez toutes les colonnes de filtre dans la feuille choices avant de construire le formulaire.

## Limitations

- Un répondant ne peut sélectionner qu'un seul choix — utilisez `select_multiple` pour les questions à réponses multiples.
- L'apparence `likert` fonctionne mieux avec 5-7 choix tenant sur une ligne.
- `quick` (avancement automatique) est réservé au mobile ; il n'a aucun effet sur les formulaires web.
