---
weight: 115
title: "Hospedagem própria"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Implante e gerencie sua própria instância do rtCloud usando o Docker. Controle total sobre seus dados, infraestrutura e configuração."
---

Execute o rtCloud em sua própria infraestrutura usando o Docker Compose. A hospedagem própria oferece propriedade completa dos seus dados, rede e ambiente de implantação — ideal para organizações com requisitos de residência de dados, redes isoladas ou necessidades de infraestrutura personalizada.

## O que é a hospedagem própria do rtCloud?

A hospedagem própria do rtCloud é uma imagem oficial do Docker que empacota toda a plataforma rtCloud em uma pilha de contêineres portátil que você pode executar em qualquer servidor Linux. A pilha inclui:

| Serviço | Descrição |
|---------|-----------|
| **rtCloud App** | Aplicativo web Apache 2.4 + PHP 7.4 com fila de processamento em segundo plano integrada (Beanstalkd), servidor de análise (Shiny) e tarefas agendadas |
| **MySQL 8.0** | Banco de dados relacional para todos os dados de aplicativos e pesquisas |
| **Keycloak** *(opcional)* | Servidor de Single Sign-On integrado para gerenciamento de identidade empresarial |

## Quando hospedar por conta própria

A hospedagem própria é a escolha certa quando você:

- Exige **soberania de dados** — todos os dados permanecem dentro de sua própria infraestrutura
- Opera em uma **rede isolada ou restrita** sem acesso à nuvem externa
- Tem **requisitos de conformidade** (GDPR, HIPAA, políticas de dados governamentais) que exigem armazenamento local
- Precisa integrar com um **provedor de identidade interno** (Active Directory, LDAP, SAML)
- Quer **personalizar recursos** — alocação de CPU, RAM e armazenamento nos seus termos

## Nesta seção

| Página | Descrição |
|--------|-----------|
| [Início rápido](quick-start) | Coloque o rtCloud em funcionamento em um servidor em menos de 10 minutos |
| [Referência de configuração](configuration) | Lista completa de todas as variáveis de ambiente e seus padrões |
| [Implantação em nuvem](cloud-deployment) | Scripts automatizados de um clique para DigitalOcean, AWS, GCP e Linode |
| [Autenticação SSO](sso-authentication) | Configurar Keycloak, OIDC externo ou Azure AD |
| [Manutenção](maintenance) | Atualizar, fazer backup, restaurar e solucionar problemas da sua instância |

## Visão geral da arquitetura

A implantação é executada como um conjunto de contêineres Docker conectados em uma rede interna:

```
┌────────────────────────────────────────┐
│            rtcloud-app                 │
│  Apache 2.4 (porta 80)                 │
│  Aplicativo PHP 7.4                    │
│  Fila Beanstalkd (interna)             │
│  Shiny Server (porta 3838)             │
│  Agendador Cron                        │
└─────────────────┬──────────────────────┘
                  │ rtcloud-net (bridge)
┌─────────────────▼──────────────────────┐
│            rtcloud-mysql               │
│  MySQL 8.0 (porta 3306, somente interna)|
└────────────────────────────────────────┘
```

Quando o SSO está habilitado, um terceiro contêiner é executado junto:

```
┌─────────────────────────────────────────┐
│            rtcloud-keycloak             │
│  Keycloak (porta 8080, somente interna) │
│  Interface admin (porta 9000, interna)  │
└─────────────────────────────────────────┘
```

Todos os contêineres se comunicam por uma rede bridge isolada do Docker. Apenas a porta do aplicativo web e (opcionalmente) a porta do servidor de análise Shiny são expostas ao host.
