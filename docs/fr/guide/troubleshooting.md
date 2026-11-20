# Dépannage

## Les rappels n'arrivent jamais

1. Ouvrez **Réglages Système → Notifications → Reminder** et vérifiez que les alertes sont autorisées
2. Vérifiez que les rappels ne sont pas suspendus dans le menu de la barre de menus
3. Assurez-vous que votre Mac est éveillé à l'heure prévue
4. Quittez puis rouvrez Reminder

Si l'invite du premier lancement a été ignorée, les notifications peuvent rester désactivées jusqu'à ce que vous les réactiviez dans les Réglages Système.

## Le compagnon n'apparaît pas

- Vérifiez que le compagnon est visible dans le menu de la barre de menus (afficher/masquer le compagnon)
- Vérifiez qu'un compagnon est sélectionné dans **Réglages → Compagnon**
- Vérifiez que le téléchargement du pack est terminé ; rouvrez la boutique et essayez **Restaurer les achats**
- Sur un écran externe ou une application en plein écran, ramenez le compagnon sur l'écran principal depuis le menu de la barre de menus

## Un achat ne se débloque pas

1. Ouvrez la boutique de compagnons et cliquez sur **Restaurer les achats**
2. Vérifiez que vous êtes connecté au Mac App Store avec le même identifiant Apple
3. Vérifiez votre connexion réseau, puis réessayez
4. Si l'échec persiste, contactez [reminder@w3cub.com](mailto:reminder@w3cub.com) en indiquant le nom du produit

## Le téléchargement d'un pack échoue

L'application vérifie chaque pack avec une somme de contrôle SHA-256 et relance une fois un téléchargement ayant échoué. Un échec persistant indique généralement un réseau instable — réessayez avec une connexion stable.

## L'application ne s'ouvre pas

1. Redémarrez votre Mac
2. Réinstallez depuis le Mac App Store (les données locales sont conservées en dehors du bundle de l'application)
3. Si Gatekeeper bloque une version GitHub, utilisez **Réglages Système → Confidentialité et sécurité → Ouvrir quand même**

## Où sont mes journaux et mes données ?

Les versions bac à sable stockent les données dans :

```
~/Library/Containers/com.w3cub.reminder/Data/Library/Application Support/com.w3cub.reminder/
```

Utilisez **Réglages → Général → Dossier des journaux** pour l'ouvrir directement.

## Toujours bloqué ?

Ouvrez un ticket dans le [dépôt du projet](https://github.com/petreminder/reminder) en indiquant votre version de macOS, votre version de Reminder, les étapes de reproduction et les journaux, ou écrivez à [reminder@w3cub.com](mailto:reminder@w3cub.com).
