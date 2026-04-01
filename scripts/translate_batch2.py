#!/usr/bin/env python3
"""
Translate sso-authentication, maintenance, configuration into 35 languages.
Uses full translations for key UI text; keeps technical content in English.
"""
import os

BASE = "/Volumes/ExDisk/rtLab/webapp/doc.rtsurvey.com/content"
LANGUAGES = [
    "ar","bg","cs","da","de","el","es","fi","fr","hi",
    "hu","id","it","ja","km","ko","lt","lv","nb","nl",
    "pl","pt","pt-br","ru","sk","sq","sr","sv","te","th",
    "tr","uk","vi","zh-hans","zh-hant"
]

# ── Metadata tables ──────────────────────────────────────────

SSO_META = dict(weight=5, date="2026-03-12T00:00:00+07:00", lastmod="2026-03-12T00:00:00+07:00",
                draft="false", author="rtSurvey", icon="lock", toc="true")
MAINT_META = dict(weight=6, date="2026-03-12T00:00:00+07:00", lastmod="2026-03-12T00:00:00+07:00",
                  draft="false", author="rtSurvey", icon="build", toc="true")
CONF_META  = dict(weight=2, date="2026-03-12T00:00:00+07:00", lastmod="2026-03-12T00:00:00+07:00",
                  draft="false", author="rtSurvey", icon="settings", toc="true")

SSO_TITLES = {
    "ar":"مصادقة SSO","bg":"SSO удостоверяване","cs":"SSO autentizace",
    "da":"SSO-godkendelse","de":"SSO-Authentifizierung","el":"Έλεγχος ταυτότητας SSO",
    "es":"Autenticación SSO","fi":"SSO-todennus","fr":"Authentification SSO",
    "hi":"SSO प्रमाणीकरण","hu":"SSO hitelesítés","id":"Autentikasi SSO",
    "it":"Autenticazione SSO","ja":"SSO認証","km":"ការផ្ទៀងផ្ទាត់ SSO",
    "ko":"SSO 인증","lt":"SSO autentifikacija","lv":"SSO autentifikācija",
    "nb":"SSO-godkjenning","nl":"SSO-verificatie","pl":"Uwierzytelnianie SSO",
    "pt":"Autenticação SSO","pt-br":"Autenticação SSO","ru":"SSO-аутентификация",
    "sk":"SSO autentifikácia","sq":"Autentifikimi SSO","sr":"SSO аутентификација",
    "sv":"SSO-autentisering","te":"SSO ప్రమాణీకరణ","th":"การยืนยันตัวตน SSO",
    "tr":"SSO Kimlik Doğrulama","uk":"SSO автентифікація","vi":"Xác thực SSO",
    "zh-hans":"SSO 身份验证","zh-hant":"SSO 身份驗證",
}
SSO_DESCS = {
    "ar":"تكوين تسجيل الدخول الموحد لـ rtCloud المستضاف ذاتياً باستخدام Keycloak المدمج أو موفر OIDC خارجي أو Azure Active Directory.",
    "bg":"Конфигуриране на единично влизане за самостоятелно хостван rtCloud чрез вграден Keycloak, външен OIDC доставчик или Azure Active Directory.",
    "cs":"Konfigurace jednotného přihlašování pro self-hosted rtCloud pomocí vestavěného Keycloak, externího poskytovatele OIDC nebo Azure Active Directory.",
    "da":"Konfigurer Single Sign-On til selvhostet rtCloud ved hjælp af indlejret Keycloak, en ekstern OIDC-udbyder eller Azure Active Directory.",
    "de":"Single Sign-On für selbst gehostetes rtCloud konfigurieren mit eingebettetem Keycloak, einem externen OIDC-Anbieter oder Azure Active Directory.",
    "el":"Ρύθμιση Ενιαίας Σύνδεσης για αυτο-φιλοξενούμενο rtCloud χρησιμοποιώντας ενσωματωμένο Keycloak, εξωτερικό πάροχο OIDC ή Azure Active Directory.",
    "es":"Configure el inicio de sesión único para rtCloud autohospedado usando Keycloak integrado, un proveedor OIDC externo o Azure Active Directory.",
    "fi":"Määritä kertakirjautuminen itse isännöidylle rtCloudille käyttäen upotettua Keycloakia, ulkoista OIDC-tarjoajaa tai Azure Active Directoryä.",
    "fr":"Configurer l'authentification unique pour rtCloud auto-hébergé avec Keycloak intégré, un fournisseur OIDC externe ou Azure Active Directory.",
    "hi":"एम्बेडेड Keycloak, बाहरी OIDC प्रदाता, या Azure Active Directory का उपयोग करके सेल्फ-होस्टेड rtCloud के लिए Single Sign-On कॉन्फ़िगर करें।",
    "hu":"Single Sign-On konfigurálása önállóan üzemeltetett rtCloud számára beágyazott Keycloak, külső OIDC-szolgáltató vagy Azure Active Directory segítségével.",
    "id":"Konfigurasikan Single Sign-On untuk rtCloud yang dihosting sendiri menggunakan Keycloak tertanam, penyedia OIDC eksternal, atau Azure Active Directory.",
    "it":"Configurare il Single Sign-On per rtCloud self-hosted utilizzando Keycloak integrato, un provider OIDC esterno o Azure Active Directory.",
    "ja":"組み込みKeycloak、外部OIDCプロバイダー、またはAzure Active Directoryを使用して、セルフホスト型rtCloudのシングルサインオンを設定します。",
    "km":"កំណត់រចនាសម្ព័ន្ធ Single Sign-On សម្រាប់ rtCloud ដែលបង្ហោះខ្លួនឯង ដោយប្រើ Keycloak ដែលបានបញ្ចូល, អ្នកផ្តល់ OIDC ខាងក្រៅ, ឬ Azure Active Directory។",
    "ko":"내장된 Keycloak, 외부 OIDC 공급자 또는 Azure Active Directory를 사용하여 자체 호스팅 rtCloud에 Single Sign-On을 구성합니다.",
    "lt":"Konfigūruokite Single Sign-On savastiškai patalpintam rtCloud naudojant integruotą Keycloak, išorinį OIDC teikėją arba Azure Active Directory.",
    "lv":"Konfigurējiet Single Sign-On pašu mitinātam rtCloud, izmantojot iebūvētu Keycloak, ārēju OIDC sniedzēju vai Azure Active Directory.",
    "nb":"Konfigurer Single Sign-On for selvhostet rtCloud ved hjelp av innebygd Keycloak, en ekstern OIDC-leverandør eller Azure Active Directory.",
    "nl":"Configureer Single Sign-On voor zelf-gehoste rtCloud met ingebedde Keycloak, een externe OIDC-provider of Azure Active Directory.",
    "pl":"Skonfiguruj Single Sign-On dla samodzielnie hostowanego rtCloud przy użyciu wbudowanego Keycloak, zewnętrznego dostawcy OIDC lub Azure Active Directory.",
    "pt":"Configure o início de sessão único para rtCloud auto-hospedado usando Keycloak incorporado, um fornecedor OIDC externo ou Azure Active Directory.",
    "pt-br":"Configure o Single Sign-On para rtCloud auto-hospedado usando Keycloak incorporado, um provedor OIDC externo ou Azure Active Directory.",
    "ru":"Настройте единый вход для самостоятельно размещённого rtCloud с помощью встроенного Keycloak, внешнего поставщика OIDC или Azure Active Directory.",
    "sk":"Nakonfigurujte Single Sign-On pre self-hosted rtCloud pomocou vstavaného Keycloak, externého poskytovateľa OIDC alebo Azure Active Directory.",
    "sq":"Konfiguroni Single Sign-On për rtCloud të vetë-hostuar duke përdorur Keycloak të integruar, një ofrues OIDC të jashtëm ose Azure Active Directory.",
    "sr":"Конфигуришите Single Sign-On за самостално хостовани rtCloud користећи уграђени Keycloak, спољни OIDC провајдер или Azure Active Directory.",
    "sv":"Konfigurera Single Sign-On för egenhostad rtCloud med inbyggd Keycloak, en extern OIDC-leverantör eller Azure Active Directory.",
    "te":"ఎంబెడెడ్ Keycloak, బాహ్య OIDC ప్రొవైడర్ లేదా Azure Active Directory ఉపయోగించి స్వీయ-హోస్ట్ చేయబడిన rtCloud కోసం Single Sign-On కాన్ఫిగర్ చేయండి.",
    "th":"กำหนดค่า Single Sign-On สำหรับ rtCloud ที่โฮสต์เองโดยใช้ Keycloak ในตัว ผู้ให้บริการ OIDC ภายนอก หรือ Azure Active Directory",
    "tr":"Gömülü Keycloak, harici OIDC sağlayıcısı veya Azure Active Directory kullanarak kendi barındırdığınız rtCloud için Single Sign-On yapılandırın.",
    "uk":"Налаштуйте єдиний вхід для самостійно розміщеного rtCloud за допомогою вбудованого Keycloak, зовнішнього постачальника OIDC або Azure Active Directory.",
    "vi":"Cấu hình Single Sign-On cho rtCloud tự lưu trữ bằng Keycloak nhúng, nhà cung cấp OIDC bên ngoài hoặc Azure Active Directory.",
    "zh-hans":"使用内嵌 Keycloak、外部 OIDC 提供商或 Azure Active Directory 为自托管 rtCloud 配置单点登录。",
    "zh-hant":"使用內嵌 Keycloak、外部 OIDC 提供商或 Azure Active Directory 為自託管 rtCloud 設定單一登入。",
}

