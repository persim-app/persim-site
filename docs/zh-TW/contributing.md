# 參與貢獻

感謝你協助改善 Reminder 文件。無論是勘誤、翻譯或新指南，我們都非常歡迎。

## 貢獻方式

- 修正錯字、失效連結或過時的用語
- 讓難以理解的步驟更清楚
- 將頁面翻譯成其他語言
- 為尚未涵蓋的工作流程新增指南

## 文件開發

本站使用 [VitePress](https://vitepress.dev/) 建置。

```bash
pnpm install
pnpm docs:dev      # local preview at http://localhost:5173
pnpm docs:build    # output in docs/.vitepress/dist
```

首頁內容放在各語言的 `index.md` frontmatter 中。導覽列、側邊欄與頁尾標籤則位於 `docs/.vitepress/config.ts`。指南頁面使用相對連結，以便在所有語言前綴下都能正常運作。

## 寫作風格

- 語氣保持沉穩、務實 —— App 的調性是安靜，而非促銷
- 偏好短句與具體步驟
- 價格與產品名稱請與 [寵物與 App 內購買項目](guide/pets.md) 所列完全一致
- 指南頁面內請使用相對連結

## 回報 App 問題

若是應用程式本身的問題（非文件），請到 [專案儲存庫](https://github.com/petreminder/reminder) 開啟 issue，並附上你的 macOS 版本、Reminder 版本、重現步驟與相關紀錄檔。
