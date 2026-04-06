---
title: "Trigger / Acknowledge"
description: "As perguntas trigger exibem uma declaração que o enumerador deve explicitamente reconhecer antes de continuar."
icon: "check-circle"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 240
---

O tipo de pergunta `trigger` (também chamado `acknowledge`) exibe uma **declaração com uma caixa de verificação**. O enumerador deve marcar a caixa de verificação para confirmar que leu e compreendeu a declaração antes de o formulário lhes permitir continuar. Nenhum valor de dados é armazenado — apenas se a caixa de verificação foi marcada.

## Especificação XLSForm Básica

| type | name | label |
|------|------|-------|
| trigger | consent_ack | O respondente deu consentimento informado verbal. |

Ou usando o alias `acknowledge`:

| type | name | label |
|------|------|-------|
| acknowledge | consent_ack | O respondente deu consentimento informado verbal. |

Tanto `trigger` como `acknowledge` são equivalentes — use o que a sua plataforma documenta.

## Utilizações

As perguntas trigger/acknowledge são comummente usadas para:

1. **Consentimento informado** — confirmar que o enumerador obteve consentimento antes de registar dados sensíveis
2. **Alertas suaves** — avisar sobre um valor invulgar e exigir confirmação explícita antes de prosseguir
3. **Itens de lista de verificação** — confirmar que uma observação física foi concluída (por ex., "Observei a fonte de água diretamente")
4. **Instruções** — forçar o enumerador a reconhecer uma instrução ao nível de secção antes de continuar
5. **Verificações de qualidade** — sinalizar valores atípicos e exigir que o enumerador os verifique

## Exemplo de Utilização

### Reconhecimento de consentimento

| type | name | label | required |
|------|------|-------|----------|
| trigger | consent | O respondente deu consentimento informado verbal para participar neste inquérito. | yes |

### Alerta suave para valores atípicos

Usado juntamente com uma expressão `relevant` para mostrar o trigger apenas quando é introduzido um valor suspeito:

| type | name | label | relevant | required |
|------|------|-------|----------|----------|
| integer | children | Número de filhos | | |
| trigger | children_confirm | Introduziu ${children} filhos. Por favor verifique com o respondente e toque em OK para confirmar. | `${children} > 10` | `${children} > 10` |

### Reconhecimento de instrução no início de secção

| type | name | label |
|------|------|-------|
| trigger | section_b_ack | Secção B: Uso Agrícola da Terra. Faça todas as perguntas desta secção apenas ao chefe do agregado familiar. |

## Tornar o trigger obrigatório

Adicione `required: yes` para impedir o avanço até que a caixa seja marcada:

| type | name | label | required | required_message |
|------|------|-------|----------|------------------|
| trigger | safety_check | Todo o equipamento de segurança está presente e funcional. | yes | Deve confirmar antes de prosseguir. |

## Exibição condicional

Mostre o trigger apenas quando uma condição é satisfeita:

| type | name | label | relevant |
|------|------|-------|----------|
| select_one yesno | has_well | O agregado familiar tem um poço? | |
| trigger | well_observation | Confirme que observou diretamente as condições do poço. | `${has_well} = 'yes'` |

## Diferença em relação a `note`

| | `note` | `trigger` |
|--|--------|-----------|
| Exibe texto | Sim | Sim |
| Requer interação | Não | Sim (deve marcar) |
| Armazena dados | Não | Não (apenas OK/marcado) |
| Pode bloquear progresso | Não | Sim (com `required`) |

## Melhores Práticas

1. Mantenha as etiquetas do trigger concisas e acionáveis — o enumerador deve conseguir ler e confirmar em segundos.
2. Adicione sempre `required: yes` quando o reconhecimento é obrigatório.
3. Use triggers para consentimento e verificações de segurança onde precisa de um registo de auditoria de que o enumerador confirmou.
4. Combine com `relevant` para alertas suaves condicionais para que o trigger apareça apenas quando um valor precisa de verificação.

## Limitações

- Os campos trigger não armazenam um valor de dados significativo — apenas registam que a caixa foi marcada.
- O widget trigger é renderizado como uma caixa de verificação/botão simples na maioria dos clientes; não é uma assinatura eletrónica completa.
