---
title: "การข้ามคำถาม"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 280
---

Skip logic หรือที่เรียกว่า branching หรือ conditional logic ช่วยให้คุณสร้างแบบสำรวจแบบไดนามิกที่ปรับตามคำตอบของผู้ตอบแบบสำรวจ ใน rtSurvey skip logic จะถูกนำไปใช้โดยใช้คอลัมน์ `relevant` ใน XLSForm ของคุณ

## Skip Logic พื้นฐาน

ในการใช้งาน skip logic พื้นฐาน ให้ใช้คอลัมน์ `relevant` เพื่อระบุเงื่อนไข:

```
| type           | name          | label                       | relevant            |
|----------------|---------------|-----------------------------|--------------------|
| select_one y_n | likes_pizza   | Do you like pizza?          |                    |
| select_multiple pizza_toppings | favorite_topping | Favorite toppings | ${likes_pizza} = 'yes' |
```

## ไวยากรณ์สำหรับนิพจน์ Relevant

- ใช้ `${ }` เพื่ออ้างอิงตัวแปรคำถามอื่น
- สำหรับคำถาม `select_one` เปรียบเทียบโดยตรง: `${question_name} = 'answer'`
- สำหรับคำถาม `select_multiple` ใช้ฟังก์ชัน `selected()`

## Skip Logic ขั้นสูง

### เงื่อนไขหลายข้อ

คุณสามารถรวมเงื่อนไขหลายข้อโดยใช้ `and`, `or` และวงเล็บ:

```
| type    | name  | label                   | relevant                                  |
|---------|-------|-------------------------|-------------------------------------------|
| integer | age   | What is your age?       |                                           |
| text    | school| What school do you attend? | ${age} < 18 and (${location} = 'urban' or ${location} = 'suburban') |
```

### การใช้คำถาม select_multiple

สำหรับคำถาม `select_multiple` ใช้ฟังก์ชัน `selected()`:

```
| type           | name          | label                       | relevant                               |
|----------------|---------------|-----------------------------|-----------------------------------------|
| select_multiple pizza_toppings | favorite_topping | Favorite toppings |                                         |
| text           | cheese_type   | Favorite type of cheese     | selected(${favorite_topping}, 'cheese') |
```

## แนวทางปฏิบัติที่ดีที่สุดสำหรับ Skip Logic ใน rtSurvey

1. **ทำให้เรียบง่าย**: หลีกเลี่ยงเงื่อนไข relevance ที่ซับซ้อนเกินไปเมื่อเป็นไปได้
2. **ทดสอบอย่างละเอียด**: ใช้ฟีเจอร์ preview ของ rtSurvey เพื่อทดสอบเส้นทางที่เป็นไปได้ทั้งหมดในแบบสำรวจ
3. **พิจารณาประสิทธิภาพ**: skip logic ที่ซับซ้อนมากสามารถส่งผลต่อประสิทธิภาพการสำรวจ
4. **ใช้ชื่อตัวแปรที่ชัดเจน**: ทำให้นิพจน์ relevance อ่านและบำรุงรักษาได้ง่ายขึ้น
5. **บันทึก Logic ของคุณ**: เพิ่มหมายเหตุเพื่ออธิบาย skip pattern ที่ซับซ้อน