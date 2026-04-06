---
weight: 1
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
title: "Início rápido"
icon: "play_circle"
toc: true
description: "Implemente o rtCloud no seu próprio servidor em minutos com um script de cloud automatizado."
---

Este guia ajuda-o a colocar o rtCloud a funcionar no seu próprio servidor. Os scripts automatizados tratam de tudo — Docker, SSL, base de dados, firewall — numa única execução.

## Requisitos

### Servidor

| Recurso | Mínimo | Recomendado |
|---------|--------|------------|
| RAM | 2 GB | 4 GB (necessário com Keycloak SSO) |
| Disco | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Domínio

Precisa de um nome de domínio com um **registo A a apontar para o IP do servidor** antes de executar o script. O Let's Encrypt requer resolução DNS para emitir o certificado SSL.

---

## Escolha o seu fornecedor de cloud

Selecione o seu fornecedor abaixo. Cada um tem um script automatizado que é executado no primeiro arranque e conclui a configuração em **5–10 minutos**.

| Fornecedor | Guia |
|-----------|------|
| Linode (Akamai) | [Implementar no Linode](../cloud-deployment/linode) — mais fácil, configuração baseada em formulário via StackScript |
| DigitalOcean | [Implementar no DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Implementar na AWS](../cloud-deployment/aws) |
| Google Cloud | [Implementar no GCP](../cloud-deployment/gcp) |

> **Recomendado para a maioria dos utilizadores:** Comece com o Linode — o StackScript fornece uma interface baseada em formulário para que não haja nada a editar manualmente.
