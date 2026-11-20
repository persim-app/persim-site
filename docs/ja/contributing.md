# コントリビューション

Reminder のドキュメント改善にご協力いただき、ありがとうございます。誤字の修正、翻訳、新しいガイドは、いずれも歓迎します。

## 貢献の方法

- 誤字、リンク切れ、古くなった表現の修正
- 分かりにくい手順の説明を明確にする
- ページを他の言語に翻訳する
- まだ取り上げていないワークフローのガイドを追加する

## ドキュメントの作業について

このサイトは [VitePress](https://vitepress.dev/) で構築されています。

```bash
pnpm install
pnpm docs:dev      # local preview at http://localhost:5173
pnpm docs:build    # output in docs/.vitepress/dist
```

ホームページの内容は、各言語の `index.md` の frontmatter にあります。ナビゲーション、サイドバー、フッターのラベルは `docs/.vitepress/config.ts` にあります。ガイドページは相対リンクを使用しているため、どの言語プレフィックスの下でも機能します。

## 文体

- 静かで実用的なトーンを保つ — アプリのトーンは控えめで、宣伝調ではありません
- 短い文と具体的な手順を優先する
- 価格と製品名は [ペットとアプリ内課金](guide/pets.md) の記載どおりに保つ
- ガイドページ内では相対リンクを使う

## アプリの不具合を報告する

アプリ本体の不具合（ドキュメント以外）については、[プロジェクトのリポジトリ](https://github.com/petreminder/reminder) で Issue を作成し、macOS のバージョン、Reminder のバージョン、再現手順、関連するログを添えてください。
