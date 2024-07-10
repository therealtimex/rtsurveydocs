---
title: "Audio"
description: "Audio questions allow respondents to record and submit audio files as part of the survey."
icon: "mic"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 228
---

The audio question type in XLSForms and rtSurvey enables respondents to record and submit audio files as part of their survey responses. This feature is particularly useful for capturing verbal responses, testimonials, or environmental sounds relevant to the survey.

## Basic XLSForm Specification

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| audio | voice_note  | Please record your comments    |

For more details on the basic audio question type, see the [XLSForm specification](https://xlsform.org/en/#question-types).

## Uses

Audio questions are commonly used for:

1. Capturing verbal responses to open-ended questions
2. Recording testimonials or personal stories
3. Documenting environmental sounds or noise levels
4. Collecting voice samples for research purposes
5. Allowing respondents to provide detailed explanations

## Best Practices

1. Provide clear instructions on what to record and for how long.
2. Consider privacy implications and inform respondents about how their audio will be used.
3. Be mindful of file sizes and storage limitations, especially for surveys in areas with limited internet connectivity.
4. Test the audio recording feature on various devices to ensure compatibility.

## Example Usage

Here's an example of how you might use an audio question in a survey:

| type  | name           | label                                                | hint                                    |
|-------|----------------|------------------------------------------------------|----------------------------------------|
| audio | feedback_audio | Please record your feedback about the product        | Speak clearly for up to 60 seconds     |

## rtSurvey Extensions

While the basic XLSForm specification for audio questions is straightforward, rtSurvey may offer additional features or customizations:

1. Maximum recording duration setting
2. Audio quality options (e.g., low, medium, high)
3. Playback functionality for review before submission
4. Integration with device's native audio recording app

(Note: The specific extensions available in rtSurvey for audio questions would need to be confirmed and detailed here.)

## Limitations

- Audio files can be large, which may impact data transfer and storage.
- Not all devices may support audio recording capabilities.
- Transcription of audio responses may be necessary for analysis, which can be time-consuming.
- Privacy concerns may arise with the collection of voice data.

## Data Handling

Audio files collected through this question type are typically:

1. Saved in a common audio format (e.g., MP3, WAV)
2. Stored alongside other survey data
3. Accessible for playback and analysis through the survey management platform

## Considerations for Analysis

When using audio questions, consider:

1. How the audio data will be analyzed (e.g., manual transcription, automated speech-to-text)
2. The additional time and resources needed for processing audio responses
3. Privacy and data protection measures for storing and handling voice recordings

