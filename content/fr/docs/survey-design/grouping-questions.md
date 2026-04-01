---
title: "Groupement des questions"
description: ""
icon: "auto_awesome"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 250
---

Les groupes dans XLSForm vous permettent d'organiser les questions connexes ensemble, améliorant ainsi la structure de votre enquête et renforçant les capacités d'analyse des données. rtSurvey prend entièrement en charge les groupes XLSForm et étend leurs fonctionnalités avec des caractéristiques supplémentaires.

## Structure de Base du Groupe

Pour créer un groupe de questions, utilisez la syntaxe `begin_group` et `end_group` :

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | respondent | Information sur le répondant             |
| text         | name       | Entrer le nom du répondant               |
| text         | position   | Entrer le poste du répondant             |
| end_group    |            |                                          |
```

Points clés :
- La ligne `begin_group` nécessite un `name` et un `label`.
- La ligne `end_group` n'a pas besoin de nom ou d'étiquette.
- Les questions entre `begin_group` et `end_group` font partie du groupe.

## Apparence du Groupe (Appearance)

rtSurvey prend en charge diverses options d'apparence pour les groupes :

1. **field-list** : Affiche plusieurs questions sur le même écran.
   ```
   | type         | name       | label     | appearance |
   |--------------|------------|-----------|------------|
   | begin_group  | respondent | Répondant | field-list |
   | text         | name       | Nom       |            |
   | text         | position   | Poste     |            |
   | end_group    |            |           |            |
   ```

2. **grid** : Crée une mise en page compacte, semblable à un tableau, pour les groupes (spécifique à rtSurvey).
   ```
   | type         | name       | label     | appearance |
   |--------------|------------|-----------|------------|
   | begin_group  | household  | Foyer     | grid       |
   | text         | member_name| Nom       |            |
   | integer      | member_age | Âge       |            |
   | end_group    |            |           |            |
   ```

3. **collapsible** : Crée des groupes extensibles/repliables (spécifique à rtSurvey).
   ```
   | type         | name       | label     | appearance  |
   |--------------|------------|-----------|-------------|
   | begin_group  | details    | Détails   | collapsible |
   | text         | address    | Adresse   |             |
   | text         | phone      | Téléphone |             |
   | end_group    |            |           |             |
   ```

## Groupes Imbriqués (Nested Groups)

Les groupes peuvent être imbriqués dans d'autres groupes pour des structures plus complexes :

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | hospital   | Information sur l'hôpital                |
| text         | hosp_name  | Quel est le nom de cet hôpital ?          |
| begin_group  | medication | Disponibilité des médicaments            |
| select_one y_n| hiv_meds  | Cet hôpital a-t-il des médicaments VIH ? |
| end_group    |            |                                          |
| end_group    |            |                                          |
```

**Note** : Terminez toujours le groupe le plus récemment commencé en premier pour maintenir une imbrication correcte.

## Logique de Saut pour les Groupes

Utilisez la colonne `relevant` pour implémenter la logique de saut pour des groupes entiers :

```
| type         | name   | label                                        | relevant        |
|--------------|--------|----------------------------------------------|-----------------|
| integer      | age    | Quel âge avez-vous ?                         |                 |
| begin_group  | child  | Enfant                                       | ${age} <= 5     |
| integer      | muac   | Enregistrer le périmètre brachial de l'enfant|                 |
| select_one y_n| mrdt  | Le test de diagnostic rapide est-il positif ?|                |
| end_group    |        |                                              |                 |
```

Dans cet exemple, le groupe `child` n'apparaîtra que si l'âge du répondant est de 5 ans ou moins.

## Meilleures Pratiques pour l'Utilisation des Groupes

1. Utilisez des noms significatifs pour les groupes afin d'améliorer l'analyse des données.
2. Gardez les groupes concentrés sur des questions connexes.
3. Utilisez les groupes imbriqués avec discernement pour éviter des structures trop complexes.
4. Testez soigneusement la logique de saut lors de l'utilisation de `relevant` sur des groupes.
5. Envisagez d'utiliser l'apparence `field-list` pour les groupes courts afin de réduire le défilement.
6. Utilisez la mise en page en grille (grid) de rtSurvey pour un affichage compact des informations connexes.
7. Utilisez les groupes repliables (collapsible) pour les longs formulaires afin d'améliorer la navigation.

## Fonctionnalités Spécifiques à rtSurvey

1. **Mise en page en grille (Grid Layout)** : Utilisez l'apparence `grid` pour des affichages de type tableau.
2. **Groupes repliables (Collapsible Groups)** : Implémentez l'apparence `collapsible` pour des sections extensibles.
3. **Style Personnalisé** : Appliquez du CSS personnalisé aux groupes pour des designs visuels uniques.
4. **Comportement Dynamique du Groupe** : Implémentez une logique de saut et des calculs complexes au sein des groupes.

## Support Multilingue

rtSurvey prend en charge les groupes multilingues. Utilisez des colonnes spécifiques à la langue pour les étiquettes :

```
| type         | name       | label::English | label::French |
|--------------|------------|----------------|---------------|
| begin_group  | personal   | Personal Info  | Infos Personnelles |
| text         | name       | Name           | Nom           |
| end_group    |            |                |               |
```

## Considérations pour l'Application Mobile

- Les groupes avec l'apparence `field-list` sont affichés sur un seul écran dans l'application mobile.
- Les groupes repliables peuvent améliorer la navigation sur les petits écrans.
- Les mises en page en grille peuvent s'ajuster pour une meilleure visibilité sur les appareils mobiles.

## Limitations Connues

- Une imbrication extrêmement profonde des groupes peut affecter les performances sur certains appareils.
- Certaines options de style avancées peuvent ne pas être disponibles pour les groupes dans l'application mobile.

## Dépannage des Groupes

1. Assurez-vous que chaque `begin_group` a un `end_group` correspondant.
2. Vérifiez que les noms des groupes sont uniques au sein du formulaire.
3. Vérifiez que la logique de saut fait référence aux noms de questions corrects.
4. Testez soigneusement les groupes sur les interfaces web et mobiles.

En utilisant efficacement les groupes dans vos XLSForms avec rtSurvey, vous pouvez créer des enquêtes bien organisées et efficaces qui améliorent à la fois l'expérience de collecte de données et la qualité de votre analyse de données.
