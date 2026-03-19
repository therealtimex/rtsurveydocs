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

### Funções de string

{{% alert icon=" " context="warning" %}}
Ao trabalhar com strings em expressões, é importante usar aspas simples ('') para incluir strings literais. No entanto, há uma exceção quando você quer incluir aspas simples dentro de uma string literal. Nesses casos, você pode usar aspas duplas ("") para envolver toda a string.

Por exemplo:
- Correto: if(${yesno} = 1, "a string with 'single quotes' in it", "no single quotes here")
- Incorreto: if(${yesno} = 1, 'a string with 'single quotes' in it', 'no single quotes here')

Em relação às aspas inteligentes, é crucial estar ciente de sua presença, pois elas podem causar problemas em expressões. Muitos editores de texto rico convertem automaticamente aspas retas ("" ou '') em aspas inteligentes ou curvas ("" ou ''), o que pode resultar em erros de sintaxe ou comportamento inesperado. Para evitar isso, certifique-se de usar aspas retas ('') de forma consistente em suas expressões.
{{% /alert %}}

O rtSurvey suporta várias funções, incluindo:

1. `string(field)`: Converte um campo para uma string.
   - Exemplo: `string(34.8)` será convertido para `'34.8'`.

2. `string-length(field)`: Retorna o comprimento de um campo string.
   - Exemplo: `string-length(.) > 3 and string-length(.) < 10` pode ser usado para garantir que o campo atual tenha entre 3 e 10 caracteres.

3. `substr(fieldorstring, startindex, endindex)`: Retorna uma substring começando em `startindex` e terminando logo antes de `endindex`. Os índices começam em 0 para o primeiro caractere da string.
   - Exemplo: `substr(${phone}, 0, 3)` retornará os três primeiros dígitos de um número de telefone.

4. `concat(a, b, c, ...)`: Concatena campos (e/ou strings) juntos.
   - Exemplo: `concat(${firstname}, ' ', ${lastname})` retornará um nome completo combinando os valores nos campos `firstname` e `lastname`.

5. `linebreak()`: Retorna um caractere de quebra de linha.
   - Exemplo: `concat(${field1}, linebreak(), ${field2}, linebreak(), ${field3})` retornará uma lista de três valores de campo com quebras de linha entre eles.

6. `lower()`: Converte uma string para todos os caracteres minúsculos.
   - Exemplo: `lower('Street Name')` retornará "street name".

7. `upper()`: Converte uma string para todos os caracteres maiúsculos.
   - Exemplo: `upper('Street Name')` retornará "STREET NAME".

### Funções select_one e select_multiple

1. `count-selected(field)`: Retorna o número de itens selecionados em um campo select_multiple.
   - Exemplo: `count-selected(.) = 3` pode ser usado como expressão de restrição para garantir que exatamente três opções sejam selecionadas.

2. `selected(field, value)`: Retorna verdadeiro ou falso dependendo se o valor especificado foi selecionado no campo select_one ou select_multiple.
   - Exemplo: `selected(${color}, 'Blue')` pode ser usado como expressão de relevância para mostrar um grupo ou campo somente se o respondente selecionou "Blue" como sua cor favorita.
   - Nota: O segundo parâmetro deve sempre especificar o valor da opção, não o rótulo da opção. Use o valor da coluna value na planilha de opções da definição do formulário.

3. `selected-at(field, number)`: Retorna o item selecionado na posição especificada em um campo select_multiple. Quando o número passado é 0, retorna o primeiro item selecionado; quando o número é 1, retorna o segundo item selecionado, e assim por diante.
   - Exemplo: `selected-at(${fruits}, 0) = 'Apple'` pode ser usado como expressão de relevância para mostrar um grupo ou campo somente se a primeira opção selecionada for "Apple".
   - Nota: O valor retornado será o valor da opção, não o rótulo. Use o valor da coluna value na planilha de opções da definição do formulário.

4. `choice-label(field, value)`: Retorna o rótulo para uma opção de campo select_one ou select_multiple, conforme definido na planilha de opções da definição do formulário.
   - Exemplo 1: `choice-label(${country}, ${country})` retornará o rótulo da opção para a opção atualmente selecionada no campo chamado `country`.
   - Exemplo 2: `choice-label(${languages}, selected-at(${languages}, 0))` retornará o rótulo para a primeira opção selecionada no campo chamado `languages`.
   - Nota: Esta função recupera o rótulo da opção, não o valor. Ela usa a coluna label da planilha de opções da definição do formulário.

