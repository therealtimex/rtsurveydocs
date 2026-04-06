---
title: "Monitoring Data Quality"
description: "Techniques for ensuring accurate data collection in the field."
icon: "fact_check"
date: "2023-05-22T00:34:57+01:00"
lastmod: "2023-05-22T00:34:57+01:00"
draft: false
weight: 312
---

A key advantage of digital data collection systems like rtSurvey is the ability to actively monitor and enforce data quality while the survey is ongoing, rather than waiting until the end of the project.

## 1. Utilize Built-in Data Constraints

The first line of defense against poor data quality is the survey design itself. Form authors should rigorously apply constraints and logic:

- **Validation Rules:** Prevent impossible inputs. (e.g., "Age" cannot be less than 0 or greater than 120; "Date of Birth" cannot be in the future).
- **Required Questions:** Mark crucial questions as mandatory to prevent enumerators from skipping essential data points.
- **Skip Logic:** Use relevance rules to hide questions that do not apply based on previous answers, reducing enumerator fatigue and confusion.

## 2. Real-Time Monitoring Interface

Project managers should actively use the **Manage Submissions** and **Manage Quality** dashboards throughout the data collection phase:

- **Check Timestamps:** Review the start and end times of submitted records. Submissions completed unusually fast may indicate an enumerator rushed through the interview or fabricated data.
- **Review Media Evidence:** If the survey requires photographic evidence (e.g., a photo of a storefront or a signature), managers should spot-check these media attachments for validity and clarity.
- **GPS Auditing:** For household or geographic surveys, verify the random distribution of GPS coordinates on the Manage Quality map to ensure enumerators are physically visiting the assigned locations and not submitting records from a single spot.

## 3. Communication and Feedback

Identifying errors is only half the battle; correcting them is the other.

- **Return Instances:** If a reviewer finds a discrepancy or missing critical piece of evidence in a submission, use the **Return Instance** action in the Manage Submissions interface. This sends the specific record back to the enumerator's device for correction.
- **iNotes and Follow-ups:** Use the iNote system to leave internal comments for data cleaning or flag specific records for "Follow up" if supervisor intervention is needed in the field.

By combining rigid form rules with active oversight, teams can guarantee a high-quality, verifiable dataset.