MAINT_TITLES = {
    "ar":"الصيانة","bg":"Поддръжка","cs":"Údržba","da":"Vedligeholdelse",
    "de":"Wartung","el":"Συντήρηση","es":"Mantenimiento","fi":"Ylläpito",
    "fr":"Maintenance","hi":"रखरखाव","hu":"Karbantartás","id":"Pemeliharaan",
    "it":"Manutenzione","ja":"メンテナンス","km":"ការថែទាំ","ko":"유지보수",
    "lt":"Priežiūra","lv":"Uzturēšana","nb":"Vedlikehold","nl":"Onderhoud",
    "pl":"Konserwacja","pt":"Manutenção","pt-br":"Manutenção","ru":"Обслуживание",
    "sk":"Údržba","sq":"Mirëmbajtja","sr":"Одржавање","sv":"Underhåll",
    "te":"నిర్వహణ","th":"การบำรุงรักษา","tr":"Bakım","uk":"Обслуговування",
    "vi":"Bảo trì","zh-hans":"维护","zh-hant":"維護",
}
MAINT_DESCS = {
    "ar":"الصيانة اليومية لنسخة rtCloud المستضافة ذاتياً: الترقية والنسخ الاحتياطي والاستعادة واستكشاف الأخطاء الشائعة.",
    "bg":"Ежедневна поддръжка на самостоятелно хостван rtCloud: надграждане, архивиране, възстановяване и отстраняване на чести проблеми.",
    "cs":"Každodenní údržba samostojně hostovaného rtCloud: upgrady, zálohy, obnova a řešení běžných problémů.",
    "da":"Daglig vedligeholdelse af en selvhostet rtCloud-instans: opgradering, sikkerhedskopiering, gendannelse og fejlfinding.",
    "de":"Tägliche Wartung einer selbst gehosteten rtCloud-Instanz: Upgrades, Backups, Wiederherstellung und Fehlerbehebung.",
    "el":"Καθημερινή συντήρηση αυτο-φιλοξενούμενης rtCloud: αναβαθμίσεις, αντίγραφα ασφαλείας, επαναφορά και αντιμετώπιση προβλημάτων.",
    "es":"Mantenimiento diario de una instancia rtCloud autohospedada: actualizaciones, copias de seguridad, restauración y solución de problemas comunes.",
    "fi":"Itse isännöidyn rtCloud-instanssin päivittäinen ylläpito: päivitykset, varmuuskopiot, palautus ja yleisten ongelmien vianmääritys.",
    "fr":"Maintenance quotidienne d'une instance rtCloud auto-hébergée : mises à niveau, sauvegardes, restauration et dépannage des problèmes courants.",
    "hi":"सेल्फ-होस्टेड rtCloud इंस्टेंस का दैनिक रखरखाव: अपग्रेड, बैकअप, पुनर्स्थापना और सामान्य समस्याओं का निवारण।",
    "hu":"Önállóan üzemeltetett rtCloud példány napi karbantartása: frissítések, biztonsági mentések, visszaállítás és hibaelhárítás.",
    "id":"Pemeliharaan sehari-hari untuk instans rtCloud yang dihosting sendiri: pembaruan, pencadangan, pemulihan, dan pemecahan masalah umum.",
    "it":"Manutenzione quotidiana di un'istanza rtCloud self-hosted: aggiornamenti, backup, ripristino e risoluzione dei problemi comuni.",
    "ja":"セルフホスト型rtCloudインスタンスの日常メンテナンス：アップグレード、バックアップ、復元、一般的な問題のトラブルシューティング。",
    "km":"ការថែទាំប្រចាំថ្ងៃសម្រាប់ rtCloud instance ដែលបង្ហោះខ្លួនឯង: ការដំឡើងកំណែ, ការបម្រុងទុក, ការស្ដារ, និងការដោះស្រាយបញ្ហាទូទៅ។",
    "ko":"자체 호스팅 rtCloud 인스턴스의 일상 유지보수: 업그레이드, 백업, 복원, 일반적인 문제 해결.",
    "lt":"Kasdienė savastiškai patalpinto rtCloud egzemplioriaus priežiūra: naujinimai, atsarginės kopijos, atkūrimas ir bendrų problemų šalinimas.",
    "lv":"Pašu mitinātās rtCloud instances ikdienas uzturēšana: jauninājumi, dublēšana, atjaunošana un biežu problēmu novēršana.",
    "nb":"Daglig vedlikehold av en selvhostet rtCloud-instans: oppgraderinger, sikkerhetskopiering, gjenoppretting og feilsøking.",
    "nl":"Dagelijks onderhoud van een zelf-gehoste rtCloud-instantie: upgrades, back-ups, herstel en probleemoplossing.",
    "pl":"Codzienne utrzymanie samodzielnie hostowanej instancji rtCloud: aktualizacje, kopie zapasowe, przywracanie i rozwiązywanie typowych problemów.",
    "pt":"Manutenção diária de uma instância rtCloud auto-hospedada: atualizações, cópias de segurança, restauração e resolução de problemas comuns.",
    "pt-br":"Manutenção diária de uma instância rtCloud auto-hospedada: atualizações, backups, restauração e solução de problemas comuns.",
    "ru":"Ежедневное обслуживание самостоятельно размещённого экземпляра rtCloud: обновления, резервные копии, восстановление и устранение распространённых проблем.",
    "sk":"Každodenná údržba self-hosted inštancie rtCloud: aktualizácie, zálohy, obnova a riešenie bežných problémov.",
    "sq":"Mirëmbajtja ditore e një instanze rtCloud të vetë-hostuar: përditësime, kopje rezervë, rivendosje dhe zgjidhje e problemeve të zakonshme.",
    "sr":"Свакодневно одржавање самостално хостоване rtCloud инстанце: надоградње, резервне копије, враћање и отклањање уобичајених проблема.",
    "sv":"Dagligt underhåll av en egenhostad rtCloud-instans: uppgraderingar, säkerhetskopieringar, återställning och felsökning.",
    "te":"స్వీయ-హోస్ట్ చేయబడిన rtCloud ఇన్‌స్టాన్స్ యొక్క రోజువారీ నిర్వహణ: అప్‌గ్రేడ్‌లు, బ్యాకప్‌లు, పునరుద్ధరణ మరియు సాధారణ సమస్యల పరిష్కారం.",
    "th":"การบำรุงรักษาประจำวันสำหรับ rtCloud instance ที่โฮสต์เอง: การอัพเกรด, การสำรองข้อมูล, การกู้คืน และการแก้ไขปัญหาทั่วไป",
    "tr":"Kendi barındırdığınız rtCloud örneğinin günlük bakımı: yükseltmeler, yedeklemeler, geri yükleme ve yaygın sorunların giderilmesi.",
    "uk":"Щоденне обслуговування самостійно розміщеного екземпляра rtCloud: оновлення, резервні копії, відновлення та усунення типових проблем.",
    "vi":"Bảo trì hàng ngày cho phiên bản rtCloud tự lưu trữ: nâng cấp, sao lưu, khôi phục và khắc phục sự cố thông thường.",
    "zh-hans":"自托管 rtCloud 实例的日常维护：升级、备份、恢复以及常见问题排查。",
    "zh-hant":"自託管 rtCloud 實例的日常維護：升級、備份、還原及常見問題排解。",
}

