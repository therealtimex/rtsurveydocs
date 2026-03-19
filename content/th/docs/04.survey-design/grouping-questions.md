---
title: "การจัดกลุ่มคำถาม"
description: ""
icon: "auto_awesome"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 250
---

กลุ่มใน XLSForm ช่วยให้คุณจัดระเบียบคำถามที่เกี่ยวข้องเข้าด้วยกัน ปรับปรุงโครงสร้างของแบบสำรวจและเพิ่มความสามารถในการวิเคราะห์ข้อมูล rtSurvey รองรับกลุ่ม XLSForm อย่างเต็มที่และขยายฟังก์ชันด้วยคุณสมบัติเพิ่มเติม

## โครงสร้างกลุ่มพื้นฐาน

ในการสร้างกลุ่มคำถาม ให้ใช้ไวยากรณ์ `begin_group` และ `end_group`:

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | respondent | Respondent Information                   |
| text         | name       | Enter the respondent's name              |
| text         | position   | Enter the respondent's position          |
| end_group    |            |                                          |
```

## Appearance ของกลุ่ม

rtSurvey รองรับตัวเลือก appearance ต่างๆ สำหรับกลุ่ม:

1. **field-list**: แสดงคำถามหลายข้อบนหน้าจอเดียวกัน
2. **grid**: สร้างเลย์เอาต์แบบตารางที่กะทัดรัด (เฉพาะ rtSurvey)
3. **collapsible**: สร้างกลุ่มที่ขยาย/ยุบได้ (เฉพาะ rtSurvey)

## กลุ่มที่ซ้อนกัน

กลุ่มสามารถซ้อนกันภายในกลุ่มอื่นสำหรับโครงสร้างที่ซับซ้อนมากขึ้น:

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | hospital   | Hospital Information                     |
| text         | hosp_name  | What is the name of this hospital?       |
| begin_group  | medication | Medication Availability                  |
| select_one y_n| hiv_meds  | Does this hospital have HIV medication?  |
| end_group    |            |                                          |
| end_group    |            |                                          |
```

## Skip Logic สำหรับกลุ่ม

ใช้คอลัมน์ `relevant` เพื่อใช้งาน skip logic สำหรับทั้งกลุ่ม:

```
| type         | name   | label                                        | relevant        |
|--------------|--------|----------------------------------------------|-----------------|
| integer      | age    | How old are you?                             |                 |
| begin_group  | child  | Child                                        | ${age} <= 5     |
| integer      | muac   | Record child's mid-upper arm circumference   |                 |
| select_one y_n| mrdt  | Is the child's rapid diagnostic test positive?|                |
| end_group    |        |                                              |                 |
```

## แนวทางปฏิบัติที่ดีที่สุดสำหรับการใช้กลุ่ม

1. ใช้ชื่อที่มีความหมายสำหรับกลุ่มเพื่อปรับปรุงการวิเคราะห์ข้อมูล
2. รักษากลุ่มให้มุ่งเน้นที่คำถามที่เกี่ยวข้อง
3. ใช้กลุ่มที่ซ้อนกันอย่างรอบคอบ
4. ทดสอบ skip logic อย่างละเอียดเมื่อใช้ `relevant` กับกลุ่ม
5. พิจารณาใช้ appearance `field-list` สำหรับกลุ่มสั้นๆ
6. ใช้เลย์เอาต์ grid ของ rtSurvey สำหรับการแสดงข้อมูลที่เกี่ยวข้องแบบกะทัดรัด