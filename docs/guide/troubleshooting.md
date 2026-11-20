# Troubleshooting

## Reminders never arrive

1. Open **System Settings → Notifications → Reminder** and confirm alerts are allowed
2. Check that reminders are not paused in the tray menu
3. Make sure your Mac is awake at the scheduled time
4. Quit and reopen Reminder

If the first-launch prompt was dismissed, notifications may be disabled permanently until you re-enable them in System Settings.

## The pet does not appear

- Confirm the pet is visible in the tray menu (show/hide pet)
- Check that a companion is selected in **Settings → Pet**
- Verify the pet pack finished downloading; reopen the pet store and try **Restore Purchases**
- On an external display or full-screen app, move the pet back to the main screen from the tray menu

## A purchase does not unlock

1. Open the pet store and tap **Restore Purchases**
2. Confirm you are signed in to the Mac App Store with the same Apple ID
3. Check your network connection, then retry
4. If it still fails, contact [reminder@w3cub.com](mailto:reminder@w3cub.com) with the product name

## A pet pack fails to download

The app verifies each pack with a SHA-256 checksum and retries a failed download once. A persistent failure usually means a flaky network — try again on a stable connection.

## The app does not open

1. Restart your Mac
2. Reinstall from the Mac App Store (local data is kept outside the app bundle)
3. If Gatekeeper blocks a GitHub build, use **System Settings → Privacy & Security → Open Anyway**

## Where are my logs and data?

Sandboxed builds store data in:

```
~/Library/Containers/com.w3cub.reminder/Data/Library/Application Support/com.w3cub.reminder/
```

Use **Settings → General → Log folder** to open it directly.

## Still stuck?

Open an issue in the [project repository](https://github.com/petreminder/reminder) with your macOS version, Reminder version, steps to reproduce and logs, or email [reminder@w3cub.com](mailto:reminder@w3cub.com).
