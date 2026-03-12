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
  
The "select_one listname" prompts the user to choose a single option from a predefined list of choices. In an xlsform definition, the "listname" should correspond to a value listed in the choices worksheet's list_name column (e.g., "yesno").

By default, the choices are displayed as radio buttons, with each button representing a single static choice from the specified list. However, there are various appearance options available to customize the look, behavior, and choice list itself. Refer to the sub-sections below for more information on those options.

In the xlsform definition:
{{< table "table table-striped" >}}
| Type             | Name      | Label          | Appearance |
|------------------|-----------|----------------|------------|
| select_one listname | fieldname | question text |            |
{{</ table >}}
  
### Basic appearance options

Specify the following values in the appearance column to modify the appearance of the select_one listname field:

- "quick": Automatically advances to the next question as soon as an option is selected, without waiting for the user to swipe forward.
- "minimal": Displays a single drop-down selector instead of radio buttons.
- "compact": Shows a compact table of options. The number of columns will depend on the display width.
- "compact-#": Forces a specific number of columns in the compact table, where "#" represents the desired number of columns.
- "quickcompact": Combines the "quick" and "compact" appearances.
- "quickcompact-#": Combines the "quick" and "compact" appearances and forces a specific number of columns.

In the xlsform definition:  
{{< table "table table-striped" >}}
| Type             | Name      | Label          | Appearance       |
|------------------|-----------|----------------|------------------|
| select_one listname | fieldname | question text | quick            |
| select_one listname | fieldname | question text | minimal          |
| select_one listname | fieldname | question text | compact          |
| select_one listname | fieldname | question text | compact-#        |
| select_one listname | fieldname | question text | quickcompact     |
| select_one listname | fieldname | question text | quickcompact-#   |
{{</ table >}}