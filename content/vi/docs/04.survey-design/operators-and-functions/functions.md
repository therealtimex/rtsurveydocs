---
title: "Hàm"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 293
---

### Hàm chuỗi

{{% alert icon=" " context="warning" %}}
Khi làm việc với chuỗi trong biểu thức, hãy dùng dấu ngoặc đơn ('') để bao quanh chuỗi ký tự. Ngoại lệ là khi bạn muốn đưa dấu ngoặc đơn vào trong chuỗi — khi đó dùng dấu ngoặc kép ("") để bao quanh toàn bộ chuỗi.

Ví dụ:
- Đúng: if(${yesno} = 1, "a string with 'single quotes' in it", "no single quotes here")
- Sai: if(${yesno} = 1, 'a string with 'single quotes' in it', 'no single quotes here')

Về dấu ngoặc thông minh (smart quotes): nhiều trình soạn thảo văn bản phong phú tự động chuyển dấu ngoặc thẳng ("" hoặc '') thành dấu ngoặc cong ("" hoặc ''), có thể gây lỗi cú pháp hoặc hành vi bất ngờ. Hãy đảm bảo dùng nhất quán dấu ngoặc thẳng trong biểu thức.
{{% /alert %}}

rtSurvey hỗ trợ các hàm sau đây:

1. `string(field)`: Chuyển đổi trường sang chuỗi.
   - Ví dụ: `string(34.8)` sẽ được chuyển thành `'34.8'`.

2. `string-length(field)`: Trả về độ dài chuỗi của trường.
   - Ví dụ: `string-length(.) > 3 and string-length(.) < 10` có thể dùng để đảm bảo trường hiện tại có từ 3 đến 10 ký tự.

3. `substr(fieldorstring, startindex, endindex)`: Trả về chuỗi con bắt đầu từ `startindex` và kết thúc ngay trước `endindex`. Chỉ số bắt đầu từ 0 cho ký tự đầu tiên.
   - Ví dụ: `substr(${phone}, 0, 3)` trả về ba chữ số đầu của số điện thoại.

4. `concat(a, b, c, ...)`: Ghép các trường (và/hoặc chuỗi) lại với nhau.
   - Ví dụ: `concat(${firstname}, ' ', ${lastname})` trả về họ tên đầy đủ bằng cách kết hợp giá trị trong các trường `firstname` và `lastname`.

5. `linebreak()`: Trả về ký tự xuống dòng.
   - Ví dụ: `concat(${field1}, linebreak(), ${field2}, linebreak(), ${field3})` trả về danh sách ba giá trị trường với xuống dòng ở giữa.

6. `lower()`: Chuyển chuỗi thành chữ thường.
   - Ví dụ: `lower('Street Name')` trả về "street name".

7. `upper()`: Chuyển chuỗi thành chữ hoa.
   - Ví dụ: `upper('Street Name')` trả về "STREET NAME".

### Hàm select_one và select_multiple

1. `count-selected(field)`: Trả về số mục đã chọn trong trường `select_multiple`.
   - Ví dụ: `count-selected(.) = 3` có thể dùng làm biểu thức constraint để đảm bảo đúng ba lựa chọn được chọn.

2. `selected(field, value)`: Trả về true hoặc false tùy thuộc vào việc giá trị đã chỉ định có được chọn trong trường `select_one` hoặc `select_multiple` hay không.
   - Ví dụ: `selected(${color}, 'Blue')` có thể dùng làm biểu thức relevant để chỉ hiển thị nhóm hoặc trường nếu người trả lời chọn "Blue".
   - Lưu ý: Tham số thứ hai phải luôn chỉ định giá trị lựa chọn, không phải nhãn. Dùng giá trị từ cột value trong bảng tính choices.

3. `selected-at(field, number)`: Trả về mục được chọn tại vị trí chỉ định trong trường `select_multiple`. Số 0 trả về mục đầu tiên; số 1 trả về mục thứ hai, v.v.
   - Ví dụ: `selected-at(${fruits}, 0) = 'Apple'` có thể dùng làm biểu thức relevant để chỉ hiển thị nếu lựa chọn đầu tiên là "Apple".
   - Lưu ý: Giá trị trả về là giá trị lựa chọn, không phải nhãn.

