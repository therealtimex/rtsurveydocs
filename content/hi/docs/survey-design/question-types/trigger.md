---
title: "Trigger / Acknowledge"
description: "Trigger questions एक statement प्रदर्शित करते हैं जिसे गणनाकर्ता को जारी रखने से पहले स्पष्ट रूप से acknowledge करना होता है।"
icon: "check-circle"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 240
---

`trigger` (जिसे `acknowledge` भी कहा जाता है) question type एक **checkbox के साथ एक statement** प्रदर्शित करता है। गणनाकर्ता को confirm करने के लिए checkbox tick करना होता है कि उन्होंने form को आगे बढ़ने से पहले statement पढ़ और समझ लिया है। कोई data value store नहीं होती — केवल यह कि checkbox tick किया गया था।

## Basic XLSForm Specification

| type | name | label |
|------|------|-------|
| trigger | consent_ack | उत्तरदाता ने verbal informed consent प्रदान किया है। |

या `acknowledge` alias का उपयोग करके:

| type | name | label |
|------|------|-------|
| acknowledge | consent_ack | उत्तरदाता ने verbal informed consent प्रदान किया है। |

`trigger` और `acknowledge` दोनों equivalent हैं — जो भी आपके platform द्वारा documented हो उसका उपयोग करें।

## उपयोग

Trigger/acknowledge questions सामान्यतः इनके लिए उपयोग किए जाते हैं:

1. **Informed consent** — sensitive data record करने से पहले confirm करें कि गणनाकर्ता ने consent प्राप्त की
2. **Soft alerts** — असामान्य value के बारे में warn करें और आगे बढ़ने से पहले explicit confirmation की आवश्यकता करें
3. **Checklist items** — confirm करें कि एक physical observation complete हुई (जैसे "मैंने water source को directly observe किया है")
4. **Instructions** — गणनाकर्ता को जारी रखने से पहले एक section-level instruction acknowledge करने के लिए force करें
5. **Quality checks** — outlier values flag करें और गणनाकर्ता को उन्हें verify करने की आवश्यकता करें

## Example Usage

### Consent acknowledgement

| type | name | label | required |
|------|------|-------|----------|
| trigger | consent | उत्तरदाता ने इस survey में भाग लेने के लिए verbal informed consent दी है। | yes |

### Outlier values के लिए Soft alert

Suspicious value दर्ज होने पर ही trigger दिखाने के लिए `relevant` expression के साथ combined:

| type | name | label | relevant | required |
|------|------|-------|----------|----------|
| integer | children | बच्चों की संख्या | | |
| trigger | children_confirm | आपने ${children} बच्चे दर्ज किए। कृपया उत्तरदाता के साथ verify करें और confirm करने के लिए OK tap करें। | `${children} > 10` | `${children} > 10` |

### Section start पर Instruction acknowledgement

| type | name | label |
|------|------|-------|
| trigger | section_b_ack | Section B: Agricultural Land Use। इस section के सभी प्रश्न केवल household head को पूछें। |

## Trigger को required बनाना

Box tick होने तक आगे बढ़ने से रोकने के लिए `required: yes` जोड़ें:

| type | name | label | required | required_message |
|------|------|-------|----------|------------------|
| trigger | safety_check | सभी safety equipment present और functional है। | yes | आगे बढ़ने से पहले आपको confirm करना होगा। |

## Conditional display

केवल तभी trigger दिखाएं जब कोई condition पूरी हो:

| type | name | label | relevant |
|------|------|-------|----------|
| select_one yesno | has_well | क्या household में well है? | |
| trigger | well_observation | Confirm करें कि आपने well की condition को directly observe किया है। | `${has_well} = 'yes'` |

## `note` से अंतर

| | `note` | `trigger` |
|--|--------|-----------|
| Text प्रदर्शित करता है | हाँ | हाँ |
| Interaction की आवश्यकता है | नहीं | हाँ (tick करना होगा) |
| Data store करता है | नहीं | नहीं (केवल OK/ticked) |
| Progress block कर सकता है | नहीं | हाँ (`required` के साथ) |

## Best Practices

1. Trigger labels को concise और actionable रखें — गणनाकर्ता seconds में पढ़ और confirm कर सके।
2. जब acknowledgement mandatory हो तो हमेशा `required: yes` जोड़ें।
3. Consent और safety checks के लिए triggers का उपयोग करें जहाँ आपको audit trail की आवश्यकता हो।
4. Conditional soft alerts के लिए `relevant` के साथ combine करें ताकि trigger केवल तभी दिखे जब किसी value को verification की आवश्यकता हो।

## सीमाएं

- Trigger fields एक meaningful data value store नहीं करते — वे केवल यह record करते हैं कि box tick किया गया था।
- Trigger widget अधिकांश clients पर एक simple checkbox/button के रूप में render होता है; यह full e-signature नहीं है।
