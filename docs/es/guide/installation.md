# Instalación

Reminder está disponible para macOS a través de la Mac App Store. La versión 2.0.0 es la versión actual.

## Descarga

- **[Reminder en la Mac App Store](https://apps.apple.com/app/id6776577400)** (recomendado: actualizaciones automáticas, compilación con sandbox)
- **[Versiones de GitHub](https://github.com/petreminder/reminder/releases)** — una compilación `.dmg` directa sin actualizaciones automáticas

## Instalación desde la Mac App Store

1. Abra el enlace de la App Store indicado arriba o busque «Reminder»
2. Haga clic en **Obtener** y después en **Instalar**
3. Abra Reminder desde Aplicaciones o Launchpad

## Instalación desde las versiones de GitHub

1. Descargue el `.dmg` más reciente
2. Haga doble clic para montarlo
3. Arrastre `Reminder.app` a `Applications`
4. Expulse la imagen y abra Reminder

Si macOS bloquea la aplicación, abra **Configuración del Sistema → Privacidad y seguridad** y haga clic en **Abrir de todos modos**, o haga clic con el botón derecho en la aplicación y elija **Abrir**.

## Primer inicio

Permita las **Notificaciones** cuando macOS lo solicite: así es como se entregan los recordatorios. No se requiere nada más: no hay cuenta, ni inicio de sesión, ni credenciales de demostración. Su compañero British Shorthair viene instalado y listo desde el primer inicio.

## Actualización

- **Mac App Store**: las actualizaciones se instalan automáticamente
- **Versiones de GitHub**: descargue la nueva compilación y sustituya la aplicación en `Applications`

Sus recordatorios y mascotas se almacenan fuera del paquete de la aplicación, por lo que actualizar nunca los elimina.

## Desinstalación

1. Salga de Reminder (desde el menú de la barra o con `Cmd+Q`)
2. Mueva `Reminder.app` a la Papelera
3. Opcionalmente, elimine los datos locales:

```bash
rm -rf ~/Library/Containers/com.w3cub.reminder
```

## Solución de problemas

Si la instalación falla, consulte [Solución de problemas](./troubleshooting.md) o escriba a [reminder@w3cub.com](mailto:reminder@w3cub.com).
