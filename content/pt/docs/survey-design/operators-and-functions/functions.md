---
title: "Funções"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 293
---

### Funções de cadeia de caracteres

{{% alert icon=" " context="warning" %}}
Ao trabalhar com cadeias de caracteres dentro de expressões, é importante usar aspas simples ('') para delimitar cadeias literais. No entanto, surge uma exceção quando quer incluir aspas simples dentro de uma cadeia literal. Nesses casos, pode usar aspas duplas ("") para delimitar toda a cadeia.

Por exemplo:
- Correto: if(${yesno} = 1, "a string with 'single quotes' in it", "no single quotes here")
- Incorreto: if(${yesno} = 1, 'a string with 'single quotes' in it', 'no single quotes here')

Relativamente às aspas inteligentes, é crucial estar ciente da sua presença, pois podem causar problemas em expressões. Muitos editores de texto enriquecido convertem automaticamente aspas diretas ("" ou '') em aspas inteligentes ou curvas ("" ou ''), o que pode resultar em erros de sintaxe ou comportamento inesperado. Para evitar isto, certifique-se de que está a usar aspas diretas ('') de forma consistente nas suas expressões.
{{% /alert %}}

O rtSurvey suporta várias funções, incluindo:

1. `string(field)`: Converte um campo para uma cadeia de caracteres.
   - Exemplo: `string(34.8)` será convertido para `'34.8'`.

2. `string-length(field)`: Retorna o comprimento de um campo de cadeia de caracteres.
   - Exemplo: `string-length(.) > 3 and string-length(.) < 10` pode ser usado para garantir que o campo atual tem entre 3 e 10 caracteres.

3. `substr(fieldorstring, startindex, endindex)`: Retorna uma subcadeia de caracteres começando em `startindex` e terminando imediatamente antes de `endindex`. Os índices começam em 0 para o primeiro carácter na cadeia.
   - Exemplo: `substr(${phone}, 0, 3)` retornará os primeiros três dígitos de um número de telefone.

4. `concat(a, b, c, ...)`: Concatena campos (e/ou cadeias de caracteres) juntos.
   - Exemplo: `concat(${firstname}, ' ', ${lastname})` retornará um nome completo combinando os valores nos campos `firstname` e `lastname`.

5. `linebreak()`: Retorna um carácter de quebra de linha.
   - Exemplo: `concat(${field1}, linebreak(), ${field2}, linebreak(), ${field3})` retornará uma lista de três valores de campo com quebras de linha entre eles.

6. `lower()`: Converte uma cadeia de caracteres para todos os caracteres em minúsculas.
   - Exemplo: `lower('Street Name')` retornará "street name".

7. `upper()`: Converte uma cadeia de caracteres para todos os caracteres em maiúsculas.
   - Exemplo: `upper('Street Name')` retornará "STREET NAME".

### Funções select_one e select_multiple

1. `count-selected(field)`: Retorna o número de itens selecionados num campo select_multiple.
   - Exemplo: `count-selected(.) = 3` pode ser usado como expressão de restrição para garantir que exatamente três escolhas estão selecionadas.

2. `selected(field, value)`: Retorna verdadeiro ou falso dependendo de se o valor especificado foi selecionado no campo select_one ou select_multiple.
   - Exemplo: `selected(${color}, 'Blue')` pode ser usado como expressão de relevância para mostrar um grupo ou campo apenas se o respondente selecionou "Blue" como cor favorita.
   - Nota: O segundo parâmetro deve sempre especificar o valor da escolha, não a etiqueta da escolha. Use o valor da coluna de valor na folha de trabalho choices da definição do formulário.

3. `selected-at(field, number)`: Retorna o item selecionado na posição especificada num campo select_multiple. Quando o número passado é 0, retorna o primeiro item selecionado; quando o número é 1, retorna o segundo item selecionado, e assim por diante.
   - Exemplo: `selected-at(${fruits}, 0) = 'Apple'` pode ser usado como expressão de relevância para mostrar um grupo ou campo apenas se a primeira escolha selecionada for "Apple".
   - Nota: O valor retornado será o valor da escolha, não a etiqueta da escolha.

