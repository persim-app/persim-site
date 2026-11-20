import { defineConfig } from 'vitepress'

// ── Per-locale UI strings (nav / sidebar / footer) ────────────────
const STR = {
  en: {
    home: 'Home', guide: 'Guide', pets: 'Pets', faq: 'FAQ',
    github: 'GitHub', productHunt: 'Product Hunt',
    guideGroup: 'Guide',
    intro: 'Introduction', install: 'Installation', usage: 'Usage',
    petsPage: 'Pets & IAP', permissions: 'Permissions', customize: 'Customize',
    troubleshooting: 'Troubleshooting',
    legalGroup: 'Legal',
    privacy: 'Privacy Policy', privacyChoices: 'Privacy Choices', terms: 'Terms of Service',
    footerMessage: 'A calm, local-first reminder app for macOS — with a companion that grows with your streak.',
    footerCopyright: 'Copyright © 2026 Terry. All rights reserved.',
    product: 'Product', about: 'About', features: 'Features',
    support: 'Support', documentation: 'Documentation', contact: 'Contact',
    company: 'Company', langMenuLabel: 'Language',
  },
  'zh-CN': {
    home: '首页', guide: '指南', pets: '宠物', faq: '常见问题',
    github: 'GitHub', productHunt: 'Product Hunt',
    guideGroup: '指南',
    intro: '简介', install: '安装', usage: '使用',
    petsPage: '宠物与内购', permissions: '权限', customize: '个性化',
    troubleshooting: '故障排除',
    legalGroup: '法律',
    privacy: '隐私政策', privacyChoices: '隐私选项', terms: '服务条款',
    footerMessage: '一款安静、本地优先的 macOS 提醒应用 —— 还有一只陪你一起成长的伙伴。',
    footerCopyright: '© 2026 Terry。保留所有权利。',
    product: '产品', about: '关于', features: '功能',
    support: '支持', documentation: '文档', contact: '联系我们',
    company: '公司', langMenuLabel: '语言',
  },
  'zh-TW': {
    home: '首頁', guide: '指南', pets: '寵物', faq: '常見問題',
    github: 'GitHub', productHunt: 'Product Hunt',
    guideGroup: '指南',
    intro: '簡介', install: '安裝', usage: '使用',
    petsPage: '寵物與內購', permissions: '權限', customize: '個人化',
    troubleshooting: '故障排除',
    legalGroup: '法律',
    privacy: '隱私政策', privacyChoices: '隱私選項', terms: '服務條款',
    footerMessage: '一款安靜、本機優先的 macOS 提醒 App —— 還有一隻陪你一起成長的夥伴。',
    footerCopyright: '© 2026 Terry。保留所有權利。',
    product: '產品', about: '關於', features: '功能',
    support: '支援', documentation: '文件', contact: '聯絡我們',
    company: '公司', langMenuLabel: '語言',
  },
  ja: {
    home: 'ホーム', guide: 'ガイド', pets: 'ペット', faq: 'よくある質問',
    github: 'GitHub', productHunt: 'Product Hunt',
    guideGroup: 'ガイド',
    intro: 'はじめに', install: 'インストール', usage: '使い方',
    petsPage: 'ペットとアプリ内課金', permissions: '権限', customize: 'カスタマイズ',
    troubleshooting: 'トラブルシューティング',
    legalGroup: '法務',
    privacy: 'プライバシーポリシー', privacyChoices: 'プライバシーの選択', terms: '利用規約',
    footerMessage: '静かでローカルファーストな macOS リマインダー —— 継続とともに育つ相棒と一緒に。',
    footerCopyright: '© 2026 Terry. All rights reserved.',
    product: '製品', about: '概要', features: '機能',
    support: 'サポート', documentation: 'ドキュメント', contact: 'お問い合わせ',
    company: '会社', langMenuLabel: '言語',
  },
  de: {
    home: 'Start', guide: 'Anleitung', pets: 'Haustiere', faq: 'FAQ',
    github: 'GitHub', productHunt: 'Product Hunt',
    guideGroup: 'Anleitung',
    intro: 'Einführung', install: 'Installation', usage: 'Nutzung',
    petsPage: 'Haustiere & In-App-Käufe', permissions: 'Berechtigungen', customize: 'Anpassen',
    troubleshooting: 'Fehlerbehebung',
    legalGroup: 'Rechtliches',
    privacy: 'Datenschutz', privacyChoices: 'Datenschutz-Einstellungen', terms: 'Nutzungsbedingungen',
    footerMessage: 'Eine ruhige, lokal gespeicherte Erinnerungs-App für macOS — mit einem Begleiter, der mit deiner Serie wächst.',
    footerCopyright: '© 2026 Terry. Alle Rechte vorbehalten.',
    product: 'Produkt', about: 'Über', features: 'Funktionen',
    support: 'Support', documentation: 'Dokumentation', contact: 'Kontakt',
    company: 'Unternehmen', langMenuLabel: 'Sprache',
  },
  es: {
    home: 'Inicio', guide: 'Guía', pets: 'Mascotas', faq: 'Preguntas frecuentes',
    github: 'GitHub', productHunt: 'Product Hunt',
    guideGroup: 'Guía',
    intro: 'Introducción', install: 'Instalación', usage: 'Uso',
    petsPage: 'Mascotas y compras', permissions: 'Permisos', customize: 'Personalizar',
    troubleshooting: 'Solución de problemas',
    legalGroup: 'Legal',
    privacy: 'Política de privacidad', privacyChoices: 'Opciones de privacidad', terms: 'Términos del servicio',
    footerMessage: 'Una app de recordatorios tranquila y local para macOS — con un compañero que crece con tu racha.',
    footerCopyright: '© 2026 Terry. Todos los derechos reservados.',
    product: 'Producto', about: 'Acerca de', features: 'Funciones',
    support: 'Soporte', documentation: 'Documentación', contact: 'Contacto',
    company: 'Empresa', langMenuLabel: 'Idioma',
  },
  fr: {
    home: 'Accueil', guide: 'Guide', pets: 'Animaux', faq: 'FAQ',
    github: 'GitHub', productHunt: 'Product Hunt',
    guideGroup: 'Guide',
    intro: 'Introduction', install: 'Installation', usage: 'Utilisation',
    petsPage: 'Animaux & achats intégrés', permissions: 'Autorisations', customize: 'Personnaliser',
    troubleshooting: 'Dépannage',
    legalGroup: 'Mentions légales',
    privacy: 'Politique de confidentialité', privacyChoices: 'Choix de confidentialité', terms: 'Conditions d’utilisation',
    footerMessage: 'Une app de rappels calme et locale pour macOS — avec un compagnon qui grandit avec votre série.',
    footerCopyright: '© 2026 Terry. Tous droits réservés.',
    product: 'Produit', about: 'À propos', features: 'Fonctionnalités',
    support: 'Assistance', documentation: 'Documentation', contact: 'Contact',
    company: 'Société', langMenuLabel: 'Langue',
  },
}

