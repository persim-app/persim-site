# Privacy Choices

Reminder stores everything locally, so there is no server-side profile to access, download or delete. You stay in control directly on your Mac.

## Your Data Stays Local

- Reminders, lists, notes, tags and subtasks
- Statistics, streaks and achievements
- Settings, shortcuts and downloaded pet packs

We do not collect, sell or share personal information, and we do not use third-party analytics or advertising services.

## Managing or Removing Data

- Delete individual reminders, lists or notes inside the app
- Export your data from the app before removing it, if you want a copy
- Remove everything by quitting Reminder and deleting its container:

```bash
rm -rf ~/Library/Containers/com.w3cub.reminder
```

Development builds may store data outside the container; check **Settings → General → Data folder** for the exact path.

## Optional Network Features

- Pet store catalog and pet downloads are only used when you open the store or buy a pet
- Feedback is only sent when you explicitly submit the in-app form
- Cloud sync and accounts do not exist in Reminder, so there is nothing to opt out of

## In-App Purchases

Purchase and restoration are handled by Apple. To review or manage purchase history, use the Mac App Store with your Apple ID. To unlock pets on a new Mac, use **Restore Purchases** in the pet store.

Questions? Email [reminder@w3cub.com](mailto:reminder@w3cub.com) or read the [Privacy Policy](./privacy.md).
