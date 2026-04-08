---
title: "Image"
description: "คำถาม image ให้ผู้ตอบแบบสำรวจบันทึกและส่งภาพถ่ายเป็นส่วนหนึ่งของแบบสำรวจ"
icon: "image"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 227
---

ประเภทคำถาม image ใน XLSForms และ rtSurvey ให้ผู้ตอบแบบสำรวจบันทึกและส่งภาพถ่ายเป็นส่วนหนึ่งของคำตอบแบบสำรวจ ฟีเจอร์นี้มีประโยชน์โดยเฉพาะสำหรับการรวบรวมข้อมูลภาพ การบันทึกการสังเกต หรือการให้หลักฐานในการสำรวจภาคสนาม

## ส่วนขยาย image ของ rtSurvey

### watermark()

appearance `watermark()` จะวางลายน้ำข้อความทับบนรูปถ่ายที่ถ่ายด้วยฟิลด์นี้ ลายน้ำมักจะประกอบด้วยข้อมูลเมตาเช่นชื่อผู้เก็บข้อมูล วันที่/เวลา หรือพิกัด GPS ที่ประทับลงบนรูปภาพโดยตรงก่อนบันทึก

| type | name | label | appearance |
|------|------|-------|------------|
| image | site_photo | Take a photo of the site | `watermark("${enumerator_id} ${today()}")` |

อาร์กิวเมนต์ของ `watermark()` คือ expression XPath ที่ประเมิน ณ เวลาถ่ายภาพ สตริงผลลัพธ์จะแสดงเป็นข้อความลายน้ำ

### editable

appearance `editable` ช่วยให้ผู้ตอบแบบสำรวจสามารถใส่คำอธิบายหรือวาดบนรูปถ่ายที่ถ่ายได้ แถบเครื่องมือวาดภาพจะปรากฏเหนือรูปภาพ

| type | name | label | appearance |
|------|------|-------|------------|
| image | annotated_photo | Photograph and mark areas of concern | editable |

{{% alert icon=" " context="info" %}}
`editable` สามารถรวมกับ `watermark()` ได้: `appearance: editable watermark("${id}")`
{{% /alert %}}