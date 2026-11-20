# 權限

Reminder 只會向 macOS 要求極少數權限。沒有帳號、沒有分析，也沒有背景雲端同步。

## 通知

**必要。** 提醒事項是透過 macOS 原生通知送達，因此即使 App 不在前景也能準時出現。macOS 會在你第一次排定提醒時詢問；請到**系統設定 → 通知 → Reminder** 允許。

## 檔案與資料夾

採沙盒的 Mac App Store 版本會把提醒事項、設定、紀錄檔與下載的寵物包存放在它自己的容器內：

```
~/Library/Containers/com.w3cub.reminder/Data/Library/Application Support/com.w3cub.reminder/
```

匯入 `.catpet` 寵物包時會使用 macOS 標準的檔案選擇器 —— App 只會讀取你自己選取的檔案。

## 輔助使用／螢幕錄製

**不需要。** 浮動寵物視窗由 App 自己繪製；Reminder 不會擷取你的螢幕，也不會讀取其他 App 的內容。

## 網路

對外連線僅限於：

- 寵物商店目錄與寵物包下載（`app-sources.w3cub.com`）
- Apple 的 StoreKit 服務，用於購買與回復
- 你選擇從 App 內送出的選用意見回饋

## 管理權限

開啟**系統設定 → 隱私權與安全性**即可檢視或撤銷任何權限。變更權限後，請結束並重新開啟 Reminder。若通知詢問曾被略過，請參閱[疑難排解](./troubleshooting.md)。
