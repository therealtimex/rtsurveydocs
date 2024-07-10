---
title: "File"
description: "File questions allow respondents to upload files as part of their survey responses."
icon: "upload_file"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 230
---

The file question type in XLSForms and rtSurvey enables respondents to upload files as part of their survey responses. This feature is particularly useful for collecting documents, images, or other file types relevant to the survey.

## Basic XLSForm Specification

| type | name      | label                       |
|------|-----------|----------------------------|
| file | document  | Please upload your document |

For more details on the basic file question type, see the [XLSForm specification](https://xlsform.org/en/#question-types).

## Uses

File questions are commonly used for:

1. Collecting supporting documents (e.g., receipts, certificates)
2. Gathering visual evidence (e.g., photos of field conditions)
3. Uploading completed forms or spreadsheets
4. Collecting any type of digital file relevant to the survey

## Best Practices

1. Provide clear instructions on what type of file to upload and any size limitations.
2. Consider privacy implications and inform respondents about how their files will be used and stored.
3. Be mindful of file sizes and storage limitations, especially for surveys in areas with limited internet connectivity.
4. Specify accepted file formats if necessary.

## Example Usage

Here's an example of how you might use a file question in a survey:

| type | name           | label                                      | hint                                        |
|------|----------------|--------------------------------------------|--------------------------------------------|
| file | receipt_upload | Please upload a photo of your receipt      | Accepted formats: JPG, PNG. Max size: 5MB   |

## rtSurvey Extensions

While the basic XLSForm specification for file questions is straightforward, rtSurvey may offer additional features or customizations:

1. File type restrictions (e.g., only images, only PDFs)
2. File size limitations
3. Multiple file upload capability
4. Integration with device's file system or cloud storage services

(Note: The specific extensions available in rtSurvey for file questions would need to be confirmed and detailed here.)

## Data Handling

Files collected through this question type are typically:

1. Saved in their original format
2. Stored alongside other survey data, often in a separate media folder
3. Accessible for download and analysis through the survey management platform

## Considerations for Analysis

When using file questions, consider:

1. How the uploaded files will be processed and analyzed
2. The additional storage space required for file attachments
3. Privacy and data protection measures for storing and handling uploaded files
4. Potential need for specialized software to open or analyze certain file types

## Limitations

- Large files can significantly impact data transfer and storage requirements.
- Not all devices may have easy access to files for uploading.
- Analyzing file attachments can be more time-consuming than text-based responses.
- There may be compatibility issues with certain file types across different systems.

