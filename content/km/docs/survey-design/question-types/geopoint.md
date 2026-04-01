---
title: "Geopoint"
description: "សំណួរ geopoint ចាប់ geographic coordinates (latitude, longitude, altitude, និង accuracy) ជាផ្នែកនៃការស្ទង់មតិ។"
icon: "location_on"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 232
---

ប្រភេទសំណួរ geopoint ក្នុង XLSForms និង rtSurvey ឱ្យប្រមូល geographic coordinates ដោយប្រើ GPS ឬ location services ផ្សេងៗ។ feature នេះមានប្រយោជន៍ជាពិសេសសម្រាប់ mapping survey responses, ការតាមដាន field activities, ឬការ associate data ជាមួយ locations ជាក់លាក់។

## ការបញ្ជាក់ XLSForm មូលដ្ឋាន

| type     | name        | label                           |
|----------|-------------|--------------------------------|
| geopoint | location    | Record the current location     |

សម្រាប់ព័ត៌មានបន្ថែម សូមមើល [XLSForm specification](https://xlsform.org/en/#question-types)។

## ការប្រើប្រាស់

សំណួរ geopoint ប្រើជាទូទៅសម្រាប់:

1. Mapping survey responses ភូមិសាស្ត្រ
2. ការបញ្ជាក់ location នៃ field activities
3. ការតាមដានផ្លូវ enumerators
4. ការ associate environmental ឬ social data ជាមួយ locations ជាក់លាក់
5. ការ calculating distances ឬ areas ក្នុង geographical analyses

## ការអនុវត្តល្អ

1. ធានាថា device មាន location services enabled និង permissions ត្រូវបានអនុញ្ញាត។
2. អនុញ្ញាតពេលវេលាគ្រប់គ្រាន់ដើម្បីឱ្យ GPS acquire accurate fix។
3. ពិចារណា privacy implications ហើយ inform respondents អំពីការប្រមូល location data។
4. ប្រើ ជាមួយ question types ផ្សេងទៀតដើម្បីផ្តល់ context សម្រាប់ location data។

## ឧទាហរណ៍ការប្រើប្រាស់

| type     | name           | label                                      | hint                                        |
|----------|----------------|--------------------------------------------|--------------------------------------------|
| geopoint | sample_location| Record the location of the sample collection | Stand in an open area for better GPS signal |

## ផ្នែកពង្រីករបស់ rtSurvey

ខណៈដែល XLSForm specification មូលដ្ឋានសម្រាប់ geopoint គឺ straightforward rtSurvey អាចផ្តល់:

1. Map integration សម្រាប់ visual confirmation នៃ location ដែលបានចាប់
2. Accuracy threshold settings
3. Option ដើម្បី manually input coordinates
4. Integration ជាមួយ offline maps សម្រាប់ remote areas

## ទម្រង់ Data

ទិន្នន័យ geopoint ជាធម្មតារក្សាទុកជា string នៃ 4 values ដែលបំបែកដោយ space:

```
latitude longitude altitude accuracy
```

ឧទាហរណ៍:
```
41.40338 2.17403 30.5 10
```

## ការពិចារណាសម្រាប់ Analysis

នៅពេលប្រើ geopoint questions ពិចារណា:

1. របៀប geographic data នឹងត្រូវ visualize (ឧ. mapping software)
2. ភាពត្រឹមត្រូវ coordinates ដែលប្រមូល និង impact របស់វាលើ analysis
3. Privacy និង data protection measures សម្រាប់ handling location data
4. ការ integration ពណ៌ប្រចាំ GIS (Geographic Information System) tools

## ការដាក់កំហិត

- ភាពត្រឹមត្រូវអាចប្រែប្រួលអាស្រ័យ device និង environmental conditions។
- GPS signals ប្រហែលខ្សោយ ឬ unavailable ក្នុង indoor locations ឬ areas ដែលមាន obstructions។
- ការប្រមូល location data ប្រហែល impact battery life device។
- ប្រហែលមាន privacy concerns ដែលទាក់ទង់ប្រមូល precise location data។