### Funções de campo repetido

No rtSurvey, se você quiser fazer a(s) mesma(s) pergunta(s) várias vezes, pode colocar um campo dentro de um grupo de repetição. Isso resulta em múltiplas instâncias do mesmo campo. As seguintes funções podem ajudar a lidar com esses campos repetidos e os dados repetidos que eles produzem. Consulte o tópico de ajuda sobre campos repetidos para mais detalhes.

1. `join(string, repeatedfield)`: Para um campo dentro de um grupo de repetição, gera uma lista separada por string dos valores. O primeiro parâmetro especifica o delimitador a usar para separar os valores.
   - Exemplo: `join(', ', ${member_name})` gerará uma lista única separada por vírgulas de todos os nomes inseridos.

2. `join-if(string, repeatedfield, expression)`: Funciona exatamente como `join()`, exceto que verifica cada instância no grupo de repetição usando a expressão fornecida. Se a expressão for avaliada como falsa, o item será omitido da saída.
   - Exemplo: `join-if(', ', ${member_name}, ${age} >= 18)` gerará uma lista separada por vírgulas de nomes apenas dos membros adultos (aqueles com idades de 18 anos ou mais).

3. `count(repeatgroup)`: Retorna o número atual de vezes que um grupo de repetição se repetiu.
   - Exemplo: `count(${groupname})` retornará o número de instâncias do grupo.

4. `count-if(repeatgroup, expression)`: Funciona exatamente como `count()`, exceto que verifica cada instância no grupo de repetição usando a expressão fornecida. Se a expressão for avaliada como falsa, o item será omitido da saída.
   - Exemplo: `count-if(${members}, ${age} >= 18)` retornará a contagem de membros adultos com base no campo age dentro do grupo de repetição "members".

5. `sum(repeatedfield)`: Para um campo dentro de um grupo de repetição, calcula a soma de todos os valores.
   - Exemplo: `sum(${loan_amount})` retornará o valor total de todos os empréstimos.

6. `sum-if(repeatedfield, expression)`: Funciona exatamente como `sum()`, exceto que verifica cada instância no grupo de repetição usando a expressão fornecida. Se a expressão for avaliada como falsa, o item será omitido da saída.
   - Exemplo: `sum-if(${loan_amount}, ${loan_amount} > 500)` retornará o valor total de todos os empréstimos acima de 500. Empréstimos menores serão ignorados.

7. `min(repeatedfield)`: Para um campo dentro de um grupo de repetição, calcula o mínimo de todos os valores.
   - Exemplo: `min(${member_age})` retornará a idade do membro mais jovem do grupo.

8. `min-if(repeatedfield, expression)`: Funciona exatamente como `min()`, exceto que verifica cada instância no grupo de repetição usando a expressão fornecida. Se a expressão for avaliada como falsa, o item será omitido da saída.
   - Exemplo: `min-if(${member_age}, ${member_age} >= 18)` retornará a idade do adulto mais jovem do grupo. Aqueles com menos de 18 serão ignorados.

9. `max(repeatedfield)`: Para um campo dentro de um grupo de repetição, calcula o máximo de todos os valores.
   - Exemplo: `max(${member_age})` retornará a idade do membro mais velho do grupo.

10. `max-if(repeatedfield, expression)`: Funciona exatamente como `max()`, exceto que verifica cada instância no grupo de repetição usando a expressão fornecida. Se a expressão for avaliada como falsa, o item será omitido da saída.
    - Exemplo: `max-if(${member_age}, ${member_age} >= 18)` retornará a idade do adulto mais velho do grupo. Aqueles com menos de 18 serão ignorados.

11. `index()`: Chamado dentro de um grupo de repetição, retorna o número de índice para o grupo ou instância atual.
    - Exemplo: `index()` quando usado dentro de um grupo de repetição retornará 1 para a primeira instância, 2 para a segunda, e assim por diante.

