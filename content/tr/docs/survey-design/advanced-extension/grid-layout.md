---
title: "Izgara Düzeni"
description: "Izgara düzeni, bir grup içindeki alanları CSS ızgarasına konumlandırmanıza olanak tanır; çok sütunlu form tasarımları oluşturmanızı sağlar."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 296
---

**Izgara Düzeni** özelliği, `gridformat<>` görünüm etiketini kullanarak bir grup içindeki soruları **çok sütunlu bir ızgarada** düzenlemenize olanak tanır. Bu, dikey olarak istiflemek yerine yan yana görünmesi gereken birden fazla ilgili alanın bulunduğu yoğun veri girişi formları için kullanışlıdır.

---

## Nasıl çalışır

Izgara düzeni iki düzeyde uygulanır:

1. **Grup** — ızgaranın kaç sütuna sahip olduğunu tanımlamak için `appearance: field-list grid(weight=N)` ayarlayın
2. **Gruptaki her alan** — alanı konumlandırmak için `appearance: gridformat<row=R col=C colspan=S/>` ayarlayın

Izgara, 12 sütunlu Bootstrap tarzı bir sistem kullanır. `weight=N`, ızgaranızın kaç mantıksal sütuna sahip olduğunu tanımlar; her sütun `12/N` Bootstrap sütunu kaplar.

---

## Grup düzeyinde görünüm

| Görünüm | Açıklama |
|------------|-------------|
| `field-list grid(weight=2)` | 2 sütunlu ızgara (her sütun = 6 Bootstrap sütunu) |
| `field-list grid(weight=3)` | 3 sütunlu ızgara (her sütun = 4 Bootstrap sütunu) |
| `field-list grid(weight=4)` | 4 sütunlu ızgara (her sütun = 3 Bootstrap sütunu) |
| `field-list grid(weight=6)` | 6 sütunlu ızgara (her sütun = 2 Bootstrap sütunu) |

---

## Alan düzeyinde `gridformat<>` sözdizimi

```
gridformat<row=R col=C colspan=S/>
gridformat<row=R col=C colspan=S backgroundcolor=COLOR/>
```

| Öznitelik | Açıklama |
|-----------|-------------|
| `row` | Satır numarası (1'den başlar) |
| `col` | Sütun numarası (1'den başlar, `weight` ile tanımlanan ızgara içinde) |
| `colspan` | Bu alanın kapladığı sütun sayısı (varsayılan 1) |
| `backgroundcolor` | Alan arka planı için isteğe bağlı CSS rengi (örn. `#f0f0f0`, `lightblue`) |

---

## Örnek: 2 sütunlu hane anketi bölümü

| type | name | label | appearance |
|------|------|-------|------------|
| begin_group | demographics | Demografik Bilgiler | `field-list grid(weight=2)` |
| text | first_name | Ad | `gridformat<row=1 col=1/>` |
| text | last_name | Soyad | `gridformat<row=1 col=2/>` |
| integer | age | Yaş | `gridformat<row=2 col=1/>` |
| select_one gender | gender | Cinsiyet | `gridformat<row=2 col=2/>` |
| text | address | Tam adres | `gridformat<row=3 col=1 colspan=2/>` |
| end_group | | | |

Bu şu şekilde görüntülenir:

```
[ Ad                ] [ Soyad              ]
[ Yaş               ] [ Cinsiyet           ]
[ Tam adres (her iki sütunu kapsar)        ]
```

---

## Örnek: 3 sütunlu arazi verisi girişi

| type | name | label | appearance |
|------|------|-------|------------|
| begin_group | plot_data | Arazi ayrıntıları | `field-list grid(weight=3)` |
| text | plot_id | Arazi Kimliği | `gridformat<row=1 col=1/>` |
| decimal | area_ha | Alan (ha) | `gridformat<row=1 col=2/>` |
| select_one crop_type | crop | Ürün türü | `gridformat<row=1 col=3/>` |
| decimal | yield | Verim (kg) | `gridformat<row=2 col=1/>` |
| decimal | revenue | Gelir | `gridformat<row=2 col=2/>` |
| text | notes | Notlar | `gridformat<row=2 col=3/>` |
| end_group | | | |

---

## Arka plan renkleri

Bölümleri görsel olarak ayırt etmek için `backgroundcolor` kullanın:

| type | name | label | appearance |
|------|------|-------|------------|
| note | section_a | Bölüm A | `gridformat<row=1 col=1 colspan=2 backgroundcolor=#e8f4f8/>` |

---

## En İyi Uygulamalar

1. Izgara düzenini yalnızca yan yana alanların gerçekten kaydırmayı azalttığı **veri girişi yoğun** ekranlarda kullanın.
2. `colspan=1` alanlarını kısa tutun (kimlikler, kodlar, kısa seçimler) — geniş etiketler dar ızgara sütunlarında kötü görünür.
3. Uzun etiketli veya çok satırlı metin girişleri olan alanlar için `colspan=N` kullanın.
4. Sayımcıların kullanmasını beklediğiniz en küçük ekran boyutunu test edin — 4 sütunlu bir ızgara telefonda dar hissettirirseniz.
5. Izgara düzeni web ve tablet form faktörlerinde en iyi çalışır; cep telefonlarında genellikle 2 sütunlu düzen maksimum rahat genişliktir.

## Sınırlamalar

- `gridformat<>` yalnızca `grid(weight=N)` görünümüne sahip bir grup içinde çalışır — üst düzeyde etkisi yoktur.
- Izgara düzeni, rtSurvey web formu uzantısıdır ve diğer ODK uyumlu istemcilerde doğru şekilde görüntülenmeyebilir.
- Form oluşturma zamanında satır ve sütun konumu doğrulanmaz — örtüşen alanların her ikisi de görüntülenecek ama bozuk görünebilir.
