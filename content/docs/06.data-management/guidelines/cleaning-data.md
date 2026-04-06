---
title: "Post-Collection Cleaning"
description: "Reviewing, exporting, and sanitizing dataset submissions."
icon: "cleaning_services"
date: "2023-05-22T00:34:57+01:00"
lastmod: "2023-05-22T00:34:57+01:00"
draft: false
weight: 312
---

Even with stringent form constraints, survey data often requires some level of cleaning and review before it is ready for final analysis.

## 1. In-System Data Review

Use the **Manage Submissions** interface to conduct initial reviews of incoming data.

- **Spot-Checking:** Frequently review a random sample of submitted records to identify misunderstanding of questions by enumerators.
- **Handling Outliers:** If you notice extreme outliers in the data grid, use the **Return Instance** feature (if the enumerator is still in the field) or leave an **iNote** to document the anomaly for the data cleaning team.
- **Duplicate Checks:** Look for duplicate submissions, which can happen if an enumerator accidentally interviews the same respondent twice or if there was a device syncing issue.

## 2. Exporting for Cleaning

While basic review happens within the CPMS, intensive data cleaning usually requires external statistical software.

- Navigate to the **Manage Submissions** or the specific Data View for your form.
- Export the dataset to standard formats like `.csv` or `.xlsx`. 
- For advanced users, exports can be tailored for immediate import into statistical packages like Stata, SPSS, or R.

## 3. External Cleaning Procedures

Once your dataset is in an external tool (like Excel or Stata), standard cleaning procedures apply:

- **Removing PII:** If the dataset will be shared with external researchers or public stakeholders, immediately anonymize the data by removing Personally Identifiable Information (PII) like names, exact addresses, and phone numbers.
- **Standardizing Text:** Clean up open-ended text responses by standardizing spellings or categorizing common answers.
- **Handling Missing Values:** Decide on a consistent strategy for handling missing data (e.g., leaving it blank, using a specific code like `-999`, or imputing values) before running analyses.
- **Recoding Variables:** You may need to collapse continuous variables into categories (e.g., changing exact ages into "Age Groups") for easier reporting.
