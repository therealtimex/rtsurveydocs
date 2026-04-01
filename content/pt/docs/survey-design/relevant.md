---
title: "Omitir perguntas"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 280
---

A lógica de salto, também conhecida como ramificação ou lógica condicional, permite-lhe criar inquéritos dinâmicos que se adaptam às respostas dos respondentes. No rtSurvey, a lógica de salto é implementada usando a coluna `relevant` no seu XLSForm.

## Lógica de Salto Básica

Para implementar lógica de salto básica, use a coluna `relevant` para especificar uma condição:

```
| type           | name          | label                       | relevant            |
|----------------|---------------|-----------------------------|--------------------|
| select_one y_n | likes_pizza   | Gosta de pizza?          |                    |
| select_multiple pizza_toppings | favorite_topping | Coberturas favoritas | ${likes_pizza} = 'yes' |
```

Neste exemplo, a pergunta "Coberturas favoritas" só aparece se o respondente responder "yes" a gostar de pizza.

## Sintaxe para Expressões Relevantes

- Use `${ }` para referenciar outras variáveis de perguntas.
- Para perguntas `select_one`, compare diretamente: `${question_name} = 'answer'`
- Para perguntas `select_multiple`, use a função `selected()`.

## Lógica de Salto Avançada

### Múltiplas Condições

Pode combinar múltiplas condições usando `and`, `or` e parênteses:

```
| type    | name  | label                   | relevant                                  |
|---------|-------|-------------------------|-------------------------------------------|
| integer | age   | Qual é a sua idade?       |                                           |
| text    | school| Que escola frequenta? | ${age} < 18 and (${location} = 'urban' or ${location} = 'suburban') |
```

### Usar Perguntas select_multiple

Para perguntas `select_multiple`, use a função `selected()`:

```
| type           | name          | label                       | relevant                               |
|----------------|---------------|-----------------------------|-----------------------------------------|
| select_multiple pizza_toppings | favorite_topping | Coberturas favoritas |                                         |
| text           | cheese_type   | Tipo favorito de queijo     | selected(${favorite_topping}, 'cheese') |
```

### Opção "Outro" em Escolha Múltipla

Implementar uma opção "Outro" de texto livre usando `relevant`:

```
| type           | name                  | label                               | relevant                               |
|----------------|----------------------|-------------------------------------|---------------------------------------|
| select_multiple pizza_toppings | favorite_toppings | Quais são as suas coberturas de pizza favoritas? |                                       |
| text           | favorite_toppings_other | Que outras coberturas gosta?   | selected(${favorite_toppings}, 'other') |
```

Lembre-se de incluir 'other' como opção na sua folha de trabalho choices.

## Funcionalidades Específicas do rtSurvey

### Relevância Dinâmica

O rtSurvey permite relevância dinâmica baseada em campos calculados:

```
| type      | name       | label              | calculation                   |
|-----------|------------|--------------------|-----------------------------|
| calculate | total_score| Pontuação Total        | ${score1} + ${score2} + ${score3} |
| text      | feedback   | Comentários           | ${total_score} > 75             |
```

### Relevância em Repetições

O rtSurvey suporta relevância dentro de grupos de repetição:

```
| type         | name         | label            | relevant               |
|--------------|--------------|------------------|------------------------|
| begin repeat | child_info   | Informação da Criança|                        |
| integer      | child_age    | Idade da Criança      |                        |
| text         | school_name  | Nome da Escola      | ${child_age} >= 5      |
| end repeat   |              |                  |                        |
```

### Relevância em Cascata

O rtSurvey lida eficientemente com relevância em cascata, onde a relevância de uma pergunta depende de outra, que por sua vez depende de uma terceira:

```
| type           | name        | label                  | relevant               |
|----------------|-------------|------------------------|------------------------|
| select_one y_n | has_car     | Possui um carro?      |                        |
| select_one car_type | car_type | Que tipo de carro?    | ${has_car} = 'yes'     |
| text           | model       | Modelo específico         | ${car_type} = 'sedan'  |
```

## Melhores Práticas para Lógica de Salto no rtSurvey

1. **Mantenha-o Simples**: Evite condições de relevância excessivamente complexas quando possível.
2. **Teste Cuidadosamente**: Use a funcionalidade de pré-visualização do rtSurvey para testar todos os caminhos possíveis no seu inquérito.
3. **Considere o Desempenho**: Lógica de salto muito complexa pode afetar o desempenho do inquérito, especialmente em dispositivos móveis.
4. **Use Nomes de Variáveis Claros**: Isto torna as suas expressões de relevância mais fáceis de ler e manter.
5. **Documente a Sua Lógica**: Adicione notas para explicar padrões de salto complexos, especialmente para colaboração em equipa.
6. **Esteja Ciente da Análise de Dados**: As perguntas ignoradas resultarão em dados ausentes. Planeie a sua análise em conformidade.

## Resolução de Problemas de Lógica de Salto

- **Erros de Sintaxe**: Certifique-se de que todos os `${ }` estão corretamente fechados e escritos corretamente.
- **Referências Circulares**: Evite criar loops onde as perguntas dependem umas das outras.
- **Sensibilidade a Maiúsculas**: Lembre-se que as opções de resposta são sensíveis a maiúsculas e minúsculas nas expressões de relevância.
- **Comparações Numéricas**: Use operadores apropriados (`<`, `>`, `=`) para comparações numéricas.

## Conclusão

O uso eficaz da lógica de salto pode melhorar significativamente a experiência do respondente e a qualidade dos dados nos seus projetos rtSurvey. Ao aproveitar as funcionalidades avançadas do rtSurvey e seguir as melhores práticas, pode criar inquéritos dinâmicos e eficientes que se adaptam à situação única de cada respondente.
