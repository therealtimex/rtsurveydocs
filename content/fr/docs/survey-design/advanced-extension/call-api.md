---
title: "Call API"
description: "Call API permet à votre enquête de récupérer des données depuis un service web externe et d'utiliser la réponse pour peupler des champs ou valider des réponses."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 294
---

La fonctionnalité **Call API** permet à un champ d'enquête d'effectuer une requête HTTP vers un service externe et d'utiliser la réponse pour peupler une valeur calculée ou valider la saisie de l'utilisateur. Cela permet des recherches en temps réel, des vérifications d'identité, des recherches de codes-barres et toute autre vérification côté serveur pendant la collecte de données.

Deux fonctions sont disponibles :

- `callapi()` — récupère une valeur depuis une API et la stocke dans un champ `calculate` ou `text`
- `callapi-verify()` — appelle une API et bloque la progression si la réponse ne correspond pas à la valeur attendue (utilisé dans `constraint`)

---

## `callapi()` — Récupérer et stocker une réponse API

### Syntaxe

Placez `callapi()` dans la colonne **`calculation`** d'un champ `calculate` ou `text` :

```
callapi(method, url, allowed_auto, max_retry, no_overwrite, extract_expr, timeout, lifetime, response_q, call_type, post_body)
```

### Paramètres

| # | Paramètre | Description |
|---|-----------|-------------|
| 1 | `method` | Méthode HTTP : `'GET'` ou `'POST'` |
| 2 | `url` | URL du point de terminaison API |
| 3 | `allowed_auto` | `1` pour appeler automatiquement quand le champ est atteint ; `0` pour exiger un bouton déclencheur manuel |
| 4 | `max_retry` | Nombre maximum de tentatives en cas d'échec |
| 5 | `no_overwrite` | `1` pour conserver la valeur existante si le champ en a déjà une ; `0` pour toujours écraser |
| 6 | `extract_expr` | Expression JSONPath pour extraire la valeur souhaitée de la réponse (ex. : `$.data.name`) |
| 7 | `timeout` | Délai d'expiration de la requête en millisecondes |
| 8 | `lifetime` | Durée (ms) pendant laquelle la réponse mise en cache reste valide avant une nouvelle récupération |
| 9 | `response_q` | Nom d'un champ pour stocker le code de réponse HTTP brut (ex. : `${response_status}`) |
| 10 | `call_type` | *(Optionnel)* Mode d'appel spécial : `'lazy-upload'` ou `'lazy-upload-multiple'` |
| 11 | `post_body` | *(Optionnel)* Chaîne de corps POST. Référencez les champs du formulaire avec `##fieldname##` |

### Exemple : Requête GET pour rechercher un ménage par ID

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| text | household_id | Identifiant du ménage | | |
| calculate | hh_name | | callapi | `callapi('GET', concat('https://api.example.com/households/', ${household_id}), 1, 3, 0, '$.name', 10000, 0, '')` |
| note | hh_display | Ménage : ${hh_name} | | |

### Exemple : Requête POST avec un corps JSON

```
callapi('POST', 'https://api.example.com/lookup', 1, 2, 0, '$.result.value', 15000, 0, '', '', '{"id": "##household_id##"}')
```

Dans le `post_body`, utilisez `##fieldname##` pour injecter la valeur actuelle de n'importe quel champ du formulaire.

### Apparence : `callapi`

Ajoutez `callapi` à la colonne `appearance` du champ pour activer l'intégration d'appel API :

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | api_result | | callapi | `callapi('GET', ...)` |

Lorsque `allowed_auto` est `0`, rtSurvey affiche un **bouton "Récupérer"** que l'enquêteur actionne manuellement.

---

## `callapi-verify()` — Valider une valeur par rapport à une API

`callapi-verify()` bloque la soumission d'un champ jusqu'à ce qu'une API confirme que la valeur saisie est valide. Utilisez-le dans la colonne **`constraint`**.

### Syntaxe

```
callapi-verify(method, url, extract_expr, match_expr, timeout, constraint_mode, post_body, message)
```

### Paramètres

| # | Paramètre | Description |
|---|-----------|-------------|
| 1 | `method` | Méthode HTTP : `'GET'` ou `'POST'` |
| 2 | `url` | Point de terminaison API de vérification |
| 3 | `extract_expr` | JSONPath pour extraire la valeur attendue de la réponse |
| 4 | `match_expr` | Expression comparant la valeur extraite à la valeur du champ (ex. : `$.status = 'valid'`) |
| 5 | `timeout` | Délai d'expiration de la requête en millisecondes |
| 6 | `constraint_mode` | `'soft'` pour un avertissement uniquement ; `'hard'` pour bloquer la progression |
| 7 | `post_body` | *(Optionnel)* Corps POST avec substitutions `##fieldname##` |
| 8 | `message` | *(Optionnel)* Message d'erreur. Supporte le multi-langues : `<en>Invalid!</en><vi>Không hợp lệ!</vi>` |

### Exemple : Vérifier un code-barres par rapport à un registre d'actifs

| type | name | label | appearance | constraint | constraint_message |
|------|------|-------|------------|------------|-------------------|
| barcode | asset_code | Scanner le code-barres de l'actif | callapi-verify | `callapi-verify('POST', 'https://api.example.com/assets/verify', '$.valid', ". = 'true'", 10000, 'hard', '{"code": "##asset_code##"}')` | Actif non trouvé dans le registre |

### Apparence : `callapi-verify(...)`

La colonne `appearance` sur un champ avec `callapi-verify()` dans la contrainte doit contenir `callapi-verify(params)` ou `callapi-verify(dynamicParams)` pour indiquer à rtSurvey que ce champ utilise la vérification API.

---

## Utiliser les données App API avec callapi

Combinez `callapi()` avec `pulldata('app-api', 'user.token')` pour injecter le jeton de l'utilisateur authentifié dans votre requête API :

```
callapi('POST', 'https://api.example.com/data', 1, 2, 0, '$.value', 10000, 0, '', '',
  concat('{"token":"', pulldata('app-api','user.token'), '","id":"##item_id##"}'))
```

## Bonnes pratiques

1. Définissez toujours un `timeout` raisonnable (5000-15000 ms) — n'utilisez pas 0 ou des valeurs très élevées.
2. Définissez `allowed_auto=0` pour les vérifications que l'enquêteur doit déclencher consciemment (ex. : vérifications d'identité).
3. Définissez `no_overwrite=1` lorsque le champ peut être modifié ultérieurement et que vous ne souhaitez pas que la nouvelle récupération écrase les corrections manuelles.
4. Utilisez `extract_expr` avec un JSONPath spécifique plutôt que de compter sur le texte de réponse brut.
5. Testez les appels API en mode hors ligne — callapi échouera gracieusement et affichera une erreur, mais le formulaire doit rester remplissable pour les champs non critiques.

## Limitations

- Nécessite une connectivité réseau au moment de l'appel — les appels échouent lorsque l'appareil est hors ligne.
- Les réponses API doivent être en JSON — les réponses XML ou texte brut nécessitent un traitement supplémentaire.
- Une fréquence d'appels élevée (ex. : un appel API par instance de répétition) peut ralentir la navigation dans le formulaire.