12. `indexed-repeat(repeatedfield, repeatgroup, index)`: Referencia um campo ou grupo que está dentro de um grupo de repetição de fora desse grupo de repetição. O primeiro parâmetro especifica o campo ou grupo repetido de interesse, o segundo especifica o grupo de repetição dentro do qual o campo ou grupo está localizado, e o terceiro especifica o número da instância dentro do grupo de repetição a usar.
    - Exemplo 1: `indexed-repeat(${name}, ${names}, 1)` retornará o primeiro nome disponível quando o campo name estiver dentro de um grupo de repetição anterior chamado "names".
    - Exemplo 2: `indexed-repeat(${name}, ${names}, index())` obterá o nome correspondente ao número de instância do grupo de repetição atual.

13. `rank-index(index, repeatedfield)`: Esta função calcula a classificação ordinal da instância especificada de um campo repetido para uso fora do grupo de repetição. A classificação 1 é atribuída à instância com o valor mais alto, a classificação 2 à instância com o próximo valor mais alto, e assim por diante. Se você passar um índice inválido ou um índice para uma instância com um valor não numérico, uma classificação de 999 será retornada.
    - Exemplo: `rank-index(1, ${random_draw})` calcula a classificação da primeira instância com base no valor de seu campo `random_draw` comparado aos valores de outras instâncias.

14. `rank-index-if(index, repeatedfield, expression)`: Esta função funciona de forma semelhante a `rank-index()`, mas verifica cada instância no grupo de repetição do campo repetido usando a expressão fornecida. Se a expressão for avaliada como falsa, o item será omitido do cálculo. O índice usado é baseado no conjunto completo de instâncias antes de avaliar a expressão para cada instância. Se você passar um índice para uma instância que foi ignorada por não satisfazer a expressão, ele é considerado um índice inválido e uma classificação de 999 será retornada.
    - Exemplo: `rank-index-if(1, ${age}, ${age} >= 18)` calcula a classificação de idade dentro do conjunto de adultos, considerando apenas as instâncias onde a idade é maior ou igual a 18.

### Funções numéricas

{{< table >}}
| Operador | Operação | Exemplo | Resposta de exemplo |
|----------|----------|---------|---------------------|
| `+` | Adição | 1 + 1 | 2 |
| `-` | Subtração | 3 - 2 | 1 |
| `*` | Multiplicação | 3 * 2 | 6 |
| `div` | Divisão | 10 div 2 | 5 |
| `mod` | Módulo | 9 mod 2 | 1 |
{{< /table >}}

O rtSurvey suporta funções numéricas, incluindo:
- `number(field)`: Converte o valor do campo para um número.
  - Exemplo: `number('34.8')` = 34.8

- `int(field)`: Converte o valor do campo para um inteiro.
  - Exemplo: `int('39.2')` = 39

- `min(field1, ..., fieldx)`: Retorna o valor mínimo entre os campos passados.
  - Exemplo: `min(${father_age}, ${mother_age})` retornará a idade do pai ou da mãe, a que for menor.

- `max(field1, ..., fieldx)`: Retorna o valor máximo entre os campos passados.
  - Exemplo: `max(${father_age}, ${mother_age})` retornará a idade do pai ou da mãe, a que for maior.

- `format-number(field)`: Formata o valor de um campo inteiro ou decimal de acordo com as configurações de localidade do usuário.
  - Exemplo: `format-number(${income})` Esta expressão pode formatar "120000" como "120.000".

- `round(field, digits)`: Arredonda o valor do campo numérico para o número especificado de dígitos após a vírgula decimal.
  - Exemplo: `round(${interest_rate}, 2)`

- `abs(number)`: Retorna o valor absoluto de um número.
  
- `pow(base, exponent)`: Retorna o valor do primeiro parâmetro elevado à potência do segundo parâmetro.
  - Cada parâmetro pode ser um campo, número ou expressão.

- `log10(fieldorvalue)`: Retorna o logaritmo de base dez do campo ou valor passado.

- `sin(fieldorvalue)`: Retorna o seno do campo ou valor passado, expresso em radianos.
  
- `cos(fieldorvalue)`: Retorna o cosseno do campo ou valor passado, expresso em radianos.

- `tan(fieldorvalue)`: Retorna a tangente do campo ou valor passado, expresso em radianos.

- `asin(fieldorvalue)`: Retorna o arco seno do campo ou valor passado, expresso em radianos.

