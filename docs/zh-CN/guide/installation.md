# 安装

Reminder 通过 Mac App Store 面向 macOS 提供。当前版本为 2.0.0。

## 下载

- **[Mac App Store 上的 Reminder](https://apps.apple.com/app/id6776577400)**（推荐 — 自动更新、沙盒构建）
- **[GitHub Releases](https://github.com/petreminder/reminder/releases)** — 直接提供 `.dmg` 构建，不含自动更新

## 从 Mac App Store 安装

1. 打开上方的 App Store 链接，或搜索 "Reminder"
2. 点击 **获取**，再点击 **安装**
3. 从「应用程序」或「启动台」启动 Reminder

## 从 GitHub Releases 安装

1. 下载最新的 `.dmg`
2. 双击挂载
3. 将 `Reminder.app` 拖入 `Applications`
4. 推出磁盘映像并打开 Reminder

如果 macOS 阻止打开应用，请前往 **系统设置 → 隐私与安全性**，点击 **仍要打开**；或右键点击应用并选择 **打开**。

## 首次启动

当 macOS 询问时，请允许 **通知**——提醒正是通过它送达的。除此之外无需其他操作：没有账户、没有登录，也没有演示凭据。你的英国短毛猫伙伴从首次启动起就已装好、随时可用。

## 更新

- **Mac App Store**：自动安装更新
- **GitHub Releases**：下载新构建，替换 `Applications` 中的应用

提醒与宠物数据存放在应用包之外，因此更新不会将其删除。

## 卸载

1. 退出 Reminder（从托盘菜单，或按 `Cmd+Q`）
2. 将 `Reminder.app` 移到废纸篓
3. 可选：删除本地数据

```bash
rm -rf ~/Library/Containers/com.w3cub.reminder
```

## 故障排查

如果安装失败，请参阅 [故障排查](./troubleshooting.md)，或发邮件至 [reminder@w3cub.com](mailto:reminder@w3cub.com)。
