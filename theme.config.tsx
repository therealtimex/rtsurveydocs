import React, { useEffect, useRef, useState } from 'react';
import { DocsThemeConfig } from 'nextra-theme-docs';
import { useRouter } from 'next/router';

const LanguageSwitcher = () => {
  const { asPath } = useRouter();
  const [currentLocale, setCurrentLocale] = useState('en');
  const [isOpen, setIsOpen] = useState(false);
  const [isDark, setIsDark] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const update = () => setIsDark(document.documentElement.classList.contains('dark'));
    update();
    const observer = new MutationObserver(update);
    observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });
    return () => observer.disconnect();
  }, []);

  // Close dropdown on outside click (avoids onBlur/onClick race condition)
  useEffect(() => {
    if (!isOpen) return;
    const handleOutside = (e: MouseEvent) => {
      if (containerRef.current && !containerRef.current.contains(e.target as Node)) {
        setIsOpen(false);
      }
    };
    document.addEventListener('mousedown', handleOutside);
    return () => document.removeEventListener('mousedown', handleOutside);
  }, [isOpen]);

  const ALL_LANGUAGES = [
  {
    "code": "en",
    "name": "English"
  },
  {
    "code": "id",
    "name": "Bahasa Indonesia"
  },
  {
    "code": "cs",
    "name": "Čeština"
  },
  {
    "code": "da",
    "name": "Dansk"
  },
  {
    "code": "de",
    "name": "Deutsch"
  },
  {
    "code": "es",
    "name": "Español"
  },
  {
    "code": "fr",
    "name": "Français"
  },
  {
    "code": "it",
    "name": "Italiano"
  },
  {
    "code": "lv",
    "name": "Latviešu"
  },
  {
    "code": "lt",
    "name": "Lietuvių"
  },
  {
    "code": "hu",
    "name": "Magyar"
  },
  {
    "code": "nl",
    "name": "Nederlands"
  },
  {
    "code": "nb",
    "name": "Norsk Bokmål"
  },
  {
    "code": "pl",
    "name": "Polski"
  },
  {
    "code": "pt",
    "name": "Português"
  },
  {
    "code": "pt-br",
    "name": "Português (Brasil)"
  },
  {
    "code": "sq",
    "name": "Shqip"
  },
  {
    "code": "sk",
    "name": "Slovenčina"
  },
  {
    "code": "sr",
    "name": "Srpski"
  },
  {
    "code": "fi",
    "name": "Suomi"
  },
  {
    "code": "sv",
    "name": "Svenska"
  },
  {
    "code": "vi",
    "name": "Tiếng Việt"
  },
  {
    "code": "tr",
    "name": "Türkçe"
  },
  {
    "code": "el",
    "name": "Ελληνικά"
  },
  {
    "code": "bg",
    "name": "Български"
  },
  {
    "code": "ru",
    "name": "Русский"
  },
  {
    "code": "uk",
    "name": "Українська"
  },
  {
    "code": "ar",
    "name": "العربية"
  },
  {
    "code": "hi",
    "name": "हिन्दी"
  },
  {
    "code": "te",
    "name": "తెలుగు"
  },
  {
    "code": "th",
    "name": "ไทย"
  },
  {
    "code": "km",
    "name": "ភាសាខ្មែរ"
  },
  {
    "code": "ko",
    "name": "한국어"
  },
  {
    "code": "ja",
    "name": "日本語"
  },
  {
    "code": "zh-hans",
    "name": "简体中文"
  },
  {
    "code": "zh-hant",
    "name": "繁體中文"
  }
];

  useEffect(() => {
    // Determine current locale from URL path
    const path = window.location.pathname;
    const pathParts = path.split('/');
    // Check if first part is a known locale (excluding empty string from leading slash)
    const firstPart = pathParts[1];
    if (firstPart && ALL_LANGUAGES.some(l => l.code === firstPart)) {
      setCurrentLocale(firstPart);
    } else {
      setCurrentLocale('en');
    }
  }, [asPath]);

  const switchLanguage = (locale: string) => {
    if (locale === currentLocale) {
      setIsOpen(false);
      return;
    }

    const currentPath = window.location.pathname;
    
    // 1. Remove current locale prefix if it exists
    let cleanPath = currentPath;
    if (currentLocale !== 'en') {
      const regex = new RegExp(`^/${currentLocale}(/|$)`);
      cleanPath = currentPath.replace(regex, '/');
    }

    // 2. Ensure cleanPath doesn't have double slashes and has a single leading slash
    cleanPath = '/' + cleanPath.replace(/\/+/g, '/').replace(/^\//, '');

    // 3. Add new locale prefix if not switching to English
    let newPath = '';
    if (locale === 'en') {
      newPath = cleanPath;
    } else {
      newPath = `/${locale}${cleanPath === '/' ? '/' : cleanPath}`;
    }

    // 4. Final safety: ensure it ends with a slash (Nextra trailingSlash: true)
    if (!newPath.endsWith('/')) {
      newPath += '/';
    }
    
    // Remove double slashes again just in case
    newPath = newPath.replace(/\/+/g, '/');

    window.location.href = newPath;
  };

  const currentLangName = ALL_LANGUAGES.find(l => l.code === currentLocale)?.name || 'English';

  return (
    <div ref={containerRef} style={{ position: 'relative', display: 'inline-block' }}>
      <button
        onClick={() => setIsOpen(!isOpen)}
        style={{
          padding: '0.4rem 0.8rem',
          borderRadius: '6px',
          fontSize: '0.85rem',
          fontWeight: 600,
          cursor: 'pointer',
          background: 'transparent',
          color: 'inherit',
          border: '1px solid rgba(128,128,128,0.2)',
          display: 'inline-flex',
          alignItems: 'center',
          gap: '6px',
          marginLeft: '8px',
          marginRight: '8px'
        }}
      >
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
          <circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
        </svg>
        {currentLangName}
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ marginLeft: '2px', transform: isOpen ? 'rotate(180deg)' : 'none', transition: 'transform 0.2s' }}>
          <path d="M6 9l6 6 6-6"/>
        </svg>
      </button>

      {isOpen && (
        <div style={{
          position: 'absolute',
          top: '100%',
          right: '8px',
          marginTop: '8px',
          background: isDark ? '#1a1a1a' : '#ffffff',
          border: '1px solid rgba(128,128,128,0.25)',
          borderRadius: '6px',
          boxShadow: '0 8px 24px rgba(0,0,0,0.15)',
          zIndex: 1000,
          minWidth: '160px',
          maxHeight: '400px',
          overflowY: 'auto',
          overflowX: 'hidden'
        }}>
          {ALL_LANGUAGES.map(lang => (
            <div
              key={lang.code}
              onMouseDown={(e) => { e.preventDefault(); switchLanguage(lang.code); }}
              style={{
                padding: '8px 12px',
                cursor: 'pointer',
                fontSize: '0.85rem',
                background: currentLocale === lang.code ? 'rgba(128,128,128,0.1)' : 'transparent',
                fontWeight: currentLocale === lang.code ? 600 : 400,
                whiteSpace: 'nowrap'
              }}
              onMouseEnter={(e) => (e.currentTarget.style.background = 'rgba(128,128,128,0.1)')}
              onMouseLeave={(e) => (e.currentTarget.style.background = currentLocale === lang.code ? 'rgba(128,128,128,0.1)' : 'transparent')}
            >
              {lang.name}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

const SEARCH_PLACEHOLDERS: Record<string, string> = {
  en: 'Search documentation...',
  ar: 'البحث في التوثيق...',
  bg: 'Търсене в документацията...',
  cs: 'Prohledat dokumentaci...',
  da: 'Søg i dokumentationen...',
  de: 'Dokumentation durchsuchen...',
  el: 'Αναζήτηση στην τεκμηρίωση...',
  es: 'Buscar en la documentación...',
  fi: 'Hae dokumentaatiosta...',
  fr: 'Rechercher dans la documentation...',
  hi: 'दस्तावेज़ीकरण खोजें...',
  hu: 'Keresés a dokumentációban...',
  id: 'Cari dokumentasi...',
  it: 'Cerca nella documentazione...',
  ja: 'ドキュメントを検索...',
  km: 'ស្វែងរកឯកសារ...',
  ko: '문서 검색...',
  lt: 'Ieškoti dokumentacijoje...',
  lv: 'Meklēt dokumentācijā...',
  nb: 'Søk i dokumentasjonen...',
  nl: 'Documentatie doorzoeken...',
  pl: 'Szukaj w dokumentacji...',
  pt: 'Pesquisar na documentação...',
  'pt-br': 'Pesquisar na documentação...',
  ru: 'Поиск по документации...',
  sk: 'Hľadať v dokumentácii...',
  sq: 'Kërko në dokumentacion...',
  sr: 'Претражи документацију...',
  sv: 'Sök i dokumentationen...',
  te: 'డాక్యుమెంటేషన్ శోధించండి...',
  th: 'ค้นหาเอกสาร...',
  tr: 'Belgelerde ara...',
  uk: 'Пошук у документації...',
  vi: 'Tìm kiếm tài liệu...',
  'zh-hans': '搜索文档...',
  'zh-hant': '搜尋文件...',
};

const EDIT_PAGE_LABELS: Record<string, string> = {
  en: 'Edit this page',
  ar: 'تعديل هذه الصفحة',
  bg: 'Редактирай тази страница',
  cs: 'Upravit tuto stránku',
  da: 'Rediger denne side',
  de: 'Diese Seite bearbeiten',
  el: 'Επεξεργασία αυτής της σελίδας',
  es: 'Editar esta página',
  fi: 'Muokkaa tätä sivua',
  fr: 'Modifier cette page',
  hi: 'इस पृष्ठ को संपादित करें',
  hu: 'Oldal szerkesztése',
  id: 'Edit halaman ini',
  it: 'Modifica questa pagina',
  ja: 'このページを編集',
  km: 'កែសម្រួលទំព័រនេះ',
  ko: '이 페이지 편집',
  lt: 'Redaguoti šį puslapį',
  lv: 'Rediģēt šo lapu',
  nb: 'Rediger denne siden',
  nl: 'Bewerk deze pagina',
  pl: 'Edytuj tę stronę',
  pt: 'Editar esta página',
  'pt-br': 'Editar esta página',
  ru: 'Редактировать страницу',
  sk: 'Upraviť túto stránku',
  sq: 'Redakto këtë faqe',
  sr: 'Измени ову страницу',
  sv: 'Redigera den här sidan',
  te: 'ఈ పేజీని సవరించండి',
  th: 'แก้ไขหน้านี้',
  tr: 'Bu sayfayı düzenle',
  uk: 'Редагувати цю сторінку',
  vi: 'Chỉnh sửa trang này',
  'zh-hans': '编辑此页',
  'zh-hant': '編輯此頁',
};

const FEEDBACK_LABELS: Record<string, string> = {
  en: 'Question? Give us feedback →',
  ar: 'سؤال؟ أعطنا تعليقك →',
  bg: 'Въпрос? Дайте ни обратна връзка →',
  cs: 'Dotaz? Pošlete nám zpětnou vazbu →',
  da: 'Spørgsmål? Giv os feedback →',
  de: 'Frage? Gib uns Feedback →',
  el: 'Ερώτηση; Στείλτε μας σχόλια →',
  es: '¿Pregunta? Envíanos tu opinión →',
  fi: 'Kysymys? Anna meille palautetta →',
  fr: 'Question ? Donnez-nous votre avis →',
  hi: 'प्रश्न? हमें फ़ीडबैक दें →',
  hu: 'Kérdés? Küldj visszajelzést →',
  id: 'Ada pertanyaan? Beri kami masukan →',
  it: 'Domanda? Inviaci un feedback →',
  ja: 'ご質問は？フィードバックを送る →',
  km: 'មានសំណួរ? ផ្ញើមតិកែលម្អ →',
  ko: '질문이 있으신가요? 피드백 보내기 →',
  lt: 'Klausimas? Pateikite atsiliepimą →',
  lv: 'Jautājums? Sniedziet atsauksmi →',
  nb: 'Spørsmål? Gi oss tilbakemelding →',
  nl: 'Vraag? Geef ons feedback →',
  pl: 'Pytanie? Prześlij nam opinię →',
  pt: 'Dúvida? Envie-nos feedback →',
  'pt-br': 'Dúvida? Envie-nos feedback →',
  ru: 'Вопрос? Отправьте отзыв →',
  sk: 'Otázka? Pošlite nám spätnú väzbu →',
  sq: 'Pyetje? Na jepni komente →',
  sr: 'Питање? Пошаљите нам повратне информације →',
  sv: 'Fråga? Ge oss feedback →',
  te: 'ప్రశ్న ఉందా? మాకు అభిప్రాయం పంపండి →',
  th: 'มีคำถาม? ส่งความคิดเห็นถึงเรา →',
  tr: 'Sorunuz mu var? Bize geri bildirim gönderin →',
  uk: 'Питання? Надішліть нам відгук →',
  vi: 'Câu hỏi? Gửi phản hồi cho chúng tôi →',
  'zh-hans': '有疑问？给我们反馈 →',
  'zh-hant': '有疑問？給我們回饋 →',
};

const useLocale = () => {
  const { asPath } = useRouter();
  const first = asPath.split('/')[1];
  return (first && EDIT_PAGE_LABELS[first]) ? first : 'en';
};

const EditLinkText: React.FC = () => {
  const locale = useLocale();
  return <>{EDIT_PAGE_LABELS[locale]}</>;
};

const FeedbackContent: React.FC = () => {
  const locale = useLocale();
  return <>{FEEDBACK_LABELS[locale]}</>;
};

const LAST_UPDATED_LABELS: Record<string, string> = {
  en: 'Last updated on',
  ar: 'آخر تحديث في',
  bg: 'Последна актуализация на',
  cs: 'Poslední aktualizace',
  da: 'Sidst opdateret',
  de: 'Zuletzt aktualisiert am',
  el: 'Τελευταία ενημέρωση',
  es: 'Última actualización el',
  fi: 'Viimeksi päivitetty',
  fr: 'Dernière mise à jour le',
  hi: 'अंतिम अपडेट',
  hu: 'Utolsó frissítés',
  id: 'Terakhir diperbarui pada',
  it: 'Ultimo aggiornamento il',
  ja: '最終更新日',
  km: 'បានធ្វើបច្ចុប្បន្នភាពចុងក្រោយ',
  ko: '마지막 업데이트',
  lt: 'Paskutinį kartą atnaujinta',
  lv: 'Pēdējo reizi atjaunināts',
  nb: 'Sist oppdatert',
  nl: 'Laatst bijgewerkt op',
  pl: 'Ostatnia aktualizacja',
  pt: 'Última atualização em',
  'pt-br': 'Última atualização em',
  ru: 'Последнее обновление',
  sk: 'Posledná aktualizácia',
  sq: 'Përditësimi i fundit',
  sr: 'Последња измена',
  sv: 'Senast uppdaterad',
  te: 'చివరిగా నవీకరించబడింది',
  th: 'อัปเดตล่าสุดเมื่อ',
  tr: 'Son güncelleme',
  uk: 'Останнє оновлення',
  vi: 'Cập nhật lần cuối vào',
  'zh-hans': '最后更新于',
  'zh-hant': '最後更新於',
};

// Map app locale codes to BCP 47 tags for Intl.DateTimeFormat
const INTL_LOCALE_MAP: Record<string, string> = {
  'zh-hans': 'zh-Hans',
  'zh-hant': 'zh-Hant',
  'pt-br': 'pt-BR',
  'nb': 'nb-NO',
};

const GitTimestamp: React.FC<{ timestamp: Date }> = ({ timestamp }) => {
  const { asPath } = useRouter();
  const pathParts = asPath.split('/');
  const firstPart = pathParts[1];
  const locale = (firstPart && LAST_UPDATED_LABELS[firstPart]) ? firstPart : 'en';
  const intlLocale = INTL_LOCALE_MAP[locale] || locale;
  const label = LAST_UPDATED_LABELS[locale] || LAST_UPDATED_LABELS['en'];
  const formatted = new Intl.DateTimeFormat(intlLocale, { year: 'numeric', month: 'long', day: 'numeric' }).format(timestamp);
  return <>{label} {formatted}</>;
};

const config: DocsThemeConfig = {
  project: {
    link: 'https://github.com/therealtimex/rtsurvey',
  },
  chat: {
    link: 'https://twitter.com/RtSurvey',
    icon: (
      <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
        <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
      </svg>
    ),
  },
  navbar: {
    extraContent: <LanguageSwitcher />
  },
  search: {
    placeholder: () => {
      // SSR / static generation: read locale from NEXT_BASE_PATH (e.g. "/vi")
      if (typeof window === 'undefined') {
        const base = process.env.NEXT_BASE_PATH || '';
        const locale = base.replace(/^\//, '');
        return SEARCH_PLACEHOLDERS[locale] || SEARCH_PLACEHOLDERS['en'];
      }
      // Client-side: read locale from URL path
      const parts = window.location.pathname.split('/');
      const locale = parts[1] && SEARCH_PLACEHOLDERS[parts[1]] ? parts[1] : 'en';
      return SEARCH_PLACEHOLDERS[locale];
    },
  },
  editLink: { text: EditLinkText },
  feedback: { content: FeedbackContent },
  gitTimestamp: GitTimestamp,
  docsRepositoryBase: 'https://github.com/therealtimex/rtsurvey/tree/main/docs',
  footer: {
    text: (
      <span>
        MIT {new Date().getFullYear()} ©{' '}
        <a href="https://rtsurvey.com" target="_blank">
          rtSurvey
        </a>
        .
      </span>
    ),
  },
  head: (
    <>
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <meta property="og:title" content="rtSurvey Docs" />
      <meta property="og:description" content="Official documentation for rtSurvey platform." />
      <link rel="icon" href="/favicon.ico" type="image/x-icon" />
    </>
  ),
  logo: (
    <span style={{ fontWeight: 700, fontSize: '1.1rem' }}>
      rtSurvey Docs
    </span>
  ),
}

export default config;
