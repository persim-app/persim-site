# 权限

Reminder 只申请极少量 macOS 权限。没有账户、没有分析统计，也没有后台云同步。

## 通知

**必需。** 提醒通过 macOS 原生通知送达，因此即使应用不在前台也能准时到达。首次安排提醒时 macOS 会弹出授权提示；请在 **系统设置 → 通知 → Reminder** 中允许。

## 文件与文件夹

采用沙盒的 Mac App Store 版本会把提醒、设置、日志与已下载的宠物包存放在自己的容器内：

```
~/Library/Containers/com.w3cub.reminder/Data/Library/Application Support/com.w3cub.reminder/
```

导入 `.catpet` 宠物包会使用 macOS 标准文件选择器 — 应用只读取你亲自选择的文件。

## 辅助功能 / 屏幕录制

**无需授权。** 悬浮宠物窗口由应用自身绘制；Reminder 不会截取你的屏幕，也不会读取其他应用的内容。

## 网络

对外请求仅限于：

- 宠物商店目录与宠物包下载（`app-sources.w3cub.com`）
- 用于购买与恢复的 Apple StoreKit 服务
- 你主动从应用内发送的可选反馈

## 管理权限

打开 **系统设置 → 隐私与安全性** 即可查看或撤销各项权限。更改权限后，请退出并重新打开 Reminder。若之前关闭了通知授权提示，请参阅 [故障排查](./troubleshooting.md)。
