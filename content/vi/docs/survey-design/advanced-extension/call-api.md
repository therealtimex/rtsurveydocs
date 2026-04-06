---
title: "Call API"
description: "Call API cho phép khảo sát lấy dữ liệu từ dịch vụ web bên ngoài và dùng phản hồi để điền vào trường hoặc xác thực câu trả lời."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 294
---

Tính năng **Call API** cho phép trường khảo sát thực hiện yêu cầu HTTP đến dịch vụ bên ngoài và dùng phản hồi để điền giá trị tính toán hoặc xác thực đầu vào người dùng. Điều này cho phép tra cứu thời gian thực, xác minh ID, tra cứu mã vạch, và bất kỳ kiểm tra phía server nào trong quá trình thu thập dữ liệu.

Có hai hàm:

- `callapi()` — lấy giá trị từ API và lưu vào trường `calculate` hoặc `text`
- `callapi-verify()` — gọi API và chặn tiến độ nếu phản hồi không khớp giá trị mong đợi (dùng trong `constraint`)

---

## `callapi()` — Lấy và lưu phản hồi API

### Cú pháp

Đặt `callapi()` trong cột **`calculation`** của trường `calculate` hoặc `text`:

```
callapi(method, url, allowed_auto, max_retry, no_overwrite, extract_expr, timeout, lifetime, response_q, call_type, post_body)
```

### Tham số

| # | Tham số | Mô tả |
|---|---------|-------|
| 1 | `method` | Phương thức HTTP: `'GET'` hoặc `'POST'` |
| 2 | `url` | URL endpoint API |
| 3 | `allowed_auto` | `1` để gọi tự động khi đến trường; `0` để yêu cầu kích hoạt thủ công |
| 4 | `max_retry` | Số lần thử lại tối đa khi thất bại |
| 5 | `no_overwrite` | `1` để giữ giá trị hiện tại nếu trường đã có; `0` để luôn ghi đè |
| 6 | `extract_expr` | Biểu thức JSONPath để trích xuất giá trị mong muốn từ phản hồi (ví dụ: `$.data.name`) |
| 7 | `timeout` | Thời gian chờ yêu cầu tính bằng mili giây |
| 8 | `lifetime` | Thời gian (ms) phản hồi được lưu cache trước khi lấy lại |
| 9 | `response_q` | Tên trường để lưu mã phản hồi HTTP thô (ví dụ: `${response_status}`) |
| 10 | `call_type` | *(Tùy chọn)* Chế độ gọi đặc biệt: `'lazy-upload'` hoặc `'lazy-upload-multiple'` |
| 11 | `post_body` | *(Tùy chọn)* Chuỗi body POST. Tham chiếu trường biểu mẫu bằng `##fieldname##` |

### Ví dụ: Yêu cầu GET để tra cứu hộ gia đình theo ID

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| text | household_id | ID hộ gia đình | | |
| calculate | hh_name | | callapi | `callapi('GET', concat('https://api.example.com/households/', ${household_id}), 1, 3, 0, '$.name', 10000, 0, '')` |
| note | hh_display | Hộ gia đình: ${hh_name} | | |

### Ví dụ: Yêu cầu POST với body JSON

```
callapi('POST', 'https://api.example.com/lookup', 1, 2, 0, '$.result.value', 15000, 0, '', '', '{"id": "##household_id##"}')
```

Trong `post_body`, dùng `##fieldname##` để đưa vào giá trị hiện tại của bất kỳ trường biểu mẫu nào.

### Appearance: `callapi`

Thêm `callapi` vào cột `appearance` của trường để bật tích hợp gọi API:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | api_result | | callapi | `callapi('GET', ...)` |

Khi `allowed_auto` là `0`, rtSurvey hiển thị **nút "Lấy dữ liệu"** mà người điều tra nhấn thủ công.

---

## `callapi-verify()` — Xác thực giá trị với API

`callapi-verify()` chặn gửi trường cho đến khi API xác nhận giá trị nhập vào là hợp lệ. Dùng trong cột **`constraint`**.

### Cú pháp

```
callapi-verify(method, url, extract_expr, match_expr, timeout, constraint_mode, post_body, message)
```

### Tham số

| # | Tham số | Mô tả |
|---|---------|-------|
| 1 | `method` | Phương thức HTTP: `'GET'` hoặc `'POST'` |
| 2 | `url` | Endpoint API xác minh |
| 3 | `extract_expr` | JSONPath để trích xuất giá trị mong đợi từ phản hồi |
| 4 | `match_expr` | Biểu thức so sánh giá trị đã trích xuất với giá trị trường (ví dụ: `$.status = 'valid'`) |
| 5 | `timeout` | Thời gian chờ yêu cầu tính bằng mili giây |
| 6 | `constraint_mode` | `'soft'` chỉ cảnh báo; `'hard'` để chặn tiến độ |
| 7 | `post_body` | *(Tùy chọn)* Body POST với thay thế `##fieldname##` |
| 8 | `message` | *(Tùy chọn)* Thông báo lỗi. Hỗ trợ đa ngôn ngữ: `<en>Invalid!</en><vi>Không hợp lệ!</vi>` |

### Ví dụ: Xác minh mã vạch với registry tài sản

| type | name | label | appearance | constraint | constraint_message |
|------|------|-------|------------|------------|-------------------|
| barcode | asset_code | Quét mã vạch tài sản | callapi-verify | `callapi-verify('POST', 'https://api.example.com/assets/verify', '$.valid', ". = 'true'", 10000, 'hard', '{"code": "##asset_code##"}')` | Không tìm thấy tài sản trong registry |

### Appearance: `callapi-verify(...)`

Cột `appearance` trên trường có `callapi-verify()` trong constraint phải chứa `callapi-verify(params)` hoặc `callapi-verify(dynamicParams)` để báo cho rtSurvey biết trường này dùng xác minh API.

---

## Kết hợp dữ liệu App API với callapi

Kết hợp `callapi()` với `pulldata('app-api', 'user.token')` để đưa token đã xác thực của người dùng vào yêu cầu API:

```
callapi('POST', 'https://api.example.com/data', 1, 2, 0, '$.value', 10000, 0, '', '',
  concat('{"token":"', pulldata('app-api','user.token'), '","id":"##item_id##"}'))
```

## Thực hành tốt

1. Luôn đặt `timeout` hợp lý (5000–15000 ms) — không dùng 0 hoặc giá trị rất cao.
2. Đặt `allowed_auto=0` cho các xác minh người điều tra cần kích hoạt có ý thức (ví dụ: kiểm tra ID).
3. Đặt `no_overwrite=1` khi trường có thể được chỉnh sửa sau này và bạn không muốn lấy lại ghi đè chỉnh sửa thủ công.
4. Dùng `extract_expr` với JSONPath cụ thể thay vì dựa vào văn bản phản hồi thô.
5. Kiểm tra gọi API ở chế độ ngoại tuyến — callapi sẽ thất bại và hiển thị lỗi, nhưng biểu mẫu vẫn có thể hoàn thành với các trường không quan trọng.

## Giới hạn

- Cần kết nối mạng tại thời điểm gọi — các lần gọi sẽ thất bại khi thiết bị ngoại tuyến.
- Phản hồi API phải là JSON — phản hồi XML hoặc văn bản thuần cần phân tích thêm.
- Tần suất gọi cao (ví dụ: một lần gọi API mỗi phiên bản lặp) có thể làm chậm điều hướng biểu mẫu.
