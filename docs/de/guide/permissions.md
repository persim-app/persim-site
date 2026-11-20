# Berechtigungen

Reminder fragt nur sehr wenige macOS-Berechtigungen an. Es gibt kein Konto, keine Analysefunktionen und keine Cloud-Synchronisierung im Hintergrund.

## Mitteilungen

**Erforderlich.** Erinnerungen werden über native macOS-Mitteilungen zugestellt, damit sie auch dann ankommen, wenn die App nicht im Vordergrund ist. macOS fragt beim ersten Planen einer Erinnerung danach; erlauben Sie sie unter **Systemeinstellungen → Mitteilungen → Reminder**.

## Dateien & Ordner

Der Sandbox-Build aus dem Mac App Store speichert Erinnerungen, Einstellungen, Protokolle und heruntergeladene Haustier-Pakete in seinem eigenen Container:

```
~/Library/Containers/com.w3cub.reminder/Data/Library/Application Support/com.w3cub.reminder/
```

Beim Importieren eines `.catpet`-Pakets wird der standardmäßige macOS-Dateiauswahldialog verwendet – die App liest nur Dateien, die Sie selbst auswählen.

## Bedienungshilfen / Bildschirmaufnahme

**Nicht erforderlich.** Das schwebende Haustierfenster wird von der App selbst gezeichnet; Reminder nimmt Ihren Bildschirm nicht auf und liest keine Inhalte anderer Apps aus.

## Netzwerk

Ausgehende Anfragen beschränken sich auf:

- den Katalog des Haustier-Shops und den Download von Haustier-Paketen (`app-sources.w3cub.com`)
- die StoreKit-Dienste von Apple für Käufe und Wiederherstellung
- optionales Feedback, das Sie aus der App heraus senden

## Berechtigungen verwalten

Öffnen Sie **Systemeinstellungen → Datenschutz & Sicherheit**, um Berechtigungen zu prüfen oder zu widerrufen. Beenden Sie Reminder nach einer Änderung und öffnen Sie es erneut. Wurden die Mitteilungsabfragen abgelehnt, lesen Sie [Fehlerbehebung](./troubleshooting.md).
