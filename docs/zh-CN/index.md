---
layout: home

hero:
  name: "Reminder"
  text: "与你一同成长的提醒"
  tagline: "一款安静、本地优先的 macOS 提醒应用——还有一位会留意你按时完成的小陪伴。设个提醒、完成它，看着你的宠物慢慢茁壮。"
  image:
    src: /hero-illustration.jpg
    alt: Reminder —— macOS 上的提醒事项与桌面宠物伴侣
  actions:
    - theme: brand
      text: 快速开始
      link: /guide/introduction
    - theme: alt
      text: 下载
      link: /guide/installation

versionBadge: "版本 2.0.0 · 从零重构"

features:
  - icon:
      light: /icons/eye.svg
      dark: /icons/eye-dark.svg
      alt: Eye
      width: "24"
      height: "24"
    title: 设置真正贴合日常节奏的提醒
    details: 一次性与重复提醒、macOS 原生通知、稍后提醒、提示音与全局快捷键。即使应用不在前台，一切照常运行。
    link: /guide/usage
    linkText: 了解更多
  - icon:
      light: /icons/sparkles.svg
      dark: /icons/sparkles-dark.svg
      alt: Sparkles
      width: "24"
      height: "24"
    title: 随连续打卡一起成长的宠物
    details: 每完成一个提醒，都会滋养你的伙伴。连续天数不断累积，它也会随之变化——新的心情、新的动画、新的里程碑。
    link: /guide/pets
    linkText: 认识这些宠物
  - icon:
      light: /icons/layers.svg
      dark: /icons/layers-dark.svg
      alt: Layers
      width: "24"
      height: "24"
    title: 重新打造的任务窗口
    details: 在一处完成撰写、安排时间与勾选。快速录入时，光标会一直停留在标题栏，方便你设置时间。
    link: /guide/usage
    linkText: 了解更多
  - icon:
      light: /icons/frame.svg
      dark: /icons/frame-dark.svg
      alt: Frame
      width: "24"
      height: "24"
    title: Markdown 笔记
    details: 任务描述与独立笔记支持块级编辑——标题、列表、待办、引用、代码与分隔线，最终仍以 Markdown 保存。
    link: /guide/usage
    linkText: 了解更多
  - icon:
      light: /icons/zap.svg
      dark: /icons/zap-dark.svg
      alt: Zap
      width: "24"
      height: "24"
    title: 看见你的进步
    details: 完成趋势、连续天数与 11 个内置成就。为那些你真正坚持下来的日子，送上一份安静的奖励。
    link: /guide/introduction
    linkText: 了解更多
  - icon:
      light: /icons/camera.svg
      dark: /icons/camera-dark.svg
      alt: Camera
      width: "24"
      height: "24"
    title: 为不打扰而设计
    details: 一切数据都留在你的 Mac 上。无需账户、无需登录、没有广告，也不经过云端——并启用了 App Sandbox。
    link: /guide/privacy
    linkText: 了解隐私

sections:
  featuresTitle: 你需要的，样样具备；用不到的，一概不添
  featuresSubtitle: 一款用 Rust 与 GPUI 重构的安静 macOS 应用——原生、快速，小巧到几乎感觉不到它的存在。
  screenshotsTitle: 细节一览
  screenshotsSubtitle: 这些细节，让它在你的 Mac 上恰到好处。
  petsTitle: 认识你的伙伴们
  petsSubtitle: 五只手绘宠物，各有专属动画与音效。挑一只，或者把它们全部带回家。
  howTitle: 三步，让一天更从容
  howSubtitle: 无需配置、无需账户、没有信息流。只是把你的一天，打理得更好一点。
  faqTitle: 常见问题
  faqSubtitle: 给 macOS 用户的快速解答

screenshots:
  - src: /screenshot-settings.jpg
    title: 按你的喜好调校
    desc: 显示语言、强调色、菜单栏图标与启动方式——全都收在一个整洁的设置窗口里。支持 25 种界面语言，以及浅色与深色主题。
  - src: /screenshot-pet-store.jpg
    title: 找到最合你心意的伙伴
    desc: 逛逛宠物商店，预览动画，单买一只或一次解锁全部。已购内容可在你的任意一台 Mac 上恢复。

pets:
  - name: 英国短毛猫
    image: /pets/british_optimized.png
    desc: 一只圆滚滚、惹人喜爱的猫，作为起步伙伴。
    price: 免费
    free: true
  - name: 柯基
    image: /pets/corgi_optimized.png
    desc: 一只活泼的彭布罗克威尔士柯基。
    price: $3.99
    badge: 推荐
  - name: 哈士奇
    image: /pets/husky_optimized.png
    desc: 一只精力充沛的西伯利亚哈士奇。
    price: $3.99
    badge: 推荐
  - name: 布偶猫
    image: /pets/ragdoll_optimized.png
    desc: 一只优雅温顺的布偶猫。
    price: $3.99
    badge: 推荐
  - name: 柴犬
    image: /pets/shibainu_optimized.png
    desc: 一只活泼又独立的柴犬。
    price: $3.99
    badge: 推荐

bundle:
  title: 全部宠物礼包
  desc: 一次性解锁商店里全部的高级宠物。
  price: $19.99

petsCta: "查看全部宠物与价格"

steps:
  - num: "01"
    title: 设置一个提醒
    desc: 输入标题、选定时间、设置重复规则——或者干脆按下全局快捷键，然后继续手头的工作。
  - num: "02"
    title: 完成它
    desc: 原生通知准时送达。在列表或任务窗口里勾选完成，你的伙伴都看在眼里。
  - num: "03"
    title: 看着宠物长大
    desc: 连续天数、成就与新心情悄悄累积，你的待办清单也有了心跳。

faqs:
  - question: Reminder 免费吗？
    answer: 是的。应用本身与英国短毛猫伙伴均免费。其他宠物为可选的内购项目——每只 $3.99，或以 $19.99 购买全部宠物礼包。Reminder 的功能从不要求付费。
  - question: 需要账户或联网吗？
    answer: 不需要。提醒、笔记、统计与宠物动画均可离线使用。只有在下载新购买的宠物包时才需要联网。
  - question: 支持哪些 macOS 版本？
    answer: Reminder 支持 macOS 12 Monterey 及更高版本，兼容 Apple Silicon（M 系列）与 Intel Mac。
  - question: 应用支持哪些语言？
    answer: 提供 25 种界面语言，包括英语、简体中文、繁体中文、日语、德语、西班牙语和法语。浅色与深色主题跟随系统设置。
  - question: 我的数据私密吗？
    answer: 所有数据都本地存储在你的 Mac 上。没有分析 SDK、没有广告、没有追踪，也没有云同步。内购完全由 Apple 处理。

cta:
  title: 给你的待办清单一个心跳。
  description: 下载 Reminder 2.0.0，让一位小小的伙伴陪你把日子好好过下去。
  primary: 下载 Reminder
  primaryLink: /guide/installation
  secondary: 阅读指南
  secondaryLink: /guide/introduction
---
