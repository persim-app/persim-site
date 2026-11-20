# Permissions

Reminder asks for very few macOS permissions. There is no account, no analytics and no background cloud sync.

## Notifications

**Required.** Reminders are delivered through native macOS notifications, so they arrive even when the app is not in front. macOS prompts you the first time a reminder is scheduled; allow it in **System Settings → Notifications → Reminder**.

## Files & Folders

The sandboxed Mac App Store build stores reminders, settings, logs and downloaded pet packs inside its own container:

```
~/Library/Containers/com.w3cub.reminder/Data/Library/Application Support/com.w3cub.reminder/
```

Importing a `.catpet` pack uses the standard macOS file picker — the app only reads files you choose yourself.

## Accessibility / Screen Recording

**Not required.** The floating pet window is drawn by the app itself; Reminder does not capture your screen or read other apps' contents.

## Network

Outbound requests are limited to:

- the pet store catalog and pet pack downloads (`app-sources.w3cub.com`)
- Apple's StoreKit services for purchases and restoration
- optional feedback you choose to send from the app

## Managing Permissions

Open **System Settings → Privacy & Security** to review or revoke anything. After changing permissions, quit and reopen Reminder. If notification prompts were dismissed, see [Troubleshooting](./troubleshooting.md).
