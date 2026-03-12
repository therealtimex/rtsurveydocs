---
title: "Âm thanh (Audio)"
description: "Các câu hỏi kiểu Âm thanh cho phép người trả lời ghi âm và gửi các tệp âm thanh như một phần của cuộc khảo sát."
icon: "mic"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 228
---

Loại câu hỏi `audio` (âm thanh) trong XLSForm và rtSurvey cho phép người trả lời ghi âm và gửi các tệp âm thanh như một phần câu trả lời khảo sát của họ. Tính năng này đặc biệt hữu ích để thu thập các câu trả lời bằng lời nói, lời chứng thực hoặc âm thanh môi trường liên quan đến cuộc khảo sát.

## Đặc tả XLSForm cơ bản

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| audio | voice_note  | Vui lòng ghi âm ý kiến của bạn |

Để biết thêm chi tiết về loại câu hỏi âm thanh cơ bản, hãy xem [đặc tả XLSForm](https://xlsform.org/en/#question-types).

## Các trường hợp sử dụng

Câu hỏi âm thanh thường được dùng cho:

1. Thu thập các câu trả lời bằng lời nói cho các câu hỏi mở
2. Ghi lại các lời chứng thực hoặc câu chuyện cá nhân
3. Ghi lại âm thanh môi trường hoặc mức độ tiếng ồn
4. Thu thập các mẫu giọng nói cho mục đích nghiên cứu
5. Cho phép người trả lời cung cấp các giải thích chi tiết

## Các phương pháp hay nhất

1. Cung cấp hướng dẫn rõ ràng về những gì cần ghi âm và thời lượng bao lâu.
2. Xem xét hệ quả về quyền riêng tư và thông báo cho người trả lời về cách âm thanh của họ sẽ được sử dụng.
3. Lưu ý đến kích thước tệp và giới hạn lưu trữ, đặc biệt đối với các khảo sát ở khu vực có kết nối internet hạn chế.
4. Kiểm tra tính năng ghi âm trên nhiều thiết bị khác nhau để đảm bảo khả năng tương thích.

## Ví dụ sử dụng

Dưới đây là một ví dụ về cách bạn có thể sử dụng câu hỏi âm thanh trong một cuộc khảo sát:

| type  | name           | label                                                | hint                                    |
|-------|----------------|------------------------------------------------------|----------------------------------------|
| audio | feedback_audio | Vui lòng ghi lại phản hồi của bạn về sản phẩm        | Nói rõ ràng trong tối đa 60 giây       |

## Các phần mở rộng của rtSurvey

Mặc dù đặc tả XLSForm cơ bản cho câu hỏi âm thanh khá đơn giản, rtSurvey có thể cung cấp thêm các tính năng hoặc tùy chỉnh bổ sung:

1. Thiết lập thời lượng ghi âm tối đa
2. Các tùy chọn chất lượng âm thanh (ví dụ: thấp, trung bình, cao)
3. Chức năng phát lại để kiểm tra trước khi gửi
4. Tích hợp với ứng dụng ghi âm gốc của thiết bị

## Hạn chế

- Các tệp âm thanh có thể có kích thước lớn, ảnh hưởng đến việc truyền tải và lưu trữ dữ liệu.
- Không phải tất cả các thiết bị đều hỗ trợ khả năng ghi âm.
- Việc chuyển lời thoại từ tệp âm thanh có thể cần thiết để phân tích, điều này gây tốn thời gian.
- Các lo ngại về quyền riêng tư có thể phát sinh khi thu thập dữ liệu giọng nói.

## Xử lý dữ liệu

Các tệp âm thanh được thu thập qua loại câu hỏi này thường được:

1. Lưu dưới định dạng âm thanh phổ biến (ví dụ: MP3, WAV)
2. Lưu trữ cùng với các dữ liệu khảo sát khác
3. Có thể phát lại và phân tích thông qua nền tảng quản lý khảo sát

## Các lưu ý khi phân tích

Khi sử dụng câu hỏi âm thanh, hãy cân nhắc:

1. Cách dữ liệu âm thanh sẽ được phân tích (ví dụ: chép lời thủ công, tự động chuyển từ giọng nói sang văn bản)
2. Thời gian và tài nguyên bổ sung cần thiết để xử lý các câu trả lời âm thanh
3. Các biện pháp bảo mật và bảo vệ dữ liệu khi lưu trữ và xử lý các bản ghi giọng nói
