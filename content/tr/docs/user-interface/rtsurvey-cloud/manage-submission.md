---
title: "Gönderim Yönetimi"
description: "Ham veri girişlerini ve gönderimleri inceleyin, yönetin ve dışa aktarın."
icon: "cloud"
date: "2023-05-22T00:34:57+01:00"
lastmod: "2023-05-22T00:34:57+01:00"
draft: false
weight: 317
---

**Gönderim Yönetimi** modülü (Form Ailesi bölümündeki **Veri Görünümü** düğmesi aracılığıyla erişilir), proje yöneticilerinin ve denetçilerin gelen ham verilerle doğrudan etkileşime girmesine olanak tanır. Sayımcı gönderimleri incelemek, cihaz tanımlayıcılarını takip etmek ve veri kalitesi işlemleri gerçekleştirmek için birleşik bir çalışma alanı görevi görür.

![Gönderim Yönetimi Arayüzü](/images/manage_submissions.png)

## Verilere Genel Bakış ve Sütunlar

Veri ızgarası, belirli bir form için toplanan verileri dinamik olarak görüntüler. İki ana modda çalışır: **Resmi** (Kesinleştirilmiş kayıtlar) ve **Çalışma** (Gerçek Zamanlı, kesinleştirilmemiş kayıtlar).

### Temel Veri Sütunları

Formda tanımlanan özel sorulardan bağımsız olarak ızgara, denetim yardımı için çeşitli standart meta veri sütunları içerir:

- **Gönderen:** Gönderimin kaynak platformunu tanımlar (örn. FA Saha Uygulaması için, WEB Web Formu için, RS uzak sistemler için).
- **Ayrıntı:** Bu örnek için gönderilen her değişkeni ve cevabı incelemek için odaklanmış, tek kayıt görünümünü (Arama simgesi) açar.
- **iNot:** Denetçilerin toplanan verileri değiştirmeden belirli bir kayda yan notlar veya dahili yorumlar eklemesine olanak tanır (kalem simgesiyle temsil edilir).
- **Tarih alanları:** Kaydın ne zaman başlatıldığını, tamamlandığını veya senkronize edildiğini gösteren zaman damgaları.
- **Medya ekleri:** Anket sırasında toplanan görüntülere, imzalara veya dosyalara doğrudan küçük resim bağlantıları.
- **Tekrar grupları:** Ana form içindeki tekrarlanan sorular için iç içe tablolara erişmek için adanmış bağlantılar.

## Gönderim Eylemleri

Aktif veri kalitesi kontrolünü kolaylaştırmak için arayüz, seçilen kayıtlarda yürütülebilen eyleme dönüştürülebilir komutların açılır menüsünü sağlar:

- **Yeni örnek oluştur:** Yöneticilerin doğrudan veritabanına yeni bir anket kaydı manüel olarak girmesine olanak tanır.
- **Örneği geri gönder:** Gönderilen kaydı reddeder ve sayımcıdan bilgiyi yeniden doğrulamasını veya yeniden toplamasını ister.
- **Örneği takip et:** Bir kaydı daha fazla dikkat için işaretler; genellikle netleştirme için saha ekibine bir uyarı gönderir.
- **Geri döndürülen komutlar dosyasına aktar / Takip komutları paketi:** Özellikle iade veya takip için işaretlenmiş veri kümelerini içeren toplu dışa aktarmaları (dosyaları) oluşturur.
- **XML'e dönüştür:** Yapılandırılmış veri kümesini arka uç analizi veya sistem entegrasyonu için ham XML biçimine geri dönüştürür.
- **Örnekleri İlet:** (*Çalışma* modunda mevcut) Kesinleştirilmemiş verileri anında başka bir cihaza veya kullanıcıya iter.
- **Sil:** Seçilen örnekleri veritabanından kalıcı olarak kaldırır.
