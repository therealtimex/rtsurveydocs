---
weight: 150
date: "2023-05-03T22:37:22+01:00"
draft: false
author: "RealTimeX"
title: "ការប្រមូលទិន្នន័យ"
icon: "rocket_launch"
toc: true
description: "មគ្គុទ្ទេសក៍ quickstart ដើម្បី run ការស្ទង់មតិជាមួយ rtSurvey"
publishdate: "2023-05-03T22:37:22+01:00"
tags: ["Beginners"]
---

នៅពេល form ត្រូវបាន deploy ហើយ enumerators ត្រូវបានកំណត់ ការប្រមូលទិន្នន័យអាចចាប់ផ្ដើម។ **rtSurvey** គាំទ្រការ gathering ទិន្នន័យ seamless ទាំងក្នុង web browsers និង dedicated mobile applications ដោយ ទ្ទួលបានភាពបត់បែន មិនថា team ភ្ជាប់ internet ឬ ធ្វើការក្នុង remote, offline environments ។

## ការជ្រើសរើស Collection Method ត្រឹមត្រូវ

អាស្រ័យ geography នៃ project ហើយ connectivity, អ្នកអាចជ្រើស method ល្អប្រសើរ សម្រាប់ enumerators:

- **Web Browser (Online):** ល្អបំផុតសម្រាប់ call centers, office-based data entry, ឬ respondents fill out self-administered public surveys ។
- **rtWork / rtSurvey Mobile App (Online & Offline):** ល្អបំផុតសម្រាប់ field operations, remote areas ជាមួយ internet unstable, ហើយ surveys ដែលត្រូវការ media attachments (photos, GPS coordinates, offline maps) ។

---

## Method 1: ការប្រមូលទិន្នន័យតាម Web Browser

ការប្រើ Webform interface ឱ្យ enumerators ចាប់ផ្ដើម collect data ភ្លាមៗ ដោយ install software ។

### 1. ការ Access Webform URL
ពី **Manage Forms** dashboard ក្នុង Control Panel, locate target form ហើយ click button **Webform's URL** ដើម្បី generate secure link ។

### 2. Form Entry
- Open URL ដែលបានផ្ដល់ ក្នុង modern web browser ណាមួយ ។
- ប្រសិនបើ form ត្រូវការ authentication, enumerator ត្រូវ log in ដោយ credentials ។ ប្រសិនបើ set ជា "Public Visibility" ពួកគេអាច proceed ដោយផ្ទាល់ ។
- Fill out survey questions ។ Interface នឹង automatically enforce logic, skip patterns, ហើយ validation rules ។
- **Media Capture:** ប្រសិនបើ form include image, audio, ឬ video questions web browser នឹង prompt upload file ពី computer ឬ ប្រើ webcam/microphone ។

### 3. Submission
នៅពេល reach final page, click **Submit**។ Browser ត្រូវការ active internet connection ដើម្បី finalize submission ។ ក្រោយ successful, ទិន្នន័យ reflect ភ្លាមៗ ក្នុង **Manage Submissions** interface ។

---

## Method 2: ការប្រមូលទិន្នន័យតាម Mobile App (Offline)

សម្រាប់ field data collection ដ៏ robust, mobile applications ផ្ដល់ offline capabilities ពេញ ។

### 1. Install ហើយ Authenticate
- Download application **rtWork** (ឬ **rtSurvey**) ពី Google Play Store ឬ Apple App Store ។
- Open app ហើយ log in ដោយ assigned enumerator credentials ។

### 2. Download Forms (ត្រូវការ Internet)
- Navigate ទៅ section **Forms** ឬ **Tasks** ក្នុង app ។
- Tap icon **Sync** ឬ **Download** ដើម្បី fetch questionnaire designs ចុងក្រោយ ពី server ។ ក្រោយ download, forms ត្រូវ store locally ក្នុង device ។

### 3. ប្រមូលទិន្នន័យ (Offline)
- Open downloaded form ហើយ ចាប់ផ្ដើម interview ។
- អ្នកអាច collect data offline ទាំងស្រុង ។
- **Media Capture:** Mobile app integrates ជា native ជាមួយ hardware device ។ អ្នកអាច capture photos, record audio, record video, ហើយ log precise GPS coordinates ដោយផ្ទាល់ ក្នុង app, ហួស internet connection ។
- ពេល finish interview, finalize record ។ Finalized records ត្រូវ queue safely ក្នុង outbox app ។

### 4. Sync Submissions (ត្រូវការ Internet)
- ពេល enumerator return ទៅ area ជាមួយ internet access (Wi-Fi ឬ cellular data), ពួកគេ ត្រូវ navigate ទៅ **Outbox** ឬ **Sync** interface ។
- Instruct app ដើម្បីផ្ញើ finalized forms ។ App នឹង transmit queued records ហើយ attached media files ទាំងអស់ securely ទៅ server ហើយ ក្រោយ submit ពួកវានឹង appear ក្នុង data grid សម្រាប់ review ។