CONF_TITLES = {
    "ar":"مرجع التكوين","bg":"Справочник за конфигурация","cs":"Referenční příručka konfigurace",
    "da":"Konfigurationsreference","de":"Konfigurationsreferenz","el":"Αναφορά διαμόρφωσης",
    "es":"Referencia de configuración","fi":"Konfiguraatioviite","fr":"Référence de configuration",
    "hi":"कॉन्फ़िगरेशन संदर्भ","hu":"Konfigurációs referencia","id":"Referensi Konfigurasi",
    "it":"Riferimento configurazione","ja":"設定リファレンス","km":"ឯកសារយោងការកំណត់រចនាសម្ព័ន្ធ",
    "ko":"구성 참조","lt":"Konfigūracijos nuoroda","lv":"Konfigurācijas uzziņa",
    "nb":"Konfigurasjonsreferanse","nl":"Configuratiereferentie","pl":"Dokumentacja konfiguracji",
    "pt":"Referência de configuração","pt-br":"Referência de configuração","ru":"Справочник конфигурации",
    "sk":"Referenčná príručka konfigurácie","sq":"Referenca e konfigurimit","sr":"Референца конфигурације",
    "sv":"Konfigurationsreferens","te":"కాన్ఫిగరేషన్ రిఫరెన్స్","th":"เอกสารอ้างอิงการกำหนดค่า",
    "tr":"Yapılandırma Referansı","uk":"Довідник конфігурації","vi":"Tài liệu tham khảo cấu hình",
    "zh-hans":"配置参考","zh-hant":"配置參考",
}
CONF_DESCS = {
    "ar":"مرجع كامل لجميع متغيرات البيئة المستخدمة لتكوين نشر rtCloud المستضاف ذاتياً.",
    "bg":"Пълна справка за всички променливи на средата, използвани за конфигуриране на самостоятелно хостван rtCloud.",
    "cs":"Kompletní přehled všech proměnných prostředí používaných ke konfiguraci self-hosted nasazení rtCloud.",
    "da":"Komplet reference for alle miljøvariabler brugt til at konfigurere en selvhostet rtCloud-installation.",
    "de":"Vollständige Referenz aller Umgebungsvariablen zur Konfiguration einer selbst gehosteten rtCloud-Bereitstellung.",
    "el":"Πλήρης αναφορά για όλες τις μεταβλητές περιβάλλοντος που χρησιμοποιούνται για τη διαμόρφωση μιας αυτο-φιλοξενούμενης ανάπτυξης rtCloud.",
    "es":"Referencia completa de todas las variables de entorno utilizadas para configurar una implementación de rtCloud autohospedado.",
    "fi":"Täydellinen viite kaikista ympäristömuuttujista, joita käytetään itseisännöidyn rtCloud-asennuksen määrittämiseen.",
    "fr":"Référence complète de toutes les variables d'environnement utilisées pour configurer un déploiement rtCloud auto-hébergé.",
    "hi":"सेल्फ-होस्टेड rtCloud डिप्लॉयमेंट को कॉन्फ़िगर करने के लिए उपयोग किए जाने वाले सभी पर्यावरण चर का पूरा संदर्भ।",
    "hu":"Teljes referencia az önállóan üzemeltetett rtCloud telepítés konfigurálásához használt összes környezeti változóhoz.",
    "id":"Referensi lengkap untuk semua variabel lingkungan yang digunakan untuk mengonfigurasi deployment rtCloud yang dihosting sendiri.",
    "it":"Riferimento completo per tutte le variabili d'ambiente utilizzate per configurare un'implementazione rtCloud self-hosted.",
    "ja":"セルフホスト型rtCloudデプロイメントを設定するために使用されるすべての環境変数の完全なリファレンス。",
    "km":"ឯកសារយោងពេញលេញសម្រាប់អថេរបរិស្ថានទាំងអស់ដែលប្រើដើម្បីកំណត់រចនាសម្ព័ន្ធ rtCloud ដែលបង្ហោះខ្លួនឯង។",
    "ko":"자체 호스팅 rtCloud 배포를 구성하는 데 사용되는 모든 환경 변수에 대한 완전한 참조.",
    "lt":"Išsami visų aplinkos kintamųjų, naudojamų savastiškai patalpintam rtCloud diegimui konfigūruoti, nuoroda.",
    "lv":"Pilna uzziņa par visiem vides mainīgajiem, ko izmanto pašu mitinātā rtCloud izvietojuma konfigurēšanai.",
    "nb":"Komplett referanse for alle miljøvariabler som brukes til å konfigurere en selvhostet rtCloud-distribusjon.",
    "nl":"Volledige referentie voor alle omgevingsvariabelen die worden gebruikt voor het configureren van een zelf-gehoste rtCloud-implementatie.",
    "pl":"Pełna dokumentacja wszystkich zmiennych środowiskowych używanych do konfiguracji samodzielnie hostowanego wdrożenia rtCloud.",
    "pt":"Referência completa de todas as variáveis de ambiente utilizadas para configurar uma implementação rtCloud auto-hospedada.",
    "pt-br":"Referência completa de todas as variáveis de ambiente usadas para configurar uma implantação rtCloud auto-hospedada.",
    "ru":"Полный справочник всех переменных окружения, используемых для настройки самостоятельно размещённого развёртывания rtCloud.",
    "sk":"Kompletná referencia pre všetky premenné prostredia používané na konfiguráciu self-hosted nasadenia rtCloud.",
    "sq":"Referencë e plotë për të gjitha variablat e mjedisit të përdorura për konfigurimin e një vendosjeje rtCloud të vetë-hostuar.",
    "sr":"Потпуна референца за све променљиве окружења које се користе за конфигурисање самостално хостованог rtCloud.",
    "sv":"Fullständig referens för alla miljövariabler som används för att konfigurera en egenhostad rtCloud-driftsättning.",
    "te":"స్వీయ-హోస్ట్ చేయబడిన rtCloud విన్యాసాన్ని కాన్ఫిగర్ చేయడానికి ఉపయోగించే అన్ని పర్యావరణ వేరియబుల్స్ కోసం పూర్తి సూచన.",
    "th":"เอกสารอ้างอิงครบถ้วนสำหรับตัวแปรสภาพแวดล้อมทั้งหมดที่ใช้ในการกำหนดค่าการติดตั้ง rtCloud ที่โฮสต์เอง",
    "tr":"Kendi barındırdığınız rtCloud dağıtımını yapılandırmak için kullanılan tüm ortam değişkenlerine yönelik tam referans.",
    "uk":"Повний довідник усіх змінних середовища для налаштування самостійно розміщеного розгортання rtCloud.",
    "vi":"Tài liệu tham khảo đầy đủ về tất cả biến môi trường được sử dụng để cấu hình triển khai rtCloud tự lưu trữ.",
    "zh-hans":"用于配置自托管 rtCloud 部署的所有环境变量的完整参考。",
    "zh-hant":"用於設定自託管 rtCloud 部署的所有環境變數的完整參考。",
}

# ── Body builders ────────────────────────────────────────────
# For SSO and Maintenance, we use the English body with the translated intro sentence.
# For Configuration, same approach — translated intro + all tables in English.

SSO_INTRO = {
    "ar": "يدعم rtCloud ثلاثة أساليب لتسجيل الدخول الموحد (SSO):",
    "bg": "rtCloud поддържа три подхода за единично влизане (SSO):",
    "cs": "rtCloud podporuje tři přístupy k jednotnému přihlašování (SSO):",
    "da": "rtCloud understøtter tre tilgange til Single Sign-On (SSO):",
    "de": "rtCloud unterstützt drei Ansätze für Single Sign-On (SSO):",
    "el": "Το rtCloud υποστηρίζει τρεις προσεγγίσεις για Ενιαία Σύνδεση (SSO):",
    "es": "rtCloud admite tres enfoques para el inicio de sesión único (SSO):",
    "fi": "rtCloud tukee kolmea lähestymistapaa kertakirjautumiseen (SSO):",
    "fr": "rtCloud prend en charge trois approches pour l'authentification unique (SSO) :",
    "hi": "rtCloud सिंगल साइन-ऑन (SSO) के लिए तीन दृष्टिकोणों का समर्थन करता है:",
    "hu": "Az rtCloud háromféle megközelítést támogat az egyszeri bejelentkezéshez (SSO):",
    "id": "rtCloud mendukung tiga pendekatan untuk Single Sign-On (SSO):",
    "it": "rtCloud supporta tre approcci per il Single Sign-On (SSO):",
    "ja": "rtCloudはシングルサインオン（SSO）の3つのアプローチをサポートしています：",
    "km": "rtCloud គាំទ្របីវិធីសម្រាប់ Single Sign-On (SSO):",
    "ko": "rtCloud은 Single Sign-On(SSO)에 대한 세 가지 접근 방식을 지원합니다:",
    "lt": "rtCloud palaiko tris vieningojo prisijungimo (SSO) metodus:",
    "lv": "rtCloud atbalsta trīs pieejas vienotai pieteikšanās (SSO):",
    "nb": "rtCloud støtter tre tilnærminger for Single Sign-On (SSO):",
    "nl": "rtCloud ondersteunt drie benaderingen voor Single Sign-On (SSO):",
    "pl": "rtCloud obsługuje trzy podejścia do logowania jednokrotnego (SSO):",
    "pt": "O rtCloud suporta três abordagens para o início de sessão único (SSO):",
    "pt-br": "O rtCloud suporta três abordagens para Single Sign-On (SSO):",
    "ru": "rtCloud поддерживает три подхода к единому входу (SSO):",
    "sk": "rtCloud podporuje tri prístupy k jednotnému prihláseniu (SSO):",
    "sq": "rtCloud mbështet tre qasje për Single Sign-On (SSO):",
    "sr": "rtCloud подржава три приступа за Single Sign-On (SSO):",
    "sv": "rtCloud stöder tre metoder för Single Sign-On (SSO):",
    "te": "rtCloud Single Sign-On (SSO) కోసం మూడు విధానాలకు మద్దతు ఇస్తుంది:",
    "th": "rtCloud รองรับสามแนวทางสำหรับ Single Sign-On (SSO):",
    "tr": "rtCloud, Single Sign-On (SSO) için üç yaklaşımı destekler:",
    "uk": "rtCloud підтримує три підходи до єдиного входу (SSO):",
    "vi": "rtCloud hỗ trợ ba cách tiếp cận cho Single Sign-On (SSO):",
    "zh-hans": "rtCloud 支持三种单点登录（SSO）方式：",
    "zh-hant": "rtCloud 支援三種單一登入（SSO）方式：",
}

