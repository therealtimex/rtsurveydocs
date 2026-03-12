---
title: "Hàm (Functions)"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 293
---

### Các hàm chuỗi (String functions)

{{% alert icon=" " context="warning" %}}
Khi làm việc với các chuỗi bên trong biểu thức, điều quan trọng là phải sử dụng dấu ngoặc đơn ('') để bao quanh các chuỗi ký tự. Tuy nhiên, có một ngoại lệ khi bạn muốn bao gồm dấu ngoặc đơn bên trong một chuỗi ký tự. Trong những trường hợp như vậy, bạn có thể sử dụng dấu ngoặc kép ("") để bao quanh toàn bộ chuỗi.

Ví dụ:
- Đúng: if(${yesno} = 1, "a string with 'single quotes' in it", "no single quotes here")
- Sai: if(${yesno} = 1, 'a string with 'single quotes' in it', 'no single quotes here')

Liên quan đến các dấu ngoặc thông minh (smart quotes), điều quan trọng là phải nhận biết sự hiện diện của chúng, vì chúng có thể gây ra lỗi trong biểu thức. Nhiều trình chỉnh sửa văn bản phong phú tự động chuyển đổi các dấu ngoặc thẳng ("" hoặc '') thành các dấu ngoặc thông minh hoặc dấu ngoặc cong (“” hoặc ‘’), điều này có thể dẫn đến lỗi cú pháp hoặc hành vi không mong muốn. Để tránh điều này, hãy đảm bảo rằng bạn sử dụng nhất quán các dấu ngoặc thẳng ('') trong các biểu thức của mình.

Vui lòng cho tôi biết nếu bạn có bất kỳ câu hỏi nào khác hoặc cần hỗ trợ thêm!
{{% /alert %}}

rtSurvey hỗ trợ nhiều hàm khác nhau, bao gồm:

1. `string(field)`: Chuyển đổi một trường sang dạng chuỗi.
   - Ví dụ: `string(34.8)` sẽ được chuyển đổi thành `'34.8'`.

2. `string-length(field)`: Trả về độ dài của một trường chuỗi.
   - Ví dụ: `string-length(.) > 3 and string-length(.) < 10` có thể được sử dụng để đảm bảo trường hiện tại có độ dài từ 3 đến 10 ký tự.

3. `substr(fieldorstring, startindex, endindex)`: Trả về một chuỗi con bắt đầu tại `startindex` và kết thúc ngay trước `endindex`. Chỉ mục (index) bắt đầu từ 0 cho ký tự đầu tiên trong chuỗi.
   - Ví dụ: `substr(${phone}, 0, 3)` sẽ trả về ba chữ số đầu tiên của một số điện thoại.

4. `concat(a, b, c, ...)`: Nối các trường (và/hoặc các chuỗi) lại với nhau.
   - Ví dụ: `concat(${firstname}, ' ', ${lastname})` sẽ trả về họ tên đầy đủ bằng cách kết hợp các giá trị trong các trường `firstname` và `lastname`.

5. `linebreak()`: Trả về một ký tự xuống dòng.
   - Ví dụ: `concat(${field1}, linebreak(), ${field2}, linebreak(), ${field3})` sẽ trả về danh sách ba giá trị trường với các dấu xuống dòng ở giữa.

6. `lower()`: Chuyển đổi một chuỗi thành tất cả các ký tự viết thường.
   - Ví dụ: `lower('Street Name')` sẽ trả về "street name".

7. `upper()`: Chuyển đổi một chuỗi thành tất cả các ký tự viết hoa.
   - Ví dụ: `upper('Street Name')` sẽ trả về "STREET NAME".

### Các hàm cho select_one và select_multiple

1. `count-selected(field)`: Trả về số lượng mục đã được chọn trong một trường `select_multiple`.
   - Ví dụ: `count-selected(.) = 3` có thể được sử dụng làm biểu thức ràng buộc (`constraint`) để đảm bảo chính xác ba lựa chọn được chọn.

2. `selected(field, value)`: Trả về `true` hoặc `false` tùy thuộc vào việc giá trị đã chỉ định có được chọn trong trường `select_one` hoặc `select_multiple` hay không.
   - Ví dụ: `selected(${color}, 'Blue')` có thể được sử dụng làm biểu thức hiển thị (`relevance`) để chỉ hiển thị một nhóm hoặc trường nếu người trả lời chọn "Blue" là màu sắc yêu thích của họ.
   - Lưu ý: Tham số thứ hai phải luôn chỉ định giá trị lựa chọn (`value`), không phải nhãn lựa chọn (`label`). Sử dụng giá trị từ cột `value` trong bảng khảo sát `choices` của định nghĩa biểu mẫu.

