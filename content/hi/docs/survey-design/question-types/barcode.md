---
title: "Barcode"
description: "Barcode questions आपके survey में barcode data को scan और capture करने की अनुमति देते हैं।"
icon: "qr_code_scanner"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 231
---

XLSForms और rtSurvey में barcode question type users को survey के भीतर directly barcode data scan और capture करने की अनुमति देता है। यह सुविधा inventory management, product tracking, या किसी भी scenario के लिए विशेष रूप से उपयोगी है जहाँ coded information की quick और accurate data entry की आवश्यकता होती है।

## Basic XLSForm Specification

| type    | name          | label                   |
|---------|---------------|-------------------------|
| barcode | product_code  | Product barcode scan करें |

Basic barcode question type के बारे में अधिक जानकारी के लिए, [XLSForm specification](https://xlsform.org/en/#question-types) देखें।

## उपयोग

Barcode questions सामान्यतः इनके लिए उपयोग किए जाते हैं:

1. Inventory surveys में product identification
2. Field operations में asset tracking
3. Events पर ticket या ID verification
4. Coded information के लिए quick data entry

## rtSurvey Extensions

Basic XLSForm specification के अतिरिक्त, rtSurvey अतिरिक्त सुविधाएं या customizations प्रदान कर सकता है:

1. Multiple barcode formats का समर्थन (जैसे QR codes, UPC, EAN)
2. Barcode scanning के लिए device camera के साथ integration
3. यदि barcode damaged हो या scan नहीं किया जा सकता तो manual entry विकल्प

## Best Practices

1. Accurate barcode scanning के लिए proper lighting conditions सुनिश्चित करें।
2. Scanning के लिए device को position करने के तरीके पर users को clear instructions प्रदान करें।
3. Scanning difficulties के मामले में एक fallback के रूप में manual entry विकल्प शामिल करें।
4. Survey deploy करने से पहले विभिन्न devices और barcode types के साथ barcode scanning feature का परीक्षण करें।

## सीमाएं

- Barcode scanning accuracy device की camera quality और environmental conditions के आधार पर vary कर सकती है।
- कुछ पुराने या low-end devices barcode scanning का समर्थन नहीं कर सकते।
- Implementation के आधार पर कुछ barcode types supported नहीं हो सकते।

## Example Usage

यहाँ बताया गया है कि आप inventory survey में barcode question का उपयोग कैसे कर सकते हैं:

| type    | name          | label                   | hint                                      |
|---------|---------------|-------------------------|-------------------------------------------|
| barcode | product_code  | Product barcode scan करें | Barcode को frame के भीतर position करें   |
| integer | quantity      | Product quantity दर्ज करें |                                           |
| note    | confirmation  | Product scan किया: ${product_code}। Quantity: ${quantity} |           |

इस उदाहरण में, survey एक product का barcode capture करती है, quantity पूछती है, और फिर scanned information के साथ एक confirmation note प्रदर्शित करती है।
