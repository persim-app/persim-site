<template>
  <div class="accent-picker" ref="rootEl">
    <button
      type="button"
      class="accent-trigger"
      :title="label"
      :aria-label="label"
      :aria-expanded="open"
      @click="open = !open"
    >
      <span class="accent-dot" :style="{ background: activeAccent }"></span>
    </button>

    <Transition name="accent-pop">
      <div v-if="open" class="accent-menu" role="group" :aria-label="label">
        <p class="accent-menu-title">{{ label }}</p>
        <button
          v-for="(accent, index) in ACCENTS"
          :key="accent.value"
          type="button"
          class="accent-option"
          :class="{ active: activeAccent === accent.value }"
          @click="choose(accent.value)"
        >
          <span class="option-dot" :style="{ background: accent.value }">
            <svg
              v-if="activeAccent === accent.value"
              viewBox="0 0 24 24" width="12" height="12" fill="none"
              stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"
              aria-hidden="true"
            ><path d="m5 12 5 5L19 7" /></svg>
          </span>
          <span class="option-name">{{ names[index] || accent.name }}</span>
        </button>
      </div>
    </Transition>
  </div>
</template>

<script setup lang="ts">
import { computed, ref, onMounted, onUnmounted, watch } from 'vue'
import { useData, useRoute } from 'vitepress'
import { ACCENTS } from './site'
import { activeAccent, applyAccent } from './accent'

const { theme } = useData()
const route = useRoute()

const rootEl = ref<HTMLElement | null>(null)
const open = ref(false)

const label = computed(() => (theme.value as any).accentLabel || 'Accent colour')
const names = computed(() => (theme.value as any).accentNames || [])

function choose(value: string) {
  applyAccent(value)
  open.value = false
}

function onDocClick(e: MouseEvent) {
  if (open.value && rootEl.value && !rootEl.value.contains(e.target as Node)) {
    open.value = false
  }
}
function onKey(e: KeyboardEvent) {
  if (e.key === 'Escape') open.value = false
}

watch(() => route.path, () => { open.value = false })
onMounted(() => {
  document.addEventListener('click', onDocClick)
  document.addEventListener('keydown', onKey)
})
onUnmounted(() => {
  document.removeEventListener('click', onDocClick)
  document.removeEventListener('keydown', onKey)
})
</script>

<style scoped>
.accent-picker {
  position: relative;
  display: flex;
  align-items: center;
}

.accent-trigger {
  width: 34px;
  height: 34px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0;
  border: 1px solid var(--vp-c-divider);
  border-radius: 10px;
  background: var(--vp-c-bg);
  cursor: pointer;
  transition: border-color .18s ease, background .18s ease;
}
.accent-trigger:hover,
.accent-trigger[aria-expanded='true'] {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}

.accent-dot {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  box-shadow: inset 0 0 0 1px rgba(0, 0, 0, .08), 0 0 0 3px var(--vp-c-brand-soft);
}

.accent-menu {
  position: absolute;
  top: calc(100% + 10px);
  right: 0;
  width: 168px;
  padding: 10px;
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 14px;
  box-shadow: 0 14px 38px rgba(15, 23, 42, .14);
  z-index: 1001;
}
.dark .accent-menu { box-shadow: 0 14px 38px rgba(0, 0, 0, .5); }

.accent-menu-title {
  margin: 2px 8px 8px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--vp-c-text-3);
}

.accent-option {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 7px 8px;
  border: 0;
  border-radius: 8px;
  background: transparent;
  color: var(--vp-c-text-2);
  font-size: 13px;
  text-align: left;
  cursor: pointer;
  transition: background .15s ease, color .15s ease;
}
.accent-option:hover { background: var(--vp-c-bg-soft); color: var(--vp-c-text-1); }
.accent-option.active { color: var(--vp-c-brand-1); font-weight: 600; }

.option-dot {
  flex: 0 0 auto;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-shadow: inset 0 0 0 1px rgba(0, 0, 0, .08);
}

.option-name { white-space: nowrap; }

.accent-pop-enter-active, .accent-pop-leave-active { transition: opacity .15s ease, transform .15s ease; }
.accent-pop-enter-from, .accent-pop-leave-to { opacity: 0; transform: translateY(-6px); }
</style>