3. `selected-at(field, number)`: Trả về mục được chọn tại vị trí đã chỉ định trong trường `select_multiple`. Khi số truyền vào là 0, nó sẽ trả về mục được chọn đầu tiên; khi số là 1, nó trả về mục được chọn thứ hai, và vân vân.
   - Ví dụ: `selected-at(${fruits}, 0) = 'Apple'` có thể được sử dụng làm biểu thức hiển thị để chỉ hiển thị một nhóm hoặc trường nếu lựa chọn đầu tiên được chọn là "Apple".
   - Lưu ý: Giá trị được trả về sẽ là giá trị lựa chọn (`value`), không phải nhãn lựa chọn (`label`). Sử dụng giá trị từ cột `value` trong bảng khảo sát `choices` của định nghĩa biểu mẫu.

4. `choice-label(field, value)`: Trả về nhãn (`label`) cho một lựa chọn của trường `select_one` hoặc `select_multiple`, như được định nghĩa trong bảng khảo sát `choices` của định nghĩa biểu mẫu.
   - Ví dụ 1: `choice-label(${country}, ${country})` sẽ trả về nhãn của lựa chọn đang được chọn trong trường tên là `country`.
   - Ví dụ 2: `choice-label(${languages}, selected-at(${languages}, 0))` sẽ trả về nhãn cho lựa chọn được chọn đầu tiên trong trường tên là `languages`.
   - Lưu ý: Hàm này lấy nhãn lựa chọn, không phải giá trị. Nó sử dụng cột `label` từ bảng khảo sát `choices` của định nghĩa biểu mẫu.

### Các hàm cho trường lặp (Repeated field functions)

Trong rtSurvey, nếu bạn muốn hỏi cùng một (các) câu hỏi nhiều lần, bạn có thể đặt một trường bên trong một nhóm lặp (`repeat group`). Điều này dẫn đến nhiều phiên bản của cùng một trường. Các hàm sau đây có thể giúp bạn làm việc với các trường lặp này và dữ liệu lặp mà chúng tạo ra. Xem chủ đề trợ giúp về các trường lặp để biết thêm chi tiết.

1. `join(string, repeatedfield)`: Đối với một trường bên trong một nhóm lặp, tạo ra một danh sách các giá trị được phân tách bằng chuỗi. Tham số đầu tiên chỉ định ký tự phân tách để sử dụng.
   - Ví dụ: `join(', ', ${member_name})` sẽ tạo ra một chuỗi danh sách tên được phân tách bằng dấu phẩy từ tất cả các tên đã nhập.

2. `join-if(string, repeatedfield, expression)`: Hoạt động chính xác giống như `join()`, ngoại trừ việc nó kiểm tra từng phiên bản trong nhóm lặp bằng biểu thức được cung cấp. Nếu biểu thức trả về `false`, mục đó sẽ bị loại khỏi đầu ra.
   - Ví dụ: `join-if(', ', ${member_name}, ${age} >= 18)` sẽ tạo ra một danh sách tên được phân tách bằng dấu phẩy của chỉ những thành viên là người lớn (những người có tuổi từ 18 trở lên).

3. `count(repeatgroup)`: Trả về số lần hiện tại mà một nhóm lặp đã lặp lại.
   - Ví dụ: `count(${groupname})` sẽ trả về số lượng phiên bản của nhóm.

4. `count-if(repeatgroup, expression)`: Hoạt động chính xác giống như `count()`, ngoại trừ việc nó kiểm tra từng phiên bản trong nhóm lặp bằng biểu thức được cung cấp. Nếu biểu thức trả về `false`, mục đó sẽ bị loại khỏi kết quả đếm.
   - Ví dụ: `count-if(${members}, ${age} >= 18)` sẽ trả về số lượng thành viên là người lớn dựa trên trường tuổi bên trong nhóm lặp "members".

5. `sum(repeatedfield)`: Đối with một trường bên trong một nhóm lặp, tính tổng của tất cả các giá trị.
   - Ví dụ: `sum(${loan_amount})` sẽ trả về tổng giá trị của tất cả các khoản vay.