4. `choice-label(field, value)`: Retorna a etiqueta para uma escolha de campo select_one ou select_multiple, conforme definido na folha de trabalho choices da definição do formulário.
   - Exemplo 1: `choice-label(${country}, ${country})` retornará a etiqueta de escolha para a escolha atualmente selecionada no campo denominado `country`.
   - Exemplo 2: `choice-label(${languages}, selected-at(${languages}, 0))` retornará a etiqueta para a primeira escolha selecionada no campo denominado `languages`.

### Funções de campo repetido

No rtSurvey, se quiser fazer a(s) mesma(s) pergunta(s) múltiplas vezes, pode colocar um campo dentro de um grupo de repetição. Isto resulta em múltiplas instâncias do mesmo campo. As seguintes funções podem ajudá-lo a lidar com estes campos repetidos e os dados repetidos que produzem.

1. `join(string, repeatedfield)`: Para um campo dentro de um grupo de repetição, gera uma lista de valores separados por cadeia de caracteres. O primeiro parâmetro especifica o delimitador a usar para separar os valores.
   - Exemplo: `join(', ', ${member_name})` gerará uma única lista separada por vírgulas de todos os nomes introduzidos.

2. `join-if(string, repeatedfield, expression)`: Funciona exatamente como `join()`, exceto que verifica cada instância no grupo de repetição usando a expressão fornecida. Se a expressão for avaliada como falsa, o item será omitido da saída.
   - Exemplo: `join-if(', ', ${member_name}, ${age} >= 18)` gerará uma lista separada por vírgulas de nomes apenas de membros adultos.

3. `count(repeatgroup)`: Retorna o número atual de vezes que um grupo de repetição se repetiu.
   - Exemplo: `count(${groupname})` retornará o número de instâncias do grupo.

4. `count-if(repeatgroup, expression)`: Funciona exatamente como `count()`, exceto que verifica cada instância no grupo de repetição usando a expressão fornecida.
   - Exemplo: `count-if(${members}, ${age} >= 18)` retornará a contagem de membros adultos.

5. `sum(repeatedfield)`: Para um campo dentro de um grupo de repetição, calcula a soma de todos os valores.
   - Exemplo: `sum(${loan_amount})` retornará o valor total de todos os empréstimos.

6. `sum-if(repeatedfield, expression)`: Funciona exatamente como `sum()`, exceto que verifica cada instância.
   - Exemplo: `sum-if(${loan_amount}, ${loan_amount} > 500)` retornará o valor total de todos os empréstimos superiores a 500.

7. `min(repeatedfield)`: Para um campo dentro de um grupo de repetição, calcula o mínimo de todos os valores.
   - Exemplo: `min(${member_age})` retornará a idade do membro mais jovem no grupo.

8. `min-if(repeatedfield, expression)`: Funciona exatamente como `min()`, exceto que verifica cada instância.
   - Exemplo: `min-if(${member_age}, ${member_age} >= 18)` retornará a idade do adulto mais jovem.

9. `max(repeatedfield)`: Para um campo dentro de um grupo de repetição, calcula o máximo de todos os valores.
   - Exemplo: `max(${member_age})` retornará a idade do membro mais velho no grupo.

10. `max-if(repeatedfield, expression)`: Funciona exatamente como `max()`, exceto que verifica cada instância.
    - Exemplo: `max-if(${member_age}, ${member_age} >= 18)` retornará a idade do adulto mais velho.

11. `index()`: Chamada dentro de um grupo de repetição, retorna o número de índice para o grupo ou instância atual.
    - Exemplo: `index()` quando usado dentro de um grupo de repetição retornará 1 para a primeira instância, 2 para a segunda, e assim por diante.

12. `indexed-repeat(repeatedfield, repeatgroup, index)`: Referencia um campo ou grupo que está dentro de um grupo de repetição a partir de fora desse grupo de repetição.
    - Exemplo 1: `indexed-repeat(${name}, ${names}, 1)` retornará o primeiro nome disponível quando o campo de nome está dentro de um grupo de repetição anterior denominado "names".

13. `rank-index(index, repeatedfield)`: Esta função calcula o ranking ordinal da instância especificada de um campo repetido para uso fora do grupo de repetição.
    - Exemplo: `rank-index(1, ${random_draw})` calcula o ranking da primeira instância com base no valor do seu campo `random_draw`.

