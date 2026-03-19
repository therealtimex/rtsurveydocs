---
title: "Range"
description: "Câu hỏi range cho phép người trả lời chọn một số bằng cách kéo thanh trượt giữa giá trị tối thiểu và tối đa đã xác định."
icon: "sliders"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 238
---

Loại câu hỏi `range` hiển thị một **thanh trượt** (hoặc input tương đương) cho phép người trả lời chọn một số trong phạm vi tối thiểu và tối đa đã xác định. Loại này lý tưởng để thu thập đánh giá, điểm hài lòng, hoặc bất kỳ giá trị số nào mà bạn muốn giới hạn phạm vi một cách trực quan thay vì dựa vào ô nhập văn bản với ràng buộc.

## Cấu hình XLSForm cơ bản

| type | name | label | parameters |
|------|------|-------|------------|
| range | satisfaction | Bạn hài lòng với dịch vụ như thế nào? | start=1 end=5 step=1 |

Cột `parameters` xác định giới hạn thanh trượt và kích thước bước:

| Tham số | Mô tả | Mặc định |
|---------|-------|----------|
| `start` | Giá trị tối thiểu (bao gồm) | 0 |
| `end` | Giá trị tối đa (bao gồm) | 10 |
| `step` | Khoảng tăng giữa các giá trị hợp lệ | 1 |

Để biết thêm chi tiết về loại câu hỏi range tiêu chuẩn, xem [thông số kỹ thuật XLSForm](https://xlsform.org/en/#question-types).

## Ứng dụng

Câu hỏi range thường được dùng cho:

1. Thang đo hài lòng hoặc đánh giá (ví dụ: 1–5 hoặc 0–10)
2. Thang số kiểu Likert
3. Thu thập đo lường khi chỉ các giá trị rời rạc mới hợp lệ
4. Khoảng tuổi hoặc khoảng điểm khi thanh trượt cải thiện khả năng sử dụng so với ô văn bản

## Ví dụ sử dụng

### Thang đánh giá cơ bản

| type | name | label | parameters |
|------|------|-------|------------|
| range | overall_rating | Đánh giá tổng thể (0–10) | start=0 end=10 step=1 |

### Bước thập phân

| type | name | label | parameters |
|------|------|-------|------------|
| range | weight_kg | Cân nặng (kg) | start=0 end=200 step=0.5 |

### Dùng giá trị trong phép tính

| type | name | label | parameters | calculation |
|------|------|-------|------------|-------------|
| range | score | Điểm kiểm tra (0–100) | start=0 end=100 step=5 | |
| calculate | grade | | | if(${score} >= 90, 'A', if(${score} >= 80, 'B', if(${score} >= 70, 'C', 'F'))) |
| note | grade_note | Điểm của bạn là: ${grade} | | |

## Appearance

Loại `range` hiển thị dưới dạng thanh trượt theo mặc định. Không cần giá trị appearance bổ sung cho cách dùng cơ bản. Bạn có thể kết hợp với `horizontal` để có bố cục rộng hơn trên biểu mẫu web:

| type | name | label | parameters | appearance |
|------|------|-------|------------|------------|
| range | nps | Bạn có khả năng giới thiệu chúng tôi không? (0–10) | start=0 end=10 step=1 | horizontal |

## Thực hành tốt

1. Luôn đặt các giá trị `start`, `end`, và `step` có ý nghĩa — không dựa vào giá trị mặc định.
2. Ghi nhãn cho hai đầu thang đo trong cột `hint` (ví dụ: `hint: 0 = Rất không hài lòng, 10 = Rất hài lòng`) để người trả lời hiểu ngữ cảnh.
3. Với thang Likert 5 điểm, dùng `start=1 end=5 step=1` thay vì 0–4, vì người trả lời kỳ vọng "1" là mức thấp nhất.
4. Dùng `range` thay vì `integer` + constraint khi bản chất giới hạn của input là một phần trong thiết kế câu hỏi (thanh trượt truyền đạt thang đo một cách trực quan).

## Giới hạn

- Widget thanh trượt có thể không lý tưởng cho phạm vi rất rộng (ví dụ: 0–10000) — `integer` dạng văn bản với constraint thân thiện hơn trong những trường hợp đó.
- Trên thiết bị di động, các giá trị bước nhỏ (ví dụ: `step=0.1`) có thể khó kiểm soát chính xác bằng thanh trượt cảm ứng.
