# Mitwirken

Vielen Dank, dass Sie helfen, die Dokumentation von Reminder zu verbessern. Korrekturen, Übersetzungen und neue Anleitungen sind jederzeit willkommen.

## Möglichkeiten zum Mitwirken

- Tippfehler, defekte Links oder veraltete Formulierungen korrigieren
- Einen Schritt verständlicher machen, der schwer nachzuvollziehen war
- Eine Seite in eine andere Sprache übersetzen
- Eine Anleitung für einen bislang nicht behandelten Arbeitsablauf ergänzen

## Arbeit an der Dokumentation

Diese Website wird mit [VitePress](https://vitepress.dev/) erstellt.

```bash
pnpm install
pnpm docs:dev      # local preview at http://localhost:5173
pnpm docs:build    # output in docs/.vitepress/dist
```

Die Inhalte der Startseite liegen im Frontmatter der jeweiligen `index.md` jeder Sprache. Beschriftungen für Navigation, Seitenleiste und Fußbereich liegen in `docs/.vitepress/config.ts`. Die Handbuchseiten verwenden relative Links, damit sie unter jedem Sprachpräfix funktionieren.

## Stil

- Bleiben Sie im Ton ruhig und sachlich – die App ist zurückhaltend, nicht werblich
- Bevorzugen Sie kurze Sätze und konkrete Schritte
- Lassen Sie Preise und Produktnamen genau so, wie sie unter [Haustiere & In-App-Käufe](guide/pets.md) aufgeführt sind
- Verwenden Sie innerhalb der Handbuchseiten relative Links

## App-Fehler melden

Für Fehler in der Anwendung (nicht in der Dokumentation) eröffnen Sie ein Issue im [Projekt-Repository](https://github.com/petreminder/reminder) und nennen Sie Ihre macOS-Version, die Reminder-Version, die Schritte zur Reproduktion sowie alle relevanten Protokolle.
