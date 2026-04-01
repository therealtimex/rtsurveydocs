---
weight: 5
title: "Manutenção"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "build"
toc: true
description: "Manutenção do dia a dia para uma instância rtCloud auto-alojada: atualizar, fazer backup, restaurar e resolver problemas comuns."
---

## Comandos Comuns

Use estes comandos regularmente para gerir os seus contentores rtCloud. Execute-os a partir do diretório que contém `docker-compose.production.yml`.

```bash
# Verificar estado e saúde de todos os contentores
docker compose -f docker-compose.production.yml ps

# Ver logs em tempo real (todos os serviços)
docker compose -f docker-compose.production.yml logs -f

# Ver logs apenas da aplicação
docker compose -f docker-compose.production.yml logs -f rtcloud

# Reiniciar um único contentor
docker compose -f docker-compose.production.yml restart rtcloud

# Parar todos os serviços
docker compose -f docker-compose.production.yml down

# Iniciar todos os serviços
docker compose -f docker-compose.production.yml up -d

# Abrir uma shell dentro do contentor da aplicação
docker compose -f docker-compose.production.yml exec rtcloud bash
```

---

## Atualização

As atualizações do rtCloud são distribuídas como novas tags de imagem Docker. A atualização obtém a imagem mais recente e recria o contentor da aplicação. As migrações de base de dados são executadas automaticamente na inicialização.

**1. Obter a imagem mais recente:**

```bash
docker compose -f docker-compose.production.yml pull
```

**2. Recriar o contentor da aplicação:**

```bash
docker compose -f docker-compose.production.yml up -d
```

O Docker substitui apenas os contentores cuja imagem foi alterada. O contentor MySQL e todos os volumes nomeados não são afetados.

### Fixar uma Versão

Para atualizar para uma versão específica em vez de `latest`, atualize `RTCLOUD_IMAGE` em `.env`:

```dotenv
RTCLOUD_IMAGE=rtawebteam/rta-smartsurvey:1.2.3
```

Depois execute `docker compose pull` e `up -d` como acima.

### Fazer Downgrade

O downgrade geralmente não é recomendado, pois as migrações de base de dados não podem ser revertidas. Se for necessário um downgrade, restaure a partir de um backup de base de dados feito antes da atualização.

---

## Backup e Restauro

### Fazer Backup da Base de Dados

Execute este comando para exportar a base de dados da aplicação para um ficheiro SQL:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > backup-$(date +%Y%m%d-%H%M%S).sql
```

O ficheiro de backup é gravado no seu diretório atual no host.

### Restaurar a Base de Dados

```bash
docker compose -f docker-compose.production.yml exec -T mysql \
  mysql -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  < backup-20240101-120000.sql
```

### Fazer Backup dos Ficheiros Carregados

As submissões de inquérito frequentemente incluem ficheiros carregados (fotos, áudio, documentos) armazenados em volumes Docker nomeados. Faça backup deles separadamente da base de dados:

```bash
# Backup de uploads
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/uploads-$(date +%Y%m%d).tar.gz -C /data .

# Backup de gravações de áudio
docker run --rm \
  -v rtcloud_audios:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/audios-$(date +%Y%m%d).tar.gz -C /data .
```

Substitua `rtcloud_uploads` e `rtcloud_audios` pelos seus nomes de volume reais (prefixados por `COMPOSE_PROJECT_NAME`) se alterou o valor predefinido.

### Restaurar Ficheiros Carregados

```bash
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar xzf /backup/uploads-20240101.tar.gz -C /data
```

### Backups Diários Automatizados

Adicione um trabalho cron no host para executar backups automaticamente. Edite o crontab do root com `crontab -e`:

```cron
# Backup diário da base de dados às 2:00 da manhã, manter 30 dias de histórico
0 2 * * * cd /opt/rtcloud && docker compose -f docker-compose.production.yml exec -T mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > /backups/db-$(date +\%Y\%m\%d).sql && \
  find /backups -name "db-*.sql" -mtime +30 -delete
