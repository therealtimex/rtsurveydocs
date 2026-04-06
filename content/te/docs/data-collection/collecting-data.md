---
weight: 150
date: "2023-05-03T22:37:22+01:00"
draft: false
author: "RealTimeX"
title: "డేటా సేకరించడం"
icon: "rocket_launch"
toc: true
description: "rtSurvey తో survey నడపడానికి quickstart గైడ్"
publishdate: "2023-05-03T22:37:22+01:00"
tags: ["Beginners"]
---

Form deploy చేయబడి enumerators assign చేయబడిన తర్వాత, డేటా సేకరణ ప్రారంభించవచ్చు. **rtSurvey** web browsers మరియు dedicated mobile applications రెండింటిలో seamless data gathering కు మద్దతు ఇస్తుంది, మీ team internet కు connected అయి ఉన్నా లేదా remote, offline environments లో పని చేస్తున్నా flexibility నిర్ధారిస్తుంది.

## సరైన సేకరణ పద్ధతి ఎంచుకోవడం

మీ project యొక్క geography మరియు connectivity ని బట్టి, మీ enumerators కు optimal పద్ధతి ఎంచుకోవచ్చు:

- **Web Browser (Online):** Call centers, office-based data entry, లేదా respondents self-administered public surveys fill చేసే సందర్భాలకు అనుకూలం.
- **rtWork / rtSurvey Mobile App (Online & Offline):** Field operations, unstable internet ఉన్న remote areas, మరియు media attachments (photos, GPS coordinates, offline maps) అవసరమైన surveys కు అనుకూలం.

---

## పద్ధతి 1: Web Browser ద్వారా డేటా సేకరించడం

Webform interface ఉపయోగించి enumerators ఏ software install చేయకుండా వెంటనే data collection ప్రారంభించవచ్చు.

### 1. Webform URL యాక్సెస్ చేయండి
Control Panel లోని **Manage Forms** dashboard నుండి, మీ target form locate చేసి secure link generate చేయడానికి **Webform's URL** button క్లిక్ చేయండి.

### 2. Form Entry
- అందించిన URL ఏ modern web browser లో తెరవండి.
- Form authentication అవసరమైతే, enumerator వారి credentials ఉపయోగించి login చేయాలి. "Public Visibility" గా set చేయబడి ఉంటే, నేరుగా proceed చేయవచ్చు.
- Survey questions fill out చేయండి. Interface స్వయంచాలకంగా logic, skip patterns, మరియు validation rules enforce చేస్తుంది.
- **Media Capture:** Form లో image, audio, లేదా video questions ఉంటే, web browser మీ computer నుండి file upload చేయమని లేదా అందుబాటులో ఉంటే మీ device webcam/microphone ఉపయోగించమని prompt చేస్తుంది.

### 3. Submission
Final page కు చేరుకున్నప్పుడు, **Submit** క్లిక్ చేయండి. Browser submission finalize చేయడానికి active internet connection అవసరం. సఫలమైన తర్వాత, డేటా **Manage Submissions** interface లో వెంటనే reflect అవుతుంది.

---

## పద్ధతి 2: Mobile App ద్వారా డేటా సేకరించడం (Offline)

బలమైన field data collection కోసం, mobile applications పూర్తి offline capabilities అందిస్తాయి.

### 1. Install మరియు Authenticate చేయండి
- Google Play Store లేదా Apple App Store నుండి **rtWork** (లేదా **rtSurvey**) application download చేయండి.
- App తెరిచి assigned enumerator credentials ఉపయోగించి login చేయండి.

### 2. Forms Download చేయండి (Internet అవసరం)
- App లో **Forms** లేదా **Tasks** section కు navigate చేయండి.
- Server నుండి latest questionnaire designs fetch చేయడానికి **Sync** లేదా **Download** icon tap చేయండి. Download అయిన తర్వాత, forms device పై locally store చేయబడతాయి.

### 3. డేటా సేకరించండి (Offline)
- Downloaded form తెరిచి interview ప్రారంభించండి.
- పూర్తిగా offline గా data safely సేకరించవచ్చు.
- **Media Capture:** Mobile app మీ device hardware తో natively integrate అవుతుంది. Internet connection లేకుండా కూడా నేరుగా app లో photos capture చేయవచ్చు, audio record చేయవచ్చు, video record చేయవచ్చు, మరియు precise GPS coordinates log చేయవచ్చు.
- Interview finish అయినప్పుడు, record finalize చేయండి. Finalized records app యొక్క outbox లో safely queue చేయబడతాయి.

### 4. Submissions Sync చేయండి (Internet అవసరం)
- Enumerator internet access (Wi-Fi లేదా cellular data) ఉన్న ప్రాంతానికి తిరిగి వచ్చిన తర్వాత, **Outbox** లేదా **Sync** interface కు navigate చేయాలి.
- Finalized forms పంపించమని app ని instruct చేయండి. App queued records మరియు attached media files అన్నింటినీ securely server కు transmit చేస్తుంది, ఆ తర్వాత అవి review కు data grid లో కనిపిస్తాయి.
