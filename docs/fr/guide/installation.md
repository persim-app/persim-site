# Installation

Reminder est disponible pour macOS sur le Mac App Store. La version 2.0.0 est la version actuelle.

## Téléchargement

- **[Reminder sur le Mac App Store](https://apps.apple.com/app/id6776577400)** (recommandé — mises à jour automatiques, version bac à sable)
- **[GitHub Releases](https://github.com/petreminder/reminder/releases)** — un `.dmg` direct sans mises à jour automatiques

## Installer depuis le Mac App Store

1. Ouvrez le lien de l'App Store ci-dessus, ou recherchez « Reminder »
2. Cliquez sur **Obtenir**, puis sur **Installer**
3. Lancez Reminder depuis Applications ou Launchpad

## Installer depuis GitHub Releases

1. Téléchargez le dernier `.dmg`
2. Double-cliquez pour le monter
3. Faites glisser `Reminder.app` dans `Applications`
4. Éjectez l'image disque et ouvrez Reminder

Si macOS bloque l'application, ouvrez **Réglages Système → Confidentialité et sécurité** et cliquez sur **Ouvrir quand même**, ou faites un clic droit sur l'application et choisissez **Ouvrir**.

## Premier lancement

Autorisez les **Notifications** lorsque macOS le demande — c'est ainsi que les rappels sont diffusés. Rien d'autre n'est requis : aucun compte, aucune connexion, aucun identifiant de démonstration. Votre compagnon British Shorthair est installé et prêt dès le premier lancement.

## Mise à jour

- **Mac App Store** : les mises à jour s'installent automatiquement
- **GitHub Releases** : téléchargez la nouvelle version et remplacez l'application dans `Applications`

Vos rappels et vos compagnons sont stockés en dehors du bundle de l'application : une mise à jour ne les supprime donc jamais.

## Désinstallation

1. Quittez Reminder (depuis le menu de la barre de menus ou `Cmd+Q`)
2. Placez `Reminder.app` dans la Corbeille
3. Supprimez facultativement les données locales :

```bash
rm -rf ~/Library/Containers/com.w3cub.reminder
```

## Dépannage

Si l'installation échoue, consultez [Dépannage](./troubleshooting.md) ou écrivez à [reminder@w3cub.com](mailto:reminder@w3cub.com).
