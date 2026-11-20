# Autorisations

Reminder ne demande que très peu d'autorisations macOS. Il n'y a ni compte, ni analyse, ni synchronisation en arrière-plan dans le cloud.

## Notifications

**Obligatoire.** Les rappels sont diffusés via les notifications natives de macOS : ils arrivent même lorsque l'application n'est pas au premier plan. macOS vous le demande la première fois qu'un rappel est planifié ; autorisez-le dans **Réglages Système → Notifications → Reminder**.

## Fichiers et dossiers

La version bac à sable du Mac App Store stocke les rappels, les réglages, les journaux et les packs de compagnons téléchargés dans son propre conteneur :

```
~/Library/Containers/com.w3cub.reminder/Data/Library/Application Support/com.w3cub.reminder/
```

L'import d'un pack `.catpet` utilise le sélecteur de fichiers standard de macOS — l'application ne lit que les fichiers que vous choisissez vous-même.

## Accessibilité / Enregistrement de l'écran

**Non nécessaire.** La fenêtre flottante du compagnon est dessinée par l'application elle-même ; Reminder ne capture pas votre écran et ne lit pas le contenu des autres applications.

## Réseau

Les requêtes sortantes se limitent à :

- le catalogue de la boutique et le téléchargement des packs de compagnons (`app-sources.w3cub.com`)
- les services StoreKit d'Apple pour les achats et la restauration
- les commentaires facultatifs que vous choisissez d'envoyer depuis l'application

## Gérer les autorisations

Ouvrez **Réglages Système → Confidentialité et sécurité** pour consulter ou révoquer ces autorisations. Après toute modification, quittez puis rouvrez Reminder. Si les invites de notification ont été ignorées, consultez [Dépannage](./troubleshooting.md).
