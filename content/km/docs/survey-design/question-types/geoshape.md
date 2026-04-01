---
title: "Geoshape"
description: "សំណួរ geoshape ឱ្យអ្នកឆ្លើយតប draw shapes លើ map ដោយចាប់ complex geographical data ជាផ្នែកនៃការស្ទង់មតិ។"
icon: "map"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 233
---

ប្រភេទសំណួរ geoshape ក្នុង XLSForms និង rtSurvey ឱ្យអ្នកឆ្លើយតប draw shapes (polygons) លើ map ដោយចាប់ complex geographical data។ feature នេះមានប្រយោជន៍ជាពិសេសសម្រាប់ mapping areas, ការកំណត់ boundaries, ឬ marking regions of interest ក្នុង spatial surveys។

## ការបញ្ជាក់ XLSForm មូលដ្ឋាន

| type     | name        | label                           |
|----------|-------------|--------------------------------|
| geoshape | field_area  | Draw the boundary of the field  |

សម្រាប់ព័ត៌មានបន្ថែម សូមមើល [XLSForm specification](https://xlsform.org/en/#question-types)។

## ការប្រើប្រាស់

សំណួរ geoshape ប្រើជាទូទៅសម្រាប់:

1. Mapping field boundaries ក្នុង agricultural surveys
2. ការកំណត់ areas នៃ environmental impact
3. Marking zones ក្នុង urban planning studies
4. Outlining regions សម្រាប់ geological surveys
5. ការចាប់ complex geographical features សម្រាប់ spatial analysis

## ការអនុវត្តល្អ

1. ធានាថា device មាន location services enabled និង permissions ត្រូវបានអនុញ្ញាត។
2. ផ្តល់ការណែនាំច្បាស់អំពីរបៀប draw shape និង area ណាត្រូវ include។
3. ពិចារណា satellite imagery ឬ base maps ដើម្បីជួយ respondents draw shapes ដែលត្រឹមត្រូវ។
4. ប្រុងប្រយ័ត្នអំពី potential complexity នៃ shapes និង impact លើ data size ការ processing។

## ឧទាហរណ៍ការប្រើប្រាស់

| type     | name           | label                                      | hint                                        |
|----------|----------------|--------------------------------------------|--------------------------------------------|
| geoshape | forest_area    | Outline the boundary of the forest patch   | Use at least 3 points to create a closed shape |

## ទម្រង់ Data

ទិន្នន័យ geoshape ជាធម្មតារក្សាទុកជា string នៃ coordinate pairs ដែលបំបែកដោយ space ដែលបញ្ចូលក្នុងវង់ក្រចក:

```
(lat1 lon1; lat2 lon2; lat3 lon3; ... latN lonN)
```

ឧទាហរណ៍:
```
(38.253094215699576 21.756382658677467; 38.25021274773806 21.756382658677467; 38.25007793942195 21.763892843919166; 38.25290886154963 21.763935759263404; 38.253094215699576 21.756382658677467)
```

## ការដាក់កំហិត

- ការ drawing shapes ដែលត្រឹមត្រូវលើ small mobile screens អាចពិបាក។
- Complex shapes ប្រហែលត្រូវការ storage និង processing capacity ច្រើន។
- Geoshape questions ប្រហែលមិនស័ក្តិសមសម្រាប់ survey types ឬ respondents ទាំងអស់។
- ប្រហែលមាន privacy concerns ដែលទាក់ទង់ប្រមូល detailed spatial data។
