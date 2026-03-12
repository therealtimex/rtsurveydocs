---
title: "Video"
description: "Video questions allow respondents to record and submit video files as part of the survey."
icon: "videocam"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 229
---

The video question type in XLSForms and rtSurvey enables respondents to record and submit video files as part of their survey responses. This feature is particularly useful for capturing visual evidence, demonstrations, or testimonials relevant to the survey.

## Basic XLSForm Specification

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| video | demo_video  | Please record a short demo video |

For more details on the basic video question type, see the [XLSForm specification](https://xlsform.org/en/#question-types).

## Uses

Video questions are commonly used for:

1. Capturing visual evidence in field surveys
2. Recording product demonstrations or usage scenarios
3. Collecting video testimonials
4. Documenting processes or procedures
5. Allowing respondents to provide detailed visual explanations

## Best Practices

1. Provide clear instructions on what to record and for how long.
2. Consider privacy implications and inform respondents about how their video will be used.
3. Be mindful of file sizes and storage limitations, especially for surveys in areas with limited internet connectivity.
4. Test the video recording feature on various devices to ensure compatibility.
5. Consider specifying desired video quality or resolution in the instructions.

## Example Usage

Here's an example of how you might use a video question in a survey:

| type  | name           | label                                                | hint                                    |
|-------|----------------|------------------------------------------------------|----------------------------------------|
| video | product_demo   | Please record a short demo of using the product      | Record for 30-60 seconds, showing key features |

## rtSurvey Extensions

While the basic XLSForm specification for video questions is straightforward, rtSurvey may offer additional features or customizations:

1. Maximum recording duration setting
2. Video quality options (e.g., low, medium, high)
3. Playback functionality for review before submission
4. Integration with device's native video recording app
5. Option to upload existing video files instead of recording new ones

(Note: The specific extensions available in rtSurvey for video questions would need to be confirmed and detailed here.)

## Limitations

- Video files can be very large, which may significantly impact data transfer and storage.
- Not all devices may support video recording capabilities or may have limited storage.
- Analyzing video responses can be time-consuming and may require specialized software.
- Privacy concerns may be more pronounced with video data collection.

## Data Handling

Video files collected through this question type are typically:

1. Saved in a common video format (e.g., MP4, MOV)
2. Stored alongside other survey data, often in a separate media folder
3. Accessible for playback and analysis through the survey management platform

## Considerations for Analysis

When using video questions, consider:

1. How the video data will be analyzed (e.g., manual review, automated video analysis)
2. The additional time and resources needed for processing video responses
3. Privacy and data protection measures for storing and handling video recordings
4. Potential need for video editing or compilation tools in the analysis phase

