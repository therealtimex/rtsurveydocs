#!/bin/bash
# ==============================================================================
# rtCloud - DigitalOcean Droplet User-Data Script (Embedded Keycloak)
# ==============================================================================
# Provisions a fresh Ubuntu 22.04 LTS Droplet with Docker and launches rtCloud
# with Keycloak embedded as the SSO provider.
#
# HOW TO USE:
#   1. Edit the variables in the "CONFIGURATION" section below.
#   2. Paste this entire script into "User Data" when creating a Droplet
#      (Advanced Options > Add Initialization scripts).
#   3. Choose Ubuntu 22.04 LTS as the Droplet image.
#   4. Recommended: 2 vCPUs / 4 GB RAM or higher (Keycloak needs memory).
#
# Monitor progress:
#   ssh root@<droplet-ip> tail -f /var/log/rtcloud-setup.log
#
# SSL: Let's Encrypt via Certbot (DNS A record must point to this server first).
# ==============================================================================

# ==============================================================================
# CONFIGURATION — Edit these values before pasting as user-data
# ==============================================================================

# --- Required ---
PROJECT_ID="rtsurvey"                         # Unique identifier (no spaces)
ADMIN_PASSWORD="admin"                        # Admin password for app and Keycloak — change after first login

# --- Docker Image ---
RTCLOUD_IMAGE="rtawebteam/rta-smartsurvey:survey-dockerize"

# --- Domain + SSL (required — Keycloak needs HTTPS) ---
DOMAIN=""                   # e.g. "myapp.example.com" — DNS A record must point here first
PROJECT_URL=""              # Override URL (leave blank to use DOMAIN); useful behind Cloudflare
LETSENCRYPT_EMAIL=""        # e.g. "admin@example.com"

# --- Stata14 (optional) ---
STATA_ENABLED="false"
STATA_LICENSE_B64=""        # base64 of stata.lic (required when STATA_ENABLED=true)
#   How to encode:  base64 -w 0 stata.lic   (Linux) / base64 -i stata.lic   (macOS)

# --- Optional ---
TZ="Asia/Ho_Chi_Minh"
OPEN_REGISTRATION="true"

# ==============================================================================
# END CONFIGURATION — Do not edit below this line
# ==============================================================================

set -euo pipefail
exec > >(tee /var/log/rtcloud-setup.log) 2>&1
trap 'echo "ERROR: script failed at line $LINENO (exit $?)" >&2' ERR

echo "============================================================"
echo " rtCloud (Embedded Keycloak) starting - $(date)"
echo "============================================================"

# ------------------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------------------
normalize_bool() {
  local v="${1:-}"
  v="$(echo "$v" | tr '[:upper:]' '[:lower:]' | xargs)"
  case "$v" in
    true|1|yes|y) echo "true" ;;
    false|0|no|n|"") echo "false" ;;
    *) echo "false" ;;
  esac
}

mask() { [[ -n "${1:-}" ]] && echo "***" || echo ""; }

# ------------------------------------------------------------------------------
# Nginx config helpers
# ------------------------------------------------------------------------------

# Temporary HTTP-only config used by certbot for the ACME challenge
write_nginx_http_only() {
  local domain="$1"
  cat > /etc/nginx/sites-available/rtcloud << EOF
server {
    listen 80;
    server_name ${domain};
    root /var/www/html;
    location / { try_files \$uri \$uri/ =404; }
}
EOF
  ln -sf /etc/nginx/sites-available/rtcloud /etc/nginx/sites-enabled/rtcloud
  rm -f /etc/nginx/sites-enabled/default
}

# Full HTTPS reverse-proxy config (used after certs are available)
# Args: domain cert_path key_path keycloak_nginx_block
write_nginx_ssl_config() {
  local domain="$1"
  local cert_path="$2"
  local key_path="$3"
  local keycloak_block="$4"
  cat > /etc/nginx/sites-available/rtcloud << EOF
server {
    listen 80;
    server_name ${domain};
    return 301 https://\$host\$request_uri;
}

server {
    listen 443 ssl;
    server_name ${domain};

    ssl_certificate     ${cert_path};
    ssl_certificate_key ${key_path};
    ssl_protocols       TLSv1.2 TLSv1.3;
    ssl_ciphers         ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;
${keycloak_block}
    location / {
        proxy_pass         http://127.0.0.1:8080;
        proxy_set_header   Host              \$host;
        proxy_set_header   X-Real-IP         \$remote_addr;
        proxy_set_header   X-Forwarded-For   \$proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto \$scheme;
        proxy_read_timeout 120s;
        client_max_body_size 100M;
    }
}
EOF
  ln -sf /etc/nginx/sites-available/rtcloud /etc/nginx/sites-enabled/rtcloud
  rm -f /etc/nginx/sites-enabled/default
}

