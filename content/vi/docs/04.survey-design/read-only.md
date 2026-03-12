---
title: "Chỉ đọc (Read-only)"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 287
---

Các trường chỉ đọc (`read-only`) trong rtSurvey cho phép bạn hiển thị thông tin mà người trả lời không thể chỉnh sửa. Tính năng này đặc biệt hữu ích để hiển thị dữ liệu được điền trước, kết quả tính toán hoặc thông tin cần giữ nguyên trong suốt cuộc khảo sát.

## Cách dùng cơ bản

Để đặt một trường là chỉ đọc, hãy sử dụng cột `read_only` trong XLSForm của bạn:

```
| type    | name | label                 | read_only | default |
|---------|------|----------------------|-----------|---------|
| integer | num  | Mã số bệnh nhân là:  | yes       | 5       |
```

Trong ví dụ này, mã số bệnh nhân được đặt là 5 và người trả lời không thể thay đổi.

## Kết hợp Chỉ đọc với Giá trị mặc định

Các trường chỉ đọc thường được sử dụng kết hợp với các giá trị mặc định để hiển thị thông tin được xác định trước hoặc được tính toán:

```
| type    | name     | label               | read_only | default        |
|---------|----------|---------------------|-----------|----------------|
| text    | username | Người dùng đăng nhập: | yes       | ${current_user}|
| date    | today    | Ngày hiện tại:      | yes       | today()        |
```

Ở đây, tên người dùng và ngày hiện tại được hiển thị nhưng không thể chỉnh sửa.

## Các tính năng dành riêng cho rtSurvey

### Chỉ đọc có điều kiện (Conditional Read-only)

rtSurvey mở rộng chức năng chỉ đọc với logic có điều kiện:

```
| type    | name     | label           | read_only                |
|---------|----------|-----------------|--------------------------|
| integer | age      | Tuổi:           | ${role} = 'viewer'       |
| text    | comments | Ghi chú:        | selected(${status}, 'closed') |
```

Trong những ví dụ này:
- Trường 'tuổi' chỉ ở chế độ chỉ đọc nếu vai trò của người dùng là 'viewer'.
- Trường 'ghi chú' trở thành chỉ đọc nếu trạng thái là 'closed'.

### Trạng thái Chỉ đọc động

rtSurvey cho phép bạn thay đổi trạng thái chỉ đọc một cách linh hoạt:

```
| type      | name     | label    | read_only              |
|-----------|----------|----------| ----------------------|
| text      | address  | Địa chỉ: | ${edit_mode} = 'false' |
```

Điều này cho phép bạn chuyển đổi giữa các chế độ có thể chỉnh sửa và chỉ đọc dựa trên một số điều kiện hoặc hành động của người dùng.

## Các phương pháp hay nhất cho trường Chỉ đọc

1. **Sự rõ ràng**: Chỉ dẫn rõ ràng trường nào là chỉ đọc thông qua các gợi ý trực quan hoặc nhãn.
2. **Sự nhất quán**: Sử dụng đồng nhất các trường chỉ đọc xuyên suốt bản khảo sát.
3. **Xác thực**: Mặc dù các trường chỉ đọc không thể chỉnh sửa, nhưng hãy đưa chúng vào quy trình xác thực dữ liệu của bạn.
4. **Hiệu suất**: Cẩn trọng với các tính toán phức tạp trong các trường chỉ đọc, vì chúng có thể ảnh hưởng đến thời gian tải biểu mẫu.
5. **Khả năng tiếp cận**: Đảm bảo các trường chỉ đọc được đánh dấu đúng cách cho các trình đọc màn hình.

## Kỹ thuật nâng cao

### Trường tính toán chỉ đọc

Sử dụng các trường chỉ đọc để hiển thị kết quả tính toán dựa trên các câu trả lời khác:

```
| type      | name     | label           | read_only | calculation            |
|-----------|----------|-----------------|-----------|------------------------|
| calculate | bmi      | Chỉ số BMI:     | yes       | ${weight} / (${height} * ${height}) |
```

### Hiển thị dữ liệu lịch sử

Các trường chỉ đọc có thể hiển thị dữ liệu từ các cuộc khảo sát trước đó hoặc các nguồn bên ngoài:

```
| type    | name           | label                  | read_only | default                    |
|---------|----------------|------------------------|-----------|----------------------------|
| text    | last_visit_date| Ngày thăm khám trước:  | yes       | ${pulldata('visits', 'date', 'id', ${patient_id})} |
```

## Lưu ý về Quản lý dữ liệu

- Các trường chỉ đọc được bao gồm trong quá trình xuất dữ liệu, thường có cờ đánh dấu trạng thái chỉ đọc.
- Khi cập nhật các bản ghi hiện có, các trường chỉ đọc giữ nguyên giá trị ban đầu trừ khi được ghi đè một cách rõ ràng thông qua hệ thống quản trị.

## Hành vi trên Ứng dụng di động

- Ứng dụng di động rtSurvey tuân thủ các thiết lập chỉ đọc, bao gồm cả logic chỉ đọc có điều kiện.
- Chế độ ngoại tuyến hỗ trợ đầy đủ chức năng chỉ đọc, bao gồm cả các trường tính toán và động.

## Các hạn chế đã biết

- Một số điều kiện chỉ đọc động phức tạp có thể ảnh hưởng nhẹ đến hiệu suất trên các thiết bị cấu hình thấp.
- Các trường chỉ đọc có thể không ngăn chặn tất cả các hình thức thao túng dữ liệu trong các tệp dữ liệu đã xuất, vì vậy khuyến nghị thực hiện xác thực phía máy chủ cho dữ liệu quan trọng.
