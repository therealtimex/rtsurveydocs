---
weight: 5
title: "Manutenção"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "build"
toc: true
description: "Manutenção do dia a dia para uma instância do rtCloud com hospedagem própria: atualização, backup, restauração e solução de problemas comuns."
---

## Comandos comuns

Use estes comandos regularmente para gerenciar seus contêineres do rtCloud. Execute-os no diretório que contém `docker-compose.production.yml`.

```bash
# Verificar status e integridade de todos os contêineres
docker compose -f docker-compose.production.yml ps

# Ver logs em tempo real (todos os serviços)
docker compose -f docker-compose.production.yml logs -f

# Ver logs apenas do aplicativo
docker compose -f docker-compose.production.yml logs -f rtcloud

# Reiniciar um único contêiner
docker compose -f docker-compose.production.yml restart rtcloud

# Parar todos os serviços
docker compose -f docker-compose.production.yml down

# Iniciar todos os serviços
docker compose -f docker-compose.production.yml up -d

# Abrir um shell dentro do contêiner do aplicativo
docker compose -f docker-compose.production.yml exec rtcloud bash
```

---

## Atualização

As atualizações do rtCloud são distribuídas como novas tags de imagem Docker. A atualização baixa a imagem mais recente e recria o contêiner do aplicativo. As migrações de banco de dados são executadas automaticamente na inicialização.

**1. Baixe a imagem mais recente:**

```bash
docker compose -f docker-compose.production.yml pull
```

**2. Recrie o contêiner do aplicativo:**

```bash
docker compose -f docker-compose.production.yml up -d
```

O Docker substitui apenas os contêineres cuja imagem foi alterada. O contêiner MySQL e todos os volumes nomeados não são afetados.

### Fixando uma versão

Para atualizar para uma versão específica em vez de `latest`, atualize `RTCLOUD_IMAGE` no `.env`:

```dotenv
RTCLOUD_IMAGE=rtawebteam/rta-smartsurvey:1.2.3
```

Em seguida, execute `docker compose pull` e `up -d` como acima.

### Downgrade

O downgrade geralmente não é recomendado, pois as migrações de banco de dados não podem ser revertidas. Se um downgrade for necessário, restaure a partir de um backup de banco de dados feito antes da atualização.

---

## Backup e restauração

### Fazer backup do banco de dados

Execute este comando para exportar o banco de dados do aplicativo para um arquivo SQL:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > backup-$(date +%Y%m%d-%H%M%S).sql
```

O arquivo de backup é gravado no seu diretório atual no host.

### Restaurar o banco de dados

```bash
docker compose -f docker-compose.production.yml exec -T mysql \
  mysql -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  < backup-20240101-120000.sql
```

### Fazer backup dos arquivos enviados

Os envios de pesquisa frequentemente incluem arquivos enviados (fotos, áudio, documentos) armazenados em volumes Docker nomeados. Faça backup deles separadamente do banco de dados:

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

Substitua `rtcloud_uploads` e `rtcloud_audios` pelos seus nomes de volumes reais (prefixados por `COMPOSE_PROJECT_NAME`) se você alterou o padrão.

### Restaurar arquivos enviados

```bash
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar xzf /backup/uploads-20240101.tar.gz -C /data
```

### Backups diários automatizados

Adicione um job cron no host para executar backups automaticamente. Edite o crontab do root com `crontab -e`:

```cron
# Backup diário do banco de dados às 2:00, mantendo 30 dias de histórico
0 2 * * * cd /opt/rtcloud && docker compose -f docker-compose.production.yml exec -T mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > /backups/db-$(date +\%Y\%m\%d).sql && \
  find /backups -name "db-*.sql" -mtime +30 -delete
