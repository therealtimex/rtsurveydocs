---
title: "Validar respostas"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 270
---

Uma forma de garantir a qualidade dos dados é adicionar restrições aos campos de dados no seu formulário. As restrições ajudam a evitar que os utilizadores introduzam respostas inválidas ou impossíveis. Por exemplo, ao perguntar sobre o rendimento de uma pessoa, quer evitar valores irrealistas, como números negativos ou valores extremamente altos. Adicionar restrições de dados ao seu formulário é fácil de fazer. Basta seguir os passos abaixo:

1. Adicione uma nova coluna chamada "constraint" ao seu formulário.
2. Na coluna "constraint", introduza uma fórmula que especifique os limites na resposta.

### Exemplo

Vamos considerar um exemplo onde queremos adicionar uma restrição para o rendimento da pessoa. A restrição exige que o rendimento esteja entre $0 e $1.000.000. Aqui está como pode configurar a restrição:

{{< table >}}
| `name`      | `constraint`                  |
|---------------|-----------------------------|
| Rendimento        | . >= 0 & . <= 1000000      |
{{< /table >}}

No exemplo acima, o "." na fórmula refere-se de volta à variável de pergunta, que representa o valor introduzido pelo utilizador para a pergunta "Rendimento". A restrição ". >= 0 && . <= 1000000" garante que o rendimento introduzido é maior ou igual a 0 e menor ou igual a 1.000.000.


### Restrição rígida

Uma **restrição rígida** bloqueia completamente a submissão do formulário se o valor introduzido não satisfizer a expressão. O enumerador não pode prosseguir até introduzir um valor válido.

Para adicionar uma restrição rígida, introduza a sua expressão na coluna `constraint`. Opcionalmente adicione uma mensagem legível por humanos em `constraint_message`:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| integer | age | Idade do respondente | `. > 0 and . <= 120` | A idade deve estar entre 1 e 120 |
| decimal | temperature | Temperatura corporal (°C) | `. >= 35 and . <= 42` | A temperatura deve estar entre 35°C e 42°C |
| text | phone | Número de telefone | `regex(., '^[0-9]{10}$')` | Introduza um número de telefone de 10 dígitos |
{{< /table >}}

#### Múltiplas condições

Combine condições com `and` / `or`:

```
. >= 0 and . <= 100
```

```
. = 'yes' or . = 'no'
```

#### Usando `regex()` para validação de padrão

A função `regex(value, pattern)` testa um valor contra uma expressão regular:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| text | email | Endereço de email | `regex(., '^[^@]+@[^@]+\.[^@]+$')` | Introduza um endereço de email válido |
| text | zip_code | Código postal | `regex(., '^[0-9]{5}$')` | Introduza um código postal de 5 dígitos |
{{< /table >}}

#### Referenciar outros campos numa restrição

Use `${fieldname}` para referenciar valores de outras perguntas:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| integer | end_year | Ano de fim | `. >= ${start_year}` | O ano de fim deve ser após o ano de início |
| decimal | loan_repaid | Valor reembolsado | `. <= ${loan_amount}` | Não pode reembolsar mais do que o valor do empréstimo |
{{< /table >}}

### Alerta suave

Um **alerta suave** (também chamado de restrição suave ou aviso) avisa o enumerador que um valor parece invulgar, mas ainda lhe permite prosseguir. Isto é útil quando um valor é tecnicamente válido mas estatisticamente improvável.
