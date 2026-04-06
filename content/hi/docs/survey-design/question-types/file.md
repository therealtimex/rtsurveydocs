---
title: "File"
description: "File questions उत्तरदाताओं को अपने survey responses के हिस्से के रूप में documents और अन्य files upload करने देते हैं।"
icon: "upload_file"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 230
---

`file` question type उत्तरदाताओं को अपने device से **कोई भी file upload** करने की अनुमति देता है — documents, spreadsheets, PDFs, या अन्य file types। `image`, `audio`, और `video` के विपरीत जो specific capture tools launch करते हैं, `file` एक general-purpose file picker खोलता है।

## Basic XLSForm Specification

| type | name      | label                        |
|------|-----------|------------------------------|
| file | document  | कृपया अपना document upload करें |

Standard file question type के बारे में अधिक जानकारी के लिए, [XLSForm specification](https://xlsform.org/en/#question-types) देखें।

## उपयोग

File questions सामान्यतः इनके लिए उपयोग किए जाते हैं:

1. Supporting documents एकत्र करना (receipts, certificates, contracts, reports)
2. Scanned paper forms upload करना
3. अन्य systems से spreadsheets या data exports gather करना
4. कोई भी digital file type जिसे image/audio/video cover नहीं करते

## Data format

Uploaded files binary attachments के रूप में store होती हैं:

- **Format:** Original format में preserved (PDF, XLSX, DOCX, आदि)
- **Naming:** `{instanceID}-{fieldname}.{extension}`
- **Storage:** Submission के साथ server media folder में upload होती हैं
- **Access:** Submission management interface से downloadable

## rtSurvey extensions

### Accepted file types

कौन से file types चुने जा सकते हैं इसे restrict करने के लिए `parameters` column का उपयोग करें:

| type | name | label | parameters |
|------|------|-------|------------|
| file | report | Inspection report upload करें | `accept=.pdf` |
| file | spreadsheet | Data file upload करें | `accept=.xlsx,.csv` |

`accept` parameter standard file extension syntax (comma-separated) का उपयोग करता है।

### File size guidance

rtSurvey question level पर hard file-size limit enforce नहीं करता, लेकिन server upload limit apply होती है। गणनाकर्ता को expectations communicate करने के लिए `hint` का उपयोग करें:

| type | name | label | hint |
|------|------|-------|------|
| file | receipt | Payment receipt upload करें | Accepted: PDF या image। Maximum file size: 5 MB |

### Device file system और cloud storage के साथ integration

Android और iOS पर, `file` question device का native file picker खोलता है, जिसमें access हो सकती है:
- Local device storage
- SD card (Android)
- iCloud Drive (iOS)
- Google Drive, Dropbox (यदि installed हो)

Web पर, यह browser का standard file upload dialog खोलता है।

## Example usage

### Required PDF upload

| type | name | label | hint | required | required_message |
|------|------|-------|------|----------|-----------------|
| file | signed_consent | Signed consent form upload करें | केवल PDF, max 2MB | yes | Consent form आवश्यक है |

### Conditional document upload

| type | name | label | relevant |
|------|------|-------|----------|
| select_one yesno | has_land_title | क्या household के पास land title है? | |
| file | land_title_doc | Land title की photo या scan upload करें | `${has_land_title} = 'yes'` |

## Best Practices

1. File types restrict करने के लिए `accept` का उपयोग करें — यह गणनाकर्ताओं को accidentally wrong files upload करने से रोकता है।
2. `hint` column में size और format guidance हमेशा शामिल करें।
3. Photos और images के लिए, `image` type का उपयोग करें — यह better compression और consistent format handling प्रदान करता है।
4. File attachments के साथ large surveys के लिए, अपने data storage और download bandwidth की plan करें।
5. Target device type (Android vs. iOS vs. web) पर file picker test करें — cloud drives तक access vary करती है।

## Data handling considerations

- Files को उनके original format में store किया जाता है; rtSurvey द्वारा convert या compress नहीं किया जाता।
- Download के बाद files analyze करें — rtSurvey file contents extract या index नहीं करता।
- Large file attachments full dataset download करने के लिए आवश्यक समय को significantly बढ़ाते हैं।

## सीमाएं

- File questions file contents validate नहीं करते — केवल `accept` के माध्यम से file extension check UI level पर enforce होता है।
- बहुत बड़ी files (100 MB+) low-connectivity environments में upload पर time out हो सकती हैं।
- Offline enumerators files attach कर सकते हैं लेकिन वे connectivity restore होने तक upload नहीं होंगी।
- कुछ device configurations कुछ storage locations तक access को restrict करते हैं।
