# Installation

Reminder is available for macOS through the Mac App Store. Version 2.0.0 is the current release.

## Download

- **[Reminder on the Mac App Store](https://apps.apple.com/app/id6776577400)** (recommended — automatic updates, sandbox build)
- **[GitHub Releases](https://github.com/petreminder/reminder/releases)** — a direct `.dmg` build without automatic updates

## Install from the Mac App Store

1. Open the App Store link above, or search for "Reminder"
2. Click **Get**, then **Install**
3. Launch Reminder from Applications or Launchpad

## Install from GitHub Releases

1. Download the latest `.dmg`
2. Double-click to mount it
3. Drag `Reminder.app` into `Applications`
4. Eject the image and open Reminder

If macOS blocks the app, open **System Settings → Privacy & Security** and click **Open Anyway**, or right-click the app and choose **Open**.

## First Launch

Allow **Notifications** when macOS asks — that is how reminders are delivered. Nothing else is required: there is no account, no sign-in and no demo credentials. Your British Shorthair companion is installed and ready from the first launch.

## Updating

- **Mac App Store**: updates are installed automatically
- **GitHub Releases**: download the new build and replace the app in `Applications`

Your reminders and pets are stored outside the app bundle, so updating never removes them.

## Uninstall

1. Quit Reminder (from the tray menu or `Cmd+Q`)
2. Move `Reminder.app` to the Trash
3. Optionally remove local data:

```bash
rm -rf ~/Library/Containers/com.w3cub.reminder
```

## Troubleshooting

If installation fails, see [Troubleshooting](./troubleshooting.md) or email [reminder@w3cub.com](mailto:reminder@w3cub.com).