- `acos(fieldorvalue)`: Retorna o arco cosseno do campo ou valor passado, expresso em radianos.

- `atan(fieldorvalue)`: Retorna o arco tangente do campo ou valor passado, expresso em radianos.

- `atan2(x, y)`: Retorna o ângulo em radianos subtendido na origem pelo ponto com coordenadas (x, y) e o eixo x positivo. O resultado está no intervalo de -pi() a pi().

- `sqrt(fieldorvalue)`: Retorna a raiz quadrada não negativa do campo ou valor passado.

- `exp(x)`: Retorna o valor de e^x.

- `pi()`: Retorna o valor de pi.

### Funções de data e hora

{{% alert icon=" " context="warning" %}}
Os valores de data no rtSurvey são armazenados como strings no formato `YYYY-MM-DD`. Os valores de datetime são armazenados como strings ISO 8601 (`YYYY-MM-DDTHH:MM:SS`). Use `decimal-date-time()` para converter para um número para aritmética (por exemplo, calcular durações).
{{% /alert %}}

1. `today()`: Retorna a data de hoje como uma string no formato `YYYY-MM-DD`. Avaliado uma vez quando o formulário abre.
   - Exemplo: `today()` → `'2024-03-15'`
   - Uso comum: coluna `default` para pré-preencher a data de hoje, ou em `relevant`/`constraint` para comparar com um campo de data.

2. `now()`: Retorna a data e hora atuais como uma string ISO 8601. Avaliado cada vez que a expressão é computada.
   - Exemplo: `now()` → `'2024-03-15T14:32:00.000+03:00'`
   - Uso comum: Registrar o registro de data/hora exato de um evento específico durante a pesquisa.

3. `date(value)`: Converte um valor (string ou número) para uma string de data. Útil para converter valores calculados em um tipo de data.
   - Exemplo: `date('2024-03-15')` → `'2024-03-15'`

4. `date-time(value)`: Converte um valor para uma string de datetime.
   - Exemplo: `date-time(${event_timestamp})`

5. `decimal-date-time(value)`: Converte uma string de data ou datetime para um número decimal representando milissegundos desde o epoch Unix dividido por 86400000 (ou seja, dias fracionários desde 1970-01-01). Use isso para realizar aritmética em datas.
   - Exemplo: Duração em dias entre duas datas:
     `decimal-date-time(${end_date}) - decimal-date-time(${start_date})`
   - Exemplo: Duração em minutos entre dois datetimes:
     `(decimal-date-time(${end_time}) - decimal-date-time(${start_time})) * 1440`

6. `format-date(date, format)`: Formata um valor de data usando uma string de padrão.
   - Tokens de formato: `%Y` (ano com 4 dígitos), `%y` (ano com 2 dígitos), `%m` (mês 01–12), `%d` (dia 01–31), `%a` (dia da semana abreviado), `%b` (nome do mês abreviado)
   - Exemplo: `format-date(today(), '%d/%m/%Y')` → `'15/03/2024'`
   - Exemplo: `format-date(${dob}, '%B %d, %Y')` → `'March 15, 1990'`

7. `format-date-time(datetime, format)`: Formata um valor de datetime usando uma string de padrão. Aceita todos os tokens de `format-date` mais:
   - `%H` (hora 00–23), `%h` (hora 01–12), `%M` (minutos 00–59), `%S` (segundos 00–59), `%3` (milissegundos), `%P` (AM/PM)
   - Exemplo: `format-date-time(now(), '%d/%m/%Y %H:%M')` → `'15/03/2024 14:32'`
   - Exemplo: `format-date-time(${event_time}, '%I:%M %p')` → `'02:32 PM'`

---

### Funções booleanas

1. `boolean(value)`: Converte qualquer valor para um booleano. Retorna `true` para strings não vazias, números não zero e `true`; retorna `false` para strings vazias, `0` e `false`.
   - Exemplo: `boolean(${name})` retorna `true` se `name` não estiver vazio.

2. `boolean-from-string(string)`: Retorna `true` se a string for `'1'` ou `'true'` (sem distinção de maiúsculas/minúsculas); retorna `false` caso contrário.
   - Exemplo: `boolean-from-string(${enabled_flag})` — útil quando um campo armazena `'true'`/`'false'` como texto.

