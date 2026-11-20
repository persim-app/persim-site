<script setup lang="ts">
import { withBase } from 'vitepress'
</script>

<template>
  <div class="home-badge-row">
    <a
      href="https://apps.apple.com/app/id6776577400"
      target="_blank"
      rel="noopener noreferrer"
      class="store-badge-link"
      aria-label="Download Reminder on the Mac App Store"
    >
      <img
        :src="withBase('/badges/Mac-App-Store.png')"
        alt="Download on the Mac App Store"
        class="store-badge"
        width="156"
        height="46"
      />
    </a>
    <a
      href="https://www.producthunt.com/products/pet-reminder?embed=true&utm_source=badge-featured&utm_medium=badge&utm_campaign=badge-pet-reminder"
      target="_blank"
      rel="noopener noreferrer"
      class="store-badge-link ph-link"
      aria-label="Reminder on Product Hunt"
    >
      <img
        src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1188444&theme=light"
        alt="Reminder — Reminders that grow with you | Product Hunt"
        class="store-badge ph-badge"
        width="250"
        height="54"
      />
    </a>
  </div>
</template>

<style scoped>
.home-badge-row {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 14px;
  margin-top: 32px;
  justify-content: center;
}

.store-badge-link {
  display: inline-flex;
  border-radius: 10px;
  transition: opacity 0.18s ease, transform 0.18s ease;
  outline-offset: 3px;
}

.store-badge-link:hover {
  opacity: 0.82;
  transform: translateY(-1px);
}

.store-badge {
  display: block;
  height: 46px;
  width: auto;
}

.ph-badge {
  height: 46px;
  border-radius: 10px;
  background: #ffffff;
}
</style>
