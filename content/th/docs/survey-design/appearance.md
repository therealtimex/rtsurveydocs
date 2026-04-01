---
title: "Appearance"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

คอลัมน์ `appearance` ใน rtSurvey ช่วยให้คุณปรับแต่งการแสดงผลและพฤติกรรมของคำถามในแบบสำรวจ ฟีเจอร์นี้ช่วยเพิ่มประสบการณ์ผู้ใช้และสามารถปรับปรุงประสิทธิภาพการเก็บข้อมูลได้อย่างมีนัยสำคัญ rtSurvey รองรับแอตทริบิวต์ appearance มาตรฐานของ XLSForm และขยายด้วยตัวเลือกเพิ่มเติม

## แอตทริบิวต์ Appearance มาตรฐานของ XLSForm

rtSurvey รองรับแอตทริบิวต์ appearance มาตรฐานของ XLSForm ต่อไปนี้:

| Appearance Attribute | Question Types | คำอธิบาย |
|----------------------|----------------|-------------|
| multiline | text | สร้างกล่องข้อความหลายบรรทัด (เหมาะสำหรับ web clients) |
| minimal | select_one, select_multiple | แสดงตัวเลือกในเมนูแบบเลื่อนลง |
| quick | select_one | เลื่อนไปคำถามถัดไปโดยอัตโนมัติหลังเลือก (มือถือเท่านั้น) |
| no-calendar | date | ระงับการแสดงปฏิทิน (มือถือเท่านั้น) |
| month-year | date | อนุญาตให้เลือกเดือนและปีเท่านั้น |
| year | date | อนุญาตให้เลือกปีเท่านั้น |
| horizontal-compact | select_one, select_multiple | แสดงตัวเลือกแนวนอน (เว็บเท่านั้น) |
| horizontal | select_one, select_multiple | แสดงตัวเลือกแนวนอนในคอลัมน์ (เว็บเท่านั้น) |
| likert | select_one | นำเสนอตัวเลือกเป็นมาตราวัด Likert |
| compact | select_one, select_multiple | แสดงตัวเลือกเคียงกันกับ padding ต่ำสุด |
| quickcompact | select_one | รวมการแสดงผลแบบ compact กับการเลื่อนอัตโนมัติ (มือถือเท่านั้น) |
| field-list | groups | แสดงทั้งกลุ่มในหน้าจอเดียว (มือถือเท่านั้น) |
| label | select_one, select_multiple | แสดงป้ายกำกับตัวเลือกโดยไม่มีอินพุต |
| list-nolabel | select_one, select_multiple | แสดงอินพุตโดยไม่มีป้ายกำกับ (ใช้กับ `label`) |
| table-list | groups | แสดงคำถามในรูปแบบตาราง |
| signature | image | เปิดใช้งานการจับลายเซ็น (มือถือเท่านั้น) |
| draw | image | อนุญาตการวาดอิสระ (มือถือเท่านั้น) |
| map, quick map | select_one, select_one_from_file | เปิดใช้งานการเลือกจากคุณลักษณะแผนที่ |

## แนวทางปฏิบัติที่ดีที่สุดในการใช้ Appearance

1. **ความสม่ำเสมอ**: ใช้แอตทริบิวต์ appearance อย่างสม่ำเสมอในแบบสำรวจของคุณ
2. **มือถือกับเว็บ**: พิจารณาว่า appearance จะแสดงบนอุปกรณ์และแพลตฟอร์มต่างๆ อย่างไร
3. **ประสิทธิภาพ**: ระวังแอตทริบิวต์ appearance ที่อาจทำให้การโหลดแบบฟอร์มช้าลง
4. **ประสบการณ์ผู้ใช้**: เลือก appearance ที่ทำให้การป้อนข้อมูลง่ายและใช้งานง่ายยิ่งขึ้น
5. **การทดสอบ**: ทดสอบแบบฟอร์มของคุณบนอุปกรณ์เป้าหมายเสมอ

## แอตทริบิวต์ Appearance ขยายของ rtSurvey

นอกจาก appearance มาตรฐานของ XLSForm แล้ว rtSurvey ยังรองรับตัวเลือกเฉพาะแพลตฟอร์มต่อไปนี้:

### การควบคุมข้อมูลและการแสดงผล

| Appearance Attribute | Question Types | คำอธิบาย |
|----------------------|----------------|-------------|
| `invisible` | any | ซ่อนฟิลด์จากการมองเห็นขณะยังคงรวบรวมหรือคำนวณค่า |
| `displaytitle` | any | บังคับแสดงป้ายกำกับ/ชื่อของฟิลด์แม้ว่าจะถูกระงับ |
| `autopull` | select_one, select_multiple | ดึงข้อมูลภายนอกโดยอัตโนมัติเพื่อเติมตัวเลือก |
| `floating_hint` | text, integer, decimal | แสดงข้อความ hint เป็นป้ายกำกับลอยอยู่เหนือฟิลด์อินพุต |
| `calculate-button` | calculate | เพิ่มปุ่มที่มองเห็นได้ที่ทริกเกอร์การคำนวณใหม่ตามต้องการ |

### เลย์เอาต์

| Appearance Attribute | Question Types | คำอธิบาย |
|----------------------|----------------|-------------|
| `1screen` | group | บังคับให้ทั้งกลุ่มแสดงในหน้าจอเดียว |
| `columns(n)` | select_one, select_multiple | แสดงตัวเลือกใน `n` คอลัมน์ |
| `gridformat<row=R col=C colspan=S align=center>` | any | วางฟิลด์ในเลย์เอาต์ CSS-grid |
| `ignore-simplify` | any | สั่งให้ renderer ข้ามการลดความซับซ้อนอัตโนมัติ |

### วิดเจ็ต

| Appearance Attribute | Question Types | คำอธิบาย |
|----------------------|----------------|-------------|
| `likert` | select_one | นำเสนอตัวเลือกเป็นแถว Likert scale |
| `distress` | select_one | เรนเดอร์ตัวเลือกเป็น Kessler Psychological Distress Scale (K10) |

### การผสานรวม API

| Appearance Attribute | Question Types | คำอธิบาย |
|----------------------|----------------|-------------|
| `callapi` | text, integer, decimal, select_one | เปิดใช้งานการผสานรวม API call สำหรับฟิลด์นี้ |
| `callapi-verify(params)` | text, integer, decimal | ทริกเกอร์ API verification call โดยใช้พารามิเตอร์คงที่ |
| `callapi-verify(dynamicParams)` | text, integer, decimal | เช่นเดียวกับ `callapi-verify` แต่ใช้พารามิเตอร์จากฟิลด์อื่น |

## ข้อจำกัดที่ทราบ

- appearance ที่ซับซ้อนอาจไม่เรนเดอร์เหมือนกันในทุกแพลตฟอร์ม
- appearance ขั้นสูงบางอย่างของ rtSurvey อาจไม่รองรับในโหมดออฟไลน์

## การแก้ไขปัญหา Appearance

1. **Appearance ไม่ถูกใช้งาน**: ตรวจสอบการพิมพ์ผิดในคอลัมน์ appearance
2. **การเรนเดอร์ไม่สม่ำเสมอ**: ตรวจสอบความเข้ากันได้กับประเภทคำถามและแพลตฟอร์ม
3. **ปัญหาประสิทธิภาพ**: พิจารณาลดความซับซ้อนของ appearance ที่ซับซ้อน