/**
 * Site-wide accent colour state.
 *
 * A single module-level ref keeps the nav picker and the homepage swatches in
 * sync, while the CSS variables are written to <html> so guide pages, the
 * sidebar, the footer and dark mode all follow the selection. The choice is
 * persisted so it survives reloads and language switches.
 */
import { ref } from 'vue'
import { ACCENTS, ACCENT_STORAGE_KEY, DEFAULT_ACCENT } from './site'

export const activeAccent = ref<string>(DEFAULT_ACCENT)

export function applyAccent(value: string) {
  const color = ACCENTS.find((a) => a.value === value)?.value ?? DEFAULT_ACCENT
  const root = document.documentElement

  root.style.setProperty('--vp-c-brand-1', color)
  // Inline variables beat VitePress' `.dark` rules, so the darker shades must
  // be derived here too instead of relying on the stylesheet defaults.
  root.style.setProperty('--vp-c-brand-2', `color-mix(in srgb, ${color} 84%, #000)`)
  root.style.setProperty('--vp-c-brand-3', `color-mix(in srgb, ${color} 70%, #000)`)
  root.style.setProperty('--vp-c-brand-soft', `color-mix(in srgb, ${color} 13%, transparent)`)
  root.style.setProperty(
    '--vp-home-hero-name-background',
    `linear-gradient(135deg, ${color} 0%, color-mix(in srgb, ${color} 74%, #000) 100%)`
  )

  document.querySelector('meta[name="theme-color"]')?.setAttribute('content', color)

  try {
    localStorage.setItem(ACCENT_STORAGE_KEY, color)
  } catch {
    // Private browsing / disabled storage: the choice still applies this session.
  }

  activeAccent.value = color
}

export function initAccent() {
  // VitePress also runs enhanceApp during the static build (Node, no DOM).
  if (typeof document === 'undefined') return

  let saved: string | null = null
  try {
    saved = localStorage.getItem(ACCENT_STORAGE_KEY)
  } catch {
    // Ignore and fall back to the logo colour.
  }
  applyAccent(saved || DEFAULT_ACCENT)
}