14. `rank-index-if(index, repeatedfield, expression)`: Esta função funciona de forma semelhante a `rank-index()`, mas verifica cada instância usando a expressão fornecida.
    - Exemplo: `rank-index-if(1, ${age}, ${age} >= 18)` calcula o ranking de idade dentro do conjunto de adultos.

### Funções numéricas

{{< table >}}
| Operador | Operação | Exemplo | Resposta de exemplo |
|----------|-----------|---------|----------------|
| `+` | Adição | 1 + 1 | 2 |
| `-` | Subtração | 3 - 2 | 1 |
| `*` | Multiplicação | 3 * 2 | 6 |
| `div` | Divisão | 10 div 2 | 5 |
| `mod` | Módulo | 9 mod 2 | 1 |
{{< /table >}}

O rtSurvey suporta funções numéricas, incluindo:
- `number(field)`: Converte o valor do campo para um número.
- `int(field)`: Converte o valor do campo para um número inteiro.
- `min(field1, ..., fieldx)`: Retorna o valor mínimo entre os campos passados.
- `max(field1, ..., fieldx)`: Retorna o valor máximo entre os campos passados.
- `format-number(field)`: Formata o valor de um campo inteiro ou decimal de acordo com as configurações regionais do utilizador.
- `round(field, digits)`: Arredonda o valor do campo numérico para o número especificado de dígitos após o ponto decimal.
- `abs(number)`: Retorna o valor absoluto de um número.
- `pow(base, exponent)`: Retorna o valor do primeiro parâmetro elevado à potência do segundo parâmetro.
- `log10(fieldorvalue)`: Retorna o logaritmo de base dez do campo ou valor passado.
- `sin(fieldorvalue)`: Retorna o seno do campo ou valor passado, expresso em radianos.
- `cos(fieldorvalue)`: Retorna o cosseno do campo ou valor passado, expresso em radianos.
- `tan(fieldorvalue)`: Retorna a tangente do campo ou valor passado, expresso em radianos.
- `asin(fieldorvalue)`: Retorna o arco seno do campo ou valor passado, expresso em radianos.
- `acos(fieldorvalue)`: Retorna o arco cosseno do campo ou valor passado, expresso em radianos.
- `atan(fieldorvalue)`: Retorna o arco tangente do campo ou valor passado, expresso em radianos.
- `sqrt(fieldorvalue)`: Retorna a raiz quadrada não negativa do campo ou valor passado.
- `exp(x)`: Retorna o valor de e^x.
- `pi()`: Retorna o valor de pi.

### Funções de data e hora

{{% alert icon=" " context="warning" %}}
Os valores de data no rtSurvey são armazenados como cadeias de caracteres no formato `YYYY-MM-DD`. Os valores de data e hora são armazenados como cadeias ISO 8601 (`YYYY-MM-DDTHH:MM:SS`). Use `decimal-date-time()` para converter para um número para aritmética (por ex., calcular durações).
{{% /alert %}}

1. `today()`: Retorna a data de hoje como uma cadeia de caracteres no formato `YYYY-MM-DD`. Avaliado uma vez quando o formulário abre.

2. `now()`: Retorna a data e hora atuais como uma cadeia ISO 8601. Avaliado cada vez que a expressão é calculada.

3. `date(value)`: Converte um valor (cadeia de caracteres ou número) para uma cadeia de data.

4. `date-time(value)`: Converte um valor para uma cadeia de data e hora.

5. `decimal-date-time(value)`: Converte uma cadeia de data ou data e hora para um número decimal. Use isto para realizar aritmética em datas.
   - Exemplo: Duração em dias entre duas datas:
     `decimal-date-time(${end_date}) - decimal-date-time(${start_date})`

6. `format-date(date, format)`: Formata um valor de data usando uma cadeia de padrão.
   - Tokens de formato: `%Y` (ano 4 dígitos), `%y` (ano 2 dígitos), `%m` (mês 01–12), `%d` (dia 01–31), `%a` (dia da semana abreviado), `%b` (nome do mês abreviado)

7. `format-date-time(datetime, format)`: Formata um valor de data e hora usando uma cadeia de padrão. Aceita todos os tokens `format-date` mais:
   - `%H` (hora 00–23), `%h` (hora 01–12), `%M` (minutos 00–59), `%S` (segundos 00–59), `%3` (milissegundos), `%P` (AM/PM)

