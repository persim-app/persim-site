# 参与贡献

感谢你帮助改进 Reminder 文档。无论是纠错、翻译还是新增指南，我们都欢迎。

## 贡献方式

- 修正错别字、失效链接或过时的表述
- 把难以理解的步骤说明白
- 将某个页面翻译成其他语言
- 为我们尚未涵盖的用法补充一篇指南

## 参与文档开发

本站使用 [VitePress](https://vitepress.dev/) 构建。

```bash
pnpm install
pnpm docs:dev      # local preview at http://localhost:5173
pnpm docs:build    # output in docs/.vitepress/dist
```

首页内容存放在各语言 `index.md` 的 frontmatter 中。导航、侧边栏与页脚文案位于 `docs/.vitepress/config.ts`。指南页面使用相对链接，以便在任何语言前缀下都能正常工作。

## 写作风格

- 保持平和、务实的语气——应用的调性是安静克制，而非宣传推销
- 多用短句和具体步骤
- 价格与产品名称请与 [宠物与内购](guide/pets.md) 中列出的完全一致
- 指南页面内部使用相对链接

## 反馈应用问题

若是应用本身的缺陷（而非文档问题），请在 [项目仓库](https://github.com/petreminder/reminder) 中提交 issue，并附上你的 macOS 版本、Reminder 版本、复现步骤以及相关日志。
