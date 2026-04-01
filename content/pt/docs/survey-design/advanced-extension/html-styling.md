---
title: "HTML Styling"
description: "O rtSurvey suporta tags HTML em etiquetas e dicas, permitindo formatação de texto rico, ligações e temas de cores dinâmicos."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 297
---

O rtSurvey renderiza o texto de **etiqueta** e **dica** como HTML em formulários web. Isto significa que pode usar tags HTML padrão para formatar texto, adicionar quebras de linha, criar ligações e aplicar cores. Isto é particularmente útil para campos de nota, instruções de secção e resumos dinâmicos.

{{% alert icon=" " context="warning" %}}
O HTML em etiquetas é renderizado no **formulário web** e nas aplicações móveis rtSurvey. Pode não ser renderizado em todos os clientes compatíveis com ODK. Teste sempre na sua plataforma alvo.
{{% /alert %}}

---

## Tags HTML suportadas

### Formatação de texto

| Tag | Resultado |
|-----|-----------|
| `<strong>texto</strong>` ou `<b>texto</b>` | **Texto a negrito** |
| `<em>texto</em>` ou `<i>texto</i>` | *Texto em itálico* |
| `<u>texto</u>` | Texto sublinhado |
| `<br>` | Quebra de linha |
| `<span style="...">texto</span>` | Estilo em linha |

### Ligações

```html
<a href="https://example.com" target="_blank">Clique aqui</a>
```

Abre num novo separador. Use para documentos de referência, diretrizes ou recursos externos que o enumerador deve consultar.

### Cores

Use `<span>` com estilos em linha:

```html
<span style="color: red;">Aviso: o valor está fora do intervalo</span>
<span style="color: #009688;">Secção concluída</span>
```

---

## Variáveis de tema de cores

O rtSurvey suporta **tokens de tema de cores** que se adaptam ao tema configurado da aplicação. Use a sintaxe `__COLOR_THEME_NAME__`:

```html
<span style="color: var(--color-theme-primary);">Texto em cor primária</span>
```

Ou usando o atalho de token no texto da etiqueta:

```
<font color="var(--COLOR_THEME_PRIMARY)">Nota importante</font>
```

Isto é automaticamente convertido para o `<span>` equivalente com uma variável CSS no momento da renderização.

---

## Etiquetas com múltiplos idiomas

Envolva o conteúdo em tags de idioma para suportar múltiplos idiomas numa única célula de etiqueta:

```
<en>Enter the household size</en><vi>Nhập quy mô hộ gia đình</vi>
```

O rtSurvey extrai o conteúdo correspondente ao idioma atual da aplicação. Se não for encontrada nenhuma tag de idioma correspondente, a cadeia completa é mostrada tal como está.

---

## Exemplos em campos de nota

### Instrução de secção com negrito e quebra de linha

| type | name | label |
|------|------|-------|
| note | section_intro | `<strong>Secção 3: Uso da Terra</strong><br>Faça todas as perguntas nesta secção apenas ao chefe do agregado familiar.` |

### Resumo dinâmico com referência a cálculo

| type | name | label |
|------|------|-------|
| calculate | total | | `${adults} + ${children}` |
| note | summary | `Total de membros do agregado familiar: <strong>${total}</strong><br><span style="color: gray;">Adultos: ${adults} · Crianças: ${children}</span>` |

### Aviso a vermelho

| type | name | label | relevant |
|------|------|-------|----------|
| note | age_warning | `<span style="color: red;"><strong>Aviso:</strong> A idade introduzida (${age}) é invulgarmente alta. Por favor verifique.</span>` | `${age} > 100` |

### Ligação para documento de referência

| type | name | label |
|------|------|-------|
| note | guidelines_link | `Consulte as <a href="https://docs.example.com/guidelines" target="_blank">Diretrizes de Campo</a> antes de iniciar esta secção.` |

---

## Tags HTML especiais do rtSurvey

### `<webbox src='url' title='title'>...</webbox>`

Incorpora um botão que abre um URL num modal dentro do formulário. Consulte [Webbox](webbox) para detalhes completos.

### `<delete-repeat-current>etiqueta</delete-repeat-current>`

Renderiza um botão dentro de um grupo de repetição que elimina a instância de repetição atual quando tocado.

### `<delete-repeat-last>etiqueta</delete-repeat-last>`

Renderiza um botão que elimina a última instância de repetição.

Exemplo de utilização num grupo de repetição:

| type | name | label |
|------|------|-------|
| note | delete_btn | `<delete-repeat-current>Remover este membro</delete-repeat-current>` |

---

## Melhores Práticas

1. Use HTML com moderação — etiquetas excessivamente formatadas são mais difíceis de ler, não mais fáceis.
2. Prefira `<strong>` para negrito e `<em>` para itálico em vez de `<b>` e `<i>` obsoletos.
3. Mantenha o uso de cores significativo — use vermelho para avisos, não para decoração.
4. Teste sempre a renderização HTML tanto na aplicação móvel como no formulário web, pois a renderização pode diferir ligeiramente.
5. Evite tags `<table>` dentro de etiquetas — raramente são renderizadas bem em ecrãs móveis.
6. Não use JavaScript (`<script>`) — será removido ou causará erros.

## Limitações

- HTML complexo (tabelas, formulários, scripts) não é suportado e pode quebrar a renderização.
- Alguns clientes móveis mais antigos podem exibir tags HTML como texto literal — teste em todos os dispositivos alvo.
- As ligações `<a>` abrem num navegador ou WebView — o enumerador sai do formulário, o que pode ser perturbador no móvel.
