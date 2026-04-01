---
title: "Áudio"
description: "As perguntas de áudio permitem que os respondentes gravem e enviem arquivos de áudio como parte da pesquisa."
icon: "mic"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 228
---

O tipo de pergunta `audio` permite que os respondentes **gravem áudio** ou façam upload de um arquivo de áudio existente como parte de sua resposta à pesquisa. É útil para capturar relatos verbais, sons ambientais, depoimentos ou qualquer informação que seja melhor transmitida por voz do que por texto.

## Especificação básica do XLSForm

| type  | name        | label                        |
|-------|-------------|------------------------------|
| audio | voice_note  | Por favor, grave seus comentários |

Para mais detalhes sobre o tipo de pergunta de áudio padrão, consulte a [especificação do XLSForm](https://xlsform.org/en/#question-types).

## Usos

As perguntas de áudio são comumente usadas para:

1. Capturar respostas verbais abertas para reduzir a carga de digitação do entrevistador
2. Gravar depoimentos, histórias pessoais ou histórias orais
3. Documentar sons ambientais (por exemplo, níveis de ruído perto de infraestrutura)
4. Coletar amostras de voz para pesquisas linguísticas ou de saúde
5. Permitir que os respondentes adicionem esclarecimentos verbais a respostas numéricas ou de seleção

## Formato de dados

Os arquivos de áudio são armazenados como anexos binários junto com o envio do formulário, tipicamente:

- **Formato:** MP3 ou AAC (gravação móvel); WAV (gravação de alta qualidade)
- **Nomenclatura:** `{instanceID}-{fieldname}.mp3` (ou equivalente)
- **Armazenamento:** Enviados para a pasta de mídia do servidor e vinculados ao registro de envio
- **Acesso:** Reproduzíveis e baixáveis a partir da interface de gerenciamento de envios

## Extensões do rtSurvey

### Duração máxima

Use a coluna `parameters` para limitar a duração da gravação:

| type | name | label | parameters |
|------|------|-------|------------|
| audio | interview | Gravar a entrevista | `max-duration=120` |

`max-duration` está em segundos. O gravador para automaticamente no limite.

### Configurações de qualidade

A qualidade da gravação pode ser definida via `parameters`:

| type | name | label | parameters |
|------|------|-------|------------|
| audio | feedback | Gravar feedback | `quality=normal` |

Valores suportados: `low`, `normal` (padrão), `voice-only`. `voice-only` otimiza para áudio falado com redução de ruído.

### Reprodução antes do envio

No celular, o entrevistador pode reproduzir o clipe gravado antes de prosseguir. Isso é habilitado por padrão — nenhuma configuração é necessária.

### Integração com gravador nativo

No Android e iOS, `audio` inicia o aplicativo de gravação nativo do dispositivo. Na web, usa a API MediaRecorder integrada do navegador.

## Exemplo de uso

### Com duração máxima e dica

| type | name | label | hint | parameters |
|------|------|-------|------|------------|
| audio | story | Conte-nos sobre o incidente com suas próprias palavras | Fale claramente. A gravação para após 3 minutos. | `max-duration=180` |

### Áudio condicional — apenas se um problema foi relatado

| type | name | label | relevant | required |
|------|------|-------|----------|----------|
| select_one yesno | issue_found | Um problema foi encontrado? | | |
| audio | issue_audio | Grave uma descrição do problema | `${issue_found} = 'yes'` | `${issue_found} = 'yes'` |

## Práticas recomendadas

1. Declare claramente no `label` ou `hint` o que o entrevistador deve dizer e por quanto tempo.
2. Use `max-duration` para evitar arquivos excessivamente grandes em áreas com velocidades de upload lentas.
3. Informe os respondentes antes de iniciar a gravação — gravação inesperada pode levantar preocupações de privacidade.
4. Teste a gravação no dispositivo de destino e nas condições de rede antes da implantação.
5. Defina `quality=voice-only` para gravações no estilo entrevista para reduzir o tamanho do arquivo sem perder inteligibilidade.

## Limitações

- Os arquivos de áudio podem ser grandes (uma gravação de 2 minutos em qualidade normal é ~2 a 4 MB) — leve isso em conta nas estimativas de plano de dados e tempo de upload.
- Nem todos os navegadores suportam a API MediaRecorder — Chrome e Firefox funcionam de forma confiável; o Safari em versões mais antigas do iOS pode ter problemas.
- A transcrição de respostas de áudio requer processamento adicional pós-coleta (manual ou conversão automática de fala em texto).
- Regulamentos de privacidade podem restringir a gravação de vozes — verifique os requisitos locais de proteção de dados.
