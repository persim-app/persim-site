# 故障排查

## 提醒始终没有送达

1. 打开 **系统设置 → 通知 → Reminder**，确认已允许提醒
2. 检查托盘菜单中是否暂停了提醒
3. 确认在预定时间 Mac 处于唤醒状态
4. 退出并重新打开 Reminder

如果首次启动时关闭了授权提示，通知可能会被永久禁用，直到你在「系统设置」中重新开启。

## 宠物没有出现

- 确认托盘菜单中宠物处于显示状态（显示/隐藏宠物）
- 检查 **设置 → 宠物** 中是否已选择伙伴
- 确认宠物包已下载完成；重新打开宠物商店并尝试 **恢复购买**
- 若使用外接显示器或全屏应用，可从托盘菜单把宠物移回主屏幕

## 购买后未解锁

1. 打开宠物商店并点按 **恢复购买**
2. 确认已使用同一 Apple ID 登录 Mac App Store
3. 检查网络连接后重试
4. 若仍失败，请附上产品名称联系 [reminder@w3cub.com](mailto:reminder@w3cub.com)

## 宠物包下载失败

应用会用 SHA-256 校验每个宠物包，并对失败的下载重试一次。若持续失败，通常是网络不稳定 — 请换用稳定的网络再试。

## 应用无法打开

1. 重启 Mac
2. 从 Mac App Store 重新安装（本地数据保存在应用包之外）
3. 若 Gatekeeper 阻止了 GitHub 构建，请使用 **系统设置 → 隐私与安全性 → 仍要打开**

## 日志与数据在哪里？

沙盒版本将数据存放在：

```
~/Library/Containers/com.w3cub.reminder/Data/Library/Application Support/com.w3cub.reminder/
```

使用 **设置 → 通用 → 日志文件夹** 可直接打开。

## 仍未解决？

请在 [项目仓库](https://github.com/petreminder/reminder) 提交 issue，附上你的 macOS 版本、Reminder 版本、复现步骤与日志，或发邮件至 [reminder@w3cub.com](mailto:reminder@w3cub.com)。
