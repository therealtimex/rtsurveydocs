---
weight: 100
title: "शुरुआत करें"
date: "2023-05-03T22:37:22+01:00"
draft: false
author: "rtSurvey"
icon: "rocket_launch"
toc: true
description: "rtSurvey के साथ सर्वेक्षण चलाने के लिए एक त्वरित प्रारंभ मार्गदर्शिका"
publishdate: "2023-05-03T22:37:22+01:00"
---

rtSurvey आपको शक्तिशाली फ़ॉर्म और वर्कफ़्लो बनाने की सुविधा देता है, ताकि आप जहाँ भी हों वहाँ से डेटा संग्रह कर सकें। आप यह कर सकते हैं:

1.  शक्तिशाली फ़ॉर्म बनाएं जिनमें फ़ोटो, GPS स्थान, स्किप लॉजिक,
    गणनाएं, बाहरी डेटासेट, कई भाषाएं और बहुत कुछ शामिल हो।
2.  मोबाइल ऐप या वेब ऐप से ऑफलाइन डेटा संग्रह करें।
    इंटरनेट कनेक्शन मिलने पर फ़ॉर्म और सबमिशन स्वचालित रूप से सिंक हो जाते हैं।
3.  डेटा को CSV के रूप में डाउनलोड करके या rtSurvey को Excel, Power BI, Python या R से
    जोड़कर लाइव-अपडेट होने वाले डैशबोर्ड बनाएं और आसानी से विश्लेषण करें।

शोधकर्ता, फील्ड टीमें और अन्य पेशेवर लोग आपके जैसे ही rtSurvey का उपयोग
अपने महत्वपूर्ण डेटा संग्रह के लिए करते हैं। यहाँ बताया गया है कि कैसे शुरुआत करें।

## 1. rtSurvey Cloud प्राप्त करें {#getting-started-rtCloud}

rtSurvey Cloud प्राप्त करने का सबसे तेज़ और सरल तरीका आधिकारिक प्रबंधित होस्टिंग सेवा [rtSurvey
Cloud](https://rtSurvey.com/#rtSurvey-cloud) का उपयोग करना है। यह rtSurvey की वेबसाइट पर उपलब्ध है और तेज़, विश्वसनीय तथा सुरक्षित बुनियादी ढाँचे पर आधारित है।

## 2. rtCloud पर अपना XLSForm अपलोड करें या Form Builder (Beta) से फ़ॉर्म बनाएं {#getting-started-create-form}

1.  `XLSForm <xlsform>`{.interpreted-text
    role="doc"} का उपयोग करके फ़ॉर्म परिभाषा बनाएं या इस [All Widgets
    form](https://docs.google.com/spreadsheets/d/1af_Sl8A_L8_EULbhRLHVl8OclCfco09Hq2tqb9CslwQ/edit#gid=0) को आज़माएं।
2.  `rtCloud पर अपना XLSForm अपलोड करें <rtCloud-forms-upload>`{.interpreted-text
    role="ref"} और उसे प्रकाशित करें।

## 3. rtSurvey ऐप प्राप्त करें {#getting-started-get-collect}

rtSurvey ऐप डाउनलोड करने के लिए, अपने डिवाइस के आधार पर ये चरण अपनाएं:

### Android डिवाइस के लिए:
1. [Google Play Store](https://play.google.com/store/apps/details?id=vn.rta.rtsurvey) पर जाएं।
2. खोज बार में "rtSurvey" खोजें।
3. rtSurvey लोगो वाले ऐप पर टैप करें।
4. अपने Android डिवाइस पर ऐप डाउनलोड और इंस्टॉल करने के लिए "Install" बटन पर क्लिक करें।

### iOS डिवाइस के लिए:
1. अपने iOS डिवाइस पर [App Store](https://apps.apple.com/vn/app/rtsurvey/id1178851547) खोलें।
2. खोज टैब में "rtSurvey" खोजें।
3. rtSurvey लोगो वाले ऐप को ढूंढें।
4. अपने iOS डिवाइस पर ऐप डाउनलोड और इंस्टॉल करने के लिए "Get" बटन पर टैप करें।

ऐप डाउनलोड और इंस्टॉल होने के बाद, आप इसे लॉन्च कर सकते हैं और सर्वेक्षण तथा विश्लेषण सेवाओं के लिए rtSurvey का उपयोग शुरू कर सकते हैं।

## 4. Collect को rtCloud से जोड़ें {#getting-started-connect}

1.  rtCloud में `App User बनाएं <rtCloud-users-app-overview>`{.interpreted-text
    role="ref"} और
    `उस उपयोगकर्ता को आपका फ़ॉर्म असाइन करें <rtCloud-projects-form-access>`{.interpreted-text
    role="ref"}।
2.  Collect खोलें, `Configure with QR code`{.interpreted-text
    role="guilabel"} पर टैप करें और अपने App User के लिए बनाया गया कोड स्कैन करें।

## 5. Collect में अपना फ़ॉर्म भरें {#getting-started-fill-form}

1.  फ़ॉर्म भरने के लिए `Fill Blank Form`{.interpreted-text role="guilabel"} चुनें।
2.  समाप्त होने पर आपका फ़ॉर्म डेटा स्वचालित रूप से rtCloud को भेजा जाएगा।

## 6. rtCloud में अपने डेटा का उपयोग करें {#getting-started-use-data}

1.  rtCloud में लॉग इन करें और अपना डेटा देखें।
2.  अपने डेटा को CSV के रूप में डाउनलोड करें या
    `Power BI में विज़ुअलाइज़ करें <rtCloud-submissions-odata>`{.interpreted-text
    role="ref"}।