3. `true()`: Retorna o valor booleano `true`.
   - Exemplo: Na coluna `required`, `true()` é equivalente a `yes`.

4. `false()`: Retorna o valor booleano `false`.
   - Exemplo: `if(${skip_section} = 'yes', false(), true())` — definir dinamicamente o campo como obrigatório.

5. `not(expression)`: Retorna a negação lógica da expressão. Retorna `true` se a expressão for falsa, e vice-versa.
   - Exemplo: `not(${consent} = 'yes')` — mostrar um aviso quando o consentimento NÃO foi dado.
   - Exemplo: `not(selected(${issues}, 'none'))` — exigir detalhes apenas se "nenhum" não foi selecionado.

---

### Funções de string adicionais

1. `starts-with(string, prefix)`: Retorna `true` se `string` começar com `prefix`.
   - Exemplo: `starts-with(${phone}, '+254')` verifica se o número de telefone começa com o código do país do Quênia.

2. `contains(string, substring)`: Retorna `true` se `string` contiver `substring`.
   - Exemplo: `contains(${email}, '@')` verifica se um endereço de e-mail tem um sinal `@`.
   - Exemplo: `contains(${notes}, 'urgent')` aciona uma pergunta de acompanhamento se as notas mencionarem "urgent".

3. `substring-before(string, needle)`: Retorna a parte de `string` que aparece antes da primeira ocorrência de `needle`.
   - Exemplo: `substring-before(${full_name}, ' ')` extrai a primeira palavra (primeiro nome).

4. `substring-after(string, needle)`: Retorna a parte de `string` que aparece após a primeira ocorrência de `needle`.
   - Exemplo: `substring-after(${email}, '@')` extrai a parte de domínio de um endereço de e-mail.

5. `normalize-space(string)`: Remove espaços em branco iniciais e finais e recolhe todas as sequências internas de espaços para um único espaço.
   - Exemplo: `normalize-space(${name})` — limpa um nome que pode ter sido digitado com espaços extras.

6. `translate(string, search_chars, replace_chars)`: Substitui cada caractere em `string` que aparece em `search_chars` pelo caractere correspondente em `replace_chars`. Caracteres em `search_chars` sem caractere correspondente em `replace_chars` são excluídos.
   - Exemplo: `translate(${code}, 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')` converte para maiúsculas (equivalente a `upper()`).
   - Exemplo: `translate(${phone}, ' -()', '')` remove espaços, traços e parênteses de um número de telefone.

---

### Funções matemáticas adicionais

1. `floor(number)`: Retorna o maior inteiro menor ou igual a `number` (arredonda em direção ao infinito negativo).
   - Exemplo: `floor(4.9)` = 4, `floor(-2.1)` = -3

2. `ceiling(number)`: Retorna o menor inteiro maior ou igual a `number` (arredonda em direção ao infinito positivo).
   - Exemplo: `ceiling(4.1)` = 5, `ceiling(-2.9)` = -2

3. `random()`: Retorna um número decimal aleatório entre 0,0 (inclusive) e 1,0 (exclusivo). Tipicamente usado em campos `calculate` para atribuir valores aleatórios ou randomizar a ordem das perguntas.
   - Exemplo: `random()` → por exemplo, `0.7341`
   - Exemplo: `int(random() * 6) + 1` → número aleatório de 1 a 6 (jogada de dado)

4. `coalesce(a, b)`: Retorna `a` se `a` não estiver vazio; caso contrário, retorna `b`. Útil como fallback quando um campo pode estar vazio.
   - Exemplo: `coalesce(${preferred_name}, ${full_name})` — usa o nome preferido se definido, caso contrário usa o nome completo.

5. `once(value)`: Avalia `value` e o armazena, mas apenas se o campo atual estiver **vazio**. Se o campo já tiver um valor (por exemplo, foi definido anteriormente), `once()` retorna o valor existente sem alteração. Isso evita que o recálculo sobrescreva a entrada do usuário.
   - Exemplo: `once(today())` na coluna `default` define a data de hoje uma vez e não é atualizado se o entrevistador reabrir o formulário.
   - Exemplo: `once(uuid())` gera um UUID uma vez e o mantém estável em reedições.

---

### Funções geográficas