4. `choice-label(field, value)`: Trả về nhãn cho một lựa chọn trong trường `select_one` hoặc `select_multiple`, như được định nghĩa trong bảng tính choices.
   - Ví dụ 1: `choice-label(${country}, ${country})` trả về nhãn của lựa chọn đang được chọn trong trường `country`.
   - Ví dụ 2: `choice-label(${languages}, selected-at(${languages}, 0))` trả về nhãn của lựa chọn đầu tiên trong trường `languages`.
   - Lưu ý: Hàm này lấy nhãn lựa chọn, không phải giá trị.

### Hàm cho trường lặp

Trong rtSurvey, nếu bạn muốn hỏi cùng một câu hỏi nhiều lần, bạn có thể đặt trường trong nhóm lặp. Điều này tạo ra nhiều phiên bản của cùng một trường. Các hàm sau giúp làm việc với các trường lặp và dữ liệu lặp chúng tạo ra.

1. `join(string, repeatedfield)`: Với trường trong nhóm lặp, tạo danh sách các giá trị phân cách bởi chuỗi. Tham số đầu tiên chỉ định ký tự phân cách.
   - Ví dụ: `join(', ', ${member_name})` tạo danh sách tên phân cách bởi dấu phẩy từ tất cả tên đã nhập.

2. `join-if(string, repeatedfield, expression)`: Hoạt động giống `join()`, nhưng kiểm tra từng phiên bản bằng biểu thức. Nếu biểu thức là false, mục đó bị loại.
   - Ví dụ: `join-if(', ', ${member_name}, ${age} >= 18)` tạo danh sách tên người lớn phân cách bởi dấu phẩy.

3. `count(repeatgroup)`: Trả về số lần nhóm lặp đã lặp lại.
   - Ví dụ: `count(${groupname})` trả về số phiên bản của nhóm.

4. `count-if(repeatgroup, expression)`: Hoạt động giống `count()`, nhưng kiểm tra từng phiên bản bằng biểu thức.
   - Ví dụ: `count-if(${members}, ${age} >= 18)` trả về số thành viên là người lớn.

5. `sum(repeatedfield)`: Với trường trong nhóm lặp, tính tổng tất cả các giá trị.
   - Ví dụ: `sum(${loan_amount})` trả về tổng giá trị tất cả các khoản vay.

6. `sum-if(repeatedfield, expression)`: Hoạt động giống `sum()`, nhưng kiểm tra từng phiên bản bằng biểu thức.
   - Ví dụ: `sum-if(${loan_amount}, ${loan_amount} > 500)` trả về tổng các khoản vay trên 500.

7. `min(repeatedfield)`: Với trường trong nhóm lặp, tính giá trị nhỏ nhất.
   - Ví dụ: `min(${member_age})` trả về tuổi thành viên nhỏ nhất.

8. `min-if(repeatedfield, expression)`: Hoạt động giống `min()`, nhưng kiểm tra từng phiên bản bằng biểu thức.
   - Ví dụ: `min-if(${member_age}, ${member_age} >= 18)` trả về tuổi người lớn trẻ nhất.

9. `max(repeatedfield)`: Với trường trong nhóm lặp, tính giá trị lớn nhất.
   - Ví dụ: `max(${member_age})` trả về tuổi thành viên lớn nhất.

10. `max-if(repeatedfield, expression)`: Hoạt động giống `max()`, nhưng kiểm tra từng phiên bản bằng biểu thức.
    - Ví dụ: `max-if(${member_age}, ${member_age} >= 18)` trả về tuổi người lớn nhất trong nhóm.

11. `index()`: Được gọi trong nhóm lặp, trả về số thứ tự (bắt đầu từ 1) của phiên bản hiện tại.
    - Ví dụ: `index()` trong nhóm lặp trả về 1 cho phiên bản đầu tiên, 2 cho phiên bản thứ hai, v.v.

12. `indexed-repeat(repeatedfield, repeatgroup, index)`: Tham chiếu trường trong nhóm lặp từ bên ngoài. Tham số đầu chỉ định trường lặp, tham số hai chỉ định nhóm lặp, tham số ba chỉ định số thứ tự phiên bản.
    - Ví dụ 1: `indexed-repeat(${name}, ${names}, 1)` trả về tên đầu tiên khi trường `name` nằm trong nhóm lặp "names".
    - Ví dụ 2: `indexed-repeat(${name}, ${names}, index())` lấy tên tương ứng với phiên bản nhóm lặp hiện tại.