# Hardcoded: always use embedded Keycloak
EMBED_KEYCLOAK=true
KEYCLOAK_NGINX_BLOCK="    location /auth/ {
        proxy_pass              http://127.0.0.1:8090/auth/;
        proxy_set_header        Host              \$host;
        proxy_set_header        X-Real-IP         \$remote_addr;
        proxy_set_header        X-Forwarded-For   \$proxy_add_x_forwarded_for;
        proxy_set_header        X-Forwarded-Proto \$scheme;
        proxy_buffer_size       128k;
        proxy_buffers           4 256k;
        proxy_busy_buffers_size 256k;
        proxy_read_timeout      120s;
    }"

STATA_ENABLED="$(normalize_bool "${STATA_ENABLED:-false}")"
OPEN_REGISTRATION="$(normalize_bool "${OPEN_REGISTRATION:-true}")"

# Auto-generate DB passwords
MYSQL_PASSWORD="admin"
MYSQL_ROOT_PASSWORD="admin"

# Admin web UI password defaults to Keycloak admin password
ADMIN_PASSWORD="${ADMIN_PASSWORD:-admin}"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"

# Validate required fields
[[ -z "${KEYCLOAK_ADMIN_PASSWORD:-}" ]] && { echo "ERROR: KEYCLOAK_ADMIN_PASSWORD is required." >&2; exit 1; }
[[ -z "${DOMAIN:-}" ]]                  && { echo "ERROR: DOMAIN is required." >&2; exit 1; }
[[ -z "${LETSENCRYPT_EMAIL:-}" ]]       && { echo "ERROR: LETSENCRYPT_EMAIL is required." >&2; exit 1; }

# ==============================================================================
# 1. System update + Docker + Nginx
# ==============================================================================
echo "[1/7] Updating system and installing Docker and Nginx..."

export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get install -y -qq \
  curl ca-certificates gnupg lsb-release ufw nginx openssl

# Add Docker's official GPG key
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
  | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
chmod a+r /etc/apt/keyrings/docker.gpg

# Add Docker repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
  > /etc/apt/sources.list.d/docker.list

apt-get update -qq
apt-get install -y -qq \
  docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

systemctl enable --now docker
echo "  Docker $(docker --version) installed."

# ==============================================================================
# 2. Write docker-compose.production.yml
# ==============================================================================
echo "[2/7] Writing docker-compose.production.yml..."

mkdir -p /opt/rtcloud
cd /opt/rtcloud

cat > docker-compose.production.yml << 'COMPOSE_EOF'
version: '3.8'