```

---

## Resolução de Problemas

### O contentor da aplicação não inicia

Verifique os logs do contentor para mensagens de erro:

```bash
docker compose -f docker-compose.production.yml logs rtcloud
```

Causas comuns:
- Variáveis de ambiente em `.env` em falta ou inválidas
- MySQL ainda não pronto (aguarde 60 segundos e verifique novamente)
- Conflito de porta — outro processo já está a usar `APP_PORT`

### MySQL não saudável

```bash
docker compose -f docker-compose.production.yml logs mysql
```

Causas comuns:
- `MYSQL_ROOT_PASSWORD` não definido em `.env`
- Volume de dados corrompido (raro — verifique espaço em disco com `df -h`)

O MySQL pode demorar 30–60 segundos para inicializar na primeira inicialização. Aguarde e verifique novamente antes de assumir falha.

### Porta já em uso

Altere `APP_PORT` ou `SHINY_PORT` em `.env` para uma porta livre e recrie os contentores:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate
```

Para descobrir o que está a usar uma porta no host:

```bash
lsof -i :8080
```

### 400 CSRF Token Não Pôde Ser Verificado

Este erro aparece em ambientes locais ou de proxy reverso onde a origem do pedido não corresponde ao host esperado. Desative a validação CSRF apenas para desenvolvimento local:

```dotenv
CSRF_VALIDATION_ENABLED=false
```

Depois reinicie a aplicação:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

> Não desative a validação CSRF em produção. Se este erro ocorrer em produção, certifique-se de que o seu proxy reverso está a encaminhar os cabeçalhos `Host` e `X-Forwarded-For` corretos.

### Esqueceu a Palavra-passe de Administrador

Redefina a palavra-passe de administrador diretamente na base de dados. Ligue ao contentor MySQL e atualize o hash da palavra-passe:

**Passo 1** — Gere o novo hash de palavra-passe. Substitua `newpassword` pela palavra-passe desejada:

```bash
docker compose -f docker-compose.production.yml exec rtcloud php -r "
  \$salt = trim(shell_exec(\"mysql -h mysql -u root -p\\\"\${MYSQL_ROOT_PASSWORD}\\\" \${MYSQL_DATABASE} -se \\\"SELECT salt FROM ss_user WHERE username='admin';\\\"\"));
  echo md5(\$salt . 'newpassword') . PHP_EOL;
"
```

**Passo 2** — Atualize o hash na base de dados:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysql -u root -p"${MYSQL_ROOT_PASSWORD}" smartsurvey \
  -e "UPDATE ss_user SET password='<hash_from_step_1>' WHERE username='admin';"
```

### O contentor continua a reiniciar

Verifique se a verificação de saúde está a falhar:

```bash
docker compose -f docker-compose.production.yml ps
docker inspect rtcloud-app --format '{{json .State.Health}}'
```

A verificação de saúde da aplicação chama o endpoint `/health`. Se falhar repetidamente, verifique os logs da aplicação para erros de inicialização.

### Disco cheio

Identifique o que está a consumir espaço:

```bash
# Verificar uso do disco do host
df -h

# Verificar uso do disco Docker (imagens, contentores, volumes)
docker system df

# Remover imagens não utilizadas e contentores parados (seguro de executar)
docker system prune
```

Não use `docker system prune --volumes` pois isto eliminará os dados da aplicação.

---

## Verificações de Saúde

Cada serviço tem uma verificação de saúde automática. O estado do contentor reflete o resultado:

| Contentor | Método de Verificação | Período de Início | Intervalo |
|-----------|----------------------|-------------------|-----------|
| `rtcloud-app` | HTTP GET `/health` | 90 segundos | 30 segundos |
| `rtcloud-mysql` | `mysqladmin ping` | 30 segundos | 10 segundos |
| `rtcloud-keycloak` | HTTP GET `:9000/health/live` | 120 segundos | 30 segundos |

Os contentores com uma verificação de saúde a falhar são automaticamente reiniciados de acordo com a configuração `RESTART_POLICY` (predefinição: `unless-stopped`).
