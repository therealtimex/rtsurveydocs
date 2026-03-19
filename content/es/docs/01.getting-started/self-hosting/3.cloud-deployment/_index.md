---
weight: 3
title: "Implementación en la nube"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud_upload"
toc: true
description: "Implemente rtCloud en los principales proveedores de nube con scripts automatizados para DigitalOcean, AWS EC2, Google Cloud y Linode."
---

El repositorio de implementación incluye scripts de aprovisionamiento automatizado para los principales proveedores de nube. Cada script se ejecuta en el primer arranque de un servidor **Ubuntu 22.04 LTS** nuevo y realiza una configuración completamente desatendida:

- Instala Docker y Docker Compose
- Genera contraseñas aleatorias seguras para todos los servicios internos
- Escribe `docker-compose.production.yml` y `.env`
- Configura Nginx como proxy inverso
- Obtiene un certificado TLS gratuito de Let's Encrypt (reintenta automáticamente hasta que el DNS se resuelva)
- Configura el firewall UFW
- Opcionalmente implementa el servidor SSO Keycloak integrado
- Muestra un resumen completo de la implementación con todas las credenciales

La configuración se completa en **5–10 minutos** en una instancia estándar.

---

## Cómo elegir un script

Hay múltiples variantes de scripts según su proveedor de nube y la configuración de SSO:

| Script | Proveedor | Modo SSO | Mejor para |
|--------|----------|----------|----------|
| `digitalocean-droplet-keycloak-embed.sh` | DigitalOcean | Keycloak integrado | SSO simple y autocontenido |
| `digitalocean-droplet.sh` | DigitalOcean | Keycloak o OIDC externo | Control total |
| `linode-stackscript-keycloak-embed.sh` | Linode | Keycloak integrado | Configuración basada en formulario, la más simple |
| `linode-stackscript-oidc.sh` | Linode | Solo OIDC externo | Proveedor de identidad existente |
| `linode-stackscript.sh` | Linode | Keycloak o OIDC externo | Control total |
| `aws-ec2.sh` | AWS EC2 | Keycloak o OIDC externo | Implementaciones en AWS |
| `gcp-compute.sh` | Google Cloud | Keycloak o OIDC externo | Implementaciones en GCP |

> **Recomendado para la mayoría de los usuarios:** Use la variante `keycloak-embed`. Incluye un servidor de identidad Keycloak integrado y requiere la menor cantidad de campos de configuración.

---

## Guía de dimensionamiento del servidor

| Caso de uso | RAM | Disco | Ejemplo |
|----------|-----|------|---------|
| Evaluación / desarrollo | 2 GB | 25 GB | DO Basic $18/mes, t3.small, e2-small |
| Equipo pequeño (< 50 usuarios) | 4 GB | 40 GB | DO Basic $24/mes, t3.medium, e2-medium |
| Producción (> 50 usuarios) | 8 GB | 80 GB | DO General $48/mes, t3.large, n2-standard-2 |

> Keycloak integrado requiere al menos **4 GB de RAM**. Use 2 GB solo para evaluación sin Keycloak.

---

## Configuración de DNS

Todos los scripts requieren un dominio con un **registro A apuntando a la IP de su servidor** antes de que Let's Encrypt pueda emitir un certificado.

El script imprime la IP de su servidor al inicio del proceso de configuración:

```
============================================================
 Server IP : 139.162.51.85
 Add this DNS A record now if you haven't already:
   myapp.example.com  ->  139.162.51.85
 The script will retry Certbot every 60s until DNS resolves.
============================================================
```

El script **reintenta automáticamente** Let's Encrypt cada 60 segundos durante hasta 1 hora. Solo agregue el registro DNS y espere — no es necesario reiniciar.

> **Límite de velocidad:** Let's Encrypt permite un máximo de **5 certificados por dominio cada 7 días**. Evite implementar y destruir servidores repetidamente con el mismo dominio. Si alcanza el límite, el script mostrará una marca de tiempo `retry after` y se detendrá inmediatamente.

---

## Lista de verificación post-implementación

- [ ] La aplicación se abre en `https://su-dominio.com`
- [ ] Inicie sesión con `admin` y la contraseña que configuró
- [ ] Todos los contenedores están en buen estado: `docker compose -f /opt/rtcloud/docker-compose.production.yml ps`
- [ ] La renovación de Let's Encrypt funciona: `certbot renew --dry-run`
- [ ] El puerto MySQL 3306 **no** está expuesto: `ufw status`
- [ ] Configure una copia de seguridad diaria de la base de datos (consulte [Mantenimiento](../maintenance))

---

## Solución de problemas

### Revise el registro completo de configuración

```bash
# Linode
tail -200 /var/log/stackscript.log

# DigitalOcean / AWS / GCP
tail -200 /var/log/rtcloud-setup.log
```

### Límite de velocidad de Let's Encrypt

Si ve `too many certificates` en el registro, ha alcanzado el límite de 5 certificados/7 días. El registro muestra el tiempo exacto de reintento:

```
[SSL] ERROR: Let's Encrypt rate limit hit. retry after 2026-03-15 16:22 UTC.
```

Espere hasta ese momento y vuelva a implementar.

### Keycloak permanece sin funcionar correctamente

Asegúrese de que el servidor tenga al menos 4 GB de RAM, luego verifique los registros:

```bash
docker logs rtcloud-keycloak --tail 50
free -h
```

### La configuración SSL no se aplica después de certbot

Si el certificado fue emitido pero Nginx todavía muestra solo HTTP, verifique el registro en busca del error y recargue Nginx manualmente:

```bash
nginx -t && systemctl reload nginx
```
