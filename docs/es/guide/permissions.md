# Permisos

Reminder solicita muy pocos permisos de macOS. No hay cuenta, ni análisis de datos, ni sincronización en la nube en segundo plano.

## Notificaciones

**Obligatorio.** Los recordatorios se entregan mediante las notificaciones nativas de macOS, por lo que llegan incluso cuando la aplicación no está en primer plano. macOS se lo solicita la primera vez que se programa un recordatorio; permita el acceso en **Configuración del Sistema → Notificaciones → Reminder**.

## Archivos y carpetas

La compilación de la Mac App Store con sandbox almacena los recordatorios, los ajustes, los registros y los paquetes de mascotas descargados dentro de su propio contenedor:

```
~/Library/Containers/com.w3cub.reminder/Data/Library/Application Support/com.w3cub.reminder/
```

La importación de un paquete `.catpet` usa el selector de archivos estándar de macOS: la aplicación solo lee los archivos que usted elige.

## Accesibilidad / Grabación de pantalla

**No es necesario.** La ventana flotante de la mascota la dibuja la propia aplicación; Reminder no captura su pantalla ni lee el contenido de otras aplicaciones.

## Red

Las solicitudes salientes se limitan a:

- el catálogo de la tienda de mascotas y las descargas de paquetes (`app-sources.w3cub.com`)
- los servicios StoreKit de Apple para compras y restauración
- los comentarios opcionales que usted decida enviar desde la aplicación

## Gestionar los permisos

Abra **Configuración del Sistema → Privacidad y seguridad** para revisar o revocar cualquier permiso. Después de cambiar los permisos, salga de Reminder y vuelva a abrirlo. Si descartó las solicitudes de notificaciones, consulte [Solución de problemas](./troubleshooting.md).
