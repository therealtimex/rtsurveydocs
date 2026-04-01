---
weight: 150
date: "2023-05-03T22:37:22+01:00"
draft: false
author: "RealTimeX"
title: "Coletando dados"
icon: "rocket_launch"
toc: true
description: "Um guia de início rápido para executar uma pesquisa com o rtSurvey"
publishdate: "2023-05-03T22:37:22+01:00"
tags: ["Iniciantes"]
---

Depois que um formulário é implantado e os entrevistadores são designados, a coleta de dados pode começar. O **rtSurvey** suporta coleta de dados contínua tanto em navegadores web quanto em aplicativos móveis dedicados, garantindo flexibilidade se sua equipe estiver conectada à internet ou trabalhando em ambientes remotos e offline.

## Escolhendo o método de coleta correto

Dependendo da geografia e conectividade do seu projeto, você pode escolher o método ideal para seus entrevistadores:

- **Navegador web (online):** Melhor para centrais de atendimento, entrada de dados no escritório ou respondentes preenchendo pesquisas públicas autoadministradas.
- **Aplicativo móvel rtWork / rtSurvey (online e offline):** Melhor para operações de campo, áreas remotas com internet instável e pesquisas que exigem anexos de mídia (fotos, coordenadas GPS, mapas offline).

---

## Método 1: Coletando dados via navegador web

Usar a interface de formulário web permite que os entrevistadores comecem a coletar dados imediatamente sem instalar nenhum software.

### 1. Acesse a URL do formulário web
No painel **Gerenciar formulários** no Painel de controle, localize seu formulário de destino e clique no botão **URL do formulário web** para gerar um link seguro.

### 2. Preenchimento do formulário
- Abra a URL fornecida em qualquer navegador web moderno.
- Se o formulário exigir autenticação, o entrevistador deve fazer login usando suas credenciais. Se estiver definido como "Visibilidade pública", ele pode prosseguir diretamente.
- Preencha as perguntas da pesquisa. A interface aplicará automaticamente a lógica, padrões de pulo e regras de validação.
- **Captura de mídia:** Se o formulário incluir perguntas de imagem, áudio ou vídeo, o navegador solicitará que você faça upload de um arquivo do seu computador ou use a webcam/microfone do seu dispositivo, se disponível.

### 3. Envio
Ao chegar na página final, clique em **Enviar**. O navegador requer uma conexão ativa com a internet para finalizar o envio. Uma vez bem-sucedido, os dados serão refletidos instantaneamente na interface de **Gerenciar envios**.

---

## Método 2: Coletando dados via aplicativo móvel (offline)

Para coleta de dados de campo robusta, os aplicativos móveis fornecem capacidades offline completas.

### 1. Instalar e autenticar
- Baixe o aplicativo **rtWork** (ou **rtSurvey**) da Google Play Store ou Apple App Store.
- Abra o aplicativo e faça login usando as credenciais do entrevistador designado.

### 2. Baixar formulários (requer internet)
- Navegue para a seção **Formulários** ou **Tarefas** no aplicativo.
- Toque no ícone **Sincronizar** ou **Baixar** para buscar os designs de questionário mais recentes do servidor. Uma vez baixados, os formulários são armazenados localmente no dispositivo.

### 3. Coletar dados (offline)
- Abra o formulário baixado e comece a entrevista.
- Você pode coletar dados com segurança completamente offline.
- **Captura de mídia:** O aplicativo móvel se integra nativamente com o hardware do seu dispositivo. Você pode capturar fotos, gravar áudio, gravar vídeo e registrar coordenadas GPS precisas diretamente no aplicativo, mesmo sem uma conexão com a internet.
- Quando você termina uma entrevista, finalize o registro. Os registros finalizados são enfileirados com segurança na caixa de saída do aplicativo.

### 4. Sincronizar envios (requer internet)
- Depois que o entrevistador retornar a uma área com acesso à internet (Wi-Fi ou dados móveis), ele deve navegar para a interface **Caixa de saída** ou **Sincronizar**.
- Instrua o aplicativo a enviar os formulários finalizados. O aplicativo transmitirá os registros enfileirados e todos os arquivos de mídia anexados com segurança ao servidor, após o que aparecerão na grade de dados para revisão.
