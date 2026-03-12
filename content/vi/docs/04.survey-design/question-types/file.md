---
title: "Tệp (File)"
description: "Các câu hỏi kiểu Tệp cho phép người trả lời tải lên các tệp như một phần của câu trả lời khảo sát."
icon: "upload_file"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 230
---

Loại câu hỏi `file` (tệp) trong XLSForm và rtSurvey cho phép người trả lời tải lên các tệp như một phần câu trả lời khảo sát của họ. Tính năng này đặc biệt hữu ích để thu thập tài liệu, hình ảnh hoặc các loại tệp khác liên quan đến cuộc khảo sát.

## Đặc tả XLSForm cơ bản

| type | name      | label                       |
|------|-----------|----------------------------|
| file | document  | Vui lòng tải lên tài liệu của bạn |

Để biết thêm chi tiết về loại câu hỏi tệp cơ bản, hãy xem [đặc tả XLSForm](https://xlsform.org/en/#question-types).

## Các trường hợp sử dụng

Câu hỏi tệp thường được dùng cho:

1. Thu thập các tài liệu hỗ trợ (ví dụ: hóa đơn, chứng chỉ)
2. Thu thập bằng chứng trực quan (ví dụ: ảnh về điều kiện thực địa)
3. Tải lên các biểu mẫu hoặc bảng tính đã hoàn thành
4. Thu thập bất kỳ loại tệp kỹ thuật số nào liên quan đến cuộc khảo sát

## Các phương pháp hay nhất

1. Cung cấp hướng dẫn rõ ràng về loại tệp cần tải lên và bất kỳ giới hạn kích thước nào.
2. Xem xét hệ quả về quyền riêng tư và thông báo cho người trả lời về cách các tệp của họ sẽ được sử dụng và lưu trữ.
3. Lưu ý đến kích thước tệp và giới hạn lưu trữ, đặc biệt đối với các khảo sát ở khu vực có kết nối internet hạn chế.
4. Chỉ định các định dạng tệp được chấp nhận nếu cần thiết.

## Ví dụ sử dụng

Dưới đây là một ví dụ về cách bạn có thể sử dụng câu hỏi tệp trong một cuộc khảo sát:

| type | name           | label                                      | hint                                        |
|------|----------------|--------------------------------------------|--------------------------------------------|
| file | receipt_upload | Vui lòng tải lên ảnh hóa đơn của bạn       | Định dạng chấp nhận: JPG, PNG. Tối đa: 5MB  |

## Các phần mở rộng của rtSurvey

Mặc dù đặc tả XLSForm cơ bản cho câu hỏi tệp khá đơn giản, rtSurvey có thể cung cấp thêm các tính năng hoặc tùy chỉnh bổ sung:

1. Hạn chế loại tệp (ví dụ: chỉ cho phép ảnh, chỉ cho phép PDF)
2. Giới hạn kích thước tệp
3. Khả năng tải lên nhiều tệp
4. Tích hợp với hệ thống tệp của thiết bị hoặc các dịch vụ lưu trữ đám mây

## Xử lý dữ liệu

Các tệp được thu thập thông qua loại câu hỏi này thường được:

1. Lưu dưới định dạng gốc của chúng
2. Lưu trữ cùng với dữ liệu khảo sát khác, thường là trong một thư mục phương tiện riêng biệt
3. Có thể tải xuống và phân tích thông qua nền tảng quản lý khảo sát

## Các lưu ý khi phân tích

Khi sử dụng câu hỏi tệp, hãy cân nhắc:

1. Cách các tệp tải lên sẽ được xử lý và phân tích
2. Không gian lưu trữ bổ sung cần thiết cho các tệp đính kèm
3. Các biện pháp bảo mật và bảo vệ dữ liệu khi lưu trữ và xử lý các tệp đã tải lên
4. Nhu cầu tiềm năng về phần mềm chuyên dụng để mở hoặc phân tích một số loại tệp nhất định

## Hạn chế

- Các tệp lớn có thể ảnh hưởng đáng kể đến việc truyền tải dữ liệu và yêu cầu lưu trữ.
- Không phải tất cả các thiết bị đều có thể dễ dàng truy cập vào các tệp để tải lên.
- Phân tích các tệp đính kèm có thể tốn nhiều thời gian hơn so với các câu trả lời dạng văn bản.
- Có thể có các vấn đề về khả năng tương thích với một số loại tệp nhất định trên các hệ thống khác nhau.