MAINT_INTRO = {
    "ar": "استخدم هذه الأوامر بانتظام لإدارة حاويات rtCloud. شغّلها من المجلد الذي يحتوي على `docker-compose.production.yml`.",
    "bg": "Използвайте тези команди редовно за управление на rtCloud контейнерите. Изпълнявайте ги от директорията, съдържаща `docker-compose.production.yml`.",
    "cs": "Tyto příkazy používejte pravidelně ke správě kontejnerů rtCloud. Spouštějte je z adresáře obsahujícího `docker-compose.production.yml`.",
    "da": "Brug disse kommandoer regelmæssigt til at administrere dine rtCloud-containere. Kør dem fra mappen med `docker-compose.production.yml`.",
    "de": "Verwenden Sie diese Befehle regelmäßig zur Verwaltung Ihrer rtCloud-Container. Führen Sie sie aus dem Verzeichnis aus, das `docker-compose.production.yml` enthält.",
    "el": "Χρησιμοποιήστε αυτές τις εντολές τακτικά για να διαχειριστείτε τα containers rtCloud. Εκτελέστε τες από τον κατάλογο που περιέχει `docker-compose.production.yml`.",
    "es": "Use estos comandos regularmente para administrar sus contenedores rtCloud. Ejecútelos desde el directorio que contiene `docker-compose.production.yml`.",
    "fi": "Käytä näitä komentoja säännöllisesti rtCloud-konttien hallintaan. Suorita ne `docker-compose.production.yml`-tiedoston sisältävästä hakemistosta.",
    "fr": "Utilisez ces commandes régulièrement pour gérer vos conteneurs rtCloud. Exécutez-les depuis le répertoire contenant `docker-compose.production.yml`.",
    "hi": "अपने rtCloud कंटेनर प्रबंधित करने के लिए इन कमांड का नियमित उपयोग करें। इन्हें `docker-compose.production.yml` वाले डायरेक्टरी से चलाएं।",
    "hu": "Használja ezeket a parancsokat rendszeresen az rtCloud konténerek kezeléséhez. Futtassa őket a `docker-compose.production.yml` fájlt tartalmazó könyvtárból.",
    "id": "Gunakan perintah-perintah ini secara teratur untuk mengelola container rtCloud Anda. Jalankan dari direktori yang berisi `docker-compose.production.yml`.",
    "it": "Usare questi comandi regolarmente per gestire i container rtCloud. Eseguirli dalla directory contenente `docker-compose.production.yml`.",
    "ja": "rtCloudコンテナを管理するためにこれらのコマンドを定期的に使用してください。`docker-compose.production.yml`を含むディレクトリから実行してください。",
    "km": "ប្រើពាក្យបញ្ជាទាំងនេះជាប្រចាំដើម្បីគ្រប់គ្រងកំប៉ុង rtCloud របស់អ្នក។ រត់ពួកវាពីថតឯកសារដែលមាន `docker-compose.production.yml`។",
    "ko": "rtCloud 컨테이너를 관리하려면 이 명령어들을 정기적으로 사용하세요. `docker-compose.production.yml`이 있는 디렉터리에서 실행하세요.",
    "lt": "Naudokite šias komandas reguliariai rtCloud konteinerių valdymui. Vykdykite jas iš katalogo, kuriame yra `docker-compose.production.yml`.",
    "lv": "Izmantojiet šīs komandas regulāri, lai pārvaldītu rtCloud konteinerus. Palaidiet tās no direktorijas, kurā atrodas `docker-compose.production.yml`.",
    "nb": "Bruk disse kommandoene regelmessig for å administrere dine rtCloud-containere. Kjør dem fra katalogen som inneholder `docker-compose.production.yml`.",
    "nl": "Gebruik deze opdrachten regelmatig om uw rtCloud-containers te beheren. Voer ze uit vanuit de map met `docker-compose.production.yml`.",
    "pl": "Używaj tych poleceń regularnie do zarządzania kontenerami rtCloud. Uruchamiaj je z katalogu zawierającego `docker-compose.production.yml`.",
    "pt": "Utilize estes comandos regularmente para gerir os seus contentores rtCloud. Execute-os a partir do diretório que contém `docker-compose.production.yml`.",
    "pt-br": "Use esses comandos regularmente para gerenciar seus contêineres rtCloud. Execute-os a partir do diretório que contém `docker-compose.production.yml`.",
    "ru": "Используйте эти команды регулярно для управления контейнерами rtCloud. Запускайте их из директории с файлом `docker-compose.production.yml`.",
    "sk": "Používajte tieto príkazy pravidelne na správu kontajnerov rtCloud. Spúšťajte ich z adresára obsahujúceho `docker-compose.production.yml`.",
    "sq": "Përdorni këto komanda rregullisht për të menaxhuar kontejnerët tuaj rtCloud. Ekzekutojini nga drejtoria që përmban `docker-compose.production.yml`.",
    "sr": "Користите ове команде редовно за управљање вашим rtCloud контејнерима. Покрећите их из директоријума који садржи `docker-compose.production.yml`.",
    "sv": "Använd dessa kommandon regelbundet för att hantera dina rtCloud-containrar. Kör dem från katalogen som innehåller `docker-compose.production.yml`.",
    "te": "మీ rtCloud కంటైనర్‌లను నిర్వహించడానికి ఈ ఆదేశాలను క్రమంగా ఉపయోగించండి. వాటిని `docker-compose.production.yml` ఉన్న డైరెక్టరీ నుండి అమలు చేయండి.",
    "th": "ใช้คำสั่งเหล่านี้เป็นประจำเพื่อจัดการคอนเทนเนอร์ rtCloud ของคุณ รันจากไดเรกทอรีที่มี `docker-compose.production.yml`",
    "tr": "rtCloud konteynerlerinizi yönetmek için bu komutları düzenli olarak kullanın. Bunları `docker-compose.production.yml` dosyasını içeren dizinden çalıştırın.",
    "uk": "Використовуйте ці команди регулярно для управління контейнерами rtCloud. Запускайте їх з директорії, що містить `docker-compose.production.yml`.",
    "vi": "Sử dụng các lệnh này thường xuyên để quản lý các container rtCloud. Chạy chúng từ thư mục chứa `docker-compose.production.yml`.",
    "zh-hans": "定期使用这些命令管理您的 rtCloud 容器。在包含 `docker-compose.production.yml` 的目录中运行。",
    "zh-hant": "定期使用這些命令管理您的 rtCloud 容器。在包含 `docker-compose.production.yml` 的目錄中執行。",
}

