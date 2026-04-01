---
title: "Toán tử (Operators)"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 292
---

### Toán tử so sánh (Comparison operators)

{{< table >}}
Toán tử | Phép toán      | Ví dụ              | Kết quả ví dụ
-------- | -------------- | -------------------- | --------------
`=`        | Bằng (Equal)          | ${age} = 25     | true hoặc false
`!=`       | Không bằng (Not equal)      | ${age} != 25    | true hoặc false
`>`        | Lớn hơn (Greater-than)   | ${age} > 25     | true hoặc false
`>=`       | Lớn hơn hoặc bằng (Greater-than or equal) | ${age} >= 25 | true hoặc false
`<`        | Nhỏ hơn (Less-than)      | ${age} < 25     | true hoặc false
`<=`       | Nhỏ hơn hoặc bằng (Less-than or equal) | ${age} <= 25  | true hoặc false
{{< /table >}}

Trong các ví dụ trên, `${age}` đại diện cho giá trị của trường hiện tại, và toán tử được sử dụng để so sánh giá trị đó với 25. Ràng buộc (`constraint`) sẽ trả về kết quả là `true` hoặc `false`, tùy thuộc vào việc phép so sánh có được thỏa mãn hay không.

### Toán tử logic (Logical operators)

Các toán tử logic được sử dụng để kết hợp nhiều biểu thức trong các ràng buộc. Dưới đây là một số toán tử logic thường được sử dụng cùng với các phép toán và ví dụ:

Toán tử | Phép toán      | Ví dụ                                           
-------- | -------------- | --------------------------------------------------
`or`       | Trả về true nếu một trong các biểu thức là đúng          | ${age} = 3 or ${age} = 4
`and`      | Chỉ trả về true nếu cả hai biểu thức đều đúng    | ${age} > 3 and ${age} < 5
`not()`    | Trả về true nếu biểu thức không phải là đúng        | not(${age} > 3 and ${age} < 5)

Trong các ví dụ trên, `${age}` đại diện cho giá trị của trường hiện tại, và các toán tử logic được sử dụng để kết hợp các biểu thức. Ràng buộc sẽ được đánh giá là `true` hoặc `false` dựa trên các điều kiện đã chỉ định.

Ví dụ 1:
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` sẽ trả về `true` nếu tuổi là 3 hoặc 4." />}}

Ví dụ 2:
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` sẽ trả về `true` nếu tuổi nằm trong khoảng từ 3 đến 5 (không bao gồm 3 và 5)." />}}

Ví dụ 3:
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` sẽ trả về `true` nếu tuổi không nằm trong khoảng từ 3 đến 5." />}}
