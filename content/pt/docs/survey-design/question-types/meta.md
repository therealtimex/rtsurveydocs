---
title: "Meta"
description: "Os tipos de pergunta meta capturam automaticamente informações do dispositivo, enumerador e temporização sem qualquer entrada do respondente."
icon: "info"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 237
---

Os tipos de pergunta meta são campos especiais que são preenchidos **automaticamente** — o respondente nunca os vê. Capturam contexto sobre a submissão: quando foi recolhida, qual dispositivo foi usado e quem a recolheu. Adicione-os na folha de trabalho `survey` como qualquer outro tipo de pergunta; simplesmente não aparecem no ecrã.

## Especificação XLSForm Básica

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| deviceid | deviceid | |

As etiquetas são opcionais para campos meta pois nunca são exibidas.

---

## Campos meta de temporização

### `start`

Regista a **data e hora em que o formulário foi aberto**. Armazenado em formato ISO 8601 (`YYYY-MM-DDTHH:MM:SS.sss+HH:MM`).

```
type    | name  | label
start   | start |
```

### `end`

Regista a **data e hora em que o formulário foi submetido**. Juntamente com `start`, pode calcular o tempo gasto a preencher o formulário:

```
type      | name          | calculation
calculate | duration_min  | (decimal-date-time(${end}) - decimal-date-time(${start})) * 1440
```

### `today`

Regista a **data atual** (sem componente de hora). Armazenado como `YYYY-MM-DD`. Útil quando precisa apenas da data sem o carimbo temporal completo.

```
type  | name  | label
today | today |
```

---

## Campos meta do dispositivo

### `deviceid`

Regista o **identificador único do dispositivo** usado para recolha de dados. No Android, este é tipicamente o IMEI ou Android ID. Útil para rastrear qual dispositivo submeteu cada formulário e detetar submissões duplicadas do mesmo dispositivo.

```
type      | name     | label
deviceid  | deviceid |
```

### `devicephonenum`

Regista o **número de telefone do cartão SIM** no dispositivo (se disponível). Pode estar vazio se o dispositivo não tiver SIM ou se o número não estiver armazenado no SIM.

```
type           | name          | label
devicephonenum | devicephonenum |
```

### `simserial`

Regista o **número de série do cartão SIM** (ICCID). Útil para identificar qual SIM/operador foi usado.

```
type      | name      | label
simserial | simserial |
```

### `subscriberid`

Regista o **IMSI (International Mobile Subscriber Identity)** — o identificador único de subscritor no cartão SIM.

```
type         | name        | label
subscriberid | subscriberid |
```

---

## Campos meta do enumerador

### `username`

Regista o **nome de utilizador do enumerador com sessão iniciada** (a conta usada na aplicação rtSurvey). Esta é a forma mais fiável de rastrear quem recolheu cada submissão.

```
type     | name     | label
username | username |
```

### `email`

Regista o **endereço de email do enumerador com sessão iniciada**.

```
type  | name  | label
email | email |
```

### `phonenumber`

Regista o **número de telefone associado à conta do enumerador** (se configurado).

```
type        | name       | label
phonenumber | phonenumber |
```

---

## Registo de auditoria

### `audit`

O campo meta `audit` ativa o **registo de auditoria detalhado** — regista um registo com carimbo temporal de cada pergunta que o enumerador visitou, quanto tempo passou em cada uma, e (opcionalmente) a sua localização GPS em cada passo. O registo de auditoria é guardado como um ficheiro `audit.csv` separado juntamente com cada submissão.

```
type  | name  | parameters
audit | audit | location-priority=balanced location-min-interval=30 location-max-age=60
```

#### Parâmetros de auditoria

| Parâmetro | Descrição |
|-----------|-----------|
| `location-priority` | Nível de precisão do GPS: `no-gps`, `low-power`, `balanced`, `high-accuracy` |
| `location-min-interval` | Segundos mínimos entre capturas de localização |
| `location-max-age` | Idade máxima (segundos) de uma localização em cache para aceitar |

O registo de auditoria captura:
- Nome da pergunta e tipo de evento (`question`, `form.start`, `form.exit`, `form.save`, `form.finalize`)
- Carimbos temporais de início e fim para cada evento
- Coordenadas GPS (se `location-priority` estiver definido)

{{% alert icon=" " context="warning" %}}
O campo `audit` gera um ficheiro separado por submissão. Certifique-se de que o seu pipeline de dados processa tanto os dados do formulário principal como o CSV de auditoria.
{{% /alert %}}

---

## Exemplo completo

Um inquérito típico a agregados familiares pode incluir todos os campos meta de temporização e enumerador:

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| today | today | |
| deviceid | deviceid | |
| username | username | |
| email | email | |
| audit | audit | |
| text | household_id | ID do Agregado Familiar |
| ... | ... | ... |

---

## Melhores Práticas

1. Inclua sempre `start` e `end` — são gratuitos, automáticos e inestimáveis para monitorização de qualidade.
2. Inclua sempre `username` para rastrear enumeradores.
3. Inclua `deviceid` quando quiser detetar submissões duplicadas ou rastrear dispositivos de campo.
4. Use `audit` em inquéritos de alta responsabilização onde precisa de verificar que os enumeradores visitaram efetivamente cada pergunta.
5. Os campos relacionados com SIM (`simserial`, `subscriberid`, `devicephonenum`) são apenas fiáveis em dispositivos Android com cartões SIM ativos — ignore-os para implementações apenas com tablets.

---

## Limitações

- Todos os campos meta são **apenas de leitura** — não podem ser referenciados ou modificados por outros cálculos.
- `username` e `email` requerem que o enumerador tenha sessão iniciada; ficarão vazios para submissões anónimas.
- Os campos meta de SIM/telefone podem devolver valores vazios em tablets apenas com Wi-Fi e algumas versões do Android devido a restrições de permissão.
