---
title: "Référencer des valeurs"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 291
---

La syntaxe `${fieldname}` est utilisée pour faire référence à la valeur actuelle d'un autre champ de votre formulaire. Elle peut représenter la valeur saisie, sélectionnée ou calculée, et sera affichée exactement telle qu'elle apparaît dans les données soumises.

Exemple :
Si vous avez un champ nommé "age" et que vous souhaitez récupérer la valeur exacte saisie dans ce champ, vous pouvez utiliser `${age}`.

Pour les contraintes, le symbole "." est utilisé pour faire référence à la saisie ou sélection proposée par l'utilisateur pour le champ actuel. Il vous permet d'appliquer des conditions ou des limites basées sur la valeur que l'utilisateur est en train de saisir ou de sélectionner.

Exemple :
Si vous souhaitez vérifier que la valeur proposée pour le champ actuel est inférieure à 3, vous pouvez utiliser la contrainte `. < 3`.

---

## `..` — Référence au groupe parent

À l'intérieur d'un groupe ou d'un groupe de répétition, `..` fait référence au **contexte parent**. C'est rarement nécessaire en pratique, mais utilisé dans les expressions XPath avancées pour naviguer dans la hiérarchie du formulaire.

---

## Où les références sont utilisées

| Colonne | Type de référence | Exemple |
|--------|---------------|---------|
| `relevant` | `${fieldname}` | `${consent} = 'yes'` |
| `constraint` | `.` pour le champ actuel, `${fieldname}` pour les autres | `. > 0 and . <= ${max_value}` |
| `calculation` | `${fieldname}` | `${adults} + ${children}` |
| `required` | `${fieldname}` | `${has_income} = 'yes'` |
| `default` | `${fieldname}` | `${previous_answer}` |
| `label` | `${fieldname}` dans le texte | `"Votre âge est ${age} ans"` |
| `choice_filter` | Nom de colonne (sans `${}`) | `district = ${district}` |

{{% alert icon=" " context="warning" %}}
Dans la colonne `choice_filter`, référencez les **noms de colonnes de choix** directement (sans `${}`), et référencez les **champs du formulaire** avec `${}`. Confondre les deux est une source d'erreurs fréquente.
{{% /alert %}}

---

## Référencer des valeurs dans les groupes de répétition

À l'intérieur d'une répétition, `${fieldname}` fait référence au champ dans la **même instance** de la répétition :

```
relevant: ${member_age} < 18
```

Ceci utilise la valeur `member_age` pour l'instance de répétition actuelle, pas toutes les instances.

Pour référencer un champ dans une **instance spécifique** de répétition depuis l'extérieur de la répétition, utilisez `indexed-repeat()` :

```
indexed-repeat(${member_name}, ${household_members}, 1)
```

Consultez [Fonctions — Fonctions de champ répété](functions#repeated-field-functions) pour les détails complets.

---

## Vérifications de valeur vide

Tester si un champ a reçu une réponse :

```
${fieldname} != ''       (le champ n'est pas vide)
${fieldname} = ''        (le champ est vide)
```

Pour les nombres, vérifiez également :
```
${age} > 0               (l'âge a une valeur positive — implicitement non vide dans un contexte numérique)
```

---

## Coercition de type dans les références

Lorsque vous utilisez `${fieldname}` dans un contexte numérique (ex. : `${age} + 1`), rtSurvey convertit automatiquement la valeur chaîne en nombre. Un champ vide est converti en `0` ou `NaN` selon l'opération — utilisez `coalesce(${field}, 0)` pour défautiver en toute sécurité un champ numérique vide à zéro.
