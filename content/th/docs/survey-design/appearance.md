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
| `required-but-simplify` | any | ฟิลด์จำเป็นต้องกรอก แต่เลย์เอาต์ยังคงถูกย่อโดย renderer |
| `embed` | any | เรนเดอร์ฟิลด์ในโหมดแสดงผลแบบฝังตัว/อินไลน์ |
| `popup` | select_one, select_multiple | เรนเดอร์รายการตัวเลือกในป๊อปอัป/โมดัลแทนการแสดงในบรรทัด |
| `auto-hide-empty` | boxtag, select | ซ่อนวิดเจ็ตคำถามทั้งหมดเมื่อรายการตัวเลือกว่างเปล่า |
| `text-nolabel` | select_one, select_multiple | ซ่อนป้ายกำกับข้อความสำหรับแต่ละตัวเลือก แสดงเฉพาะตัวควบคุมอินพุต |

### วิดเจ็ต

| Appearance Attribute | Question Types | คำอธิบาย |
|----------------------|----------------|-------------|
| `likert` | select_one | นำเสนอตัวเลือกเป็นแถว Likert scale |
| `distress` | select_one | เรนเดอร์ตัวเลือกเป็น Kessler Psychological Distress Scale (K10) |

### วิดเจ็ตภาพสำหรับการเลือก

appearances เหล่านี้เปลี่ยนการแสดงผลทั้งหมดของรายการตัวเลือก

| Appearance Attribute | Question Types | คำอธิบาย |
|----------------------|----------------|-------------|
| `tagging` | select_one, select_multiple | ตัวเลือกแสดงเป็นชิปแท็กรูปเม็ดยาที่คลิกได้ |
| `boxtag` | select_one, select_multiple | ตัวเลือกแสดงเป็นกล่องสี่เหลี่ยมที่มีสไตล์ให้แตะ |
| `boxtag -search` | select_one, select_multiple | เลย์เอาต์ Boxtag พร้อมช่องค้นหา/กรองแบบ live เหนือกล่อง |
| `duolingo-style1` | select_one, select_multiple | เลย์เอาต์การ์ดขนาดใหญ่สไตล์ Duolingo — เหมาะสำหรับรายการสั้นที่มีไอคอน |
| `rating_box` | select_one, select_multiple | กริดของกล่องตัวเลขที่แตะได้ — เหมาะสำหรับคำถามแบบสเกลหรือ NPS |
| `star_rating` | select_one | ตัวเลือกแสดงเป็นดาว จำนวนดาวเท่ากับจำนวนตัวเลือก |
| `choices-noshow` | select_one, select_multiple | แสดง 10 ตัวเลือกแรกเริ่มต้นพร้อมตัวควบคุม "แสดงเพิ่มเติม" |
| `noshow` | select_one, select_multiple | ซ่อนรายการตัวเลือกทั้งหมด ค่าถูกกำหนดโดยโปรแกรมผ่าน `calculate` หรือ API |
| `checkall` | select_multiple | เพิ่มทางลัด "เลือกทั้งหมด" ที่ด้านบนของรายการตัวเลือก |
| `max-items(N)` | select_one, select_multiple | จำกัดรายการตัวเลือกที่มองเห็นเป็น N รายการ ตัวอย่าง: `max-items(5)` |

### วิดเจ็ตภาพสำหรับข้อความ

| Appearance Attribute | Question Types | คำอธิบาย |
|----------------------|----------------|-------------|
| `richtext` | text | แทนที่กล่องข้อความธรรมดาด้วย rich text editor (หนา เอียง รายการ ลิงก์) เก็บ HTML |
| `typingtest` | text | วิดเจ็ตทดสอบพิมพ์ดีด — ข้อความป้ายกำกับคือข้อความที่ต้องพิมพ์ วิดเจ็ตบันทึกคำตอบที่พิมพ์และเวลา |

### ส่วนขยายมีเดีย

| Appearance Attribute | Question Types | คำอธิบาย |
|----------------------|----------------|-------------|
| `watermark("expression")` | image | วางลายน้ำข้อความทับบนรูปถ่ายที่ถ่าย อาร์กิวเมนต์คือ XPath expression ที่ประเมิน ณ เวลาถ่าย ตัวอย่าง: `watermark("${id} ${today()}")` |
| `editable` | image | เปิดใช้งานการใส่คำอธิบาย/วาดภาพบนรูปถ่ายที่ถ่ายก่อนบันทึก |

### การกำหนดค่าการแสดงผลแบบอินไลน์

โมดิฟายเออร์ `display{}` และ `results{}` สามารถต่อท้าย appearance แบบ `inline` เพื่อควบคุมการจัดแนวไอคอนและการแสดงผล ใช้ร่วมกับส่วนขยายอินพุตเวลา `inline` ในฟิลด์ `text` และวิดเจ็ตบันทึกมีเดีย

#### พารามิเตอร์ `display{}`

```
inline display{left}
inline display{right,small}
inline display{top,large,inline-icon}
```

| พารามิเตอร์ | ค่า | คำอธิบาย |
|-----------|--------|-------------|
| การจัดแนว | `left`, `right`, `top`, `bottom`, `center` | ตำแหน่งไอคอนเทียบกับฟิลด์อินพุต |
| ขนาด | `small`, `medium`, `large` | ขนาดไอคอน (2.5 rem, 5 rem, 8 rem ตามลำดับ) |
| โหมด | `inline-icon` | เรนเดอร์ตัวกระตุ้นเป็นไอคอนเท่านั้น (ไม่มีกรอบปุ่ม) |
| โหมด | `inline-button` | เรนเดอร์ตัวกระตุ้นเป็นปุ่มเต็มรูปแบบ |

#### พารามิเตอร์ `results{}`

```
inline results{right}
inline results{left,hide(seconds)}
```

| พารามิเตอร์ | ค่า | คำอธิบาย |
|-----------|--------|-------------|
| การจัดแนว | `left`, `right`, `top`, `bottom`, `center` | ตำแหน่งการแสดงค่าผลลัพธ์ |
| `hide(field)` | ชื่อ sub-field ใดก็ได้ | ซ่อนส่วนประกอบเฉพาะของผลลัพธ์ (เช่น `hide(seconds)`) |

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