13. `rank-index(index, repeatedfield)`: Tính thứ hạng theo thứ tự của phiên bản lặp cụ thể để dùng bên ngoài nhóm lặp. Thứ hạng 1 cho phiên bản có giá trị cao nhất. Trả về 999 nếu chỉ số không hợp lệ.
    - Ví dụ: `rank-index(1, ${random_draw})` tính thứ hạng của phiên bản đầu tiên so với các phiên bản khác.

14. `rank-index-if(index, repeatedfield, expression)`: Hoạt động giống `rank-index()`, nhưng kiểm tra từng phiên bản bằng biểu thức. Trả về 999 nếu phiên bản bị loại do không thỏa biểu thức.
    - Ví dụ: `rank-index-if(1, ${age}, ${age} >= 18)` tính thứ hạng tuổi trong nhóm người lớn.

### Hàm số học

{{< table >}}
| Toán tử | Phép toán | Ví dụ | Kết quả |
|---------|-----------|-------|---------|
| `+` | Cộng | 1 + 1 | 2 |
| `-` | Trừ | 3 - 2 | 1 |
| `*` | Nhân | 3 * 2 | 6 |
| `div` | Chia | 10 div 2 | 5 |
| `mod` | Chia lấy dư | 9 mod 2 | 1 |
{{< /table >}}

rtSurvey hỗ trợ các hàm số học, bao gồm:
- `number(field)`: Chuyển đổi giá trị trường sang số.
  - Ví dụ: `number('34.8')` = 34.8

- `int(field)`: Chuyển đổi giá trị trường sang số nguyên.
  - Ví dụ: `int('39.2')` = 39

- `min(field1, ..., fieldx)`: Trả về giá trị nhỏ nhất trong các trường được truyền vào.
  - Ví dụ: `min(${father_age}, ${mother_age})` trả về tuổi của bố hoặc mẹ, tùy theo ai trẻ hơn.

- `max(field1, ..., fieldx)`: Trả về giá trị lớn nhất trong các trường được truyền vào.
  - Ví dụ: `max(${father_age}, ${mother_age})` trả về tuổi của bố hoặc mẹ, tùy theo ai lớn hơn.

- `format-number(field)`: Định dạng giá trị trường số nguyên hoặc thập phân theo cài đặt ngôn ngữ người dùng.
  - Ví dụ: `format-number(${income})` có thể định dạng "120000" thành "120,000".

- `round(field, digits)`: Làm tròn giá trị trường số đến số chữ số thập phân chỉ định.
  - Ví dụ: `round(${interest_rate}, 2)`

- `abs(number)`: Trả về giá trị tuyệt đối của một số.

- `pow(base, exponent)`: Trả về giá trị của tham số đầu lũy thừa tham số hai.
  - Mỗi tham số có thể là trường, số hoặc biểu thức.

- `log10(fieldorvalue)`: Trả về logarit cơ số 10 của trường hoặc giá trị.

- `sin(fieldorvalue)`: Trả về sin của trường hoặc giá trị, tính bằng radian.

- `cos(fieldorvalue)`: Trả về cos của trường hoặc giá trị, tính bằng radian.

- `tan(fieldorvalue)`: Trả về tan của trường hoặc giá trị, tính bằng radian.

- `asin(fieldorvalue)`: Trả về arcsin của trường hoặc giá trị, tính bằng radian.

- `acos(fieldorvalue)`: Trả về arccos của trường hoặc giá trị, tính bằng radian.

- `atan(fieldorvalue)`: Trả về arctan của trường hoặc giá trị, tính bằng radian.

- `atan2(x, y)`: Trả về góc tính bằng radian của điểm (x, y) so với trục x dương. Kết quả trong khoảng -pi() đến pi().

- `sqrt(fieldorvalue)`: Trả về căn bậc hai không âm của trường hoặc giá trị.

- `exp(x)`: Trả về giá trị e^x.

- `pi()`: Trả về giá trị số pi.

### Hàm ngày và giờ

{{% alert icon=" " context="warning" %}}
Giá trị ngày trong rtSurvey được lưu dưới dạng chuỗi `YYYY-MM-DD`. Giá trị datetime được lưu dưới dạng chuỗi ISO 8601 (`YYYY-MM-DDTHH:MM:SS`). Dùng `decimal-date-time()` để chuyển đổi sang số cho phép tính số học (ví dụ: tính khoảng thời gian).
{{% /alert %}}

