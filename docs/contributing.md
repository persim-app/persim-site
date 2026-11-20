# Contributing

Thanks for helping improve the Reminder documentation. Corrections, translations and new guides are all welcome.

## Ways to Contribute

- Fix typos, broken links or outdated wording
- Clarify a step that was hard to follow
- Translate a page into another language
- Add a guide for a workflow we haven't covered

## Working on the Docs

This site is built with [VitePress](https://vitepress.dev/).

```bash
pnpm install
pnpm docs:dev      # local preview at http://localhost:5173
pnpm docs:build    # output in docs/.vitepress/dist
```

The homepage content lives in each language's `index.md` frontmatter. Navigation, sidebar and footer labels live in `docs/.vitepress/config.ts`. Guide pages use relative links so they work under every language prefix.

## Style

- Keep the tone calm and practical — the app's tone is quiet, not promotional
- Prefer short sentences and concrete steps
- Keep prices and product names exactly as listed in [Pets & IAP](guide/pets.md)
- Use relative links inside guide pages

## Reporting App Bugs

For application bugs (not documentation), open an issue in the [project repository](https://github.com/petreminder/reminder) and include your macOS version, Reminder version, reproduction steps and any relevant logs.
