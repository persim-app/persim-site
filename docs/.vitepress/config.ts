import { defineConfig } from 'vitepress'
import { APP_STORE_URL, SITE_URL, OG_IMAGE, SUPPORT_EMAIL, DEFAULT_ACCENT } from './theme/site'

// ── Per-locale UI strings (nav / sidebar / footer) ────────────────
type Strings = {
  home: string; features: string; guide: string; download: string; faq: string
  startGroup: string; intro: string; install: string
  useGroup: string; usage: string
  aboutGroup: string; privacy: string; troubleshooting: string
  legalGroup: string; legal: string; privacyPolicy: string; privacyChoices: string; terms: string
  footerMessage: string; footerCopyright: string
  product: string; support: string; aboutUs: string; contact: string
  langMenuLabel: string; searchText: string; outline: string
  accentLabel: string; accentNames: string[]
}

const STR: Record<string, Strings> = {
  en: {
    home: 'Home', features: 'Features', guide: 'Guide', download: 'Download', faq: 'FAQ',
    startGroup: 'Getting started', intro: 'What is Persim', install: 'Install',
    useGroup: 'Everyday use', usage: 'Feature tour',
    aboutGroup: 'About', privacy: 'Privacy',
    troubleshooting: 'Troubleshooting', legalGroup: 'Legal', legal: 'Legal information', privacyPolicy: 'Privacy Policy', privacyChoices: 'Privacy Choices', terms: 'Terms of Service',
    footerMessage: 'A clean, fast browser for Mac — built to stay out of your way.',
    footerCopyright: '© 2026 w3cub.com. All rights reserved.',
    product: 'Product', support: 'Support', aboutUs: 'About', contact: 'Contact',
    langMenuLabel: 'Language', searchText: 'Search docs', outline: 'On this page',
    accentLabel: 'Accent colour',
    accentNames: ['Persimmon', 'Violet', 'Teal', 'Green', 'Blue', 'Rose'],
  },
  'zh-CN': {
    home: '首页', features: '功能', guide: '使用指南', download: '下载', faq: '常见问题',
    startGroup: '开始使用', intro: '认识 Persim', install: '安装',
    useGroup: '日常使用', usage: '功能一览',
    aboutGroup: '关于', privacy: '隐私与数据',
    troubleshooting: '问题排查', legalGroup: '法律', legal: '法律信息', privacyPolicy: '隐私政策', privacyChoices: '隐私选择', terms: '服务条款',
    footerMessage: '一款清爽、快速的 Mac 浏览器——安静地做好本分。',
    footerCopyright: '© 2026 w3cub.com。保留所有权利。',
    product: '产品', support: '支持', aboutUs: '关于', contact: '联系我们',
    langMenuLabel: '语言', searchText: '搜索文档', outline: '本页目录',
    accentLabel: '主题色',
    accentNames: ['柿子色', '紫色', '青色', '绿色', '蓝色', '玫红'],
  },
  'zh-TW': {
    home: '首頁', features: '功能', guide: '使用指南', download: '下載', faq: '常見問題',
    startGroup: '開始使用', intro: '認識 Persim', install: '安裝',
    useGroup: '日常使用', usage: '功能一覽',
    aboutGroup: '關於', privacy: '隱私與資料',
    troubleshooting: '問題排查', legalGroup: '法律', legal: '法律資訊', privacyPolicy: '隱私權政策', privacyChoices: '隱私選擇', terms: '服務條款',
    footerMessage: '一款清爽、快速的 Mac 瀏覽器——安靜地做好本分。',
    footerCopyright: '© 2026 w3cub.com。保留所有權利。',
    product: '產品', support: '支援', aboutUs: '關於', contact: '聯絡我們',
    langMenuLabel: '語言', searchText: '搜尋文件', outline: '本頁目錄',
    accentLabel: '主題色',
    accentNames: ['柿子色', '紫色', '青色', '綠色', '藍色', '玫紅'],
  },
  ja: {
    home: 'ホーム', features: '機能', guide: 'ガイド', download: 'ダウンロード', faq: 'よくある質問',
    startGroup: 'はじめに', intro: 'Persim とは', install: 'インストール',
    useGroup: '毎日の使い方', usage: '機能一覧',
    aboutGroup: '情報', privacy: 'プライバシー',
    troubleshooting: 'トラブルシューティング', legalGroup: '法務', legal: '法務情報', privacyPolicy: 'プライバシーポリシー', privacyChoices: 'プライバシー設定', terms: '利用規約',
    footerMessage: '邪魔をしない、すっきり速い Mac 用ブラウザー。',
    footerCopyright: '© 2026 w3cub.com. All rights reserved.',
    product: '製品', support: 'サポート', aboutUs: '概要', contact: 'お問い合わせ',
    langMenuLabel: '言語', searchText: 'ドキュメントを検索', outline: 'このページの内容',
    accentLabel: 'アクセントカラー',
    accentNames: ['柿色', 'バイオレット', 'ティール', 'グリーン', 'ブルー', 'ローズ'],
  },
  de: {
    home: 'Start', features: 'Funktionen', guide: 'Anleitung', download: 'Download', faq: 'FAQ',
    startGroup: 'Erste Schritte', intro: 'Persim kennenlernen', install: 'Installieren',
    useGroup: 'Im Alltag', usage: 'Funktionen im Überblick',
    aboutGroup: 'Info', privacy: 'Datenschutz',
    troubleshooting: 'Fehlerbehebung', legalGroup: 'Rechtliches', legal: 'Rechtliches', privacyPolicy: 'Datenschutzerklärung', privacyChoices: 'Datenschutz-Optionen', terms: 'Nutzungsbedingungen',
    footerMessage: 'Ein aufgeräumter, schneller Browser für Mac — ganz ohne Ablenkung.',
    footerCopyright: '© 2026 w3cub.com. Alle Rechte vorbehalten.',
    product: 'Produkt', support: 'Support', aboutUs: 'Über uns', contact: 'Kontakt',
    langMenuLabel: 'Sprache', searchText: 'Dokumentation durchsuchen', outline: 'Auf dieser Seite',
    accentLabel: 'Akzentfarbe',
    accentNames: ['Persimmon', 'Violett', 'Türkis', 'Grün', 'Blau', 'Rosé'],
  },
  es: {
    home: 'Inicio', features: 'Funciones', guide: 'Guía', download: 'Descargar', faq: 'Preguntas frecuentes',
    startGroup: 'Primeros pasos', intro: 'Qué es Persim', install: 'Instalación',
    useGroup: 'Día a día', usage: 'Recorrido por las funciones',
    aboutGroup: 'Información', privacy: 'Privacidad',
    troubleshooting: 'Solución de problemas', legalGroup: 'Legal', legal: 'Información legal', privacyPolicy: 'Política de privacidad', privacyChoices: 'Opciones de privacidad', terms: 'Términos del servicio',
    footerMessage: 'Un navegador limpio y rápido para Mac, pensado para no estorbar.',
    footerCopyright: '© 2026 w3cub.com. Todos los derechos reservados.',
    product: 'Producto', support: 'Soporte', aboutUs: 'Acerca de', contact: 'Contacto',
    langMenuLabel: 'Idioma', searchText: 'Buscar documentación', outline: 'En esta página',
    accentLabel: 'Color de acento',
    accentNames: ['Persimón', 'Violeta', 'Turquesa', 'Verde', 'Azul', 'Rosa'],
  },
  fr: {
    home: 'Accueil', features: 'Fonctionnalités', guide: 'Guide', download: 'Télécharger', faq: 'FAQ',
    startGroup: 'Premiers pas', intro: 'Découvrir Persim', install: 'Installation',
    useGroup: 'Au quotidien', usage: 'Tour des fonctionnalités',
    aboutGroup: 'À propos', privacy: 'Confidentialité',
    troubleshooting: 'Dépannage', legalGroup: 'Mentions légales', legal: 'Mentions légales', privacyPolicy: 'Politique de confidentialité', privacyChoices: 'Choix de confidentialité', terms: "Conditions d'utilisation",
    footerMessage: 'Un navigateur clair et rapide pour Mac, conçu pour rester discret.',
    footerCopyright: '© 2026 w3cub.com. Tous droits réservés.',
    product: 'Produit', support: 'Assistance', aboutUs: 'À propos', contact: 'Contact',
    langMenuLabel: 'Langue', searchText: 'Rechercher dans la documentation', outline: 'Sur cette page',
    accentLabel: 'Couleur d’accent',
    accentNames: ['Persimmon', 'Violet', 'Sarcelle', 'Vert', 'Bleu', 'Rose'],
  },
}