1. `today()`: Trả về ngày hôm nay dưới dạng chuỗi `YYYY-MM-DD`. Được đánh giá một lần khi biểu mẫu mở.
   - Ví dụ: `today()` → `'2024-03-15'`
   - Dùng phổ biến: cột `default` để điền sẵn ngày hôm nay, hoặc trong `relevant`/`constraint` để so sánh với trường ngày.

2. `now()`: Trả về ngày và giờ hiện tại dưới dạng chuỗi ISO 8601. Được đánh giá mỗi lần biểu thức được tính.
   - Ví dụ: `now()` → `'2024-03-15T14:32:00.000+03:00'`
   - Dùng phổ biến: Ghi lại dấu thời gian chính xác của một sự kiện cụ thể trong khảo sát.

3. `date(value)`: Chuyển đổi giá trị (chuỗi hoặc số) thành chuỗi ngày.
   - Ví dụ: `date('2024-03-15')` → `'2024-03-15'`

4. `date-time(value)`: Chuyển đổi giá trị thành chuỗi datetime.
   - Ví dụ: `date-time(${event_timestamp})`

5. `decimal-date-time(value)`: Chuyển đổi chuỗi ngày hoặc datetime thành số thập phân đại diện cho mili giây kể từ Unix epoch chia cho 86400000 (tức là số ngày phân số kể từ 1970-01-01). Dùng để thực hiện tính toán số học trên ngày.
   - Ví dụ: Khoảng thời gian tính theo ngày giữa hai ngày:
     `decimal-date-time(${end_date}) - decimal-date-time(${start_date})`
   - Ví dụ: Khoảng thời gian tính theo phút giữa hai datetime:
     `(decimal-date-time(${end_time}) - decimal-date-time(${start_time})) * 1440`

6. `format-date(date, format)`: Định dạng giá trị ngày theo chuỗi mẫu.
   - Mã định dạng: `%Y` (năm 4 chữ số), `%y` (năm 2 chữ số), `%m` (tháng 01–12), `%d` (ngày 01–31), `%a` (tên ngày viết tắt), `%b` (tên tháng viết tắt)
   - Ví dụ: `format-date(today(), '%d/%m/%Y')` → `'15/03/2024'`
   - Ví dụ: `format-date(${dob}, '%B %d, %Y')` → `'March 15, 1990'`

7. `format-date-time(datetime, format)`: Định dạng giá trị datetime theo chuỗi mẫu. Chấp nhận tất cả mã `format-date` cộng thêm:
   - `%H` (giờ 00–23), `%h` (giờ 01–12), `%M` (phút 00–59), `%S` (giây 00–59), `%3` (mili giây), `%P` (SA/CH)
   - Ví dụ: `format-date-time(now(), '%d/%m/%Y %H:%M')` → `'15/03/2024 14:32'`
   - Ví dụ: `format-date-time(${event_time}, '%I:%M %p')` → `'02:32 PM'`

---

### Hàm boolean

1. `boolean(value)`: Chuyển đổi bất kỳ giá trị nào thành boolean. Trả về `true` cho chuỗi không rỗng, số khác không, và `true`; trả về `false` cho chuỗi rỗng, `0`, và `false`.
   - Ví dụ: `boolean(${name})` trả về `true` nếu `name` không rỗng.

2. `boolean-from-string(string)`: Trả về `true` nếu chuỗi là `'1'` hoặc `'true'` (không phân biệt hoa thường); trả về `false` trong trường hợp khác.
   - Ví dụ: `boolean-from-string(${enabled_flag})` — hữu ích khi trường lưu `'true'`/`'false'` dưới dạng văn bản.

3. `true()`: Trả về giá trị boolean `true`.
   - Ví dụ: Trong cột `required`, `true()` tương đương với `yes`.

4. `false()`: Trả về giá trị boolean `false`.
   - Ví dụ: `if(${skip_section} = 'yes', false(), true())` — đặt required động.

5. `not(expression)`: Trả về phủ định logic của biểu thức. Trả về `true` nếu biểu thức là false, và ngược lại.
   - Ví dụ: `not(${consent} = 'yes')` — hiển thị cảnh báo khi đồng ý KHÔNG được cho.
   - Ví dụ: `not(selected(${issues}, 'none'))` — chỉ yêu cầu chi tiết khi "none" không được chọn.

---

### Hàm chuỗi bổ sung

