---
title: "Agrupando perguntas"
description: ""
icon: "auto_awesome"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 250
---

Os grupos no XLSForm permitem organizar perguntas relacionadas, melhorando a estrutura da sua pesquisa e aprimorando as capacidades de análise de dados. O rtSurvey suporta totalmente os grupos do XLSForm e estende sua funcionalidade com recursos adicionais.

## Estrutura básica de grupo

Para criar um grupo de perguntas, use a sintaxe `begin_group` e `end_group`:

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | respondent | Informações do respondente               |
| text         | name       | Insira o nome do respondente             |
| text         | position   | Insira o cargo do respondente            |
| end_group    |            |                                          |
```

Pontos principais:
- A linha `begin_group` requer um `name` e um `label`.
- A linha `end_group` não precisa de nome ou rótulo.
- As perguntas entre `begin_group` e `end_group` fazem parte do grupo.

## Aparência do grupo

O rtSurvey suporta várias opções de aparência para grupos:

1. **field-list**: Exibe várias perguntas na mesma tela.
   ```
   | type         | name       | label       | appearance |
   |--------------|------------|-------------|------------|
   | begin_group  | respondent | Respondente | field-list |
   | text         | name       | Nome        |            |
   | text         | position   | Cargo       |            |
   | end_group    |            |             |            |
   ```

2. **grid**: Cria um layout compacto, semelhante a uma tabela, para grupos (específico do rtSurvey).
   ```
   | type         | name       | label     | appearance |
   |--------------|------------|-----------|------------|
   | begin_group  | household  | Domicílio | grid       |
   | text         | member_name| Nome      |            |
   | integer      | member_age | Idade     |            |
   | end_group    |            |           |            |
   ```

3. **collapsible**: Cria grupos expansíveis/recolhíveis (específico do rtSurvey).
   ```
   | type         | name       | label    | appearance  |
   |--------------|------------|----------|-------------|
   | begin_group  | details    | Detalhes | collapsible |
   | text         | address    | Endereço |             |
   | text         | phone      | Telefone |             |
   | end_group    |            |          |             |
   ```

## Grupos aninhados

Os grupos podem ser aninhados dentro de outros grupos para estruturas mais complexas:

```
| type         | name       | label                                    |
|--------------|------------|------------------------------------------|
| begin_group  | hospital   | Informações do hospital                  |
| text         | hosp_name  | Qual é o nome deste hospital?            |
| begin_group  | medication | Disponibilidade de medicamentos          |
| select_one y_n| hiv_meds  | Este hospital tem medicamentos para HIV? |
| end_group    |            |                                          |
| end_group    |            |                                          |
```

**Nota**: Sempre termine o grupo iniciado mais recentemente primeiro para manter o aninhamento adequado.

## Lógica de salto para grupos

Use a coluna `relevant` para implementar lógica de salto para grupos inteiros:

```
| type         | name   | label                                        | relevant        |
|--------------|--------|----------------------------------------------|-----------------|
| integer      | age    | Quantos anos você tem?                       |                 |
| begin_group  | child  | Criança                                      | ${age} <= 5     |
| integer      | muac   | Registre a circunferência do meio do braço   |                 |
| select_one y_n| mrdt  | O teste de diagnóstico rápido da criança é positivo? |           |
| end_group    |        |                                              |                 |
```

Neste exemplo, o grupo `child` aparecerá apenas se a idade do respondente for 5 anos ou menos.

## Práticas recomendadas para usar grupos

1. Use nomes significativos para os grupos para melhorar a análise de dados.
2. Mantenha os grupos focados em perguntas relacionadas.
3. Use grupos aninhados com moderação para evitar estruturas excessivamente complexas.
4. Teste minuciosamente a lógica de salto ao usar `relevant` em grupos.
5. Considere usar a aparência `field-list` para grupos curtos para reduzir a rolagem.
6. Utilize o layout em grade do rtSurvey para exibição compacta de informações relacionadas.
7. Use grupos recolhíveis para formulários longos para melhorar a navegação.

## Recursos específicos do rtSurvey

1. **Layout em grade**: Use a aparência `grid` para exibições semelhantes a tabelas.
2. **Grupos recolhíveis**: Implemente a aparência `collapsible` para seções expansíveis.
3. **Estilo personalizado**: Aplique CSS personalizado a grupos para designs visuais únicos.
4. **Comportamento dinâmico de grupo**: Implemente lógica de salto complexa e cálculos dentro de grupos.

## Suporte multilíngue

O rtSurvey suporta grupos multilíngues. Use colunas específicas de idioma para rótulos:

```
| type         | name       | label::Português | label::English |
|--------------|------------|------------------|----------------|
| begin_group  | personal   | Informações pessoais | Personal Info |
| text         | name       | Nome             | Name           |
| end_group    |            |                  |                |
```

## Considerações sobre aplicativo móvel

- Grupos com a aparência `field-list` são exibidos como uma única tela no aplicativo móvel.
- Grupos recolhíveis podem melhorar a navegação em telas menores.
- Layouts em grade podem se ajustar para melhor visibilidade em dispositivos móveis.

## Limitações conhecidas

- Aninhamento excessivamente profundo de grupos pode afetar o desempenho em alguns dispositivos.
- Algumas opções avançadas de estilo podem não estar disponíveis para grupos no aplicativo móvel.

## Solução de problemas de grupos

1. Certifique-se de que cada `begin_group` tem um `end_group` correspondente.
2. Verifique se os nomes dos grupos são únicos dentro do formulário.
3. Verifique se a lógica de salto faz referência a nomes de perguntas corretos.
4. Teste grupos minuciosamente nas interfaces web e móvel.

Ao usar grupos de forma eficaz nos seus XLSForms com o rtSurvey, você pode criar pesquisas bem organizadas e eficientes que melhoram tanto a experiência de coleta de dados quanto a qualidade da sua análise de dados.