// Build a locale's themeConfig. Internal links get the locale prefix so the
// default VitePress nav / sidebar / footer resolve to the localized page.
function tc(S: Strings, lang: string) {
  const base = !lang || lang === 'en' ? '' : `/${lang}`
  const L = (p: string) => `${base}${p}`
  return {
    langMenuLabel: S.langMenuLabel,
    accentLabel: S.accentLabel,
    accentNames: S.accentNames,
    outline: { level: [2, 3], title: S.outline },
    nav: [
      { text: S.home, link: L('/') },
      { text: S.features, link: L('/#features') },
      { text: S.guide, link: L('/guide/introduction') },
      { text: S.download, link: L('/guide/installation') },
      { text: S.faq, link: L('/guide/faq') },
    ],
    sidebar: [
      {
        text: S.startGroup,
        items: [
          { text: S.intro, link: L('/guide/introduction') },
          { text: S.install, link: L('/guide/installation') },
        ],
      },
      {
        text: S.useGroup,
        items: [
          { text: S.usage, link: L('/guide/features') },
          { text: S.faq, link: L('/guide/faq') },
          { text: S.troubleshooting, link: L('/guide/troubleshooting') },
        ],
      },
      {
        text: S.aboutGroup,
        items: [
          { text: S.privacy, link: L('/guide/privacy') },
          { text: S.legal, link: L('/guide/legal') },
        ],
      },
      {
        text: S.legalGroup,
        items: [
          { text: S.privacyPolicy, link: L('/guide/privacy-policy') },
          { text: S.privacyChoices, link: L('/guide/privacy-choices') },
          { text: S.terms, link: L('/guide/terms') },
        ],
      },
    ],
    footer: {
      message: S.footerMessage,
      copyright: S.footerCopyright,
      items: [
        {
          text: S.product,
          items: [
            { text: S.features, link: L('/#features') },
            { text: S.usage, link: L('/guide/features') },
            { text: S.download, link: APP_STORE_URL },
          ],
        },
        {
          text: S.support,
          items: [
            { text: S.guide, link: L('/guide/introduction') },
            { text: S.faq, link: L('/guide/faq') },
            { text: S.troubleshooting, link: L('/guide/troubleshooting') },
            { text: S.contact, link: `mailto:${SUPPORT_EMAIL}` },
          ],
        },
        {
          text: S.legalGroup,
          items: [
            { text: S.privacyPolicy, link: L('/guide/privacy-policy') },
            { text: S.privacyChoices, link: L('/guide/privacy-choices') },
            { text: S.terms, link: L('/guide/terms') },
          ],
        },
        {
          text: S.aboutUs,
          items: [
            { text: S.intro, link: L('/guide/introduction') },
            { text: S.privacy, link: L('/guide/privacy') },
            { text: 'Mac App Store', link: APP_STORE_URL },
          ],
        },
      ],
    },
    search: { provider: 'local', options: { translations: { button: { buttonText: S.searchText } } } },
  }
}

