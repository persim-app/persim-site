<template>
  <div class="advanced-home">
    <!-- Shared navigation: brand + nav + language switcher + dark mode toggle -->
    <SiteNav />

    <!-- Hero -->
    <section class="hero-section">
      <div class="hero-container">
        <div class="hero-copy">
          <span class="version-badge">{{ content.versionBadge }}</span>
          <h1 class="hero-title">{{ data.hero.name }}</h1>
          <p class="hero-subtitle">{{ data.hero.text }}</p>
          <p class="hero-description">{{ data.hero.tagline }}</p>
          <HomeActions />
        </div>
        <div class="hero-visual-wide">
          <img :src="withBase(data.hero.image.src)" :alt="data.hero.image.alt" />
        </div>
      </div>
      <div class="hero-bg-pattern"></div>
    </section>

    <!-- Features -->
    <section class="features-section" id="features">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">{{ content.sections.featuresTitle }}</h2>
          <p class="section-subtitle">{{ content.sections.featuresSubtitle }}</p>
        </div>
        <div class="features-grid">
          <div v-for="(feature, index) in data.features" :key="feature.title"
               class="feature-card"
               :style="{ animationDelay: `${index * 0.08}s` }">
            <div class="feature-icon" :style="{ backgroundColor: featureColors[index % featureColors.length] }">
              <img :src="withBase(feature.icon.light)" :alt="feature.icon.alt"
                   :width="feature.icon.width" :height="feature.icon.height" />
            </div>
            <h3 class="feature-title">{{ feature.title }}</h3>
            <p class="feature-description">{{ feature.details }}</p>
            <a v-if="feature.link" :href="localeLink(feature.link, lang)" class="feature-link">{{ feature.linkText }}</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Screenshots -->
    <section class="shots-section">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">{{ content.sections.screenshotsTitle }}</h2>
          <p class="section-subtitle">{{ content.sections.screenshotsSubtitle }}</p>
        </div>
        <div class="shots-grid">
          <figure class="shot-card" v-for="shot in content.screenshots" :key="shot.src">
            <div class="shot-image">
              <img :src="withBase(shot.src)" :alt="shot.title" loading="lazy" />
            </div>
            <figcaption>
              <h3>{{ shot.title }}</h3>
              <p>{{ shot.desc }}</p>
            </figcaption>
          </figure>
        </div>
      </div>
    </section>

    <!-- Pets & pricing -->
    <section class="pets-section">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">{{ content.sections.petsTitle }}</h2>
          <p class="section-subtitle">{{ content.sections.petsSubtitle }}</p>
        </div>
        <div class="pets-grid">
          <div class="pet-card" v-for="pet in content.pets" :key="pet.name">
            <span v-if="pet.badge" class="pet-badge">{{ pet.badge }}</span>
            <div class="pet-image">
              <img :src="withBase(pet.image)" :alt="pet.name" class="pet-img" loading="lazy" />
            </div>
            <h3 class="pet-name">{{ pet.name }}</h3>
            <p class="pet-desc">{{ pet.desc }}</p>
            <div class="pet-price" :class="{ free: pet.free }">{{ pet.price }}</div>
          </div>
        </div>
        <div class="bundle-card">
          <div class="bundle-info">
            <h3>{{ content.bundle.title }}</h3>
            <p>{{ content.bundle.desc }}</p>
          </div>
          <div class="bundle-price">{{ content.bundle.price }}</div>
        </div>
        <div class="pets-cta">
          <a :href="localeLink('/guide/pets', lang)" class="btn btn-primary">{{ content.petsCta }}</a>
        </div>
      </div>
    </section>

    <!-- How it works -->
    <section class="how-section">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">{{ content.sections.howTitle }}</h2>
          <p class="section-subtitle">{{ content.sections.howSubtitle }}</p>
        </div>
        <div class="steps-grid">
          <div class="step-card" v-for="(step, index) in content.steps" :key="index">
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
          <h2 class="section-title">{{ content.sections.faqTitle }}</h2>
          <p class="section-subtitle">{{ content.sections.faqSubtitle }}</p>
        </div>
        <div class="faq-grid">
          <div v-for="faq in content.faqs" :key="faq.question" class="faq-item">
            <details class="faq-details">
              <summary class="faq-question">{{ faq.question }}</summary>
              <div class="faq-answer">{{ faq.answer }}</div>
            </details>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="cta-section">
      <div class="container cta-container">
        <h2 class="cta-title">{{ content.cta.title }}</h2>
        <p class="cta-description">{{ content.cta.description }}</p>
        <div class="cta-actions">
          <a :href="localeLink(content.cta.primaryLink, lang)" class="btn btn-primary">{{ content.cta.primary }}</a>
          <a :href="localeLink(content.cta.secondaryLink, lang)" class="btn btn-secondary">{{ content.cta.secondary }}</a>
        </div>
      </div>
    </section>

    <SiteFooter />
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { withBase, useData } from 'vitepress'
import HomeActions from './HomeActions.vue'
import SiteNav from './SiteNav.vue'
import SiteFooter from './SiteFooter.vue'
import { localeLink } from './locale'

