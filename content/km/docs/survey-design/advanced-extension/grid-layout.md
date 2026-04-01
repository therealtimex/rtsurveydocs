---
title: "Grid Layout"
description: "Grid layout ឱ្យ position fields ក្នុង CSS grid ក្នុង group, enabling multi-column form designs។"
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 296
---

**Grid Layout** feature ឱ្យ arrange questions ក្នុង **multi-column grid** ។

---

## How it works

Grid layout ត ្ រ ូ វ អ ន ុ វ ត ្ ត ក ្ ន ុ ង levels ពី រ :

1. **Group** — set `appearance: field-list grid(weight=N)`
2. **Fields** — set `appearance: gridformat<row=R col=C colspan=S/>`

---

## Group-level appearance

| Appearance | ការពិពណ៌នា |
|------------|-------------|
| `field-list grid(weight=2)` | 2-column grid |
| `field-list grid(weight=3)` | 3-column grid |
| `field-list grid(weight=4)` | 4-column grid |

---

## Field-level `gridformat<>` syntax

```
gridformat<row=R col=C colspan=S/>
gridformat<row=R col=C colspan=S backgroundcolor=COLOR/>
```

| Attribute | ការពិពណ៌នា |
|-----------|-------------|
| `row` | Row number (1-based) |
| `col` | Column number (1-based) |
| `colspan` | ចំ នួ ន columns ដ ែ ល field span |
| `backgroundcolor` | CSS color ស ្ រ ើ ច ចិ ត ្ ត |

---

## Example: 2-column household survey

| type | name | label | appearance |
|------|------|-------|------------|
| begin_group | demographics | Demographics | `field-list grid(weight=2)` |
| text | first_name | First name | `gridformat<row=1 col=1/>` |
| text | last_name | Last name | `gridformat<row=1 col=2/>` |
| integer | age | Age | `gridformat<row=2 col=1/>` |
| text | address | Full address | `gridformat<row=3 col=1 colspan=2/>` |
| end_group | | | |

---

## Best Practices

1. ប ្ រ ើ grid layout ស ម ្ រ ា ប ់ screens data-entry intensive ។
2. Test ន ៅ ល ើ screen size ត ូ ច ជ ា ង ។
3. Grid layout ល ្ អ ជ ា ង ន ៅ web ហ ើ យ tablet ។

## Limitations

- `gridformat<>` ដ ំ ណ ើ រ ការ ប ា ន ត ែ ក ្ ន ុ ង group ដ ែ ល ម ា ន `grid(weight=N)` ។
- Grid layout ជ ា rtSurvey web form extension ។
