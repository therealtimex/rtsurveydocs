---
weight: 15
date: "2026-03-04T00:00:00+00:00"
draft: false
title: "Sistem Kullanıcısı"
icon: "people"
toc: true
description: "Tüm platform katılımcıları için rolleri, izinleri ve işe alım süreçlerini yönetin."
tags: ["Users", "Access Control", "Onboarding", "Roles"]
---

# Sistem Kullanıcısı Yönetimi

**Sistem Kullanıcısı** modülü (`/cpms/cpmsSystemUser/admin`), Gerçek Zamanlı Anket platformunuza (RT-CPMS) kimin erişeceğini ve hangi işlemleri gerçekleştirebileceğini kontrol etmek için kapsamlı bir yönetim arayüzüdür.

![Sistem Kullanıcısı Arayüzü](/images/system_user.png)

## Birleşik Yönetim Yaklaşımı

RT-CPMS'de bir **Sayımcı**, yalnızca bir Sistem Kullanıcısına atanan belirli bir Roldür. Ayrı bir "Sayımcı" veritabanı bulunmamaktadır. İster web portalını izleyen üst düzey bir Yönetici olsun ister mobil uygulama aracılığıyla veri toplayan bir saha Sayımcısı olsun, tüm kullanıcılar bu tek, birleşik çerçeve içinde yönetilmektedir.

## Temel Özellikler

### 1. Kullanıcı Dizini ve Izgara Görünümü
Ana arayüz, çalışma alanına bağlı tüm kullanıcıların sayfalandırılmış bir listesini görüntüler. Temel özellikler şunlardır:
* **Organizasyon Kimliği ve Adı**: Kullanıcıların belirli organizasyonel birimler altında mantıksal gruplaması (örn. `rta`, `partner_org`).
* **Rol**: Kullanıcının izin düzeyini belirtir (örn. `Yönetici`, `Lider Ekip`, `Sayımcı`).
* **Grup**: Mekansal veya mantıksal gruplama atamaları (örn. belirli bölgeler veya operasyonel ekipler).
* **Senkronize Edildi**: Hesabın merkezi Tek Oturum Açma (SSO) sistemiyle başarıyla entegre edilip edilmediğini gösterir.
* **Durum**: Bir hesabın `Aktif`, `Pasif`, `Silindi` veya `Engellendi` olduğunu doğrulayan görsel göstergeler.

**Genel Eylemler:**
* **Sistem Kullanıcısı Ekle**: Bireysel profil manüel olarak oluşturun.
* **Sistem Kullanıcısı İçe Aktar**: Excel şablonu kullanarak hesapları toplu yükleyin. `Atla` veya `Değiştir` modlarını kullanarak çakışmaları çözebilir ve doğrudan SSO ile senkronize edebilirsiniz.
* **Toplu Sil**: Toplu hesap kaldırma için çoklu seçim desteği.

### 2. Erişim Kontrolü ve Güvenlik
Kullanıcı profili oluştururken veya düzenlerken çeşitli kritik güvenlik ve iş akışı alanları mevcuttur:
* **Kullanıcı Kodu**: Yerel CPMS hesabını merkezi SSO deposuna bağlayan benzersiz tanımlayıcı.
* **Cihaz Değiştirme Kodu**: Bir sayımcının veri toplama için kullandığı mobil cihazı değiştirmesi gerektiğinde gerekli olan güçlü güvenlik belirteci.
* **Güç Düzeyi**: 0 (en düşük) ile 20 (en yüksek) arasında granüler öncelik/erişim ölçeği.
* **Denetim Geçişi**: Standart bir kullanıcıyı anında yönetim statüsüne yükselten onay kutusu.
* **İş Akışı Otomasyonu**: "Düzenleme İsteğini Otomatik Onayla" seçeneği; güvenilir kullanıcılar için veri temizleme ve doğrulama sürecini kolaylaştırır.

### 3. Kod Yönetimi (Otomatik İşe Alım)
"Kod" alt sekmesinde bulunan bu özellik, karma tabanlı kayıt ve davet bağlantılarını yöneterek büyük ekipler için işe alım sürecini kolaylaştırır.

* **Kayıt vs. Davet**: Kullanıcıların dağıtılmış bir bağlantı kullanarak kendilerini kaydedip kaydedemeyeceğini veya doğrudan yönetici davetine ihtiyaç duyup duymadıklarını seçin.
* **Son Kullanma Tarihleri**: İşe alımı belirli zaman dilimleriyle sınırlayın.
* **Kullanım Sınırları**: Tek bir oluşturulan kodla katılabilecek kullanıcı sayısını sınırlayın.
* **Önceden Atanmış Roller**: Bu kodlar aracılığıyla katılan kullanıcılar, manuel yönetici müdahalesi olmadan çalışmaya hazır olduklarından emin olmak için önceden tanımlanmış rolü ve güç düzeyini otomatik olarak devralır.
