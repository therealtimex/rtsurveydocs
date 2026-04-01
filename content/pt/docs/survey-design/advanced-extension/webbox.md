---
title: "Webbox"
description: "O Webbox incorpora uma página web externa dentro do inquérito como um iframe modal, permitindo aos enumeradores ver referências ou interagir com ferramentas externas sem sair do formulário."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 299
---

**Webbox** incorpora uma página web externa dentro do inquérito como um **popup modal** (iframe). O enumerador toca num botão na etiqueta ou no texto de nota, a página abre num sobreposição de ecrã completo dentro do formulário, e quando a fecha volta exatamente ao ponto onde estava. Isto permite mostrar material de referência, mapas, painéis de controlo ou ferramentas personalizadas sem abrir um separador de navegador separado.

---

## Sintaxe

Insira uma tag HTML `<webbox>` diretamente na coluna de etiqueta de um campo `label` ou `note`:

```html
<webbox src='https://example.com/reference' title='Guia de Referência'>Abrir Guia de Referência</webbox>
```

| Atributo | Descrição |
|----------|-----------|
| `src` | O URL a carregar no iframe. Suporta aspas simples e duplas. |
| `title` | Texto exibido na barra de cabeçalho do modal. Suporta texto simples. |
| *(conteúdo)* | A etiqueta de botão clicável mostrada no campo do inquérito |

---

## Exemplo básico

| type | name | label |
|------|------|-------|
| note | ref_guide | `<webbox src='https://docs.example.com/field-guide' title='Guia de Campo'>Abrir Guia de Campo</webbox>` |

Isto renderiza um botão com a etiqueta "Abrir Guia de Campo". Quando tocado, um modal abre exibindo o website do guia de campo.

---

## Incorporar um mapa

| type | name | label |
|------|------|-------|
| note | area_map | `<webbox src='https://maps.example.com/survey-area' title='Mapa da Área de Inquérito'>Ver Mapa</webbox>` |

---

## Passar valores do formulário para a página incorporada

Adicione valores de campos do formulário ao URL usando `concat()` na coluna `calculation` e referencie o resultado na etiqueta:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | webbox_url | | `concat('https://dashboard.example.com/household?id=', ${household_id})` |
| note | hh_dash | `<webbox src='${webbox_url}' title='Painel do Agregado Familiar'>Abrir Painel</webbox>` |

{{% alert icon=" " context="warning" %}}
O atributo `src` na tag `<webbox>` suporta referências `${fieldname}` quando a etiqueta é calculada a partir de um campo `calculate`. Construa o URL completo num campo `calculate` e referencie-o.
{{% /alert %}}

---

## Interação com repetições: botões de eliminação

O Webbox também suporta tags de ação especiais para gerir grupos de repetição dentro de etiquetas:

```html
<delete-repeat-current>Remover esta linha</delete-repeat-current>
<delete-repeat-last>Remover última linha</delete-repeat-last>
```

Estes renderizam como botões que eliminam instâncias de repetição quando tocados. Coloque-os num campo `note` dentro (ou imediatamente após) o grupo de repetição:

| type | name | label |
|------|------|-------|
| begin_repeat | items | Item |
| text | item_name | Nome do item |
| note | delete_btn | `<delete-repeat-current>Remover este item</delete-repeat-current>` |
| end_repeat | | |

---

## Comunicação com a página incorporada (postMessage)

O iframe do webbox e o formulário pai podem comunicar usando a API `postMessage` do navegador. O pai envia uma mensagem `init` para o iframe quando abre. A página incorporada pode responder com:

- `delete-repeat-current` — aciona a eliminação da instância de repetição atual
- `delete-repeat-last` — aciona a eliminação da última instância de repetição

Isto permite que ferramentas web personalizadas (por ex., ferramentas de desenho, mapas interativos) acionem ações de formulário quando o utilizador confirma uma ação dentro do iframe.

---

## Melhores Práticas

1. Use o webbox para **material de referência** (diretrizes, tabelas de pesquisa, mapas) — não para recolher dados que devem estar no formulário.
2. Certifique-se de que o URL incorporado é acessível a partir da rede do dispositivo — o webbox requer conectividade.
3. Mantenha a página incorporada com boa adaptação a dispositivos móveis — o modal tem no máximo 800px de largura e 80% da altura do viewport.
4. Use texto de botão descritivo (por ex., "Ver Mapa da Aldeia") em vez de etiquetas genéricas ("Clique aqui").
5. Informe os enumeradores que fechar o modal os devolve ao inquérito — alguns utilizadores podem não saber como fechar uma sobreposição de iframe.

## Limitações

- O Webbox requer conectividade de rede para carregar o URL incorporado.
- Alguns sites externos bloqueiam a incorporação em iframes via cabeçalhos `X-Frame-Options` ou `Content-Security-Policy` — estes sites não podem ser usados com webbox.
- O modal fecha quando o enumerador navega para longe da pergunta — qualquer estado não guardado no iframe é perdido.
- O Webbox é uma extensão de formulário web do rtSurvey e pode não funcionar noutros clientes compatíveis com ODK.
