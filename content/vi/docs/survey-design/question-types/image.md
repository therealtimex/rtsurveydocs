---
title: "Hình ảnh (Image)"
description: "Các câu hỏi kiểu Hình ảnh cho phép người trả lời chụp và gửi ảnh như một phần của cuộc khảo sát."
icon: "image"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 227
---

Loại câu hỏi `image` (hình ảnh) trong XLSForm và rtSurvey cho phép người trả lời chụp và gửi ảnh như một phần câu trả lời khảo sát của họ. Tính năng này đặc biệt hữu ích để thu thập dữ liệu trực quan, ghi lại các quan sát hoặc cung cấp bằng chứng trong các cuộc khảo sát thực địa.

## Đặc tả XLSForm cơ bản

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| image | photo       | Chụp ảnh vị trí này            |

Để biết thêm chi tiết về loại câu hỏi hình ảnh cơ bản, hãy xem [đặc tả XLSForm](https://xlsform.org/en/#question-types).

## Các trường hợp sử dụng

Câu hỏi hình ảnh thường được dùng cho:

1. Ghi lại các điều kiện hoặc quan sát tại thực địa
2. Thu thập bằng chứng trực quan trong các nghiên cứu
3. Thu thập ảnh trước và sau khi đánh giá tác động
4. Xác minh việc hoàn thành nhiệm vụ hoặc sự có mặt tại địa điểm
5. Thu thập dữ liệu trực quan để phân tích từ xa

## Các phương pháp hay nhất

1. Cung cấp hướng dẫn rõ ràng về những gì cần được chụp ảnh.
2. Xem xét hệ quả về quyền riêng tư và thông báo cho người trả lời về cách ảnh của họ sẽ được sử dụng.
3. Lưu ý đến kích thước tệp và giới hạn lưu trữ, đặc biệt đối với các khảo sát ở khu vực có kết nối internet hạn chế.
4. Đảm bảo thiết bị có đủ dung lượng lưu trữ và quyền truy cập camera đã được cấp.

## Ví dụ sử dụng

Dưới đây là một ví dụ về cách bạn có thể sử dụng câu hỏi hình ảnh trong một cuộc khảo sát:

| type  | name           | label                                      | hint                                        |
|-------|----------------|--------------------------------------------|--------------------------------------------|
| image | storefront     | Chụp ảnh lối vào cửa hàng                  | Đảm bảo tên cửa hàng được hiển thị rõ ràng  |

## Các phần mở rộng của rtSurvey

Mặc dù đặc tả XLSForm cơ bản cho câu hỏi hình ảnh khá đơn giản, rtSurvey có thể cung cấp thêm các tính năng hoặc tùy chỉnh bổ sung:

1. Thiết lập chất lượng hình ảnh (ví dụ: độ phân giải thấp, trung bình, cao)
2. Tùy chọn thêm chú thích hoặc nhãn cho ảnh
3. Chụp nhiều ảnh cho một câu hỏi duy nhất
4. Tích hợp với ứng dụng camera gốc hoặc thư viện ảnh của thiết bị

## Xử lý dữ liệu

Hình ảnh được thu thập qua loại câu hỏi này thường được:

1. Lưu dưới định dạng hình ảnh phổ biến (ví dụ: JPG, PNG)
2. Lưu trữ cùng với dữ liệu khảo sát khác, thường là trong một thư mục phương tiện riêng biệt
3. Có thể xem và phân tích thông qua nền tảng quản lý khảo sát

## Các lưu ý khi phân tích

Khi sử dụng câu hỏi hình ảnh, hãy cân nhắc:

1. Cách các hình ảnh sẽ được phân tích (ví dụ: xem xét thủ công, phân tích ảnh tự động)
2. Không gian lưu trữ bổ sung cần thiết cho các tệp hình ảnh
3. Các biện pháp bảo mật và bảo vệ dữ liệu khi lưu trữ và xử lý ảnh
4. Nhu cầu tiềm năng về các công cụ chỉnh sửa hoặc sắp xếp ảnh trong giai đoạn phân tích

## Hạn chế

- Các tệp hình ảnh có thể có kích thước lớn, ảnh hưởng đến việc truyền tải và lưu trữ dữ liệu.
- Không phải tất cả các thiết bị đều có camera chất lượng cao hoặc đủ dung lượng lưu trữ.
- Phân tích số lượng lớn hình ảnh có thể mất nhiều thời gian.
- Có thể có những lo ngại về quyền riêng tư khi chụp ảnh, đặc biệt là ở những nơi công cộng.

## Phần mở rộng hình ảnh rtSurvey

### watermark()

Kiểu hiển thị `watermark()` chèn hình mờ văn bản lên ảnh được chụp bằng trường này. Hình mờ thường chứa siêu dữ liệu như tên người điều tra, ngày/giờ hoặc tọa độ GPS, được đóng dấu trực tiếp lên ảnh trước khi lưu.

| type | name | label | appearance |
|------|------|-------|------------|
| image | site_photo | Chụp ảnh địa điểm | `watermark("${enumerator_id} ${today()}")` |

Tham số của `watermark()` là một biểu thức XPath được đánh giá tại thời điểm chụp. Chuỗi kết quả được hiển thị làm văn bản hình mờ.

### editable

Kiểu hiển thị `editable` cho phép người trả lời chú thích hoặc vẽ lên ảnh đã chụp. Thanh công cụ vẽ xuất hiện trên ảnh.

| type | name | label | appearance |
|------|------|-------|------------|
| image | annotated_photo | Chụp ảnh và đánh dấu các khu vực cần lưu ý | editable |

{{% alert icon=" " context="info" %}}
`editable` có thể kết hợp với `watermark()`: `appearance: editable watermark("${id}")`
{{% /alert %}}
