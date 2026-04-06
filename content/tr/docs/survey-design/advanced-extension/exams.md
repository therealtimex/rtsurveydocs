---
title: "Sınavlar"
description: "Sınav özelliği, bir ankete doğru ve yanlış cevaplar için isteğe bağlı ses geri bildirimi olan zamanlanmış bir quiz modu ekler."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 298
---

**Sınav** özelliği, bir anketi zamanlanmış bir quiz'e dönüştürür. Katılımcıya bir geri sayım zamanlayıcısı görüntülenir ve anket, bitirdiklerinde kalan süreyi kaydeder. İsteğe bağlı olarak, doğru ve yanlış cevaplar için sesler çalabilir.

Bu, bilgi değerlendirmeleri, okuryazarlık testleri, saha personeli yeterlilik kontrolleri ve görev süresinin anlamlı veri olduğu herhangi bir anket için kullanışlıdır.

---

## `check-exam()` fonksiyonu

Sınavı, formun başına yerleştirilen bir `calculate` alanının **`calculation`** sütunundaki `check-exam()` kullanarak yapılandırın:

```
check-exam(examTime, questionToStoreRemainingTime)
check-exam(examTime, questionToStoreRemainingTime, rightSound, wrongSound, excludeQuestion)
```

### Parametreler

| # | Parametre | Açıklama |
|---|-----------|-------------|
| 1 | `examTime` | Saniye cinsinden toplam sınav süresi |
| 2 | `questionToStoreRemainingTime` | Sınav sona erdiğinde kalan süreyi depolayacak `calculate` veya `integer` alanının `name`'i |
| 3 | `rightSound` | *(İsteğe bağlı)* Doğru cevap verildiğinde çalınacak ses dosyasının adı (forma medya dosyası olarak ekleyin) |
| 4 | `wrongSound` | *(İsteğe bağlı)* Yanlış cevap verildiğinde çalınacak ses dosyasının adı |
| 5 | `excludeQuestion` | *(İsteğe bağlı)* Sınav zamanlayıcısından çıkarılacak alan adlarının virgülle ayrılmış listesi (örn. `'intro_note,consent'`) |

---

## Temel kurulum

### Adım 1: Sınav alanlarını ekle

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | exam_config | | `check-exam(600, 'remaining_time')` |
| calculate | remaining_time | | |

`exam_config`, 600 saniyelik (10 dakika) zamanlayıcıyı tetikler. `remaining_time`, katılımcı bitirdiğinde otomatik olarak doldurulur.

### Adım 2: Sorularınızı ekleyin

Sınav zamanlayıcısı, `excludeQuestion`'da listelenenler dışındaki formdaki tüm soruları kapsar.

| type | name | label |
|------|------|-------|
| select_one yesno | q1 | Kenya'nın başkenti Nairobi'dir. Doğru mu yanlış mı? |
| select_one choices | q2 | Kanı vücutta hangi organ pompalar? |
| select_one choices | q3 | Deniz seviyesinde su 100°C'de kaynar. Doğru mu yanlış mı? |

### Adım 3: Kalan süreyi depolayın

Parametre 2'de adlandırılan alan (`remaining_time`), katılımcı gönderdiğinde kalan saniye sayısına otomatik olarak ayarlanır. `0` değeri, sürenin dolduğu anlamına gelir; yüksek bir değer hızlı bitirdikleri anlamına gelir.

---

## Ses geri bildirimi ile

Ses dosyalarını forma ekleyin (medya ekleri olarak) ve ardından referans alın:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | exam_config | | `check-exam(300, 'remaining_time', 'correct.mp3', 'wrong.mp3')` |

- `correct.mp3`, katılımcı doğru cevabı seçtiğinde çalar
- `wrong.mp3`, katılımcı yanlış cevabı seçtiğinde çalar

{{% alert icon=" " context="warning" %}}
Ses dosyaları forma medya dosyaları olarak eklenmeli ve dosya adı tam olarak eşleşmelidir (uzantı dahil büyük/küçük harf duyarlı).
{{% /alert %}}

---

## Soruları zamanlayıcıdan çıkarma

Sınavdan çıkarılacak alan adlarının virgülle ayrılmış listesini geçin (örn. giriş notları veya onay soruları):

```
check-exam(300, 'remaining_time', '', '', 'intro_note,consent_ack,section_header')
```

Sese ihtiyaç duymuyorsanız ama çıkarmalara ihtiyaç duyuyorsanız `rightSound` ve `wrongSound`'u boş dizeler `''` olarak bırakın.

---

## Tam örnek

| type | name | label | calculation |
|------|------|-------|-------------|
| note | intro | Sağlık bilgisi değerlendirmesine hoş geldiniz. Tüm soruları yanıtlamak için 5 dakikanız var. | |
| trigger | start_ack | Başlamaya hazır olduğunuzda Tamam'a dokunun. | |
| calculate | exam_config | | `check-exam(300, 'remaining_time', 'correct.mp3', 'wrong.mp3', 'intro,start_ack')` |
| calculate | remaining_time | | |
| select_one yesno | q1 | El yıkama hastalığın yayılmasını önler. | |
| select_one yesno | q2 | Günde en az 2 litre su içmelisiniz. | |
| select_one yesno | q3 | Sıtma bir virüsten kaynaklanır. | |

---

## En İyi Uygulamalar

1. Başlamadan önce katılımcıları zaman sınırı hakkında her zaman bilgilendirin — `check-exam()` alanından önce bir `note` veya `trigger` kullanın.
2. `excludeQuestion` parametresini kullanarak giriş notlarını ve onay sorularını zamanlayıcıdan çıkarın.
3. Zaman aşımlarını tespit etmek için `remaining_time`'ı takip eden bir hesaplamada kullanın: `if(${remaining_time} = 0, 'Zaman doldu', 'Tamamlandı')`.
4. Soru sayısını izin verilen süreyle orantılı tutun — çoğu bilgi değerlendirmesi için soru başına 2–3 dakika makul bir temel çizgidir.
5. Dağıtımdan önce ses dosyalarını gerçek cihazda test edin — ses oynatma Android sürümleri ve tarayıcılar arasında farklılık gösterir.

## Sınırlamalar

- Zamanlayıcı yalnızca görüntüleme amaçlıdır — süre dolduğunda form otomatik olarak gönderilmez; katılımcı yine de manuel olarak göndermek zorundadır.
- Ses geri bildirimi, cihaz sesinin açık ve sessiz modda olmadığını gerektirir.
- Sınav özelliği bir rtSurvey uzantısıdır ve standart XLSForm spesifikasyonunun bir parçası değildir.
