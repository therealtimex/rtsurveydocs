---
title: "सर्वर से कनेक्ट करना"
description: "rtSurvey मोबाइल ऐप को अपने प्रोजेक्ट सर्वर से कनेक्ट करना, भूमिका-विशिष्ट कार्यात्मकताएं एक्सेस करना और कई परियोजनाओं में सर्वेक्षणों पर सहयोग शुरू करना सीखें।"
icon: "cloud_sync"
date: "2023-05-22T00:34:57+01:00"
lastmod: "2023-05-22T00:34:57+01:00"
draft: false
weight: 313
---

rtSurvey ऐप को एक सर्वर से कनेक्ट करना डेटा संग्रह, प्रबंधन और विश्लेषण के लिए ऐप का उपयोग शुरू करने का एक महत्वपूर्ण चरण है। यह प्रक्रिया सुनिश्चित करती है कि सभी सर्वेक्षण भूमिकाएं रियल-टाइम में आवश्यक कार्यात्मकताओं और डेटा तक पहुँच सकें।

## ODK Collect से मुख्य अंतर

rtSurvey विभिन्न सर्वेक्षण भूमिकाओं के लिए ODK Collect की तुलना में बेहतर कार्यात्मकताएं प्रदान करता है:
- **Administrator**: मैसेजिंग, अपडेट के लिए सूचनाएं (डेटा सबमिशन, नई रिपोर्ट, नए खाते), फ़ॉर्म भरना और विश्लेषण रिपोर्ट देखना।
- **Project Manager**: Administrators जैसी कार्यात्मकताएं, परियोजना सेटअप और प्रबंधन सहित।
- **Survey Designer**: मैसेजिंग, सूचनाएं, फ़ॉर्म भरना और विश्लेषण रिपोर्ट देखना।
- **Field Enumerator**: फ़ॉर्म भरना, मैसेजिंग, सूचनाएं और प्रगति रिपोर्ट।
- **Data Analyst**: मैसेजिंग, सूचनाएं और analytics रिपोर्ट तक पहुँच।

## rtSurvey ऐप को सर्वर से कनेक्ट करने के चरण

### 1. सुनिश्चित करें कि आपके पास एक खाता है

सर्वर से कनेक्ट करने के लिए, आपको एक खाते की आवश्यकता है। खाते Administrator द्वारा या Administrator द्वारा सेटअप किए गए खाता निर्माण URL का उपयोग करके स्टाफ द्वारा बनाए जा सकते हैं।

### 2. rtSurvey ऐप खोलें

