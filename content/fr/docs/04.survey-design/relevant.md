---
title: "Saut de questions"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 280
---

La logique de saut, également connue sous le nom de branchement ou de logique conditionnelle, vous permet de créer des enquêtes dynamiques qui s'adaptent aux réponses des répondants. Dans rtSurvey, la logique de saut est implémentée en utilisant la colonne `relevant` dans votre XLSForm.

## Logique de Saut de Base

Pour implémenter une logique de saut de base, utilisez la colonne `relevant` pour spécifier une condition :

```
| type           | name          | label                       | relevant            |
|----------------|---------------|-----------------------------|--------------------|
| select_one y_n | likes_pizza   | Aimez-vous la pizza ?       |                    |
| select_multiple pizza_toppings | favorite_topping | Garnitures préférées | ${likes_pizza} = 'yes' |
```

Dans cet exemple, la question "Garnitures préférées" n'apparaît que si le répondant répond "yes" à la question sur son goût pour la pizza.

## Syntaxe pour les Expressions Relevant

- Utilisez `${ }` pour référencer d'autres variables de questions.
- Pour les questions `select_one`, comparez directement : `${nom_question} = 'reponse'`
- Pour les questions `select_multiple`, utilisez la fonction `selected()`.

## Logique de Saut Avancée

### Conditions Multiples

Vous pouvez combiner plusieurs conditions en utilisant `and`, `or`, et des parenthèses :

```
| type    | name  | label                   | relevant                                  |
|---------|-------|-------------------------|-------------------------------------------|
| integer | age   | Quel est votre âge ?    |                                           |
| text    | school| Quelle école fréquentez-vous ? | ${age} < 18 and (${location} = 'urban' or ${location} = 'suburban') |
```

### Utilisation des Questions select_multiple

Pour les questions `select_multiple`, utilisez la fonction `selected()` :

```
| type           | name          | label                       | relevant                               |
|----------------|---------------|-----------------------------|-----------------------------------------|
| select_multiple pizza_toppings | favorite_topping | Garnitures préférées |                                         |
| text           | cheese_type   | Type de fromage préféré     | selected(${favorite_topping}, 'cheese') |
```

### Option "Autre" dans les Choix Multiples

Privilégiez l'implémentation d'une option "Autre" avec saisie de texte libre en utilisant `relevant` :

```
| type           | name                  | label                               | relevant                               |
|----------------|----------------------|-------------------------------------|---------------------------------------|
| select_multiple pizza_toppings | favorite_toppings | Quelles sont vos garnitures de pizza préférées ? |                                       |
| text           | favorite_toppings_other | Quelles autres garnitures aimez-vous ? | selected(${favorite_toppings}, 'other') |
```

N'oubliez pas d'inclure 'other' comme option dans votre feuille de calcul choices.

## Fonctionnalités Spécifiques à rtSurvey

### Pertinence Dynamique

rtSurvey permet une pertinence dynamique basée sur des champs calculés :

```
| type      | name       | label              | calculation                   |
|-----------|------------|--------------------|-----------------------------|
| calculate | total_score| Score Total        | ${score1} + ${score2} + ${score3} |
| text      | feedback   | Commentaires       | ${total_score} > 75             |
```

### Pertinence dans les Répétitions (Repeats)

rtSurvey prend en charge la pertinence au sein des groupes de répétition :

```
| type         | name         | label            | relevant               |
|--------------|--------------|------------------|------------------------|
| begin repeat | child_info   | Infos Enfant     |                        |
| integer      | child_age    | Âge de l'enfant  |                        |
| text         | school_name  | Nom de l'école   | ${child_age} >= 5      |
| end repeat   |              |                  |                        |
```

### Pertinence en Cascade

rtSurvey gère efficacement la pertinence en cascade, où la pertinence d'une question dépend d'une autre, qui elle-même dépend d'une troisième :

```
| type           | name        | label                  | relevant               |
|----------------|-------------|------------------------|------------------------|
| select_one y_n | has_car     | Possédez-vous une voiture ? |                   |
| select_one car_type | car_type | Quel type de voiture ? | ${has_car} = 'yes'     |
| text           | model       | Modèle spécifique      | ${car_type} = 'sedan'  |
```

## Meilleures Pratiques pour la Logique de Saut dans rtSurvey

1. **Restez Simple** : Évitez les conditions de pertinence trop complexes lorsque c'est possible.
2. **Testez Soigneusement** : Utilisez la fonction de prévisualisation de rtSurvey pour tester tous les chemins possibles de votre enquête.
3. **Considérez la Performance** : Une logique de saut très complexe peut impacter la performance de l'enquête, surtout sur les appareils mobiles.
4. **Utilisez des Noms de Variables Clairs** : Cela rend vos expressions de pertinence plus faciles à lire et à maintenir.
5. **Documentez votre Logique** : Ajoutez des notes pour expliquer les schémas de saut complexes, surtout pour la collaboration en équipe.
6. **Soyez Conscient de l'Analyse des Données** : Les questions sautées entraîneront des données manquantes. Planifiez votre analyse en conséquence.

## Dépannage de la Logique de Saut

- **Erreurs de Syntaxe** : Assurez-vous que tous les `${ }` sont correctement fermés et orthographiés.
- **Références Circulaires** : Évitez de créer des boucles où les questions dépendent les unes des autres.
- **Sensibilité à la Casse** : Rappelez-vous que les choix de réponses sont sensibles à la casse dans les expressions de pertinence.
- **Comparaisons Numériques** : Utilisez les opérateurs appropriés (`<`, `>`, `=`) pour les comparaisons numériques.

## Conclusion

L'utilisation efficace de la logique de saut peut considérablement améliorer l'expérience du répondant et la qualité des données dans vos projets rtSurvey. En tirant parti des fonctionnalités avancées de rtSurvey et en suivant les meilleures pratiques, vous pouvez créer des enquêtes dynamiques et efficaces qui s'adaptent à la situation unique de chaque répondant.
