---
weight: 5
title: "Mantenimiento"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "build"
toc: true
description: "Mantenimiento diario de una instancia de rtCloud autoalojada: actualización, copia de seguridad, restauración y solución de problemas comunes."
---

## Comandos comunes

Use estos comandos regularmente para gestionar sus contenedores de rtCloud. Ejecútelos desde el directorio que contiene `docker-compose.production.yml`.

```bash
# Verificar el estado y la salud de todos los contenedores
docker compose -f docker-compose.production.yml ps

# Ver registros en vivo (todos los servicios)
docker compose -f docker-compose.production.yml logs -f

# Ver registros solo de la aplicación
docker compose -f docker-compose.production.yml logs -f rtcloud

# Reiniciar un solo contenedor
docker compose -f docker-compose.production.yml restart rtcloud

# Detener todos los servicios
docker compose -f docker-compose.production.yml down

# Iniciar todos los servicios
docker compose -f docker-compose.production.yml up -d

# Abrir un shell dentro del contenedor de la aplicación
docker compose -f docker-compose.production.yml exec rtcloud bash
```

---

## Actualización

Las actualizaciones de rtCloud se distribuyen como nuevas etiquetas de imágenes Docker. La actualización descarga la última imagen y recrea el contenedor de la aplicación. Las migraciones de base de datos se ejecutan automáticamente al inicio.

**1. Descargue la última imagen:**

```bash
docker compose -f docker-compose.production.yml pull
```

**2. Recree el contenedor de la aplicación:**

```bash
docker compose -f docker-compose.production.yml up -d
```

Docker reemplaza solo los contenedores cuya imagen ha cambiado. El contenedor MySQL y todos los volúmenes nombrados no se ven afectados.

### Fijar una versión

Para actualizar a una versión específica en lugar de `latest`, actualice `RTCLOUD_IMAGE` en `.env`:

```dotenv
RTCLOUD_IMAGE=rtawebteam/rta-smartsurvey:1.2.3
```

Luego ejecute `docker compose pull` y `up -d` como se indicó arriba.

### Degradar

Generalmente no se recomienda degradar, ya que las migraciones de base de datos no se pueden revertir. Si es necesario degradar, restaure desde una copia de seguridad de la base de datos tomada antes de la actualización.

---

## Copia de seguridad y restauración

### Copia de seguridad de la base de datos

Ejecute este comando para exportar la base de datos de la aplicación a un archivo SQL:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > backup-$(date +%Y%m%d-%H%M%S).sql
```

El archivo de copia de seguridad se escribe en su directorio actual en el host.

### Restaurar la base de datos

```bash
docker compose -f docker-compose.production.yml exec -T mysql \
  mysql -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  < backup-20240101-120000.sql
```

### Copia de seguridad de archivos subidos

Los envíos de encuestas a menudo incluyen archivos subidos (fotos, audio, documentos) almacenados en volúmenes Docker nombrados. Haga una copia de seguridad de ellos por separado de la base de datos:

```bash
# Copia de seguridad de los archivos subidos
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/uploads-$(date +%Y%m%d).tar.gz -C /data .

# Copia de seguridad de grabaciones de audio
docker run --rm \
  -v rtcloud_audios:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/audios-$(date +%Y%m%d).tar.gz -C /data .
```

Reemplace `rtcloud_uploads` y `rtcloud_audios` con sus nombres de volumen reales (con el prefijo de `COMPOSE_PROJECT_NAME`) si cambió el predeterminado.

### Restaurar archivos subidos

```bash
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar xzf /backup/uploads-20240101.tar.gz -C /data
```

### Copias de seguridad diarias automatizadas

Agregue un trabajo cron en el host para ejecutar copias de seguridad automáticamente. Edite el crontab raíz con `crontab -e`:

```cron
# Copia de seguridad diaria de la base de datos a las 2:00 AM, conservar 30 días de historial
0 2 * * * cd /opt/rtcloud && docker compose -f docker-compose.production.yml exec -T mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > /backups/db-$(date +\%Y\%m\%d).sql && \
  find /backups -name "db-*.sql" -mtime +30 -delete
