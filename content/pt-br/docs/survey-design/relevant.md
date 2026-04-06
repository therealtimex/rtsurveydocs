---
title: "Pulando perguntas"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 280
---

A lógica de salto, também conhecida como ramificação ou lógica condicional, permite criar pesquisas dinâmicas que se adaptam às respostas dos respondentes. No rtSurvey, a lógica de salto é implementada usando a coluna `relevant` no seu XLSForm.

## Lógica de salto básica

Para implementar lógica de salto básica, use a coluna `relevant` para especificar uma condição:

```
| type           | name          | label                           | relevant             |
|----------------|---------------|---------------------------------|---------------------|
| select_one y_n | likes_pizza   | Você gosta de pizza?            |                     |
| select_multiple pizza_toppings | favorite_topping | Ingredientes favoritos | ${likes_pizza} = 'yes' |
```

Neste exemplo, a pergunta "Ingredientes favoritos" só aparece se o respondente responder "sim" para gostar de pizza.

## Sintaxe para expressões de relevância

- Use `${ }` para referenciar outras variáveis de pergunta.
- Para perguntas `select_one`, compare diretamente: `${nome_da_pergunta} = 'resposta'`
- Para perguntas `select_multiple`, use a função `selected()`.

## Lógica de salto avançada

### Múltiplas condições

Você pode combinar múltiplas condições usando `and`, `or` e parênteses:

```
| type    | name  | label                           | relevant                                  |
|---------|-------|---------------------------------|-------------------------------------------|
| integer | age   | Qual é a sua idade?             |                                           |
| text    | school| Em que escola você estuda?      | ${age} < 18 and (${location} = 'urban' or ${location} = 'suburban') |
```

### Usando perguntas select_multiple

Para perguntas `select_multiple`, use a função `selected()`:

```
| type           | name          | label                     | relevant                                |
|----------------|---------------|---------------------------|------------------------------------------|
| select_multiple pizza_toppings | favorite_topping | Ingredientes favoritos |                                         |
| text           | cheese_type   | Tipo favorito de queijo   | selected(${favorite_topping}, 'cheese') |
```

### Opção "Outro" em múltipla escolha

Implemente uma opção de texto livre "Outro" usando `relevant`:

```
| type           | name                  | label                                    | relevant                               |
|----------------|----------------------|-----------------------------------------|---------------------------------------|
| select_multiple pizza_toppings | favorite_toppings | Quais são seus ingredientes favoritos de pizza? |                                       |
| text           | favorite_toppings_other | Que outros ingredientes você gosta? | selected(${favorite_toppings}, 'other') |
```

Lembre-se de incluir 'other' como opção na sua planilha choices.

## Recursos específicos do rtSurvey

### Relevância dinâmica

O rtSurvey permite relevância dinâmica baseada em campos calculados:

```
| type      | name       | label          | calculation                       |
|-----------|------------|----------------|----------------------------------|
| calculate | total_score| Pontuação total| ${score1} + ${score2} + ${score3} |
| text      | feedback   | Feedback       | ${total_score} > 75              |
```

### Relevância em repetições

O rtSurvey suporta relevância dentro de grupos de repetição:

```
| type         | name         | label                  | relevant               |
|--------------|--------------|------------------------|------------------------|
| begin repeat | child_info   | Informações da criança |                        |
| integer      | child_age    | Idade da criança       |                        |
| text         | school_name  | Nome da escola         | ${child_age} >= 5      |
| end repeat   |              |                        |                        |
```

### Relevância em cascata

O rtSurvey lida eficientemente com relevância em cascata, onde a relevância de uma pergunta depende de outra, que por sua vez depende de uma terceira:

```
| type           | name        | label                     | relevant               |
|----------------|-------------|---------------------------|------------------------|
| select_one y_n | has_car     | Você tem carro?           |                        |
| select_one car_type | car_type | Que tipo de carro?     | ${has_car} = 'yes'     |
| text           | model       | Modelo específico         | ${car_type} = 'sedan'  |
```

## Práticas recomendadas para lógica de salto no rtSurvey

1. **Mantenha simples**: Evite condições de relevância excessivamente complexas quando possível.
2. **Teste minuciosamente**: Use o recurso de visualização do rtSurvey para testar todos os caminhos possíveis na sua pesquisa.
3. **Considere o desempenho**: Lógica de salto muito complexa pode impactar o desempenho da pesquisa, especialmente em dispositivos móveis.
4. **Use nomes de variáveis claros**: Isso torna suas expressões de relevância mais fáceis de ler e manter.
5. **Documente sua lógica**: Adicione notas para explicar padrões complexos de salto, especialmente para colaboração em equipe.
6. **Esteja ciente da análise de dados**: Perguntas puladas resultarão em dados ausentes. Planeje sua análise de acordo.

## Solução de problemas de lógica de salto

- **Erros de sintaxe**: Garanta que todos os `${ }` estejam devidamente fechados e escritos corretamente.
- **Referências circulares**: Evite criar loops onde as perguntas dependem umas das outras.
- **Diferenciação de maiúsculas e minúsculas**: Lembre-se que as opções de resposta diferenciam maiúsculas de minúsculas nas expressões de relevância.
- **Comparações numéricas**: Use operadores apropriados (`<`, `>`, `=`) para comparações numéricas.

## Conclusão

O uso eficaz da lógica de salto pode melhorar significativamente a experiência do respondente e a qualidade dos dados nos seus projetos rtSurvey. Ao aproveitar os recursos avançados do rtSurvey e seguir as práticas recomendadas, você pode criar pesquisas dinâmicas e eficientes que se adaptam à situação única de cada respondente.
