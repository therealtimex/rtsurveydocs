---
title: "Call API"
description: "Call API ให้แบบสำรวจดึงข้อมูลจากบริการเว็บภายนอกและใช้การตอบสนองเพื่อเติมฟิลด์หรือตรวจสอบคำตอบ"
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 294
---

ฟีเจอร์ **Call API** ให้ฟิลด์แบบสำรวจทำ HTTP request ไปยังบริการภายนอกและใช้การตอบสนองเพื่อเติมค่าที่คำนวณหรือตรวจสอบอินพุตของผู้ใช้ ซึ่งเปิดใช้งานการค้นหาแบบเรียลไทม์ การตรวจสอบ ID การค้นหา barcode และการตรวจสอบฝั่งเซิร์ฟเวอร์อื่นๆ ระหว่างการเก็บข้อมูล

มีสองฟังก์ชัน:

- `callapi()` — ดึงค่าจาก API และเก็บไว้ในฟิลด์ `calculate` หรือ `text`
- `callapi-verify()` — เรียก API และบล็อกความคืบหน้าหากการตอบสนองไม่ตรงกับค่าที่คาดหวัง

---

## `callapi()` — ดึงและเก็บการตอบสนอง API

### ไวยากรณ์

วาง `callapi()` ในคอลัมน์ **`calculation`** ของฟิลด์ `calculate` หรือ `text`:

```
callapi(method, url, allowed_auto, max_retry, no_overwrite, extract_expr, timeout, lifetime, response_q, call_type, post_body)
```