```

---

## Solução de problemas

### Contêiner do aplicativo não inicia

Verifique os logs do contêiner em busca de mensagens de erro:

```bash
docker compose -f docker-compose.production.yml logs rtcloud
```

Causas comuns:
- Variáveis de ambiente ausentes ou inválidas no `.env`
- MySQL ainda não pronto (aguarde 60 segundos e verifique novamente)
- Conflito de porta — outro processo já está usando `APP_PORT`

### MySQL não saudável

```bash
docker compose -f docker-compose.production.yml logs mysql
```

Causas comuns:
- `MYSQL_ROOT_PASSWORD` não definido no `.env`
- Volume de dados corrompido (raro — verifique o espaço em disco com `df -h`)

O MySQL pode levar de 30 a 60 segundos para inicializar na primeira inicialização. Aguarde e verifique novamente antes de assumir falha.

### Porta já em uso

Altere `APP_PORT` ou `SHINY_PORT` no `.env` para uma porta livre, depois recrie os contêineres:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate
```

Para descobrir o que está usando uma porta no host:

```bash
lsof -i :8080
```

### Erro 400 de token CSRF não pôde ser verificado

Este erro aparece em ambientes locais ou de proxy reverso onde a origem da solicitação não corresponde ao host esperado. Desabilite a validação CSRF apenas para desenvolvimento local:

```dotenv
CSRF_VALIDATION_ENABLED=false
```

Depois reinicie o aplicativo:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

> Não desabilite a validação CSRF em produção. Se este erro ocorrer em produção, certifique-se de que seu proxy reverso está encaminhando os cabeçalhos `Host` e `X-Forwarded-For` corretos.

### Esqueci a senha do administrador

Redefina a senha do administrador diretamente no banco de dados. Conecte-se ao contêiner MySQL e atualize o hash da senha:

**Etapa 1** — Gere o novo hash de senha. Substitua `novasenha` pela senha desejada:

```bash
docker compose -f docker-compose.production.yml exec rtcloud php -r "
  \$salt = trim(shell_exec(\"mysql -h mysql -u root -p\\\"\${MYSQL_ROOT_PASSWORD}\\\" \${MYSQL_DATABASE} -se \\\"SELECT salt FROM ss_user WHERE username='admin';\\\"\"));
  echo md5(\$salt . 'novasenha') . PHP_EOL;
"
```

**Etapa 2** — Atualize o hash no banco de dados:

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysql -u root -p"${MYSQL_ROOT_PASSWORD}" smartsurvey \
  -e "UPDATE ss_user SET password='<hash_da_etapa_1>' WHERE username='admin';"
```

### Contêiner continua reiniciando

Verifique se a verificação de integridade está falhando:

```bash
docker compose -f docker-compose.production.yml ps
docker inspect rtcloud-app --format '{{json .State.Health}}'
```

A verificação de integridade do aplicativo chama o endpoint `/health`. Se falhar repetidamente, verifique os logs do aplicativo em busca de erros de inicialização.

### Disco cheio

Identifique o que está consumindo espaço:

```bash
# Verificar uso do disco do host
df -h

# Verificar uso do disco do Docker (imagens, contêineres, volumes)
docker system df

# Remover imagens não utilizadas e contêineres parados (seguro de executar)
docker system prune
```

Não use `docker system prune --volumes`, pois isso excluirá os dados do aplicativo.

---

## Verificações de integridade

Cada serviço tem uma verificação de integridade automática. O status do contêiner reflete o resultado:

| Contêiner | Método de verificação | Período de início | Intervalo |
|-----------|----------------------|-------------------|-----------|
| `rtcloud-app` | HTTP GET `/health` | 90 segundos | 30 segundos |
| `rtcloud-mysql` | `mysqladmin ping` | 30 segundos | 10 segundos |
| `rtcloud-keycloak` | HTTP GET `:9000/health/live` | 120 segundos | 30 segundos |

Contêineres com verificação de integridade com falha são automaticamente reiniciados de acordo com a configuração `RESTART_POLICY` (padrão: `unless-stopped`).
