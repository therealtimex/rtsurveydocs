---
title: "Media"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 286
---

rtSurvey surveys में rich media integration का समर्थन करता है, जिससे आप अपने questionnaires को images, audio, और video के साथ बेहतर बना सकते हैं। यह सुविधा उत्तरदाता अनुभव और एकत्र किए गए डेटा की गुणवत्ता में महत्वपूर्ण सुधार कर सकती है।

## समर्थित Media Types

rtSurvey निम्नलिखित media types का समर्थन करता है:
- Images (jpg, png, gif)
- Audio (mp3, wav)
- Video (mp4, webm)

## अपने Survey में Media जोड़ना

अपने rtSurvey form में media शामिल करने के लिए, अपने XLSForm में निम्नलिखित columns का उपयोग करें:

- `image`: Images प्रदर्शित करने के लिए
- `audio`: Audio files चलाने के लिए
- `video`: Video files चलाने के लिए

उदाहरण:

```
| type | name          | label         | image        | audio       | video       |
|------|---------------|---------------|--------------|-------------|-------------|
| note | media_example | Media example | example.jpg  | sound.mp3   | clip.mp4    |
```

## Media File Management

### Web-based surveys
Web-based surveys के लिए, rtSurvey एक media management interface प्रदान करता है जहाँ आप अपनी media files upload और organize कर सकते हैं। ये files फिर आपके surveys में उपयोग के लिए स्वचालित रूप से उपलब्ध हो जाती हैं।

### Mobile app
rtSurvey mobile app का उपयोग करते समय:
1. अपनी media files को अपने device पर `/rtSurvey/forms/[form-name]-media/` folder में रखें।
2. अपने XLSForm में exact file name का संदर्भ दें।

## rtSurvey-Specific Features

### Dynamic Media Loading
rtSurvey survey responses के आधार पर media की dynamic loading का समर्थन करता है:

```
| type         | name      | label              | image                    |
|--------------|-----------|--------------------|--------------------------| 
| select_one species | animal | एक जानवर चुनें | ${animal}.jpg            |
```

### Choice Options में Media
rtSurvey आपको select questions के choice options में media का उपयोग करने की अनुमति देता है:

```
| type                | name    | label           | media::image |
|---------------------|---------|-----------------|--------------|
| select_one_from_file animals | एक जानवर चुनें |              |
```

choices sheet में:
```
| list_name | name  | label | media::image |
|-----------|-------|-------|--------------|
| animals   | dog   | कुत्ता | dog.jpg      |
| animals   | cat   | बिल्ली | cat.jpg      |
```

### Media Capture
rtSurvey XLSForm को media capture capabilities के साथ विस्तारित करता है:

```
| type  | name        | label               |
|-------|-------------|---------------------|
| image | photo       | एक photo लें        |
| audio | voice_note  | एक voice note record करें |
| video | video_clip  | एक video record करें |
```

## Media के उपयोग के लिए Best Practices

1. **File sizes optimize करें**: बड़ी media files survey loading और submission को धीमा कर सकती हैं।
2. **उचित formats का उपयोग करें**: व्यापक रूप से समर्थित formats का उपयोग करें (images के लिए jpg, audio के लिए mp3, video के लिए mp4)।
3. **Alternatives प्रदान करें**: accessibility के लिए हमेशा text alternatives शामिल करें।
4. **पूरी तरह से परीक्षण करें**: सुनिश्चित करें कि media सभी target devices पर सही ढंग से प्रदर्शित हो।
5. **Offline उपयोग पर विचार करें**: ऐसे surveys के लिए जो offline conduct किए जा सकते हैं, सुनिश्चित करें कि सभी media locally उपलब्ध हो।

## Multilingual Media Support

rtSurvey language-specific media का समर्थन करता है। `::language` suffix का उपयोग करें:

```
| type | name  | label    | image::English | image::Spanish |
|------|-------|----------|----------------|----------------|
| note | intro | स्वागत है | welcome_en.jpg | welcome_es.jpg |
```

## Data Export में Media

rtSurvey से डेटा export करते समय:
- Web surveys के लिए, media URLs को export में शामिल किया जाता है।
- Mobile app surveys के लिए, file paths शामिल किए जाते हैं।

## Mobile App से संबंधित बातें

- Media-heavy surveys के लिए devices पर पर्याप्त storage space सुनिश्चित करें।
- rtSurvey mobile app offline media playback और capture का समर्थन करता है।
- बड़ी media files low-end devices पर app performance को प्रभावित कर सकती हैं।

## ज्ञात सीमाएं

- कुछ पुराने browsers सभी media formats का समर्थन नहीं कर सकते।
- बहुत बड़ी video files low-bandwidth situations में समस्याएं पैदा कर सकती हैं।

## Media संबंधी समस्याओं का समाधान

1. **Media प्रदर्शित नहीं हो रही**: सटीकता के लिए file paths और names की जांच करें।
2. **Playback संबंधी समस्याएं**: सुनिश्चित करें कि media format target devices द्वारा समर्थित है।
3. **Slow loading**: file sizes को optimize करने या media preloading पर विचार करें।

## Advanced Media Features

### Geotagging
rtSurvey surveys के दौरान capture किए गए media को स्वचालित रूप से geotag कर सकता है:

```
| type  | name        | label        | appearance |
|-------|-------------|--------------|------------|
| image | photo       | एक photo लें | geotag     |
```

### Media Annotations
उत्तरदाताओं को images annotate करने की अनुमति दें:

```
| type  | name        | label        | appearance |
|-------|-------------|--------------|------------|
| image | photo       | image को annotate करें | annotate |
```

अपने rtSurvey forms में media का प्रभावी उपयोग करके, आप अधिक engaging, informative, और सटीक surveys बना सकते हैं। media को शामिल करने के फायदों को performance considerations के साथ संतुलित करना याद रखें, विशेषकर ऐसे surveys के लिए जो सीमित internet connectivity या lower-end devices वाले क्षेत्रों में deploy किए जाते हैं।