1. `starts-with(string, prefix)`: Trả về `true` nếu `string` bắt đầu bằng `prefix`.
   - Ví dụ: `starts-with(${phone}, '+84')` kiểm tra nếu số điện thoại bắt đầu bằng mã quốc gia Việt Nam.

2. `contains(string, substring)`: Trả về `true` nếu `string` chứa `substring`.
   - Ví dụ: `contains(${email}, '@')` kiểm tra địa chỉ email có ký tự `@`.
   - Ví dụ: `contains(${notes}, 'urgent')` kích hoạt câu hỏi tiếp theo nếu ghi chú đề cập đến "urgent".

3. `substring-before(string, needle)`: Trả về phần của `string` xuất hiện trước lần xuất hiện đầu tiên của `needle`.
   - Ví dụ: `substring-before(${full_name}, ' ')` trích xuất từ đầu tiên (tên).

4. `substring-after(string, needle)`: Trả về phần của `string` xuất hiện sau lần xuất hiện đầu tiên của `needle`.
   - Ví dụ: `substring-after(${email}, '@')` trích xuất phần tên miền của địa chỉ email.

5. `normalize-space(string)`: Loại bỏ khoảng trắng đầu/cuối và thu gọn tất cả chuỗi khoảng trắng nội tại thành một dấu cách.
   - Ví dụ: `normalize-space(${name})` — làm sạch tên có thể đã được nhập với khoảng trắng thừa.

6. `translate(string, search_chars, replace_chars)`: Thay thế từng ký tự trong `string` xuất hiện trong `search_chars` bằng ký tự tương ứng trong `replace_chars`. Các ký tự trong `search_chars` không có ký tự tương ứng trong `replace_chars` sẽ bị xóa.
   - Ví dụ: `translate(${phone}, ' -()', '')` loại bỏ dấu cách, gạch ngang và dấu ngoặc khỏi số điện thoại.

---

### Hàm toán học bổ sung

1. `floor(number)`: Trả về số nguyên lớn nhất nhỏ hơn hoặc bằng `number` (làm tròn về âm vô cùng).
   - Ví dụ: `floor(4.9)` = 4, `floor(-2.1)` = -3

2. `ceiling(number)`: Trả về số nguyên nhỏ nhất lớn hơn hoặc bằng `number` (làm tròn về dương vô cùng).
   - Ví dụ: `ceiling(4.1)` = 5, `ceiling(-2.9)` = -2

3. `random()`: Trả về số thập phân ngẫu nhiên từ 0.0 (bao gồm) đến 1.0 (không bao gồm). Thường dùng trong trường `calculate` để gán giá trị ngẫu nhiên.
   - Ví dụ: `random()` → ví dụ `0.7341`
   - Ví dụ: `int(random() * 6) + 1` → số ngẫu nhiên từ 1–6 (tung xúc xắc)

4. `coalesce(a, b)`: Trả về `a` nếu `a` không rỗng; ngược lại trả về `b`. Hữu ích làm giá trị dự phòng khi trường có thể rỗng.
   - Ví dụ: `coalesce(${preferred_name}, ${full_name})` — dùng tên ưa thích nếu có, ngược lại dùng tên đầy đủ.

5. `once(value)`: Đánh giá `value` và lưu lại, nhưng chỉ khi trường hiện tại **rỗng**. Nếu trường đã có giá trị, `once()` trả về giá trị hiện tại không thay đổi. Điều này ngăn tính lại ghi đè đầu vào của người dùng.
   - Ví dụ: `once(today())` trong cột `default` đặt ngày hôm nay một lần và không cập nhật nếu người điều tra mở lại biểu mẫu.
   - Ví dụ: `once(uuid())` tạo UUID một lần và giữ ổn định qua các lần chỉnh sửa.

---

### Hàm địa lý

1. `area(geoshape_value)`: Tính **diện tích tính bằng mét vuông** của một geoshape (đa giác).
   - Tham số là giá trị trường geoshape theo định dạng `lat1 lon1 0 0; lat2 lon2 0 0; ...`
   - Ví dụ: `area(${field_boundary})` — tính diện tích thửa đất khảo sát tính bằng m².
   - Ví dụ: `round(area(${field_boundary}) div 10000, 2)` — chuyển sang hecta.