// ── Build a themeConfig for a given locale ────────────────────────
// Internal links are prefixed with the locale segment so the default
// VitePress nav / sidebar / footer resolve to the localized page.
function tc(S: typeof STR.en, lang: string) {
  const base = !lang || lang === 'en' ? '' : `/${lang}`
  const L = (p: string) =>
    /^https?:\/\//.test(p) || p.startsWith('mailto:') || p.startsWith(base)
      ? p
      : `${base}${p}`
  return {
    langMenuLabel: S.langMenuLabel,
    nav: [
      { text: S.home, link: L('/') },
      { text: S.guide, link: L('/guide/introduction') },
      { text: S.pets, link: L('/guide/pets') },
      { text: S.faq, link: L('/guide/faq') },
      { text: S.github, link: 'https://github.com/petreminder/reminder' },
      { text: S.productHunt, link: 'https://www.producthunt.com/products/pet-reminder?utm_source=badge-featured&utm_medium=badge&utm_campaign=badge-pet-reminder' },
    ],
    sidebar: [
      {
        text: S.guideGroup,
        items: [
          { text: S.intro, link: L('/guide/introduction') },
          { text: S.install, link: L('/guide/installation') },
          { text: S.usage, link: L('/guide/usage') },
          { text: S.petsPage, link: L('/guide/pets') },
          { text: S.permissions, link: L('/guide/permissions') },
          { text: S.customize, link: L('/guide/customize') },
          { text: S.troubleshooting, link: L('/guide/troubleshooting') },
          { text: S.faq, link: L('/guide/faq') },
        ],
      },
      {
        text: S.legalGroup,
        items: [
          { text: S.privacy, link: L('/guide/privacy') },
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
            { text: S.about, link: L('/guide/introduction') },
            { text: S.features, link: L('/#features') },
            { text: S.pets, link: L('/guide/pets') },
            { text: S.install, link: L('/guide/installation') },
          ],
        },
        {
          text: S.support,
          items: [
            { text: S.documentation, link: L('/guide/introduction') },
            { text: S.faq, link: L('/guide/faq') },
            { text: S.troubleshooting, link: L('/guide/troubleshooting') },
            { text: S.contact, link: 'mailto:reminder@w3cub.com' },
          ],
        },
        {
          text: S.company,
          items: [
            { text: S.about, link: L('/guide/introduction') },
            { text: S.privacy, link: L('/guide/privacy') },
            { text: S.terms, link: L('/guide/terms') },
            { text: S.github, link: 'https://github.com/petreminder/reminder' },
          ],
        },
      ],
    },
  }
}

