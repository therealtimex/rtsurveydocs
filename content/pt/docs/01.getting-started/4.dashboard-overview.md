---
weight: 10
date: "2026-03-04T00:00:00+00:00"
draft: false
title: "Visão Geral do Dashboard"
icon: "home"
toc: true
description: "Compreender o Dashboard do Sistema RT-CPMS e as ferramentas de supervisão de projetos."
tags: ["Dashboard", "Overview", "Monitoring"]
---

# O Dashboard do Sistema

O Dashboard (`/cpms/cpmsDashBoard/indexNew`) serve como centro de comando administrativo e página de destino principal para a plataforma Real-Time Survey (RT-CPMS).

![Pré-visualização do Dashboard do Sistema](/images/dashboard_overview.png)

Foi concebido para dar aos gestores de inquérito uma visão geral imediata dos projetos ativos, ligações rápidas às ferramentas essenciais e um hub centralizado para navegar por todos os principais módulos da plataforma.

## Funcionalidades Principais

### 1. Seleção de Projeto e Formulário
O painel do lado esquerdo contém o navegador de **Formulários e Relatórios**. Esta área lista todos os inquéritos ativos no seu espaço de trabalho.
* Ao selecionar um inquérito específico (por ex., *RTA - SURVEY 02*), direciona o dashboard para focar a monitorização e as métricas exclusivamente nesse projeto.

### 2. Filtros de Visualização e Métricas
Acima da lista de projetos, pode alternar entre várias perspetivas críticas de dados para monitorizar o progresso do trabalho de campo em tempo real:
* **Contagem por hora de início / hora de fim**: Acompanhe quando os enumeradores estão a iniciar e a concluir as suas sessões de inquérito.
* **Contagem por data de submissão**: Monitorize o volume diário geral de dados a chegar ao servidor.
* **Contagem por nome de utilizador**: Avalie a produtividade e o desempenho individual dos enumeradores.
* **Mapa de entrevistas**: Visualize uma distribuição geográfica (GIS) de onde as respostas ao inquérito estão a ser recolhidas para garantir que os requisitos de cobertura espacial são cumpridos.

### 3. Portais de Aplicação
O centro do dashboard fornece acesso imediato às interfaces de recolha de dados. Dependendo do hardware dos seus enumeradores, pode lançar ou direcioná-los para:
* **Aplicação Web**: Para recolha de dados baseada em navegador.
* **Aplicação Android**: Ligação para o Google Play Store ou APK.
* **Aplicação iOS**: Ligação para a Apple App Store.

### 4. Atalhos Diretos para Módulos
Três botões de ação proeminentes permitem a transição rápida para os módulos operacionais mais frequentemente utilizados:
* **Entrada de Formulários e Dados**: Salte diretamente para a gestão manual de dados recolhidos.
* **Análise e Relatórios**: Abra o conjunto de Business Intelligence (BI) para cruzar tabulações e representar graficamente as respostas ao inquérito.
* **Configuração de Permissões**: Ajuste quem tem acesso ao inquérito ativo e que funções desempenham.

### 5. Barra Lateral de Navegação Global
A barra lateral esquerda recolhível fornece acesso ao ecossistema completo de módulos de backend do RT-CPMS. A partir daqui, pode aprofundar:
* **Configuração**: Gestão de pessoal e dispositivos ativos.
* **Gestão de Trabalho de Campo**: Acompanhamento da atividade diária dos enumeradores.
* **Garantia de Qualidade**: Implementação e revisão de regras e sinalizadores de controlo de qualidade.
* **Entregas Finais**: Exportação dos seus conjuntos de dados limpos para CSV, PDF ou Stata.
