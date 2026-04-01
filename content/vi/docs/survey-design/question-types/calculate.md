---
title: "Tính toán (Calculate)"
description: ""
icon: "calculate"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 235
---

Các câu hỏi `calculate` (tính toán) trong XLSForms và rtSurvey được sử dụng để thực hiện các phép tính dựa trên các trường hoặc giá trị khác trong biểu mẫu của bạn. Các câu hỏi này không hiển thị cho người dùng mà chạy ở chế độ nền, lưu kết quả của chúng để sử dụng hoặc gửi sau này.

## Cú pháp

Trong XLSForm, một câu hỏi tính toán được định nghĩa như sau:

| type      | name     | label | calculation |
|-----------|----------|-------|-------------|
| calculate | calc_q1  |       | ${q1} + ${q2} |

- **type**: Luôn là "calculate" cho loại câu hỏi này.
- **name**: Một tên duy nhất cho câu hỏi tính toán.
- **label**: Thường được để trống vì các câu hỏi tính toán không hiển thị cho người dùng.
- **calculation**: Công thức sẽ được thực hiện.

## Các trường hợp sử dụng

Câu hỏi tính toán thường được dùng cho:

1. Thực hiện các phép toán số học
2. Nối các chuỗi văn bản
3. Áp dụng các logic hoặc hàm phức tạp
4. Lưu trữ các kết quả trung gian để sử dụng sau này

## Ví dụ

### Toán số học cơ bản

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | total    | ${price} * ${quantity} |
```

### Nối chuỗi văn bản

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | full_name| concat(${first_name}, ' ', ${last_name}) |
```

### Sử dụng các hàm

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | age      | int((today() - ${date_of_birth}) / 365.25) |
```

## Cách dùng nâng cao trong rtSurvey

### Hàm pulldata()

rtSurvey hỗ trợ hàm `pulldata()` trong các trường tính toán, cho phép bạn truy xuất dữ liệu từ các tệp CSV bên ngoài:

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | city     | pulldata('cities', 'city_name', 'zip_code', ${zip_input}) |
```

#### Cú pháp

Cú pháp cơ bản cho pulldata() là:

```
pulldata('csv_filename', 'column_to_return', 'key_column', ${matching_value})
```

- 'csv_filename': Tên tệp CSV (không có đuôi .csv)
- 'column_to_return': Tên cột chứa dữ liệu bạn muốn lấy
- 'key_column': Tên cột dùng để khớp dữ liệu
- ${matching_value}: Giá trị cần tra cứu trong cột khóa (thường là một biến từ biểu mẫu)

#### Các lưu ý quan trọng

1. Tệp CSV phải được tải lên cùng với XLSForm của bạn khi triển khai cuộc khảo sát.
2. Sử dụng dấu phẩy làm dấu phân cách trong tệp CSV của bạn, không phải dấu chấm phẩy.
3. Tránh sử dụng dấu phẩy bên trong các trường dữ liệu của tệp CSV, vì chúng có thể gây ra lỗi phân tích cú pháp.
4. pulldata() chỉ hỗ trợ mối quan hệ 1-1. Nếu tìm thấy nhiều kết quả khớp, nó chỉ trả về kết quả đầu tiên.
5. Có thể có giới hạn về độ dài văn bản có thể kéo về (khoảng 76 ký tự).
6. Bạn có thể sử dụng pulldata() trong các ràng buộc (`constraints`) để xác thực các mục nhập so với dữ liệu CSV.

### Tính toán có điều kiện

Bạn có thể sử dụng câu lệnh if() cho các phép tính có điều kiện:

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | discount | if(${total} > 1000, ${total} * 0.1, 0) |
```

## Các phương pháp hay nhất

1. Sử dụng tên có ý nghĩa cho các trường tính toán để cải thiện khả năng đọc biểu mẫu.
2. Tránh các phép tính quá phức tạp trong một trường duy nhất; hãy chia nhỏ chúng nếu cần thiết.
3. Kiểm tra kỹ các phép tính của bạn, đặc biệt là khi sử dụng các công thức phức tạp hoặc dữ liệu bên ngoài.
4. Hãy nhớ rằng các trường tính toán sẽ chạy mỗi khi biểu mẫu được đánh giá, điều này có thể ảnh hưởng đến hiệu suất nếu có quá nhiều hoặc các phép tính rất phức tạp.
5. Khi sử dụng pulldata(), hãy đảm bảo các tệp CSV của bạn được định dạng chính xác và kiểm tra kỹ lưỡng với dữ liệu và cấu trúc biểu mẫu cụ thể của bạn.

## Hạn chế

- Các trường tính toán không thể chỉnh sửa trực tiếp bởi người dùng.
- Kết quả của trường tính toán không hiển thị ngay lập tức trừ khi được tham chiếu trong một trường hiển thị hoặc được sử dụng trong logic biểu mẫu.
