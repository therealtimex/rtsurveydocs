---
title: "ส่วนขยายขั้นสูง"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 289
---

คอลัมน์ `appearance` ใน rtSurvey ช่วยให้คุณปรับแต่งการแสดงผลภาพและพฤติกรรมของคำถามในแบบสำรวจ ฟีเจอร์นี้ช่วยเพิ่มประสบการณ์ผู้ใช้และสามารถปรับปรุงประสิทธิภาพการเก็บข้อมูลได้อย่างมีนัยสำคัญ rtSurvey รองรับแอตทริบิวต์ appearance มาตรฐานของ XLSForm และขยายด้วยตัวเลือกเพิ่มเติม

## ส่วนขยาย Appearance เฉพาะของ rtSurvey

rtSurvey ขยายตัวเลือก appearance มาตรฐานด้วยสิ่งต่อไปนี้:

### การปรับแต่ง Time Input

สำหรับคำถามประเภท `text` ที่ใช้สำหรับอินพุตเวลา:

- `appearance:` - แสดงนาฬิกาสำหรับเลือกชั่วโมงและนาที
- `appearance: inline` - แสดงนาฬิกาเป็นไอคอน
- `appearance: inline-1line` - แสดงนาฬิกาในรูปแบบแถวเดียว
- `appearance: inline-[FORMAT]` - ปรับแต่งรูปแบบการแสดงเวลา (เช่น `[%H:%M]`, `[%h:%M:%S]`)

### การปรับแต่งสี

rtSurvey อนุญาตการปรับแต่งสีสำหรับ appearance ต่างๆ:

- `appearance: inline colors("0099FF")` - ปรับแต่งสีไอคอน
- `appearance: inline-1line colors("0000FF","FFFF00")` - ปรับแต่งสีในรูปแบบแถวเดียว

### Grid Layout

rtSurvey แนะนำ grid layout สำหรับการแสดงแบบกะทัดรัดคล้ายตาราง:

- `appearance: grid` - ใช้กับกลุ่มเพื่อสร้าง grid layout

### Collapsible Groups

- `appearance: collapsible` - สร้างกลุ่มที่ขยาย/ยุบได้