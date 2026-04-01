---
title: "Padrão"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 287
---

Os valores padrão no rtSurvey permitem pré-preencher perguntas com respostas quando um respondente as encontra pela primeira vez. Este recurso pode melhorar significativamente a eficiência da pesquisa e a qualidade dos dados, fornecendo valores iniciais comumente selecionados ou que servem como exemplos de entrada esperada.

## Uso básico

Para definir um valor padrão, use a coluna `default` no seu XLSForm:

```
| type    | name        | label                              | default    |
|---------|-------------|------------------------------------|------------|
| date    | survey_date | Data da pesquisa                   | 2024-07-04 |
| decimal | weight      | Peso do respondente? (em kg)       | 51.3       |
```

Neste exemplo, a data da pesquisa será pré-preenchida com 4 de julho de 2024, e o campo de peso começará com 51,3 kg.

## Padrões dinâmicos

O rtSurvey suporta valores padrão dinâmicos usando funções:

```
| type | name | label                                    | default  |
|------|------|------------------------------------------| ---------|
| date | d    | Informe a data em que o evento ocorreu?  | today()  |
```

Aqui, a função `today()` define automaticamente o padrão para a data atual.

## Recursos específicos do rtSurvey

### Padrões sensíveis ao contexto

O rtSurvey estende a funcionalidade de padrão com padrões sensíveis ao contexto:

```
| type    | name     | label            | default            |
|---------|----------|------------------|--------------------|
| text    | location | Localização atual| ${current_location}|
```

Isso usa a variável `${current_location}` do rtSurvey para pré-preencher a localização com base no GPS do dispositivo.

### Padrões em cascata

O rtSurvey permite padrões baseados em respostas anteriores:

```
| type    | name     | label    | default         |
|---------|----------|----------|-----------------|
| text    | city     | Cidade   |                 |
| text    | district | Distrito | ${city}-distrito|
```

Aqui, o campo de distrito é pré-preenchido com base na cidade inserida.

### Padrão em repetições

Para perguntas dentro de um grupo de repetição, o padrão é calculado quando a repetição é adicionada:

```
| type         | name      | label          | default                |
|--------------|-----------|----------------|------------------------|
| begin repeat | visits    | Visitas clínicas|                       |
| date         | visit_date| Data da visita | ${previous_visit_date} |
| end repeat   |           |                |                        |
```

Isso define a data da visita padrão para a data da visita anterior.

## Práticas recomendadas para usar padrões

1. **Use com moderação**: Use padrões apenas quando eles melhorarem significativamente a eficiência ou a qualidade dos dados.
2. **Garanta precisão**: Revise e atualize regularmente os valores padrão estáticos.
3. **Teste minuciosamente**: Especialmente ao usar padrões dinâmicos ou calculados.
4. **Considere a experiência do usuário**: Garanta que os padrões não enganem os respondentes ou introduzam viés.
5. **Documente claramente**: Certifique-se de que todos os membros da equipe entendam a justificativa por trás dos valores padrão.

## Técnicas avançadas de padrão

### Padrões aleatorizados

O rtSurvey suporta padrões aleatorizados para certos tipos de perguntas:

```
| type              | name    | label        | default           |
|-------------------|---------|--------------|-------------------|
| select_one options| choice  | Selecione um:| random(options)   |
```

Isso seleciona aleatoriamente uma opção padrão da lista 'options'.

### Padrões condicionais

Use relevância para definir padrões condicionais:

```
| type    | name     | label    | default | relevant        |
|---------|----------|----------|---------|-----------------|
| text    | other    | Especifique | N/A  | ${q1} = 'other' |
```

Aqui, 'N/A' é o padrão apenas quando 'other' é selecionado em uma pergunta anterior.

## Considerações de gerenciamento de dados

- Os valores padrão são incluídos nas exportações de dados, normalmente com um sinalizador indicando que eram valores padrão.
- O recurso de trilha de auditoria do rtSurvey rastreia quando os valores padrão são alterados pelos respondentes.

## Comportamento no aplicativo móvel

- O aplicativo móvel rtSurvey suporta todas as funcionalidades de padrão, incluindo padrões dinâmicos e sensíveis ao contexto.
- O modo off-line pode afetar alguns padrões dinâmicos que dependem de dados em tempo real.

## Limitações conhecidas

- Padrões calculados complexos podem impactar o tempo de carregamento do formulário, especialmente em dispositivos de baixo custo.
- Alguns padrões dinâmicos podem não funcionar conforme esperado no modo de visualização.

## Solução de problemas de valores padrão

1. **Padrão não aparece**: Verifique erros de sintaxe na expressão padrão.
2. **Valores inesperados**: Verifique a lógica de cálculo e teste com vários cenários.
3. **Problemas de desempenho**: Otimize cálculos padrão complexos ou considere abordagens alternativas.
