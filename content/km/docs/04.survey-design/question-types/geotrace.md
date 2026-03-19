---
title: "Geotrace"
description: "សំណួរ geotrace ឱ្យអ្នកឆ្លើយតបចាប់ series ចំណុចដែលភ្ជាប់គ្នានៅលើ map ដោយ create lines ឬ paths ជាផ្នែកនៃការស្ទង់មតិ។"
icon: "timeline"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 234
---

ប្រភេទសំណួរ geotrace ក្នុង XLSForms និង rtSurvey ឱ្យអ្នកឆ្លើយតបចាប់ series ចំណុចដែលភ្ជាប់គ្នានៅលើ map ដោយ create lines ឬ paths។ feature នេះមានប្រយោជន៍ជាពិសេសសម្រាប់ mapping routes, boundaries, ឬ linear features ក្នុង spatial surveys។

## ការបញ្ជាក់ XLSForm មូលដ្ឋាន

| type     | name        | label                           |
|----------|-------------|--------------------------------|
| geotrace | river_path  | Trace the path of the river     |

សម្រាប់ព័ត៌មានបន្ថែម សូមមើល [XLSForm specification](https://xlsform.org/en/#question-types)។

## ការប្រើប្រាស់

សំណួរ geotrace ប្រើជាទូទៅសម្រាប់:

1. Mapping routes ឬ paths ដែលចូលក្នុង field surveys
2. Tracing linear features ដូចជា roads, rivers, ឬ boundaries
3. ការចាប់ extent នៃ linear infrastructure (ឧ. pipelines, power lines)
4. ការ recording travel paths ក្នុង transportation studies
5. ការ defining transects ក្នុង ecological surveys

## ការអនុវត្តល្អ

1. ធានាថា device មាន location services enabled និង permissions ត្រូវបានអនុញ្ញាត។
2. ផ្តល់ការណែនាំច្បាស់អំពីរបៀប trace ផ្លូវ និង features ណាត្រូវ include។
3. ពិចារណា satellite imagery ឬ base maps ដើម្បីជួយ respondents trace paths ដែលត្រឹមត្រូវ។
4. ប្រុងប្រយ័ត្នអំពី potential complexity នៃ traces និង impact លើ data size ការ processing។

## ឧទាហរណ៍ការប្រើប្រាស់

| type     | name           | label                                      | hint                                        |
|----------|----------------|--------------------------------------------|--------------------------------------------|
| geotrace | hiking_trail   | Trace the path of the hiking trail         | Start at the trailhead and end at the summit |

## ទម្រង់ Data

ទិន្នន័យ geotrace ជាធម្មតារក្សាទុកជា string នៃ coordinate pairs ដែលបំបែកដោយ space ស្រដៀង geoshape ប៉ុន្តែ គ្មាន closing point:

```
lat1 lon1; lat2 lon2; lat3 lon3; ... latN lonN
```

ឧទាហរណ៍:
```
38.253094215699576 21.756382658677467; 38.25021274773806 21.756382658677467; 38.25007793942195 21.763892843919166; 38.25290886154963 21.763935759263404
```

## ការដាក់កំហិត

- ការ tracing paths ដែលត្រឹមត្រូវលើ small mobile screens អាចពិបាក។
- Complex traces ប្រហែលត្រូវការ storage និង processing capacity ច្រើន។
- ការប្រើ GPS continuous សម្រាប់ automatic tracing អាច drain battery device យ៉ាងឆាប់។
- ប្រហែលមាន privacy concerns ដែលទាក់ទង់ប្រមូល detailed path data។
