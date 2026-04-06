---
title: "Type de question dynamique"
description: "Le type de question dynamique permet de déterminer le type de widget et le comportement d'un champ au moment de l'exécution, en fonction d'une réponse API ou d'une valeur calculée."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 301
---

La fonctionnalité **Type de question dynamique** permet de déterminer le widget de saisie et le comportement de validation d'un champ **au moment de l'exécution** plutôt qu'au moment de la conception du formulaire. C'est une extension rtSurvey avancée utilisée lorsque le type de données à collecter dépend d'une configuration côté serveur, d'une réponse API ou de la valeur d'un champ précédent.

Un cas d'utilisation courant est une liste de contrôle d'inspection configurable où le serveur définit quels champs sont requis, quel type ils sont (text, integer, select, etc.) et quelles options sont disponibles — sans reconstruire le formulaire pour chaque configuration.

---

## Fonctionnement

Un champ marqué comme type de question dynamique utilise `callapi()` pour récupérer sa configuration depuis une API. La réponse API définit :

- Le type de saisie à afficher (text, integer, select_one, etc.)
- Les choix disponibles (pour les types de sélection)
- Les règles de validation

Le champ est marqué en interne avec `specialFeature: isDynamicQuestionType`, ce qui indique au moteur de formulaire d'utiliser la réponse API pour construire le widget plutôt que la définition statique du formulaire.

---

## Configuration

### Étape 1 : Récupérer la configuration du champ

Utilisez un champ `calculate` avec `callapi()` pour récupérer la configuration dynamique :

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | field_config | | callapi | `callapi('POST', 'https://api.example.com/field-config', 1, 2, 0, '$.config', 10000, 0, '', '', '{"form_id": "##form_id##", "field_id": "inspection_result"}')` |

### Étape 2 : Référencer la configuration dans le champ dynamique

Le champ dynamique utilise `callapi-verify()` dans son `appearance` ou `constraint` pour se lier à la configuration récupérée :

| type | name | label | appearance |
|------|------|-------|------------|
| text | inspection_result | Résultat d'inspection | `callapi-verify(dynamicParams)` |

Le moteur de formulaire lit `field_config` et détermine dynamiquement si `inspection_result` doit être affiché comme un champ `text`, `integer` ou `select_one`.

---

## Format de réponse API

L'API doit retourner un objet JSON décrivant la configuration du champ. Une réponse typique :

```json
{
  "config": {
    "type": "select_one",
    "choices": [
      {"value": "pass", "label": "Réussi"},
      {"value": "fail", "label": "Échoué"},
      {"value": "na", "label": "N/A"}
    ],
    "required": true,
    "constraint": ". != ''"
  }
}
```

---

## Exemple : Formulaire d'inspection configurable

Un formulaire d'inspection où les éléments de liste de contrôle et leurs types de réponse sont récupérés depuis un serveur en fonction de la catégorie d'inspection :

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| select_one inspection_type | insp_type | Type d'inspection | | |
| calculate | checklist_config | | callapi | `callapi('POST', 'https://api.example.com/checklist', 1, 2, 0, '$.items', 10000, 0, '', '', '{"type": "##insp_type##"}')` |
| text | item_1 | Élément 1 | `callapi-verify(dynamicParams)` | |
| text | item_2 | Élément 2 | `callapi-verify(dynamicParams)` | |
| text | item_3 | Élément 3 | `callapi-verify(dynamicParams)` | |

Le serveur retourne le type de widget correct, l'étiquette, les choix et la validation pour chaque élément en fonction du `insp_type`.

---

## Bonnes pratiques

1. Utilisez les types de questions dynamiques uniquement lorsque la structure du champ varie réellement au moment de l'exécution — pour les formulaires statiques, utilisez les types de questions standard.
2. Assurez-vous que l'API de configuration répond rapidement (en moins de 2 secondes) et est disponible sur le réseau terrain.
3. Définissez toujours une solution de repli sensée dans le formulaire pour le cas où l'API est inaccessible — un champ `text` simple avec une note est préférable à un widget défaillant.
4. Versionnez le schéma de réponse de votre API — les modifications du format de réponse affecteront tous les formulaires actifs utilisant ce point de terminaison.
5. Testez chaque combinaison de types de champs que l'API peut retourner avant le déploiement.

## Limitations

- Les types de questions dynamiques nécessitent une connectivité réseau pour récupérer la configuration.
- La gamme complète des types de widgets disponibles dynamiquement dépend de la version du client rtSurvey — testez sur votre version cible.
- C'est une extension rtSurvey avancée sans équivalent dans la spécification XLSForm standard.
- Les erreurs de débogage sont plus difficiles à tracer car la définition du champ se trouve en partie dans le formulaire et en partie dans la réponse API.