// ── Per-locale markdown renderer strings ─────────────────────────
const MD = {
  'zh-CN': {
    container: { tipLabel: '提示', warningLabel: '警告', dangerLabel: '危险', infoLabel: '信息', detailsLabel: '详情' },
    codeCopyButton: { tooltipText: '复制代码', copiedText: '已复制' },
  },
  'zh-TW': {
    container: { tipLabel: '提示', warningLabel: '警告', dangerLabel: '危險', infoLabel: '資訊', detailsLabel: '詳情' },
    codeCopyButton: { tooltipText: '複製程式碼', copiedText: '已複製' },
  },
  ja: {
    container: { tipLabel: 'ヒント', warningLabel: '警告', dangerLabel: '危険', infoLabel: '情報', detailsLabel: '詳細' },
    codeCopyButton: { tooltipText: 'コードをコピー', copiedText: 'コピーしました' },
  },
  de: {
    container: { tipLabel: 'Tipp', warningLabel: 'Warnung', dangerLabel: 'Gefahr', infoLabel: 'Info', detailsLabel: 'Details' },
    codeCopyButton: { tooltipText: 'Code kopieren', copiedText: 'Kopiert' },
  },
  es: {
    container: { tipLabel: 'Consejo', warningLabel: 'Advertencia', dangerLabel: 'Peligro', infoLabel: 'Info', detailsLabel: 'Detalles' },
    codeCopyButton: { tooltipText: 'Copiar código', copiedText: 'Copiado' },
  },
  fr: {
    container: { tipLabel: 'Astuce', warningLabel: 'Avertissement', dangerLabel: 'Danger', infoLabel: 'Info', detailsLabel: 'Détails' },
    codeCopyButton: { tooltipText: 'Copier le code', copiedText: 'Copié' },
  },
}

export default defineConfig({
  base: '/',
  title: 'Reminder',
  titleTemplate: 'Reminder — :title',
  description: 'Reminder — a calm, local-first reminder app for macOS with a desktop pet that grows with your streak. No account, no ads, no cloud.',
  lastUpdated: true,
  head: [
    ['link', { rel: 'icon', type: 'image/png', href: '/logo.png' }],
    ['link', { rel: 'apple-touch-icon', href: '/logo.png' }],
    ['meta', { name: 'theme-color', content: '#f97316' }],
    ['meta', { name: 'viewport', content: 'width=device-width, initial-scale=1.0' }],
    ['meta', { name: 'keywords', content: 'reminder, to-do, pet companion, desktop pet, macos, productivity, streak, achievements, local-first' }],
    ['meta', { name: 'author', content: 'Terry' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:site_name', content: 'Reminder' }],
    ['meta', { property: 'og:url', content: 'https://reminder.w3cub.com/' }],
    ['meta', { property: 'og:title', content: 'Reminder — Reminders that grow with you' }],
    ['meta', { property: 'og:description', content: 'A calm, local-first reminder app for macOS — and a small companion that grows as you keep your days together.' }],
    ['meta', { property: 'og:image', content: 'https://reminder.w3cub.com/preview.jpg' }],
    ['meta', { property: 'og:image:width', content: '1200' }],
    ['meta', { property: 'og:image:height', content: '750' }],
    ['meta', { property: 'og:image:alt', content: 'Reminder — reminders and a desktop pet companion on macOS' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { name: 'twitter:url', content: 'https://reminder.w3cub.com/' }],
    ['meta', { name: 'twitter:title', content: 'Reminder — Reminders that grow with you' }],
    ['meta', { name: 'twitter:description', content: 'A calm, local-first reminder app for macOS — and a small companion that grows as you keep your days together.' }],
    ['meta', { name: 'twitter:image', content: 'https://reminder.w3cub.com/preview.jpg' }],
    ['meta', { name: 'twitter:image:alt', content: 'Reminder — reminders and a desktop pet companion on macOS' }],
  ],
  themeConfig: {
    siteTitle: 'Reminder',
    logo: '/logo.png',
    search: { provider: 'local' },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/petreminder/reminder' },
    ],
  },
  locales: {
    root: {
      label: 'English',
      lang: 'en',
      themeConfig: tc(STR.en, 'en'),
    },
    'zh-CN': {
      label: '简体中文', lang: 'zh-CN', link: '/zh-CN/',
      themeConfig: tc(STR['zh-CN'], 'zh-CN'), markdown: MD['zh-CN'],
    },
    'zh-TW': {
      label: '繁體中文', lang: 'zh-TW', link: '/zh-TW/',
      themeConfig: tc(STR['zh-TW'], 'zh-TW'), markdown: MD['zh-TW'],
    },
    ja: {
      label: '日本語', lang: 'ja', link: '/ja/',
      themeConfig: tc(STR.ja, 'ja'), markdown: MD.ja,
    },
    de: {
      label: 'Deutsch', lang: 'de', link: '/de/',
      themeConfig: tc(STR.de, 'de'), markdown: MD.de,
    },
    es: {
      label: 'Español', lang: 'es', link: '/es/',
      themeConfig: tc(STR.es, 'es'), markdown: MD.es,
    },
    fr: {
      label: 'Français', lang: 'fr', link: '/fr/',
      themeConfig: tc(STR.fr, 'fr'), markdown: MD.fr,
    },
  },
})
