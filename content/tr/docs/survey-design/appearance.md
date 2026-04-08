---
title: "Görünüm"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

rtSurvey'deki `appearance` sütunu, anketlerdeki soruların görsel sunumunu ve davranışını özelleştirmenize olanak tanır. Bu özellik kullanıcı deneyimini geliştirir ve veri toplama verimliliğini önemli ölçüde artırabilir. rtSurvey, standart XLSForm görünüm özniteliklerini destekler ve bunları ek seçeneklerle genişletir.

## Standart XLSForm Görünüm Öznitelikleri

rtSurvey aşağıdaki standart XLSForm görünüm özniteliklerini destekler:

| Görünüm Özniteliği | Soru Türleri | Açıklama |
|----------------------|----------------|-------------|
| multiline | text | Çok satırlı metin kutusu oluşturur (web istemcileri için en uygun) |
| minimal | select_one, select_multiple | Seçenekleri açılır menüde görüntüler |
| quick | select_one | Seçimden sonra bir sonraki soruya otomatik ilerler (yalnızca mobil) |
| no-calendar | date | Takvim görüntüsünü bastırır (yalnızca mobil) |
| month-year | date | Yalnızca ay ve yıl seçimine izin verir |
| year | date | Yalnızca yıl seçimine izin verir |
| horizontal-compact | select_one, select_multiple | Seçenekleri yatay olarak görüntüler (yalnızca web) |
| horizontal | select_one, select_multiple | Seçenekleri sütunlarda yatay olarak görüntüler (yalnızca web) |
| likert | select_one | Seçenekleri Likert ölçeği olarak sunar |
| compact | select_one, select_multiple | Seçenekleri minimum dolgu ile yan yana görüntüler |
| quickcompact | select_one | Kompakt görünümü otomatik ilerlemeyle birleştirir (yalnızca mobil) |
| field-list | groups | Tüm grubu tek ekranda görüntüler (yalnızca mobil) |
| label | select_one, select_multiple | Girişler olmadan seçenek etiketlerini gösterir |
| list-nolabel | select_one, select_multiple | Etiketler olmadan girişleri gösterir (`label` ile kullanın) |
| table-list | groups | Soruları tablo biçiminde görüntüler |
| signature | image | İmza yakalamayı etkinleştirir (yalnızca mobil) |
| draw | image | Serbest çizime izin verir (yalnızca mobil) |
| map, quick map | select_one, select_one_from_file | Harita özelliklerinden seçime olanak tanır |

## Görünüm Kullanımı için En İyi Uygulamalar

1. **Tutarlılık**: Tekdüze bir görünüm için anketiniz genelinde görünüm özniteliklerini tutarlı biçimde kullanın.
2. **Mobil ve Web**: Görünümlerin farklı cihaz ve platformlarda nasıl görüneceğini göz önünde bulundurun.
3. **Performans**: Form yüklemesini yavaşlatabilecek görünüm öznitelikleri konusunda dikkatli olun (örn. büyük gruplar için `table-list`).
4. **Kullanıcı Deneyimi**: Katılımcılar için veri girişini daha kolay ve sezgisel hale getiren görünümleri seçin.
5. **Test**: Görünümlerin beklendiği gibi çalıştığından emin olmak için formunuzu her zaman hedef cihazlarda test edin.

## Gelişmiş Teknikler

### Görünümleri Birleştirme

