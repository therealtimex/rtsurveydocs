---
title: "Repeating questions"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 260
---

Repeats are a powerful feature in rtSurvey that allow you to collect the same set of information multiple times within a single survey. This is particularly useful for scenarios such as household surveys, where you might need to gather data about multiple household members.

## Basic Repeat Structure

To create a repeat in rtSurvey, use the `begin repeat` and `end repeat` construct:

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat |                      |
| text         | name         | Child's name         |
| decimal      | birthweight  | Child's birthweight  |
| select_one male_female | sex | Child's sex         |
| end repeat   |              |                      |
```

In this example, the user can collect information about multiple children by adding new repeats in the form.

## Labeling Repeats

While the `label` column is optional for `begin repeat`, adding a label can improve navigation:

```
| type         | name         | label                |
|--------------|--------------|----------------------|
| begin repeat | child_repeat | Child Information    |
| text         | name         | Child's name         |
| decimal      | birthweight  | Child's birthweight  |
| select_one male_female | sex | Child's sex         |
| end repeat   |              |                      |
```

rtSurvey will display "Child Information" as a title for each repeat instance.

## Fixed Repeat Counts

To specify a fixed number of repeats, use the `repeat_count` column:

```
| type         | name         | label                | repeat_count |
|--------------|--------------|----------------------|--------------|
| begin repeat | child_repeat | Child Information    | 3            |
| text         | name         | Child's name         |              |
| decimal      | birthweight  | Child's birthweight  |              |
| end repeat   |              |                      |              |
```

This will create exactly 3 child repeats.

## Dynamic Repeat Counts

rtSurvey supports dynamic repeat counts based on previous answers:

```
| type     | name           | label                          | repeat_count       |
|----------|----------------|--------------------------------|--------------------|
| integer  | num_hh_members | Number of household members?   |                    |
| begin repeat | hh_member  | Household Member               | ${num_hh_members}  |
| text     | name           | Name                           |                    |
| integer  | age            | Age                            |                    |
| end repeat |              |                                |                    |
```

## Conditional Repeats

You can use the `relevant` column to conditionally display repeats:

```
| type              | name        | label                     | relevant           |
|-------------------|-------------|---------------------------|---------------------|
| select_one yes_no | has_child   | Do any children live here?|                     |
| begin repeat      | child_repeat| Child Information         | ${has_child} = 'yes'|
| text              | name        | Child's name              |                     |
| decimal           | birthweight | Child's birthweight       |                     |
| end repeat        |             |                           |                     |
```

## rtSurvey-Specific Features

### Repeat Summary

rtSurvey provides a summary view of repeats. To customize the summary, use a group within the repeat:

```
| type         | name         | label                                    |
|--------------|--------------|------------------------------------------|
| begin repeat | person_repeat|                                          |
| begin group  | person       | ${first_name} ${last_name} - ${age}      |
| text         | first_name   | First name                               |
| text         | last_name    | Last name                                |
| integer      | age          | Age                                      |
| end group    |              |                                          |
| end repeat   |              |                                          |
```

### Repeat Appearance Options

rtSurvey offers additional appearance options for repeats:

- `appearance: field-list` - Displays all questions in a repeat on one screen
- `appearance: table-list` - Presents repeats in a tabular format

```
| type         | name         | label            | appearance  |
|--------------|--------------|-------------------|-------------|
| begin repeat | child_repeat | Child Information | table-list  |
| text         | name         | Name              |             |
| integer      | age          | Age               |             |
| end repeat   |              |                   |             |
```

### Nested Repeats

rtSurvey supports nested repeats for complex data structures:

```
| type         | name           | label                |
|--------------|----------------|----------------------|
| begin repeat | household      | Household            |
| text         | hh_name        | Household Name       |
| begin repeat | hh_member      | Household Member     |
| text         | member_name    | Member Name          |
| integer      | member_age     | Member Age           |
| end repeat   |                |                      |
| end repeat   |                |                      |
```

## Best Practices for Using Repeats in rtSurvey

1. Use meaningful names and labels for repeats to improve data analysis.
2. Consider using dynamic repeat counts to reduce data entry errors.
3. Test your form thoroughly, especially when using complex nested repeats.
4. Use the summary feature to help enumerators navigate long lists of repeats.
5. Be cautious with large numbers of repeats, as they can impact form performance.

## Handling Zero Repeats

To represent zero repeats in rtSurvey:

1. Train enumerators to delete the first repeat if not needed.
2. Use dynamic repeat counts when the exact number is known.
3. Use `relevant` to conditionally display repeats.

## Data Export Considerations

When exporting data from rtSurvey, repeat data is typically flattened. Each repeat instance becomes a separate row in the exported data, with the parent form's data repeated for each instance.

## Mobile App Considerations

- Repeats in the rtSurvey mobile app support offline data collection.
- Large numbers of repeats may impact app performance on low-end devices.

By effectively using repeats in rtSurvey, you can create flexible and powerful surveys capable of capturing complex, hierarchical data structures while maintaining a user-friendly interface for enumerators.
