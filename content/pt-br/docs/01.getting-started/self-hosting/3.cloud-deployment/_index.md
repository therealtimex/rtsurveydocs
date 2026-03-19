---
weight: 3
title: "Implantação em nuvem"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud_upload"
toc: true
description: "Implante o rtCloud nos principais provedores de nuvem com scripts automatizados para DigitalOcean, AWS EC2, Google Cloud e Linode."
---

O repositório de implantação inclui scripts de provisionamento automatizado para os principais provedores de nuvem. Cada script é executado na primeira inicialização de um servidor **Ubuntu 22.04 LTS** novo e realiza uma configuração completamente autônoma:

- Instala o Docker e o Docker Compose
- Gera senhas aleatórias seguras para todos os serviços internos
- Escreve `docker-compose.production.yml` e `.env`
- Configura o Nginx como proxy reverso
- Obtém um certificado TLS gratuito do Let's Encrypt (com novas tentativas automáticas até que o DNS seja resolvido)
- Configura o firewall UFW
- Opcionalmente implanta o servidor SSO Keycloak integrado
- Exibe um resumo completo da implantação com todas as credenciais

A configuração é concluída em **5 a 10 minutos** em uma instância padrão.

---

## Escolhendo um script

Existem múltiplas variantes de scripts dependendo do seu provedor de nuvem e configuração de SSO:

| Script | Provedor | Modo SSO | Melhor para |
|--------|----------|----------|-------------|
| `digitalocean-droplet-keycloak-embed.sh` | DigitalOcean | Keycloak integrado | SSO simples e autossuficiente |
| `digitalocean-droplet.sh` | DigitalOcean | Keycloak ou OIDC externo | Controle total |
| `linode-stackscript-keycloak-embed.sh` | Linode | Keycloak integrado | Configuração baseada em formulário, mais simples |
| `linode-stackscript-oidc.sh` | Linode | Somente OIDC externo | Provedor de identidade existente |
| `linode-stackscript.sh` | Linode | Keycloak ou OIDC externo | Controle total |
| `aws-ec2.sh` | AWS EC2 | Keycloak ou OIDC externo | Implantações AWS |
| `gcp-compute.sh` | Google Cloud | Keycloak ou OIDC externo | Implantações GCP |

> **Recomendado para a maioria dos usuários:** Use a variante `keycloak-embed`. Ela inclui um servidor de identidade Keycloak integrado e requer o mínimo de campos de configuração.

---

## Guia de dimensionamento de servidores

| Caso de uso | RAM | Disco | Exemplo |
|-------------|-----|-------|---------|
| Avaliação / desenvolvimento | 2 GB | 25 GB | DO Basic $18/mês, t3.small, e2-small |
| Equipe pequena (< 50 usuários) | 4 GB | 40 GB | DO Basic $24/mês, t3.medium, e2-medium |
| Produção (> 50 usuários) | 8 GB | 80 GB | DO General $48/mês, t3.large, n2-standard-2 |

> O Keycloak integrado requer pelo menos **4 GB de RAM**. Use 2 GB apenas para avaliação sem Keycloak.

---

## Configuração de DNS

Todos os scripts requerem um domínio com um **registro A apontando para o IP do seu servidor** antes que o Let's Encrypt possa emitir um certificado.

O script exibe o IP do seu servidor no início do processo de configuração:

```
============================================================
 IP do servidor : 139.162.51.85
 Adicione este registro A de DNS agora, se ainda não o fez:
   meuapp.exemplo.com.br  ->  139.162.51.85
 O script repetirá o Certbot a cada 60s até que o DNS seja resolvido.
============================================================
```

O script **tenta novamente automaticamente** o Let's Encrypt a cada 60 segundos por até 1 hora. Basta adicionar o registro DNS e aguardar — não é necessário reiniciar.

> **Limite de taxa:** O Let's Encrypt permite no máximo **5 certificados por domínio a cada 7 dias**. Evite implantar e destruir servidores repetidamente com o mesmo domínio. Se você atingir o limite, o script exibirá um timestamp `tente novamente após` e parará imediatamente.

---

## Lista de verificação pós-implantação

- [ ] O aplicativo abre em `https://seu-dominio.com.br`
- [ ] Entre com `admin` e a senha que você configurou
- [ ] Todos os contêineres estão saudáveis: `docker compose -f /opt/rtcloud/docker-compose.production.yml ps`
- [ ] A renovação do Let's Encrypt funciona: `certbot renew --dry-run`
- [ ] A porta 3306 do MySQL **não** está exposta: `ufw status`
- [ ] Configure um backup diário do banco de dados (consulte [Manutenção](../maintenance))

---

## Solução de problemas

### Verifique o log completo de configuração

```bash
# Linode
tail -200 /var/log/stackscript.log

# DigitalOcean / AWS / GCP
tail -200 /var/log/rtcloud-setup.log
```

### Limite de taxa do Let's Encrypt

Se você vir `too many certificates` no log, atingiu o limite de 5 certificados por 7 dias. O log mostra o tempo exato de nova tentativa:

```
[SSL] ERROR: Let's Encrypt rate limit hit. retry after 2026-03-15 16:22 UTC.
```

Aguarde até esse momento e reimplante.

### Keycloak permanece não saudável

Certifique-se de que o servidor tem pelo menos 4 GB de RAM, depois verifique os logs:

```bash
docker logs rtcloud-keycloak --tail 50
free -h
```

### Configuração SSL não aplicada após o certbot

Se o certificado foi emitido, mas o Nginx ainda mostra apenas HTTP, verifique o log em busca da linha de erro e recarregue o Nginx manualmente:

```bash
nginx -t && systemctl reload nginx
```
