# 疑難排解

## 提醒事項遲遲沒出現

1. 開啟**系統設定 → 通知 → Reminder**，確認已允許提示
2. 檢查選單列選單中是否暫停了提醒
3. 確認 Mac 在排定時間處於喚醒狀態
4. 結束並重新開啟 Reminder

若首次啟動的詢問曾被略過，通知可能會一直維持停用，直到你到「系統設定」重新啟用為止。

## 寵物沒有出現

- 確認選單列選單中寵物為顯示狀態（顯示／隱藏寵物）
- 檢查**設定 → 寵物**中是否已選取夥伴
- 確認寵物包已完成下載；重新開啟寵物商店並試試**回復購買項目**
- 若使用外接螢幕或全螢幕 App，請從選單列選單把寵物移回主螢幕

## 購買後沒有解鎖

1. 開啟寵物商店並點擊**回復購買項目**
2. 確認已使用相同的 Apple ID 登入 Mac App Store
3. 檢查網路連線後再試一次
4. 若仍失敗，請附上產品名稱寄信到 [reminder@w3cub.com](mailto:reminder@w3cub.com)

## 寵物包下載失敗

App 會以 SHA-256 校驗碼驗證每個寵物包，並在下載失敗時自動重試一次。若持續失敗，通常是網路不穩 —— 請改用穩定的連線再試。

## App 無法開啟

1. 重新啟動 Mac
2. 從 Mac App Store 重新安裝（本機資料保存在 App 安裝包之外）
3. 若 Gatekeeper 封鎖了 GitHub 版本，請使用**系統設定 → 隱私權與安全性 → 強制開啟**

## 我的紀錄檔與資料在哪裡？

採沙盒的版本會將資料存放在：

```
~/Library/Containers/com.w3cub.reminder/Data/Library/Application Support/com.w3cub.reminder/
```

使用**設定 → 一般 → 紀錄檔資料夾**即可直接開啟。

## 還是卡住了？

請到 [專案儲存庫](https://github.com/petreminder/reminder) 開啟 issue，附上你的 macOS 版本、Reminder 版本、重現步驟與紀錄檔，或寄信到 [reminder@w3cub.com](mailto:reminder@w3cub.com)。
