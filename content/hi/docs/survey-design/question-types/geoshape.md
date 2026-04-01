---
title: "Geoshape"
description: "Geoshape questions उत्तरदाताओं को map पर shapes draw करने देते हैं, survey के हिस्से के रूप में complex geographical data capture करते हैं।"
icon: "map"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 233
---

XLSForms और rtSurvey में geoshape question type उत्तरदाताओं को map पर shapes (polygons) draw करने में सक्षम बनाता है, complex geographical data capture करता है। यह सुविधा areas map करने, boundaries define करने, या spatial surveys में interest के regions mark करने के लिए विशेष रूप से उपयोगी है।

## Basic XLSForm Specification

| type     | name        | label                           |
|----------|-------------|--------------------------------|
| geoshape | field_area  | Field की boundary draw करें    |

Basic geoshape question type के बारे में अधिक जानकारी के लिए, [XLSForm specification](https://xlsform.org/en/#question-types) देखें।

## उपयोग

Geoshape questions सामान्यतः इनके लिए उपयोग किए जाते हैं:

1. Agricultural surveys में field boundaries map करना
2. Environmental impact के areas define करना
3. Urban planning studies में zones mark करना
4. Geological surveys के लिए regions outline करना
5. Spatial analysis के लिए complex geographical features capture करना

## Best Practices

1. सुनिश्चित करें कि device में location services enabled हों और permissions granted हों।
2. Shape कैसे draw करें और कौन सा area शामिल होना चाहिए, इस पर clear instructions प्रदान करें।
3. Shapes accurately draw करने में उत्तरदाताओं की मदद के लिए satellite imagery या base maps का उपयोग करने पर विचार करें।
4. Shapes की potential complexity और data size और processing पर उनके प्रभाव के प्रति सावधान रहें।

## Example Usage

यहाँ बताया गया है कि आप survey में geoshape question का उपयोग कैसे कर सकते हैं:

| type     | name           | label                                      | hint                                        |
|----------|----------------|--------------------------------------------|--------------------------------------------|
| geoshape | forest_area    | Forest patch की boundary outline करें       | एक closed shape बनाने के लिए कम से कम 3 points का उपयोग करें |

## rtSurvey Extensions

Basic XLSForm specification के अतिरिक्त, rtSurvey अतिरिक्त सुविधाएं या customizations प्रदान कर सकता है:

1. Remote areas के लिए offline maps के साथ integration
2. Shape के लिए minimum और maximum number of points set करने के विकल्प
3. Initial drawing के बाद shapes edit या refine करने की ability
4. Free-form polygons के अतिरिक्त different shape types (जैसे rectangles, circles) का समर्थन

## Data Format

Geoshape data आमतौर पर space-separated coordinate pairs की string के रूप में store होती है:

```
(lat1 lon1; lat2 lon2; lat3 lon3; ... latN lonN)
```

उदाहरण के लिए:
```
(38.253094215699576 21.756382658677467; 38.25021274773806 21.756382658677467; 38.25007793942195 21.763892843919166; 38.25290886154963 21.763935759263404; 38.253094215699576 21.756382658677467)
```

## Analysis के लिए विचार

Geoshape questions का उपयोग करते समय, विचार करें:

1. Geographic data कैसे visualize और analyze होगा (जैसे GIS software)
2. Complex shapes की data cleaning या simplification की potential need
3. Detailed spatial data handle करने के लिए privacy और data protection measures
4. Comprehensive analysis के लिए अन्य spatial data sources के साथ integration

## सीमाएं

- Small mobile screens पर accurate shapes draw करना challenging हो सकता है।
- Complex shapes के लिए significant storage और processing capacity की आवश्यकता हो सकती है।
- Geoshape questions सभी types के surveys या उत्तरदाताओं के लिए suitable नहीं हो सकते।
- Detailed spatial data एकत्र करने से associated privacy concerns हो सकती हैं।