const MD = {
  'zh-CN': { container: { tipLabel: '提示', warningLabel: '注意', dangerLabel: '危险', infoLabel: '信息', detailsLabel: '详情' }, codeCopyButton: { tooltipText: '复制代码', copiedText: '已复制' } },
  'zh-TW': { container: { tipLabel: '提示', warningLabel: '注意', dangerLabel: '危險', infoLabel: '資訊', detailsLabel: '詳情' }, codeCopyButton: { tooltipText: '複製程式碼', copiedText: '已複製' } },
  ja: { container: { tipLabel: 'ヒント', warningLabel: '注意', dangerLabel: '危険', infoLabel: '情報', detailsLabel: '詳細' }, codeCopyButton: { tooltipText: 'コードをコピー', copiedText: 'コピーしました' } },
  de: { container: { tipLabel: 'Tipp', warningLabel: 'Achtung', dangerLabel: 'Gefahr', infoLabel: 'Info', detailsLabel: 'Details' }, codeCopyButton: { tooltipText: 'Code kopieren', copiedText: 'Kopiert' } },
  es: { container: { tipLabel: 'Consejo', warningLabel: 'Atención', dangerLabel: 'Peligro', infoLabel: 'Info', detailsLabel: 'Detalles' }, codeCopyButton: { tooltipText: 'Copiar código', copiedText: 'Copiado' } },
  fr: { container: { tipLabel: 'Astuce', warningLabel: 'Attention', dangerLabel: 'Danger', infoLabel: 'Info', detailsLabel: 'Détails' }, codeCopyButton: { tooltipText: 'Copier le code', copiedText: 'Copié' } },
}

