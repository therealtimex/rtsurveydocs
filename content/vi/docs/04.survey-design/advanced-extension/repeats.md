---
title: "Nhóm lặp nâng cao"
description: "Các mẫu nâng cao cho nhóm lặp: số lần lặp động, lặp lồng nhau, tóm tắt dữ liệu lặp và tham chiếu giá trị giữa các lần lặp."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 295
---

Trang này đề cập đến các mẫu nâng cao khi làm việc với nhóm lặp trong rtSurvey. Để biết kiến thức cơ bản về thiết lập nhóm lặp, xem [Nhóm và Lặp](../repeats).

---

## Số lần lặp động

Mặc định, người điều tra quyết định số lần lặp. Bạn có thể cố định số lần lặp bằng `repeat_count`:

| type | name | label | repeat_count |
|------|------|-------|--------------|
| begin_repeat | household_members | Thành viên hộ gia đình | `${num_members}` |
| text | member_name | Tên thành viên | |
| integer | member_age | Tuổi | |
| end_repeat | | | |

Vòng lặp chạy đúng `${num_members}` lần, nơi `num_members` được thu thập trước đó trong biểu mẫu. Người điều tra không thể thêm hoặc xóa phiên bản.

---

## Truy cập theo chỉ số: `indexed-repeat()`

Truy cập giá trị trường của một phiên bản lặp cụ thể từ **bên ngoài** nhóm lặp bằng `indexed-repeat(repeatedField, repeatGroup, index)`:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | first_name | | `indexed-repeat(${member_name}, ${household_members}, 1)` |
| calculate | second_name | | `indexed-repeat(${member_name}, ${household_members}, 2)` |

Điều này hữu ích để xây dựng trường tóm tắt hoặc tham chiếu dữ liệu thành viên "chính" sau vòng lặp.

---

## Vị trí phiên bản hiện tại: `index()`

Trong nhóm lặp, `index()` trả về vị trí (bắt đầu từ 1) của phiên bản hiện tại. Dùng để gán nhãn mỗi lần lặp hoặc tạo mã định danh duy nhất:

| type | name | label |
|------|------|-------|
| begin_repeat | plots | Thửa đất |
| note | plot_label | Thửa đất số ${index()} |
| text | plot_id | ID thửa đất |
| end_repeat | | |

---

## Tham chiếu trường trong cùng phiên bản

Trong vòng lặp, dùng `${fieldname}` để tham chiếu trường khác **trong cùng phiên bản lặp**. Không cần `indexed-repeat()` trong cùng vòng lặp:

| type | name | label | relevant |
|------|------|-------|----------|
| begin_repeat | members | Thành viên | |
| text | member_name | Tên | |
| integer | member_age | Tuổi | |
| text | school_name | Tên trường | `${member_age} < 18` |
| end_repeat | | | |

---

## Tham chiếu trường cha từ trong vòng lặp

Các trường bên ngoài (phía trên) nhóm lặp có thể được tham chiếu bình thường bằng `${fieldname}`:

| type | name | label |
|------|------|-------|
| text | village | Tên làng/xã |
| begin_repeat | plots | Thửa đất nông nghiệp |
| note | plot_context | Thửa đất ở ${village} |
| end_repeat | | |

---

## Tóm tắt dữ liệu lặp

Dùng các hàm tổng hợp lặp **bên ngoài** nhóm lặp để tóm tắt:

| Hàm | Ví dụ | Mô tả |
|-----|-------|-------|
| `count(group)` | `count(${household_members})` | Số phiên bản |
| `sum(field)` | `sum(${loan_amount})` | Tổng trường số |
| `min(field)` | `min(${member_age})` | Giá trị nhỏ nhất |
| `max(field)` | `max(${member_age})` | Giá trị lớn nhất |
| `join(sep, field)` | `join(', ', ${member_name})` | Danh sách phân cách bởi dấu phẩy |
| `count-if(group, expr)` | `count-if(${members}, ${member_age} < 18)` | Đếm có điều kiện |
| `sum-if(field, expr)` | `sum-if(${loan_amount}, ${loan_amount} > 500)` | Tổng có điều kiện |
| `join-if(sep, field, expr)` | `join-if(', ', ${name}, ${age} >= 18)` | Ghép có điều kiện |

### Ví dụ: Tóm tắt hộ gia đình

| type | name | label | calculation |
|------|------|-------|-------------|
| integer | num_members | Có bao nhiêu thành viên? | |
| begin_repeat | members | Thành viên | `${num_members}` |
| text | member_name | Tên | |
| integer | member_age | Tuổi | |
| end_repeat | | | |
| calculate | total_members | | `count(${members})` |
| calculate | children_count | | `count-if(${members}, ${member_age} < 18)` |
| calculate | adult_names | | `join-if(', ', ${member_name}, ${member_age} >= 18)` |
| note | summary | ${total_members} thành viên; ${children_count} dưới 18 tuổi. Người lớn: ${adult_names} | |

---

## Lặp lồng nhau

Nhóm lặp có thể chứa nhóm lặp khác. Dùng cẩn thận — lặp lồng nhau thêm độ phức tạp và có thể gây nhầm lẫn cho người điều tra.

| type | name | label |
|------|------|-------|
| begin_repeat | households | Hộ gia đình |
| text | hh_id | ID hộ gia đình |
| begin_repeat | hh_members | Thành viên |
| text | member_name | Tên thành viên |
| end_repeat | | |
| end_repeat | | |

Để tham chiếu trường trong vòng lặp ngoài từ vòng lặp trong, dùng `${fieldname}` — nó phân giải đến tổ tiên khớp gần nhất:

Bên trong vòng lặp `hh_members`, `${hh_id}` trả về ID của **hộ gia đình hiện tại**, không phải tất cả hộ gia đình.

---

## Rank trong nhóm lặp: `rank-index()`

Khi trường `rank` tồn tại trong vòng lặp, dùng `rank-index(instanceNumber, repeatedField)` từ bên ngoài để lấy thứ hạng theo thứ tự của một phiên bản cụ thể:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | top_scorer | | `rank-index(1, ${score})` |

`rank-index(1, ${score})` trả về chỉ số phiên bản có điểm cao nhất.

---

## Thực hành tốt

1. Luôn dùng `repeat_count` khi số lần lặp đã biết trước — điều này ngăn người điều tra vô tình thêm hoặc xóa phiên bản.
2. Giữ nhóm lặp tập trung — vòng lặp với 20+ câu hỏi mỗi phiên bản khó điều hướng.
3. Đặt tên nhóm lặp rõ ràng (ví dụ: `household_members`, không phải `repeat1`) — tên xuất hiện trong lời gọi hàm và dữ liệu xuất.
4. Kiểm tra với số lần lặp tối đa dự kiến để xác minh hiệu suất.
5. Dùng appearance `field-list` trên nhóm lặp để hiển thị tất cả trường trên một màn hình mỗi phiên bản (mobile).

---

## Giới hạn

- `indexed-repeat()` cần chỉ số hợp lệ (1 đến số phiên bản) — chỉ số ngoài phạm vi trả về rỗng.
- Lặp lồng nhau quá 2 cấp không được khuyến nghị và có thể gây vấn đề hiển thị trên một số client.
- Các hàm tổng hợp (`sum`, `count`, v.v.) hoạt động trên toàn bộ nhóm lặp — bạn không thể tổng hợp một tập con phiên bản nếu không dùng các biến thể `*-if`.
