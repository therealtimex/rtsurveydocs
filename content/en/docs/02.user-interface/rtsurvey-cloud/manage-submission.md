---
title: "Managing Submissions"
description: "Review, manage, and export raw data entries and submissions."
icon: "cloud"
date: "2023-05-22T00:34:57+01:00"
lastmod: "2023-05-22T00:34:57+01:00"
draft: false
weight: 317
---

The **Managing Submissions** module (accessed via the **Data View** button in the Form Family section) allows project managers and supervisors to directly interact with incoming raw data. It serves as a unified workspace to review enumerator submissions, trace device identifiers, and perform data quality operations.

![Managing Submissions Interface](/images/manage_submissions.png)

## Data Overview and Columns

The data grid dynamically displays data collected for a specific form. It operates in two main modes: **Official** (Finalized records) and **Working** (Real-Time, unfinalized records).

### Key Data Columns

Regardless of the custom questions defined in the form, the grid includes several standard metadata columns to help with auditing:

- **Submit by:** Identifies the origin platform of the submission (e.g., FA for Field App, WEB for Webform, RS for remote systems).
- **Detail:** Opens a focused, single-record view (Search icon) to inspect every variable and answer submitted for that instance.
- **iNote:** Allows supervisors to attach side-notes or internal comments to a specific record without altering the collected data itself (represented by a pencil icon).
- **Date fields:** Timestamps indicating when the record was initiated, completed, or synced.
- **Media attachments:** Direct thumbnail links to images, signatures, or files collected during the survey.
- **Repeat groups:** Dedicated links to access nested tables for repeated questions within the parent form.

## Submission Actions

To facilitate active data quality control, the interface provides a drop-down menu of actionable commands that can be executed on selected records:

- **Create a new instance:** Allows admins to manually enter a new survey record directly into the database.
- **Return instance:** Rejects the submitted record and tasks the enumerator to re-verify or re-collect the information.
- **Follow up instance:** Flags a record for further attention, usually dispatching an alert to the field team for clarification.
- **Export to Returned commands file / Follow-up commands package:** Generates batch exports (files) containing datasets specifically marked for returns or follow-ups.
- **Convert to XML:** Transforms the structured dataset back into its raw XML format for backend analysis or system integration.
- **Forward Instances:** (Available in *Working* mode) Pushes unfinalized data immediately to another device or user.
- **Delete:** Permanently removes selected instances from the database.