6. `sum-if(repeatedfield, expression)`: Hoạt động chính xác giống như `sum()`, ngoại trừ việc nó kiểm tra từng phiên bản trong nhóm lặp bằng biểu thức được cung cấp. Nếu biểu thức trả về `false`, mục đó sẽ bị loại khỏi phép tính tổng.
   - Ví dụ: `sum-if(${loan_amount}, ${loan_amount} > 500)` sẽ trả về tổng giá trị của tất cả các khoản vay lớn hơn 500. Các khoản vay nhỏ hơn sẽ bị bỏ qua.

7. `min(repeatedfield)`: Đối với một trường bên trong một nhóm lặp, tính giá trị nhỏ nhất trong tất cả các giá trị.
   - Ví dụ: `min(${member_age})` sẽ trả về tuổi của thành viên trẻ nhất trong nhóm.

8. `min-if(repeatedfield, expression)`: Hoạt động chính xác giống như `min()`, ngoại trừ việc nó kiểm tra từng phiên bản trong nhóm lặp bằng biểu thức được cung cấp. Nếu biểu thức trả về `false`, mục đó sẽ bị loại khỏi phép tính giá trị nhỏ nhất.
   - Ví dụ: `min-if(${member_age}, ${member_age} >= 18)` sẽ trả về tuổi của người lớn trẻ nhất trong nhóm. Những người trẻ hơn 18 tuổi sẽ bị bỏ qua.

9. `max(repeatedfield)`: Đối với một trường bên trong một nhóm lặp, tính giá trị lớn nhất trong tất cả các giá trị.
   - Ví dụ: `max(${member_age})` sẽ trả về tuổi của thành viên lớn tuổi nhất trong nhóm.

10. `max-if(repeatedfield, expression)`: Hoạt động chính xác giống như `max()`, ngoại trừ việc nó kiểm tra từng phiên bản trong nhóm lặp bằng biểu thức được cung cấp. Nếu biểu thức trả về `false`, mục đó sẽ bị loại khỏi phép tính giá trị lớn nhất.
    - Ví dụ: `max-if(${member_age}, ${member_age} >= 18)` sẽ trả về tuổi của người lớn nhất trong nhóm. Những người trẻ hơn 18 tuổi sẽ bị bỏ qua.

11. `index()`: Được gọi bên trong một nhóm lặp, trả về số chỉ mục cho nhóm hoặc phiên bản hiện tại.
    - Ví dụ: `index()` khi được sử dụng bên trong một nhóm lặp sẽ trả về 1 cho phiên bản đầu tiên, 2 cho phiên bản thứ hai, và vân vân.

12. `indexed-repeat(repeatedfield, repeatgroup, index)`: Tham chiếu đến một trường hoặc nhóm nằm bên trong một nhóm lặp từ bên ngoài nhóm lặp đó. Tham số đầu tiên chỉ định trường hoặc nhóm lặp cần quan tâm, tham số thứ hai chỉ định tên nhóm lặp chứa trường đó, và tham số thứ ba chỉ định số thứ tự phiên bản trong nhóm lặp để lấy dữ liệu.
    - Ví dụ 1: `indexed-repeat(${name}, ${names}, 1)` sẽ trả về tên đầu tiên có sẵn khi trường `name` nằm bên trong một nhóm lặp trước đó tên là "names".
    - Ví dụ 2: `indexed-repeat(${name}, ${names}, index())` sẽ lấy tên tương ứng với số thứ tự phiên bản của nhóm lặp hiện tại.

13. `rank-index(index, repeatedfield)`: Hàm này tính toán thứ hạng (ordinal rank) của giá trị tại phiên bản lặp cụ thể của một trường để sử dụng bên ngoài nhóm lặp. Thứ hạng 1 được gán cho phiên bản có giá trị cao nhất, thứ hạng 2 cho phiên bản có giá trị cao tiếp theo, và cứ thế. Nếu bạn truyền một chỉ mục không hợp lệ hoặc chỉ mục của một phiên bản có giá trị không phải dạng số, giá trị 999 sẽ được trả về.
    - Ví dụ: `rank-index(1, ${random_draw})` tính toán thứ hạng của phiên bản đầu tiên dựa trên giá trị của trường `random_draw` của nó so với giá trị của các phiên bản khác.