CONF_INTRO = {
    "ar": "يتم كل التكوين من خلال متغيرات البيئة في ملف `.env` في جذر دليل النشر. يقرأ Docker Compose هذا الملف تلقائياً — لا حاجة لعلامة `--env-file`.\n\nالمتغيرات المحددة بـ **مطلوب** يجب تعيينها قبل تشغيل الحاويات. جميع الأخرى لها قيم افتراضية وهي اختيارية.",
    "bg": "Цялата конфигурация се извършва чрез променливи на средата в `.env` файла в основата на директорията за разгръщане. Docker Compose чете този файл автоматично — не е необходим флаг `--env-file`.\n\nПроменливите, отбелязани като **задължителни**, трябва да бъдат зададени преди стартиране на контейнерите. Всички останали имат стойности по подразбиране и са незадължителни.",
    "cs": "Veškerá konfigurace se provádí prostřednictvím proměnných prostředí v souboru `.env` v kořenovém adresáři nasazení. Docker Compose čte tento soubor automaticky — není potřeba příznak `--env-file`.\n\nProměnné označené jako **povinné** musí být nastaveny před spuštěním kontejnerů. Všechny ostatní mají výchozí hodnoty a jsou volitelné.",
    "da": "Al konfiguration sker via miljøvariabler i `.env`-filen i roden af din installationsmappe. Docker Compose læser denne fil automatisk — ingen `--env-file`-flag er nødvendigt.\n\nVariabler markeret **påkrævet** skal indstilles inden containerne startes. Alle andre har standardværdier og er valgfrie.",
    "de": "Die gesamte Konfiguration erfolgt über Umgebungsvariablen in der `.env`-Datei im Stammverzeichnis Ihres Bereitstellungsverzeichnisses. Docker Compose liest diese Datei automatisch — kein `--env-file`-Flag erforderlich.\n\nVariablen, die als **erforderlich** markiert sind, müssen vor dem Start der Container gesetzt werden. Alle anderen haben Standardwerte und sind optional.",
    "el": "Όλη η διαμόρφωση γίνεται μέσω μεταβλητών περιβάλλοντος στο αρχείο `.env` στη ρίζα του καταλόγου ανάπτυξης. Το Docker Compose διαβάζει αυτό το αρχείο αυτόματα — δεν χρειάζεται σημαία `--env-file`.\n\nΟι μεταβλητές που σημειώνονται ως **υποχρεωτικές** πρέπει να οριστούν πριν την εκκίνηση των containers. Όλες οι άλλες έχουν προεπιλεγμένες τιμές και είναι προαιρετικές.",
    "es": "Toda la configuración se realiza mediante variables de entorno en el archivo `.env` en la raíz del directorio de implementación. Docker Compose lee este archivo automáticamente — no se necesita el indicador `--env-file`.\n\nLas variables marcadas como **requeridas** deben establecerse antes de iniciar los contenedores. Todas las demás tienen valores predeterminados y son opcionales.",
    "fi": "Kaikki konfigurointi tehdään ympäristömuuttujien avulla `.env`-tiedostossa käyttöönottohakemiston juuressa. Docker Compose lukee tämän tiedoston automaattisesti — `--env-file`-lippua ei tarvita.\n\nMuuttujat, jotka on merkitty **pakollisiksi**, on asetettava ennen konttien käynnistämistä. Kaikilla muilla on oletusarvot ja ne ovat valinnaisia.",
    "fr": "Toute la configuration se fait via des variables d'environnement dans le fichier `.env` à la racine de votre répertoire de déploiement. Docker Compose lit ce fichier automatiquement — aucun indicateur `--env-file` n'est nécessaire.\n\nLes variables marquées **obligatoires** doivent être définies avant de démarrer les conteneurs. Toutes les autres ont des valeurs par défaut et sont optionnelles.",
    "hi": "सभी कॉन्फ़िगरेशन आपके डिप्लॉयमेंट डायरेक्टरी की जड़ में `.env` फ़ाइल में पर्यावरण चर के माध्यम से की जाती है। Docker Compose इस फ़ाइल को स्वचालित रूप से पढ़ता है — `--env-file` फ्लैग की आवश्यकता नहीं।\n\n**आवश्यक** चिह्नित चर कंटेनर शुरू करने से पहले सेट किए जाने चाहिए। बाकी सभी के डिफ़ॉल्ट मान हैं और वैकल्पिक हैं।",
    "hu": "Minden konfiguráció a telepítési könyvtár gyökerében lévő `.env` fájlban lévő környezeti változókon keresztül történik. A Docker Compose automatikusan olvassa ezt a fájlt — nincs szükség `--env-file` jelölőre.\n\nA **kötelező** jelöléssel ellátott változókat a konténerek indítása előtt kell beállítani. Minden más változónak van alapértéke és nem kötelező.",
    "id": "Semua konfigurasi dilakukan melalui variabel lingkungan di file `.env` di root direktori deployment Anda. Docker Compose membaca file ini secara otomatis — tidak diperlukan flag `--env-file`.\n\nVariabel yang ditandai **diperlukan** harus ditetapkan sebelum memulai container. Semua yang lain memiliki nilai default dan bersifat opsional.",
    "it": "Tutta la configurazione avviene tramite variabili d'ambiente nel file `.env` nella radice della directory di distribuzione. Docker Compose legge questo file automaticamente — nessun flag `--env-file` necessario.\n\nLe variabili contrassegnate come **obbligatorie** devono essere impostate prima di avviare i container. Tutte le altre hanno valori predefiniti e sono opzionali.",
    "ja": "すべての設定は、デプロイメントディレクトリのルートにある`.env`ファイルの環境変数を通じて行います。Docker Composeはこのファイルを自動的に読み込みます — `--env-file`フラグは不要です。\n\n**必須**と記載された変数はコンテナ起動前に設定する必要があります。それ以外はすべてデフォルト値があり、任意です。",
    "km": "ការកំណត់រចនាសម្ព័ន្ធទាំងអស់ត្រូវបានធ្វើឡើងតាមរយៈអថេរបរិស្ថានក្នុងឯកសារ `.env` នៅ root នៃថតឯកសារដំឡើងរបស់អ្នក។ Docker Compose អានឯកសារនេះដោយស្វ័យប្រវត្តិ — មិនត្រូវការ flag `--env-file`។\n\nអថេរដែលមានទំហំ **ចាំបាច់** ត្រូវតែកំណត់មុនពេលចាប់ផ្តើមកំប៉ុង។ ផ្សេងទៀតទាំងអស់មានតម្លៃលំនាំដើម ហើយជាជម្រើស។",
    "ko": "모든 구성은 배포 디렉터리 루트의 `.env` 파일에 있는 환경 변수를 통해 수행됩니다. Docker Compose가 이 파일을 자동으로 읽습니다 — `--env-file` 플래그가 필요하지 않습니다.\n\n**필수**로 표시된 변수는 컨테이너 시작 전에 설정해야 합니다. 나머지는 모두 기본값이 있고 선택 사항입니다.",
    "lt": "Visa konfigūracija atliekama naudojant aplinkos kintamuosius `.env` faile jūsų diegimo katalogo šaknyje. Docker Compose automatiškai skaito šį failą — `--env-file` žymė nereikalinga.\n\nKintamieji, pažymėti kaip **būtini**, turi būti nustatyti prieš paleidžiant konteinerius. Visi kiti turi numatytąsias reikšmes ir yra neprivalomi.",
    "lv": "Visa konfigurācija tiek veikta caur vides mainīgajiem `.env` failā jūsu izvietošanas direktorijas saknē. Docker Compose automātiski lasa šo failu — nav nepieciešams `--env-file` karodziņš.\n\nMainīgie, kas atzīmēti kā **obligāti**, jāiestata pirms konteineru palaišanas. Visiem pārējiem ir noklusējuma vērtības un tie ir neobligāti.",
    "nb": "All konfigurasjon gjøres via miljøvariabler i `.env`-filen i roten av distribusjonskatalogen. Docker Compose leser denne filen automatisk — ingen `--env-file`-flagg er nødvendig.\n\nVariabler merket **påkrevd** må settes før containerne startes. Alle andre har standardverdier og er valgfrie.",
    "nl": "Alle configuratie wordt gedaan via omgevingsvariabelen in het `.env`-bestand in de root van uw implementatiemap. Docker Compose leest dit bestand automatisch — geen `--env-file`-vlag nodig.\n\nVariabelen gemarkeerd als **vereist** moeten worden ingesteld voordat de containers worden gestart. Alle andere hebben standaardwaarden en zijn optioneel.",
    "pl": "Cała konfiguracja odbywa się za pomocą zmiennych środowiskowych w pliku `.env` w katalogu głównym wdrożenia. Docker Compose czyta ten plik automatycznie — flaga `--env-file` nie jest potrzebna.\n\nZmienne oznaczone jako **wymagane** muszą być ustawione przed uruchomieniem kontenerów. Wszystkie inne mają wartości domyślne i są opcjonalne.",
    "pt": "Toda a configuração é feita através de variáveis de ambiente no ficheiro `.env` na raiz do diretório de implementação. O Docker Compose lê este ficheiro automaticamente — não é necessário o sinalizador `--env-file`.\n\nAs variáveis marcadas como **obrigatórias** devem ser definidas antes de iniciar os contentores. Todas as outras têm valores predefinidos e são opcionais.",
    "pt-br": "Toda a configuração é feita através de variáveis de ambiente no arquivo `.env` na raiz do diretório de implantação. O Docker Compose lê esse arquivo automaticamente — nenhum sinalizador `--env-file` é necessário.\n\nVariáveis marcadas como **obrigatórias** devem ser definidas antes de iniciar os contêineres. Todas as outras têm valores padrão e são opcionais.",
    "ru": "Вся конфигурация выполняется через переменные окружения в файле `.env` в корне директории развёртывания. Docker Compose читает этот файл автоматически — флаг `--env-file` не нужен.\n\nПеременные, отмеченные как **обязательные**, должны быть установлены до запуска контейнеров. У всех остальных есть значения по умолчанию, и они необязательны.",
    "sk": "Celá konfigurácia sa vykonáva prostredníctvom premenných prostredia v súbore `.env` v koreňovom adresári nasadenia. Docker Compose číta tento súbor automaticky — nie je potrebný príznak `--env-file`.\n\nPremenné označené ako **povinné** musia byť nastavené pred spustením kontajnerov. Všetky ostatné majú predvolené hodnoty a sú voliteľné.",
    "sq": "E gjithë konfigurimi bëhet nëpërmjet variablave të mjedisit në skedarin `.env` në rrënjën e direktorisë suaj të vendosjes. Docker Compose lexon këtë skedar automatikisht — nuk nevojitet flamuri `--env-file`.\n\nVariablat e shënuara si **të detyrueshme** duhet të vendosen para fillimit të kontejnerëve. Të gjithë të tjerët kanë vlera parazgjedhje dhe janë opsionale.",
    "sr": "Сва конфигурација се врши кроз променљиве окружења у `.env` датотеци у корену директоријума за примену. Docker Compose чита ову датотеку аутоматски — није потребна заставица `--env-file`.\n\nПроменљиве означене као **обавезне** морају бити постављене пре покретања контејнера. Све остале имају подразумеване вредности и нису обавезне.",
    "sv": "All konfiguration sker via miljövariabler i `.env`-filen i roten av din driftsättningskatalog. Docker Compose läser den här filen automatiskt — ingen `--env-file`-flagga behövs.\n\nVariabler markerade **obligatoriska** måste anges innan containrarna startas. Alla andra har standardvärden och är valfria.",
    "te": "అన్ని కాన్ఫిగరేషన్ మీ విన్యాస డైరెక్టరీ రూట్‌లో `.env` ఫైల్‌లో పర్యావరణ వేరియబుల్స్ ద్వారా చేయబడుతుంది. Docker Compose ఈ ఫైల్‌ను స్వయంచాలకంగా చదువుతుంది — `--env-file` ఫ్లాగ్ అవసరం లేదు.\n\n**అవసరమైన** అని గుర్తించబడిన వేరియబుల్స్ కంటైనర్‌లు ప్రారంభించే ముందు సెట్ చేయబడాలి. మిగతా అన్నింటికీ డిఫాల్ట్ విలువలు ఉన్నాయి మరియు ఐచ్ఛికం.",
    "th": "การกำหนดค่าทั้งหมดทำผ่านตัวแปรสภาพแวดล้อมในไฟล์ `.env` ที่รูทของไดเรกทอรีการติดตั้ง Docker Compose อ่านไฟล์นี้โดยอัตโนมัติ — ไม่ต้องใช้ flag `--env-file`\n\nตัวแปรที่ทำเครื่องหมาย **จำเป็น** ต้องตั้งค่าก่อนเริ่มคอนเทนเนอร์ ตัวอื่นๆ มีค่าเริ่มต้นและเป็นทางเลือก",
    "tr": "Tüm yapılandırma, dağıtım dizininizin kökündeki `.env` dosyasındaki ortam değişkenleri aracılığıyla yapılır. Docker Compose bu dosyayı otomatik olarak okur — `--env-file` bayrağı gerekli değildir.\n\n**Zorunlu** olarak işaretlenen değişkenler, kapsayıcılar başlatılmadan önce ayarlanmalıdır. Diğerlerinin varsayılan değerleri vardır ve isteğe bağlıdır.",
    "uk": "Вся конфігурація виконується через змінні середовища у файлі `.env` у корені директорії розгортання. Docker Compose читає цей файл автоматично — прапор `--env-file` не потрібен.\n\nЗмінні, позначені як **обов'язкові**, мають бути встановлені до запуску контейнерів. Всі інші мають значення за замовчуванням і є необов'язковими.",
    "vi": "Tất cả cấu hình được thực hiện thông qua các biến môi trường trong tệp `.env` ở thư mục gốc của thư mục triển khai. Docker Compose đọc tệp này tự động — không cần cờ `--env-file`.\n\nCác biến được đánh dấu **bắt buộc** phải được đặt trước khi khởi động các container. Tất cả các biến khác có giá trị mặc định và là tùy chọn.",
    "zh-hans": "所有配置通过部署目录根目录中的 `.env` 文件中的环境变量完成。Docker Compose 自动读取此文件 — 不需要 `--env-file` 标志。\n\n标记为**必填**的变量必须在启动容器前设置。其他所有变量都有默认值，是可选的。",
    "zh-hant": "所有配置透過部署目錄根目錄中的 `.env` 文件中的環境變數完成。Docker Compose 自動讀取此文件 — 不需要 `--env-file` 標誌。\n\n標記為**必填**的變數必須在啟動容器前設定。其他所有變數都有預設值，是可選的。",
}

