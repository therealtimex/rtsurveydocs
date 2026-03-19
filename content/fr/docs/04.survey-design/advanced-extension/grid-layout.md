---
title: "Mise en page en grille"
description: "La mise en page en grille vous permet de positionner les champs dans une grille CSS au sein d'un groupe, permettant des conceptions de formulaires multi-colonnes."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 296
---

La fonctionnalité **Mise en page en grille** vous permet d'organiser les questions dans une **grille multi-colonnes** au sein d'un groupe, en utilisant la balise d'apparence `gridformat<>`. C'est utile pour les formulaires de saisie de données denses où plusieurs champs liés doivent apparaître côte à côte plutôt qu'empilés verticalement.

---

## Fonctionnement

La mise en page en grille est appliquée à deux niveaux :

1. **Le groupe** — définissez `appearance: field-list grid(weight=N)` pour spécifier le nombre de colonnes de la grille
2. **Chaque champ dans le groupe** — définissez `appearance: gridformat<row=R col=C colspan=S/>` pour positionner le champ

La grille utilise un système Bootstrap à 12 colonnes. `weight=N` définit le nombre de colonnes logiques de votre grille ; chaque colonne occupe `12/N` colonnes Bootstrap.

---

## Apparence au niveau du groupe

| Apparence | Description |
|------------|-------------|
| `field-list grid(weight=2)` | Grille à 2 colonnes (chaque colonne = 6 cols Bootstrap) |
| `field-list grid(weight=3)` | Grille à 3 colonnes (chaque colonne = 4 cols Bootstrap) |
| `field-list grid(weight=4)` | Grille à 4 colonnes (chaque colonne = 3 cols Bootstrap) |
| `field-list grid(weight=6)` | Grille à 6 colonnes (chaque colonne = 2 cols Bootstrap) |

---

## Syntaxe `gridformat<>` au niveau du champ

```
gridformat<row=R col=C colspan=S/>
gridformat<row=R col=C colspan=S backgroundcolor=COLOR/>
```

| Attribut | Description |
|-----------|-------------|
| `row` | Numéro de ligne (basé sur 1) |
| `col` | Numéro de colonne (basé sur 1, dans la grille définie par `weight`) |
| `colspan` | Nombre de colonnes que ce champ occupe (par défaut 1) |
| `backgroundcolor` | Couleur CSS optionnelle pour l'arrière-plan du champ (ex. : `#f0f0f0`, `lightblue`) |

---

## Exemple : Section d'enquête ménage à 2 colonnes

| type | name | label | appearance |
|------|------|-------|------------|
| begin_group | demographics | Données démographiques | `field-list grid(weight=2)` |
| text | first_name | Prénom | `gridformat<row=1 col=1/>` |
| text | last_name | Nom de famille | `gridformat<row=1 col=2/>` |
| integer | age | Âge | `gridformat<row=2 col=1/>` |
| select_one gender | gender | Genre | `gridformat<row=2 col=2/>` |
| text | address | Adresse complète | `gridformat<row=3 col=1 colspan=2/>` |
| end_group | | | |

Ce rendu donne :

```
[ Prénom             ] [ Nom de famille     ]
[ Âge                ] [ Genre              ]
[ Adresse complète (occupe les deux colonnes)]
```

---

## Exemple : Saisie de données de parcelle en 3 colonnes

| type | name | label | appearance |
|------|------|-------|------------|
| begin_group | plot_data | Détails de la parcelle | `field-list grid(weight=3)` |
| text | plot_id | Identifiant de la parcelle | `gridformat<row=1 col=1/>` |
| decimal | area_ha | Superficie (ha) | `gridformat<row=1 col=2/>` |
| select_one crop_type | crop | Type de culture | `gridformat<row=1 col=3/>` |
| decimal | yield | Rendement (kg) | `gridformat<row=2 col=1/>` |
| decimal | revenue | Revenus | `gridformat<row=2 col=2/>` |
| text | notes | Notes | `gridformat<row=2 col=3/>` |
| end_group | | | |

---

## Couleurs de fond

Utilisez `backgroundcolor` pour distinguer visuellement les sections :

| type | name | label | appearance |
|------|------|-------|------------|
| note | section_a | Section A | `gridformat<row=1 col=1 colspan=2 backgroundcolor=#e8f4f8/>` |

---

## Bonnes pratiques

1. Utilisez la mise en page en grille uniquement pour les écrans **à forte intensité de saisie** où les champs côte à côte réduisent réellement le défilement.
2. Gardez les champs `colspan=1` courts (identifiants, codes, sélections courtes) — les longues étiquettes se tronquent mal dans les colonnes de grille étroites.
3. Utilisez `colspan=N` pour les champs avec de longues étiquettes ou des saisies de texte multi-lignes.
4. Testez sur la plus petite taille d'écran que vous attendez des enquêteurs — une grille à 4 colonnes est à l'étroit sur un téléphone.
5. La mise en page en grille fonctionne mieux sur les formulaires web et tablettes ; sur les téléphones mobiles, une mise en page à 2 colonnes est généralement la largeur maximale confortable.

## Limitations

- `gridformat<>` fonctionne uniquement dans un groupe avec l'apparence `grid(weight=N)` — il n'a aucun effet au niveau supérieur.
- La mise en page en grille est une extension de formulaire web rtSurvey et peut ne pas s'afficher correctement dans d'autres clients compatibles ODK.
- Le positionnement en lignes et colonnes n'est pas validé au moment de la construction du formulaire — les champs qui se chevauchent s'afficheront tous les deux mais peuvent sembler cassés.
