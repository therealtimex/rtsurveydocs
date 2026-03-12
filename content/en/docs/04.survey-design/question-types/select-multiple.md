---
title: "Select_multiple"
description: ""
icon: "check_box"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 225
---

### select_multiple listname

The "select_multiple listname" prompts the user to select one or more choices from a predefined list of choices. In a xlsform definition, the "listname" should correspond to a value listed in the choices worksheet's list_name column (e.g., "country").

By default, the choices are displayed as checkboxes, where each checkbox represents a single static choice from the specified list. However, there are various appearance options available to customize the look, functionality, and even the choice list itself. Please refer to the sub-sections below for more information on those options.

When exporting the data, each row will include a column with a space-separated list of all chosen response values for each select_multiple field.

When using a select_multiple field in field validation or skip patterns (constraint or relevance expressions), the "selected()" function needs to be utilized to check whether a specific choice has been selected. You can find more information on constraint and relevance expressions in the help topics.

In the xlsform definition:

| Type                  | Name      | Label          | Appearance |
|-----------------------|-----------|----------------|------------|
| select_multiple listname | fieldname | question text |            |