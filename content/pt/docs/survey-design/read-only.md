---
title: "Apenas leitura"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 287
---

Os campos de apenas leitura no rtSurvey permitem-lhe exibir informação que não pode ser editada pelo respondente. Esta funcionalidade é particularmente útil para mostrar dados pré-preenchidos, resultados calculados ou informação que deve permanecer constante ao longo do inquérito.

## Utilização Básica

Para tornar um campo apenas leitura, use a coluna `read_only` no seu XLSForm:

```
| type    | name | label                 | read_only | default |
|---------|------|----------------------|-----------|---------|
| integer | num  | Número do paciente é:    | yes       | 5       |
```

Neste exemplo, o número do paciente está definido como 5 e não pode ser alterado pelo respondente.

## Combinar Apenas Leitura com Valores Predefinidos

Os campos de apenas leitura são frequentemente usados em conjunto com valores predefinidos para exibir informação pré-determinada ou calculada:

```
| type    | name     | label               | read_only | default        |
|---------|----------|---------------------|-----------|----------------|
| text    | username | Utilizador com sessão iniciada:     | yes       | ${current_user}|
| date    | today    | Data de hoje:       | yes       | today()        |
```

Aqui, o nome de utilizador e a data atual são exibidos mas não podem ser editados.

## Funcionalidades Específicas do rtSurvey

### Apenas Leitura Condicional

O rtSurvey alarga a funcionalidade de apenas leitura com lógica condicional:

```
| type    | name     | label           | read_only                |
|---------|----------|-----------------|--------------------------|
| integer | age      | Idade:            | ${role} = 'viewer'       |
| text    | comments | Comentários:       | selected(${status}, 'closed') |
```

Nestes exemplos:
- O campo 'age' é apenas leitura se a função do utilizador for 'viewer'.
- O campo 'comments' torna-se apenas leitura se o estado for 'closed'.

### Estado de Apenas Leitura Dinâmico

O rtSurvey permite-lhe alterar o estado de apenas leitura dinamicamente:

```
| type      | name     | label    | read_only              |
|-----------|----------|----------| ----------------------|
| text      | address  | Endereço: | ${edit_mode} = 'false' |
```

Isto permite-lhe alternar entre modos editável e apenas leitura com base em certas condições ou ações do utilizador.

## Melhores Práticas para Usar Campos de Apenas Leitura

1. **Clareza**: Indique claramente quais os campos que são apenas leitura através de pistas visuais ou etiquetas.
2. **Consistência**: Use campos de apenas leitura de forma consistente ao longo do seu inquérito.
3. **Validação**: Mesmo que os campos de apenas leitura não possam ser editados, inclua-os no seu processo de validação de dados.
4. **Desempenho**: Seja cauteloso com cálculos complexos em campos de apenas leitura, pois podem afetar o tempo de carregamento do formulário.
5. **Acessibilidade**: Certifique-se de que os campos de apenas leitura são corretamente marcados para leitores de ecrã.

## Técnicas Avançadas

### Campos de Apenas Leitura Calculados

Use campos de apenas leitura para exibir cálculos baseados noutras respostas:

```
| type      | name     | label           | read_only | calculation            |
|-----------|----------|-----------------|-----------|------------------------|
| calculate | bmi      | IMC:            | yes       | ${weight} / (${height} * ${height}) |
```

### Exibir Dados Históricos

Os campos de apenas leitura podem exibir dados de inquéritos anteriores ou fontes externas:

```
| type    | name           | label                  | read_only | default                    |
|---------|----------------|------------------------|-----------|----------------------------|
| text    | last_visit_date| Data da última visita:    | yes       | ${pulldata('visits', 'date', 'id', ${patient_id})} |
```

## Considerações de Gestão de Dados

- Os campos de apenas leitura são incluídos nas exportações de dados, tipicamente com um sinalizador indicando o seu estado de apenas leitura.
- Ao atualizar registos existentes, os campos de apenas leitura preservam os seus valores originais a menos que sejam explicitamente substituídos através do backend.

## Comportamento da Aplicação Móvel

- A aplicação móvel rtSurvey respeita as configurações de apenas leitura, incluindo lógica de apenas leitura condicional.
- O modo offline suporta completamente a funcionalidade de apenas leitura, incluindo campos de apenas leitura dinâmicos e calculados.

## Limitações Conhecidas

- Algumas condições de apenas leitura dinâmicas complexas podem ter um ligeiro impacto no desempenho em dispositivos de baixo desempenho.
- Os campos de apenas leitura podem não impedir todas as formas de manipulação de dados em ficheiros de dados exportados, por isso a validação do lado do servidor é recomendada para dados críticos.

## Resolução de Problemas de Campos de Apenas Leitura

1. **Campo Inesperadamente Editável**: Verifique erros de sintaxe na coluna `read_only` ou na lógica condicional.
2. **Valores Calculados Não Atualizam**: Verifique a lógica de cálculo e certifique-se de que todos os campos referenciados estão corretamente nomeados.
3. **Problemas de Desempenho**: Otimize cálculos complexos ou considere abordagens alternativas para exibir dados de apenas leitura.