14. `rank-index-if(index, repeatedfield, expression)`: Hàm này hoạt động tương tự như `rank-index()`, nhưng nó kiểm tra từng phiên bản trong nhóm lặp của trường lặp bằng biểu thức được cung cấp. Nếu biểu thức trả về `false`, mục đó sẽ bị loại khỏi tính toán thứ hạng. Chỉ mục được sử dụng dựa trên tập hợp đầy đủ các phiên bản trước khi đánh giá biểu thức cho từng phiên bản. Nếu bạn truyền một chỉ mục cho một phiên bản bị bỏ qua do không thỏa mãn biểu thức, nó được coi là chỉ mục không hợp lệ và giá trị 999 sẽ được trả về.
    - Ví dụ: `rank-index-if(1, ${age}, ${age} >= 18)` tính toán thứ hạng tuổi trong tập hợp những người lớn, chỉ xem xét các phiên bản có tuổi lớn hơn hoặc bằng 18.

### Các hàm số học (Number functions)

{{< table >}}
| Toán tử | Phép toán | Ví dụ | Kết quả ví dụ |
|----------|-----------|---------|----------------|
| `+` | Cộng (Addition) | 1 + 1 | 2 |
| `-` | Trừ (Subtraction) | 3 - 2 | 1 |
| `*` | Nhân (Multiplication) | 3 * 2 | 6 |
| `div` | Chia (Division) | 10 div 2 | 5 |
| `mod` | Chia lấy dư (Modulus) | 9 mod 2 | 1 |
{{< /table >}}

rtSurvey hỗ trợ các hàm số học, bao gồm:
- `number(field)`: Chuyển đổi giá trị của trường sang dạng số.
  - Ví dụ: `number('34.8')` = 34.8

- `int(field)`: Chuyển đổi giá trị của trường sang dạng số nguyên.
  - Ví dụ: `int('39.2')` = 39

- `min(field1, ..., fieldx)`: Trả về giá trị nhỏ nhất trong số các trường được truyền vào.
  - Ví dụ: `min(${father_age}, ${mother_age})` sẽ trả về tuổi của bố hoặc mẹ, tùy theo ai trẻ hơn.

- `max(field1, ..., fieldx)`: Trả về giá trị lớn nhất trong số các trường được truyền vào.
  - Ví dụ: `max(${father_age}, ${mother_age})` sẽ trả về tuổi của bố hoặc mẹ, tùy theo ai lớn tuổi hơn.

- `format-number(field)`: Định dạng giá trị của một trường số nguyên hoặc số thập phân theo cài đặt ngôn ngữ (locale) của người dùng.
  - Ví dụ: `format-number(${income})` Biểu thức này có thể định dạng "120000" thành "120,000".

- `round(field, digits)`: Làm tròn giá trị trường số đến số chữ số thập phân được chỉ định.
  - Ví dụ: `round(${interest_rate}, 2)`

- `abs(number)`: Trả về giá trị tuyệt đối của một số.
  
- `pow(base, exponent)`: Trả về giá trị của tham số thứ nhất lũy thừa với tham số thứ hai.
  - Mỗi tham số có thể là một trường, một số hoặc một biểu thức.

- `log10(fieldorvalue)`: Trả về logarit cơ số 10 của trường hoặc giá trị được truyền vào.

- `sin(fieldorvalue)`: Trả về sin của trường hoặc giá trị được truyền vào, tính bằng radian.
  
- `cos(fieldorvalue)`: Trả về cos của trường hoặc giá trị được truyền vào, tính bằng radian.

- `tan(fieldorvalue)`: Trả về tan của trường hoặc giá trị được truyền vào, tính bằng radian.

- `asin(fieldorvalue)`: Trả về arcsin của trường hoặc giá trị được truyền vào, tính bằng radian.

- `acos(fieldorvalue)`: Trả về arccos của trường hoặc giá trị được truyền vào, tính bằng radian.

- `atan(fieldorvalue)`: Trả về arctan của trường hoặc giá trị được truyền vào, tính bằng radian.

- `atan2(x, y)`: Trả về góc tính bằng radian được tạo bởi điểm có tọa độ (x, y) và trục x dương. Kết quả nằm trong khoảng -pi() đến pi().

- `sqrt(fieldorvalue)`: Trả về căn bậc hai không âm của trường hoặc giá trị được truyền vào.

- `exp(x)`: Trả về giá trị của e^x.

- `pi()`: Trả về giá trị của số pi.