2. `distance(coordinates)`: Tính **tổng chiều dài đường đi tính bằng mét** của geotrace (đường), hoặc khoảng cách giữa hai geopoint.
   - Với geotrace: `distance(${route})` trả về tổng chiều dài đường đi tính bằng mét.
   - Với hai geopoint: `distance(concat(${point_a}, ' ', ${point_b}))` trả về khoảng cách giữa chúng.
   - Ví dụ: `round(distance(${road_trace}) div 1000, 3)` — chiều dài đường tính bằng km.

---

### Hàm xác thực

1. `regex(value, pattern)`: Trả về `true` nếu `value` khớp với biểu thức chính quy `pattern`. Dùng trong cột `constraint` để xác thực dựa trên mẫu.
   - Mẫu dùng cú pháp regex tiêu chuẩn (tập con POSIX ERE).
   - Ví dụ: `regex(., '^[0-9]{10}$')` — xác thực số 10 chữ số.
   - Ví dụ: `regex(., '^[A-Z]{2}[0-9]{6}$')` — xác thực định dạng số hộ chiếu (2 chữ hoa + 6 chữ số).
   - Ví dụ: `regex(., '^[^@]+@[^@]+\.[^@]{2,}$')` — kiểm tra định dạng email cơ bản.

2. `checklist(min, max, v1, v2, ...)`: Đánh giá danh sách biểu thức boolean và trả về `true` nếu số giá trị `true` nằm trong khoảng `min` đến `max` (bao gồm). Truyền `-1` cho `min` hoặc `max` để bỏ qua giới hạn đó.
   - Ví dụ: `checklist(2, 3, ${q1} = 'yes', ${q2} = 'yes', ${q3} = 'yes')` — đúng nếu chính xác 2 hoặc 3 trong ba điều kiện là true.
   - Ví dụ: `checklist(1, -1, ${smoke_alarm}, ${fire_ext}, ${emergency_plan})` — ít nhất một biện pháp an toàn phải là true.

3. `weighted-checklist(min, max, v1, w1, v2, w2, ...)`: Giống `checklist()`, nhưng mỗi giá trị có trọng số. Tổng trọng số của các giá trị `true` phải nằm trong khoảng `min` đến `max`.
   - Ví dụ: `weighted-checklist(10, -1, ${has_toilet}, 4, ${has_sink}, 3, ${has_shower}, 5)` — tổng trọng số của các tiện nghi có mặt phải ít nhất là 10.

---

### Hàm tiện ích

1. `uuid()`: Tạo UUID ngẫu nhiên (định dạng RFC 4122 v4) dưới dạng chuỗi.
   - Ví dụ: `uuid()` → `'a3f8b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c'`
   - Thường dùng với `once()` để tạo ID duy nhất ổn định: `once(uuid())`

2. `version()`: Trả về giá trị thuộc tính `version` của biểu mẫu được đặt trong bảng tính settings.
   - Ví dụ: `version()` → `'3.1'`
   - Hữu ích trong trường `calculate` để nhúng phiên bản biểu mẫu vào dữ liệu xuất.

3. `position()`: Khi được gọi trong **nhóm lặp**, trả về chỉ số (bắt đầu từ 1) của phiên bản lặp hiện tại.
   - Ví dụ: `position()` trong phiên bản đầu tiên trả về `1`, phiên bản thứ hai trả về `2`, v.v.
   - Xem thêm: `index()` (bí danh), `indexed-repeat()` để tham chiếu giá trị lặp từ bên ngoài nhóm.

4. `thousandsep(length, separator, value)`: Định dạng số với ký tự phân cách hàng nghìn. `length` là độ dài chuỗi tối thiểu (đệm bằng dấu cách nếu ngắn hơn), `separator` là ký tự dùng (ví dụ: `','`), và `value` là số cần định dạng.
   - Ví dụ: `thousandsep(0, ',', 1234567)` → `'1,234,567'`
   - Ví dụ: `thousandsep(0, '.', ${income})` → định dạng thu nhập với dấu chấm làm ký tự phân cách hàng nghìn.

5. `substr-jsonpath(value, jsonpath)`: Trích xuất chuỗi con từ chuỗi JSON bằng biểu thức JSONPath.
   - Ví dụ: `substr-jsonpath(${api_response}, '$.data.name')` — trích xuất trường `name` từ chuỗi JSON lưu trong `api_response`.
   - Thường dùng cùng với `callapi()` để trích xuất giá trị cụ thể từ phản hồi API.
