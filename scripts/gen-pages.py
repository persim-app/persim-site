#!/usr/bin/env python3
"""Generate the localized homepage + guide pages for the Persim website.

All copy is written for everyday users: what the browser does for them, not how
it is built. Edit the strings below and re-run `python3 scripts/gen-pages.py`.
"""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1] / "docs"
STORE = "https://apps.apple.com/app/id6835099132"


def F(icon, title, details):
    return {"icon": f"/icons/{icon}.svg", "iconAlt": "", "title": title, "details": details}


def G(title, summary, body):
    return {"title": title, "summary": summary, "body": body.strip()}


DATA = {
    "en": {
        "versionBadge": "For Mac · Free to download",
        "hero": {
            "name": "Persim",
            "text": "A browser that feels light",
            "tagline": "Tabs, ad blocking, video saving, reading mode and AI shortcuts — everything you use every day, in one quiet place.",
            "image": {"src": "/screenshot-newtab.png", "alt": "Persim new tab page"},
        },
        "actions": [
            {"text": "Download for free", "link": STORE, "theme": "brand", "external": True},
            {"text": "See the features", "link": "/#features", "theme": "alt"},
        ],
        "downloadNote": "macOS 12 or later · Apple Silicon and Intel",
        "features": [
            F("tabs", "Tabs that keep up", "Open, drag and group tabs the way you already do. Press ⌘⇧A to find one in a flash."),
            F("shield", "Fewer ads, cleaner pages", "Built-in ad blocking with subscriptions, your own rules and a whitelist. Mute a tab or block pop-ups in one click."),
            F("download", "Keep the videos you like", "Spot a video on a page and save it from the download panel. Split videos are joined into a single MP4; downloads can pause and resume."),
            F("ai", "Ask AI without detours", "Type “ai + your question” in the address bar to reach your favourite AI sites. ChatGPT, Claude and more are one click away on the new tab page."),
            F("book", "A calmer way to read", "Reading mode strips away menus and ads and leaves the article. Force dark pages, take a full-page capture or print cleanly."),
            F("palette", "Make it yours", "Light, dark or system theme; six accent colours; three bookmark-bar modes; 25 interface languages."),
        ],
        "sections": {
            "featuresTitle": "Just the right amount of browser",
            "featuresSubtitle": "No setup wizard. Open Persim, search, browse, save — that's it.",
            "shotsTitle": "A quick look",
            "shotsSubtitle": "The new tab page puts your sites up front. Settings keep the theme, accent colour and language together.",
            "accentTitle": "Pick your accent colour",
            "accentSubtitle": "Switch from the colour button in the top bar, or here — the whole site follows your choice.",
            "howTitle": "Three steps to a cleaner browser",
            "howSubtitle": "From download to daily use takes only a few minutes.",
            "faqTitle": "Common questions",
            "faqSubtitle": "About downloading, privacy and everyday use",
        },
        "banners": [{"title": "Tabs that keep up", "alt": "Persim new tab page banner"}, {"title": "Make it yours", "alt": "Persim settings banner"}, {"title": "Supercharge your browser", "alt": "Persim userscripts banner"}],
        "accentLabels": ["Persimmon", "Violet", "Teal", "Green", "Blue", "Rose"],
        "steps": [
            {"num": "01", "title": "Install it", "desc": "Download from the Mac App Store and drag the app into Applications. No account needed."},
            {"num": "02", "title": "Bring your bookmarks", "desc": "Export bookmarks as an HTML file from Chrome or Edge, then import it in Persim's bookmark manager."},
            {"num": "03", "title": "Set it up your way", "desc": "Choose a theme, accent colour and language in Settings. Turn on “Restore last session” to pick up where you left off."},
        ],
        "faqs": [
            {"question": "Is Persim free?", "answer": "You can download and use the core browsing features for free from the Mac App Store. Some advanced features are available through an in-app purchase; the free version shows a small badge in the tab bar."},
            {"question": "Which Macs does it support?", "answer": "macOS 12 or later, on both Apple Silicon and Intel Macs."},
            {"question": "Is my browsing history uploaded?", "answer": "No. History, bookmarks, sessions and downloads stay on your Mac, and there is no account. Only features that need the network — such as refreshing ad-blocking subscriptions — connect to the internet."},
            {"question": "How do I import Chrome bookmarks?", "answer": "Export bookmarks to an HTML file in Chrome, then open Persim's bookmark manager and choose “Import HTML”."},
            {"question": "How do I save a video from a page?", "answer": "Open the media panel, pick a detected video and download it. Split videos are joined into one MP4. Regular downloads can be paused, resumed and retried."},
        ],
        "faqMore": "More questions →",
        "cta": {
            "title": "Give browsing a little breathing room.",
            "description": "Download Persim and set it up exactly the way you like.",
            "primary": "Download on the Mac App Store",
            "primaryLink": STORE,
            "secondary": "Read the guide",
            "secondaryLink": "/guide/introduction",
        },
        "guides": {
            "introduction": G("What is Persim", "A browser for Mac that is ready the moment you open it.", """
## From the first click

- **Browse and search.** Type an address or a question in the address bar. Places you visit often come up first.
- **Tabs and windows.** Open, drag, group, mute and preview tabs. Press ⌘⇧A to find a tab quickly.
- **Find things again.** Bookmarks, the bookmark bar, history, downloads and “Restore last session”.

## A little quieter

- Ad blocking with subscriptions, custom rules and a whitelist for sites you trust.
- Force dark pages, mute a tab and block pop-ups from Settings.
- A private window (⌘⇧N) doesn't write browsing history.

## Videos and long reads

- The media panel lists videos found on a page; saving one produces a single MP4 you can open with any app you like.
- Reading mode (⌘⇧R) keeps the article and drops the clutter. Capture what you see or the whole page as a PDF.

## Made to fit you

Light, dark or system appearance; six accent colours; three bookmark-bar modes; 25 interface languages. Appearance changes show up right away — a language change takes effect after you reopen the window.
"""),
            "installation": G("Install Persim", "Download, set as default and bring your bookmarks along.", """
## Download and install

1. Open the [Mac App Store](""" + STORE + """) and find Persim.
2. After downloading, drag the app into your Applications folder. If macOS asks for confirmation, approve it.
3. To make it your default browser, open **System Settings → Default Web Browser** and choose Persim.

Requires macOS 12 or later, on Apple Silicon and Intel Macs.

## Your first minute

- In `persim://settings` → **General**, choose the appearance, accent colour and bookmark bar.
- 25 interface languages are available; a language change takes effect after you reopen the window.
- The new tab page already has popular sites and AI shortcuts — start using them right away.

## Bring your bookmarks

1. Export bookmarks as an HTML file in Chrome or Edge.
2. Open Persim's bookmark manager and choose **Import HTML**.
3. Nested folders are restored and duplicate addresses are skipped. You can reorder the bookmark bar anytime.

## Updates

Get new versions from the **Updates** tab in the Mac App Store. Your data stays where it is.
"""),
            "features": G("Feature tour", "A short guide to the things you'll use most.", """
## Everyday browsing

- Multiple tabs and windows: drag them out, group them, fold a group away, mute a tab or hover to preview.
- The address bar suggests sites you know first, then falls back to search.
- Command palette (⌘K), tab search (⌘⇧A), find on page (⌘F) and a keyboard shortcut list in the gear menu.

## Easy on the eyes

- Appearance: follow system, light or dark. You can also force dark pages and switch themes automatically each day.
- Six accent colours: blue, violet, teal, green, orange and rose.
- Bookmark bar: always hidden, always visible, or only on the new tab page.

## Ads and scripts

- Ad blocking supports subscriptions, your own rules and a whitelist. If a subscription fails to update, the old rules keep working.
- User scripts (`.user.js`) are managed in Settings and install as soon as the download finishes.

## Videos and files

- Downloads can pause, resume, cancel and retry. When a download finishes you can reveal it in Finder or open it with the related app.
- The media panel detects videos on a page and saves them as one MP4, even when the site serves them in pieces.

## Shortcuts at a glance

| Shortcut | What it does |
| --- | --- |
| ⌘T / ⌘W | New / close tab |
| ⌘L | Focus the address bar |
| ⌘F | Find on the page |
| ⌘⇧N | Private window |
| ⌘K | Command palette |
| ⌘⇧A | Search tabs |
| ⌘⇧R | Reading mode |
"""),
            "faq": G("FAQ", "Quick answers about Persim.", """
### Is Persim free?

You can download and use the core browsing features for free. Some advanced capabilities are unlocked with an in-app purchase, and the free version shows a small badge in the tab bar.

### Which operating systems are supported?

Persim is built for macOS 12 or later and runs on Apple Silicon and Intel Macs.

### Will my data be uploaded?

No account is required, and history, bookmarks, sessions and downloads stay on your Mac. Features that need the network — such as updating an ad-blocking subscription — fetch only what they need. You can remove site data from the cookie manager.

### How do I import bookmarks from another browser?

Export your bookmarks to an HTML file from Chrome or Edge, then use **Import HTML** in Persim's bookmark manager. Folders and duplicate links are handled for you.

### How do I save a video I found online?

Open the media panel, choose one of the detected videos and download it. Videos served in several pieces are joined into one MP4, and finished files can be opened with your usual apps.

### How do I change the interface language?

Open `persim://settings` → **General** → **Language**. The app offers 25 languages; reopen the window to see the change.

### Still have a question?

Write to **persim@w3cub.com** and tell us what you were trying to do.
"""),
            "privacy": G("Privacy and your data", "What stays on your Mac, and what needs the network.", """
## Stored on your Mac

Your history, bookmarks, open tabs, downloads and cookies are saved locally. There is no account and no cloud sync. A private window (⌘⇧N) doesn't add to your history or session.

## When the network is used

- Loading the websites you visit, of course.
- Refreshing an ad-blocking subscription, when one is enabled. If the update fails, the saved rules keep working.
- Downloading a user script or a file you asked for.

## Your permissions

Camera and microphone access is remembered per site, so you can allow one site and refuse another. Location and notifications are controlled by macOS itself. Pop-ups are limited to sites you allow.

## Files on disk

Persim only reads files you choose in the system file dialog or explicitly grant access to. You can review and revoke those grants in Settings.

## Contact

Questions about privacy: **persim@w3cub.com**.
"""),

            "troubleshooting": G("Troubleshooting", "Fixes for the problems you might run into.", """
## A page won't load

- Check that other sites open, then try reloading with ⌘R.
- If you enabled an ad-blocking rule list, pause it for a moment to see whether it is blocking this site.
- Try a private window (⌘⇧N). If the page works there, clear the site's cookies from the cookie manager.

## A download is stuck or incomplete

- Open the download panel and pause, then resume the item.
- For videos saved from a page, delete the partial file and try again. Split videos are joined into one MP4; a failed join leaves the original pieces in the download folder.

## Bookmarks did not import

Export bookmarks to an HTML file from your old browser first, then in Persim open the bookmark manager and choose **Import HTML**. Folders and duplicate links are handled for you.

## Videos are not detected

Not every site exposes a video file. Open the media panel on the page you want; if nothing appears, the site may be streaming in a way that can't be saved directly.

## The app feels slow

Close tabs you are not using, or disable an ad-blocking subscription you no longer need. You can review site permissions in Settings.

## Still stuck?

Write to **persim@w3cub.com** with what you were doing and, if you can, a screenshot.
"""),
            "legal": G("Legal", "Legal information for Persim.", """
Persim is developed and published by w3cub.com.

- [Privacy Policy](./privacy-policy) — what data is handled and how.
- [Privacy Choices](./privacy-choices) — how to control what is stored and shared.
- [Terms of Service](./terms) — the terms for using the app.

Questions about these documents: **persim@w3cub.com**.
"""),
            "privacy-policy": G("Privacy Policy", "What Persim collects and what stays on your device.", """
## No account, no cloud profile

Persim does not ask you to sign in and does not create an online account for you. Your history, bookmarks, open tabs, downloads and cookies are saved on your Mac.

## Information used to show pages

Like any browser, Persim sends the addresses you visit to the websites you open. Persim itself does not upload your browsing history to a server.

## Network features you can turn on

- Ad-blocking subscriptions refresh their rule lists over the network. If an update fails, the saved list keeps working.
- User scripts and files you download are fetched only when you ask for them.
- Search suggestions come from your chosen search engine when you type in the address bar.

## Local permissions

Camera, microphone and file access are remembered per site and can be changed in Settings. Location and notifications are controlled by macOS. A private window (⌘⇧N) does not add to your history or session.

## Third-party sites

Pages you visit are operated by others and follow their own privacy practices. Persim's built-in pages do not track you.

## Contact

Privacy questions: **persim@w3cub.com**.
"""),
            "privacy-choices": G("Privacy Choices", "Simple ways to stay in control.", """
## Browse without a record

Use a private window (⌘⇧N). It does not add to your history or remember your session, and its tabs disappear when you close it.

## Clear what is stored

Remove cookies and site data from the cookie manager in Settings. You can clear browsing history and downloads from the same area.

## Decide what each site can do

Camera, microphone and file access are remembered per site. Allow a site you trust and refuse others in Settings. Pop-ups are limited to sites you allow.

## Control background features

Turn ad-blocking subscriptions on or off in Settings. When one is off, no rule list is fetched.

## Choose your search engine

Pick your default search engine in Settings. Search suggestions come from the engine you choose.

## Questions

Write to **persim@w3cub.com** if you want to know more about how your data is handled.
"""),
            "terms": G("Terms of Service", "The terms for using Persim.", """
## Using the app

Persim is provided for personal use. You may download and use it on Macs you own or are allowed to use.

## Free and paid features

Core browsing features are available for free. Some advanced capabilities are unlocked with an in-app purchase. The free version shows a small badge in the tab bar; removing it requires the in-app purchase.

## Third-party content

Websites, subscriptions and user scripts you use through Persim are provided by their own authors. Persim is not responsible for their content or availability.

## Changes

Features and these terms may change over time. The version published on this website is the current one.

## Contact

Questions about these terms: **persim@w3cub.com**.
"""),
        },
    },
    "zh-CN": {
        "versionBadge": "为 Mac 打造 · 免费下载",
        "hero": {
            "name": "Persim 柿子浏览器",
            "text": "轻快上网，清爽如初",
            "tagline": "多标签、广告拦截、视频保存、阅读模式与 AI 直达——你每天要用的，都在这里。打开就会用，不用折腾。",
            "image": {"src": "/screenshot-newtab.png", "alt": "Persim 新标签页"},
        },
        "actions": [
            {"text": "免费下载", "link": STORE, "theme": "brand", "external": True},
            {"text": "看看功能", "link": "/#features", "theme": "alt"},
        ],
        "downloadNote": "适用于 macOS 12 及以上 · 支持 Apple Silicon 与 Intel",
        "features": [
            F("tabs", "多个标签，随手切换", "新建、拖动、分组、静音、悬停预览，都按你熟悉的来。想找某个页面，按 ⌘⇧A 搜一下就行。"),
            F("shield", "广告少一点，页面净一点", "内置广告拦截，可订阅规则、自己加白名单。网页静音、弹窗拦截也在设置里一键开关。"),
            F("download", "喜欢的视频，留下来", "看到想收藏的视频，从嗅探面板一键保存；分成多段的视频会合成一个 MP4，下载还能暂停、继续和重试。"),
            F("ai", "把问题直接交给 AI", "地址栏输入「ai 今天吃什么」就能直达常用 AI 站点，ChatGPT、Claude、豆包等都在新标签页里。"),
            F("book", "长文读起来更舒服", "阅读模式去掉导航和广告，只留下正文；网页强制深色、整页截图和打印也顺手可用。"),
            F("palette", "调成你喜欢的样子", "浅色 / 深色 / 跟随系统，六种主色，书签栏三种显示方式，界面语言 25 种。"),
        ],
        "sections": {
            "featuresTitle": "每天要用的，都刚刚好",
            "featuresSubtitle": "没有复杂的设置向导。打开 Persim，搜索、浏览、保存——就是这么简单。",
            "shotsTitle": "看一眼，就知道它有多清爽",
            "shotsSubtitle": "新标签页把常用网站放在眼前；设置页把主题、主色和语言放在一起，改完立刻生效。",
            "accentTitle": "选一种主色调",
            "accentSubtitle": "点顶部导航栏的色块按钮就能换色，也可以在这里选——整站都会跟着变。",
            "howTitle": "三步，开始清爽浏览",
            "howSubtitle": "从下载到顺手，只要几分钟。",
            "faqTitle": "常见问题",
            "faqSubtitle": "关于下载、隐私和日常使用",
        },
        "banners": [{"title": "多标签，跟得上", "alt": "Persim 新标签页宣传图"}, {"title": "随你定制", "alt": "Persim 设置页宣传图"}, {"title": "效率升级", "alt": "Persim 油猴脚本宣传图"}],
        "accentLabels": ["柿子色", "紫色", "青色", "绿色", "蓝色", "玫红"],
        "steps": [
            {"num": "01", "title": "装好就打开", "desc": "从 Mac App Store 下载，拖进「应用程序」即可，不需要注册账户。"},
            {"num": "02", "title": "把常用站点带过来", "desc": "从 Chrome 或 Edge 导出书签 HTML，在 Persim 的书签管理器里一次导入，常用网站还在原来的位置。"},
            {"num": "03", "title": "按你的习惯调整", "desc": "在设置里切换主题、主色和界面语言；想恢复上次的标签，打开「恢复上次会话」。"},
        ],
        "faqs": [
            {"question": "Persim 收费吗？", "answer": "可以从 Mac App Store 免费下载，基础浏览功能可直接使用；部分高级能力通过应用内购买解锁。免费版会在标签栏显示一个小标记。"},
            {"question": "支持哪些 Mac？", "answer": "macOS 12 及以上，Apple Silicon 和 Intel 芯片都支持。"},
            {"question": "我的浏览记录会上传吗？", "answer": "不会。历史、书签、会话和下载记录都留在你的 Mac 上，也不需要账户。只有更新广告拦截订阅这类功能才会联网。"},
            {"question": "怎么把 Chrome 的书签导进来？", "answer": "在 Chrome 中把书签导出为 HTML 文件，然后打开 Persim 的书签管理器，选择「导入 HTML」。"},
            {"question": "怎么保存网页里的视频？", "answer": "打开嗅探面板，选择识别到的视频，点下载即可；分成多段的视频会合成一个 MP4。普通文件下载也能暂停、继续和重试。"},
        ],
        "faqMore": "更多问题 →",
        "cta": {
            "title": "给上网这件事，留一点清爽。",
            "description": "下载 Persim，把浏览器调成你喜欢的样子。",
            "primary": "在 Mac App Store 下载",
            "primaryLink": STORE,
            "secondary": "阅读使用指南",
            "secondaryLink": "/guide/introduction",
        },
        "guides": {
            "introduction": G("认识 Persim", "一个打开就能用的 Mac 浏览器：标签、搜索、书签、下载，都在该在的位置。", """
## 打开就会做什么

- **上网与搜索**：地址栏既能输入网址，也能直接搜索；常去的地址会优先补全。
- **多个标签与窗口**：新建、拖动、分组、静音、悬停预览，按 ⌘⇧A 快速找到某个标签。
- **收藏与找回**：书签栏、书签管理器、历史记录、下载中心，还有「恢复上次会话」。

## 想安静一点

- 广告拦截支持订阅规则、自定义规则和白名单，信任的站点可以放行。
- 网页强制深色、标签静音、弹窗拦截都在设置里一键开关。
- 无痕窗口（⌘⇧N）不会写下浏览历史。

## 看视频与读长文

- 嗅探面板列出页面里的视频，保存后就是一个完整的 MP4，用你习惯的应用打开即可。
- 阅读模式（⌘⇧R）去掉导航和广告，只留下正文；还可以截可视区或整页 PDF。

## 按你的习惯来

浅色 / 深色 / 跟随系统，六种主色，书签栏三种显示方式，界面语言 25 种。外观改完立刻生效，界面语言需要重新打开窗口。
"""),
            "installation": G("安装 Persim", "下载、设为默认浏览器，再把书签带过来。", """
## 下载与安装

1. 打开 [Mac App Store](""" + STORE + """)，搜索 Persim。
2. 下载完成后，把应用拖进「应用程序」文件夹；系统询问时确认即可。
3. 想设为默认浏览器，打开「系统设置 → 默认网页浏览器」，选择 Persim。

需要 macOS 12 及以上，Apple Silicon 和 Intel 芯片都支持。

## 第一次打开

- 在 `persim://settings` 的「常规」里选择外观、主色和书签栏显示方式。
- 界面语言有 25 种；切换后重新打开窗口生效。
- 新标签页已经放好常用网站和 AI 直达入口，直接用即可。

## 把书签带过来

1. 在 Chrome 或 Edge 里把书签导出成 HTML 文件。
2. 打开 Persim 的书签管理器，选择「导入 HTML」并选中文件。
3. 多层文件夹会还原，重复网址会自动跳过；书签栏还可以随时拖动排序。

## 后续更新

在 Mac App Store 的「更新」里获取新版本，已有数据会保留。
"""),
            "features": G("功能一览", "日常最常用的功能，快速看一遍。", """
## 每天浏览

- 多个标签与窗口：拖出、合并、分组、折叠、静音、悬停预览。
- 地址栏优先补全你常去的站点，找不到时直接用搜索引擎搜索。
- 命令面板（⌘K）、标签搜索（⌘⇧A）、页内查找（⌘F），齿轮菜单里还有完整快捷键表。

## 看得舒服

- 主题：跟随系统 / 浅色 / 深色；网页强制深色；每日自动切换。
- 主色：蓝、紫、青、绿、橙、玫红，六选一。
- 书签栏：始终隐藏 / 始终显示 / 仅在新标签页显示。

## 广告与脚本

- 广告拦截支持订阅、自定义规则和白名单；订阅更新失败时会沿用旧规则。
- 用户脚本（`.user.js`）可在设置页管理，下载完成即安装。

## 视频与文件

- 下载可以暂停、继续、取消和重试；完成后可在访达中显示，或用关联应用打开。
- 嗅探面板识别页面里的视频，分成多段的也会合成一个 MP4。

## 快捷键速查

| 快捷键 | 作用 |
| --- | --- |
| ⌘T / ⌘W | 新建 / 关闭标签 |
| ⌘L | 定位地址栏 |
| ⌘F | 查找页面内容 |
| ⌘⇧N | 无痕窗口 |
| ⌘K | 命令面板 |
| ⌘⇧A | 搜索标签 |
| ⌘⇧R | 阅读模式 |
"""),
            "faq": G("常见问题", "关于 Persim 的快速解答。", """
### Persim 收费吗？

可以从 Mac App Store 免费下载，基础浏览功能可直接使用。部分高级能力通过应用内购买解锁，免费版会在标签栏显示一个小标记。

### 支持哪些系统？

Persim 面向 macOS 12 及以上，兼容 Apple Silicon 与 Intel 芯片的 Mac。

### 我的数据会上传吗？

不需要账户。历史、书签、会话和下载记录都留在你的 Mac 上。需要联网的功能（例如更新广告拦截订阅）只获取它需要的内容；Cookie 管理器里可以清除站点数据。

### 怎么导入其他浏览器的书签？

在 Chrome 或 Edge 中把书签导出为 HTML 文件，再在 Persim 书签管理器里选择「导入 HTML」。多层文件夹和重复链接都会自动处理。

### 怎么保存网页上的视频？

打开嗅探面板，选择识别到的视频并下载。分成多段的视频会合成一个 MP4，下载完可以用你平时用的应用打开。

### 怎么切换界面语言？

打开 `persim://settings` → 「常规」→「界面语言」。应用提供 25 种语言，重新打开窗口后生效。

### 还有其他问题？

写信到 **persim@w3cub.com**，告诉我们你想做什么，我们会尽力帮忙。
"""),
            "privacy": G("隐私与数据", "哪些内容留在你的 Mac 上，哪些情况需要联网。", """
## 保存在本机

历史、书签、当前标签、下载记录和 Cookie 都保存在本地。没有账户，也没有云同步。无痕窗口（⌘⇧N）不会写入历史与会话。

## 什么时候会联网

- 打开你访问的网站，这是理所当然的。
- 启用了广告订阅时，更新订阅规则。更新失败也会沿用已保存的规则。
- 下载你主动请求的用户脚本或文件。

## 权限由你决定

摄像头和麦克风按网站记住：你可以允许一个站点、拒绝另一个。定位与通知由 macOS 系统管理。弹窗默认只放行你允许的站点。

## 磁盘上的文件

Persim 只会读取你在系统文件面板里选择、或明确授权过的文件夹，授权情况可以在设置中查看和撤销。

## 联系我们

关于隐私的问题：**persim@w3cub.com**。
"""),

            "troubleshooting": G("常见问题排查", "遇到问题时可以试试这些办法。", """
## 网页打不开

- 先确认其他网站能否打开，再按 ⌘R 刷新。
- 如果开了广告拦截规则，先暂停一下，看看是不是拦了这个网站。
- 用无痕窗口（⌘⇧N）试试。如果无痕下正常，可在设置里清除该网站的 Cookie。

## 下载卡住或不完整

- 打开下载面板，暂停后重试。
- 从网页保存的视频如果失败，先删除不完整的文件再试。分段视频会合成一个 MP4，合成失败时原始分片会留在下载目录。

## 书签没导入成功

先在旧浏览器里把书签导出成 HTML 文件，再在 Persim 的书签管理器里选择「导入 HTML」。文件夹和重复链接会自动处理。

## 检测不到视频

不是每个网站都能直接保存视频。在目标页面打开媒体面板看看；如果没有列出，说明该站点的播放方式不支持直接保存。

## 浏览器变慢

关掉不用的标签页，或停用不再需要的广告拦截订阅。站点权限可以在设置里查看。

## 还是解决不了

发邮件到 **persim@w3cub.com**，说明你在做什么，最好附一张截图。
"""),
            "legal": G("法律信息", "Persim 的相关法律条款。", """
Persim 由 w3cub.com 开发与发布。

- [隐私政策](./privacy-policy) — 收集哪些数据、如何处理。
- [隐私选择](./privacy-choices) — 如何控制存储与分享的内容。
- [服务条款](./terms) — 使用本应用的条款。

对以上文档有疑问：**persim@w3cub.com**。
"""),
            "privacy-policy": G("隐私政策", "Persim 收集什么，什么只留在你的设备上。", """
## 无需账户，没有云端资料

Persim 不需要登录，也不会为你创建在线账户。历史记录、书签、打开的标签、下载和 Cookie 都保存在你的 Mac 上。

## 打开网页时用到的信息

和所有浏览器一样，Persim 会把你访问的地址发送给对应网站。Persim 自身不会把你的浏览历史上传到服务器。

## 你可以开启的网络功能

- 广告拦截订阅会联网更新规则；更新失败时，已保存的规则继续生效。
- 油猴脚本和你下载的文件，只在你主动操作时才会获取。
- 在地址栏输入时会向你选择的搜索引擎获取搜索建议。

## 本地权限

摄像头、麦克风和文件权限按网站分别记住，可在设置里修改。定位与通知由 macOS 管理。无痕窗口（⌘⇧N）不会写入历史记录或会话。

## 第三方网站

你访问的网站由他人运营，遵循各自的隐私政策。Persim 的内置页面不会追踪你。

## 联系我们

隐私相关问题：**persim@w3cub.com**。
"""),
            "privacy-choices": G("隐私选择", "几个简单的方法，让你自己掌控。", """
## 无痕浏览

使用无痕窗口（⌘⇧N）。它不会写入历史记录或记住会话，关闭后标签页即消失。

## 清除已存内容

在设置的 Cookie 管理器里删除 Cookie 和网站数据。历史记录和下载记录也可以在同一处清除。

## 决定每个网站能做什么

摄像头、麦克风和文件权限按网站分别记住。在设置里允许你信任的网站、拒绝其他网站。弹窗只对你允许的网站开放。

## 控制后台功能

在设置里随时开关广告拦截订阅。关闭后不会拉取任何规则。

## 选择搜索引擎

在设置里指定默认搜索引擎，搜索建议来自你选择的引擎。

## 有疑问

想了解更多数据处理方式，请写信到 **persim@w3cub.com**。
"""),
            "terms": G("服务条款", "使用 Persim 的条款。", """
## 使用本应用

Persim 供个人使用。你可以在自己拥有或获准使用的 Mac 上下载和使用它。

## 免费与付费功能

核心浏览功能免费提供。部分高级功能需通过应用内购买解锁。免费版会在标签栏显示一个小徽标，购买后可移除。

## 第三方内容

你通过 Persim 使用的网站、订阅和油猴脚本均由各自作者提供。Persim 对其内容或可用性不承担责任。

## 变更

功能和本条款可能随时间调整。以本网站发布的最新版本为准。

## 联系我们

对本条款有疑问：**persim@w3cub.com**。
"""),
        },
    },
    "zh-TW": {
        "versionBadge": "為 Mac 打造 · 免費下載",
        "hero": {
            "name": "Persim 柿子瀏覽器",
            "text": "輕快上網，清爽如初",
            "tagline": "多分頁、廣告攔截、影片儲存、閱讀模式與 AI 直達——你每天要用的，都在這裡。打開就會用，不用折騰。",
            "image": {"src": "/screenshot-newtab.png", "alt": "Persim 新分頁"},
        },
        "actions": [
            {"text": "免費下載", "link": STORE, "theme": "brand", "external": True},
            {"text": "看看功能", "link": "/#features", "theme": "alt"},
        ],
        "downloadNote": "適用於 macOS 12 及以上 · 支援 Apple Silicon 與 Intel",
        "features": [
            F("tabs", "多個分頁，隨手切換", "新增、拖曳、分組、靜音、暫停預覽，都照你熟悉的來。想找某個頁面，按 ⌘⇧A 搜一下就行。"),
            F("shield", "廣告少一點，頁面淨一點", "內建廣告攔截，可訂閱規則、自己加白名單。網頁靜音、彈窗攔截也在設定裡一鍵開關。"),
            F("download", "喜歡的影片，留下來", "看到想收藏的影片，從偵測面板一鍵儲存；分成多段的影片會合成一個 MP4，下載還能暫停、繼續和重試。"),
            F("ai", "把問題直接交給 AI", "網址列輸入「ai 今天吃什麼」就能直達常用 AI 網站，ChatGPT、Claude、豆包等都在新分頁裡。"),
            F("book", "長文讀起來更舒服", "閱讀模式拿掉導覽和廣告，只留下正文；網頁強制深色、整頁截圖和列印也順手可用。"),
            F("palette", "調成你喜歡的樣子", "淺色 / 深色 / 跟隨系統，六種主色，書籤列三種顯示方式，介面語言 25 種。"),
        ],
        "sections": {
            "featuresTitle": "每天要用的，都剛剛好",
            "featuresSubtitle": "沒有複雜的設定精靈。打開 Persim，搜尋、瀏覽、儲存——就是這麼簡單。",
            "shotsTitle": "看一眼，就知道它有多清爽",
            "shotsSubtitle": "新分頁把常用網站放在眼前；設定頁把主題、主色和語言放在一起，改完立刻生效。",
            "accentTitle": "選一種主色調",
            "accentSubtitle": "點上方導覽列的色塊按鈕就能換色，也可以在這裡選——整個網站都會跟著變。",
            "howTitle": "三步，開始清爽瀏覽",
            "howSubtitle": "從下載到順手，只要幾分鐘。",
            "faqTitle": "常見問題",
            "faqSubtitle": "關於下載、隱私和日常使用",
        },
        "banners": [{"title": "多分頁，跟得上", "alt": "Persim 新分頁宣傳圖"}, {"title": "隨你定制", "alt": "Persim 設定頁宣傳圖"}, {"title": "效率升級", "alt": "Persim 油猴腳本宣傳圖"}],
        "accentLabels": ["柿子色", "紫色", "青色", "綠色", "藍色", "玫紅"],
        "steps": [
            {"num": "01", "title": "裝好就打開", "desc": "從 Mac App Store 下載，拖進「應用程式」即可，不需要註冊帳戶。"},
            {"num": "02", "title": "把常用網站帶過來", "desc": "從 Chrome 或 Edge 匯出書籤 HTML，在 Persim 的書籤管理員裡一次匯入。"},
            {"num": "03", "title": "按你的習慣調整", "desc": "在設定裡切換主題、主色和介面語言；想恢復上次的分頁，打開「恢復上次工作階段」。"},
        ],
        "faqs": [
            {"question": "Persim 收費嗎？", "answer": "可以從 Mac App Store 免費下載，基礎瀏覽功能可直接使用；部分進階功能透過應用程式內購買解鎖。免費版會在分頁列顯示一個小標記。"},
            {"question": "支援哪些 Mac？", "answer": "macOS 12 及以上，Apple Silicon 和 Intel 晶片都支援。"},
            {"question": "我的瀏覽紀錄會上傳嗎？", "answer": "不會。歷史、書籤、工作階段和下載紀錄都留在你的 Mac 上，也不需要帳戶。只有更新廣告訂閱這類功能才會連網。"},
            {"question": "怎麼把 Chrome 的書籤匯進來？", "answer": "在 Chrome 中把書籤匯出成 HTML 檔，然後開啟 Persim 的書籤管理員，選擇「匯入 HTML」。"},
            {"question": "怎麼儲存網頁裡的影片？", "answer": "開啟偵測面板，選擇辨識到的影片，按下載即可；分成多段的影片會合成一個 MP4。一般檔案下載也能暫停、繼續和重試。"},
        ],
        "faqMore": "更多問題 →",
        "cta": {
            "title": "給上網這件事，留一點清爽。",
            "description": "下載 Persim，把瀏覽器調成你喜歡的樣子。",
            "primary": "在 Mac App Store 下載",
            "primaryLink": STORE,
            "secondary": "閱讀使用指南",
            "secondaryLink": "/guide/introduction",
        },
        "guides": {
            "introduction": G("認識 Persim", "一個打開就能用的 Mac 瀏覽器：分頁、搜尋、書籤、下載，都在該在的位置。", """
## 打開就會做什麼

- **上網與搜尋**：網址列既能輸入網址，也能直接搜尋；常去的地址會優先補全。
- **多個分頁與視窗**：新增、拖曳、分組、靜音、暫停預覽，按 ⌘⇧A 快速找到某個分頁。
- **收藏與找回**：書籤列、書籤管理員、歷史紀錄、下載中心，還有「恢復上次工作階段」。

## 想安靜一點

- 廣告攔截支援訂閱規則、自訂規則與白名單，信任的網站可以放行。
- 網頁強制深色、分頁靜音、彈窗攔截都在設定裡一鍵開關。
- 無痕視窗（⌘⇧N）不會寫下瀏覽紀錄。

## 看影片與讀長文

- 偵測面板列出頁面裡的影片，儲存後就是一個完整的 MP4，用你習慣的應用程式開啟即可。
- 閱讀模式（⌘⇧R）拿掉導覽和廣告，只留下正文；也可以擷取可視區或整頁 PDF。

## 按你的習慣來

淺色 / 深色 / 跟隨系統，六種主色，書籤列三種顯示方式，介面語言 25 種。外觀改完立刻生效，介面語言需要重新開啟視窗。
"""),
            "installation": G("安裝 Persim", "下載、設為預設瀏覽器，再把書籤帶過來。", """
## 下載與安裝

1. 開啟 [Mac App Store](""" + STORE + """)，搜尋 Persim。
2. 下載完成後，把應用程式拖進「應用程式」資料夾；系統詢問時確認即可。
3. 想設為預設瀏覽器，開啟「系統設定 → 預設網頁瀏覽器」，選擇 Persim。

需要 macOS 12 及以上，Apple Silicon 和 Intel 晶片都支援。

## 第一次開啟

- 在 `persim://settings` 的「一般」裡選擇外觀、主色與書籤列顯示方式。
- 介面語言有 25 種；切換後重新開啟視窗生效。
- 新分頁已經放好常用網站與 AI 直達入口，直接用即可。

## 把書籤帶過來

1. 在 Chrome 或 Edge 裡把書籤匯出成 HTML 檔。
2. 開啟 Persim 的書籤管理員，選擇「匯入 HTML」並選取檔案。
3. 多層資料夾會還原，重複網址會自動略過；書籤列也可以隨時拖曳排序。

## 後續更新

在 Mac App Store 的「更新」頁取得新版本，已有資料會保留。
"""),
            "features": G("功能一覽", "日常最常用的功能，快速看一遍。", """
## 每天瀏覽

- 多個分頁與視窗：拖出、合併、分組、摺疊、靜音、暫停預覽。
- 網址列優先補全你常去的網站，找不到時直接用搜尋引擎搜尋。
- 命令面板（⌘K）、分頁搜尋（⌘⇧A）、頁內尋找（⌘F），齒輪選單裡還有完整快速鍵表。

## 看得舒服

- 主題：跟隨系統 / 淺色 / 深色；網頁強制深色；每日自動切換。
- 主色：藍、紫、青、綠、橙、玫紅，六選一。
- 書籤列：始終隱藏 / 始終顯示 / 僅在新分頁顯示。

## 廣告與腳本

- 廣告攔截支援訂閱、自訂規則與白名單；訂閱更新失敗時會沿用舊規則。
- 使用者腳本（`.user.js`）可在設定頁管理，下載完成即安裝。

## 影片與檔案

- 下載可以暫停、繼續、取消和重試；完成後可在 Finder 中顯示，或用關聯應用程式開啟。
- 偵測面板辨識頁面裡的影片，分成多段的也會合成一個 MP4。

## 快速鍵速查

| 快速鍵 | 作用 |
| --- | --- |
| ⌘T / ⌘W | 新增 / 關閉分頁 |
| ⌘L | 定位網址列 |
| ⌘F | 尋找頁面內容 |
| ⌘⇧N | 無痕視窗 |
| ⌘K | 命令面板 |
| ⌘⇧A | 搜尋分頁 |
| ⌘⇧R | 閱讀模式 |
"""),
            "faq": G("常見問題", "關於 Persim 的快速解答。", """
### Persim 收費嗎？

可以從 Mac App Store 免費下載，基礎瀏覽功能可直接使用。部分進階功能透過應用程式內購買解鎖，免費版會在分頁列顯示一個小標記。

### 支援哪些系統？

Persim 面向 macOS 12 及以上，相容 Apple Silicon 與 Intel 晶片的 Mac。

### 我的資料會上傳嗎？

不需要帳戶。歷史、書籤、工作階段和下載紀錄都留在你的 Mac 上。需要連網的功能（例如更新廣告訂閱）只會取得它需要的內容；Cookie 管理員裡可以清除網站資料。

### 怎麼匯入其他瀏覽器的書籤？

在 Chrome 或 Edge 中把書籤匯出為 HTML 檔案，再在 Persim 書籤管理員裡選擇「匯入 HTML」。多層資料夾和重複連結都會自動處理。

### 怎麼儲存網頁上的影片？

開啟偵測面板，選擇辨識到的影片並下載。分成多段的影片會合成一個 MP4，下載完可以用你平時用的應用程式開啟。

### 怎麼切換介面語言？

開啟 `persim://settings` → 「一般」→「介面語言」。應用程式提供 25 種語言，重新開啟視窗後生效。

### 還有其他問題？

寫信到 **persim@w3cub.com**，告訴我們你想做什麼，我們會盡力幫忙。
"""),
            "privacy": G("隱私與資料", "哪些內容留在你的 Mac 上，哪些情況需要連網。", """
## 保存在本機

歷史、書籤、目前分頁、下載紀錄與 Cookie 都保存在本機。沒有帳戶，也沒有雲端同步。無痕視窗（⌘⇧N）不會寫入歷史與工作階段。

## 什麼時候會連網

- 開啟你造訪的網站，這是理所當然的。
- 啟用了廣告訂閱時，更新訂閱規則。更新失敗也會沿用已儲存的規則。
- 下載你主動要求的使用者腳本或檔案。

## 權限由你決定

鏡頭和麥克風按網站記住：你可以允許一個網站、拒絕另一個。定位與通知由 macOS 系統管理。彈窗預設只放行你允許的網站。

## 磁碟上的檔案

Persim 只會讀取你在系統檔案面板中選擇、或明確授權過的資料夾，授權情況可以在設定中查看和撤銷。

## 聯絡我們

關於隱私的問題：**persim@w3cub.com**。
"""),

            "troubleshooting": G("常見問題排查", "遇到問題時可以試試這些辦法。", """
## 網頁打不開

- 先確認其他網站能否開啟，再按 ⌘R 重新整理。
- 如果開啟了廣告攔截規則，先暫停一下，看看是不是攔了這個網站。
- 用無痕視窗（⌘⇧N）試試。如果無痕下正常，可在設定裡清除該網站的 Cookie。

## 下載卡住或不完整

- 開啟下載面板，暫停後重試。
- 從網頁儲存的影片如果失敗，先刪除不完整的檔案再試。分段影片會合成一個 MP4，合成失敗時原始分片會留在下載目錄。

## 書籤沒匯入成功

先在舊瀏覽器裡把書籤匯出成 HTML 檔，再在 Persim 的書籤管理員裡選擇「匯入 HTML」。資料夾和重複連結會自動處理。

## 偵測不到影片

不是每個網站都能直接儲存影片。在目標頁面開啟媒體面板看看；如果沒有列出，代表該站點的播放方式不支援直接儲存。

## 瀏覽器變慢

關掉不用的分頁，或停用不再需要的廣告攔截訂閱。網站權限可以在設定裡檢視。

## 還是解決不了

寄信到 **persim@w3cub.com**，說明你在做什麼，最好附上一張截圖。
"""),
            "legal": G("法律資訊", "Persim 的相關法律條款。", """
Persim 由 w3cub.com 開發與發布。

- [隱私權政策](./privacy-policy) — 收集哪些資料、如何處理。
- [隱私選擇](./privacy-choices) — 如何控制儲存與分享的內容。
- [服務條款](./terms) — 使用本應用程式的條款。

對以上文件有疑問：**persim@w3cub.com**。
"""),
            "privacy-policy": G("隱私權政策", "Persim 收集什麼，什麼只留在你的裝置上。", """
## 無需帳號，沒有雲端資料

Persim 不需要登入，也不會為你建立線上帳號。歷史記錄、書籤、開啟的分頁、下載與 Cookie 都儲存在你的 Mac 上。

## 開啟網頁時用到的資訊

和所有瀏覽器一樣，Persim 會把你造訪的位址傳送給對應網站。Persim 本身不會將你的瀏覽歷史上傳到伺服器。

## 你可以開啟的網路功能

- 廣告攔截訂閱會連線更新規則；更新失敗時，已儲存的規則繼續生效。
- 油猴腳本與你下載的檔案，只在你主動操作時才會取得。
- 在網址列輸入時會向你選擇的搜尋引擎取得搜尋建議。

## 本機權限

相機、麥克風與檔案權限按網站分別記住，可在設定裡修改。定位與通知由 macOS 管理。無痕視窗（⌘⇧N）不會寫入歷史記錄或工作階段。

## 協力廠商網站

你造訪的網站由他人經營，遵循各自的隱私權政策。Persim 的內建頁面不會追蹤你。

## 聯絡我們

隱私相關問題：**persim@w3cub.com**。
"""),
            "privacy-choices": G("隱私選擇", "幾個簡單的方法，讓你自己掌控。", """
## 無痕瀏覽

使用無痕視窗（⌘⇧N）。它不會寫入歷史記錄或記住工作階段，關閉後分頁即消失。

## 清除已存內容

在設定的 Cookie 管理員裡刪除 Cookie 與網站資料。歷史記錄與下載記錄也可以在同一處清除。

## 決定每個網站能做什麼

相機、麥克風與檔案權限按網站分別記住。在設定裡允許你信任的網站、拒絕其他網站。彈出式視窗只對你允許的網站開放。

## 控制背景功能

在設定裡隨時開關廣告攔截訂閱。關閉後不會拉取任何規則。

## 選擇搜尋引擎

在設定裡指定預設搜尋引擎，搜尋建議來自你選擇的引擎。

## 有疑問

想了解更多資料處理方式，請寫信到 **persim@w3cub.com**。
"""),
            "terms": G("服務條款", "使用 Persim 的條款。", """
## 使用本應用程式

Persim 供個人使用。你可以在自己擁有或獲准使用的 Mac 上下載與使用它。

## 免費與付費功能

核心瀏覽功能免費提供。部分進階功能需透過應用程式內購買解鎖。免費版會在分頁列顯示一個小徽標，購買後可移除。

## 協力廠商內容

你透過 Persim 使用的網站、訂閱與油猴腳本均由各自作者提供。Persim 對其內容或可用性不承担责任。

## 變更

功能與本條款可能隨時間調整。以本網站發布的最新版本為準。

## 聯絡我們

對本條款有疑問：**persim@w3cub.com**。
"""),
        },
    },
    "ja": {
        "versionBadge": "Mac 向け · 無料でダウンロード",
        "hero": {
            "name": "Persim",
            "text": "軽やかに、すっきりと",
            "tagline": "タブ、広告ブロック、動画保存、リーディングモード、AI ショートカット。毎日使う機能が、静かで使いやすい場所に揃っています。",
            "image": {"src": "/screenshot-newtab.png", "alt": "Persim の新しいタブ"},
        },
        "actions": [
            {"text": "無料でダウンロード", "link": STORE, "theme": "brand", "external": True},
            {"text": "機能を見る", "link": "/#features", "theme": "alt"},
        ],
        "downloadNote": "macOS 12 以降 · Apple Silicon と Intel に対応",
        "features": [
            F("tabs", "タブを自由に", "タブの作成、ドラッグ、グループ化、ミュート、ホバープレビュー。⌘⇧A で目的のタブをすぐに見つけられます。"),
            F("shield", "広告を減らし、画面をすっきり", "広告ブロックを内蔵。購読ルールや自分で追加したルール、許可リストも使えます。"),
            F("download", "見つけた動画を残す", "ページ内の動画を検出して保存。分割された動画はひとつの MP4 にまとまり、ダウンロードは一時停止と再開に対応します。"),
            F("ai", "AI にまっすぐ質問", "アドレスバーに「ai + 質問」と入力すると、よく使う AI サイトへ。ChatGPT や Claude などが新しいタブに並んでいます。"),
            F("book", "長い文章を快適に", "リーディングモードがメニューや広告を除いて本文だけを表示。ページの強制ダーク表示や全ページ保存も便利です。"),
            F("palette", "自分らしく設定", "ライト / ダーク / システムに従う、6 色のアクセントカラー、ブックマークバーの 3 モード、25 言語の UI。"),
        ],
        "sections": {
            "featuresTitle": "ちょうどいいブラウザー",
            "featuresSubtitle": "面倒な設定は不要。Persim を開いて、検索して、見て、保存するだけです。",
            "shotsTitle": "ひと目でわかる使いやすさ",
            "shotsSubtitle": "新しいタブにはよく行くサイト。設定にはテーマ、アクセントカラー、言語がまとまっています。",
            "accentTitle": "アクセントカラーを選ぶ",
            "accentSubtitle": "上部バーのカラーボタン、またはここから切り替えられます。サイト全体が変わります。",
            "howTitle": "3 ステップで快適に",
            "howSubtitle": "ダウンロードから毎日の利用まで、ほんの数分です。",
            "faqTitle": "よくある質問",
            "faqSubtitle": "ダウンロード、プライバシー、日常の使い方",
        },
        "banners": [{"title": "タブが追いつく", "alt": "Persim 新しいタブのバナー"}, {"title": "自分らしくカスタマイズ", "alt": "Persim 設定のバナー"}, {"title": "ブラウザーをさらに便利に", "alt": "Persim ユーザースクリプトのバナー"}],
        "accentLabels": ["柿色", "バイオレット", "ティール", "グリーン", "ブルー", "ローズ"],
        "steps": [
            {"num": "01", "title": "インストール", "desc": "Mac App Store からダウンロードし、Applications フォルダーへドラッグ。アカウント登録は不要です。"},
            {"num": "02", "title": "ブックマークを持ってくる", "desc": "Chrome や Edge でブックマークを HTML に書き出し、Persim のブックマークマネージャーで読み込みます。"},
            {"num": "03", "title": "好みに合わせる", "desc": "設定でテーマ、色、言語を変更。前回のセッションを復元する設定もあります。"},
        ],
        "faqs": [
            {"question": "Persim は無料ですか？", "answer": "Mac App Store から無料でダウンロードでき、基本的なブラウジングは無料で使えます。一部の高度な機能はアプリ内課金で利用できます。無料版ではタブバーに小さなバッジが表示されます。"},
            {"question": "どの Mac で使えますか？", "answer": "macOS 12 以降、Apple Silicon と Intel の両方に対応しています。"},
            {"question": "履歴はアップロードされますか？", "answer": "いいえ。履歴、ブックマーク、セッション、ダウンロードは Mac 内に保存され、アカウントも不要です。広告ブロックの購読更新など、必要な機能だけが通信します。"},
            {"question": "Chrome のブックマークを移行するには？", "answer": "Chrome でブックマークを HTML ファイルに書き出し、Persim のブックマークマネージャーで「HTML を読み込む」を選びます。"},
            {"question": "ページ内の動画を保存するには？", "answer": "メディアパネルを開いて検出された動画を選択し、ダウンロードします。分割された動画はひとつの MP4 にまとめられます。"},
        ],
        "faqMore": "その他の質問 →",
        "cta": {
            "title": "ブラウジングに、少しの余白を。",
            "description": "Persim をダウンロードして、好きな形に整えましょう。",
            "primary": "Mac App Store でダウンロード",
            "primaryLink": STORE,
            "secondary": "ガイドを読む",
            "secondaryLink": "/guide/introduction",
        },
        "guides": {
            "introduction": G("Persim とは", "開いた瞬間から使える Mac ブラウザー。タブ、検索、ブックマーク、ダウンロードが揃っています。", """
## まずできること

- **検索と閲覧**：アドレスバーに URL も質問も入力できます。よく行くサイトが先に候補として出ます。
- **タブとウィンドウ**：作成、ドラッグ、グループ化、ミュート、ホバーでプレビュー。⌘⇧A でタブを検索できます。
- **あとで見つける**：ブックマーク、履歴、ダウンロード、そして「前回のセッションを復元」。

## 少し静かに

- 広告ブロックは購読ルール、独自ルール、許可リストに対応。
- ページの強制ダーク表示、タブのミュート、ポップアップ制限は設定で切り替えます。
- プライベートウィンドウ（⌘⇧N）では履歴を残しません。

## 動画と長文

- メディアパネルにページ内の動画が並び、保存するとひとつの MP4 になります。
- リーディングモード（⌘⇧R）は本文だけを残します。表示範囲や全ページを PDF で保存できます。

## 自分らしく

ライト / ダーク / システムに従う、6 色のアクセント、ブックマークバーの 3 モード、25 言語の UI。外観はすぐ反映され、言語はウィンドウを開き直すと反映されます。
"""),
            "installation": G("インストール", "ダウンロード、既定のブラウザー設定、ブックマークの移行。", """
## ダウンロードとインストール

1. [Mac App Store](""" + STORE + """) で Persim を探します。
2. ダウンロード後、Applications フォルダーにドラッグします。
3. 既定のブラウザーにするには「システム設定 → 既定の Web ブラウザー」で Persim を選びます。

macOS 12 以降、Apple Silicon / Intel の両方に対応しています。

## 最初の 1 分

- `persim://settings` の「一般」で外観、アクセントカラー、ブックマークバーを選びます。
- UI 言語は 25 言語。切り替えたらウィンドウを開き直してください。
- 新しいタブにはよく行くサイトと AI ショートカットが最初から並んでいます。

## ブックマークの移行

1. Chrome または Edge でブックマークを HTML に書き出します。
2. Persim のブックマークマネージャーで「HTML を読み込む」を選びます。
3. 入れ子のフォルダーは復元され、重複 URL はスキップされます。

## アップデート

Mac App Store の「更新」から入手できます。データはそのまま残ります。
"""),
            "features": G("機能一覧", "よく使う機能を手早く確認。", """
## 毎日のブラウジング

- タブとウィンドウ：ドラッグ、グループ化、折りたたみ、ミュート、プレビュー。
- アドレスバーはよく行くサイトを先に提案し、見つからなければ検索します。
- コマンドパレット（⌘K）、タブ検索（⌘⇧A）、ページ内検索（⌘F）、キーボードショートカット一覧。

## 見やすく

- テーマ：システムに従う / ライト / ダーク。ページの強制ダークや毎日の自動切り替えも。
- アクセントカラーは 6 色：ブルー、バイオレット、ティール、グリーン、オレンジ、ローズ。
- ブックマークバー：常に非表示 / 常に表示 / 新しいタブのみ。

## 広告とスクリプト

- 広告ブロックは購読、独自ルール、許可リストに対応。更新できなくても古いルールが効き続けます。
- ユーザースクリプト（`.user.js`）は設定で管理し、ダウンロード完了時にインストールされます。

## 動画とファイル

- ダウンロードは一時停止、再開、キャンセル、再試行に対応。完了後は Finder で表示したり関連アプリで開けます。
- メディアパネルは分割された動画もひとつの MP4 にまとめます。

## ショートカット

| キー | 動作 |
| --- | --- |
| ⌘T / ⌘W | タブの作成 / 閉じる |
| ⌘L | アドレスバーへ |
| ⌘F | ページ内検索 |
| ⌘⇧N | プライベートウィンドウ |
| ⌘K | コマンドパレット |
| ⌘⇧A | タブ検索 |
| ⌘⇧R | リーディングモード |
"""),
            "faq": G("よくある質問", "Persim についての簡単な回答。", """
### 無料ですか？

基本機能は無料で使えます。一部の高度な機能はアプリ内課金で利用でき、無料版ではタブバーに小さなバッジが表示されます。

### 対応 OS は？

macOS 12 以降、Apple Silicon と Intel の Mac に対応しています。

### データはアップロードされますか？

アカウントは不要で、履歴、ブックマーク、セッション、ダウンロードは Mac 内に残ります。通信が必要な機能（広告ブロックの購読更新など）だけがインターネットに接続します。

### ブックマークを移行するには？

Chrome や Edge で HTML に書き出し、Persim のブックマークマネージャーで読み込みます。フォルダーや重複リンクは自動で処理されます。

### 動画を保存するには？

メディアパネルで検出された動画を選んでダウンロードします。分割された動画はひとつの MP4 にまとまります。

### 言語を変えるには？

`persim://settings` → 「一般」→「言語」へ。25 言語から選べ、ウィンドウを開き直すと反映されます。

### その他の質問

**persim@w3cub.com** までご連絡ください。
"""),
            "privacy": G("プライバシーとデータ", "Mac に残るものと、通信が必要な場合。", """
## ローカルに保存されるもの

履歴、ブックマーク、開いているタブ、ダウンロード、Cookie はローカルに保存されます。アカウントもクラウド同期もありません。プライベートウィンドウ（⌘⇧N）では履歴とセッションに残りません。

## 通信する場合

- あなたが開くウェブサイトを読み込むとき。
- 広告ブロックの購読を有効にしているときの更新。失敗しても保存済みのルールは働き続けます。
- あなたが指定したスクリプトやファイルをダウンロードするとき。

## 権限

カメラとマイクの許可はサイトごとに記憶されます。位置情報と通知は macOS が管理します。ポップアップは許可したサイトだけに限定されます。

## ファイルアクセス

Persim が読めるのは、ファイルダイアログで選んだ、または明示的に許可したフォルダーだけです。設定で確認と取り消しができます。

## お問い合わせ

プライバシーについて：**persim@w3cub.com**。
"""),

            "troubleshooting": G("トラブルシューティング", "よくある問題とその解決方法。", """
## ページが開かない

- 他のサイトが開けるか確認してから、⌘R で再読み込みしてください。
- 広告ブロックのルールを有効にしている場合、一時的に止めて原因を確かめてください。
- プライベートウィンドウ（⌘⇧N）で試してください。そこで開ける場合は、設定からそのサイトの Cookie を削除してください。

## ダウンロードが止まる・途中で終わる

- ダウンロードパネルで一時停止してから再開してください。
- ページから保存した動画が失敗したら、途中のファイルを削除して再度お試しください。分割動画は MP4 に結合され、失敗した場合は元の分割ファイルがダウンロードフォルダに残ります。

## ブックマークが読み込めない

まず旧ブラウザーでブックマークを HTML ファイルに書き出し、Persim のブックマークマネージャーで「HTML を読み込む」を選んでください。フォルダーや重複リンクは自動で整理されます。

## 動画が見つからない

すべてのサイトで動画を保存できるわけではありません。対象ページでメディアパネルを開いてみてください。何も表示されない場合、そのサイトの再生方式では直接保存できません。

## 動作が重い

使っていないタブを閉じるか、不要になった広告ブロックの購読を無効にしてください。サイトの権限は設定で確認できます。

## 解決しない場合

**persim@w3cub.com** まで、何をしようとしていたか（可能ならスクリーンショットも）をお知らせください。
"""),
            "legal": G("法務情報", "Persim に関する法務情報。", """
Persim は w3cub.com が開発・提供しています。

- [プライバシーポリシー](./privacy-policy) — 扱うデータとその方法。
- [プライバシー設定](./privacy-choices) — 保存・共有の制御方法。
- [利用規約](./terms) — アプリの利用条件。

これらの文書に関するご質問：**persim@w3cub.com**。
"""),
            "privacy-policy": G("プライバシーポリシー", "Persim が収集する情報と、端末に残る情報。", """
## アカウント不要、クラウドプロフィールなし

Persim はログインを求めず、オンラインアカウントも作成しません。履歴、ブックマーク、開いているタブ、ダウンロード、Cookie は Mac 上に保存されます。

## ページ表示に使う情報

他のブラウザーと同様、開いたサイトのアドレスをそのサイトに送信します。Persim 自身が閲覧履歴をサーバーへアップロードすることはありません。

## オン・オフできるネットワーク機能

- 広告ブロックの購読はルール一覧を更新します。更新に失敗しても保存済みのルールは動作し続けます。
- ユーザースクリプトやダウンロードファイルは、あなたが求めたときだけ取得します。
- アドレスバーへの入力では、選択した検索エンジンから候補を取得します。

## ローカルの権限

カメラ、マイク、ファイルへのアクセスはサイトごとに記憶され、設定で変更できます。位置情報と通知は macOS が管理します。プライベートウィンドウ（⌘⇧N）は履歴やセッションに残りません。

## サードパーティのサイト

訪問するサイトは他社が運営し、それぞれのプライバシーポリシーに従います。Persim の内蔵ページはあなたを追跡しません。

## お問い合わせ

プライバシーに関するご質問：**persim@w3cub.com**。
"""),
            "privacy-choices": G("プライバシー設定", "自分で管理するための簡単な方法。", """
## 記録を残さずに browsing

プライベートウィンドウ（⌘⇧N）を使ってください。履歴やセッションに残らず、閉じるとタブは消えます。

## 保存した内容を消す

設定の Cookie マネージャーから Cookie とサイトデータを削除できます。履歴やダウンロードも同じ場所で消去できます。

## サイトごとに許可を決める

カメラ、マイク、ファイルのアクセスはサイトごとに記憶されます。設定で信頼するサイトを許可し、それ以外を拒否できます。ポップアップは許可したサイトだけに開かれます。

## バックグラウンド機能を制御する

広告ブロックの購読は設定からいつでもオン・オフできます。オフにするとルールは取得されません。

## 検索エンジンを選ぶ

設定で既定の検索エンジンを指定できます。検索候補は選択したエンジンから届きます。

## ご質問

データの扱いについて詳しく知りたい場合は **persim@w3cub.com** までご連絡ください。
"""),
            "terms": G("利用規約", "Persim の利用条件。", """
## アプリの利用

Persim は個人利用のために提供されます。所有している、または使用を許可された Mac でダウンロードして利用できます。

## 無料と有料の機能

基本的なブラウジング機能は無料です。一部の高度な機能はアプリ内購入で利用できます。無料版ではタブバーに小さなバッジが表示され、購入すると削除できます。

## サードパーティのコンテンツ

Persim を通じて利用するサイト、購読、ユーザースクリプトは各作者が提供します。Persim はその内容や可用性について責任を負いません。

## 変更

機能と本規約は変更される場合があります。现行的なものは本サイトに掲載された版です。

## お問い合わせ

本規約に関するご質問：**persim@w3cub.com**。
"""),
        },
    },
    "de": {
        "versionBadge": "Für Mac · Kostenlos herunterladen",
        "hero": {
            "name": "Persim",
            "text": "Leicht und aufgeräumt",
            "tagline": "Tabs, Werbeblocker, Video-Downloads, Lesemodus und AI-Kürzel — alles, was du täglich brauchst, an einem ruhigen Ort.",
            "image": {"src": "/screenshot-newtab.png", "alt": "Persim Neuer Tab"},
        },
        "actions": [
            {"text": "Kostenlos herunterladen", "link": STORE, "theme": "brand", "external": True},
            {"text": "Funktionen ansehen", "link": "/#features", "theme": "alt"},
        ],
        "downloadNote": "macOS 12 oder neuer · Apple Silicon und Intel",
        "features": [
            F("tabs", "Tabs, die mithalten", "Tabs öffnen, verschieben, gruppieren, stummschalten und in der Vorschau ansehen — wie du es gewohnt bist. Mit ⌘⇧A findest du einen Tab sofort."),
            F("shield", "Weniger Werbung, sauberere Seiten", "Integrierter Werbeblocker mit Abonnements, eigenen Regeln und einer Erlaubnisliste. Tabs stummschalten und Pop-ups blockieren geht mit einem Klick."),
            F("download", "Videos behalten, die dir gefallen", "Videos auf einer Seite erkennen und mit einem Klick speichern. Aufgeteilte Videos werden zu einer einzigen MP4 zusammengefügt."),
            F("ai", "Direkt zu deiner KI", "Tippe „ai + deine Frage“ in die Adressleiste und erreiche deine Lieblings-KI-Seiten. ChatGPT, Claude und mehr liegen im neuen Tab bereit."),
            F("book", "Angenehmer lesen", "Der Lesemodus entfernt Menüs und Werbung und lässt nur den Text. Dunkle Seiten, ganze Seiten als Bild und sauberes Drucken sind ebenfalls dabei."),
            F("palette", "Ganz nach deinem Geschmack", "Hell, dunkel oder Systemeinstellung; sechs Akzentfarben; drei Modi für die Lesezeichenleiste; 25 Oberflächensprachen."),
        ],
        "sections": {
            "featuresTitle": "Genau die richtige Menge Browser",
            "featuresSubtitle": "Kein Einrichtungszauber. Persim öffnen, suchen, surfen, speichern — fertig.",
            "shotsTitle": "Auf einen Blick",
            "shotsSubtitle": "Der neue Tab zeigt deine Lieblingsseiten. Die Einstellungen halten Design, Farbe und Sprache an einem Ort.",
            "accentTitle": "Akzentfarbe wählen",
            "accentSubtitle": "Wechsle über den Farbbutton in der oberen Leiste oder hier — die ganze Website folgt deiner Wahl.",
            "howTitle": "In drei Schritten entspannter surfen",
            "howSubtitle": "Vom Download bis zum Alltag dauert es nur wenige Minuten.",
            "faqTitle": "Häufige Fragen",
            "faqSubtitle": "Zu Download, Datenschutz und Alltag",
        },
        "banners": [{"title": "Tabs, die mithalten", "alt": "Persim neuer Tab Banner"}, {"title": "Mach es zu deinem", "alt": "Persim Einstellungen Banner"}, {"title": "Mehr aus deinem Browser", "alt": "Persim Userscripts Banner"}],
        "accentLabels": ["Persimmon", "Violett", "Türkis", "Grün", "Blau", "Rosé"],
        "steps": [
            {"num": "01", "title": "Installieren", "desc": "Aus dem Mac App Store herunterladen und in den Ordner „Programme“ ziehen. Kein Konto nötig."},
            {"num": "02", "title": "Lesezeichen mitnehmen", "desc": "Lesezeichen in Chrome oder Edge als HTML exportieren und im Persim-Lesezeichenmanager importieren."},
            {"num": "03", "title": "Nach Wunsch anpassen", "desc": "Design, Akzentfarbe und Sprache in den Einstellungen wählen. „Letzte Sitzung wiederherstellen“ öffnet deine Tabs erneut."},
        ],
        "faqs": [
            {"question": "Ist Persim kostenlos?", "answer": "Du kannst Persim kostenlos herunterladen und die grundlegenden Browserfunktionen nutzen. Einige erweiterte Funktionen gibt es per In-App-Kauf; die kostenlose Version zeigt ein kleines Abzeichen in der Tab-Leiste."},
            {"question": "Welche Macs werden unterstützt?", "answer": "macOS 12 oder neuer, sowohl Apple Silicon als auch Intel."},
            {"question": "Werden meine Verläufe hochgeladen?", "answer": "Nein. Verlauf, Lesezeichen, Sitzungen und Downloads bleiben auf deinem Mac. Nur Funktionen wie das Aktualisieren eines Werbeblocker-Abonnements benötigen das Netz."},
            {"question": "Wie importiere ich Chrome-Lesezeichen?", "answer": "Exportiere die Lesezeichen in Chrome als HTML-Datei und wähle im Persim-Lesezeichenmanager „HTML importieren“."},
            {"question": "Wie speichere ich ein Video von einer Seite?", "answer": "Öffne das Medienfenster, wähle ein erkanntes Video und lade es herunter. Aufgeteilte Videos werden zu einer MP4 zusammengefügt."},
        ],
        "faqMore": "Weitere Fragen →",
        "cta": {
            "title": "Etwas mehr Luft beim Surfen.",
            "description": "Lade Persim herunter und richte es genau so ein, wie du es magst.",
            "primary": "Im Mac App Store laden",
            "primaryLink": STORE,
            "secondary": "Anleitung lesen",
            "secondaryLink": "/guide/introduction",
        },
        "guides": {
            "introduction": G("Persim kennenlernen", "Ein Mac-Browser, der sofort loslegt: Tabs, Suche, Lesezeichen und Downloads.", """
## Von Anfang an

- **Surfen und Suchen.** URL oder Frage in die Adressleiste tippen. Oft besuchte Seiten erscheinen zuerst.
- **Tabs und Fenster.** Öffnen, ziehen, gruppieren, stummschalten, in der Vorschau ansehen. Mit ⌘⇧A findest du einen Tab schnell wieder.
- **Wiederfinden.** Lesezeichen, Lesezeichenleiste, Verlauf, Downloads und „Letzte Sitzung wiederherstellen“.

## Etwas ruhiger

- Werbeblocker mit Abonnements, eigenen Regeln und Erlaubnisliste für vertraute Seiten.
- Dunkle Seiten, stumme Tabs und Pop-up-Blocker in den Einstellungen.
- Ein privates Fenster (⌘⇧N) schreibt keinen Verlauf.

## Videos und lange Texte

- Das Medienfenster listet Videos auf der Seite. Gespeicherte Videos werden zu einer MP4 und lassen sich mit jeder App öffnen.
- Der Lesemodus (⌘⇧R) lässt nur den Artikel übrig. Screenshots und komplette Seiten als PDF sind ebenfalls möglich.

## Passend für dich

Hell, dunkel oder Systemeinstellung; sechs Akzentfarben; drei Lesezeichenleisten-Modi; 25 Oberflächensprachen. Design ändert sich sofort, eine Sprachänderung nach dem erneuten Öffnen des Fensters.
"""),
            "installation": G("Persim installieren", "Herunterladen, als Standardbrowser festlegen und Lesezeichen übernehmen.", """
## Download und Installation

1. Öffne den [Mac App Store](""" + STORE + """) und suche nach Persim.
2. Ziehe die App nach dem Download in den Ordner „Programme“.
3. Als Standardbrowser: **Systemeinstellungen → Standard-Webbrowser** → Persim wählen.

Erfordert macOS 12 oder neuer, auf Apple Silicon und Intel.

## Die erste Minute

- In `persim://settings` → **Allgemein** Design, Akzentfarbe und Lesezeichenleiste festlegen.
- 25 Oberflächensprachen sind verfügbar; die Änderung gilt nach dem erneuten Öffnen des Fensters.
- Der neue Tab enthält bereits beliebte Seiten und AI-Kürzel.

## Lesezeichen übernehmen

1. Lesezeichen in Chrome oder Edge als HTML-Datei exportieren.
2. Im Persim-Lesezeichenmanager **HTML importieren** wählen.
3. Verschachtelte Ordner bleiben erhalten, doppelte Adressen werden übersprungen.

## Aktualisieren

Neue Versionen gibt es im Bereich „Aktualisierungen“ des Mac App Store. Deine Daten bleiben erhalten.
"""),
            "features": G("Funktionen im Überblick", "Ein kurzer Rundgang durch das, was du am häufigsten nutzt.", """
## Täglich surfen

- Mehrere Tabs und Fenster: herausziehen, gruppieren, einklappen, stummschalten, Vorschau.
- Die Adressleiste schlägt zuerst bekannte Seiten vor und sucht sonst im Web.
- Befehlspalette (⌘K), Tabsuche (⌘⇧A), Finden auf der Seite (⌘F) und eine Tastenkürzel-Liste im Zahnradmenü.

## Angenehm für die Augen

- Design: System folgen, hell oder dunkel. Dunkle Seiten und automatischer Wechsel pro Tag sind möglich.
- Sechs Akzentfarben: Blau, Violett, Türkis, Grün, Orange und Rosé.
- Lesezeichenleiste: immer aus, immer an oder nur im neuen Tab.

## Werbung und Skripte

- Der Werbeblocker unterstützt Abonnements, eigene Regeln und eine Erlaubnisliste. Schlägt ein Update fehl, gelten die alten Regeln weiter.
- Benutzerskripte (`.user.js`) werden in den Einstellungen verwaltet und nach dem Download installiert.

## Videos und Dateien

- Downloads lassen sich pausieren, fortsetzen, abbrechen und wiederholen. Danach im Finder zeigen oder mit der zugehörigen App öffnen.
- Das Medienfenster erkennt Videos auf Seiten und fügt aufgeteilte Videos zu einer MP4 zusammen.

## Tastenkürzel

| Kürzel | Funktion |
| --- | --- |
| ⌘T / ⌘W | Tab öffnen / schließen |
| ⌘L | Adressleiste fokussieren |
| ⌘F | Auf der Seite suchen |
| ⌘⇧N | Privates Fenster |
| ⌘K | Befehlspalette |
| ⌘⇧A | Tabsuche |
| ⌘⇧R | Lesemodus |
"""),
            "faq": G("Häufige Fragen", "Kurze Antworten zu Persim.", """
### Ist Persim kostenlos?

Die grundlegenden Browserfunktionen sind kostenlos nutzbar. Einige erweiterte Funktionen gibt es per In-App-Kauf; die kostenlose Version zeigt ein kleines Abzeichen in der Tab-Leiste.

### Welche Betriebssysteme werden unterstützt?

Persim ist für macOS 12 oder neuer entwickelt und läuft auf Apple Silicon und Intel.

### Werden meine Daten hochgeladen?

Nein. Verlauf, Lesezeichen, Sitzungen und Downloads bleiben lokal, ein Konto ist nicht nötig. Nur Funktionen wie die Aktualisierung eines Werbeblocker-Abonnements nutzen das Netz.

### Wie übernehme ich Lesezeichen aus einem anderen Browser?

In Chrome oder Edge als HTML exportieren, dann im Persim-Lesezeichenmanager „HTML importieren“ wählen. Ordner und doppelte Links werden automatisch behandelt.

### Wie speichere ich ein Video?

Medienfenster öffnen, erkanntes Video auswählen und herunterladen. Aufgeteilte Videos werden zu einer MP4 zusammengefügt.

### Wie ändere ich die Sprache?

`persim://settings` → **Allgemein** → **Sprache**. 25 Sprachen stehen bereit; nach dem erneuten Öffnen des Fensters ist die Änderung sichtbar.

### Noch eine Frage?

Schreibe an **persim@w3cub.com** und beschreibe, was du tun möchtest.
"""),
            "privacy": G("Datenschutz und deine Daten", "Was auf deinem Mac bleibt und wann das Netz nötig ist.", """
## Lokal gespeichert

Verlauf, Lesezeichen, offene Tabs, Downloads und Cookies liegen auf deinem Mac. Es gibt kein Konto und keine Cloud-Synchronisierung. Ein privates Fenster (⌘⇧N) hinterlässt keine Spuren in Verlauf und Sitzung.

## Wann das Netz genutzt wird

- Natürlich beim Laden der Seiten, die du aufrufst.
- Beim Aktualisieren eines aktiven Werbeblocker-Abonnements. Schlägt das fehl, gelten die gespeicherten Regeln weiter.
- Beim Herunterladen eines Skripts oder einer Datei, die du angefordert hast.

## Deine Berechtigungen

Kamera und Mikrofon werden pro Seite gemerkt. Standort und Benachrichtigungen verwaltet macOS selbst. Pop-ups sind auf erlaubte Seiten beschränkt.

## Dateien auf der Platte

Persim liest nur Dateien, die du im Systemdialog auswählst oder ausdrücklich freigibst. Freigaben kannst du in den Einstellungen prüfen und widerrufen.

## Kontakt

Fragen zum Datenschutz: **persim@w3cub.com**.
"""),

            "troubleshooting": G("Fehlerbehebung", "Lösungen für häufige Probleme.", """
## Eine Seite lädt nicht

- Prüfe, ob andere Seiten funktionieren, und lade mit ⌘R neu.
- Wenn eine Werbeblockier-Liste aktiv ist, pausiere sie kurz, um zu sehen, ob sie die Seite blockiert.
- Versuche ein privates Fenster (⌘⇧N). Funktioniert die Seite dort, lösche die Cookies der Seite in den Einstellungen.

## Download bleibt hängen oder ist unvollständig

- Öffne das Download-Panel, pausiere den Vorgang und setze ihn fort.
- Lösche bei einem fehlgeschlagenen Video-Download die unvollständige Datei und versuche es erneut. Geteilte Videos werden zu einer MP4 zusammengefügt; bei einem Fehler bleiben die Teile im Download-Ordner.

## Lesezeichen wurden nicht importiert

Exportiere zuerst die Lesezeichen deines alten Browsers als HTML-Datei und wähle dann in Persim **HTML importieren** im Lesezeichen-Manager. Ordner und doppelte Links werden automatisch sortiert.

## Videos werden nicht erkannt

Nicht jede Website stellt eine speicherbare Videodatei bereit. Öffne das Medien-Panel auf der Seite. Wenn nichts erscheint, lässt sich das Video dort nicht direkt speichern.

## Die App ist langsam

Schließe nicht mehr benötigte Tabs oder deaktiviere ein Abo zur Werbeblockierung. Website-Berechtigungen kannst du in den Einstellungen prüfen.

## Immer noch kein Erfolg?

Schreibe an **persim@w3cub.com** und beschreibe, was du tun wolltest — am besten mit einem Screenshot.
"""),
            "legal": G("Rechtliches", "Rechtliche Hinweise zu Persim.", """
Persim wird von w3cub.com entwickelt und herausgegeben.

- [Datenschutzerklärung](./privacy-policy) — welche Daten verarbeitet werden.
- [Datenschutz-Optionen](./privacy-choices) — wie du Speicherung und Weitergabe kontrollierst.
- [Nutzungsbedingungen](./terms) — die Bedingungen für die Nutzung der App.

Fragen zu diesen Dokumenten: **persim@w3cub.com**.
"""),
            "privacy-policy": G("Datenschutzerklärung", "Was Persim erhebt und was auf deinem Gerät bleibt.", """
## Kein Konto, kein Cloud-Profil

Persim verlangt keine Anmeldung und erstellt kein Online-Konto. Verlauf, Lesezeichen, offene Tabs, Downloads und Cookies werden auf deinem Mac gespeichert.

## Informationen zum Anzeigen von Seiten

Wie jeder Browser sendet Persim die aufgerufenen Adressen an die jeweilige Website. Persim selbst lädt deinen Browserverlauf nicht auf einen Server hoch.

## Netzwerkfunktionen, die du einschalten kannst

- Abonnements zur Werbeblockierung aktualisieren ihre Regeln über das Netz. Schlägt die Aktualisierung fehl, wirken die gespeicherten Regeln weiter.
- Userscripts und Dateien werden nur heruntergeladen, wenn du es anforderst.
- Bei der Eingabe in der Adressleiste kommen Vorschläge von deiner gewählten Suchmaschine.

## Lokale Berechtigungen

Kamera, Mikrofon und Dateizugriff werden pro Website gemerkt und lassen sich in den Einstellungen ändern. Standort und Benachrichtigungen verwaltet macOS. Ein privates Fenster (⌘⇧N) hinterlässt keine Spuren in Verlauf und Sitzung.

## Websites Dritter

Die besuchten Websites werden von anderen betrieben und haben eigene Datenschutzregeln. Die integrierten Seiten von Persim verfolgen dich nicht.

## Kontakt

Datenschutzfragen: **persim@w3cub.com**.
"""),
            "privacy-choices": G("Datenschutz-Optionen", "Einfache Wege, die Kontrolle zu behalten.", """
## Surfen ohne Spuren

Nutze ein privates Fenster (⌘⇧N). Es schreibt nichts in den Verlauf, merkt sich keine Sitzung und seine Tabs verschwinden beim Schließen.

## Gespeichertes löschen

Entferne Cookies und Websitedaten über den Cookie-Manager in den Einstellungen. Verlauf und Downloads lassen sich dort ebenfalls löschen.

## Pro Website entscheiden

Kamera, Mikrofon und Dateizugriff werden pro Website gemerkt. Erlaube vertrauten Sites und lehne andere in den Einstellungen ab. Pop-ups öffnen sich nur auf erlaubten Sites.

## Hintergrundfunktionen steuern

Schalte Abonnements zur Werbeblockierung in den Einstellungen jederzeit ein oder aus. Ist eines aus, werden keine Regeln geladen.

## Suchmaschine wählen

Lege in den Einstellungen deine Standardsuchmaschine fest. Suchvorschläge stammen von der Engine deiner Wahl.

## Fragen

Schreibe an **persim@w3cub.com**, wenn du mehr über den Umgang mit deinen Daten wissen möchtest.
"""),
            "terms": G("Nutzungsbedingungen", "Die Bedingungen für die Nutzung von Persim.", """
## Nutzung der App

Persim ist für die persönliche Nutzung gedacht. Du darfst sie auf Macs herunterladen und verwenden, die dir gehören oder die du nutzen darfst.

## Kostenlose und kostenpflichtige Funktionen

Die grundlegenden Browserfunktionen sind kostenlos. Einige erweiterte Funktionen werden über einen In-App-Kauf freigeschaltet. Die kostenlose Version zeigt ein kleines Abzeichen in der Tab-Leiste; der Kauf entfernt es.

## Inhalte Dritter

Websites, Abonnements und Userscripts, die du über Persim nutzt, stammen von ihren jeweiligen Anbietern. Persim übernimmt keine Verantwortung für deren Inhalte oder Verfügbarkeit.

## Änderungen

Funktionen und diese Bedingungen können sich im Laufe der Zeit ändern. Maßgeblich ist die auf dieser Website veröffentlichte Version.

## Kontakt

Fragen zu diesen Bedingungen: **persim@w3cub.com**.
"""),
        },
    },
    "es": {
        "versionBadge": "Para Mac · Descarga gratuita",
        "hero": {
            "name": "Persim",
            "text": "Un navegador ligero y limpio",
            "tagline": "Pestañas, bloqueo de anuncios, guardado de vídeos, modo lectura y accesos a IA: todo lo que usas cada día, en un lugar tranquilo.",
            "image": {"src": "/screenshot-newtab.png", "alt": "Nueva pestaña de Persim"},
        },
        "actions": [
            {"text": "Descargar gratis", "link": STORE, "theme": "brand", "external": True},
            {"text": "Ver funciones", "link": "/#features", "theme": "alt"},
        ],
        "downloadNote": "macOS 12 o posterior · Apple Silicon e Intel",
        "features": [
            F("tabs", "Pestañas a tu ritmo", "Abre, arrastra, agrupa, silencia y previsualiza pestañas como siempre. Pulsa ⌘⇧A para encontrar una al instante."),
            F("shield", "Menos anuncios, páginas más limpias", "Bloqueo de anuncios integrado con suscripciones, reglas propias y lista de permitidos. Silencia pestañas o bloquea ventanas emergentes con un clic."),
            F("download", "Guarda los vídeos que te gustan", "Detecta vídeos en una página y guárdalos desde el panel. Los vídeos divididos se unen en un único MP4 y las descargas se pueden pausar y reanudar."),
            F("ai", "Pregunta a la IA sin rodeos", "Escribe «ai + tu pregunta» en la barra de direcciones para ir a tus sitios de IA favoritos. ChatGPT, Claude y otros están a un clic en la nueva pestaña."),
            F("book", "Leer textos largos con calma", "El modo lectura elimina menús y anuncios y deja solo el texto. También puedes forzar el modo oscuro, capturar la página entera e imprimir sin ruido."),
            F("palette", "Hazlo tuyo", "Claro, oscuro o según el sistema; seis colores de acento; tres modos de barra de marcadores; 25 idiomas de interfaz."),
        ],
        "sections": {
            "featuresTitle": "Justo lo que necesitas",
            "featuresSubtitle": "Sin asistentes de configuración. Abre Persim, busca, navega y guarda. Así de fácil.",
            "shotsTitle": "Échale un vistazo",
            "shotsSubtitle": "La nueva pestaña muestra tus sitios habituales. Los ajustes reúnen tema, color e idioma en un mismo lugar.",
            "accentTitle": "Elige tu color de acento",
            "accentSubtitle": "Cambia el color desde el botón de la barra superior o aquí: todo el sitio te sigue.",
            "howTitle": "Tres pasos para navegar mejor",
            "howSubtitle": "De la descarga al uso diario solo tardas unos minutos.",
            "faqTitle": "Preguntas frecuentes",
            "faqSubtitle": "Sobre descargas, privacidad y uso diario",
        },
        "banners": [{"title": "Pestañas que siguen tu ritmo", "alt": "Banner de la nueva pestaña de Persim"}, {"title": "Hazlo tuyo", "alt": "Banner de ajustes de Persim"}, {"title": "Potencia tu navegador", "alt": "Banner de userscripts de Persim"}],
        "accentLabels": ["Persimón", "Violeta", "Turquesa", "Verde", "Azul", "Rosa"],
        "steps": [
            {"num": "01", "title": "Instálalo", "desc": "Descárgalo de Mac App Store y arrástralo a Aplicaciones. No hace falta crear una cuenta."},
            {"num": "02", "title": "Trae tus marcadores", "desc": "Exporta los marcadores a HTML desde Chrome o Edge e impórtalos en el gestor de marcadores de Persim."},
            {"num": "03", "title": "Ajústalo a tu gusto", "desc": "Elige tema, color e idioma en Ajustes. Activa «Restaurar la última sesión» para recuperar tus pestañas."},
        ],
        "faqs": [
            {"question": "¿Persim es gratis?", "answer": "Puedes descargarlo gratis y usar las funciones básicas de navegación. Algunas funciones avanzadas se desbloquean con una compra integrada; la versión gratuita muestra una pequeña insignia en la barra de pestañas."},
            {"question": "¿Qué Macs son compatibles?", "answer": "macOS 12 o posterior, en Macs con Apple Silicon e Intel."},
            {"question": "¿Se sube mi historial?", "answer": "No. El historial, los marcadores, las sesiones y las descargas permanecen en tu Mac y no hace falta cuenta. Solo funciones como actualizar una suscripción de bloqueo necesitan Internet."},
            {"question": "¿Cómo importo los marcadores de Chrome?", "answer": "Exporta los marcadores a un archivo HTML en Chrome y elige «Importar HTML» en el gestor de marcadores de Persim."},
            {"question": "¿Cómo guardo un vídeo de una página?", "answer": "Abre el panel de multimedia, elige un vídeo detectado y descárgalo. Los vídeos divididos se unen en un solo MP4."},
        ],
        "faqMore": "Más preguntas →",
        "cta": {
            "title": "Un poco más de espacio al navegar.",
            "description": "Descarga Persim y configúralo exactamente como te gusta.",
            "primary": "Descargar en Mac App Store",
            "primaryLink": STORE,
            "secondary": "Leer la guía",
            "secondaryLink": "/guide/introduction",
        },
        "guides": {
            "introduction": G("Qué es Persim", "Un navegador para Mac listo desde el primer momento: pestañas, búsqueda, marcadores y descargas.", """
## Desde el primer clic

- **Navegar y buscar.** Escribe una dirección o una pregunta en la barra. Los sitios que más visitas aparecen primero.
- **Pestañas y ventanas.** Abre, arrastra, agrupa, silencia y previsualiza. Pulsa ⌘⇧A para encontrar una pestaña.
- **Volver a encontrar.** Marcadores, barra de marcadores, historial, descargas y «Restaurar la última sesión».

## Un poco más tranquilo

- Bloqueo de anuncios con suscripciones, reglas propias y lista de permitidos.
- Fuerza el modo oscuro en páginas, silencia pestañas y bloquea ventanas emergentes desde Ajustes.
- Una ventana privada (⌘⇧N) no guarda el historial.

## Vídeos y textos largos

- El panel multimedia muestra los vídeos de la página; al guardarlos obtienes un MP4 que puedes abrir con la app que quieras.
- El modo lectura (⌘⇧R) conserva el artículo y quita el ruido. Puedes capturar lo que ves o la página completa en PDF.

## A tu manera

Claro, oscuro o según el sistema; seis colores de acento; tres modos de barra de marcadores; 25 idiomas. El aspecto cambia al instante; el idioma se aplica al volver a abrir la ventana.
"""),
            "installation": G("Instalar Persim", "Descárgalo, ponlo como predeterminado y trae tus marcadores.", """
## Descarga e instalación

1. Abre la [Mac App Store](""" + STORE + """) y busca Persim.
2. Tras descargarlo, arrastra la app a la carpeta Aplicaciones.
3. Para hacerlo predeterminado: **Ajustes del sistema → Navegador web predeterminado** → Persim.

Necesita macOS 12 o posterior, en Apple Silicon e Intel.

## Tu primer minuto

- En `persim://settings` → **General**, elige aspecto, color y barra de marcadores.
- Hay 25 idiomas; el cambio se aplica al volver a abrir la ventana.
- La nueva pestaña ya incluye sitios populares y accesos a IA.

## Traer tus marcadores

1. Exporta los marcadores a HTML desde Chrome o Edge.
2. En el gestor de marcadores de Persim, elige **Importar HTML**.
3. Las carpetas anidadas se restauran y las URL duplicadas se omiten.

## Actualizaciones

Consigue las nuevas versiones en la pestaña «Actualizaciones» de Mac App Store. Tus datos se conservan.
"""),
            "features": G("Recorrido de funciones", "Lo que más usarás, explicado en breve.", """
## Navegación diaria

- Varias pestañas y ventanas: arrastrar, agrupar, plegar, silenciar y previsualizar.
- La barra de direcciones sugiere primero los sitios conocidos y luego busca en la web.
- Paleta de comandos (⌘K), búsqueda de pestañas (⌘⇧A), buscar en la página (⌘F) y lista de atajos en el menú del engranaje.

## Cómodo a la vista

- Tema: seguir el sistema, claro u oscuro. También puedes forzar páginas oscuras y cambiar de tema cada día.
- Seis colores de acento: azul, violeta, turquesa, verde, naranja y rosa.
- Barra de marcadores: siempre oculta, siempre visible o solo en la nueva pestaña.

## Anuncios y scripts

- El bloqueador admite suscripciones, reglas propias y lista de permitidos. Si falla una actualización, siguen rigiendo las reglas anteriores.
- Los scripts de usuario (`.user.js`) se gestionan en Ajustes y se instalan al terminar la descarga.

## Vídeos y archivos

- Las descargas se pueden pausar, reanudar, cancelar y reintentar. Al terminar, muestra el archivo en Finder o ábrelo con la app relacionada.
- El panel multimedia reconoce vídeos en la página y une las partes en un solo MP4.

## Atajos

| Atajo | Acción |
| --- | --- |
| ⌘T / ⌘W | Nueva / cerrar pestaña |
| ⌘L | Ir a la barra de direcciones |
| ⌘F | Buscar en la página |
| ⌘⇧N | Ventana privada |
| ⌘K | Paleta de comandos |
| ⌘⇧A | Buscar pestañas |
| ⌘⇧R | Modo lectura |
"""),
            "faq": G("Preguntas frecuentes", "Respuestas rápidas sobre Persim.", """
### ¿Es gratis?

Puedes descargarlo y usar las funciones básicas sin pagar. Algunas funciones avanzadas se desbloquean con una compra integrada, y la versión gratuita muestra una pequeña insignia en la barra de pestañas.

### ¿Qué sistemas operativos son compatibles?

Persim está pensado para macOS 12 o posterior y funciona en Macs con Apple Silicon e Intel.

### ¿Se suben mis datos?

No hace falta cuenta: el historial, los marcadores, las sesiones y las descargas se quedan en tu Mac. Solo las funciones que necesitan red —como actualizar una suscripción— se conectan a Internet.

### ¿Cómo importo marcadores de otro navegador?

Exporta los marcadores a HTML desde Chrome o Edge y usa «Importar HTML» en el gestor de marcadores de Persim. Las carpetas y los enlaces duplicados se tratan automáticamente.

### ¿Cómo guardo un vídeo?

Abre el panel multimedia, elige un vídeo detectado y descárgalo. Las partes se unen en un MP4 que puedes abrir con tu aplicación habitual.

### ¿Cómo cambio el idioma?

Ve a `persim://settings` → **General** → **Idioma**. Hay 25 idiomas; vuelve a abrir la ventana para ver el cambio.

### ¿Más preguntas?

Escribe a **persim@w3cub.com** y cuéntanos qué querías hacer.
"""),
            "privacy": G("Privacidad y tus datos", "Qué se queda en tu Mac y cuándo hace falta la red.", """
## Guardado en tu Mac

El historial, los marcadores, las pestañas abiertas, las descargas y las cookies se guardan localmente. No hay cuenta ni sincronización en la nube. Una ventana privada (⌘⇧N) no deja historial ni sesión.

## Cuándo se usa la red

- Al cargar los sitios que visitas, por supuesto.
- Al actualizar una suscripción de bloqueo de anuncios, si está activada. Si falla, las reglas guardadas siguen funcionando.
- Al descargar un script o un archivo que hayas pedido.

## Tus permisos

El acceso a cámara y micrófono se recuerda por sitio. La ubicación y las notificaciones las controla macOS. Las ventanas emergentes se limitan a los sitios que permites.

## Archivos en disco

Persim solo lee archivos que eliges en el diálogo del sistema o a los que das acceso explícitamente. Puedes revisar y revocar esos permisos en Ajustes.

## Contacto

Preguntas sobre privacidad: **persim@w3cub.com**.
"""),

            "troubleshooting": G("Solución de problemas", "Soluciones para los inconvenientes más comunes.", """
## Una página no carga

- Comprueba que otras páginas sí abran y vuelve a cargar con ⌘R.
- Si tienes activa una lista de bloqueo de anuncios, pausálа un momento para ver si está bloqueando el sitio.
- Prueba una ventana privada (⌘⇧N). Si allí funciona, borra las cookies del sitio desde los ajustes.

## Una descarga se queda atascada o incompleta

- Abre el panel de descargas, pausa el elemento y reanúdalo.
- Si falla un vídeo guardado desde una página, borra el archivo incompleto e inténtalo de nuevo. Los vídeos divididos se unen en un solo MP4; si falla la unión, las partes originales quedan en la carpeta de descargas.

## No se importaron los marcadores

Primero exporta los marcadores de tu navegador anterior a un archivo HTML. Después, en Persim, abre el gestor de marcadores y elige **Importar HTML**. Las carpetas y los enlaces duplicados se ordenan automáticamente.

## No se detectan vídeos

No todos los sitios ofrecen un archivo de vídeo guardable. Abre el panel de medios en la página; si no aparece nada, el sitio puede usar un tipo de reproducción que no se puede guardar directamente.

## La app va lenta

Cierra las pestañas que no uses o desactiva una suscripción de bloqueo que ya no necesites. Los permisos de los sitios se revisan en los ajustes.

## Sigues sin solución

Escribe a **persim@w3cub.com** y cuéntanos qué intentabas hacer; si puedes, adjunta una captura.
"""),
            "legal": G("Información legal", "Información legal de Persim.", """
Persim es desarrollado y publicado por w3cub.com.

- [Política de privacidad](./privacy-policy) — qué datos se tratan y cómo.
- [Opciones de privacidad](./privacy-choices) — cómo controlar lo que se guarda y comparte.
- [Términos del servicio](./terms) — las condiciones de uso de la app.

Consultas sobre estos documentos: **persim@w3cub.com**.
"""),
            "privacy-policy": G("Política de privacidad", "Qué recopila Persim y qué permanece en tu dispositivo.", """
## Sin cuenta, sin perfil en la nube

Persim no te pide iniciar sesión ni crea una cuenta en línea. El historial, los marcadores, las pestañas abiertas, las descargas y las cookies se guardan en tu Mac.

## Información para mostrar páginas

Como cualquier navegador, Persim envía las direcciones que visitas a los sitios que abres. Persim no sube tu historial de navegación a ningún servidor.

## Funciones de red que puedes activar

- Las suscripciones de bloqueo de anuncios actualizan sus listas por la red. Si falla la actualización, la lista guardada sigue funcionando.
- Los userscripts y los archivos que descargas se obtienen solo cuando lo pides.
- Al escribir en la barra de direcciones, las sugerencias llegan del motor de búsqueda elegido.

## Permisos locales

La cámara, el micrófono y el acceso a archivos se recuerdan por sitio y se pueden cambiar en los ajustes. La ubicación y las notificaciones las controla macOS. Una ventana privada (⌘⇧N) no deja rastro en el historial ni en la sesión.

## Sitios de terceros

Los sitios que visitas son operados por otros y siguen sus propias políticas de privacidad. Las páginas integradas de Persim no te rastrean.

## Contacto

Preguntas sobre privacidad: **persim@w3cub.com**.
"""),
            "privacy-choices": G("Opciones de privacidad", "Formas sencillas de mantener el control.", """
## Navegar sin dejar rastro

Usa una ventana privada (⌘⇧N). No escribe en el historial ni recuerda la sesión, y sus pestañas desaparecen al cerrarla.

## Borrar lo guardado

Elimina las cookies y los datos de sitios desde el gestor de cookies de los ajustes. El historial y las descargas también se pueden borrar allí.

## Decide qué puede hacer cada sitio

La cámara, el micrófono y el acceso a archivos se recuerdan por sitio. Permite los que confías y rechaza los demás en los ajustes. Las ventanas emergentes solo se abren en los sitios que autorices.

## Controla las funciones en segundo plano

Activa o desactiva las suscripciones de bloqueo cuando quieras desde los ajustes. Si una está desactivada, no se descarga ninguna lista.

## Elige tu motor de búsqueda

Establece tu motor predeterminado en los ajustes. Las sugerencias provienen del motor que elijas.

## ¿Dudas?

Escribe a **persim@w3cub.com** si quieres saber más sobre cómo se tratan tus datos.
"""),
            "terms": G("Términos del servicio", "Las condiciones para usar Persim.", """
## Uso de la app

Persim se ofrece para uso personal. Puedes descargarlo y usarlo en Macs que te pertenezcan o que estés autorizado a usar.

## Funciones gratuitas y de pago

Las funciones básicas de navegación son gratuitas. Algunas capacidades avanzadas se desbloquean con una compra integrada. La versión gratuita muestra una pequeña insignia en la barra de pestañas; la compra la elimina.

## Contenido de terceros

Los sitios, suscripciones y userscripts que usas a través de Persim son proporcionados por sus propios autores. Persim no se hace responsable de su contenido ni de su disponibilidad.

## Cambios

Las funciones y estos términos pueden cambiar con el tiempo. La versión publicada en este sitio es la vigente.

## Contacto

Consultas sobre estos términos: **persim@w3cub.com**.
"""),
        },
    },
    "fr": {
        "versionBadge": "Pour Mac · Téléchargement gratuit",
        "hero": {
            "name": "Persim",
            "text": "Un navigateur léger et clair",
            "tagline": "Onglets, blocage des publicités, enregistrement de vidéos, mode lecture et accès IA : tout ce que vous utilisez chaque jour, au même endroit.",
            "image": {"src": "/screenshot-newtab.png", "alt": "Nouvel onglet Persim"},
        },
        "actions": [
            {"text": "Télécharger gratuitement", "link": STORE, "theme": "brand", "external": True},
            {"text": "Voir les fonctions", "link": "/#features", "theme": "alt"},
        ],
        "downloadNote": "macOS 12 ou supérieur · Apple Silicon et Intel",
        "features": [
            F("tabs", "Des onglets faciles à vivre", "Ouvrez, déplacez, regroupez, coupez le son et prévisualisez vos onglets comme d'habitude. ⌘⇧A pour retrouver le bon instantanément."),
            F("shield", "Moins de pubs, des pages plus propres", "Bloqueur d'annonces intégré avec abonnements, règles personnelles et liste blanche. Coupez le son d'un onglet ou bloquez les fenêtres surgissantes en un clic."),
            F("download", "Gardez les vidéos qui vous plaisent", "Repérez une vidéo sur une page et enregistrez-la en un clic. Les vidéos fragmentées sont réunies en un seul MP4, et les téléchargements peuvent être mis en pause."),
            F("ai", "Posez votre question à l'IA", "Saisissez « ai + votre question » dans la barre d'adresse pour rejoindre vos sites d'IA préférés. ChatGPT, Claude et d'autres sont à portée de clic dans le nouvel onglet."),
            F("book", "Lire plus agréablement", "Le mode lecture retire les menus et les publicités pour ne garder que le texte. Forcer le mode sombre, capturer toute la page et imprimer proprement sont aussi là."),
            F("palette", "À votre image", "Clair, sombre ou selon le système ; six couleurs d'accent ; trois modes de barre de favoris ; 25 langues d'interface."),
        ],
        "sections": {
            "featuresTitle": "Exactement ce qu'il faut",
            "featuresSubtitle": "Aucun assistant de configuration. Ouvrez Persim, cherchez, naviguez, enregistrez — c'est tout.",
            "shotsTitle": "Un coup d'œil suffit",
            "shotsSubtitle": "Le nouvel onglet affiche vos sites favoris. Les réglages réunissent thème, couleur et langue au même endroit.",
            "accentTitle": "Choisissez votre couleur",
            "accentSubtitle": "Changez la couleur depuis le bouton de la barre supérieure ou ici : tout le site vous suit.",
            "howTitle": "Trois étapes pour naviguer sereinement",
            "howSubtitle": "Du téléchargement à l'usage quotidien, quelques minutes suffisent.",
            "faqTitle": "Questions fréquentes",
            "faqSubtitle": "Téléchargement, confidentialité et usage courant",
        },
        "banners": [{"title": "Des onglets qui suivent", "alt": "Bannière du nouvel onglet Persim"}, {"title": "À votre image", "alt": "Bannière des réglages Persim"}, {"title": "Boostez votre navigateur", "alt": "Bannière des scripts utilisateur Persim"}],
        "accentLabels": ["Persimmon", "Violet", "Sarcelle", "Vert", "Bleu", "Rose"],
        "steps": [
            {"num": "01", "title": "Installez-le", "desc": "Téléchargez depuis le Mac App Store et glissez l'app dans Applications. Aucun compte requis."},
            {"num": "02", "title": "Apportez vos favoris", "desc": "Exportez vos favoris au format HTML depuis Chrome ou Edge, puis importez-les dans le gestionnaire de favoris de Persim."},
            {"num": "03", "title": "Réglez-le à votre goût", "desc": "Choisissez thème, couleur et langue dans les réglages. Activez « Restaurer la dernière session » pour retrouver vos onglets."},
        ],
        "faqs": [
            {"question": "Persim est-il gratuit ?", "answer": "Vous pouvez le télécharger gratuitement et utiliser les fonctions de navigation de base. Certaines fonctions avancées sont débloquées par un achat intégré ; la version gratuite affiche un petit badge dans la barre d'onglets."},
            {"question": "Quels Mac sont compatibles ?", "answer": "macOS 12 ou supérieur, sur les Mac Apple Silicon et Intel."},
            {"question": "Mon historique est-il envoyé en ligne ?", "answer": "Non. Historique, favoris, sessions et téléchargements restent sur votre Mac, sans compte. Seules les fonctions qui en ont besoin — comme la mise à jour d'un abonnement de blocage — utilisent le réseau."},
            {"question": "Comment importer les favoris de Chrome ?", "answer": "Exportez les favoris au format HTML dans Chrome, puis choisissez « Importer HTML » dans le gestionnaire de favoris de Persim."},
            {"question": "Comment enregistrer une vidéo d'une page ?", "answer": "Ouvrez le panneau médias, choisissez une vidéo détectée et téléchargez-la. Les vidéos fragmentées sont réunies en un seul MP4."},
        ],
        "faqMore": "Plus de questions →",
        "cta": {
            "title": "Un peu plus d'air pour naviguer.",
            "description": "Téléchargez Persim et réglez-le exactement comme vous l'aimez.",
            "primary": "Télécharger sur le Mac App Store",
            "primaryLink": STORE,
            "secondary": "Lire le guide",
            "secondaryLink": "/guide/introduction",
        },
        "guides": {
            "introduction": G("Découvrir Persim", "Un navigateur Mac prêt à l'emploi : onglets, recherche, favoris et téléchargements.", """
## Dès le premier clic

- **Naviguer et chercher.** Saisissez une adresse ou une question dans la barre. Les sites fréquentés apparaissent en premier.
- **Onglets et fenêtres.** Ouvrez, déplacez, regroupez, coupez le son et prévisualisez. ⌘⇧A retrouve un onglet rapidement.
- **Retrouver ses pages.** Favoris, barre de favoris, historique, téléchargements et « Restaurer la dernière session ».

## Plus de calme

- Blocage des publicités avec abonnements, règles personnelles et liste blanche.
- Forcer le mode sombre sur les pages, couper le son d'un onglet et bloquer les fenêtres surgissantes depuis les réglages.
- Une fenêtre privée (⌘⇧N) n'écrit pas d'historique.

## Vidéos et longs textes

- Le panneau médias liste les vidéos de la page ; une fois enregistrées, elles forment un MP4 que vous ouvrez avec l'app de votre choix.
- Le mode lecture (⌘⇧R) ne garde que l'article. Capturez l'écran ou la page entière en PDF.

## À votre façon

Clair, sombre ou selon le système ; six couleurs d'accent ; trois modes de barre de favoris ; 25 langues. L'apparence change immédiatement, la langue après réouverture de la fenêtre.
"""),
            "installation": G("Installer Persim", "Téléchargez, définissez comme navigateur par défaut et importez vos favoris.", """
## Téléchargement et installation

1. Ouvrez le [Mac App Store](""" + STORE + """) et cherchez Persim.
2. Après le téléchargement, glissez l'app dans le dossier Applications.
3. Pour en faire votre navigateur par défaut : **Réglages système → Navigateur web par défaut** → Persim.

Nécessite macOS 12 ou supérieur, sur Apple Silicon et Intel.

## Votre première minute

- Dans `persim://settings` → **Général**, choisissez l'apparence, la couleur et la barre de favoris.
- 25 langues sont disponibles ; le changement s'applique après réouverture de la fenêtre.
- Le nouvel onglet contient déjà des sites populaires et des accès IA.

## Importer vos favoris

1. Exportez vos favoris au format HTML depuis Chrome ou Edge.
2. Dans le gestionnaire de favoris de Persim, choisissez **Importer HTML**.
3. Les dossiers imbriqués sont restaurés et les adresses en double ignorées.

## Mises à jour

Les nouvelles versions arrivent via l'onglet « Mises à jour » du Mac App Store. Vos données restent en place.
"""),
            "features": G("Tour des fonctionnalités", "Un aperçu rapide de ce que vous utilisez le plus.", """
## Navigation quotidienne

- Plusieurs onglets et fenêtres : détacher, regrouper, replier, couper le son, prévisualiser.
- La barre d'adresse propose d'abord les sites connus, puis lance une recherche.
- Palette de commandes (⌘K), recherche d'onglets (⌘⇧A), recherche dans la page (⌘F) et liste des raccourcis dans le menu engrenage.

## Confort visuel

- Thème : suivre le système, clair ou sombre. Forcer les pages sombres et changer de thème chaque jour est possible.
- Six couleurs d'accent : bleu, violet, sarcelle, vert, orange et rose.
- Barre de favoris : toujours masquée, toujours visible ou uniquement dans le nouvel onglet.

## Publicités et scripts

- Le bloqueur gère abonnements, règles personnelles et liste blanche. Si une mise à jour échoue, les anciennes règles restent actives.
- Les scripts utilisateur (`.user.js`) se gèrent dans les réglages et s'installent dès la fin du téléchargement.

## Vidéos et fichiers

- Les téléchargements peuvent être mis en pause, repris, annulés et relancés. Ensuite, affichez le fichier dans le Finder ou ouvrez-le avec l'app associée.
- Le panneau médias reconnaît les vidéos d'une page et réunit les fragments en un seul MP4.

## Raccourcis

| Raccourci | Action |
| --- | --- |
| ⌘T / ⌘W | Nouvel onglet / fermer |
| ⌘L | Aller à la barre d'adresse |
| ⌘F | Rechercher dans la page |
| ⌘⇧N | Fenêtre privée |
| ⌘K | Palette de commandes |
| ⌘⇧A | Rechercher un onglet |
| ⌘⇧R | Mode lecture |
"""),
            "faq": G("Questions fréquentes", "Des réponses rapides sur Persim.", """
### Persim est-il gratuit ?

Les fonctions de navigation de base sont gratuites. Certaines fonctions avancées sont débloquées par un achat intégré ; la version gratuite affiche un petit badge dans la barre d'onglets.

### Quels systèmes sont compatibles ?

Persim est conçu pour macOS 12 ou supérieur, sur Apple Silicon et Intel.

### Mes données sont-elles envoyées ?

Aucun compte n'est nécessaire : historique, favoris, sessions et téléchargements restent sur votre Mac. Seules les fonctions qui nécessitent le réseau — comme la mise à jour d'un abonnement — se connectent à Internet.

### Comment importer les favoris d'un autre navigateur ?

Exportez-les au format HTML depuis Chrome ou Edge, puis utilisez « Importer HTML » dans le gestionnaire de Persim. Dossiers et liens en double sont traités automatiquement.

### Comment enregistrer une vidéo ?

Ouvrez le panneau médias, sélectionnez une vidéo détectée et téléchargez-la. Les fragments sont réunis en un MP4 que vous ouvrez avec votre application habituelle.

### Comment changer de langue ?

Ouvrez `persim://settings` → **Général** → **Langue**. 25 langues sont proposées ; rouvrez la fenêtre pour voir le changement.

### Une autre question ?

Écrivez à **persim@w3cub.com** en expliquant ce que vous souhaitez faire.
"""),
            "privacy": G("Confidentialité et données", "Ce qui reste sur votre Mac et quand le réseau est nécessaire.", """
## Enregistré localement

Historique, favoris, onglets ouverts, téléchargements et cookies sont conservés sur votre Mac. Pas de compte, pas de synchronisation cloud. Une fenêtre privée (⌘⇧N) ne laisse ni historique ni session.

## Quand le réseau est utilisé

- Pour charger les sites que vous visitez, évidemment.
- Pour actualiser un abonnement de blocage d'annonces, s'il est actif. Si la mise à jour échoue, les règles enregistrées continuent de s'appliquer.
- Pour télécharger un script ou un fichier que vous avez demandé.

## Vos autorisations

L'accès à la caméra et au micro est mémorisé par site. La localisation et les notifications sont gérées par macOS. Les fenêtres surgissantes sont limitées aux sites autorisés.

## Fichiers sur le disque

Persim ne lit que les fichiers choisis dans le dialogue système ou auxquels vous avez donné accès explicitement. Vous pouvez vérifier et révoquer ces autorisations dans les réglages.

## Contact

Questions de confidentialité : **persim@w3cub.com**.
"""),

            "troubleshooting": G("Dépannage", "Des solutions aux problèmes les plus courants.", """
## Une page ne s'ouvre pas

- Vérifiez que d'autres sites s'ouvrent, puis rechargez avec ⌘R.
- Si un filtre de publicités est actif, mettez-le en pause un instant pour voir s'il bloque le site.
- Essayez une fenêtre privée (⌘⇧N). Si la page s'ouvre là, supprimez les cookies du site depuis les réglages.

## Un téléchargement bloque ou reste incomplet

- Ouvrez le panneau de téléchargement, mettez l'élément en pause, puis reprenez.
- Si une vidéo enregistrée depuis une page a échoué, supprimez le fichier incomplet et réessayez. Les vidéos fractionnées sont assemblées en un seul MP4 ; en cas d'échec, les morceaux restent dans le dossier de téléchargements.

## Les favoris ne se sont pas importés

Exportez d'abord les favoris de votre ancien navigateur au format HTML. Dans Persim, ouvrez le gestionnaire de favoris et choisissez **Importer HTML**. Dossiers et liens en double sont triés automatiquement.

## Aucune vidéo détectée

Tous les sites ne proposent pas une vidéo enregistrable. Ouvrez le panneau multimédia sur la page concernée. Si rien n'apparaît, le mode de lecture du site ne permet pas un enregistrement direct.

## L'application ralentit

Fermez les onglets inutilisés ou désactivez un abonnement de filtrage dont vous n'avez plus besoin. Les autorisations des sites se vérifient dans les réglages.

## Toujours aucun résultat

Écrivez à **persim@w3cub.com** en décrivant ce que vous faisiez ; si possible, joignez une capture d'écran.
"""),
            "legal": G("Mentions légales", "Informations légales sur Persim.", """
Persim est développé et publié par w3cub.com.

- [Politique de confidentialité](./privacy-policy) — quelles données sont traitées et comment.
- [Choix de confidentialité](./privacy-choices) — comment contrôler ce qui est stocké et partagé.
- [Conditions d'utilisation](./terms) — les conditions d'utilisation de l'application.

Questions sur ces documents : **persim@w3cub.com**.
"""),
            "privacy-policy": G("Politique de confidentialité", "Ce que Persim collecte et ce qui reste sur votre appareil.", """
## Aucun compte, aucun profil dans le cloud

Persim ne demande pas de connexion et ne crée pas de compte en ligne. Historique, favoris, onglets ouverts, téléchargements et cookies sont enregistrés sur votre Mac.

## Informations nécessaires à l'affichage des pages

Comme tout navigateur, Persim envoie les adresses visitées aux sites que vous ouvrez. Persim n'envoie pas votre historique de navigation à un serveur.

## Fonctions réseau que vous pouvez activer

- Les abonnements de filtrage mettent à jour leurs listes via le réseau. Si la mise à jour échoue, la liste enregistrée continue de fonctionner.
- Les scripts utilisateur et les fichiers ne sont téléchargés qu'à votre demande.
- Lors de la saisie dans la barre d'adresse, les suggestions proviennent du moteur de recherche choisi.

## Autorisations locales

Caméra, micro et accès aux fichiers sont mémorisés par site et modifiables dans les réglages. La localisation et les notifications sont gérées par macOS. Une fenêtre privée (⌘⇧N) ne laisse aucune trace dans l'historique ni la session.

## Sites tiers

Les sites que vous visitez sont exploités par d'autres et suivent leurs propres règles de confidentialité. Les pages intégrées de Persim ne vous suivent pas.

## Contact

Questions sur la confidentialité : **persim@w3cub.com**.
"""),
            "privacy-choices": G("Choix de confidentialité", "Des moyens simples de garder le contrôle.", """
## Naviguer sans traces

Utilisez une fenêtre privée (⌘⇧N). Elle n'écrit rien dans l'historique, ne mémorise pas la session, et ses onglets disparaissent à la fermeture.

## Effacer ce qui est enregistré

Supprimez les cookies et les données de sites depuis le gestionnaire de cookies des réglages. L'historique et les téléchargements peuvent aussi être effacés au même endroit.

## Décider ce que chaque site peut faire

Caméra, micro et accès aux fichiers sont mémorisés par site. Autorisez les sites de confiance et refusez les autres dans les réglages. Les fenêtres surgissantes ne s'ouvrent que sur les sites autorisés.

## Contrôler les fonctions en arrière-plan

Activez ou désactivez les abonnements de filtrage à tout moment depuis les réglages. Désactivé, aucun filtre n'est téléchargé.

## Choisir votre moteur de recherche

Définissez votre moteur par défaut dans les réglages. Les suggestions proviennent du moteur choisi.

## Une question

Écrivez à **persim@w3cub.com** pour en savoir plus sur le traitement de vos données.
"""),
            "terms": G("Conditions d'utilisation", "Les conditions d'utilisation de Persim.", """
## Utilisation de l'application

Persim est proposé pour un usage personnel. Vous pouvez le télécharger et l'utiliser sur les Mac qui vous appartiennent ou que vous êtes autorisé à utiliser.

## Fonctions gratuites et payantes

Les fonctions de navigation essentielles sont gratuites. Certaines capacités avancées sont débloquées par un achat intégré. La version gratuite affiche un petit badge dans la barre d'onglets ; l'achat le supprime.

## Contenus tiers

Les sites, abonnements et scripts utilisateur que vous utilisez via Persim sont fournis par leurs auteurs respectifs. Persim n'est pas responsable de leur contenu ni de leur disponibilité.

## Modifications

Les fonctions et les présentes conditions peuvent évoluer avec le temps. La version publiée sur ce site fait foi.

## Contact

Questions sur ces conditions : **persim@w3cub.com**.
"""),
        },
    },
}


def quote(value):
    # JSON strings are valid YAML double-quoted scalars and handle escapes.
    return json.dumps(value, ensure_ascii=False)


def write_frontmatter(path, fields):
    lines = ["---"]
    for key, value in fields.items():
        lines.append(f"{key}: {quote(value)}")
    lines += ["---", ""]
    path.write_text("\n".join(lines), encoding="utf-8")


def generate():
    for lang, data in DATA.items():
        base = ROOT if lang == "en" else ROOT / lang
        (base / "guide").mkdir(parents=True, exist_ok=True)

        homepage = {k: data[k] for k in (
            "versionBadge", "hero", "actions", "downloadNote", "features",
            "sections", "banners", "accentLabels", "steps", "faqs", "faqMore", "cta",
        )}
        homepage["layout"] = "home"
        write_frontmatter(base / "index.md", homepage)

        for name, guide in data["guides"].items():
            body = f"# {guide['title']}\n\n{guide['summary']}\n\n{guide['body']}\n"
            (base / "guide" / f"{name}.md").write_text(body, encoding="utf-8")

        print(f"{lang}: homepage + {len(data['guides'])} guides")


if __name__ == "__main__":
    generate()
