---
title: "Soru Türleri"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 220
---

rtSurvey tüm standart XLSForm soru türlerini ve birkaç uzantıyı destekler. Her soru türü, ne tür verinin toplandığını ve giriş widget'ının cihazda nasıl görüntüleneceğini belirler.

Soru türünü ayarlamak için XLSForm'unuzdaki **survey** çalışma sayfasının `type` sütununa tür adını girin.

## Metin girişi

| Tür | Açıklama |
|------|-------------|
| [text](text) | Serbest metin yanıtı — tüm karakterlere izin verilir |
| [integer](integer) | Tam sayı (ondalık yok) |
| [decimal](decimal) | Ondalıklı sayı |
| [range](range) | Tanımlı min/maks aralığı içinde kaydırıcıdan seçilen sayı |

## Seçim

| Tür | Açıklama |
|------|-------------|
| [select_one listname](select-one) | Listeden tam olarak bir seçenek seç |
| [select_multiple listname](select-multiple) | Listeden bir veya daha fazla seçenek seç |
| [select_one_from_file filename](select-one-from-file) | Harici bir CSV dosyasından yüklenen seçeneklerden birini seç |
| [rank listname](rank) | Seçenekleri tercih veya önceliğe göre sırala |

## Tarih ve Saat

| Tür | Açıklama |
|------|-------------|
| [date](date) | Takvim tarihi (yıl, ay, gün) |
| [time](time) | Günün saati (saat, dakika) |
| [datetime](datetime-date-time) | Birleşik tarih ve saat |

## Konum

| Tür | Açıklama |
|------|-------------|
| [geopoint](geopoint) | Tek GPS koordinatı (enlem, boylam, irtifa, doğruluk) |
| [geotrace](geotrace) | Bir yol — GPS noktalarından oluşan bir çizgi |
| [geoshape](geoshape) | Bir alan — GPS noktalarından oluşan kapalı çokgen |

## Medya

| Tür | Açıklama |
|------|-------------|
| [image](image) | Fotoğraf çekimi veya görsel yükleme |
| [audio](audio) | Ses kaydı |
| [video](video) | Video kaydı |
| [file](file) | Genel dosya yükleme (PDF, belge vb.) |

## Diğer

| Tür | Açıklama |
|------|-------------|
| [barcode](barcode) | Barkod veya QR kod tarama |
| [note](note) | Salt okunur görüntü metni — talimatları veya hesaplanmış özetleri gösterir |
| [calculate](calculate) | Hesaplanmış bir değer saklayan gizli alan |
| [hidden](hidden) | Statik veya önceden doldurulmuş bir değer saklayan gizli alan |
| [trigger / acknowledge](trigger) | Sayımcının bir ifadeyi okuduğunu onaylamak için işaretlemesi gereken onay kutusu |
| [meta](meta) | Otomatik meta veriler: zaman damgaları, cihaz kimliği, sayımcı bilgileri |

## Tür ve görünümün birlikte çalışması

`type` **hangi verinin toplandığını** belirler. `appearance` sütunu **widget'ın nasıl göründüğünü** kontrol eder. Pek çok tür birden fazla görünümü destekler — örneğin `select_one` radyo düğmeleri, açılır liste, Likert ölçeği veya kompakt ızgara olarak görünebilir.

Seçeneklerin tam listesi için [Görünüm](../appearance) bölümüne bakın.