const descriptions: Record<string, string> = {
  en: 'Persim is a clean, fast browser for Mac. Tabs, ad blocking, video saving, reading mode, AI shortcuts — all in one quiet place.',
  'zh-CN': 'Persim 柿子浏览器，一款清爽快速的 Mac 浏览器。多标签、广告拦截、视频保存、阅读模式与 AI 直达，安静地陪你上网。',
  'zh-TW': 'Persim 柿子瀏覽器，一款清爽快速的 Mac 瀏覽器。多分頁、廣告攔截、影片儲存、閱讀模式與 AI 直達，安靜地陪你上網。',
  ja: 'Persim は Mac 向けのすっきり速いブラウザーです。タブ、広告ブロック、動画保存、リーディングモード、AI ショートカットを一か所に。',
  de: 'Persim ist ein aufgeräumter, schneller Browser für Mac. Tabs, Werbeblocker, Video-Downloads, Lesemodus und AI-Kürzel — still und übersichtlich.',
  es: 'Persim es un navegador limpio y rápido para Mac. Pestañas, bloqueo de anuncios, guardado de vídeos, modo lectura y accesos a IA en un solo lugar.',
  fr: 'Persim est un navigateur clair et rapide pour Mac. Onglets, blocage des publicités, enregistrement de vidéos, mode lecture et accès IA réunis au même endroit.',
}

const titles: Record<string, string> = {
  en: 'Persim — a clean, fast browser for Mac',
  'zh-CN': 'Persim 柿子浏览器 — 清爽、快速的 Mac 浏览器',
  'zh-TW': 'Persim 柿子瀏覽器 — 清爽、快速的 Mac 瀏覽器',
  ja: 'Persim — すっきり速い Mac 用ブラウザー',
  de: 'Persim — ein aufgeräumter, schneller Browser für Mac',
  es: 'Persim — un navegador limpio y rápido para Mac',
  fr: 'Persim — un navigateur clair et rapide pour Mac',
}

export default defineConfig({
  base: '/',
  title: 'Persim',
  titleTemplate: 'Persim — :title',
  description: descriptions.en,
  lastUpdated: true,
  head: [
    ['link', { rel: 'icon', type: 'image/png', href: '/logo.png' }],
    ['link', { rel: 'apple-touch-icon', href: '/logo.png' }],
    ['meta', { name: 'theme-color', content: DEFAULT_ACCENT }],
    ['meta', { name: 'viewport', content: 'width=device-width, initial-scale=1.0' }],
    ['meta', { name: 'keywords', content: 'Persim, browser, Mac browser, 柿子浏览器, ad blocker, video download, reading mode' }],
    ['meta', { name: 'author', content: 'w3cub.com' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:site_name', content: 'Persim' }],
    ['meta', { property: 'og:url', content: `${SITE_URL}/` }],
    ['meta', { property: 'og:title', content: titles.en }],
    ['meta', { property: 'og:description', content: descriptions.en }],
    ['meta', { property: 'og:image', content: OG_IMAGE }],
    ['meta', { property: 'og:image:width', content: '1200' }],
    ['meta', { property: 'og:image:height', content: '630' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { name: 'twitter:title', content: titles.en }],
    ['meta', { name: 'twitter:description', content: descriptions.en }],
    ['meta', { name: 'twitter:image', content: OG_IMAGE }],
  ],
  themeConfig: {
    siteTitle: 'Persim',
    logo: '/logo.png',
    outline: [2, 3],
  },
  locales: {
    root: { label: 'English', lang: 'en', description: descriptions.en, title: titles.en, themeConfig: tc(STR.en, 'en') },
    'zh-CN': { label: '简体中文', lang: 'zh-CN', link: '/zh-CN/', description: descriptions['zh-CN'], title: titles['zh-CN'], themeConfig: tc(STR['zh-CN'], 'zh-CN'), markdown: MD['zh-CN'] },
    'zh-TW': { label: '繁體中文', lang: 'zh-TW', link: '/zh-TW/', description: descriptions['zh-TW'], title: titles['zh-TW'], themeConfig: tc(STR['zh-TW'], 'zh-TW'), markdown: MD['zh-TW'] },
    ja: { label: '日本語', lang: 'ja', link: '/ja/', description: descriptions.ja, title: titles.ja, themeConfig: tc(STR.ja, 'ja'), markdown: MD.ja },
    de: { label: 'Deutsch', lang: 'de', link: '/de/', description: descriptions.de, title: titles.de, themeConfig: tc(STR.de, 'de'), markdown: MD.de },
    es: { label: 'Español', lang: 'es', link: '/es/', description: descriptions.es, title: titles.es, themeConfig: tc(STR.es, 'es'), markdown: MD.es },
    fr: { label: 'Français', lang: 'fr', link: '/fr/', description: descriptions.fr, title: titles.fr, themeConfig: tc(STR.fr, 'fr'), markdown: MD.fr },
  },
})
