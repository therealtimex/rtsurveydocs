---
title: "File"
description: "សំណួរ file ឱ្យអ្នកឆ្លើយតប upload documents និង files ផ្សេងទៀតជាផ្នែកនៃ survey responses ។"
icon: "upload_file"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 230
---

ប្រភេទ question `file` ឱ្យអ្នកឆ្លើយតប **upload ឯកសារណាមួយ** ពី device ពួកគេ — documents, spreadsheets, PDFs, ឬ file types ផ្សេងទៀត។ មិនដូច `image`, `audio`, និង `video` ដែល launch specific capture tools ទេ `file` opens file picker general-purpose។

## ការបញ្ជាក់ XLSForm មូលដ្ឋាន

| type | name      | label                        |
|------|-----------|------------------------------|
| file | document  | Please upload your document  |

សម្រាប់ព័ត៌មានបន្ថែម សូមមើល [XLSForm specification](https://xlsform.org/en/#question-types)។

## ការប្រើប្រាស់

សំណួរ file ប្រើជាទូទៅសម្រាប់:

1. ការ collecting supporting documents (receipts, certificates, contracts, reports)
2. ការ uploading completed paper forms ដែលបាន scan
3. ការ gathering spreadsheets ឬ data exports ពី systems ផ្សេងទៀត
4. ប្រភេទ digital file ណាដែល image/audio/video មិនគ្រប

## ទម្រង់ Data

Uploaded files ត្រូវបានរក្សាទុកជា binary attachments:

- **Format:** ការ preserve ក្នុង original format (PDF, XLSX, DOCX, ។ល។)
- **Naming:** `{instanceID}-{fieldname}.{extension}`
- **Storage:** Upload ទៅ server media folder ជាមួយ submission
- **Access:** Downloadable ពី submission management interface

## ផ្នែកពង្រីករបស់ rtSurvey

### Accepted file types

ប្រើជួរ `parameters` ដើម្បីដាក់ restriction ថាតើ file types ណាអាចត្រូវបានជ្រើស:

| type | name | label | parameters |
|------|------|-------|------------|
| file | report | Upload the inspection report | `accept=.pdf` |
| file | spreadsheet | Upload the data file | `accept=.xlsx,.csv` |

parameter `accept` ប្រើ standard file extension syntax (comma-separated)។

### ការណែនាំ File size

rtSurvey មិន enforce hard file-size limit ក្នុង question level ប៉ុន្តែ server upload limit អនុវត្ត។ ប្រើ `hint` ដើម្បីប្រាស្រ័យ expectations ទៅ enumerator:

| type | name | label | hint |
|------|------|-------|------|
| file | receipt | Upload the payment receipt | Accepted: PDF or image. Maximum file size: 5 MB |

## ឧទាហរណ៍ការប្រើប្រាស់

### Required PDF upload

| type | name | label | hint | required | required_message |
|------|------|-------|------|----------|-----------------|
| file | signed_consent | Upload the signed consent form | PDF only, max 2MB | yes | A consent form is required |

### Conditional document upload

| type | name | label | relevant |
|------|------|-------|----------|
| select_one yesno | has_land_title | Does the household have a land title? | |
| file | land_title_doc | Upload a photo or scan of the land title | `${has_land_title} = 'yes'` |

## ការអនុវត្តល្អ

1. ប្រើ `accept` ដើម្បីដាក់ restriction file types — នេះការពារ enumerators ពីការ upload files ខុស។
2. ដូចជារួមបញ្ចូល size និង format guidance ក្នុងជួរ `hint`។
3. សម្រាប់ photos និង images ប្រើប្រភេទ `image` ជំនួស — វាផ្តល់ compression ល្អ និង consistent format handling។
4. សម្រាប់ surveys ធំ ជាមួយ file attachments plan storage data ហើយ download bandwidth ស្របគ្នា។
5. Test file picker លើ target device type (Android vs. iOS vs. web) មុន deployment — access ទៅ cloud drives ប្រែប្រួល។

## ការពិចារណាការ handling data

- Files ត្រូវបានរក្សាទុកក្នុង original format; ពួកវាមិន converted ឬ compressed ដោយ rtSurvey។
- Analyse files ក្រោយ download — rtSurvey មិន extract ឬ index file contents។
- File attachments ធំ increase time ដែលចាំបាច់ download full dataset ។

## ការដាក់កំហិត

- File questions មិន validate file contents — តែ file extension check តាម `accept` ត្រូវបានកំណត់ ក្នុង UI level។
- Files ធំណាស់ (100 MB+) ប្រហែល time out ក្នុង upload ក្នុង low-connectivity environments។
- Offline enumerators អាច attach files ប៉ុន្តែ ពួកវានឹងមិន upload ទាល់ connectivity ត្រូវបានស្ដារ។
- Device configurations ខ្លះ ដាក់ restriction access ទៅ storage locations ជាក់លាក់ (ឧ. corporate MDM policies)។
