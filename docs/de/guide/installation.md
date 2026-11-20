# Installation

Reminder ist für macOS über den Mac App Store erhältlich. Version 2.0.0 ist die aktuelle Version.

## Download

- **[Reminder im Mac App Store](https://apps.apple.com/app/id6776577400)** (empfohlen – automatische Updates, Sandbox-Build)
- **[GitHub Releases](https://github.com/petreminder/reminder/releases)** – ein direkter `.dmg`-Build ohne automatische Updates

## Installation über den Mac App Store

1. Öffnen Sie den obenstehenden App-Store-Link oder suchen Sie nach **Reminder**
2. Klicken Sie auf **Laden** und anschließend auf **Installieren**
3. Starten Sie Reminder über Programme oder Launchpad

## Installation über GitHub Releases

1. Laden Sie die aktuelle `.dmg`-Datei herunter
2. Doppelklicken Sie, um das Image einzubinden
3. Ziehen Sie `Reminder.app` in den Ordner `Applications`
4. Werfen Sie das Image aus und öffnen Sie Reminder

Falls macOS die App blockiert, öffnen Sie **Systemeinstellungen → Datenschutz & Sicherheit** und klicken Sie auf **Trotzdem öffnen**, oder klicken Sie mit der rechten Maustaste auf die App und wählen Sie **Öffnen**.

## Erster Start

Erlauben Sie **Mitteilungen**, wenn macOS danach fragt – so werden Erinnerungen zugestellt. Weiter ist nichts erforderlich: Es gibt kein Konto, keine Anmeldung und keine Demo-Zugangsdaten. Ihr Begleiter British Shorthair ist ab dem ersten Start installiert und einsatzbereit.

## Aktualisieren

- **Mac App Store**: Updates werden automatisch installiert
- **GitHub Releases**: Laden Sie den neuen Build herunter und ersetzen Sie die App im Ordner `Applications`

Ihre Erinnerungen und Haustiere werden außerhalb des App-Pakets gespeichert, sodass ein Update sie niemals entfernt.

## Deinstallation

1. Beenden Sie Reminder (über das Menüleisten-Menü oder `Cmd+Q`)
2. Verschieben Sie `Reminder.app` in den Papierkorb
3. Entfernen Sie optional die lokalen Daten:

```bash
rm -rf ~/Library/Containers/com.w3cub.reminder
```

## Fehlerbehebung

Schlägt die Installation fehl, lesen Sie [Fehlerbehebung](./troubleshooting.md) oder schreiben Sie an [reminder@w3cub.com](mailto:reminder@w3cub.com).
