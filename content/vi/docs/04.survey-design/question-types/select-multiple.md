---
title: "Chọn nhiều (Select_multiple)"
description: ""
icon: "check_box"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 225
---

### select_multiple listname

Loại câu hỏi `select_multiple listname` yêu cầu người dùng chọn một hoặc nhiều lựa chọn từ một danh sách các lựa chọn được định nghĩa trước. Trong định nghĩa XLSForm, `listname` phải tương ứng với một giá trị được liệt kê trong cột `list_name` của bảng tính `choices` (ví dụ: "country").

Theo mặc định, các lựa chọn được hiển thị dưới dạng các hộp kiểm (checkboxes), trong đó mỗi hộp kiểm đại diện cho một lựa chọn tĩnh duy nhất từ danh sách đã chỉ định. Tuy nhiên, có nhiều tùy chọn hiển thị (`appearance`) để tùy chỉnh giao diện, chức năng và thậm chí chính danh sách lựa chọn đó. Vui lòng tham khảo các phần phụ bên dưới để biết thêm thông tin về các tùy chọn này.

Khi xuất dữ liệu, mỗi hàng sẽ bao gồm một cột với danh sách các giá trị câu trả lời đã chọn, cách nhau bởi dấu cách cho mỗi trường `select_multiple`.

Khi sử dụng trường `select_multiple` trong xác thực trường hoặc các mẫu bỏ qua (`constraint` hoặc biểu thức `relevance`), hàm `selected()` cần được sử dụng để kiểm tra xem một lựa chọn cụ thể đã được chọn hay chưa. Bạn có thể tìm thêm thông tin về các biểu thức ràng buộc và hiển thị trong các chủ đề trợ giúp.

Trong định nghĩa XLSForm:

| Type                  | Name      | Label          | Appearance |
|-----------------------|-----------|----------------|------------|
| select_multiple listname | fieldname | câu hỏi văn bản |            |
