---
title: "Tìm kiếm động (Dynamic Search)"
description: ""
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 293
---

Tìm kiếm động (Dynamic Search) là một tính năng mạnh mẽ trong rtSurvey cho phép bạn tích hợp chức năng tìm kiếm động vào khảo sát của mình, cho phép truy xuất dữ liệu thời gian thực từ các nguồn bên ngoài.

## Cú pháp (Syntax)

Cú pháp cơ bản để sử dụng Search-API là:

{{< alert context="info" text="search-api(method, url, post_body, value_column, display, data_path, save_path)" />}}


### Các tham số (Parameters)

- `method`: Luôn luôn sử dụng 'POST'.
- `url`: URL để lấy dữ liệu.
- `post_body`: Thân yêu cầu (request body). Sử dụng cú pháp `searchView` (xem tài liệu DataModel Views).
- `value_column`: Trường dữ liệu được sử dụng làm giá trị (`value`).
- `display`: Trường dữ liệu được sử dụng làm nhãn (`label`). Hỗ trợ cú pháp kiểu mẫu (template) với `##key##` và `@{func}` để định dạng nâng cao.
- `data_path`: JSONPath để trích xuất dữ liệu mong muốn từ phản hồi (ví dụ: `$.hits.hits.*._source`).
- `save_path`: Vị trí để lưu trữ dữ liệu phản hồi để sử dụng sau này.

## Ví dụ sử dụng (Usage Examples)

### Cách dùng cơ bản

```
appearance: search-api('POST', 'https://api.example.com/search', '{"query": "%__input__%"}', 'id', 'name', '$.results', 'search_results')
```

### Với định dạng hiển thị nâng cao

```
appearance: search-api('POST', 'https://api.example.com/search', '{"query": "%__input__%"}', 'id', '##name## (##age## tuổi)', '$.results', 'search_results')
```

### Với Hàm trong phần hiển thị (Function in Display)

```
appearance: search-api('POST', 'https://api.example.com/search', '{"query": "%__input__%"}', 'id', '@{if_else(eq("##status##", "active"), "Hoạt động: ##name##", "Không hoạt động: ##name##")}', '$.results', 'search_results')
```

## Các loại câu hỏi hỗ trợ

- `select_one`
- `select_multiple`
- `text` (cho chức năng tự động hoàn thành - autocomplete)

## Các tính năng bổ sung

### API Mặc định (Default API)

Sử dụng `search-default-api()` sau `search-api()` để đặt các giá trị mặc định:

```
appearance: search-api(...) search-default-api(...)
```

### Ký tự phân tách đa lựa chọn (Multiple Selection Separator)

Đối với `select_multiple`, sử dụng `search-default-separator()` để chỉ định ký tự phân tách tùy chỉnh:

```
appearance: search-api(...) search-default-separator(' || ')
```

## Thực hành tốt nhất (Best Practices)

1. Tối ưu hóa các điểm cuối API (API endpoints) để đạt hiệu suất cao, đặc biệt là với các tập dữ liệu lớn.
2. Sử dụng các chiến lược lưu trữ đệm (caching) phù hợp để giảm số lượng lệnh gọi API.
3. Xử lý các lỗi mạng một cách mượt mà trong thiết kế khảo sát của bạn.
4. Kiểm tra kỹ lưỡng với các kịch bản đầu vào khác nhau.

## Các hạn chế đã biết

- Các truy vấn phức tạp có thể ảnh hưởng đến thời gian tải khảo sát.
- Chức năng ngoại tuyến có thể bị hạn chế tùy thuộc vào cách triển khai.

```mermaid
    graph TD
    %% Define styles for nodes
    classDef light fill:#cce5ff,stroke:#0066cc,stroke-width:2px,color:#003366
    classDef dark fill:#2e3b4e,stroke:#a6b1c2,stroke-width:2px,color:#e1e1e1
    classDef submit fill:#ffcc99,stroke:#cc6600,stroke-width:2px,color:#663300
    classDef link fill:#ccffcc,stroke:#009933,stroke-width:2px,color:#003300
    classDef storage fill:#ffffcc,stroke:#999900,stroke-width:2px,color:#333300
    
    %% Define shapes for nodes
    A[<span class="iconify" data-icon="mdi:file-document-multiple" data-inline="false" data-width="18" data-height="18"></span> Biên lai dạng PDF, PNG, HEIC, JPEG, Excel] --> B{<span class="iconify" data-icon="mdi:send" data-inline="false" data-width="18" data-height="18"></span> Gửi biên lai}
    B --> C1([<a href="mailto:keep@keepy.us?subject=Keep%20my%20receipts" style="color:#003300;"><span class="iconify" data-icon="mdi:email" data-inline="false" data-width="18" data-height="18"></span> Email: keep@keepy.us</a>])
    B --> C2([<a href="sms:+16504173562" style="color:#003300;"><span class="iconify" data-icon="mdi:message-text" data-inline="false" data-width="18" data-height="18"></span> SMS: 650-417-3562</a>])
    B --> C3([<a href="https://m.me/keepy.us" target="_blank" style="color:#003300;"><span class="iconify" data-icon="mdi:facebook-messenger" data-inline="false" data-width="18" data-height="18"></span> Messenger: m.me/keepy.us</a>])
    C1 --> D[[<span class="iconify" data-icon="mdi:database" data-inline="false" data-width="18" data-height="18"></span> <b>Dữ liệu biên lai được lưu trong Google Sheet</b><br> - Tự động nhận diện chữ viết<br> - Kiểm tra bởi con người để đảm bảo chính xác<br> - Sao lưu bản số của biên lai]]
    C2 --> D
    C3 --> D
    
    %% Apply classes to nodes
    class A light
    class B submit
    class C1 link
    class C2 link
    class C3 link
    class D storage
    
    %% Adjust arrow styles for better visibility
    linkStyle default stroke:#666,stroke-width:3px
```
