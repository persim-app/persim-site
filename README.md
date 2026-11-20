# Reminder Website

Official website for **Reminder** — a calm, local-first macOS reminder app with a
desktop pet companion that grows with your streak. Current app release: **2.0.0**.

Live at https://reminder.w3cub.com

## Highlights

- VitePress site with a fully data-driven custom homepage
- **7 languages**: English, 简体中文, 繁體中文, 日本語, Deutsch, Español, Français
- Light / dark appearance switch and language switcher in the shared navigation
- Localized nav, sidebar, footer, homepage and every guide / legal page
- Hero and screenshots from the 2.0.0 App Store artwork
- Pet store pricing kept in sync with the app's `output/store/iap-products.json`
  (British Shorthair free, four pets at $3.99, All Pets Pack $19.99)

## Where content lives

| Path | Purpose |
|---|---|
| `docs/index.md`, `docs/<lang>/index.md` | Homepage content (YAML frontmatter) |
| `docs/.vitepress/config.ts` | Locales, nav / sidebar / footer strings, SEO |
| `docs/.vitepress/theme/` | `AdvancedHome.vue`, `SiteNav.vue`, `SiteFooter.vue`, `HomeActions.vue`, `locale.ts`, `custom.css` |
| `docs/guide/`, `docs/<lang>/guide/` | Guides and legal pages (relative links) |
| `docs/public/` | Logo, pet images, hero, screenshots, OG preview |

> Homepage internal links are written as root paths (`/guide/...`) and get their
> locale prefix from `localeLink()` in the component. Guide pages use relative
> links so they resolve under any language prefix without edits.

## Development

```bash
pnpm install
pnpm docs:dev      # http://localhost:5173
pnpm docs:build    # docs/.vitepress/dist
pnpm docs:preview
```

## Deployment

`deploy.sh` builds the site and publishes `docs/.vitepress/dist` to GitHub Pages;
the `.github/workflows/deploy.yml` workflow does the same on push and writes the
`CNAME` for `reminder.w3cub.com`.

## Updating prices or pets

Edit the `pets` / `bundle` arrays in every `docs/<lang>/index.md` and the table in
every `docs/<lang>/guide/pets.md`. Keep USD amounts identical across languages —
StoreKit converts them to the buyer's local currency.

## License

Documentation is distributed under the repository LICENSE.
