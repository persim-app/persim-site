# Contribuir

Gracias por ayudar a mejorar la documentación de Reminder. Las correcciones, las traducciones y las guías nuevas son bienvenidas.

## Formas de contribuir

- Corregir errores tipográficos, enlaces rotos o texto desactualizado
- Aclarar un paso difícil de seguir
- Traducir una página a otro idioma
- Añadir una guía sobre un flujo de trabajo que aún no hemos cubierto

## Trabajar en la documentación

Este sitio está construido con [VitePress](https://vitepress.dev/).

```bash
pnpm install
pnpm docs:dev      # local preview at http://localhost:5173
pnpm docs:build    # output in docs/.vitepress/dist
```

El contenido de la página de inicio vive en el frontmatter del `index.md` de cada idioma. Las etiquetas de navegación, la barra lateral y el pie de página están en `docs/.vitepress/config.ts`. Las páginas de la guía usan enlaces relativos para funcionar bajo cualquier prefijo de idioma.

## Estilo

- Mantenga un tono sereno y práctico: el tono de la aplicación es discreto, no promocional
- Prefiera frases cortas y pasos concretos
- Mantenga los precios y los nombres de los productos tal como aparecen en [Mascotas y compras integradas](guide/pets.md)
- Use enlaces relativos dentro de las páginas de la guía

## Informar de errores de la aplicación

Para errores de la aplicación (no de la documentación), abra una incidencia en el [repositorio del proyecto](https://github.com/petreminder/reminder) e incluya su versión de macOS, la versión de Reminder, los pasos para reproducir el problema y los registros pertinentes.
