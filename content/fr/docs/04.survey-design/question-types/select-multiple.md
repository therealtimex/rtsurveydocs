---
title: "Select_multiple"
description: ""
icon: "check_box"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 225
---

### select_multiple listname

L'instruction `select_multiple listname` invite l'utilisateur à sélectionner un ou plusieurs choix dans une liste de choix prédéfinie. Dans une définition XLSForm, le `listname` doit correspondre à une valeur répertoriée dans la colonne `list_name` de l'onglet `choices` (par exemple, "country").

Par défaut, les choix sont affichés sous forme de cases à cocher (checkboxes), où chaque case représente un choix statique unique de la liste spécifiée. Cependant, diverses options d'apparence sont disponibles pour personnaliser l'aspect, la fonctionnalité et même la liste de choix elle-même. Veuillez vous référer aux sous-sections ci-dessous pour plus d'informations sur ces options.

Lors de l'exportation des données, chaque ligne comprendra une colonne avec une liste séparée par des espaces de toutes les valeurs de réponse choisies pour chaque champ `select_multiple`.

Lors de l'utilisation d'un champ `select_multiple` dans la validation de champ ou les sauts logiques (expressions de contrainte ou de pertinence), la fonction `selected()` doit être utilisée pour vérifier si un choix spécifique a été sélectionné. Vous trouverez plus d'informations sur les expressions de contrainte et de pertinence dans les rubriques d'aide.

Dans la définition XLSForm :

| Type                  | Name      | Label          | Appearance |
|-----------------------|-----------|----------------|------------|
| select_multiple listname | fieldname | texte de la question |            |