Bazı görünüm öznitelikleri daha karmaşık düzenler için birleştirilebilir:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Birini seçin: | minimal compact |
```

### Dinamik Görünümler

rtSurvey, form mantığına dayalı dinamik görünüm değişikliklerine izin verir:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Saati girin: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Mobil Uygulama Hususları

- Bazı görünümler (örn. `quick`, `signature`) mobil cihazlara özgüdür.
- Tutarlı davranışı sağlamak için hem Android hem de iOS'ta kapsamlı test yapın.

## rtSurvey Genişletilmiş Görünüm Öznitelikleri

Standart XLSForm görünümlerine ek olarak, rtSurvey aşağıdaki platforma özgü seçenekleri destekler:

### Veri ve görüntüleme kontrolü

| Görünüm Özniteliği | Soru Türleri | Açıklama |
|----------------------|----------------|-------------|
| `invisible` | herhangi | Alanı görünümden gizlerken değerini toplamaya veya hesaplamaya devam eder. `hidden` türünden farklı olarak alan hâlâ mantığa katılır. |
| `displaytitle` | herhangi | Alanın etiketinin/başlığının aksi hâlde bastırılacağı durumlarda bile görüntülenmesini zorlar. |
| `autopull` | select_one, select_multiple | Form yüklendiğinde veya tetikleyici alan değiştiğinde seçenekleri doldurmak için harici verileri otomatik olarak getirir. |
| `floating_hint` | text, integer, decimal | İpucu metnini aşağıda değil, giriş alanının üzerinde yüzen bir etiket olarak gösterir. |
| `calculate-button` | calculate | Otomatik hesaplamak yerine alanın isteğe bağlı olarak yeniden hesaplanmasını tetikleyen görünür bir düğme ekler. |

### Düzen

| Görünüm Özniteliği | Soru Türleri | Açıklama |
|----------------------|----------------|-------------|
| `1screen` | group | Grup boyutundan bağımsız olarak tüm grubun tek bir ekranda görüntülenmesini zorlar. |
| `columns(n)` | select_one, select_multiple | Seçenekleri `n` sütunda görüntüler. Örnek: `columns(3)` üç sütun radyo düğmesi gösterir. |
| `gridformat<row=R col=C colspan=S align=center>` | herhangi | Alanı `R` satır, `C` sütun konumunda `S` sütun kapsayan bir CSS ızgara düzenine yerleştirir. `advanced-extension/grid-layout` ile kullanılır. |
| `ignore-simplify` | herhangi | Form oluşturucuya bu alanın düzeninin otomatik basitleştirilmesini veya sıkıştırılmasını atlamasını söyler. |
| `required-but-simplify` | herhangi | Alan zorunludur ancak düzen yine de basitleştirilir |
| `embed` | herhangi | Alanı gömülü/satır içi görüntüleme modunda gösterir |
| `popup` | select_one, select_multiple | Seçenek listesini bir popup/modal katmanında gösterir |
| `auto-hide-empty` | boxtag, select | Seçenek listesi boş olduğunda widget'ı gizler |
| `text-nolabel` | select_one, select_multiple | Her seçenek için metin etiketini gizler |

### Widget'lar

| Görünüm Özniteliği | Soru Türleri | Açıklama |
|----------------------|----------------|-------------|
| `likert` | select_one | Seçenekleri Likert ölçeği satırı olarak sunar (standart tabloda zaten var; desteklendiği onaylandı). |
| `distress` | select_one | Seçenekleri duygusal ikonlarla Kessler Psikolojik Sıkıntı Ölçeği (K10) görsel widget'ı olarak gösterir. |

### Seçim görsel widget'ları

| Görünüm Özniteliği | Soru Türleri | Açıklama |
|----------------------|----------------|-------------|
| `tagging` | select_one, select_multiple | Seçenekleri radyo düğmeleri veya onay kutuları yerine tıklanabilir etiket chip'leri olarak gösterir |
| `boxtag` | select_one, select_multiple | Seçenekleri kullanıcının seçmek için dokunduğu stilize dikdörtgen kutular olarak gösterir |
| `boxtag -search` | select_one, select_multiple | Kutular üzerinde bir arama/filtreleme girişi olan boxtag düzeni |
| `duolingo-style1` | select_one, select_multiple | Duolingo ilhamlı kart düzeni — ikonlu büyük dokunulabilir kartlar |
| `rating_box` | select_one | Izgara tabanlı derecelendirme kutuları — sayısal veya ölçek seçenekleri için en iyi |
| `star_rating` | select_one | Yıldız derecelendirme widget'ı — seçenekler 1–N yıldız olarak gösterilir |
| `choices-noshow` | select_one, select_multiple | Başlangıçta yalnızca ilk 10 seçeneği gösterir; geri kalanı istek üzerine ortaya çıkarır |
| `noshow` | select_one | Seçenek listesini tamamen gizler; değer programatik olarak ayarlanır |
| `checkall` | select_multiple | Listenin üstüne "Tümünü seç" seçeneği ekler |
| `max-items(N)` | select_one, select_multiple | Görünür seçenek sayısını N ile sınırlar (örn. max-items(5)) |

### Metin görsel widget'ları

| Görünüm Özniteliği | Soru Türleri | Açıklama |
|----------------------|----------------|-------------|
| `richtext` | text | Zengin metin düzenleyici — kalın, italik, listeler ve bağlantılar içeren araç çubuğu |
| `typingtest` | text | Yazma testi arayüzü — bir metin parçası sunar ve yazma hızını ve doğruluğunu ölçer |

### Medya uzantıları

| Görünüm Özniteliği | Soru Türleri | Açıklama |
|----------------------|----------------|-------------|
| `watermark("expr")` | image | Çekilen fotoğrafın üzerine metin filigranı ekler; argüman yakalama anında değerlendirilen bir XPath ifadesidir |
| `editable` | image | Katılımcının çektikten sonra fotoğrafa açıklama eklemesine veya üzerine çizim yapmasına olanak tanır |

### Inline görüntü yapılandırması

Bir etiket veya not içindeki alan değerinin nasıl görüntüleneceğini kontrol etmek için `display{}` kullanın. Gönderi sonrası gösterilen sonuçlar özetini kontrol etmek için `results{}` kullanın.

| Sözdizimi | Soru Türleri | Açıklama |
|----------|----------------|-------------|
| `display{format="..."}` | herhangi | `${fieldname}` aracılığıyla bir etikete inline eklendiğinde alan değerini biçimlendirir |
| `results{show="true"}` | herhangi | Gönderme sonrası sonuçlar özet ekranında alan değerini gösterir |
