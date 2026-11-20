# Solución de problemas

## Los recordatorios nunca llegan

1. Abra **Configuración del Sistema → Notificaciones → Reminder** y confirme que las alertas están permitidas
2. Compruebe que los recordatorios no estén pausados en el menú de la barra
3. Asegúrese de que su Mac esté despierto a la hora programada
4. Salga de Reminder y vuelva a abrirlo

Si descartó la solicitud del primer inicio, las notificaciones pueden quedar desactivadas de forma permanente hasta que las vuelva a activar en Configuración del Sistema.

## La mascota no aparece

- Confirme que la mascota esté visible en el menú de la barra (mostrar/ocultar mascota)
- Compruebe que haya un compañero seleccionado en **Ajustes → Mascota**
- Verifique que el paquete de la mascota haya terminado de descargarse; vuelva a abrir la tienda y pruebe **Restaurar compras**
- Si usa una pantalla externa o una aplicación a pantalla completa, devuelva la mascota a la pantalla principal desde el menú de la barra

## Una compra no se desbloquea

1. Abra la tienda de mascotas y pulse **Restaurar compras**
2. Confirme que ha iniciado sesión en la Mac App Store con el mismo Apple ID
3. Compruebe su conexión de red y vuelva a intentarlo
4. Si sigue fallando, escriba a [reminder@w3cub.com](mailto:reminder@w3cub.com) indicando el nombre del producto

## Un paquete de mascotas no se descarga

La aplicación verifica cada paquete con una suma de comprobación SHA-256 y reintenta una vez una descarga fallida. Un fallo persistente suele deberse a una red inestable: inténtelo de nuevo con una conexión estable.

## La aplicación no se abre

1. Reinicie su Mac
2. Reinstale desde la Mac App Store (los datos locales se conservan fuera del paquete de la aplicación)
3. Si Gatekeeper bloquea una compilación de GitHub, use **Configuración del Sistema → Privacidad y seguridad → Abrir de todos modos**

## ¿Dónde están mis registros y mis datos?

Las compilaciones con sandbox almacenan los datos en:

```
~/Library/Containers/com.w3cub.reminder/Data/Library/Application Support/com.w3cub.reminder/
```

Use **Ajustes → General → Carpeta de registros** para abrirla directamente.

## ¿Sigue atascado?

Abra una incidencia en el [repositorio del proyecto](https://github.com/petreminder/reminder) con su versión de macOS, la versión de Reminder, los pasos para reproducir el problema y los registros, o escriba a [reminder@w3cub.com](mailto:reminder@w3cub.com).
