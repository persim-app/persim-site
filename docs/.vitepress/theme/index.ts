import DefaultTheme from 'vitepress/theme'
import { h, defineComponent } from 'vue'
import { useRoute, useData } from 'vitepress'
import AdvancedHome from './AdvancedHome.vue'
import AccentPicker from './AccentPicker.vue'
import { initAccent } from './accent'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp() {
    // Apply the saved (or default logo) accent before the first paint so every
    // page — custom home and default-theme guides alike — starts in sync.
    initAccent()
  },
  // A stateful Layout: VitePress renders `() => h(Theme.Layout)` once, so a
  // functional component would never re-run on client-side navigation and the
  // localized frontmatter would go stale after a language switch.
  Layout: defineComponent({
    name: 'PersimLayout',
    setup() {
      const route = useRoute()
      const { frontmatter } = useData()

      const isHomePage = () =>
        route.path === '/' ||
        /^\/(zh-CN|zh-TW|ja|de|es|fr)\/?$/.test(route.path)

      return () => {
        if (isHomePage()) {
          // :key forces a clean remount per URL so no locale state leaks.
          return h(AdvancedHome, { data: frontmatter.value, key: route.path })
        }
        // Guide pages use the default theme; inject the same site-wide accent
        // control into its desktop nav bar and mobile nav screen. Like the
        // reminder site, guide pages have no site footer.
        return h(DefaultTheme.Layout, null, {
          'nav-bar-content-after': () => h(AccentPicker),
          'nav-screen-content-after': () => h(AccentPicker),
        })
      }
    },
  }),
}
