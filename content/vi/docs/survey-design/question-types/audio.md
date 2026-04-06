---
title: "Audio"
description: "Câu hỏi audio cho phép người trả lời ghi âm và gửi tệp âm thanh như một phần của cuộc khảo sát."
icon: "mic"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 228
---

Loại câu hỏi `audio` cho phép người trả lời **ghi âm** hoặc tải lên tệp âm thanh có sẵn như một phần câu trả lời khảo sát. Loại này hữu ích để ghi lại lời kể bằng miệng, âm thanh môi trường, lời chứng thực, hoặc bất kỳ thông tin nào được truyền đạt qua giọng nói tốt hơn qua văn bản.

## Cấu hình XLSForm cơ bản

| type  | name        | label                        |
|-------|-------------|------------------------------|
| audio | voice_note  | Vui lòng ghi âm ý kiến của bạn |

Để biết thêm chi tiết về loại câu hỏi audio tiêu chuẩn, xem [thông số kỹ thuật XLSForm](https://xlsform.org/en/#question-types).

## Ứng dụng

Câu hỏi audio thường được dùng cho:

1. Ghi lại câu trả lời lời nói cho câu hỏi mở, giảm gánh nặng nhập liệu cho người điều tra
2. Ghi lại lời chứng thực, câu chuyện cá nhân hoặc lịch sử truyền miệng
3. Ghi lại âm thanh môi trường (ví dụ: mức tiếng ồn gần cơ sở hạ tầng)
4. Thu thập mẫu giọng nói cho nghiên cứu ngôn ngữ học hoặc y tế
5. Cho phép người trả lời bổ sung giải thích bằng lời cho các câu trả lời số hoặc lựa chọn

## Định dạng dữ liệu

Tệp âm thanh được lưu dưới dạng tệp đính kèm nhị phân cùng với bản gửi biểu mẫu, thường là:

- **Định dạng:** MP3 hoặc AAC (ghi âm di động); WAV (ghi âm chất lượng cao)
- **Tên tệp:** `{instanceID}-{fieldname}.mp3` (hoặc tương đương)
- **Lưu trữ:** Tải lên thư mục media trên server và liên kết với bản ghi gửi
- **Truy cập:** Có thể phát và tải xuống từ giao diện quản lý bản ghi gửi

## Phần mở rộng của rtSurvey

### Thời lượng tối đa

Dùng cột `parameters` để giới hạn độ dài ghi âm:

| type | name | label | parameters |
|------|------|-------|------------|
| audio | interview | Ghi âm cuộc phỏng vấn | `max-duration=120` |

`max-duration` tính bằng giây. Thiết bị ghi âm tự động dừng khi đến giới hạn.

### Cài đặt chất lượng

Chất lượng ghi âm có thể được đặt qua `parameters`:

| type | name | label | parameters |
|------|------|-------|------------|
| audio | feedback | Ghi âm phản hồi | `quality=normal` |

Các giá trị hỗ trợ: `low`, `normal` (mặc định), `voice-only`. `voice-only` tối ưu hóa cho âm thanh giọng nói với giảm tiếng ồn.

### Phát lại trước khi gửi

Trên mobile, người điều tra có thể phát lại đoạn ghi âm trước khi tiếp tục. Tính năng này được bật mặc định — không cần cấu hình thêm.

### Tích hợp máy ghi âm gốc

Trên Android và iOS, `audio` khởi chạy ứng dụng ghi âm gốc của thiết bị. Trên web, sử dụng MediaRecorder API của trình duyệt.

## Ví dụ sử dụng

### Với thời lượng tối đa và gợi ý

| type | name | label | hint | parameters |
|------|------|-------|------|------------|
| audio | story | Hãy kể cho chúng tôi nghe về sự việc theo lời của bạn | Nói rõ ràng. Ghi âm dừng sau 3 phút. | `max-duration=180` |

### Audio có điều kiện — chỉ khi phát hiện vấn đề

| type | name | label | relevant | required |
|------|------|-------|----------|----------|
| select_one yesno | issue_found | Có phát hiện vấn đề không? | | |
| audio | issue_audio | Ghi âm mô tả về vấn đề | `${issue_found} = 'yes'` | `${issue_found} = 'yes'` |

## Thực hành tốt

1. Nêu rõ trong `label` hoặc `hint` những gì người điều tra cần nói và trong bao lâu.
2. Dùng `max-duration` để tránh tệp quá lớn ở các khu vực có tốc độ tải lên chậm.
3. Thông báo cho người trả lời trước khi bắt đầu ghi — ghi âm bất ngờ có thể gây lo ngại về quyền riêng tư.
4. Kiểm tra ghi âm trên thiết bị đích và điều kiện mạng trước khi triển khai.
5. Đặt `quality=voice-only` cho ghi âm phỏng vấn để giảm kích thước tệp mà không mất độ rõ ràng.

## Giới hạn

- Tệp âm thanh có thể lớn (bản ghi âm 2 phút ở chất lượng bình thường khoảng 2–4 MB) — cần tính đến giới hạn dữ liệu và thời gian tải lên.
- Không phải tất cả trình duyệt đều hỗ trợ MediaRecorder API — Chrome và Firefox hoạt động ổn định; Safari trên iOS cũ hơn có thể gặp vấn đề.
- Chuyển ngôn âm thanh cần thêm bước xử lý sau (thủ công hoặc tự động nhận dạng giọng nói).
- Quy định về quyền riêng tư có thể hạn chế việc ghi âm giọng nói — cần xác minh yêu cầu bảo vệ dữ liệu địa phương.
