# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-11-16

### Changed
- Rebranded the site from PetReminder to **Reminder** for the app's 2.0.0 release
- Rewrote all homepage and guide copy around the 2.0.0 native Rust + GPUI rebuild
- Replaced the hero with the new App Store artwork (Slice 3) and added two
  full-width screenshots (settings and pet store)
- Reworked the homepage into a centered hero + full-width artwork layout with
  features, screenshots, pets & pricing, steps, FAQ and CTA sections
- Updated pet catalog and pricing to match the runtime store catalog:
  British Shorthair free; Corgi, Husky, Ragdoll Cat and Shiba Inu $3.99;
  All Pets Pack $19.99 (removed the outdated Tugou, Cats Bundle and CNY prices)

### Added
- Full multilingual support: 7 locales (en, zh-CN, zh-TW, ja, de, es, fr),
  matching clipboard-site
- Per-locale nav, sidebar, footer, search chrome and markdown containers
- Language switcher (desktop dropdown + mobile panel) and appearance toggle
  in the shared `SiteNav.vue`
- Localized guide, FAQ and legal pages for all 7 languages
- Dark-mode-aware design tokens for every homepage section
- `versionBadge` on the hero, OG preview from the new artwork

### Technical
- `theme/index.ts` Layout is now a stateful `defineComponent` so localized
  frontmatter re-renders correctly on client-side navigation
- Replaced hard-coded homepage copy with frontmatter-driven content
- Added `localeLink()` locale prefixing for all homepage links
- Compressed hero / screenshot / OG images to progressive JPEG (~650 KB total)

---

## [2.0.0] - 2026-11-16

### Changed
- Rebranded the site from PetReminder to **Reminder** for the app's 2.0.0 release
- Rewrote all homepage and guide copy around the 2.0.0 native Rust + GPUI rebuild
- Replaced the hero with the new App Store artwork (Slice 3) and added two
  full-width screenshots (settings and pet store)
- Reworked the homepage into a centered hero + full-width artwork layout with
  features, screenshots, pets & pricing, steps, FAQ and CTA sections
- Updated pet catalog and pricing to match the runtime store catalog:
  British Shorthair free; Corgi, Husky, Ragdoll Cat and Shiba Inu $3.99;
  All Pets Pack $19.99 (removed the outdated Tugou, Cats Bundle and CNY prices)

### Added
- Full multilingual support: 7 locales (en, zh-CN, zh-TW, ja, de, es, fr),
  matching clipboard-site
- Per-locale nav, sidebar, footer, search chrome and markdown containers
- Language switcher (desktop dropdown + mobile panel) and appearance toggle
  in the shared `SiteNav.vue`
- Localized guide, FAQ and legal pages for all 7 languages
- Dark-mode-aware design tokens for every homepage section
- `versionBadge` on the hero, OG preview from the new artwork

### Technical
- `theme/index.ts` Layout is now a stateful `defineComponent` so localized
  frontmatter re-renders correctly on client-side navigation
- Replaced hard-coded homepage copy with frontmatter-driven content
- Added `localeLink()` locale prefixing for all homepage links
- Compressed hero / screenshot / OG images to progressive JPEG (~650 KB total)

---

## [1.0.0] - 2026-06-14

### Added
- Initial release of PetReminder official website
- Complete VitePress setup with TypeScript configuration
- Comprehensive user guides:
  - Introduction to PetReminder
  - Installation instructions for macOS
  - Usage guide with keyboard shortcuts
  - Premium Pets & IAP guide
  - macOS Permissions guide
  - Pet Customization guide
  - Troubleshooting section
  - Frequently Asked Questions
- Privacy Policy, Privacy Choices, and Terms of Service
- Automatic deployment to GitHub Pages
- IAP pet file distribution via `pets/` directory
- Local search functionality
- Social links and footer
- Mac App Store download links

### Technical Details
- Built with VitePress 1.6.4
- Uses pnpm for package management
- Responsive design with modern UI
- SEO optimized with proper meta descriptions

---

## Contributing to the Changelog

When making changes to the documentation:

- Add entries to the "Unreleased" section above
- Use the following types: `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`
- Keep descriptions clear and concise
- Reference issue numbers when applicable

## Release Process

1. Update version in `package.json`
2. Move items from "Unreleased" to a new version section
3. Commit with message "Release vX.X.X"
4. Push to trigger deployment