अपने मोबाइल डिवाइस पर rtSurvey ऐप लॉन्च करें। यदि आपने इसे अभी तक इंस्टॉल नहीं किया है, तो [rtSurvey ऐप इंस्टॉल करना](#installing-rtsurvey-app) पेज देखें।

### 3. सर्वर कनेक्शन सेटिंग एक्सेस करें

1. ऐप खोलें और सेटिंग मेनू पर नेविगेट करें।
2. सर्वर से कनेक्ट करने का विकल्प चुनें।

### 4. खाता विवरण दर्ज करें और परियोजना चुनें

rtSurvey से कनेक्ट करते समय, प्रक्रिया आपके खाता कॉन्फ़िगरेशन के आधार पर सुव्यवस्थित होती है:

- **उपयोगकर्ता नाम**: अपना खाता उपयोगकर्ता नाम दर्ज करें।
- **पासवर्ड**: अपना खाता पासवर्ड दर्ज करें।

अपने क्रेडेंशियल दर्ज करने के बाद:

- यदि आपका खाता केवल एक सर्वेक्षण परियोजना से जुड़ा है:
  - ऐप स्वचालित रूप से उस परियोजना के सर्वर में आपको साइन इन करेगा।
  - आपको सर्वर URL दर्ज करने या मैन्युअल रूप से एक परियोजना चुनने की आवश्यकता नहीं है।

- यदि आपका खाता कई सर्वेक्षण परियोजनाओं से जुड़ा है:
  - सफल प्रमाणीकरण के बाद, आप उन परियोजनाओं की एक सूची देखेंगे जिन तक आपकी पहुँच है।
  - इस सूची से वह परियोजना चुनें जिस पर आप काम करना चाहते हैं।

### 5. प्रमाणित करें

सर्वर विवरण दर्ज करने के बाद, "Connect" या "Login" बटन पर टैप करें। ऐप आपके क्रेडेंशियल प्रमाणित करेगा और सर्वर से कनेक्शन स्थापित करेगा।

```mermaid
flowchart TD
    A["📱 Start rtSurvey App"] --> B["🔑 Enter Username<br>and Password"]
    style A fill:#4CAF50,stroke:#666666,stroke-width:3px,color:white
    style B fill:#2196F3,stroke:#666666,stroke-width:3px,color:white

    B --> C{"🌳 Multiple<br>projects?"}
    style C fill:#FFC107,stroke:#666666,stroke-width:3px,color:black

    C -->|Yes| D["📋 Display list<br>of projects"]
    C -->|No| E["🔄 Auto-connect to<br>single project"]
    style D fill:#FF9800,stroke:#666666,stroke-width:3px,color:white
    style E fill:#009688,stroke:#666666,stroke-width:3px,color:white

    D --> F["👆 User selects<br>a project"]
    style F fill:#FF5722,stroke:#666666,stroke-width:3px,color:white

    E --> G["☁️ Connect to server"]
    F --> G
    style G fill:#3F51B5,stroke:#666666,stroke-width:3px,color:white
    G --> H["👥 Access role-specific<br>functionalities"]
    style H fill:#9C27B0,stroke:#666666,stroke-width:3px,color:white

    H --> I["👨‍💼 Administrator/<br>Project Manager"]
    H --> J["🎨 Survey Designer"]
    H --> K["📝 Field Enumerator"]
    H --> L["📊 Data Analyst"]
    style I fill:#E91E63,stroke:#666666,stroke-width:3px,color:white
    style J fill:#795548,stroke:#666666,stroke-width:3px,color:white
    style K fill:#607D8B,stroke:#666666,stroke-width:3px,color:white
    style L fill:#8BC34A,stroke:#666666,stroke-width:3px,color:white

    I --> M["💬 Messaging<br>🔔 Notifications<br>📄 Form Filling<br>📈 Viewing Reports"]
    J --> N["💬 Messaging<br>🔔 Notifications<br>🧪 Form Testing<br>📈 Viewing Reports"]
    K --> O["📝 Form Filling<br>💬 Messaging<br>🔔 Notifications<br>📊 Progress Reports"]
    L --> P["💬 Messaging<br>🔔 Notifications<br>📊 Analytics Reports"]
    style M fill:#FF4081,stroke:#666666,stroke-width:3px,color:white
    style N fill:#9E9E9E,stroke:#666666,stroke-width:3px,color:white
    style O fill:#00BCD4,stroke:#666666,stroke-width:3px,color:white
    style P fill:#CDDC39,stroke:#666666,stroke-width:3px,color:white
```

## कनेक्शन समस्याओं का समाधान

यदि सर्वर से कनेक्ट करते समय समस्याएं आती हैं:

1. **इंटरनेट कनेक्शन जांचें**: सुनिश्चित करें कि आपका डिवाइस इंटरनेट से कनेक्ट है।
2. **क्रेडेंशियल की पुष्टि करें**: सुनिश्चित करें कि आपका उपयोगकर्ता नाम और पासवर्ड सही है।
3. **ऐप पुनः शुरू करें**: rtSurvey ऐप बंद करें और फिर से खोलें।
4. **समर्थन से संपर्क करें**: यदि समस्याएं बनी रहती हैं, तो सहायता के लिए अपने सिस्टम administrator या rtSurvey समर्थन से संपर्क करें।

## निष्कर्ष

rtSurvey ऐप को एक सर्वर से कनेक्ट करना एक सीधी प्रक्रिया है जो आपको ऐप की पूर्ण क्षमताओं का लाभ उठाने में सक्षम बनाती है। ऊपर बताए गए चरणों का पालन करके, आप अपनी विशिष्ट सर्वेक्षण भूमिका के अनुकूल डेटा संग्रह, प्रबंधन और विश्लेषण सुनिश्चित कर सकते हैं।