1. `area(geoshape_value)`: Calcula a **área em metros quadrados** delimitada por um valor geoshape (polígono).
   - O parâmetro é um valor de campo geoshape no formato `lat1 lon1 0 0; lat2 lon2 0 0; ...`
   - Exemplo: `area(${field_boundary})` — calcular a área de um campo pesquisado em m².
   - Exemplo: `round(area(${field_boundary}) div 10000, 2)` — converter para hectares.

2. `distance(coordinates)`: Calcula o **comprimento total do caminho em metros** de um geotrace (linha), ou a distância entre dois geopoints.
   - Para um geotrace: `distance(${route})` retorna o comprimento total do caminho em metros.
   - Para dois geopoints: `distance(concat(${point_a}, ' ', ${point_b}))` retorna a distância entre eles.
   - Exemplo: `round(distance(${road_trace}) div 1000, 3)` — comprimento da estrada em quilômetros.

---

### Funções de validação

1. `regex(value, pattern)`: Retorna `true` se `value` corresponder à expressão regular `pattern`. Use na coluna `constraint` para validação baseada em padrão.
   - O padrão usa sintaxe regex padrão (subconjunto POSIX ERE).
   - Exemplo: `regex(., '^[0-9]{10}$')` — validar um número de 10 dígitos.
   - Exemplo: `regex(., '^[A-Z]{2}[0-9]{6}$')` — validar o formato de um número de passaporte (2 letras maiúsculas seguidas de 6 dígitos).
   - Exemplo: `regex(., '^[^@]+@[^@]+\.[^@]{2,}$')` — verificação básica do formato de e-mail.

2. `checklist(min, max, v1, v2, ...)`: Avalia uma lista de expressões booleanas e retorna `true` se o número de valores `true` estiver entre `min` e `max` (inclusive). Passe `-1` para `min` ou `max` para ignorar esse limite.
   - Exemplo: `checklist(2, 3, ${q1} = 'yes', ${q2} = 'yes', ${q3} = 'yes')` — passa se exatamente 2 ou 3 das três condições forem verdadeiras.
   - Exemplo: `checklist(1, -1, ${smoke_alarm}, ${fire_ext}, ${emergency_plan})` — pelo menos uma medida de segurança deve ser verdadeira.

3. `weighted-checklist(min, max, v1, w1, v2, w2, ...)`: Como `checklist()`, mas cada valor tem um peso. A soma dos pesos para valores `true` deve estar entre `min` e `max`.
   - Exemplo: `weighted-checklist(10, -1, ${has_toilet}, 4, ${has_sink}, 3, ${has_shower}, 5)` — a soma dos pesos para instalações presentes deve ser pelo menos 10.

---

### Funções utilitárias

1. `uuid()`: Gera um UUID aleatório (formato RFC 4122 v4) como uma string.
   - Exemplo: `uuid()` → `'a3f8b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c'`
   - Tipicamente usado com `once()` para gerar um ID único estável: `once(uuid())`

2. `version()`: Retorna o valor do atributo `version` do formulário conforme definido na planilha de configurações.
   - Exemplo: `version()` → `'3.1'`
   - Útil em campos `calculate` para incorporar a versão do formulário nos dados exportados.

3. `position()`: Quando chamado dentro de um **grupo de repetição**, retorna o índice base 1 da instância de repetição atual.
   - Exemplo: `position()` na primeira instância retorna `1`, na segunda retorna `2`, e assim por diante.
   - Veja também: `index()` (alias), `indexed-repeat()` para referenciar valores de repetição de fora do grupo.

4. `thousandsep(length, separator, value)`: Formata um número com um separador de milhares. `length` é o comprimento total mínimo da string (preenchido com espaços se menor), `separator` é o caractere a usar (por exemplo, `','`), e `value` é o número a formatar.
   - Exemplo: `thousandsep(0, ',', 1234567)` → `'1,234,567'`
   - Exemplo: `thousandsep(0, '.', ${income})` → formata a renda com ponto como separador de milhares.

5. `substr-jsonpath(value, jsonpath)`: Extrai uma substring de uma string JSON usando uma expressão JSONPath.
   - Exemplo: `substr-jsonpath(${api_response}, '$.data.name')` — extrai o campo `name` de uma string JSON armazenada em `api_response`.
   - Tipicamente usado junto com `callapi()` para extrair valores específicos das respostas da API.
