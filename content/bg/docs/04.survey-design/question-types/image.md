---
title: "Изображение"
description: "Въпросите от тип image позволяват на респондентите да заснемат и изпращат снимки като част от анкетата."
icon: "image"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 227
---

The image question type in XLSForms and rtSurvey enables respondents to capture and submit photos as part of their survey responses. This feature is particularly useful for collecting visual data, documenting observations, or providing evidence in field surveys.

## Basic XLSForm Specification

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| image | photo       | Take a photo of the location    |

For more details on the basic image question type, see the [XLSForm specification](https://xlsform.org/en/#question-types).

## Uses

Image questions are commonly used for:

1. Documenting field conditions or observations
2. Capturing visual evidence in research studies
3. Collecting before-and-after photos in impact assessments
4. Verifying the completion of tasks or presence at locations
5. Gathering visual data for remote analysis

## Best Practices

1. Provide clear instructions on what should be photographed.
2. Consider privacy implications and inform respondents about how their photos will be used.
3. Be mindful of file sizes and storage limitations, especially for surveys in areas with limited internet connectivity.
4. Ensure the device has sufficient storage space and camera permissions are granted.

## Example Usage

Here's an example of how you might use an image question in a survey:

| type  | name           | label                                      | hint                                        |
|-------|----------------|--------------------------------------------|--------------------------------------------|
| image | storefront     | Take a photo of the store's entrance       | Ensure the store name is clearly visible    |

## rtSurvey Extensions

While the basic XLSForm specification for image questions is straightforward, rtSurvey may offer additional features or customizations:

1. Image quality settings (e.g., low, medium, high resolution)
2. Option to add captions or tags to images
3. Multiple image capture for a single question
4. Integration with device's native camera app or gallery

(Note: The specific extensions available in rtSurvey for image questions would need to be confirmed and detailed here.)

## Data Handling

Images collected through this question type are typically:

1. Saved in a common image format (e.g., JPG, PNG)
2. Stored alongside other survey data, often in a separate media folder
3. Accessible for viewing and analysis through the survey management platform

## Considerations for Analysis

When using image questions, consider:

1. How the images will be analyzed (e.g., manual review, automated image analysis)
2. The additional storage space required for image files
3. Privacy and data protection measures for storing and handling photos
4. Potential need for image editing or organization tools in the analysis phase

## Limitations

- Image files can be large, which may impact data transfer and storage.
- Not all devices may have high-quality cameras or sufficient storage space.
- Analyzing large numbers of images can be time-consuming.
- There may be privacy concerns when capturing images, especially in public spaces.

