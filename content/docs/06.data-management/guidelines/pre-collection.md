---
title: "Pre-Collection Validation"
description: "Preventing bad data from entering the system at the source."
icon: "gpp_good"
date: "2023-05-22T00:34:57+01:00"
lastmod: "2023-05-22T00:34:57+01:00"
draft: false
weight: 311
---

The most effective data management strategy is preventing errors before they occur. By designing smart, validated forms, you minimize the amount of post-collection data cleaning required.

## 1. Enforcing Constraints and Validation logic

When building your survey in the Form Builder or via XLSForm, vigorously apply validation criteria:

- **Numerical Boundaries:** Restrict integer or decimal questions to realistic ranges (e.g., household size must be between 1 and 30).
- **Text Length Limits:** Use regular expressions (regex) or character limits to ensure phone numbers or national IDs follow exact formats.
- **Date Constraints:** Prevent enumerators from selecting future dates for events that happened in the past (e.g., Date of Birth).

## 2. Using Skip Logic (Relevance)

Do not rely on enumerators to manually skip questions based on previous answers. 

- Build **Skip Logic** (or relevance conditions) directly into the form. If a respondent is male, the form should automatically hide all questions related to pregnancy. 
- This reduces survey fatigue, prevents contradictory data, and speeds up the interview process.

## 3. Mandatory Questions

Ensure that critical survey questions cannot be accidentally skipped. 

- Mark essential identifiers (like Respondent Name, GPS Location, or Consent confirmation) as **Required**. 
- The enumerator will not be able to finalize the form on the mobile app or web browser until all required fields are answered.

## 4. Testing the Instrument

Before deploying a form to a live enumerator team, thoroughly field-test the instrument.

- Create "dummy" submissions that intentionally try to break your validation rules. 
- Ensure that the error messages displayed to the enumerator are clear and helpful, guiding them to provide the correct format.