interface Props {
  data: any
}

const props = defineProps<Props>()
const { lang } = useData()

// All translatable content comes from the localized page's frontmatter.
const content = computed(() => props.data || {})

const featureColors = [
  '#f97316', // orange
  '#8b5cf6', // violet
  '#10b981', // emerald
  '#3b82f6', // blue
  '#ec4899', // pink
  '#f59e0b', // amber
]
</script>

<style scoped>
.advanced-home {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  line-height: 1.6;
  color: var(--vp-c-text-1);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* ── Hero ─────────────────────────────────────────────────────── */
.hero-section {
  padding: 140px 0 90px;
  background: var(--ah-hero-bg);
  position: relative;
  overflow: hidden;
}

.hero-container {
  max-width: 1120px;
  margin: 0 auto;
  padding: 0 20px;
  position: relative;
  z-index: 2;
}

.hero-copy {
  text-align: center;
  max-width: 780px;
  margin: 0 auto 56px;
}

.version-badge {
  display: inline-flex;
  align-items: center;
  padding: 6px 16px;
  border-radius: 999px;
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
  border: 1px solid var(--ah-badge-border);
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.02em;
  margin-bottom: 24px;
}

.hero-title {
  font-size: 4.25rem;
  font-weight: 800;
  margin: 0 0 12px;
  line-height: 1.05;
  letter-spacing: -0.03em;
  background: linear-gradient(135deg, var(--ah-hero-title-from) 0%, var(--ah-hero-title-to) 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-subtitle {
  font-size: 1.9rem;
  font-weight: 600;
  margin: 0 0 18px;
  color: var(--vp-c-text-1);
  opacity: 0.9;
  letter-spacing: -0.01em;
}

.hero-description {
  font-size: 1.12rem;
  margin: 0 auto;
  color: var(--vp-c-text-2);
  line-height: 1.7;
  max-width: 620px;
}

.hero-visual-wide {
  position: relative;
}

.hero-visual-wide img {
  display: block;
  width: 100%;
  height: auto;
  border-radius: 20px;
  border: 1px solid var(--ah-img-border);
  box-shadow: var(--ah-img-shadow);
}

.hero-bg-pattern {
  position: absolute;
  inset: 0;
  background-image:
    radial-gradient(circle at 15% 20%, rgba(249, 115, 22, 0.12) 0%, transparent 45%),
    radial-gradient(circle at 85% 12%, rgba(251, 191, 36, 0.14) 0%, transparent 45%);
  pointer-events: none;
}

/* ── Shared section bits ──────────────────────────────────────── */
.section-header {
  text-align: center;
  margin-bottom: 56px;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin: 0 0 14px;
  letter-spacing: -0.02em;
  color: var(--vp-c-text-1);
}

.section-subtitle {
  font-size: 1.05rem;
  color: var(--vp-c-text-2);
  margin: 0 auto;
  max-width: 640px;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 14px 30px;
  border-radius: 12px;
  text-decoration: none;
  font-weight: 600;
  font-size: 1rem;
  transition: all 0.2s ease;
  cursor: pointer;
}

.btn-primary {
  background: var(--vp-c-brand-1);
  color: #ffffff;
  border: 1px solid var(--vp-c-brand-1);
  box-shadow: 0 6px 20px rgba(249, 115, 22, 0.25);
}

.btn-primary:hover {
  background: var(--vp-c-brand-2);
  transform: translateY(-2px);
}

.btn-secondary {
  background: transparent;
  color: var(--vp-c-text-1);
  border: 1.5px solid var(--vp-c-divider);
}

.btn-secondary:hover {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
  transform: translateY(-2px);
}

/* ── Features ─────────────────────────────────────────────────── */
.features-section {
  padding: 100px 0;
  background: var(--vp-c-bg);
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 24px;
}

.feature-card {
  background: var(--ah-card-bg);
  padding: 36px 28px;
  border-radius: 18px;
  box-shadow: var(--ah-card-shadow);
  border: 1px solid var(--vp-c-divider);
  transition: all 0.25s ease;
  animation: fadeInUp 0.5s ease-out forwards;
  opacity: 0;
  transform: translateY(20px);
}

.feature-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--ah-card-shadow-hover);
  border-color: var(--vp-c-brand-1);
}

.feature-icon {
  width: 60px;
  height: 60px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 22px;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.12);
}

