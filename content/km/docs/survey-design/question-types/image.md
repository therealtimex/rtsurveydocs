---
title: "Image"
description: "សំណួរ image ឱ្យអ្នកឆ្លើយតបចាប់ និង submit photos ជាផ្នែកនៃការស្ទង់មតិ។"
icon: "image"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 227
---

ប្រភេទសំណួរ image ក្នុង XLSForms និង rtSurvey ឱ្យអ្នកឆ្លើយតបចាប់ និង submit photos ជាផ្នែកនៃ survey responses ។ feature នេះមានប្រយោជន៍ជាពិសេសសម្រាប់ការប្រមូល visual data, ការ documenting observations, ឬការ providing evidence ក្នុង field surveys។

## ការបញ្ជាក់ XLSForm មូលដ្ឋាន

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| image | photo       | Take a photo of the location    |

សម្រាប់ព័ត៌មានបន្ថែម សូមមើល [XLSForm specification](https://xlsform.org/en/#question-types)។

## ការប្រើប្រាស់

សំណួរ image ប្រើជាទូទៅសម្រាប់:

1. ការ documenting field conditions ឬ observations
2. ការចាប់ visual evidence ក្នុង research studies
3. ការ collecting before-and-after photos ក្នុង impact assessments
4. ការ verifying completion នៃ tasks ឬ presence ក្នុង locations
5. ការ gathering visual data សម្រាប់ remote analysis

## ការអនុវត្តល្អ

1. ផ្តល់ការណែនាំច្បាស់អំពីអ្វីដែលគួរ photographed។
2. ពិចារណា privacy implications ហើយ inform respondents អំពីរបៀបប្រើ photos ។
3. ប្រុងប្រយ័ត្នអំពី file sizes និង storage limitations ជាពិសេសសម្រាប់ surveys ក្នុង areas ដែលមាន internet connectivity ជានិច្ច។
4. ធានាថា device មាន storage space គ្រប់គ្រាន់ ហើយ camera permissions ត្រូវបានអនុញ្ញាត។

## ឧទាហរណ៍ការប្រើប្រាស់

| type  | name           | label                                      | hint                                        |
|-------|----------------|--------------------------------------------|--------------------------------------------|
| image | storefront     | Take a photo of the store's entrance       | Ensure the store name is clearly visible    |

## ផ្នែកពង្រីករបស់ rtSurvey

ខណៈដែល XLSForm specification មូលដ្ឋានសម្រាប់ image គឺ straightforward rtSurvey អាចផ្តល់:

1. Image quality settings (ឧ. low, medium, high resolution)
2. Option ដើម្បីបន្ថែម captions ឬ tags ទៅ images
3. Multiple image capture សម្រាប់ question តែមួយ
4. Integration ជាមួយ native camera app ឬ gallery របស់ device

## ការដោះស្រាយ Data

Images ដែលប្រមូលតាមប្រភេទ question នេះជាធម្មតា:

1. ត្រូវបាន save ក្នុង common image format (ឧ. JPG, PNG)
2. ត្រូវបានរក្សាទុកជាមួយ survey data ផ្សេងទៀត ជាញឹកញាប់ក្នុង media folder ដាច់ដោយឡែក
3. អាចចូលប្រើសម្រាប់ viewing និង analysis តាមរយៈ survey management platform

## ការដាក់កំហិត

- Image files អាចធំ ដែលអាច impact data transfer និង storage។
- Devices ទាំងអស់ប្រហែលមិនមាន cameras ល្អ ឬ storage space គ្រប់គ្រាន់។
- ការ Analyzing images ចំនួនច្រើន អាច time-consuming។
- ប្រហែលមាន privacy concerns នៅពេល capture images ជាពិសេសក្នុង public spaces។
