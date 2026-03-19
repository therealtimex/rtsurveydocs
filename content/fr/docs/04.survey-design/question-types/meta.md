---
title: "Meta"
description: "Les types de questions meta capturent automatiquement les informations sur l'appareil, l'enquêteur et l'horodatage, sans aucune saisie du répondant."
icon: "info"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 237
---

Les types de questions meta sont des champs spéciaux qui sont remplis **automatiquement** — le répondant ne les voit jamais. Ils capturent le contexte de la soumission : quand elle a été collectée, quel appareil a été utilisé, et qui l'a collectée. Ajoutez-les dans la feuille de calcul `survey` comme n'importe quel autre type de question ; ils n'apparaissent simplement pas à l'écran.

## Spécification XLSForm de base

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| deviceid | deviceid | |

Les étiquettes sont optionnelles pour les champs meta puisqu'ils ne sont jamais affichés.

---

## Champs meta de temps

### `start`

Enregistre la **date et l'heure d'ouverture du formulaire**. Stocké au format ISO 8601 (`YYYY-MM-DDTHH:MM:SS.sss+HH:MM`).

```
type    | name  | label
start   | start |
```

### `end`

Enregistre la **date et l'heure de soumission du formulaire**. Combiné avec `start`, vous pouvez calculer le temps passé à remplir le formulaire :

```
type      | name          | calculation
calculate | duration_min  | (decimal-date-time(${end}) - decimal-date-time(${start})) * 1440
```

### `today`

Enregistre la **date du jour** (sans composante horaire). Stocké au format `YYYY-MM-DD`. Utile lorsque vous avez besoin uniquement de la date sans l'horodatage complet.

```
type  | name  | label
today | today |
```

---

## Champs meta de l'appareil

### `deviceid`

Enregistre l'**identifiant unique de l'appareil** utilisé pour la collecte de données. Sur Android, il s'agit généralement de l'IMEI ou de l'Android ID. Utile pour suivre quel appareil a soumis chaque formulaire et détecter les soumissions en double depuis le même appareil.

```
type      | name     | label
deviceid  | deviceid |
```

### `devicephonenum`

Enregistre le **numéro de téléphone de la carte SIM** dans l'appareil (si disponible). Peut être vide si l'appareil n'a pas de SIM ou si le numéro n'est pas stocké sur la SIM.

```
type           | name          | label
devicephonenum | devicephonenum |
```

### `simserial`

Enregistre le **numéro de série de la carte SIM** (ICCID). Utile pour identifier quelle SIM/opérateur a été utilisé.

```
type      | name      | label
simserial | simserial |
```

### `subscriberid`

Enregistre l'**IMSI (International Mobile Subscriber Identity)** — l'identifiant unique d'abonné sur la carte SIM.

```
type         | name        | label
subscriberid | subscriberid |
```

---

## Champs meta de l'enquêteur

### `username`

Enregistre le **nom d'utilisateur de l'enquêteur connecté** (le compte utilisé dans l'application rtSurvey). C'est le moyen le plus fiable de suivre qui a collecté chaque soumission.

```
type     | name     | label
username | username |
```

### `email`

Enregistre l'**adresse e-mail de l'enquêteur connecté**.

```
type  | name  | label
email | email |
```

### `phonenumber`

Enregistre le **numéro de téléphone associé au compte de l'enquêteur** (si configuré).

```
type        | name       | label
phonenumber | phonenumber |
```

---

## Journal d'audit

### `audit`

Le champ meta `audit` active la **journalisation d'audit détaillée** — il enregistre un journal horodaté de chaque question visitée par l'enquêteur, le temps passé sur chacune, et (optionnellement) leur localisation GPS à chaque étape. Le journal d'audit est sauvegardé dans un fichier `audit.csv` séparé avec chaque soumission.

```
type  | name  | parameters
audit | audit | location-priority=balanced location-min-interval=30 location-max-age=60
```

#### Paramètres d'audit

| Paramètre | Description |
|-----------|-------------|
| `location-priority` | Niveau de précision GPS : `no-gps`, `low-power`, `balanced`, `high-accuracy` |
| `location-min-interval` | Secondes minimales entre les captures de localisation |
| `location-max-age` | Âge maximum (secondes) d'une localisation mise en cache à accepter |

Le journal d'audit capture :
- Nom de la question et type d'événement (`question`, `form.start`, `form.exit`, `form.save`, `form.finalize`)
- Horodatages de début et de fin pour chaque événement
- Coordonnées GPS (si `location-priority` est défini)

{{% alert icon=" " context="warning" %}}
Le champ `audit` génère un fichier séparé par soumission. Assurez-vous que votre pipeline de données traite à la fois les données principales du formulaire et le CSV d'audit.
{{% /alert %}}

---

## Exemple complet

Une enquête ménage typique pourrait inclure tous les champs meta de temps et d'enquêteur :

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| today | today | |
| deviceid | deviceid | |
| username | username | |
| email | email | |
| audit | audit | |
| text | household_id | Identifiant du ménage |
| ... | ... | ... |

---

## Bonnes pratiques

1. Incluez toujours `start` et `end` — ils sont gratuits, automatiques et inestimables pour le contrôle qualité.
2. Incluez toujours `username` pour suivre les enquêteurs.
3. Incluez `deviceid` lorsque vous souhaitez détecter les soumissions en double ou suivre les appareils terrain.
4. Utilisez `audit` dans les enquêtes à forte responsabilité où vous devez vérifier que les enquêteurs ont effectivement visité chaque question.
5. Les champs liés à la SIM (`simserial`, `subscriberid`, `devicephonenum`) ne sont fiables que sur les appareils Android avec des cartes SIM actives — ignorez-les pour les déploiements sur tablettes uniquement.

---

## Limitations

- Tous les champs meta sont **en lecture seule** — ils ne peuvent pas être référencés ou modifiés par d'autres calculs.
- `username` et `email` nécessitent que l'enquêteur soit connecté ; ils seront vides pour les soumissions anonymes.
- Les champs meta SIM/téléphone peuvent retourner des valeurs vides sur les tablettes Wi-Fi uniquement et certaines versions d'Android en raison des restrictions de permissions.