.feature-icon img {
  filter: brightness(0) invert(1);
}

.feature-title {
  font-size: 1.2rem;
  font-weight: 600;
  margin: 0 0 10px;
  color: var(--vp-c-text-1);
}

.feature-description {
  color: var(--vp-c-text-2);
  line-height: 1.65;
  margin: 0 0 18px;
  font-size: 0.95rem;
}

.feature-link {
  color: var(--vp-c-brand-1);
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
}

.feature-link:hover {
  text-decoration: underline;
}

/* ── Screenshots ──────────────────────────────────────────────── */
.shots-section {
  padding: 100px 0;
  background: var(--vp-c-bg-soft);
}

.shots-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 32px;
}

.shot-card {
  margin: 0;
  background: var(--ah-card-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 18px;
  overflow: hidden;
  box-shadow: var(--ah-card-shadow);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.shot-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--ah-card-shadow-hover);
}

.shot-image {
  padding: 16px 16px 0;
}

.shot-image img {
  display: block;
  width: 100%;
  height: auto;
  border-radius: 10px;
  border: 1px solid var(--ah-img-border);
}

.shot-card figcaption {
  padding: 20px 24px 26px;
}

.shot-card figcaption h3 {
  font-size: 1.15rem;
  font-weight: 600;
  margin: 0 0 8px;
  color: var(--vp-c-text-1);
}

.shot-card figcaption p {
  font-size: 0.93rem;
  color: var(--vp-c-text-2);
  margin: 0;
  line-height: 1.6;
}

/* ── Pets ─────────────────────────────────────────────────────── */
.pets-section {
  padding: 100px 0;
  background: var(--vp-c-bg);
}

.pets-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
  gap: 20px;
  margin-bottom: 28px;
}

.pet-card {
  position: relative;
  background: var(--ah-card-bg);
  border-radius: 18px;
  padding: 28px 20px 24px;
  text-align: center;
  box-shadow: var(--ah-card-shadow);
  border: 1px solid var(--vp-c-divider);
  transition: all 0.25s ease;
}

.pet-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--ah-card-shadow-hover);
  border-color: var(--vp-c-brand-1);
}

.pet-badge {
  position: absolute;
  top: 14px;
  right: 14px;
  padding: 3px 10px;
  border-radius: 999px;
  background: #ec4899;
  color: #ffffff;
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.02em;
}

.pet-image {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 110px;
  margin-bottom: 14px;
}

.pet-img {
  max-width: 108px;
  max-height: 108px;
  object-fit: contain;
  border-radius: 14px;
}

.pet-name {
  font-size: 1.02rem;
  font-weight: 600;
  color: var(--vp-c-text-1);
  margin: 0 0 6px;
}

.pet-desc {
  font-size: 0.82rem;
  color: var(--vp-c-text-2);
  margin: 0 0 14px;
  line-height: 1.5;
  min-height: 2.9em;
}

.pet-price {
  display: inline-block;
  padding: 4px 14px;
  border-radius: 999px;
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
  font-weight: 700;
  font-size: 0.9rem;
}

.pet-price.free {
  background: rgba(16, 185, 129, 0.14);
  color: #059669;
}

.dark .pet-price.free {
  color: #34d399;
}

.bundle-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  flex-wrap: wrap;
  padding: 24px 30px;
  border-radius: 16px;
  background: var(--ah-bundle-bg);
  border: 1px solid var(--ah-badge-border);
  margin-bottom: 36px;
}

.bundle-info h3 {
  font-size: 1.15rem;
  font-weight: 600;
  margin: 0 0 6px;
  color: var(--vp-c-text-1);
}

.bundle-info p {
  margin: 0;
  font-size: 0.92rem;
  color: var(--vp-c-text-2);
}

.bundle-price {
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--vp-c-brand-1);
  white-space: nowrap;
}

.pets-cta {
  text-align: center;
}

