---
title: "Select_one"
description: ""
icon: "radio_button_checked"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 224
---
  
  
### select_one listname
  
L'instruction `select_one listname` invite l'utilisateur à choisir une option unique dans une liste de choix prédéfinie. Dans une définition XLSForm, le `listname` doit correspondre à une valeur répertoriée dans la colonne `list_name` de l'onglet `choices` (par exemple, "yesno").

Par défaut, les choix sont affichés sous forme de boutons radio, chaque bouton représentant un choix statique unique de la liste spécifiée. Cependant, diverses options d'apparence sont disponibles pour personnaliser l'aspect, le comportement et la liste de choix elle-même. Reportez-vous aux sous-sections ci-dessous pour plus d'informations sur ces options.

Dans la définition XLSForm :
{{< table "table table-striped" >}}
| Type             | Name      | Label          | Appearance |
|------------------|-----------|----------------|------------|
| select_one listname | fieldname | texte de la question |            |
{{</ table >}}
  
### Options d'apparence de base

Spécifiez les valeurs suivantes dans la colonne `appearance` pour modifier l'aspect du champ `select_one listname` :

- "quick" : Passe automatiquement à la question suivante dès qu'une option est sélectionnée, sans attendre que l'utilisateur balaie l'écran (swipe).
- "minimal" : Affiche un sélecteur déroulant unique au lieu de boutons radio.
- "compact" : Affiche un tableau compact d'options. Le nombre de colonnes dépend de la largeur de l'affichage.
- "compact-#" : Force un nombre spécifique de colonnes dans le tableau compact, où "#" représente le nombre de colonnes souhaité.
- "quickcompact" : Combine les apparences "quick" et "compact".
- "quickcompact-#" : Combine les apparences "quick" et "compact" et force un nombre spécifique de colonnes.

Dans la définition XLSForm :  
{{< table "table table-striped" >}}
| Type             | Name      | Label          | Appearance       |
|------------------|-----------|----------------|------------------|
| select_one listname | fieldname | texte de la question | quick            |
| select_one listname | fieldname | texte de la question | minimal          |
| select_one listname | fieldname | texte de la question | compact          |
| select_one listname | fieldname | texte de la question | compact-#        |
| select_one listname | fieldname | texte de la question | quickcompact     |
| select_one listname | fieldname | texte de la question | quickcompact-#   |
{{</ table >}}
