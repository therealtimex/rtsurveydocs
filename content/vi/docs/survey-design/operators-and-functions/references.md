---
title: "Tham chiếu giá trị"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 291
---

Cú pháp `${fieldname}` được dùng để tham chiếu giá trị hiện tại của một trường khác trong biểu mẫu. Nó có thể đại diện cho giá trị đã được nhập, được chọn hoặc được tính toán, và sẽ được hiển thị chính xác như trong dữ liệu đã gửi.

Ví dụ:
Nếu bạn có trường tên là "age" và muốn lấy giá trị chính xác đã nhập vào trường đó, bạn có thể dùng `${age}`.

Với ràng buộc (`constraints`), ký hiệu `.` được dùng để tham chiếu giá trị đề xuất hoặc lựa chọn của người dùng cho trường hiện tại. Nó cho phép áp dụng các điều kiện hoặc giới hạn dựa trên giá trị người dùng đang nhập hoặc chọn tại thời điểm đó.

Ví dụ:
Nếu bạn muốn kiểm tra giá trị đề xuất cho trường hiện tại có nhỏ hơn 3 hay không, bạn có thể dùng ràng buộc `. < 3`.

---

## `..` — Tham chiếu nhóm cha

Trong nhóm hoặc nhóm lặp, `..` tham chiếu đến **ngữ cảnh cha**. Điều này hiếm khi cần trong thực tế nhưng được dùng trong các biểu thức XPath nâng cao để điều hướng hệ thống phân cấp biểu mẫu.

---

## Nơi các tham chiếu được dùng

| Cột | Loại tham chiếu | Ví dụ |
|-----|-----------------|-------|
| `relevant` | `${fieldname}` | `${consent} = 'yes'` |
| `constraint` | `.` cho trường hiện tại, `${fieldname}` cho trường khác | `. > 0 and . <= ${max_value}` |
| `calculation` | `${fieldname}` | `${adults} + ${children}` |
| `required` | `${fieldname}` | `${has_income} = 'yes'` |
| `default` | `${fieldname}` | `${previous_answer}` |
| `label` | `${fieldname}` trong văn bản | `"Tuổi của bạn là ${age} tuổi"` |
| `choice_filter` | Tên cột (không có `${}`) | `district = ${district}` |

{{% alert icon=" " context="warning" %}}
Trong cột `choice_filter`, tham chiếu **tên cột lựa chọn** trực tiếp (không có `${}`), và tham chiếu **trường biểu mẫu** bằng `${}`. Nhầm lẫn hai loại này là nguồn lỗi phổ biến.
{{% /alert %}}

---

## Tham chiếu giá trị trong nhóm lặp

Trong vòng lặp, `${fieldname}` tham chiếu trường trong **cùng phiên bản** của vòng lặp:

```
relevant: ${member_age} < 18
```

Điều này dùng giá trị `member_age` của phiên bản vòng lặp hiện tại, không phải tất cả các phiên bản.

Để tham chiếu trường trong một phiên bản **cụ thể** từ bên ngoài vòng lặp, dùng `indexed-repeat()`:

```
indexed-repeat(${member_name}, ${household_members}, 1)
```

Xem [Hàm — Hàm cho trường lặp](functions#repeated-field-functions) để biết chi tiết đầy đủ.

---

## Kiểm tra giá trị rỗng

Kiểm tra xem trường đã được trả lời chưa:

```
${fieldname} != ''       (trường không rỗng)
${fieldname} = ''        (trường rỗng)
```

Với số, cũng kiểm tra:
```
${age} > 0               (tuổi có giá trị dương — ngầm định không rỗng trong ngữ cảnh số)
```

---

## Ép kiểu trong tham chiếu

Khi bạn dùng `${fieldname}` trong ngữ cảnh số (ví dụ: `${age} + 1`), rtSurvey tự động ép kiểu giá trị chuỗi thành số. Trường rỗng được ép thành `0` hoặc `NaN` tùy thuộc vào phép toán — dùng `coalesce(${field}, 0)` để an toàn mặc định trường số rỗng về không.