/* ── How it works ─────────────────────────────────────────────── */
.how-section {
  padding: 100px 0;
  background: var(--vp-c-bg-soft);
}

.steps-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 28px;
}

.step-card {
  background: var(--ah-card-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 16px;
  padding: 32px 26px;
}

.step-number {
  font-size: 0.8rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  color: var(--vp-c-brand-1);
  margin-bottom: 16px;
}

.step-title {
  font-size: 1.15rem;
  font-weight: 600;
  margin: 0 0 10px;
  color: var(--vp-c-text-1);
}

.step-desc {
  font-size: 0.93rem;
  color: var(--vp-c-text-2);
  margin: 0;
  line-height: 1.65;
}

/* ── FAQ ──────────────────────────────────────────────────────── */
.faq-section {
  padding: 100px 0;
  background: var(--vp-c-bg);
}

.faq-container {
  max-width: 820px;
}

.faq-grid {
  display: grid;
  gap: 14px;
}

.faq-item {
  background: var(--ah-card-bg);
  border-radius: 12px;
  border: 1px solid var(--vp-c-divider);
  overflow: hidden;
}

.faq-question {
  padding: 20px 26px;
  cursor: pointer;
  font-weight: 600;
  font-size: 1rem;
  color: var(--vp-c-text-1);
  text-align: left;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  list-style: none;
}

.faq-question::-webkit-details-marker {
  display: none;
}

.faq-question:hover {
  background: var(--ah-faq-hover-bg);
}

.faq-question::after {
  content: '+';
  font-size: 20px;
  font-weight: 400;
  color: var(--vp-c-text-3);
  transition: transform 0.2s;
}

.faq-details[open] .faq-question::after {
  transform: rotate(45deg);
}

.faq-answer {
  padding: 0 26px 22px;
  color: var(--vp-c-text-2);
  line-height: 1.7;
  font-size: 0.94rem;
}

/* ── CTA ──────────────────────────────────────────────────────── */
.cta-section {
  padding: 90px 0;
  background: linear-gradient(135deg, #f97316 0%, #ea580c 60%, #dc2626 100%);
  color: #ffffff;
}

.cta-container {
  text-align: center;
  max-width: 760px;
}

.cta-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin: 0 0 16px;
  line-height: 1.2;
}

.cta-description {
  font-size: 1.1rem;
  margin: 0 0 36px;
  opacity: 0.94;
  line-height: 1.65;
}

.cta-actions {
  display: flex;
  justify-content: center;
  gap: 16px;
  flex-wrap: wrap;
}

.cta-section .btn-primary {
  background: #ffffff;
  color: #ea580c;
  border-color: #ffffff;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}

.cta-section .btn-primary:hover {
  background: #fff7ed;
}

.cta-section .btn-secondary {
  color: #ffffff;
  border-color: rgba(255, 255, 255, 0.75);
}

.cta-section .btn-secondary:hover {
  color: #ffffff;
  border-color: #ffffff;
  background: rgba(255, 255, 255, 0.12);
}

/* ── Animations ───────────────────────────────────────────────── */
@keyframes fadeInUp {
  to { opacity: 1; transform: translateY(0); }
}

/* ── Responsive ───────────────────────────────────────────────── */
@media (max-width: 960px) {
  .steps-grid { grid-template-columns: 1fr; }
  .shots-grid { grid-template-columns: 1fr; }
}

@media (max-width: 768px) {
  .hero-section { padding: 120px 0 64px; }
  .hero-copy { margin-bottom: 40px; }
  .hero-title { font-size: 3rem; }
  .hero-subtitle { font-size: 1.5rem; }
  .section-title { font-size: 2rem; }
  .features-section, .shots-section, .pets-section,
  .how-section, .faq-section { padding: 72px 0; }
  .cta-section { padding: 72px 0; }
  .cta-title { font-size: 2rem; }
  .features-grid { grid-template-columns: 1fr; }
  .cta-actions { flex-direction: column; align-items: center; }
  .cta-actions .btn { width: 100%; max-width: 280px; }
  .bundle-card { padding: 20px; }
}

@media (max-width: 480px) {
  .hero-title { font-size: 2.5rem; }
  .hero-subtitle { font-size: 1.25rem; }
  .pets-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }
  .pet-card { padding: 20px 12px; }
  .pet-image { height: 88px; }
  .pet-img { max-width: 84px; max-height: 84px; }
  .shot-image { padding: 10px 10px 0; }
}
</style>
