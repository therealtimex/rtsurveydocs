---
title: "Video"
description: "Các câu hỏi kiểu Video cho phép người trả lời quay và gửi các tệp video như một phần của cuộc khảo sát."
icon: "videocam"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 229
---

Loại câu hỏi `video` trong XLSForm và rtSurvey cho phép người trả lời quay và gửi các tệp video như một phần câu trả lời khảo sát của họ. Tính năng này đặc biệt hữu ích để thu thập bằng chứng trực quan, video hướng dẫn hoặc lời chứng thực liên quan đến cuộc khảo sát.

## Đặc tả XLSForm cơ bản

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| video | demo_video  | Vui lòng quay một video demo ngắn |

Để biết thêm chi tiết về loại câu hỏi video cơ bản, hãy xem [đặc tả XLSForm](https://xlsform.org/en/#question-types).

## Các trường hợp sử dụng

Câu hỏi video thường được dùng cho:

1. Thu thập bằng chứng trực quan trong các khảo sát thực địa
2. Ghi lại các bản demo sản phẩm hoặc kịch bản sử dụng
3. Thu thập các video chứng thực
4. Ghi lại các quy trình hoặc thủ tục
5. Cho phép người trả lời cung cấp các giải thích trực quan chi tiết

## Các phương pháp hay nhất

1. Cung cấp hướng dẫn rõ ràng về những gì cần quay và thời lượng bao lâu.
2. Xem xét hệ quả về quyền riêng tư và thông báo cho người trả lời về cách video của họ sẽ được sử dụng.
3. Lưu ý đến kích thước tệp và giới hạn lưu trữ, đặc biệt đối với các khảo sát ở khu vực có kết nối internet hạn chế.
4. Kiểm tra tính năng quay video trên nhiều thiết bị khác nhau để đảm bảo khả năng tương thích.
5. Cân nhắc chỉ định chất lượng hoặc độ phân giải video mong muốn trong phần hướng dẫn.

## Ví dụ sử dụng

Dưới đây là một ví dụ về cách bạn có thể sử dụng câu hỏi video trong một cuộc khảo sát:

| type  | name           | label                                                | hint                                    |
|-------|----------------|------------------------------------------------------|----------------------------------------|
| video | product_demo   | Vui lòng quay một đoạn demo ngắn về việc dùng sản phẩm | Quay từ 30-60 giây, hiển thị các tính năng chính |

## Các phần mở rộng của rtSurvey

Mặc dù đặc tả XLSForm cơ bản cho câu hỏi video khá đơn giản, rtSurvey có thể cung cấp thêm các tính năng hoặc tùy chỉnh bổ sung:

1. Thiết lập thời lượng ghi tối đa
2. Các tùy chọn chất lượng video (ví dụ: thấp, trung bình, cao)
3. Chức năng phát lại để kiểm tra trước khi gửi
4. Tích hợp với ứng dụng quay video gốc của thiết bị
5. Tùy chọn tải lên các tệp video hiện có thay vì quay mới

## Hạn chế

- Các tệp video có thể rất lớn, ảnh hưởng đáng kể đến việc truyền tải và lưu trữ dữ liệu.
- Không phải tất cả các thiết bị đều hỗ trợ khả năng quay video hoặc có thể có dung lượng lưu trữ hạn chế.
- Việc phân tích các câu trả lời bằng video có thể tốn thời gian và có thể yêu cầu phần mềm chuyên dụng.
- Các lo ngại về quyền riêng tư có thể rõ rệt hơn khi thu thập dữ liệu video.

## Xử lý dữ liệu

Các tệp video được thu thập qua loại câu hỏi này thường được:

1. Lưu dưới định dạng video phổ biến (ví dụ: MP4, MOV)
2. Lưu trữ cùng với dữ liệu khảo sát khác, thường là trong một thư mục phương tiện riêng biệt
3. Có thể phát lại và phân tích thông qua nền tảng quản lý khảo sát

## Các lưu ý khi phân tích

Khi sử dụng câu hỏi video, hãy cân nhắc:

1. Cách dữ liệu video sẽ được phân tích (ví dụ: đánh giá thủ công, phân tích video tự động)
2. Thời gian và tài nguyên bổ sung cần thiết để xử lý các câu trả lời video
3. Các biện pháp bảo mật và bảo vệ dữ liệu khi lưu trữ và xử lý các bản ghi video
4. Nhu cầu tiềm năng về các công cụ chỉnh sửa hoặc tổng hợp video trong giai đoạn phân tích
