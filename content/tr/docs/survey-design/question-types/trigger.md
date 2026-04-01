---
title: "Trigger / Acknowledge"
description: "Trigger soruları, sayımcının devam etmeden önce açıkça onaylaması gereken bir ifade görüntüler."
icon: "check-circle"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 240
---

`trigger` (`acknowledge` olarak da bilinir) soru türü, **onay kutusuyla birlikte bir ifade** görüntüler. Sayımcının forma devam etmeden önce ifadeyi okuduğunu ve anladığını onaylamak için onay kutusunu işaretlemesi gerekir. Hiçbir veri değeri saklanmaz — yalnızca onay kutusunun işaretlenip işaretlenmediği kaydedilir.

## Temel XLSForm Tanımı

| type | name | label |
|------|------|-------|
| trigger | consent_ack | Katılımcı sözlü bilgilendirilmiş onay vermiştir. |

Veya `acknowledge` takma adını kullanarak:

| type | name | label |
|------|------|-------|
| acknowledge | consent_ack | Katılımcı sözlü bilgilendirilmiş onay vermiştir. |

`trigger` ve `acknowledge` eşdeğerdir — platformunuzun belgelerinde hangisi yer alıyorsa onu kullanın.

## Kullanım Alanları

Trigger/acknowledge soruları yaygın olarak şunlar için kullanılır:

1. **Bilgilendirilmiş onay** — hassas verileri kaydetmeden önce sayımcının onay aldığını onaylama
2. **Yumuşak uyarılar** — olağandışı bir değer hakkında uyarı ve devam etmeden önce açık onay isteme
3. **Kontrol listesi öğeleri** — fiziksel bir gözlemin tamamlandığını onaylama (örn. "Su kaynağını doğrudan gözlemledim")
4. **Talimatlar** — devam etmeden önce sayımcının bölüm düzeyinde bir talimatı kabul etmesini zorunlu kılma
5. **Kalite kontrolleri** — aykırı değerleri işaretleme ve sayımcının bunları doğrulamasını isteme

## Örnek Kullanım

### Onay kabulü

| type | name | label | required |
|------|------|-------|----------|
| trigger | consent | Katılımcı bu ankete katılmak için sözlü olarak bilgilendirilmiş onay vermiştir. | yes |

### Aykırı değerler için yumuşak uyarı

Yalnızca şüpheli bir değer girildiğinde tetikleyiciyi göstermek için `relevant` ifadesiyle birlikte kullanılır:

| type | name | label | relevant | required |
|------|------|-------|----------|----------|
| integer | children | Çocuk sayısı | | |
| trigger | children_confirm | ${children} çocuk girdiniz. Lütfen katılımcıyla doğrulayın ve onaylamak için Tamam'a dokunun. | `${children} > 10` | `${children} > 10` |

### Bölüm başında talimat kabulü

| type | name | label |
|------|------|-------|
| trigger | section_b_ack | B Bölümü: Tarımsal Arazi Kullanımı. Bu bölümdeki tüm soruları yalnızca hane reisine sorun. |

## Tetikleyiciyi zorunlu yapma

İşaretlenene kadar ilerlemeyi engellemek için `required: yes` ekleyin:

| type | name | label | required | required_message |
|------|------|-------|----------|------------------|
| trigger | safety_check | Tüm güvenlik ekipmanları mevcut ve işlevsel. | yes | Devam etmeden önce onaylamalısınız. |

## Koşullu görüntüleme

Tetikleyiciyi yalnızca bir koşul sağlandığında gösterin:

| type | name | label | relevant |
|------|------|-------|----------|
| select_one yesno | has_well | Hanenin kuyusu var mı? | |
| trigger | well_observation | Kuyu durumunu doğrudan gözlemlediğinizi onaylayın. | `${has_well} = 'yes'` |

## `note` ile fark

| | `note` | `trigger` |
|--|--------|-----------|
| Metin görüntüler | Evet | Evet |
| Etkileşim gerektirir | Hayır | Evet (işaretlenmeli) |
| Veri saklar | Hayır | Hayır (yalnızca Tamam/işaretlendi) |
| İlerlemeyi engelleyebilir | Hayır | Evet (`required` ile) |

## En İyi Uygulamalar

1. Tetikleyici etiketlerini kısa ve eyleme yönelik tutun — sayımcı saniyeler içinde okuyup onaylayabilmelidir.
2. Onay zorunlu olduğunda her zaman `required: yes` ekleyin.
3. Sayımcının onayladığına dair bir denetim izi gerektiğinde onay ve güvenlik kontrolleri için tetikleyicileri kullanın.
4. Tetikleyicinin yalnızca bir değerin doğrulanması gerektiğinde görünmesi için koşullu yumuşak uyarılarla `relevant` ile birleştirin.

## Sınırlamalar

- Tetikleyici alanlar anlamlı bir veri değeri saklamaz — yalnızca kutunun işaretlendiğini kaydeder.
- Tetikleyici widget'ı çoğu istemcide basit bir onay kutusu/düğme olarak görüntülenir; tam bir elektronik imza değildir.
