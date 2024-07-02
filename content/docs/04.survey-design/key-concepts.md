---
title: "Key concepts"
description: "Overview of form design"
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 210
---

## What is an XLSForm?
rtSurvey supports XLSForm, which is a form standard designed to simplify the process of creating forms using Excel. 
With XLSForms, you can author forms in a human-readable format using the familiar Excel tool, making it accessible to almost everyone. 
This standard enables easy sharing and collaboration on form authoring. 
While XLSForms are beginner-friendly, they also allow experienced users to create complex forms. 
rtSurvey provides a consistent way to incorporate advanced functionalities such as skip logic into forms across various web and mobile data collection platforms.

## Basic format
Each Excel workbook usually has two worksheets: **survey** and **choices**. A third optional worksheet, called **settings**, can add additional specifications to your form and is described [below](https://xlsform.org/en/#settings-worksheet). 


It's important to note that the mandatory columns in the survey and choices worksheets must be present for the form to work properly. Optional columns in both worksheets provide further control over the behavior of each entry in the form but are not essential.

The columns in your Excel workbook can appear in any order, and optional columns can be left blank. However, it's crucial to use the precise syntax and naming conventions specified in the XLSForm documentation for the form to work correctly.

### The survey worksheet
The **survey worksheet** is where you define the structure of your form and provide the content. Each row in the survey worksheet represents a question or element in your form. The following columns are mandatory in the survey worksheet:

- `type`: Specifies the type of entry you are expecting for the question.
- `name`: Specifies the unique variable name for that entry. Names must start with a letter or an underscore and can only contain letters, digits, hyphens, underscores, and periods. Names are case-sensitive.
- `label`: Contains the actual text you see for the question in the form.

| type                | name     | label                |
| ------------------- | -------- | -------------------- |
| today               | today    |                      |
| select_one gender   | gender   | Respondent's gender? |
| integer             | age      | Respondent's age?    |

### The choices worksheet
The **`choices`** worksheet is used to specify the answer choices for multiple-choice questions. 
Each row represents an answer choice. The following columns are mandatory in the choices worksheet:

- **`list_name`**: Groups together a set of related answer choices.
- **`name`**: Specifies the unique variable name for that answer choice.
- **`label`**: Shows the answer choice exactly as you want it to appear on the form.

| list_name           | name        | label                |
| ------------------- | ----------- | -------------------- |
| gender              | transgender | Transgender          |
| gender              | female      | Female               |
| gender              | male        | Male                 |
| gender              | other       | Other                |

The columns you add to your Excel workbook, whether they are mandatory or optional, may appear in any order. Optional columns may be left out completely. Rows or columns may be left blank to aid readability, but data after 20 adjacent blank columns or rows on a sheet will not be processed. All .xlsx file formatting is ignored, so you can use dividing lines, shading, and other font formatting to make the form more readable.

One thing to keep in mind when authoring forms in Excel is that the syntax you use must be precise. For example, if you write **Choices** or **choice** instead of **choices**, the form won't work.

### Question types
XLSForm supports a number of question types. These are just some of the options you can enter in the **`type`** column in the **`survey`** worksheet in your XLSForm:

| Question type             | Answer input                                                                                 |
| ------------------------- | -------------------------------------------------------------------------------------------- |
| integer                   | Integer (i.e., whole number) input.                                                          |
| decimal                   | Decimal input.                                                                               |
| range                     | [Range](#range) input (including rating)                                                     |
| text                      | Free text response.                                                                          |
| select_one [options]      | [Multiple choice](#multiple-choice) question; only one answer can be selected.               |
| select_multiple [options] | [Multiple choice](#multiple-choice) question; multiple answers can be selected.              |
| select_one_from_file [file]| [Multiple choice from file](#multiple-choice-from-file); only one answer can be selected.      |
| select_multiple_from_file [file]| [Multiple choice from file](#multiple-choice-from-file); multiple answers can be selected.|
| rank [options]            | [Rank](#rank) question; order a list.                                                        |
| note                      | Display a note on the screen, takes no input. Shorthand for type=text with readonly=true.    |
| geopoint                  | Collect a [single GPS coordinate](#gps).                                                     |
| geotrace                  | Record a [line of two or more GPS coordinates](#gps).                                                |
| geoshape                  | Record a [polygon of multiple GPS coordinates](#gps); the last point is the same as the first point. |
| date                      | Date input.                                                                                  |
| time                      | Time input.                                                                                  |
| dateTime                  | Accepts a date and a time input.                                                             |
| image                     | Take a picture or upload an [image file](#image).                                            |
| audio                     | Take an audio recording or upload an audio file.                                             |
| background-audio          | Audio is recorded in the background while filling the form.                                  |
| video                     | Take a video recording or upload a video file.                                               |
| file                      | Generic file input (txt, pdf, xls, xlsx, doc, docx, rtf, zip)                                |
| barcode                   | Scan a barcode, requires the barcode scanner app to be installed.                            |
| calculate                 | Perform a calculation; see the [Calculation](#calculation) section below.                    |
| acknowledge               | Acknowledge prompt that sets value to "OK" if selected.                                      |
| hidden                    | A field with no associated UI element which can be used to store a constant                  |
| xml-external              | Adds a reference to an [external XML data](#external-xml-data) file                          |

## advanced format

rtSurvey expands the XLSForm standard by supporting additional capabilities such as `grid layout`, `html format`, and many new `widgets`.

### Grid layout
rtSurvey allows your form to mimic the look of traditional paper surveys by compacting multiple questions into one row.