# ── English body sources (technical content unchanged) ────────

SSO_BODY_EN = """{intro}

| Option | Best For |
|--------|----------|
| [Embedded Keycloak](#embedded-keycloak) | Organizations that want a fully self-contained SSO server bundled with rtCloud |
| [External OIDC Provider](#external-oidc-provider) | Organizations already running an identity provider (Auth0, Authentik, Okta, Supabase, etc.) |
| [Azure Active Directory](#azure-active-directory) | Organizations using Microsoft 365 or Azure AD |

Without SSO configured, users log in with local rtCloud accounts managed through the admin panel.

---

## Embedded Keycloak

The deployment includes an optional Keycloak container that runs alongside rtCloud. Keycloak is pre-configured with an rtSurvey realm and ready to use.

### Requirements

- A domain name with HTTPS (Keycloak requires HTTPS in production)
- At least 4 GB RAM on the server (Keycloak adds ~512 MB memory usage)

### Setup

**1. Configure environment variables in `.env`:**

```dotenv
# Enable the embedded Keycloak container
EMBED_KEYCLOAK=true

# Keycloak URLs — use your actual domain
KEYCLOAK_URL=https://rtcloud.example.com/auth
KC_HOSTNAME=https://rtcloud.example.com/auth
KC_HOSTNAME_STRICT=false

# Realm and client settings (match the imported realm JSON)
KEYCLOAK_REALM=rtsurvey
KEYCLOAK_CLIENT_ID=rtsurvey-app
KEYCLOAK_CLIENT_SECRET=your-client-secret-here

# Keycloak admin credentials
KEYCLOAK_ADMIN_USER=admin
KEYCLOAK_ADMIN_PASSWORD=change_me_keycloak_admin_password

# Keycloak database (created automatically)
KEYCLOAK_DB=keycloak
KEYCLOAK_DB_USER=keycloak
KEYCLOAK_DB_PASSWORD=change_me_keycloak_db_password

# Port Keycloak listens on (host-side, proxied by Nginx)
KEYCLOAK_PORT=8091
```

**2. Start with the embedded Keycloak profile:**

```bash
docker compose -f docker-compose.production.yml --profile embed-keycloak up -d
```

**3. Verify Keycloak is healthy:**

```bash
docker compose -f docker-compose.production.yml ps
```

The `rtcloud-keycloak` container should show `Up (healthy)` after 2–3 minutes.

**4. Access the Keycloak admin console:**

```
https://rtcloud.example.com/auth/admin
```

Log in with `KEYCLOAK_ADMIN_USER` and `KEYCLOAK_ADMIN_PASSWORD`.

### What Is Pre-Configured

The embedded Keycloak starts with a pre-imported `rtsurvey` realm that includes:

- Client configuration for the web application
- Default user roles (`admin`, `project_manager`, `enumerator`, `analyst`)
- Session and token settings optimized for rtSurvey

You can add users directly in the Keycloak admin console or connect Keycloak to an upstream identity provider (LDAP, SAML).

### Nginx Routing

When using the cloud deployment scripts, Nginx is configured to proxy both services:

| Path | Backend |
|------|---------|
| `/` | rtCloud app on `127.0.0.1:8080` |
| `/auth/` | Keycloak on `127.0.0.1:8090` |

---

## External OIDC Provider

Connect rtCloud to any OpenID Connect-compatible identity provider. This approach does not require the Keycloak container.

### Supported Providers

Any OIDC-compliant provider works, including:
- Authentik
- Auth0
- Okta
- Keycloak (external instance)
- Supabase
- Google (for Google Workspace organizations)
- GitHub (via OAuth apps with OIDC extension)

### Setup

**1. Register rtCloud as an OIDC client in your identity provider.**

You will need:
- A **client ID** and **client secret**
- To register the **redirect URI**: `https://rtcloud.example.com/auth/callback`
- For mobile app support, also register: `vn.rta.rtsurvey.auth://callback`

**2. Configure environment variables in `.env`:**

```dotenv
# OIDC discovery URL (provider-specific — check your IdP documentation)
OIDC_ISSUER_URL=https://your-identity-provider.com

# Client credentials from your identity provider
OIDC_CLIENT_ID=rtcloud-app
OIDC_CLIENT_SECRET=your-client-secret-here

# Scopes to request (openid, profile, and email are typically sufficient)
OIDC_SCOPE=openid profile email

# Redirect URI registered in your identity provider
OIDC_REDIRECT_URI=https://rtcloud.example.com/auth/callback

# Optional: separate mobile app client
OIDC_MOBILE_CLIENT_ID=rtcloud-mobile
OIDC_MOBILE_REDIRECT_URI=vn.rta.rtsurvey.auth://callback

# Set to true to auto-create rtCloud accounts for new OIDC users
OPEN_REGISTRATION=false
```

**3. Restart the app container to apply the changes:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

### Auto-Provisioning Users

When `OPEN_REGISTRATION=true`, rtCloud automatically creates a local account the first time a user signs in via OIDC. The account is populated with the user's name and email from the ID token.

When `OPEN_REGISTRATION=false` (default), an rtCloud administrator must create the user account first, and the OIDC identity is linked on first login.

### Custom Endpoints

If your provider does not support OIDC discovery (`.well-known/openid-configuration`), you can set endpoints manually:

```dotenv
OIDC_AUTHORIZATION_ENDPOINT=https://your-provider.com/oauth2/authorize
OIDC_TOKEN_ENDPOINT=https://your-provider.com/oauth2/token
OIDC_USERINFO_ENDPOINT=https://your-provider.com/oauth2/userinfo
```

---

## Azure Active Directory

Integrate rtCloud with your organization's Microsoft Azure AD tenant.

### Setup

**1. Register a new app in the [Azure Portal](https://portal.azure.com):**

   - Go to **Azure Active Directory** → **App registrations** → **New registration**
   - Name: `rtCloud`
   - Redirect URI: `https://rtcloud.example.com/auth/callback` (Web type)
   - After creation, note the **Application (client) ID** and **Directory (tenant) ID**
   - Under **Certificates & secrets**, create a new client secret

**2. Configure environment variables in `.env`:**

```dotenv
AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**3. Restart the app container:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Users in your Azure AD tenant can now log in to rtCloud using their Microsoft credentials.

---

## Disabling SSO

To revert to local authentication, remove or comment out all SSO-related variables from `.env`, then restart the app container:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

If you were using embedded Keycloak, stop it by omitting the `--profile embed-keycloak` flag and running `docker compose down` followed by `up -d` without the profile.
"""

