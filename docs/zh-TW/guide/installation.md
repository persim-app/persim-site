# 安裝

Reminder 可透過 Mac App Store 在 macOS 上取得。目前版本為 2.0.0。

## 下載

- **[Mac App Store 上的 Reminder](https://apps.apple.com/app/id6776577400)**（建議 —— 自動更新、沙盒版本）
- **[GitHub Releases](https://github.com/petreminder/reminder/releases)** —— 直接提供 `.dmg` 安裝檔，但不含自動更新

## 從 Mac App Store 安裝

1. 開啟上方的 App Store 連結，或搜尋「Reminder」
2. 點擊**取得**，接著點擊**安裝**
3. 從 `Applications` 或 Launchpad 啟動 Reminder

## 從 GitHub Releases 安裝

1. 下載最新的 `.dmg`
2. 雙擊以掛載
3. 將 `Reminder.app` 拖入 `Applications`
4. 退出映像檔並開啟 Reminder

若 macOS 封鎖了 App，請開啟**系統設定 → 隱私權與安全性**並點擊**強制開啟**，或在 App 上按右鍵選擇**開啟**。

## 首次啟動

當 macOS 詢問時，請允許**通知** —— 提醒事項就是透過它送達。除此之外不需要任何設定：沒有帳號、不用登入、也沒有試用憑證。你的 British Shorthair 夥伴在首次啟動時就已安裝並準備就緒。

## 更新

- **Mac App Store**：更新會自動安裝
- **GitHub Releases**：下載新版本，並取代 `Applications` 中的 App

你的提醒事項與寵物存放在 App 安裝包之外，因此更新永遠不會移除它們。

## 解除安裝

1. 結束 Reminder（從選單列選單或 `Cmd+Q`）
2. 將 `Reminder.app` 移至「廢紙簍」
3. 視需要移除本機資料：

```bash
rm -rf ~/Library/Containers/com.w3cub.reminder
```

## 疑難排解

若安裝失敗，請參閱[疑難排解](./troubleshooting.md)，或寄信到 [reminder@w3cub.com](mailto:reminder@w3cub.com)。
