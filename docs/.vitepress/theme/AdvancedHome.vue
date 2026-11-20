<template>
  <div class="advanced-home">
    <SiteNav />

    <!-- Hero: the new-tab page is the product's front door -->
    <section class="hero-section">
      <div class="hero-container">
        <div class="hero-copy">
          <span class="version-badge">{{ data.versionBadge }}</span>
          <h1 class="hero-title">{{ data.hero.name }}</h1>
          <p class="hero-subtitle">{{ data.hero.text }}</p>
          <p class="hero-description">{{ data.hero.tagline }}</p>
          <HomeActions :actions="data.actions" />
          <p class="download-note">{{ data.downloadNote }}</p>
        </div>
        <div class="hero-visual">
          <span class="tab-tint tab-tint-newtab" aria-hidden="true"></span>
          <img :src="withBase(data.hero.image.src)" :alt="data.hero.image.alt" />
        </div>
      </div>
      <div class="hero-bg-pattern"></div>
    </section>

    <!-- Features -->
    <section class="features-section" id="features">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">{{ data.sections.featuresTitle }}</h2>
          <p class="section-subtitle">{{ data.sections.featuresSubtitle }}</p>
        </div>
        <div class="features-grid">
          <div v-for="(feature, index) in data.features" :key="feature.title" class="feature-card">
            <div class="feature-icon">
              <span
                class="feature-glyph"
                role="img"
                :aria-label="feature.iconAlt || ''"
                :style="{
                  '-webkit-mask-image': `url(${withBase(feature.icon)})`,
                  maskImage: `url(${withBase(feature.icon)})`,
                }"
              ></span>
            </div>
            <h3 class="feature-title">{{ feature.title }}</h3>
            <p class="feature-description">{{ feature.details }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Screenshots + accent-colour playground -->
    <section class="shots-section">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">{{ data.sections.shotsTitle }}</h2>
          <p class="section-subtitle">{{ data.sections.shotsSubtitle }}</p>
        </div>
        <div class="banner-gallery">
          <div class="banner-stage">
            <a
              v-for="(banner, index) in bannerImages"
              :key="banner.src"
              :href="banner.href"
              class="banner-slide"
              :class="{ active: activeBanner === index }"
              :aria-hidden="activeBanner !== index"
              :tabindex="activeBanner === index ? 0 : -1"
            >
              <img :src="withBase(banner.src)" :alt="banner.alt" loading="lazy" />
            </a>
          </div>
          <div class="banner-controls">
            <button
              v-for="(banner, index) in bannerImages"
              :key="banner.src"
              type="button"
              class="banner-thumb"
              :class="{ active: activeBanner === index }"
              :aria-pressed="activeBanner === index"
              @click="activeBanner = index"
            >
              <span class="thumb-index">0{{ index + 1 }}</span>
              <span class="thumb-title">{{ data.banners?.[index]?.title || banner.title }}</span>
            </button>
          </div>
        </div>
        <div class="accent-panel">
          <div class="accent-copy">
            <h3>{{ data.sections.accentTitle }}</h3>
            <p>{{ data.sections.accentSubtitle }}</p>
          </div>
          <div class="accent-swatches" role="group" :aria-label="data.sections.accentTitle">
            <button
              v-for="(accent, index) in accents"
              :key="accent.value"
              type="button"
              class="accent-swatch"
              :class="{ active: activeAccent === accent.value }"
              :style="{ backgroundColor: accent.value }"
              :title="accentNames[index] || data.accentLabels?.[index] || accent.name"
              :aria-label="accentNames[index] || data.accentLabels?.[index] || accent.name"
              :aria-pressed="activeAccent === accent.value"
              @click="applyAccent(accent.value)"
            >
              <svg v-if="activeAccent === accent.value" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 5 5L19 7" /></svg>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- How it works -->
    <section class="how-section">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">{{ data.sections.howTitle }}</h2>
          <p class="section-subtitle">{{ data.sections.howSubtitle }}</p>
        </div>
        <div class="steps-grid">
          <div class="step-card" v-for="step in data.steps" :key="step.num">
            <div class="step-number">{{ step.num }}</div>
            <h3 class="step-title">{{ step.title }}</h3>
            <p class="step-desc">{{ step.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="faq-section">
      <div class="container faq-container">
        <div class="section-header">
          <h2 class="section-title">{{ data.sections.faqTitle }}</h2>
          <p class="section-subtitle">{{ data.sections.faqSubtitle }}</p>
        </div>
        <div class="faq-grid">
          <details v-for="faq in data.faqs" :key="faq.question" class="faq-item">
            <summary class="faq-question">{{ faq.question }}</summary>
            <div class="faq-answer">{{ faq.answer }}</div>
          </details>
        </div>
        <p class="faq-more"><a :href="withBase(localeLink('/guide/faq', lang))">{{ data.faqMore }}</a></p>
      </div>
    </section>

    <!-- Download CTA -->
    <section class="cta-section">
      <div class="container cta-container">
        <h2 class="cta-title">{{ data.cta.title }}</h2>
        <p class="cta-description">{{ data.cta.description }}</p>
        <div class="cta-actions">
          <a :href="data.cta.primaryLink" target="_blank" rel="noopener noreferrer" class="btn btn-primary">{{ data.cta.primary }}</a>
          <a :href="withBase(localeLink(data.cta.secondaryLink, lang))" class="btn btn-secondary">{{ data.cta.secondary }}</a>
        </div>
      </div>
    </section>

    <SiteFooter />
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { withBase, useData } from 'vitepress'
import HomeActions from './HomeActions.vue'
import SiteNav from './SiteNav.vue'
import SiteFooter from './SiteFooter.vue'
import { localeLink } from './locale'
import { ACCENTS } from './site'
import { activeAccent, applyAccent } from './accent'

defineProps<{ data: any }>()
const { lang, theme } = useData()
const accents = ACCENTS
const accentNames = computed(() => (theme.value as any).accentNames || [])
const activeBanner = ref(0)
const bannerImages = [
  { src: '/banners/tabs.png', alt: 'Persim new tab page', title: 'Tabs that keep up', href: '#features' },
  { src: '/banners/settings.png', alt: 'Persim settings', title: 'Make it yours', href: localeLink('/guide/features', lang.value) },
  { src: '/banners/tampermonkey.png', alt: 'Persim userscripts', title: 'Supercharge your browser', href: localeLink('/guide/features', lang.value) },
]
</script>

<style scoped>
.advanced-home {
  font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
  line-height: 1.6;
  color: var(--vp-c-text-1);
  overflow: hidden;
}
.container { max-width: 1120px; margin: 0 auto; padding: 0 24px; }

/* Hero */
.hero-section { padding: 132px 0 80px; background: var(--ah-hero-bg); position: relative; }
.hero-container { max-width: 1060px; margin: 0 auto; padding: 0 24px; position: relative; z-index: 2; }
.hero-copy { text-align: center; max-width: 720px; margin: 0 auto 48px; }
.version-badge { display: inline-flex; padding: 5px 14px; border-radius: 999px; background: var(--vp-c-brand-soft); color: var(--vp-c-brand-1); border: 1px solid var(--ah-badge-border); font-size: 13px; font-weight: 600; margin-bottom: 20px; }
.hero-title { font-size: 3.7rem; font-weight: 700; margin: 0 0 10px; line-height: 1.1; letter-spacing: -0.035em; color: var(--vp-c-text-1); }
.hero-subtitle { font-size: 1.65rem; font-weight: 600; margin: 0 0 14px; color: var(--vp-c-text-1); }
.hero-description { font-size: 1.03rem; margin: 0 auto; color: var(--vp-c-text-2); max-width: 600px; }
.download-note { margin: 16px 0 0; font-size: 12.5px; color: var(--vp-c-text-3); }
.hero-visual { position: relative; }
.hero-visual img { display: block; width: 100%; height: auto; border-radius: 18px; border: 1px solid var(--ah-img-border); box-shadow: var(--ah-img-shadow); }

/* The screenshot's tab strip is knocked out to transparency, with a matching
   alpha mask for the exact curves (window corners + active tab). One image,
   one mask, one colour layer that follows the site accent. */
.tab-tint {
  position: absolute;
  inset: 0;
  z-index: 0;
  border-radius: inherit;
  /* Mirrors Rust's tab_strip.rs: `accent.opacity(0.08)` over white.
     The original screenshot's pale blue IS #2563eb at 8% over #fff, so the
     replacement must use the same 8% ratio — anything stronger looks too dark. */
  background: color-mix(in srgb, var(--vp-c-brand-1) 8%, #ffffff);
  -webkit-mask-repeat: no-repeat;
  mask-repeat: no-repeat;
  -webkit-mask-size: 100% 100%;
  mask-size: 100% 100%;
  pointer-events: none;
}
.tab-tint-newtab { -webkit-mask-image: url('/screenshot-newtab-mask.png'); mask-image: url('/screenshot-newtab-mask.png'); }
.hero-visual img { position: relative; z-index: 1; }
.hero-bg-pattern { position: absolute; inset: 0; pointer-events: none; background: radial-gradient(circle at 18% 24%, color-mix(in srgb, var(--vp-c-brand-1) 9%, transparent) 0%, transparent 42%), radial-gradient(circle at 84% 10%, color-mix(in srgb, var(--vp-c-brand-1) 7%, #ffffff) 0%, transparent 42%); }

/* Shared */
.section-header { text-align: center; margin-bottom: 46px; }
.section-title { font-size: 2.1rem; font-weight: 700; margin: 0 0 12px; letter-spacing: -0.025em; }
.section-subtitle { font-size: 1rem; color: var(--vp-c-text-2); margin: 0 auto; max-width: 640px; }
.btn { display: inline-flex; align-items: center; justify-content: center; padding: 13px 28px; border-radius: 12px; text-decoration: none; font-weight: 600; font-size: 15px; transition: .18s ease; }
.btn-primary { background: var(--vp-c-brand-1); color: #fff; box-shadow: 0 6px 18px color-mix(in srgb, var(--vp-c-brand-1) 25%, transparent); }
.btn-primary:hover { transform: translateY(-2px); }
.btn-secondary { background: var(--ah-card-bg); color: var(--vp-c-text-1); border: 1px solid var(--vp-c-divider); }
.btn-secondary:hover { border-color: var(--vp-c-brand-1); color: var(--vp-c-brand-1); transform: translateY(-2px); }

/* Features */
.features-section { padding: 92px 0; background: var(--vp-c-bg); }
.features-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 18px; }
.feature-card { background: var(--ah-card-bg); padding: 30px 26px; border-radius: 16px; border: 1px solid var(--vp-c-divider); box-shadow: var(--ah-card-shadow); transition: border-color .2s ease, transform .2s ease; }
.feature-card:hover { transform: translateY(-3px); border-color: var(--vp-c-brand-1); }
.feature-icon { width: 48px; height: 48px; border-radius: 13px; background: var(--vp-c-brand-soft); display: flex; align-items: center; justify-content: center; margin-bottom: 20px; }
/* Masks use each SVG's alpha, so the glyph always matches the live accent
   instead of the fixed blue baked into the files. */
.feature-glyph {
  display: block;
  width: 26px;
  height: 26px;
  background: var(--vp-c-brand-1);
  -webkit-mask-repeat: no-repeat;
  mask-repeat: no-repeat;
  -webkit-mask-position: center;
  mask-position: center;
  -webkit-mask-size: contain;
  mask-size: contain;
}
.feature-title { font-size: 1.08rem; font-weight: 650; margin: 0 0 8px; }
.feature-description { color: var(--vp-c-text-2); font-size: .92rem; line-height: 1.7; margin: 0; }

/* Screenshots + accents */
.shots-section { padding: 92px 0; background: var(--vp-c-bg-soft); }
/* Screenshot banners: one large slide + selectable captions beneath. */
.banner-gallery { max-width: 1080px; margin: 0 auto; }
.banner-stage {
  position: relative;
  width: 100%;
  aspect-ratio: 1586 / 992;
  border-radius: 18px;
  overflow: hidden;
  border: 1px solid var(--vp-c-divider);
  box-shadow: var(--ah-img-shadow);
  background: var(--ah-card-bg);
}
.banner-slide {
  position: absolute;
  inset: 0;
  opacity: 0;
  visibility: hidden;
  transition: opacity .3s ease;
}
.banner-slide.active { opacity: 1; visibility: visible; }
.banner-slide img { display: block; width: 100%; height: 100%; object-fit: cover; }
.banner-controls { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-top: 16px; }
.banner-thumb {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 14px 16px;
  background: var(--ah-card-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  cursor: pointer;
  text-align: left;
  transition: border-color .18s ease, transform .18s ease;
}
.banner-thumb:hover { transform: translateY(-2px); border-color: var(--vp-c-brand-1); }
.banner-thumb.active { border-color: var(--vp-c-brand-1); background: var(--vp-c-brand-soft); }
.thumb-index { font-size: .72rem; font-weight: 700; color: var(--vp-c-brand-1); letter-spacing: .08em; }
.thumb-title { font-size: .88rem; font-weight: 600; color: var(--vp-c-text-1); }
.accent-panel { margin-top: 24px; display: flex; align-items: center; justify-content: space-between; gap: 28px; flex-wrap: wrap; padding: 24px 30px; background: var(--ah-card-bg); border: 1px solid var(--vp-c-divider); border-radius: 16px; }
.accent-copy h3 { margin: 0 0 4px; font-size: 1.1rem; font-weight: 650; }
.accent-copy p { margin: 0; color: var(--vp-c-text-2); font-size: .9rem; }
.accent-swatches { display: flex; gap: 12px; }
.accent-swatch { width: 32px; height: 32px; border-radius: 50%; border: 3px solid var(--ah-card-bg); box-shadow: 0 0 0 1px var(--vp-c-divider); display: inline-flex; align-items: center; justify-content: center; cursor: pointer; padding: 0; transition: transform .15s ease, box-shadow .15s ease; }
.accent-swatch:hover { transform: scale(1.12); }
.accent-swatch.active { box-shadow: 0 0 0 2px var(--vp-c-brand-1); }

/* Steps */
.how-section { padding: 92px 0; background: var(--vp-c-bg); }
.steps-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 22px; }
.step-card { background: var(--ah-card-bg); border: 1px solid var(--vp-c-divider); border-radius: 16px; padding: 30px 26px; }
.step-number { font-size: .78rem; font-weight: 700; letter-spacing: .14em; color: var(--vp-c-brand-1); margin-bottom: 14px; }
.step-title { font-size: 1.08rem; font-weight: 650; margin: 0 0 8px; }
.step-desc { font-size: .92rem; color: var(--vp-c-text-2); margin: 0; }

/* FAQ */
.faq-section { padding: 92px 0; background: var(--vp-c-bg-soft); }
.faq-container { max-width: 800px; }
.faq-grid { display: grid; gap: 12px; }
.faq-item { background: var(--ah-card-bg); border: 1px solid var(--vp-c-divider); border-radius: 12px; }
.faq-question { padding: 18px 24px; cursor: pointer; font-weight: 600; color: var(--vp-c-text-1); list-style: none; display: flex; align-items: center; justify-content: space-between; gap: 12px; }
.faq-question::-webkit-details-marker { display: none; }
.faq-question::after { content: '+'; font-size: 20px; font-weight: 400; color: var(--vp-c-text-3); }
.faq-item[open] .faq-question::after { transform: rotate(45deg); }
.faq-answer { padding: 0 24px 20px; color: var(--vp-c-text-2); font-size: .93rem; }
.faq-more { text-align: center; margin: 24px 0 0; }
.faq-more a { color: var(--vp-c-brand-1); font-weight: 600; text-decoration: none; }

/* CTA */
.cta-section { padding: 84px 0; background: linear-gradient(135deg, color-mix(in srgb, var(--vp-c-brand-1) 12%, var(--vp-c-bg)) 0%, color-mix(in srgb, var(--vp-c-brand-1) 4%, var(--vp-c-bg)) 100%); border-top: 1px solid var(--vp-c-divider); }
.cta-container { text-align: center; max-width: 700px; }
.cta-title { font-size: 2.1rem; font-weight: 700; margin: 0 0 14px; }
.cta-description { font-size: 1rem; color: var(--vp-c-text-2); margin: 0 0 30px; }
.cta-actions { display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; }

@media (max-width: 900px) {
  .features-grid, .steps-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .banner-controls { gap: 8px; }
  .banner-thumb { padding: 12px; }
}
@media (max-width: 680px) {
  .hero-section { padding: 112px 0 60px; }
  .hero-title { font-size: 2.7rem; }
  .hero-subtitle { font-size: 1.3rem; }
  .section-title { font-size: 1.8rem; }
  .features-section, .shots-section, .how-section, .faq-section { padding: 68px 0; }
  .features-grid, .steps-grid { grid-template-columns: 1fr; }
  .banner-controls { grid-template-columns: 1fr; }
  .cta-actions { flex-direction: column; align-items: center; }
  .cta-actions .btn { width: 100%; max-width: 280px; }
}
</style>
