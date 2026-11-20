# Contribuer

Merci de contribuer à l'amélioration de la documentation de Reminder. Corrections, traductions et nouveaux guides sont les bienvenus.

## Façons de contribuer

- Corriger des coquilles, des liens brisés ou des formulations obsolètes
- Clarifier une étape difficile à suivre
- Traduire une page dans une autre langue
- Ajouter un guide pour un flux de travail non encore couvert

## Travailler sur la documentation

Ce site est construit avec [VitePress](https://vitepress.dev/).

```bash
pnpm install
pnpm docs:dev      # local preview at http://localhost:5173
pnpm docs:build    # output in docs/.vitepress/dist
```

Le contenu de la page d'accueil se trouve dans le frontmatter du fichier `index.md` de chaque langue. La navigation, la barre latérale et les libellés du pied de page se trouvent dans `docs/.vitepress/config.ts`. Les pages du guide utilisent des liens relatifs afin de fonctionner sous chaque préfixe de langue.

## Style

- Gardez un ton calme et pragmatique — le ton de l'application est discret, non promotionnel
- Préférez les phrases courtes et les étapes concrètes
- Conservez les prix et les noms de produits tels qu'indiqués dans [Compagnons et achats intégrés](guide/pets.md)
- Utilisez des liens relatifs dans les pages du guide

## Signaler un bug de l'application

Pour les bugs de l'application (et non de la documentation), ouvrez un ticket dans le [dépôt du projet](https://github.com/petreminder/reminder) en indiquant votre version de macOS, votre version de Reminder, les étapes de reproduction et les journaux pertinents.
