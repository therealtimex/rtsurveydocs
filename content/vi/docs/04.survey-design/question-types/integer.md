---
title: "Số nguyên (Integer)"
description: "Các câu hỏi kiểu Số nguyên cho phép nhập số nguyên vào bản khảo sát của bạn."
icon: "123"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 222
---

Loại câu hỏi `integer` (số nguyên) trong XLSForm và rtSurvey được sử dụng để thu thập các câu trả lời là số nguyên. Loại câu hỏi này rất cần thiết để thu thập dữ liệu số mà không có phần thập phân, chẳng hạn như số lượng, tuổi hoặc số năm.

## Đặc tả XLSForm cơ bản

| type    | name  | label                 |
|---------|-------|------------------------|
| integer | age   | Nhập tuổi của bạn      |

Để biết thêm chi tiết về loại câu hỏi số nguyên cơ bản, hãy xem [đặc tả XLSForm](https://xlsform.org/en/#question-types).

## Các trường hợp sử dụng

Câu hỏi số nguyên thường được dùng cho:

1. Nhập tuổi
2. Đếm các mục (ví dụ: số trẻ em, số thành viên hộ gia đình)
3. Nhập năm (ví dụ: năm sinh)
4. Đánh giá trên thang điểm số
5. Bất kỳ dữ liệu thu thập nào là số nguyên

## Các phần mở rộng của rtSurvey

Trong khi đặc tả XLSForm cơ bản cho các câu hỏi số nguyên khá đơn giản, rtSurvey cung cấp thêm các tính năng hoặc tùy chỉnh bổ sung:

1. Xác thực phạm vi (Range validation)
2. Thông báo lỗi tùy chỉnh (Custom error messages)
3. Các tùy chọn hiển thị cho nhập số

## Các phương pháp hay nhất

1. Sử dụng nhãn rõ ràng và súc tích để chỉ định dữ liệu đầu vào mong muốn.
2. Triển khai các ràng buộc phạm vi (`range constraints`) để ngăn chặn các dữ liệu nhập không thực tế hoặc sai sót.
3. Cân nhắc sử dụng văn bản gợi ý (`hint`) để cung cấp ví dụ hoặc làm rõ định dạng mong muốn.
4. Đối với các số lớn, hãy cân nhắc sử dụng dấu phẩy hoặc khoảng trắng trong nhãn để cải thiện khả năng đọc (ví dụ: "Nhập dân số (tối đa 1.000.000)").

## Ràng buộc và Xác thực (Constraints and Validation)

Bạn có thể thêm các ràng buộc để đảm bảo giá trị đã nhập nằm trong một phạm vi cụ thể:

| type    | name  | label                 | constraint        | constraint_message                    |
|---------|-------|------------------------|-------------------|---------------------------------------|
| integer | age   | Nhập tuổi của bạn      | .>0 and .<=120    | Tuổi phải nằm trong khoảng từ 1 đến 120 |

## Ví dụ sử dụng

Dưới đây là một ví dụ về cách bạn có thể sử dụng các câu hỏi số nguyên trong một cuộc khảo sát hộ gia đình:

| type    | name           | label                                     | constraint | constraint_message                |
|---------|----------------|-------------------------------------------|------------|-----------------------------------|
| integer | household_size | Có bao nhiêu người sống trong hộ gia đình của bạn? | .>0        | Quy mô hộ gia đình phải ít nhất là 1 |
| integer | num_children   | Có bao nhiêu trẻ em dưới 18 tuổi trong hộ? | .>=0    | Số lượng trẻ em không được là số âm |
| integer | year_built     | Ngôi nhà của bạn được xây dựng vào năm nào? | .>1800 and .<=2023 | Năm phải nằm trong khoảng từ 1800 đến 2023 |

## Tính toán với giá trị Số nguyên

Các giá trị số nguyên có thể được sử dụng trong các phép tính. Dưới đây là một ví dụ:

| type    | name           | label                                     |
|---------|----------------|-------------------------------------------|
| integer | num_adults     | Số lượng người lớn trong hộ gia đình      |
| integer | num_children   | Số lượng trẻ em trong hộ gia đình         |
| calculate | total_members |                                           | 

Trong hàng `calculate`, bạn có thể sử dụng:

```
calculation | ${num_adults} + ${num_children}
```

Điều này sẽ cộng tổng số người lớn và trẻ em để có tổng số thành viên trong hộ gia đình.
