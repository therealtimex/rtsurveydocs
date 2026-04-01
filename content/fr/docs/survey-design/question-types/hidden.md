---
title: "Hidden"
description: "Les champs masqués stockent des valeurs qui ne sont jamais affichées au répondant — utilisés pour transmettre du contexte, pré-remplir des données ou stocker des résultats intermédiaires."
icon: "eye-slash"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 239
---

Un champ `hidden` stocke une valeur qui n'est **jamais affichée au répondant**. Contrairement à `calculate` (qui calcule une valeur), `hidden` est utilisé pour porter une **valeur fournie de l'extérieur** — par exemple, un identifiant de tâche, un identifiant de ménage transmis depuis un autre système, ou un code d'enquêteur injecté lors du lancement du formulaire.

## Spécification XLSForm de base

| type | name | label |
|------|------|-------|
| hidden | household_id | |

Les étiquettes ne sont pas nécessaires pour les champs masqués puisque rien n'est affiché à l'écran.

## Utilisations

Les champs masqués sont couramment utilisés pour :

1. Transmettre un identifiant pré-attribué depuis le système de gestion d'enquête (ex. : identifiant de ménage, numéro de cas, code de tâche)
2. Stocker la version du formulaire ou les métadonnées de déploiement
3. Injecter une configuration spécifique à l'enquêteur au lancement du formulaire
4. Transporter des données d'un formulaire parent vers un formulaire enfant dans les flux de travail liés
5. Stocker une valeur dérivée des paramètres URL lorsque le formulaire est ouvert via un lien web

## Définir une valeur par défaut

Le schéma le plus courant consiste à utiliser `hidden` avec une expression `default` pour que la valeur soit définie à l'ouverture du formulaire :

| type | name | default |
|------|------|---------|
| hidden | deployment_code | 'ZONE_A_2024' |
| hidden | form_version | '3.1' |

## Référencer un champ masqué dans des calculs

Les valeurs masquées peuvent être référencées comme n'importe quel autre champ en utilisant `${fieldname}` :

| type | name | label | calculation |
|------|------|-------|-------------|
| hidden | zone_code | | |
| calculate | label_prefix | | concat('[', ${zone_code}, '] ') |
| note | intro | ${label_prefix} Bienvenue dans l'enquête ménage | |

## Utiliser hidden avec préremplissage / paramètres URL

Lors du lancement d'un formulaire web via URL, vous pouvez passer des paramètres qui remplissent les champs masqués. Cela permet de précharger un identifiant de ménage ou un code de tâche sans que l'enquêteur ait à le saisir :

```
https://your-server.com/form/FORMID?household_id=H00123&zone_code=NORTH
```

Le champ nommé `household_id` sera automatiquement rempli avec `H00123`.

## Bonnes pratiques

1. Utilisez `hidden` (pas `calculate`) lorsque la valeur est **injectée de l'extérieur** et ne doit pas être recalculée.
2. Utilisez `calculate` lorsque la valeur est **dérivée d'autres champs** du formulaire.
3. Définissez toujours un `default` si le champ masqué doit avoir une valeur — un champ masqué sans valeur par défaut sera vide.
4. Nommez les champs masqués de façon claire pour les distinguer (ex. : préfixe `_hidden_` ou utilisation d'une convention de nommage cohérente).

## Limitations

- Les champs masqués sont inclus dans les données exportées comme n'importe quel autre champ.
- Ils ne peuvent pas être affichés conditionnellement — ils sont toujours présents (mais invisibles).
- Si vous avez besoin d'un champ qui se calcule dynamiquement, utilisez `calculate` à la place.
