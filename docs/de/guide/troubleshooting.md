# Fehlerbehebung

## Erinnerungen kommen nicht an

1. Öffnen Sie **Systemeinstellungen → Mitteilungen → Reminder** und prüfen Sie, ob Mitteilungen erlaubt sind
2. Stellen Sie sicher, dass Erinnerungen im Menüleisten-Menü nicht pausiert sind
3. Vergewissern Sie sich, dass Ihr Mac zur geplanten Zeit nicht im Ruhezustand ist
4. Beenden Sie Reminder und öffnen Sie es erneut

Wurde die Abfrage beim ersten Start abgelehnt, können Mitteilungen dauerhaft deaktiviert bleiben, bis Sie sie in den Systemeinstellungen wieder aktivieren.

## Das Haustier erscheint nicht

- Prüfen Sie, ob das Haustier im Menüleisten-Menü sichtbar ist (Haustier ein-/ausblenden)
- Stellen Sie sicher, dass unter **Einstellungen → Haustier** ein Begleiter ausgewählt ist
- Prüfen Sie, ob der Download des Haustier-Pakets abgeschlossen ist; öffnen Sie den Haustier-Shop erneut und versuchen Sie **Käufe wiederherstellen**
- Bei einem externen Display oder einer Vollbild-App verschieben Sie das Haustier über das Menüleisten-Menü zurück auf den Hauptbildschirm

## Ein Kauf wird nicht freigeschaltet

1. Öffnen Sie den Haustier-Shop und tippen Sie auf **Käufe wiederherstellen**
2. Vergewissern Sie sich, dass Sie im Mac App Store mit derselben Apple ID angemeldet sind
3. Prüfen Sie Ihre Netzwerkverbindung und versuchen Sie es erneut
4. Schlägt es weiterhin fehl, wenden Sie sich mit dem Produktnamen an [reminder@w3cub.com](mailto:reminder@w3cub.com)

## Ein Haustier-Paket lässt sich nicht herunterladen

Die App prüft jedes Paket mit einer SHA-256-Prüfsumme und wiederholt einen fehlgeschlagenen Download einmal. Ein dauerhafter Fehler deutet meist auf eine instabile Verbindung hin – versuchen Sie es erneut in einem stabilen Netzwerk.

## Die App lässt sich nicht öffnen

1. Starten Sie Ihren Mac neu
2. Installieren Sie die App aus dem Mac App Store neu (lokale Daten liegen außerhalb des App-Pakets)
3. Blockiert Gatekeeper einen GitHub-Build, nutzen Sie **Systemeinstellungen → Datenschutz & Sicherheit → Trotzdem öffnen**

## Wo finde ich Protokolle und Daten?

Sandbox-Builds speichern Daten in:

```
~/Library/Containers/com.w3cub.reminder/Data/Library/Application Support/com.w3cub.reminder/
```

Über **Einstellungen → Allgemein → Protokollordner** können Sie den Ordner direkt öffnen.

## Nichts geholfen?

Eröffnen Sie ein Issue im [Projekt-Repository](https://github.com/petreminder/reminder) mit Ihrer macOS-Version, der Reminder-Version, den Schritten zur Reproduktion und den Protokollen, oder schreiben Sie an [reminder@w3cub.com](mailto:reminder@w3cub.com).