MAINT_BODY_EN = """INTRO_PLACEHOLDER

```bash
# Check status and health of all containers
docker compose -f docker-compose.production.yml ps

# View live logs (all services)
docker compose -f docker-compose.production.yml logs -f

# View logs for the app only
docker compose -f docker-compose.production.yml logs -f rtcloud

# Restart a single container
docker compose -f docker-compose.production.yml restart rtcloud

# Stop all services
docker compose -f docker-compose.production.yml down

# Start all services
docker compose -f docker-compose.production.yml up -d

# Open a shell inside the app container
docker compose -f docker-compose.production.yml exec rtcloud bash
```

---

## Upgrading

rtCloud updates are distributed as new Docker image tags. Upgrading pulls the latest image and recreates the app container. Database migrations run automatically on startup.

**1. Pull the latest image:**

```bash
docker compose -f docker-compose.production.yml pull
```

**2. Recreate the app container:**

```bash
docker compose -f docker-compose.production.yml up -d
```

Docker replaces only the containers whose image has changed. The MySQL container and all named volumes are unaffected.

### Pinning a Version

To upgrade to a specific version instead of `latest`, update `RTCLOUD_IMAGE` in `.env`:

```dotenv
RTCLOUD_IMAGE=rtawebteam/rta-smartsurvey:1.2.3
```

Then run `docker compose pull` and `up -d` as above.

### Downgrading

Downgrading is generally not recommended, as database migrations cannot be reversed. If a downgrade is necessary, restore from a database backup taken before the upgrade.

---

## Backup and Restore

### Backup the Database

Run this command to export the application database to a SQL file:

```bash
docker compose -f docker-compose.production.yml exec mysql \\
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \\
  > backup-$(date +%Y%m%d-%H%M%S).sql
```

The backup file is written to your current directory on the host.

### Restore the Database

```bash
docker compose -f docker-compose.production.yml exec -T mysql \\
  mysql -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \\
  < backup-20240101-120000.sql
```

### Backup Uploaded Files

Survey submissions often include uploaded files (photos, audio, documents) stored in named Docker volumes. Back them up separately from the database:

```bash
# Backup uploads
docker run --rm \\
  -v rtcloud_uploads:/data \\
  -v "$(pwd):/backup" \\
  alpine tar czf /backup/uploads-$(date +%Y%m%d).tar.gz -C /data .

# Backup audio recordings
docker run --rm \\
  -v rtcloud_audios:/data \\
  -v "$(pwd):/backup" \\
  alpine tar czf /backup/audios-$(date +%Y%m%d).tar.gz -C /data .
```

Replace `rtcloud_uploads` and `rtcloud_audios` with your actual volume names (prefixed by `COMPOSE_PROJECT_NAME`) if you changed the default.

### Restore Uploaded Files

```bash
docker run --rm \\
  -v rtcloud_uploads:/data \\
  -v "$(pwd):/backup" \\
  alpine tar xzf /backup/uploads-20240101.tar.gz -C /data
```

### Automated Daily Backups

Add a cron job on the host to run backups automatically. Edit the root crontab with `crontab -e`:

```cron
# Daily database backup at 2:00 AM, keep 30 days of history
0 2 * * * cd /opt/rtcloud && docker compose -f docker-compose.production.yml exec -T mysql \\
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \\
  > /backups/db-$(date +\\%Y\\%m\\%d).sql && \\
  find /backups -name "db-*.sql" -mtime +30 -delete
```

---

## Troubleshooting

### App container not starting

Check the container logs for error messages:

```bash
docker compose -f docker-compose.production.yml logs rtcloud
```

Common causes:
- Missing or invalid environment variables in `.env`
- MySQL not yet ready (wait 60 seconds and check again)
- Port conflict — another process is already using `APP_PORT`

### MySQL not healthy

```bash
docker compose -f docker-compose.production.yml logs mysql
```

Common causes:
- `MYSQL_ROOT_PASSWORD` not set in `.env`
- Corrupted data volume (rare — check disk space with `df -h`)

MySQL can take 30–60 seconds to initialize on the very first boot. Wait and check again before assuming failure.

### Port already in use

Change `APP_PORT` or `SHINY_PORT` in `.env` to a free port, then recreate the containers:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate
```

To find what is using a port on the host:

```bash
lsof -i :8080
```

### 400 CSRF Token Could Not Be Verified

This error appears in local or reverse-proxy environments where the request origin does not match the expected host. Disable CSRF validation for local development only:

```dotenv
CSRF_VALIDATION_ENABLED=false
```

Then restart the app:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

> Do not disable CSRF validation in production. If this error occurs in production, ensure your reverse proxy is forwarding the correct `Host` and `X-Forwarded-For` headers.

### Forgot the Admin Password

Reset the admin password directly in the database. Connect to the MySQL container and update the password hash:

**Step 1** — Generate the new password hash. Replace `newpassword` with your desired password:

```bash
docker compose -f docker-compose.production.yml exec rtcloud php -r "
  \\$salt = trim(shell_exec(\\"mysql -h mysql -u root -p\\\\\\"\${MYSQL_ROOT_PASSWORD}\\\\\\" \\${MYSQL_DATABASE} -se \\\\\\"SELECT salt FROM ss_user WHERE username='admin';\\\\\\"\"));
  echo md5(\\$salt . 'newpassword') . PHP_EOL;
"
```

**Step 2** — Update the hash in the database:

```bash
docker compose -f docker-compose.production.yml exec mysql \\
  mysql -u root -p"${MYSQL_ROOT_PASSWORD}" smartsurvey \\
  -e "UPDATE ss_user SET password='<hash_from_step_1>' WHERE username='admin';"
```

### Container keeps restarting

Check if the health check is failing:

```bash
docker compose -f docker-compose.production.yml ps
docker inspect rtcloud-app --format '{{{{json .State.Health}}}}'
```

The app health check calls the `/health` endpoint. If it fails repeatedly, check the application logs for startup errors.

### Disk space full

Identify what is consuming space:

```bash
# Check host disk usage
df -h

# Check Docker disk usage (images, containers, volumes)
docker system df

# Remove unused images and stopped containers (safe to run)
docker system prune
```

Do not use `docker system prune --volumes` as this will delete application data.

---

## Health Checks

Each service has an automatic health check. Container status reflects the result:

| Container | Check Method | Start Period | Interval |
|-----------|-------------|-------------|----------|
| `rtcloud-app` | HTTP GET `/health` | 90 seconds | 30 seconds |
| `rtcloud-mysql` | `mysqladmin ping` | 30 seconds | 10 seconds |
| `rtcloud-keycloak` | HTTP GET `:9000/health/live` | 120 seconds | 30 seconds |

Containers with a failing health check are automatically restarted according to the `RESTART_POLICY` setting (default: `unless-stopped`).
"""

