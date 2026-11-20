# Contributing to Persim Documentation

欢迎改进 Persim 官网内容。

## 可以做什么

- 报告文案错误、失效链接或描述与实际功能不符的地方
- 改进指南的可读性，补充面向普通用户的操作步骤
- 帮忙校对某一种语言的译文

联系方式：`persim@w3cub.com`

## 写作约定

- 面向普通用户：不写实现细节（框架、引擎、库名），只描述「能做什么、怎么用」
- 首页文案写在 `docs/<lang>/index.md` 的 frontmatter；指南页正文用 Markdown
- 商店链接与邮箱只改 `docs/.vitepress/theme/site.ts`
- 新增语言需同时更新 `config.ts` 与 `theme/locale.ts`
- 提交前运行 `pnpm docs:build` 确认能正常构建
