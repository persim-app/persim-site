import DefaultTheme from 'vitepress/theme'
import { h, defineComponent } from 'vue'
import { useRoute, useData } from 'vitepress'
import AdvancedHome from './AdvancedHome.vue'
import HomeActions from './HomeActions.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  // Layout MUST be a stateful component (defineComponent), not a bare function.
  // VitePressApp renders `() => h(Theme.Layout)` once with no reactive deps of
  // its own, so a functional Layout would never re-run on client-side
  // navigation — the URL would change but the localized frontmatter never would.
  Layout: defineComponent({
    name: 'ReminderLayout',
    setup() {
      const route = useRoute()
      const { frontmatter } = useData()

      const isHomePage = () =>
        route.path === '/' ||
        /^\/(zh-CN|zh-TW|ja|de|es|fr)\/?$/.test(route.path)

      return () => {
        if (isHomePage()) {
          // `:key` forces a clean remount per URL so no stale locale state leaks.
          return h(AdvancedHome, { data: frontmatter.value, key: route.path })
        }

        return h(
          DefaultTheme.Layout,
          { sidebar: false },
          { 'home-hero-info-after': () => h(HomeActions) }
        )
      }
    },
  }),
}