### Funções booleanas

1. `boolean(value)`: Converte qualquer valor para um booleano.
2. `boolean-from-string(string)`: Retorna `true` se a cadeia for `'1'` ou `'true'` (sem distinção de maiúsculas/minúsculas); retorna `false` caso contrário.
3. `true()`: Retorna o valor booleano `true`.
4. `false()`: Retorna o valor booleano `false`.
5. `not(expression)`: Retorna a negação lógica da expressão.
   - Exemplo: `not(${consent} = 'yes')` — mostra um aviso quando o consentimento NÃO foi dado.

### Funções adicionais de cadeia de caracteres

1. `starts-with(string, prefix)`: Retorna `true` se `string` começar com `prefix`.
2. `contains(string, substring)`: Retorna `true` se `string` contiver `substring`.
3. `substring-before(string, needle)`: Retorna a parte de `string` que aparece antes da primeira ocorrência de `needle`.
4. `substring-after(string, needle)`: Retorna a parte de `string` que aparece após a primeira ocorrência de `needle`.
5. `normalize-space(string)`: Remove espaços em branco iniciais e finais e colapsa todas as sequências de espaço em branco internas para um único espaço.
6. `translate(string, search_chars, replace_chars)`: Substitui cada carácter em `string` que aparece em `search_chars` pelo carácter correspondente em `replace_chars`.

### Funções matemáticas adicionais

1. `floor(number)`: Retorna o maior inteiro menor ou igual a `number`.
2. `ceiling(number)`: Retorna o menor inteiro maior ou igual a `number`.
3. `random()`: Retorna um número decimal aleatório entre 0.0 (inclusivo) e 1.0 (exclusivo).
4. `coalesce(a, b)`: Retorna `a` se `a` não estiver vazio; caso contrário retorna `b`.
5. `once(value)`: Avalia `value` e armazena-o, mas apenas se o campo atual estiver **vazio**.
   - Exemplo: `once(today())` na coluna `default` define a data de hoje uma vez e não atualiza se o enumerador reabrir o formulário.
   - Exemplo: `once(uuid())` gera um UUID uma vez e mantém-no estável em reedições.

### Funções geográficas

1. `area(geoshape_value)`: Calcula a **área em metros quadrados** delimitada por um valor de geoshape (polígono).
   - Exemplo: `area(${field_boundary})` — calcula a área de um campo levantado em m².

2. `distance(coordinates)`: Calcula o **comprimento total do caminho em metros** de um geotrace (linha), ou a distância entre dois geopoints.
   - Exemplo: `round(distance(${road_trace}) div 1000, 3)` — comprimento da estrada em quilómetros.

### Funções de validação

1. `regex(value, pattern)`: Retorna `true` se `value` corresponder à expressão regular `pattern`.
   - Exemplo: `regex(., '^[0-9]{10}$')` — validar um número de 10 dígitos.

2. `checklist(min, max, v1, v2, ...)`: Avalia uma lista de expressões booleanas e retorna `true` se o número de valores `true` estiver entre `min` e `max`.

3. `weighted-checklist(min, max, v1, w1, v2, w2, ...)`: Como `checklist()`, mas cada valor tem um peso. A soma de pesos para valores `true` deve estar entre `min` e `max`.

### Funções utilitárias

1. `uuid()`: Gera um UUID aleatório (formato RFC 4122 v4) como cadeia de caracteres.
   - Tipicamente usado com `once()` para gerar um ID único estável: `once(uuid())`

2. `version()`: Retorna o valor do atributo `version` do formulário conforme definido na folha de trabalho settings.

3. `position()`: Quando chamada dentro de um **grupo de repetição**, retorna o índice de base 1 da instância de repetição atual.

4. `thousandsep(length, separator, value)`: Formata um número com um separador de milhares.
   - Exemplo: `thousandsep(0, ',', 1234567)` → `'1,234,567'`

5. `substr-jsonpath(value, jsonpath)`: Extrai uma subcadeia de caracteres de uma cadeia JSON usando uma expressão JSONPath.
   - Exemplo: `substr-jsonpath(${api_response}, '$.data.name')` — extrai o campo `name` de uma cadeia JSON armazenada em `api_response`.
