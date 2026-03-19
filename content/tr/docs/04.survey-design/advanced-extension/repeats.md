---
title: "Gelişmiş Tekrarlar"
description: "Tekrar grupları için gelişmiş kalıplar: dinamik sayılar, iç içe tekrarlar, tekrar verilerini özetleme ve tekrarlar arasında değerlere referans verme."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 295
---

Bu sayfa, rtSurvey'de tekrar gruplarıyla çalışmak için gelişmiş kalıpları kapsar. Tekrar grubu kurmanın temellerini görmek için [Gruplama ve Tekrarlar](../repeats) sayfasına bakın.

---

## Dinamik tekrar sayısı

Varsayılan olarak sayımcı kaç kez tekrarlayacağına karar verir. `repeat_count` kullanarak tekrarlama sayısını sabitleyebilirsiniz:

| type | name | label | repeat_count |
|------|------|-------|--------------|
| begin_repeat | household_members | Hane üyesi | `${num_members}` |
| text | member_name | Üye adı | |
| integer | member_age | Yaş | |
| end_repeat | | | |

Tekrar, daha önce formda toplanan `num_members` sayısı kadar tam olarak çalışır. Sayımcı örnek ekleyemez veya kaldıramaz.

---

## Endekslenmiş erişim: `indexed-repeat()`

Tekrar grubunun **dışından** belirli bir tekrar örneğinin alan değerine erişmek için `indexed-repeat(repeatedField, repeatGroup, index)` kullanın:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | first_name | | `indexed-repeat(${member_name}, ${household_members}, 1)` |
| calculate | second_name | | `indexed-repeat(${member_name}, ${household_members}, 2)` |

Bu, tekrardan sonra özet alanlar oluşturmak veya "birincil" üyenin verilerine referans vermek için kullanışlıdır.

---

## Geçerli örnek pozisyonu: `index()`

Bir tekrar grubu içinde, `index()` geçerli örneğin 1 tabanlı pozisyonunu döndürür. Her tekrarı etiketlemek veya benzersiz tanımlayıcılar oluşturmak için kullanın:

| type | name | label |
|------|------|-------|
| begin_repeat | plots | Arazi |
| note | plot_label | Arazi numarası ${index()} |
| text | plot_id | Arazi Kimliği |
| end_repeat | | |

---

## Aynı örnekteki alanlara referans verme

Bir tekrar içinde, **aynı tekrar örneğindeki** başka bir alana referans vermek için `${fieldname}` kullanın. Aynı döngü içinde `indexed-repeat()` gerekmez:

| type | name | label | relevant |
|------|------|-------|----------|
| begin_repeat | members | Üye | |
| text | member_name | Ad | |
| integer | member_age | Yaş | |
| text | school_name | Okul adı | `${member_age} < 18` |
| end_repeat | | | |

---

## Tekrar içinden üst alanlara referans verme

Tekrar grubunun dışında (üstünde) bulunan alanlar `${fieldname}` ile normal şekilde referans alınabilir:

| type | name | label |
|------|------|-------|
| text | village | Köy adı |
| begin_repeat | plots | Tarım arazisi |
| note | plot_context | ${village} köyündeki araziler |
| end_repeat | | |

---

## Tekrar verilerini özetleme

Özetlemek için tekrar grubunun **dışında** tekrar toplama fonksiyonlarını kullanın:

| Fonksiyon | Örnek | Açıklama |
|----------|---------|-------------|
| `count(group)` | `count(${household_members})` | Örnek sayısı |
| `sum(field)` | `sum(${loan_amount})` | Sayısal bir alanın toplamı |
| `min(field)` | `min(${member_age})` | Minimum değer |
| `max(field)` | `max(${member_age})` | Maksimum değer |
| `join(sep, field)` | `join(', ', ${member_name})` | Virgülle ayrılmış liste |
| `count-if(group, expr)` | `count-if(${members}, ${member_age} < 18)` | Koşullu sayı |
| `sum-if(field, expr)` | `sum-if(${loan_amount}, ${loan_amount} > 500)` | Koşullu toplam |
| `join-if(sep, field, expr)` | `join-if(', ', ${name}, ${age} >= 18)` | Koşullu birleştirme |

### Örnek: Hane özeti

| type | name | label | calculation |
|------|------|-------|-------------|
| integer | num_members | Kaç üye var? | |
| begin_repeat | members | Üye | `${num_members}` |
| text | member_name | Ad | |
| integer | member_age | Yaş | |
| end_repeat | | | |
| calculate | total_members | | `count(${members})` |
| calculate | children_count | | `count-if(${members}, ${member_age} < 18)` |
| calculate | adult_names | | `join-if(', ', ${member_name}, ${member_age} >= 18)` |
| note | summary | ${total_members} üye; ${children_count} 18 yaşından küçük. Yetişkinler: ${adult_names} | |

---

## İç içe tekrarlar

Bir tekrar grubu başka bir tekrar grubu içerebilir. Bunu dikkatli kullanın — iç içe tekrarlar karmaşıklık ekler ve sayımcılar için kafa karıştırıcı olabilir.

| type | name | label |
|------|------|-------|
| begin_repeat | households | Hane |
| text | hh_id | Hane Kimliği |
| begin_repeat | hh_members | Üye |
| text | member_name | Üye adı |
| end_repeat | | |
| end_repeat | | |

İç tekrardaki bir alana dış tekrardan referans vermek için `${fieldname}` kullanın — en yakın eşleşen ataya çözümlenir:

`hh_members` tekrarı içinde, `${hh_id}` **geçerli** hanenin kimliğini döndürür, tüm hanelerin kimliğini değil.

---

## Tekrar gruplarındaki sıralama: `rank-index()`

Tekrar içinde bir `rank` alanı varsa, belirli bir örneğin sıra sıralamasını dışarıdan almak için dışarıdan `rank-index(instanceNumber, repeatedField)` kullanın:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | top_scorer | | `rank-index(1, ${score})` |

`rank-index(1, ${score})`, en yüksek puanın örnek indeksini döndürür.

---

## En İyi Uygulamalar

1. Tekrarlama sayısı önceden biliniyorsa her zaman `repeat_count` kullanın — sayımcıların yanlışlıkla örnek eklemesini veya kaldırmasını önler.
2. Tekrar gruplarını odaklı tutun — örnek başına 20'den fazla sorusu olan bir tekrar gezinmesi zordur.
3. Tekrar gruplarını net biçimde adlandırın (örn. `household_members`, `repeat1` değil) — ad fonksiyon çağrılarında ve dışa aktarılan veride görünür.
4. Performansı doğrulamak için beklenen maksimum örnek sayısıyla test edin.
5. Tüm alanları tek bir ekranda göstermek için tekrar grubu üzerinde `field-list` görünümü kullanın (mobil).

---

## Sınırlamalar

- `indexed-repeat()` geçerli bir indeks (1'den örnek sayısına kadar) gerektirir — aralık dışı indeksler boş döndürür.
- 2 düzeyin ötesinde iç içe tekrarlar önerilmez ve bazı istemcilerde görüntüleme sorunlarına neden olabilir.
- Toplama fonksiyonları (`sum`, `count`, vb.) tüm tekrar grubu üzerinde çalışır — `*-if` varyantları olmadan örnek alt kümesini toplayamazsınız.
