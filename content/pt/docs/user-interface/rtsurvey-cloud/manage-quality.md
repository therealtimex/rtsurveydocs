---
title: "Gestão de Qualidade"
description: "Monitorize o progresso da recolha de dados, visualize mapas de entrevistas e analise o desempenho dos enumeradores."
icon: "cloud"
date: "2023-05-22T00:34:57+01:00"
lastmod: "2023-05-22T00:34:57+01:00"
draft: false
weight: 316
---

O módulo **Gestão de Qualidade** (acessível através do Dashboard) fornece análises em tempo real e visualizações espaciais para monitorizar o progresso da recolha de dados e o desempenho dos enumeradores. Oferece aos gestores de projeto uma interface de vista dividida para alternar rapidamente entre questionários individuais e relatórios analíticos personalizados.

![Dashboard de Gestão de Qualidade](/images/manage_quality.png)

## Visão Geral do Dashboard

O dashboard de Gestão de Qualidade está dividido em dois separadores de navegação principais: **Formulários** e **Relatórios**. Este menu lateral permite aos utilizadores pesquisar e selecionar eficientemente o conjunto de dados ou relatório específico que desejam analisar.

### Análise de Formulários

Ao selecionar um formulário específico da lista, o dashboard fornece múltiplas ferramentas de visualização incorporadas para acompanhar a qualidade e frequência das submissões:

- **Contagem por hora de início:** Um gráfico de barras que visualiza a frequência de entrevistas iniciadas ao longo de uma linha do tempo.
- **Contagem por hora de fim:** Um gráfico de barras que visualiza quando as entrevistas foram concluídas.
- **Contagem por data de submissão:** Acompanha o volume diário de dados sincronizados com o servidor.
- **Contagem por nome de utilizador:** Um gráfico de barras que identifica os enumeradores com melhor desempenho com base nas suas contagens totais de submissão.
- **Mapa de entrevistas:** Um gráfico de dispersão geográfico (powered by Leaflet) que exibe as coordenadas GPS de onde cada submissão ocorreu, permitindo aos gestores verificar as localizações de trabalho de campo.

### Relatórios Personalizados

O separador **Relatórios** concede acesso a designs analíticos R Markdown pré-configurados e outras estatísticas personalizadas. Uma vez selecionado um relatório, a área de visualização principal carrega dinamicamente a análise gerada através de um visualizador incorporado, permitindo uma verificação estatística mais profunda dos dados recolhidos.

## Pesquisa e Filtragem

Uma barra de pesquisa rápida está disponível acima da lista da barra lateral, permitindo aos utilizadores encontrar rapidamente formulários ou relatórios específicos pelo nome.
