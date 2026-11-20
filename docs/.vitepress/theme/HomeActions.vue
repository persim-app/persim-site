<script setup lang="ts">
import { withBase } from 'vitepress'
import { useData } from 'vitepress'
import { localeLink } from './locale'
import { computed } from 'vue'

type Action = { text: string; link: string; theme?: 'brand' | 'alt'; external?: boolean }

const props = defineProps<{ actions?: Action[] }>()
const { lang } = useData()

function href(action: Action) {
  if (action.external || /^(https?:|mailto:)/.test(action.link)) return action.link
  return withBase(localeLink(action.link, lang.value))
}
const items = computed(() => props.actions ?? [])
</script>

<template>
  <div class="home-actions">
    <a
      v-for="action in items"
      :key="action.text"
      :href="href(action)"
      :class="['action-btn', action.theme === 'alt' ? 'alt' : 'brand']"
      :target="action.external ? '_blank' : undefined"
      :rel="action.external ? 'noopener noreferrer' : undefined"
    >
      <svg v-if="action.theme !== 'alt'" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M12 3v12m0 0 4-4m-4 4-4-4" />
        <path d="M4 17v3h16v-3" />
      </svg>
      {{ action.text }}
    </a>
  </div>
</template>

<style scoped>
.home-actions {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 30px;
}
.action-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 9px;
  min-width: 148px;
  padding: 12px 22px;
  border-radius: 12px;
  font-size: 15px;
  font-weight: 600;
  text-decoration: none;
  transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease;
}
.action-btn.brand {
  background: var(--vp-c-brand-1);
  color: #fff;
  box-shadow: 0 6px 18px color-mix(in srgb, var(--vp-c-brand-1) 25%, transparent);
}
.action-btn.brand:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 24px color-mix(in srgb, var(--vp-c-brand-1) 32%, transparent);
}
.action-btn.alt {
  background: var(--ah-card-bg);
  color: var(--vp-c-text-1);
  border: 1px solid var(--vp-c-divider);
}
.action-btn.alt:hover {
  transform: translateY(-2px);
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
}
@media (max-width: 480px) {
  .action-btn { width: 100%; max-width: 300px; }
}
</style>
