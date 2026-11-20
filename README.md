# Persim Website

官网：[https://persim.w3cub.com](https://persim.w3cub.com)

Persim 柿子浏览器是一款清爽、快速的 Mac 浏览器。本站用 VitePress 构建，
提供 **7 种语言**（English、简体中文、繁體中文、日本語、Deutsch、Español、Français）
与浅色 / 深色主题；应用本身支持 25 种界面语言。

## 内容在哪里

| 路径 | 用途 |
|---|---|
| `docs/index.md`、`docs/<lang>/index.md` | 首页全部文案（frontmatter 驱动） |
| `docs/.vitepress/config.ts` | 语言、导航、侧栏、页脚、SEO |
| `docs/.vitepress/theme/site.ts` | **产品链接与邮箱的唯一来源**（商店链接先改这里） |
| `docs/.vitepress/theme/` | `AdvancedHome.vue`、`SiteNav.vue`、`SiteFooter.vue`、`HomeActions.vue`、`custom.css` |
| `docs/guide/`、`docs/<lang>/guide/` | 指南页（使用相对链接，天然跟随语言前缀） |
| `docs/public/` | Logo、两张浏览器截图、图标、OG 预览图 |

首页内部链接写根路径（如 `/guide/faq`），由 `localeLink()` 自动加语言前缀；
指南页之间用相对链接，无需逐语言修改。

主色：浏览器默认蓝色 `#3b82f6`。首页「选一种主色调」的色块会实时改写
`--vp-c-brand-1`，与设置页里的六个色点顺序一致。

## 开发

```bash
pnpm install
pnpm docs:dev      # http://localhost:5173
pnpm docs:build    # 产物在 docs/.vitepress/dist
pnpm docs:preview
```

## 部署

`pnpm docs:deploy` 或 GitHub Actions（推送 `main`）会构建并发布到 `gh-pages`，
CNAME 为 `persim.w3cub.com`。

## 许可

文档遵循仓库 LICENSE。
