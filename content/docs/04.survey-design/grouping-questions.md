---
title: "Grouping questions"
description: ""
icon: "auto_awesome"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 250
---

Groups in XLSForm allow you to organize related questions together, improving the structure of your survey and enhancing data analysis capabilities. rtSurvey fully supports XLSForm groups and extends their functionality with additional features.

## Basic Group Structure

To create a group of questions, use the `begin_group` and `end_group` syntax:

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | respondent | Respondent Information                   |
| text         | name       | Enter the respondent's name              |
| text         | position   | Enter the respondent's position          |
| end_group    |            |                                          |
```

Key points:
- The `begin_group` row requires a `name` and `label`.
- The `end_group` row doesn't need a name or label.
- Questions between `begin_group` and `end_group` are part of the group.

## Group Appearance

rtSurvey supports various appearance options for groups:

1. **field-list**: Displays multiple questions on the same screen.
   ```
   | type         | name       | label     | appearance |
   |--------------|------------|-----------|------------|
   | begin_group  | respondent | Respondent| field-list |
   | text         | name       | Name      |            |
   | text         | position   | Position  |            |
   | end_group    |            |           |            |
   ```

2. **grid**: Creates a compact, table-like layout for groups (rtSurvey-specific).
   ```
   | type         | name       | label     | appearance |
   |--------------|------------|-----------|------------|
   | begin_group  | household  | Household | grid       |
   | text         | member_name| Name      |            |
   | integer      | member_age | Age       |            |
   | end_group    |            |           |            |
   ```

3. **collapsible**: Creates expandable/collapsible groups (rtSurvey-specific).
   ```
   | type         | name       | label     | appearance  |
   |--------------|------------|-----------|-------------|
   | begin_group  | details    | Details   | collapsible |
   | text         | address    | Address   |             |
   | text         | phone      | Phone     |             |
   | end_group    |            |           |             |
   ```

## Nested Groups

Groups can be nested within other groups for more complex structures:

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | hospital   | Hospital Information                     |
| text         | hosp_name  | What is the name of this hospital?       |
| begin_group  | medication | Medication Availability                  |
| select_one y_n| hiv_meds  | Does this hospital have HIV medication?  |
| end_group    |            |                                          |
| end_group    |            |                                          |
```

**Note**: Always end the most recently started group first to maintain proper nesting.

## Skip Logic for Groups

Use the `relevant` column to implement skip logic for entire groups:

```
| type         | name   | label                                        | relevant        |
|--------------|--------|----------------------------------------------|-----------------|
| integer      | age    | How old are you?                             |                 |
| begin_group  | child  | Child                                        | ${age} <= 5     |
| integer      | muac   | Record child's mid-upper arm circumference   |                 |
| select_one y_n| mrdt  | Is the child's rapid diagnostic test positive?|                |
| end_group    |        |                                              |                 |
```

In this example, the `child` group will only appear if the respondent's age is 5 or younger.

## Best Practices for Using Groups

1. Use meaningful names for groups to improve data analysis.
2. Keep groups focused on related questions.
3. Use nested groups judiciously to avoid overly complex structures.
4. Test skip logic thoroughly when using `relevant` on groups.
5. Consider using `field-list` appearance for short groups to reduce scrolling.
6. Utilize rtSurvey's grid layout for compact display of related information.
7. Use collapsible groups for long forms to improve navigation.

## rtSurvey-Specific Features

1. **Grid Layout**: Use the `grid` appearance for table-like displays.
2. **Collapsible Groups**: Implement `collapsible` appearance for expandable sections.
3. **Custom Styling**: Apply custom CSS to groups for unique visual designs.
4. **Dynamic Group Behavior**: Implement complex skip logic and calculations within groups.

## Multilingual Support

rtSurvey supports multilingual groups. Use language-specific columns for labels:

```
| type         | name       | label::English | label::French |
|--------------|------------|----------------|---------------|
| begin_group  | personal   | Personal Info  | Infos Personnelles |
| text         | name       | Name           | Nom           |
| end_group    |            |                |               |
```

## Mobile App Considerations

- Groups with the `field-list` appearance are displayed as a single screen in the mobile app.
- Collapsible groups can improve navigation on smaller screens.
- Grid layouts may adjust for better visibility on mobile devices.

## Known Limitations

- Extremely deep nesting of groups may affect performance on some devices.
- Some advanced styling options may not be available for groups in the mobile app.

## Troubleshooting Groups

1. Ensure each `begin_group` has a corresponding `end_group`.
2. Check that group names are unique within the form.
3. Verify that skip logic references correct question names.
4. Test groups thoroughly on both web and mobile interfaces.

By effectively using groups in your XLSForms with rtSurvey, you can create well-organized, efficient surveys that improve both the data collection experience and the quality of your data analysis.
