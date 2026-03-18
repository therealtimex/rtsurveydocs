---
title: "Grid-layout"
description: "Grid layout lets you position fields in a CSS grid within a group, enabling multi-column form designs."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 296
---

The **Grid Layout** feature lets you arrange questions in a **multi-column grid** within a group, using the `gridformat<>` appearance tag. This is useful for dense data-entry forms where multiple related fields should appear side-by-side instead of stacked vertically.

---

## How it works

Grid layout is applied at two levels:

1. **The group** — set `appearance: field-list grid(weight=N)` to define how many columns the grid has
2. **Each field inside the group** — set `appearance: gridformat<row=R col=C colspan=S/>` to position the field

The grid uses a 12-column Bootstrap-style system. `weight=N` defines how many logical columns your grid has; each column occupies `12/N` Bootstrap columns.

---

## Group-level appearance

| Appearance | Description |
|------------|-------------|
| `field-list grid(weight=2)` | 2-column grid (each column = 6 Bootstrap cols) |
| `field-list grid(weight=3)` | 3-column grid (each column = 4 Bootstrap cols) |
| `field-list grid(weight=4)` | 4-column grid (each column = 3 Bootstrap cols) |
| `field-list grid(weight=6)` | 6-column grid (each column = 2 Bootstrap cols) |

---

## Field-level `gridformat<>` syntax

```
gridformat<row=R col=C colspan=S/>
gridformat<row=R col=C colspan=S backgroundcolor=COLOR/>
```

| Attribute | Description |
|-----------|-------------|
| `row` | Row number (1-based) |
| `col` | Column number (1-based, within the grid defined by `weight`) |
| `colspan` | Number of columns this field spans (default 1) |
| `backgroundcolor` | Optional CSS color for the field background (e.g., `#f0f0f0`, `lightblue`) |

---

## Example: 2-column household survey section

| type | name | label | appearance |
|------|------|-------|------------|
| begin_group | demographics | Demographics | `field-list grid(weight=2)` |
| text | first_name | First name | `gridformat<row=1 col=1/>` |
| text | last_name | Last name | `gridformat<row=1 col=2/>` |
| integer | age | Age | `gridformat<row=2 col=1/>` |
| select_one gender | gender | Gender | `gridformat<row=2 col=2/>` |
| text | address | Full address | `gridformat<row=3 col=1 colspan=2/>` |
| end_group | | | |

This renders as:

```
[ First name        ] [ Last name          ]
[ Age               ] [ Gender             ]
[ Full address (spans both columns)        ]
```

---

## Example: 3-column plot data entry

| type | name | label | appearance |
|------|------|-------|------------|
| begin_group | plot_data | Plot details | `field-list grid(weight=3)` |
| text | plot_id | Plot ID | `gridformat<row=1 col=1/>` |
| decimal | area_ha | Area (ha) | `gridformat<row=1 col=2/>` |
| select_one crop_type | crop | Crop type | `gridformat<row=1 col=3/>` |
| decimal | yield | Yield (kg) | `gridformat<row=2 col=1/>` |
| decimal | revenue | Revenue | `gridformat<row=2 col=2/>` |
| text | notes | Notes | `gridformat<row=2 col=3/>` |
| end_group | | | |

---

## Background colors

Use `backgroundcolor` to visually distinguish sections:

| type | name | label | appearance |
|------|------|-------|------------|
| note | section_a | Section A | `gridformat<row=1 col=1 colspan=2 backgroundcolor=#e8f4f8/>` |

---

## Best Practices

1. Use grid layout only for **data-entry intensive** screens where side-by-side fields genuinely reduce scrolling.
2. Keep `colspan=1` fields short (IDs, codes, short selects) — wide labels truncate badly in narrow grid columns.
3. Use `colspan=N` for fields with long labels or multi-line text inputs.
4. Test on the smallest screen size you expect enumerators to use — a 4-column grid is cramped on a phone.
5. Grid layout works best on web and tablet form factors; on mobile phones a 2-column layout is usually the maximum comfortable width.

## Limitations

- `gridformat<>` only works inside a group with `grid(weight=N)` appearance — it has no effect at the top level.
- Grid layout is an rtSurvey web form extension and may not render correctly in other ODK-compatible clients.
- Row and column positioning is not validated at form build time — overlapping fields will both render but may look broken.
