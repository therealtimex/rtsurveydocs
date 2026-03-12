---
title: "Chọn một (Select_one)"
description: ""
icon: "radio_button_checked"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 224
---
  
  
### select_one listname
  
Câu hỏi `select_one listname` yêu cầu người dùng chọn một tùy chọn duy nhất từ một danh sách các lựa chọn được xác định trước. Trong định nghĩa XLSForm, `listname` phải tương ứng với một giá trị được liệt kê trong cột `list_name` của bảng tính `choices` (ví dụ: "yesno").

Theo mặc định, các lựa chọn được hiển thị dưới dạng các nút chọn (radio buttons), với mỗi nút đại diện cho một lựa chọn tĩnh duy nhất từ danh sách được chỉ định. Tuy nhiên, có nhiều tùy chọn hiển thị (`appearance`) khác nhau để tùy chỉnh giao diện, hành vi và chính danh sách lựa chọn. Tham khảo các phần phụ bên dưới để biết thêm thông tin về các tùy chọn đó.

Trong định nghĩa XLSForm:
{{< table "table table-striped" >}}
| Type             | Name      | Label          | Appearance |
|------------------|-----------|----------------|------------|
| select_one listname | fieldname | câu hỏi văn bản |            |
{{</ table >}}
  
### Các tùy chọn hiển thị cơ bản (Basic appearance options)

Chỉ định các giá trị sau trong cột `appearance` để sửa đổi hình thức hiển thị của trường `select_one listname`:

- **quick**: Tự động chuyển sang câu hỏi tiếp theo ngay sau khi một tùy chọn được chọn, không cần chờ người dùng vuốt về phía trước.
- **minimal**: Hiển thị một trình chọn thả xuống (drop-down) duy nhất thay vì các nút chọn radio.
- **compact**: Hiển thị một bảng các lựa chọn nhỏ gọn. Số lượng cột sẽ tùy thuộc vào chiều rộng của màn hình.
- **compact-#**: Chỉ định số lượng cột cụ thể trong bảng nhỏ gọn, trong đó "#" đại diện cho số lượng cột mong muốn (ví dụ: `compact-3`).
- **quickcompact**: Kết hợp hai kiểu hiển thị "quick" và "compact".
- **quickcompact-#**: Kết hợp kiểu hiển thị "quick" và "compact" và chỉ định số cột cố định.

Trong định nghĩa XLSForm:  
{{< table "table table-striped" >}}
| Type             | Name      | Label          | Appearance       |
|------------------|-----------|----------------|------------------|
| select_one listname | fieldname | câu hỏi văn bản | quick            |
| select_one listname | fieldname | câu hỏi văn bản | minimal          |
| select_one listname | fieldname | câu hỏi văn bản | compact          |
| select_one listname | fieldname | câu hỏi văn bản | compact-#        |
| select_one listname | fieldname | câu hỏi văn bản | quickcompact     |
| select_one listname | fieldname | câu hỏi văn bản | quickcompact-#   |
{{</ table >}}
