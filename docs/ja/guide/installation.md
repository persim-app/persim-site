# インストール

Reminder は Mac App Store から macOS 向けに提供されています。現在のリリースはバージョン 2.0.0 です。

## ダウンロード

- **[Mac App Store の Reminder](https://apps.apple.com/app/id6776577400)**（推奨 — 自動アップデート、サンドボックスビルド）
- **[GitHub Releases](https://github.com/petreminder/reminder/releases)** — 自動アップデートなしの `.dmg` 直接ビルド

## Mac App Store からインストールする

1. 上記の App Store リンクを開くか、「Reminder」で検索します
2. **入手** をクリックし、続けて **インストール** をクリックします
3. Applications または Launchpad から Reminder を起動します

## GitHub Releases からインストールする

1. 最新の `.dmg` をダウンロードします
2. ダブルクリックしてマウントします
3. `Reminder.app` を `Applications` にドラッグします
4. ディスクイメージを取り出して Reminder を開きます

macOS がアプリをブロックする場合は、**システム設定 → プライバシーとセキュリティ** を開いて **このまま開く** をクリックするか、アプリを右クリックして **開く** を選択してください。

## 初回起動

macOS から求められたら **通知** を許可してください。これがリマインダーを届ける仕組みです。他に必要なものはありません。アカウントも、ログインも、デモ用の認証情報もありません。British Shorthair の仲間は初回起動からインストール済みで、すぐに使えます。

## アップデート

- **Mac App Store**: アップデートは自動的にインストールされます
- **GitHub Releases**: 新しいビルドをダウンロードし、`Applications` 内のアプリを置き換えます

リマインダーとペットはアプリバンドルの外に保存されるため、アップデートで削除されることはありません。

## アンインストール

1. Reminder を終了します（トレイメニューまたは `Cmd+Q`）
2. `Reminder.app` をゴミ箱に移動します
3. 必要に応じてローカルデータを削除します:

```bash
rm -rf ~/Library/Containers/com.w3cub.reminder
```

## トラブルシューティング

インストールに失敗した場合は、[トラブルシューティング](./troubleshooting.md) をご覧になるか、[reminder@w3cub.com](mailto:reminder@w3cub.com) までメールでお問い合わせください。
