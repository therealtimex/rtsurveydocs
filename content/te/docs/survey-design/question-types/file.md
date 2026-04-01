---
title: "File"
description: "File ప్రశ్నలు ప్రతిస్పందించే వ్యక్తులు వారి survey ప్రతిస్పందనల భాగంగా documents మరియు ఇతర files upload చేయడానికి అనుమతిస్తాయి."
icon: "upload_file"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 230
---

`file` ప్రశ్న రకం ప్రతిస్పందించే వ్యక్తులు వారి device నుండి **ఏ file అయినా upload** చేయడానికి అనుమతిస్తుంది — documents, spreadsheets, PDFs, లేదా ఇతర file types. Specific capture tools launch చేసే `image`, `audio`, మరియు `video` వలె కాకుండా, `file` general-purpose file picker తెరుస్తుంది.

## ప్రాథమిక XLSForm స్పెసిఫికేషన్

| type | name      | label                        |
|------|-----------|------------------------------|
| file | document  | Please upload your document  |

ప్రామాణిక file ప్రశ్న రకంపై మరిన్ని వివరాలకు, [XLSForm specification](https://xlsform.org/en/#question-types) చూడండి.

## వినియోగాలు

File ప్రశ్నలు సాధారణంగా వీటికి ఉపయోగిస్తారు:

1. Supporting documents సేకరించడం (receipts, certificates, contracts, reports)
2. Scan చేయబడిన paper forms upload చేయడం
3. ఇతర systems నుండి spreadsheets లేదా data exports సేకరించడం
4. image/audio/video cover చేయని ఏ digital file type

## ఉత్తమ పద్ధతులు

1. Upload చేయవలసిన దాని గురించి స్పష్టమైన సూచనలు అందించండి.
2. File size limitations గురించి ప్రతిస్పందించే వ్యక్తులకు తెలియజేయండి.
3. అందుబాటులో ఉన్న formats మరియు file size పరిమితులు స్పష్టంగా పేర్కొనండి.
4. Submission ముందు file అందుకోబడిందో confirm చేయడానికి ఫారం design లో plan చేయండి.

## పరిమితులు

- File uploads upload speed మరియు file size ఆధారంగా చాలా సమయం పట్టవచ్చు.
- చాలా పెద్ద files విఫలమవ్వవచ్చు లేదా network conditions ఆధారంగా time out అవ్వవచ్చు.
- File format validation server-side అమలు చేయాలి.
