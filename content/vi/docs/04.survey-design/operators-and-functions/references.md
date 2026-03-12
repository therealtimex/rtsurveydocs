---
title: "Tham chiếu giá trị (Referencing values)"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 291
---

Cú pháp `${fieldname}` được sử dụng để tham chiếu đến giá trị hiện tại của một trường khác trong biểu mẫu của bạn. Nó có thể đại diện cho giá trị đã được nhập, được chọn hoặc được tính toán, và nó sẽ được hiển thị chính xác như khi xuất hiện trong dữ liệu đã gửi.

Ví dụ:
Nếu bạn có một trường tên là "age" (tuổi) và bạn muốn lấy giá trị chính xác đã được nhập vào trường đó, bạn có thể sử dụng `${age}`.

Khi nói đến các ràng buộc (`constraints`), ký hiệu `.` được sử dụng để tham chiếu đến giá trị mà người dùng đang nhập hoặc chọn cho trường hiện tại. Nó cho phép bạn áp dụng các điều kiện hoặc giới hạn dựa trên giá trị mà người dùng đang nhập hoặc chọn tại thời điểm đó.

Ví dụ:
Nếu bạn muốn kiểm tra xem giá trị đề xuất cho trường hiện tại có nhỏ hơn 3 hay không, bạn có thể sử dụng ràng buộc `. < 3`.
