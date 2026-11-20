/**
 * Single source of truth for product links, identifiers and brand colours.
 *
 * Change the App Store URL or the support address here first — config.ts and
 * the Vue components import these constants instead of duplicating literals.
 */

export const SITE_URL = 'https://persim.w3cub.com'
export const APP_STORE_URL = 'https://apps.apple.com/app/id6835099132'
export const SUPPORT_EMAIL = 'persim@w3cub.com'
export const APP_VERSION = '1.0'
export const SITE_TITLE = 'Persim'
export const SITE_LOGO = '/logo.png'
export const OG_IMAGE = `${SITE_URL}/preview.png`

/** Languages offered by this website (the app itself ships 25 UI languages). */
export const WEBSITE_LANGS = [
  'en',
  'zh-CN',
  'zh-TW',
  'ja',
  'de',
  'es',
  'fr',
] as const

/**
 * Accent colours. The first one is sampled from the Persim logo, so the
 * website opens in the product's own colour; the rest match the app settings.
 * Order here drives both the nav picker and the homepage swatches.
 */
export const ACCENTS = [
  { name: 'persimmon', value: '#f04a00' },
  { name: 'violet', value: '#8b5cf6' },
  { name: 'teal', value: '#14b8a6' },
  { name: 'green', value: '#22c55e' },
  { name: 'blue', value: '#3b82f6' },
  { name: 'rose', value: '#f43f5e' },
] as const

export const DEFAULT_ACCENT = ACCENTS[0].value
export const ACCENT_STORAGE_KEY = 'persim-accent'
