---
title: "Imagens avançadas"
description: "Recursos avançados de imagem no rtSurvey: marca d'água, exibição em grade de mídia e anotações de imagem."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 300
---

Além do tipo de pergunta `image` padrão, o rtSurvey fornece extensões para **marca d'água** em fotos capturadas e exibição de múltiplas imagens em uma **grade de mídia**. Elas são úteis para pesquisas baseadas em evidências onde as fotos precisam ser marcadas com a identidade do entrevistador ou metadados da pesquisa, e para interfaces de revisão visual.

---

## Marca d'água

O recurso de marca d'água sobrepõe texto ou uma imagem em uma foto capturada antes de ser armazenada. Isso é usado para marcar fotos de campo com a data, nome do entrevistador, localização GPS ou quaisquer outros dados da pesquisa — tornando mais difícil passar fotos pré-existentes como evidências recém-capturadas.

### Configuração

Use `watermark()` na coluna **`calculation`** de um campo `image`, combinado com a aparência `callapi`:

```
watermark(type, size, distance, color, shadow, rotate, blur)
```

| Parâmetro | Descrição |
|-----------|-----------|
| `type` | `'text'` para uma marca d'água de texto; `'file'` para uma marca d'água de imagem |
| `size` | Tamanho da fonte em pixels (texto) ou tamanho da marca d'água como % da largura da imagem (arquivo) |
| `distance` | Espaçamento entre blocos repetidos da marca d'água (pixels) |
| `color` | Cor do texto (cor CSS ou hex). Não usado para o tipo `file` |
| `shadow` | Cor da sombra (cor CSS ou hex) |
| `rotate` | Ângulo de rotação em graus (por exemplo, `45` para diagonal) |
| `blur` | Opacidade da marca d'água (0 = invisível, 100 = totalmente opaco) |

### Exemplo de marca d'água de texto

Sobrepor o nome do entrevistador e a data de hoje diagonalmente em cada foto capturada:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | wm_text | | | `concat(pulldata('app-api', 'user.name'), ' | ', format-date(today(), '%d/%m/%Y'))` |
| image | site_photo | Tire uma foto do local | watermark | `watermark('text', 20, 60, '#ffffff', '#000000', 45, 40)` |

O texto da marca d'água é obtido de `${wm_text}`. Defina o campo de texto da marca d'água **antes** do campo de imagem no formulário.

### Exemplo de marca d'água de imagem/logotipo

Sobrepor o logotipo de uma organização (anexado como arquivo de mídia chamado `logo.png`):

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| image | evidence_photo | Tire foto da evidência | watermark | `watermark('file', 25, 80, '', '#000000', 0, 50)` |

### Desfazer/refazer

O editor de marca d'água suporta desfazer e refazer — os entrevistadores podem retroceder no histórico de edição antes de confirmar a foto.

### Ladrilhamento da marca d'água

A marca d'água se repete (em ladrilhos) por toda a imagem automaticamente. O parâmetro `distance` controla o espaçamento entre os ladrilhos; `rotate` controla o ângulo de cada ladrilho.

---

## Widget de grade de mídia

O widget de grade de mídia exibe uma coleção de arquivos de mídia (imagens, áudio, vídeo) em um layout de grade, permitindo que revisores ou entrevistadores naveguem pelos arquivos capturados visualmente.

Este widget é ativado pela aparência `mediagridwidget` e é tipicamente usado em campos `note` ou `calculate` para exibir mídia capturada anteriormente de um grupo de repetição.

### Exemplo: Mostrar todas as fotos de uma repetição como grade

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | photo_list | | | `join(' ', ${site_photo})` |
| note | photo_review | Revisar fotos capturadas | mediagridwidget | |

---

## Práticas recomendadas para fotos com marca d'água

1. Sempre calcule o texto da marca d'água em um campo `calculate` **acima** do campo de imagem para que esteja disponível quando a foto for tirada.
2. Use um ângulo de rotação (por exemplo, 45°) para dificultar o recorte das marcas d'água.
3. Defina a opacidade (`blur`) entre 30 e 60% — alto o suficiente para ser legível, baixo o suficiente para não obscurecer o assunto da foto.
4. Inclua o nome do entrevistador, data e coordenadas GPS no texto da marca d'água para maximizar o valor de auditoria.
5. Teste a renderização da marca d'água no dispositivo de menor especificação em sua frota — a marca d'água baseada em canvas pode ser lenta em hardware mais antigo.

## Limitações

- A marcação d'água é aplicada no lado do cliente usando a HTML5 Canvas API — requer um navegador ou WebView móvel capaz.
- Fotos de muito alta resolução podem levar vários segundos para marcar em dispositivos de baixo desempenho.
- As marcas d'água são incorporadas ao arquivo de imagem — elas não podem ser removidas após o envio sem edição de imagem.
- O tipo de marca d'água `file` requer que a imagem do logotipo seja anexada como arquivo de mídia com exatamente o nome de arquivo esperado.