```

---

## Solución de problemas

### El contenedor de la aplicación no inicia

Verifique los registros del contenedor en busca de mensajes de error:

```bash
docker compose -f docker-compose.production.yml logs rtcloud
```

Causas comunes:
- Variables de entorno faltantes o no válidas en `.env`
- MySQL aún no está listo (espere 60 segundos y vuelva a verificar)
- Conflicto de puerto — otro proceso ya está usando `APP_PORT`

### MySQL no está en buen estado

```bash
docker compose -f docker-compose.production.yml logs mysql
```

Causas comunes:
- `MYSQL_ROOT_PASSWORD` no está establecido en `.env`
- Volumen de datos dañado (poco frecuente — verifique el espacio en disco con `df -h`)

MySQL puede tardar 30–60 segundos en inicializarse en el primer arranque. Espere y vuelva a verificar antes de asumir un fallo.

### Puerto ya en uso

Cambie `APP_PORT` o `SHINY_PORT` en `.env` a un puerto libre, luego recree los contenedores:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate
```

Para encontrar qué está usando un puerto en el host:

```bash
lsof -i :8080
```

### 400 CSRF Token Could Not Be Verified

Este error aparece en entornos locales o de proxy inverso donde el origen de la solicitud no coincide con el host esperado. Deshabilite la validación CSRF solo para el desarrollo local:

```dotenv
CSRF_VALIDATION_ENABLED=false
```

Luego reinicie la aplicación:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

> No deshabilite la validación CSRF en producción. Si este error ocurre en producción, asegúrese de que su proxy inverso esté reenviando los encabezados correctos `Host` y `X-Forwarded-For`.

### Olvidó la contraseña del administrador

Restablezca la contraseña del administrador directamente en la base de datos. Conéctese al contenedor MySQL y actualice el hash de la contraseña:

**Paso 1** — Genere el nuevo hash de contraseña. Reemplace `newpassword` con su contraseña deseada:

```bash
docker compose -f docker-compose.production.yml exec rtcloud php -r "
  \$salt = trim(shell_exec(\"mysql -h mysql -u root -p\\\"\${MYSQL_ROOT_PASSWORD}\\\" \${MYSQL_DATABASE} -se \\\"SELECT salt FROM ss_user WHERE username='admin';\\\"\"));
  echo md5(\$salt . 'newpassword') . PHP_EOL;
"
```

**Paso 2** — Actualice el hash en la base de datos:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysql -u root -p"${MYSQL_ROOT_PASSWORD}" smartsurvey \
  -e "UPDATE ss_user SET password='<hash_from_step_1>' WHERE username='admin';"
```

### El contenedor sigue reiniciándose

Verifique si la comprobación de salud está fallando:

```bash
docker compose -f docker-compose.production.yml ps
docker inspect rtcloud-app --format '{{json .State.Health}}'
```

La comprobación de salud de la aplicación llama al endpoint `/health`. Si falla repetidamente, verifique los registros de la aplicación en busca de errores de inicio.

### Disco lleno

Identifique qué está consumiendo espacio:

```bash
# Verificar el uso del disco del host
df -h

# Verificar el uso del disco de Docker (imágenes, contenedores, volúmenes)
docker system df

# Eliminar imágenes no utilizadas y contenedores detenidos (seguro de ejecutar)
docker system prune
```

No use `docker system prune --volumes` ya que esto eliminará los datos de la aplicación.

---

## Comprobaciones de salud

Cada servicio tiene una comprobación de salud automática. El estado del contenedor refleja el resultado:

| Contenedor | Método de comprobación | Período de inicio | Intervalo |
|-----------|-------------|-------------|----------|
| `rtcloud-app` | HTTP GET `/health` | 90 segundos | 30 segundos |
| `rtcloud-mysql` | `mysqladmin ping` | 30 segundos | 10 segundos |
| `rtcloud-keycloak` | HTTP GET `:9000/health/live` | 120 segundos | 30 segundos |

Los contenedores con una comprobación de salud fallida se reinician automáticamente según la configuración de `RESTART_POLICY` (predeterminado: `unless-stopped`).