services:
  mysql:
    image: mysql:8.0
    container_name: ${COMPOSE_PROJECT_NAME:-rtcloud}-mysql
    restart: ${RESTART_POLICY:-unless-stopped}
    command: --default-authentication-plugin=mysql_native_password --character-set-server=utf8 --collation-server=utf8_unicode_ci --sql-mode=NO_ENGINE_SUBSTITUTION

    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: ${MYSQL_DATABASE:-smartsurvey}
      MYSQL_USER: ${MYSQL_USER:-smartsurvey}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
      MYSQL_ROOT_HOST: '%'
      MYSQL_CHARSET: utf8mb4
      MYSQL_COLLATION: utf8mb4_unicode_ci

    volumes:
      - mysql_data:/var/lib/mysql
      - ./mysql-init:/docker-entrypoint-initdb.d

    networks:
      - rtcloud-net

    healthcheck:
      test: ["CMD-SHELL", "mysqladmin ping -h localhost -u root -p$$MYSQL_ROOT_PASSWORD"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s

  rtcloud:
    image: ${RTCLOUD_IMAGE:-rtawebteam/rta-smartsurvey:survey-dockerize}
    container_name: ${COMPOSE_PROJECT_NAME:-rtcloud}-app
    restart: ${RESTART_POLICY:-unless-stopped}
    entrypoint: ["/bin/entrypoint-production.sh"]

    depends_on:
      mysql:
        condition: service_healthy

    ports:
      - "127.0.0.1:${APP_PORT:-8080}:80"
      - "${SHINY_PORT:-3838}:3838"

    env_file:
      - .env

    volumes:
      - app_uploads:/var/www/html/smartsurvey/uploads
      - app_audios:/var/www/html/smartsurvey/audios
      - app_downloads:/var/www/html/smartsurvey/downloads
      - app_gallery:/var/www/html/smartsurvey/gallery
      - app_voicemail:/var/www/html/smartsurvey/voicemail
      - app_runtime:/var/www/html/smartsurvey/protected/runtime
      - app_v2_runtime:/var/www/html/smartsurvey/protected/modules/v2/runtime
      - app_cache:/var/www/html/smartsurvey/cache
      - app_tmp:/var/www/html/smartsurvey/tmp
      - app_analytics:/var/www/html/smartsurvey/analytics
      - app_aggregate:/var/www/html/smartsurvey/aggregate
      - app_converter:/var/www/html/smartsurvey/converter
      - shiny_data:/srv/shiny-server/smartsurvey
      - shiny_logs:/var/log/shiny-server
      - app_assets:/var/www/html/smartsurvey/assets

    networks:
      - rtcloud-net

    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 90s

    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  keycloak:
    image: quay.io/keycloak/keycloak:latest
    container_name: ${COMPOSE_PROJECT_NAME:-rtcloud}-keycloak
    restart: ${RESTART_POLICY:-unless-stopped}
    command: start --import-realm

    environment:
      KC_BOOTSTRAP_ADMIN_USERNAME: ${KEYCLOAK_ADMIN_USER:-admin}
      KC_BOOTSTRAP_ADMIN_PASSWORD: ${KEYCLOAK_ADMIN_PASSWORD:-}
      KC_HTTP_ENABLED: "true"
      KC_HTTP_RELATIVE_PATH: /auth
      KC_PROXY_HEADERS: xforwarded
      KC_HOSTNAME: ${KC_HOSTNAME}
      KC_HOSTNAME_STRICT: "false"
      KC_DB: mysql
      KC_DB_URL_DATABASE: ${KEYCLOAK_DB:-keycloak}
      KC_DB_URL_HOST: mysql
      KC_DB_USERNAME: ${KEYCLOAK_DB_USER:-keycloak}
      KC_DB_PASSWORD: ${KEYCLOAK_DB_PASSWORD:-}

    volumes:
      - ./keycloak-import:/opt/keycloak/data/import

    ports:
      - "127.0.0.1:${KEYCLOAK_PORT:-8090}:8080"

    depends_on:
      mysql:
        condition: service_healthy

    networks:
      - rtcloud-net

    healthcheck:
      test: ["CMD-SHELL", "(exec 3<>/dev/tcp/localhost/8080) 2>/dev/null && exit 0 || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 10
      start_period: 120s

    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

volumes:
  mysql_data:
    name: ${COMPOSE_PROJECT_NAME:-rtcloud}_mysql_data
  app_uploads:
    name: ${COMPOSE_PROJECT_NAME:-rtcloud}_uploads
  app_audios:
    name: ${COMPOSE_PROJECT_NAME:-rtcloud}_audios
  app_downloads:
    name: ${COMPOSE_PROJECT_NAME:-rtcloud}_downloads
  app_gallery:
    name: ${COMPOSE_PROJECT_NAME:-rtcloud}_gallery
  app_voicemail:
    name: ${COMPOSE_PROJECT_NAME:-rtcloud}_voicemail
  app_runtime:
    name: ${COMPOSE_PROJECT_NAME:-rtcloud}_runtime
  app_v2_runtime:
    name: ${COMPOSE_PROJECT_NAME:-rtcloud}_v2_runtime
  app_cache:
    name: ${COMPOSE_PROJECT_NAME:-rtcloud}_cache
  app_tmp:
    name: ${COMPOSE_PROJECT_NAME:-rtcloud}_tmp
  app_analytics:
    name: ${COMPOSE_PROJECT_NAME:-rtcloud}_analytics
  app_aggregate:
    name: ${COMPOSE_PROJECT_NAME:-rtcloud}_aggregate
  app_converter:
    name: ${COMPOSE_PROJECT_NAME:-rtcloud}_converter
  shiny_data:
    name: ${COMPOSE_PROJECT_NAME:-rtcloud}_shiny_data
  shiny_logs:
    name: ${COMPOSE_PROJECT_NAME:-rtcloud}_shiny_logs
  app_assets:
    name: ${COMPOSE_PROJECT_NAME:-rtcloud}_assets

networks:
  rtcloud-net:
    name: ${COMPOSE_PROJECT_NAME:-rtcloud}_network
    driver: bridge
COMPOSE_EOF

echo "  docker-compose.production.yml written."

# ==============================================================================
# 3. Write .env
# ==============================================================================
echo "[3/7] Writing .env..."

EFFECTIVE_PROJECT_URL="${PROJECT_URL:-${DOMAIN}}"

KEYCLOAK_DB_PASS="admin"
KEYCLOAK_CLIENT_SECRET_GEN="admin"
KEYCLOAK_MOBILE_REDIRECT_URI="vn.rta.rtsurvey.auth://callback"

cat > .env << ENV_EOF
# Generated by DigitalOcean User-Data (Embedded Keycloak) on $(date)

# Project
PROJECT_ID=${PROJECT_ID}
PROJECT_TYPE=rtsurvey
PROJECT_URL=${DOMAIN}
PROJECT_PORT=443
HTTP_PROTOCOL=https

# Database
MYSQL_HOST=mysql
MYSQL_PORT=3306
MYSQL_DATABASE=${PROJECT_ID}
MYSQL_USER=${PROJECT_ID}
MYSQL_PASSWORD=${MYSQL_PASSWORD}
MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}

# Admin
ADMIN_PASSWORD=${ADMIN_PASSWORD}

# Ports (app bound to localhost only - Nginx terminates SSL on 80/443)
APP_PORT=8080
SHINY_PORT=3838
KEYCLOAK_PORT=8090

# Runtime
RUN_ENV=prod
RUN_MODE=admin
TZ=${TZ}
LOG_LEVEL=info

# Security
CSRF_VALIDATION_ENABLED=true
GII_ENABLED=false
OPEN_REGISTRATION=${OPEN_REGISTRATION}

# Docker
COMPOSE_PROJECT_NAME=rtcloud
RESTART_POLICY=unless-stopped
RTCLOUD_IMAGE=${RTCLOUD_IMAGE}

# SSO mode
EMBED_KEYCLOAK=true
AUTH_PROVIDER=embedded-keycloak

# Stata14
STATA_ENABLED=${STATA_ENABLED}
STATA_BIN_PATH=/usr/bin/stata
STATA_LICENSE_B64=${STATA_LICENSE_B64:-}

# ----------------------------------------------------------------------------
# SSO - Embedded Keycloak
# ----------------------------------------------------------------------------
OIDC_ISSUER_URL=https://${EFFECTIVE_PROJECT_URL}/auth/realms/rtsurvey
OIDC_CLIENT_ID=${PROJECT_ID}
OIDC_CLIENT_SECRET=${KEYCLOAK_CLIENT_SECRET_GEN}
OIDC_REDIRECT_URI=https://${EFFECTIVE_PROJECT_URL}/cpms/cpmsSite/auth
OIDC_DISCOVERY_URL=http://keycloak:8080/auth/realms/rtsurvey/.well-known/openid-configuration
OIDC_MOBILE_CLIENT_ID=${PROJECT_ID}
OIDC_MOBILE_REDIRECT_URI=${KEYCLOAK_MOBILE_REDIRECT_URI}

# Keycloak container config
KC_HOSTNAME=https://${EFFECTIVE_PROJECT_URL}/auth
KC_HEALTH_ENABLED=true
KEYCLOAK_ADMIN_USER=admin
KEYCLOAK_ADMIN_PASSWORD=${KEYCLOAK_ADMIN_PASSWORD}
KEYCLOAK_DB=keycloak
KEYCLOAK_DB_USER=keycloak
KEYCLOAK_DB_PASSWORD=${KEYCLOAK_DB_PASS}
ENV_EOF

chmod 600 .env
echo "  .env written (permissions: 600)."

echo ""
echo "=== SSO CONFIG ==="
echo "AUTH_PROVIDER=embedded-keycloak"
echo "OIDC_ISSUER_URL=https://${EFFECTIVE_PROJECT_URL}/auth/realms/rtsurvey"
echo "OIDC_CLIENT_ID=${PROJECT_ID}"
echo "OIDC_CLIENT_SECRET=$(mask "${KEYCLOAK_CLIENT_SECRET_GEN}")"
echo "KC_HOSTNAME=https://${EFFECTIVE_PROJECT_URL}/auth"
echo "KEYCLOAK_ADMIN_PASSWORD=$(mask "${KEYCLOAK_ADMIN_PASSWORD}")"
echo "=================="
echo ""

# ==============================================================================
# 4. Keycloak setup files
# ==============================================================================
mkdir -p /opt/rtcloud/mysql-init /opt/rtcloud/keycloak-import

echo "  [Keycloak] Writing MySQL init script..."
cat > /opt/rtcloud/mysql-init/01-keycloak-db.sql << SQL_EOF
CREATE DATABASE IF NOT EXISTS \`keycloak\` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'keycloak'@'%' IDENTIFIED WITH mysql_native_password BY '${KEYCLOAK_DB_PASS}';
GRANT ALL PRIVILEGES ON \`keycloak\`.* TO 'keycloak'@'%';
FLUSH PRIVILEGES;
SQL_EOF

echo "  [Keycloak] Writing realm import (realm=rtsurvey, client_id=${PROJECT_ID})..."
cat > /opt/rtcloud/keycloak-import/rtsurvey-realm.json << REALM_EOF
{
  "realm": "rtsurvey",
  "enabled": true,
  "ssoSessionIdleTimeout": 2592000,
  "ssoSessionMaxLifespan": 31536000,
  "sslRequired": "external",
  "registrationAllowed": false,
  "loginWithEmailAllowed": true,
  "clients": [
    {
      "clientId": "${PROJECT_ID}",
      "name": "${PROJECT_ID}",
      "enabled": true,
      "protocol": "openid-connect",
      "publicClient": true,
      "redirectUris": [
        "https://${EFFECTIVE_PROJECT_URL}/*",
        "vn.rta.rtsurvey.auth:/*",
        "vn.rta.rtsurvey.logout:/*"
      ],
      "webOrigins": [
        "https://${EFFECTIVE_PROJECT_URL}"
      ],
      "standardFlowEnabled": true,
      "directAccessGrantsEnabled": false,
      "serviceAccountsEnabled": false
    }
  ],
  "users": [
    {
      "username": "admin",
      "email": "admin@${EFFECTIVE_PROJECT_URL}",
      "enabled": true,
      "credentials": [
        {
          "type": "password",
          "value": "${KEYCLOAK_ADMIN_PASSWORD}",
          "temporary": false
        }
      ],
      "realmRoles": ["offline_access", "uma_authorization"]
    }
  ]
}
REALM_EOF
echo "  [Keycloak] Realm import file written."

# ==============================================================================
# 5. Pull image and start services
# ==============================================================================
echo "[5/7] Pulling image and starting services..."
docker compose -f docker-compose.production.yml pull
docker compose -f docker-compose.production.yml up -d
echo "  Services started."

echo "  [Keycloak] Waiting for rtcloud-app to be healthy before patching admin email..."
for i in $(seq 1 30); do
  STATUS=$(docker inspect --format='{{.State.Health.Status}}' rtcloud-app 2>/dev/null || echo "missing")
  if [[ "${STATUS}" == "healthy" ]]; then break; fi
  echo "    waiting... (${i}/30)"
  sleep 10
done
PATCH_OK=false
for attempt in $(seq 1 5); do
  if docker exec rtcloud-mysql mysql -u root -p"${MYSQL_ROOT_PASSWORD}" "${PROJECT_ID}" \
      -e "UPDATE ss_user SET email='admin@${EFFECTIVE_PROJECT_URL}' WHERE username='admin';"; then
    PATCH_OK=true; break
  fi
  echo "    DB patch attempt ${attempt}/5 failed, retrying in 5s..."
  sleep 5
done
if [[ "${PATCH_OK}" == "true" ]]; then
  echo "  [Keycloak] Admin user email set to admin@${EFFECTIVE_PROJECT_URL}"
else
  echo "WARNING: Could not patch admin email -- set it manually after login." >&2
fi

# ==============================================================================
# 6. SSL certificates + Nginx
# ==============================================================================
echo "[6/7] Configuring SSL and starting Nginx..."

systemctl enable nginx

# Print server IP early so user can add DNS record while waiting
SERVER_IP=$(curl -s https://api.ipify.org || hostname -I | awk '{print $1}')
echo ""
echo "============================================================"
echo " Server IP : ${SERVER_IP}"
echo " Add this DNS A record now if you haven't already:"
echo "   ${DOMAIN}  ->  ${SERVER_IP}"
echo " The script will retry Certbot every 60s until DNS resolves."
echo "============================================================"
echo ""

# Serve HTTP temporarily for the ACME challenge
mkdir -p /var/www/html
write_nginx_http_only "${DOMAIN}"
systemctl is-active nginx && systemctl reload nginx || systemctl start nginx

# Install Certbot
snap install --classic certbot
ln -sf /snap/bin/certbot /usr/bin/certbot

LE_CERT="/etc/letsencrypt/live/${DOMAIN}/fullchain.pem"
LE_KEY="/etc/letsencrypt/live/${DOMAIN}/privkey.pem"

# If cert already exists (re-run), skip certbot
CERT_OK=false
if [ -f "${LE_CERT}" ]; then
  echo "  [SSL] Certificate already exists, skipping certbot."
  CERT_OK=true
else
  # Retry until DNS propagates (up to 60 attempts = ~60 min)
  MAX_ATTEMPTS=60
  for attempt in $(seq 1 ${MAX_ATTEMPTS}); do
    echo "  [SSL] Certbot attempt ${attempt}/${MAX_ATTEMPTS}..."
    CERTBOT_OUT=$(certbot certonly --webroot -w /var/www/html -n --agree-tos -m "${LETSENCRYPT_EMAIL}" -d "${DOMAIN}" 2>&1) && CERTBOT_EXIT=0 || CERTBOT_EXIT=$?
    echo "${CERTBOT_OUT}"
    if [[ ${CERTBOT_EXIT} -eq 0 ]]; then
      CERT_OK=true; break
    fi
    if echo "${CERTBOT_OUT}" | grep -q "too many certificates"; then
      RETRY_AFTER=$(echo "${CERTBOT_OUT}" | grep -o "retry after [^:]*" | head -1 || true)
      echo "  [SSL] ERROR: Let's Encrypt rate limit hit. ${RETRY_AFTER}. Redeploy after that time." >&2
      break
    fi
    echo "  [SSL] DNS not ready yet. Retrying in 60s... (${DOMAIN} must point to ${SERVER_IP})"
    sleep 60
  done
fi

[[ "${CERT_OK}" != "true" ]] && { echo "ERROR: Could not obtain SSL cert. Check DNS or rate limits." >&2; exit 1; }

write_nginx_ssl_config "${DOMAIN}" "${LE_CERT}" "${LE_KEY}" "${KEYCLOAK_NGINX_BLOCK}"
nginx -t && systemctl reload nginx
echo "  Nginx live with Let's Encrypt cert (auto-renews via snap certbot.timer)."

# ==============================================================================
# 7. Firewall
# ==============================================================================
echo "[7/7] Configuring firewall..."
ufw --force enable
ufw allow ssh
ufw allow "Nginx Full"   # ports 80 + 443
ufw allow 3838/tcp       # Shiny (direct)
echo "  Firewall: SSH, 80, 443, 3838 allowed."

# ==============================================================================
# Done
# ==============================================================================
SERVER_IP=$(curl -s https://api.ipify.org || hostname -I | awk '{print $1}')

echo ""
echo "============================================================"
echo " rtCloud deployment complete! (Embedded Keycloak)"
echo "============================================================"
echo " Server IP : ${SERVER_IP}"
echo " Domain    : ${DOMAIN}"
echo ""
echo " App URL   : https://${DOMAIN}"
echo " Admin     : admin / ${ADMIN_PASSWORD}"
echo " DB Name   : ${PROJECT_ID}"
echo " DB User   : ${PROJECT_ID}"
echo " DB Pass   : ${MYSQL_PASSWORD}"
echo " DB Root   : ${MYSQL_ROOT_PASSWORD}"
echo " SSL       : Let's Encrypt (certbot)"
echo " Stata     : ${STATA_ENABLED}"
echo ""
echo " *** EMBEDDED KEYCLOAK -- SSO auto-configured ***"
echo ""
echo "   Realm    : rtsurvey"
echo "   Client ID: ${PROJECT_ID}"
echo ""
echo "   Keycloak Admin Console:"
echo "     https://${DOMAIN}/auth/admin"
echo "     Login: admin / ${KEYCLOAK_ADMIN_PASSWORD}"
echo ""
echo "   App login will use Keycloak -- no external provider needed."
echo ""
echo " Note: Let's Encrypt cert auto-renews every 60 days via snap certbot.timer."
echo ""
echo " Logs  : /var/log/rtcloud-setup.log"
echo " Files : /opt/rtcloud/"
echo " To change passwords, SSH in and edit /opt/rtcloud/.env"
echo ""
echo " !! SECURITY: All passwords default to 'admin'."
echo "    Change them immediately after first login:"
echo "    - App admin : https://${DOMAIN} > Settings"
echo "    - Keycloak  : https://${DOMAIN}/auth/admin"
echo "    - DB        : edit /opt/rtcloud/.env then docker compose up -d"
echo "============================================================"
