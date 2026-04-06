---
weight: 5
title: "Primeiro login"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "login"
toc: true
description: "Como fazer login na sua instância do rtSurvey pela primeira vez após a implantação."
---

> **O SSL deve ser configurado antes de fazer login.** Se você acessar o aplicativo via HTTP, verá um aviso de segurança e o SSO será bloqueado. Conclua a [Configuração de SSL](ssl-setup) primeiro.

Depois que o SSL estiver ativo, abra seu navegador na URL HTTPS:

```
https://your-domain.com
```

---

## A tela de login

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

A página de login mostra:

- Campos de **Usuário** e **Senha**
- Um botão **Entrar**
- Um botão **Entrar com SSO** (abaixo de um divisor) — para membros da equipe com contas SSO

---

## Credenciais padrão do administrador

Insira as credenciais padrão e clique em **Entrar**:

| Campo | Valor |
|-------|-------|
| Usuário | `admin` |
| Senha | `admin` |

> **Altere sua senha imediatamente após o primeiro login.**

---

## Se você vir um aviso de segurança

Se você acessar o aplicativo via HTTP (antes de o SSL ser configurado), verá:

- Um banner de aviso amarelo no topo da página de login
- Um modal ao clicar em **Entrar**, avisando que as credenciais serão enviadas sem criptografia

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Clique em **Configurar SSL** para configurar HTTPS ou em **Continuar assim mesmo** para fazer login sem SSL (não recomendado).

O login SSO está completamente bloqueado via HTTP — clicar em **Entrar com SSO** mostrará um aviso em vez de redirecionar.

---

## Após o login

Depois de entrar, você chegará ao painel. Daqui:

1. **Alterar a senha do administrador** — configurações de conta → alterar senha
2. **Criar seu primeiro projeto** — Projetos → Novo projeto
3. **Fazer upload ou criar um formulário** — Formulários → Fazer upload de XLSForm ou abrir o Form Builder
4. **Adicionar usuários** — Usuários → Convidar ou criar contas para sua equipe
