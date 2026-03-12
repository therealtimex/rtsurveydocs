---
title: "Xác thực câu trả lời"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 270
---

Một cách để đảm bảo chất lượng dữ liệu là thêm các ràng buộc (`constraints`) vào các trường dữ liệu trong biểu mẫu của bạn. Các ràng buộc giúp ngăn người dùng nhập các câu trả lời không hợp lệ hoặc không thể xảy ra. Ví dụ: khi hỏi về thu nhập của một người, bạn muốn tránh các giá trị phi thực tế, chẳng hạn như số âm hoặc giá trị cực cao. Thêm các ràng buộc dữ liệu trong biểu mẫu của bạn rất dễ thực hiện. Chỉ cần làm theo các bước dưới đây:

1. Thêm một cột mới có tên là "constraint" vào biểu mẫu của bạn.
2. Trong cột "constraint", hãy nhập một công thức chỉ định các giới hạn cho câu trả lời.

### Ví dụ

Hãy xem xét một ví dụ mà chúng ta muốn thêm ràng buộc cho thu nhập của một người. Ràng buộc yêu cầu thu nhập phải nằm trong khoảng từ 0$ đến 1,000,000$. Đây là cách bạn có thể thiết lập ràng buộc:

{{< table >}}
| `name`      | `constraint`                  |
|---------------|-----------------------------|
| Income        | . >= 0 & . <= 1000000      |
{{< /table >}}

Trong ví dụ trên, dấu "." trong công thức tham chiếu lại biến câu hỏi, đại diện cho giá trị do người dùng nhập cho câu hỏi "Income". Ràng buộc ". >= 0 && . <= 1000000" đảm bảo rằng thu nhập được nhập vào lớn hơn hoặc bằng 0 và nhỏ hơn hoặc bằng 1,000,000.

### Ràng buộc cứng (Hard constraint)

### Cảnh báo mềm (Soft alert)