CONF_BODY_EN = """{intro}

---

## Project

These variables define the identity and access point of your rtCloud instance.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `PROJECT_ID` | — | **Yes** | Unique identifier for this deployment. No spaces or special characters. Used as a prefix for internal naming. |
| `PROJECT_URL` | — | **Yes** | Domain name or IP address where users access the app (e.g., `rtcloud.example.com` or `192.168.1.100`). |
| `PROJECT_TYPE` | `rtsurvey` | No | Platform variant to activate. Options: `rtwork`, `rtsurvey`, `rthome`. |
| `PROJECT_PORT` | `80` | No | Port the application listens on inside the container. Do not change unless you know what you are doing. |
| `HTTP_PROTOCOL` | `https` | No | Protocol used to construct internal URLs. Set to `http` if you are not using SSL. |

---

## Database

MySQL connection credentials. The database is managed automatically by the MySQL container — you only need to set strong passwords.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `MYSQL_DATABASE` | `smartsurvey` | No | Name of the application database. |
| `MYSQL_USER` | `smartsurvey` | No | MySQL user for the application. |
| `MYSQL_PASSWORD` | — | **Yes** | Password for `MYSQL_USER`. Use a strong, unique value. |
| `MYSQL_ROOT_PASSWORD` | — | **Yes** | MySQL root password. Required for database initialization and admin operations. |
| `MYSQL_HOST` | `mysql` | No | MySQL hostname. Use the default unless you are connecting to an external database. |
| `MYSQL_PORT` | `3306` | No | MySQL port. |

---

## Admin Account

The admin account is created automatically on the first boot of a fresh database.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `ADMIN_PASSWORD` | `admin` | **Yes** | Password for the built-in `admin` user. Set this before first boot. Has no effect if the database already exists. |

> After first login, change the admin password from the **Account Settings** page in the web UI.

---

## Ports

Control which host ports the application binds to.

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_PORT` | `8080` | Host port for the main web UI. Change this if port 8080 is already in use on your server. |
| `SHINY_PORT` | `3838` | Host port for the Shiny analytics server. |

---

## Runtime

| Variable | Default | Description |
|----------|---------|-------------|
| `RUN_ENV` | `prod` | Runtime environment. Use `prod` for production deployments, `dev` for local development. |
| `RUN_MODE` | `admin` | Container role. `admin` runs the full stack (web + queue + cron). `worker` runs background processing only (for horizontal scaling). |
| `TZ` | `Asia/Ho_Chi_Minh` | Server timezone. Affects log timestamps, cron schedules, and date display. Use a [TZ database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (e.g., `UTC`, `America/New_York`, `Europe/London`). |
| `LOG_LEVEL` | `info` | Application log verbosity. Options: `debug`, `info`, `warning`, `error`. |
| `COMPOSE_PROJECT_NAME` | `rtcloud` | Prefix applied to all Docker container and volume names. Change this when running multiple rtCloud instances on the same host. |
| `RESTART_POLICY` | `unless-stopped` | Docker container restart behavior. Options: `no`, `always`, `on-failure`, `unless-stopped`. |
| `RTCLOUD_IMAGE` | `rtawebteam/rta-smartsurvey:survey-dockerize` | Docker image to use. Change the tag to pin a specific version. |
| `REQUIRE_LICENSE` | `false` | Enable license key validation on startup. Contact RTA for license information. |

---

## Security

| Variable | Default | Description |
|----------|---------|-------------|
| `CSRF_VALIDATION_ENABLED` | `true` | Enable CSRF token validation. Keep this `true` in production. Set to `false` only in local development if you encounter `400 CSRF token could not be verified` errors. |
| `GII_ENABLED` | `false` | Enable the Yii framework code generator tool. **Never enable in production.** |

---

## SSO — Embedded Keycloak

Enable the bundled Keycloak container for full-featured enterprise SSO. Requires a domain with HTTPS.

| Variable | Default | Description |
|----------|---------|-------------|
| `EMBED_KEYCLOAK` | `false` | Set to `true` to start the embedded Keycloak container. Activates the `embed-keycloak` Docker Compose profile. |
| `KEYCLOAK_URL` | — | Full URL of the Keycloak server (e.g., `https://rtcloud.example.com/auth`). |
| `KEYCLOAK_REALM` | — | Keycloak realm name (e.g., `rtsurvey`). |
| `KEYCLOAK_CLIENT_ID` | — | Keycloak client ID for the rtCloud application. |
| `KEYCLOAK_CLIENT_SECRET` | — | Keycloak client secret. Generate this from the Keycloak admin console. |
| `KEYCLOAK_ADMIN_USER` | `admin` | Keycloak administrator username. |
| `KEYCLOAK_ADMIN_PASSWORD` | — | Keycloak administrator password. |
| `KEYCLOAK_DB` | `keycloak` | Database name for Keycloak. Created automatically on first boot. |
| `KEYCLOAK_DB_USER` | `keycloak` | Database user for Keycloak. |
| `KEYCLOAK_DB_PASSWORD` | — | Database password for the Keycloak user. |
| `KC_HOSTNAME` | — | Keycloak frontend URL (e.g., `https://rtcloud.example.com/auth`). |
| `KC_HOSTNAME_STRICT` | `false` | Enforce strict hostname matching. Set to `true` in production with a fixed domain. |

See [SSO Authentication](sso-authentication#embedded-keycloak) for the complete setup guide.

---

## SSO — External OIDC Provider

Connect to an existing OIDC-compatible identity provider (Supabase, Auth0, Authentik, Okta, etc.).

| Variable | Default | Description |
|----------|---------|-------------|
| `OIDC_ISSUER_URL` | — | OIDC issuer discovery URL (e.g., `https://accounts.google.com`). |
| `OIDC_CLIENT_ID` | — | Client ID registered in your identity provider. |
| `OIDC_CLIENT_SECRET` | — | Client secret from your identity provider. |
| `OIDC_SCOPE` | `openid profile email` | Space-separated list of OIDC scopes to request. |
| `OIDC_REDIRECT_URI` | — | Callback URL for the web app (e.g., `https://rtcloud.example.com/auth/callback`). |
| `OIDC_MOBILE_CLIENT_ID` | — | Separate client ID for the rtSurvey mobile app. |
| `OIDC_MOBILE_REDIRECT_URI` | — | Mobile app callback URI (e.g., `vn.rta.rtsurvey.auth://callback`). |
| `OPEN_REGISTRATION` | `false` | Automatically create rtCloud accounts for users who authenticate via OIDC for the first time. |
| `OIDC_AUTHORIZATION_ENDPOINT` | — | Override the authorization endpoint URL (leave blank to use discovery). |
| `OIDC_TOKEN_ENDPOINT` | — | Override the token endpoint URL (leave blank to use discovery). |
| `OIDC_USERINFO_ENDPOINT` | — | Override the userinfo endpoint URL (leave blank to use discovery). |

---

## SSO — Azure Active Directory

| Variable | Description |
|----------|-------------|
| `AZURE_CLIENT_ID` | Azure AD application (client) ID. |
| `AZURE_TENANT_ID` | Azure AD directory (tenant) ID. |

---

## Optional Integrations

### Stata

| Variable | Default | Description |
|----------|---------|-------------|
| `STATA_ENABLED` | `false` | Enable Stata statistical software integration for data analysis. |
| `STATA_BIN_PATH` | `/usr/bin/stata` | Absolute path to the Stata binary inside the container. |

### Elasticsearch

| Variable | Description |
|----------|-------------|
| `ES_HOST` | Elasticsearch host (e.g., `http://elasticsearch:9200`). |
| `ES_PORT` | Elasticsearch port. |

### Matomo Analytics

| Variable | Description |
|----------|-------------|
| `PIWIK_URL` | Matomo (Piwik) server URL. |
| `PIWIK_ID` | Matomo site ID. |
| `PIWIK_SECRET` | Matomo authentication token. |

### OpenCPU (R Computation)

| Variable | Description |
|----------|-------------|
| `OCPU_HOST` | OpenCPU server URL for R-based statistical computation. |

### RtBox Integration

| Variable | Description |
|----------|-------------|
| `RTBOX_HOST` | RtBox service host URL. |
| `RTBOX_USER_API` | RtBox user API key. |
| `RTBOX_BASIC_AUTH` | Basic authentication credentials for RtBox. |

### Matrix Messaging

| Variable | Description |
|----------|-------------|
| `MATRIX_HOMESERVER_HOST` | Matrix homeserver host. |
| `MATRIX_HOMESERVER_PORT` | Matrix homeserver port. |

---

## Data Volumes

All application data is stored in named Docker volumes. Volumes are automatically created on first startup and persist across container restarts and updates.

| Volume | Mount Point | Contents |
|--------|-------------|----------|
| `rtcloud_mysql_data` | `/var/lib/mysql` | MySQL database files |
| `rtcloud_uploads` | `…/uploads` | Files uploaded by survey respondents |
| `rtcloud_audios` | `…/audios` | Audio recordings |
| `rtcloud_downloads` | `…/downloads` | Generated export files |
| `rtcloud_gallery` | `…/gallery` | Gallery images |
| `rtcloud_voicemail` | `…/voicemail` | Voicemail recordings |
| `rtcloud_analytics` | `…/analytics` | Analytics data |
| `rtcloud_aggregate` | `…/aggregate` | Aggregated survey results |
| `rtcloud_converter` | `…/converter` | Data conversion outputs |
| `rtcloud_shiny_data` | `/srv/shiny-server/smartsurvey` | Shiny server R scripts |
| `rtcloud_shiny_logs` | `/var/log/shiny-server` | Shiny server logs |
| `rtcloud_assets` | `…/assets` | Web assets (CSS, JS) |
| `rtcloud_runtime` | `…/protected/runtime` | Application runtime cache |
| `rtcloud_cache` | `…/cache` | Application cache |
| `rtcloud_tmp` | `…/tmp` | Temporary files |

Volume names are prefixed by the value of `COMPOSE_PROJECT_NAME` (default: `rtcloud`).

List all volumes for your deployment:

```bash
docker volume ls | grep rtcloud
```
"""

# ── Section heading translations ─────────────────────────────

MAINT_COMMON_CMDS = {
    "ar":"الأوامر الشائعة","bg":"Общи команди","cs":"Běžné příkazy","da":"Almindelige kommandoer",
    "de":"Häufige Befehle","el":"Κοινές Εντολές","es":"Comandos comunes","fi":"Yleiset komennot",
    "fr":"Commandes courantes","hi":"सामान्य कमांड","hu":"Általános parancsok","id":"Perintah Umum",
    "it":"Comandi comuni","ja":"よく使うコマンド","km":"ពាក្យបញ្ជាទូទៅ","ko":"일반 명령어",
    "lt":"Dažniausios komandos","lv":"Biežākās komandas","nb":"Vanlige kommandoer","nl":"Veelgebruikte opdrachten",
    "pl":"Typowe polecenia","pt":"Comandos comuns","pt-br":"Comandos comuns","ru":"Общие команды",
    "sk":"Bežné príkazy","sq":"Komandat e zakonshme","sr":"Уобичајене команде","sv":"Vanliga kommandon",
    "te":"సాధారణ ఆదేశాలు","th":"คำสั่งทั่วไป","tr":"Yaygın Komutlar","uk":"Загальні команди",
    "vi":"Các lệnh thông dụng","zh-hans":"常用命令","zh-hant":"常用命令",
}

# ── Build functions ───────────────────────────────────────────

def frontmatter(meta, title, desc):
    lines = ["---"]
    lines.append(f'weight: {meta["weight"]}')
    lines.append(f'title: "{title}"')
    lines.append(f'date: "{meta["date"]}"')
    lines.append(f'lastmod: "{meta["lastmod"]}"')
    lines.append(f'draft: {meta["draft"]}')
    lines.append(f'author: "{meta["author"]}"')
    lines.append(f'icon: "{meta["icon"]}"')
    lines.append(f'toc: {meta["toc"]}')
    lines.append(f'description: "{desc}"')
    lines.append("---")
    return "\n".join(lines)


def write(rel, lang, content):
    path = os.path.join(BASE, lang, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


count = 0

for lang in LANGUAGES:
    # ── SSO ──────────────────────────────────────────────────
    fm = frontmatter(SSO_META, SSO_TITLES[lang], SSO_DESCS[lang])
    body = SSO_BODY_EN.format(intro=SSO_INTRO[lang])
    write("docs/getting-started/self-hosting/sso-authentication.md", lang, fm + "\n\n" + body.rstrip() + "\n")
    count += 1

    # ── Maintenance ──────────────────────────────────────────
    fm = frontmatter(MAINT_META, MAINT_TITLES[lang], MAINT_DESCS[lang])
    cmd_heading = MAINT_COMMON_CMDS[lang]
    intro = MAINT_INTRO[lang]
    body = f"## {cmd_heading}\n\n{intro}\n\n" + MAINT_BODY_EN.replace("INTRO_PLACEHOLDER\n\n", "").lstrip("\n")
    write("docs/getting-started/self-hosting/maintenance.md", lang, fm + "\n\n" + body.rstrip() + "\n")
    count += 1

    # ── Configuration ────────────────────────────────────────
    fm = frontmatter(CONF_META, CONF_TITLES[lang], CONF_DESCS[lang])
    body = CONF_BODY_EN.format(intro=CONF_INTRO[lang])
    write("docs/getting-started/self-hosting/configuration.md", lang, fm + "\n\n" + body.rstrip() + "\n")
    count += 1

print(f"Written {count} files (sso + maintenance + configuration).")
