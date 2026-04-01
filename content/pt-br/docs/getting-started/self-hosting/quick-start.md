---
weight: 1
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
title: "Início rápido"
icon: "play_circle"
toc: true
description: "Implante o rtCloud no seu próprio servidor em minutos com um script de nuvem automatizado."
---

Este guia ajuda você a colocar o rtCloud em funcionamento no seu próprio servidor. Os scripts automatizados cuidam de tudo — Docker, SSL, banco de dados, firewall — em uma única execução.

## Requisitos

### Servidor

| Recurso | Mínimo | Recomendado |
|---------|--------|------------|
| RAM | 2 GB | 4 GB (necessário com Keycloak SSO) |
| Disco | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Domínio

Você precisa de um nome de domínio com um **registro A apontando para o IP do servidor** antes de executar o script. O Let's Encrypt requer resolução DNS para emitir o certificado SSL.

---

## Escolha seu provedor de nuvem

Selecione seu provedor abaixo. Cada um tem um script automatizado que é executado na primeira inicialização e conclui a configuração em **5–10 minutos**.

| Provedor | Guia |
|---------|------|
| Linode (Akamai) | [Implantar no Linode](../cloud-deployment/linode) — mais fácil, configuração baseada em formulário via StackScript |
| DigitalOcean | [Implantar no DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Implantar na AWS](../cloud-deployment/aws) |
| Google Cloud | [Implantar no GCP](../cloud-deployment/gcp) |

> **Recomendado para a maioria dos usuários:** Comece com o Linode — o StackScript fornece uma interface baseada em formulário para que não haja nada a editar manualmente.
