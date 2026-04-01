---
title: "Répétition de questions"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 260
---

Les répétitions (repeats) sont une fonctionnalité puissante de rtSurvey qui vous permet de collecter le même ensemble d'informations plusieurs fois au sein d'une seule enquête. C'est particulièrement utile pour des scénarios tels que les enquêtes sur les ménages, où vous pourriez avoir besoin de recueillir des données sur plusieurs membres du foyer.

## Structure de Base de la Répétition

Pour créer une répétition dans rtSurvey, utilisez la construction `begin_repeat` et `end_repeat` :

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat |                      |
| text         | name         | Nom de l'enfant      |
| decimal      | birthweight  | Poids à la naissance |
| select_one male_female | sex | Sexe de l'enfant    |
| end repeat   |              |                      |
```

Dans cet exemple, l'utilisateur peut collecter des informations sur plusieurs enfants en ajoutant de nouvelles répétitions dans le formulaire.

## Étiquetage des Répétitions

Bien que la colonne `label` soit optionnelle pour `begin repeat`, l'ajout d'une étiquette peut améliorer la navigation :

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat | Infos Enfant         |
| text         | name         | Nom de l'enfant      |
| decimal      | birthweight  | Poids à la naissance |
| select_one male_female | sex | Sexe de l'enfant    |
| end repeat   |              |                      |
```

rtSurvey affichera "Infos Enfant" comme titre pour chaque instance de répétition.

## Nombre de Répétitions Fixe

Pour spécifier un nombre fixe de répétitions, utilisez la colonne `repeat_count` :

```
| type         | name         | label                | repeat_count |
|--------------|--------------|----------------------|--------------|
| begin repeat | child_repeat | Infos Enfant         | 3            |
| text         | name         | Nom de l'enfant      |              |
| decimal      | birthweight  | Poids à la naissance |              |
| end repeat   |              |                      |              |
```

Ceci créera exactement 3 répétitions d'enfants.

## Nombre de Répétitions Dynamique

rtSurvey prend en charge les nombres de répétitions dynamiques basés sur les réponses précédentes :

```
| type     | name           | label                          | repeat_count       |
|----------|----------------|--------------------------------|--------------------|
| integer  | num_hh_members | Nombre de membres du foyer ?   |                    |
| begin repeat | hh_member  | Membre du foyer                | ${num_hh_members}  |
| text     | name           | Nom                            |                    |
| integer  | age            | Âge                            |                    |
| end repeat |              |                                |                    |
```

## Répétitions Conditionnelles

Vous pouvez utiliser la colonne `relevant` pour afficher conditionnellement les répétitions :

```
| type              | name        | label                     | relevant           |
|-------------------|-------------|---------------------------|---------------------|
| select_one yes_no | has_child   | Des enfants vivent-ils ici ? |                  |
| begin repeat      | child_repeat| Infos Enfant              | ${has_child} = 'yes'|
| text              | name        | Nom de l'enfant           |                     |
| decimal           | birthweight | Poids à la naissance      |                     |
| end repeat        |             |                           |                     |
```

## Fonctionnalités Spécifiques à rtSurvey

### Résumé de Répétition

rtSurvey fournit une vue récapitulative des répétitions. Pour personnaliser le résumé, utilisez un groupe à l'intérieur de la répétition :

```
| type         | name         | label                                    |
|--------------|--------------|------------------------------------------|
| begin repeat | person_repeat|                                          |
| begin group  | person       | ${first_name} ${last_name} - ${age}      |
| text         | first_name   | Prénom                                   |
| text         | last_name    | Nom                                      |
| integer      | age          | Âge                                      |
| end group    |              |                                          |
| end repeat   |              |                                          |
```

### Options d'Apparence de Répétition

rtSurvey propose des options d'apparence supplémentaires pour les répétitions :

- `appearance: field-list` - Affiche toutes les questions d'une répétition sur un seul écran.
- `appearance: table-list` - Présente les répétitions sous forme de tableau.

```
| type         | name         | label            | appearance  |
|--------------|--------------|-------------------|-------------|
| begin repeat | child_repeat | Infos Enfant     | table-list  |
| text         | name         | Nom              |             |
| integer      | age          | Âge              |             |
| end repeat   |              |                   |             |
```

### Répétitions Imbriquées (Nested Repeats)

rtSurvey prend en charge les répétitions imbriquées pour les structures de données complexes :

```
| type         | name           | label                |
|--------------|----------------|----------------------|
| begin repeat | household      | Foyer                |
| text         | hh_name        | Nom du foyer         |
| begin repeat | hh_member      | Membre du foyer      |
| text         | member_name    | Nom du membre        |
| integer      | member_age     | Âge du membre        |
| end repeat   |                |                      |
| end repeat   |                |                      |
```

## Meilleures Pratiques pour l'Utilisation des Répétitions dans rtSurvey

1. Utilisez des noms et des étiquettes significatifs pour les répétitions afin d'améliorer l'analyse des données.
2. Envisagez d'utiliser des nombres de répétitions dynamiques pour réduire les erreurs de saisie de données.
3. Testez soigneusement votre formulaire, surtout lors de l'utilisation de répétitions imbriquées complexes.
4. Utilisez la fonction de résumé pour aider les enquêteurs à naviguer dans de longues listes de répétitions.
5. Soyez prudent avec un grand nombre de répétitions, car cela peut impacter la performance du formulaire.

## Gestion de Zéro Répétition

Pour représenter zéro répétition dans rtSurvey :

1. Formez les enquêteurs à supprimer la première répétition si elle n'est pas nécessaire.
2. Utilisez des nombres de répétitions dynamiques lorsque le nombre exact est connu.
3. Utilisez `relevant` pour afficher conditionnellement les répétitions.

## Considérations sur l'Exportation des Données

Lors de l'exportation de données de rtSurvey, les données de répétition sont généralement aplaties. Chaque instance de répétition devient une ligne distincte dans les données exportées, les données du formulaire parent étant répétées pour chaque instance.

## Considérations pour l'Application Mobile

- Les répétitions dans l'application mobile rtSurvey prennent en charge la collecte de données hors ligne.
- Un grand nombre de répétitions peut impacter la performance de l'application sur les appareils bas de gamme.

En utilisant efficacement les répétitions dans rtSurvey, vous pouvez créer des enquêtes flexibles et puissantes capables de capturer des structures de données complexes et hiérarchiques tout en maintenant une interface conviviale pour les enquêteurs.
