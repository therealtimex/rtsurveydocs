---
title: "Select_multiple"
description: "Питання select_multiple дозволяють респондентам вибирати один або більше варіантів із заздалегідь визначеного списку."
icon: "check_box"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 225
---

Тип питання `select_multiple` відображає список, де респондент може вибрати **один або більше варіантів**. За замовчуванням варіанти відображаються як прапорці. Збережене значення — це **список обраних значень варіантів, розділений пробілами**.

## Базова специфікація XLSForm

**Таблиця survey:**

| type | name | label |
|------|------|-------|
| select_multiple crops | crops_grown | Which crops does the household grow? |

**Таблиця choices:**

| list_name | name | label |
|-----------|------|-------|
| crops | maize | Maize |
| crops | beans | Beans |
| crops | rice | Rice |
| crops | vegetables | Vegetables |
| crops | other | Other |

Для отримання додаткових відомостей дивіться [специфікацію XLSForm](https://xlsform.org/en/#question-types).

## Формат збережених даних

Експортований стовпець містить список обраних значень, розділений пробілами:

```
maize beans vegetables
```

Використовуйте функцію `selected()` — а не `=` — при перевірці значень select_multiple у виразах (дивіться нижче).

## Використання

Питання select_multiple використовуються для:

1. Збору кількох застосовних відповідей (наприклад, джерела доходу, вирощувані культури, симптоми)
2. Елементів погодження у вигляді прапорців (наприклад, "Виберіть всі, що застосовуються")
3. Інвентарів мов або навичок
4. Будь-якого питання, де одночасно дійсні кілька відповідей

## Параметри appearance

{{< table >}}
| Appearance | Опис |
|------------|-------------|
| *(none)* | Прапорці за замовчуванням, по одному на рядок |
| `minimal` | Віджет мульти-вибору випадаючого списку |
| `compact` | Компактна сітка, стовпці адаптуються до ширини екрана |
| `compact-N` | Компактна сітка, примусово N стовпців |
| `horizontal` | Варіанти розташовані горизонтально в рядок (веб) |
| `horizontal-compact` | Горизонтальне, компактне розташування (веб) |
| `label` | Показує лише мітки, без прапорців (використовується з `list-nolabel`) |
| `list-nolabel` | Показує лише прапорці, без міток (використовується з `label`) |
| `columns(N)` | Відображення в N стовпцях (розширення rtSurvey) |
{{< /table >}}

### Приклад: Компактний макет у 3 стовпці

| type | name | label | appearance |
|------|------|-------|------------|
| select_multiple symptoms | symptoms | Select all symptoms observed | compact-3 |

## Використання `selected()` у виразах

Оскільки збережене значення — це рядок, розділений пробілами, ви **повинні** використовувати `selected()` для перевірки, чи був обраний конкретний варіант. Використання `=` не працюватиме правильно.

### У `relevant`

Показати подальше питання лише якщо обрано "other":

| type | name | label | relevant |
|------|------|-------|----------|
| select_multiple crops | crops_grown | Which crops are grown? | |
| text | crops_other | Please specify other crops | `selected(${crops_grown}, 'other')` |

### У `constraint`

Вимагати щонайменше 2 варіанти:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple issues | issues | `count-selected(.) >= 2` | Select at least 2 issues |

Обмежити до максимум 3:

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple priorities | priorities | `count-selected(.) <= 3` | Select no more than 3 priorities |

### У `calculate` — об'єднання обраних міток

Об'єднайте `selected-at()`, `count-selected()` та `choice-label()` для побудови читабельного зведення:

| type | name | calculation |
|------|------|-------------|
| calculate | crops_summary | join(', ', ${crops_grown}) |

## Варіант "Жоден з перерахованих" / виключний варіант

Поширений шаблон — зробити один варіант взаємовиключним з усіма іншими. Використовуйте `constraint` для забезпечення цього:

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| select_multiple issues | issues | Select all issues present | `not(selected(., 'none') and count-selected(.) > 1)` | "None" cannot be selected with other options |

**Таблиця choices:**

| list_name | name | label |
|-----------|------|-------|
| issues | water | Water shortage |
| issues | roads | Poor roads |
| issues | health | Lack of health services |
| issues | none | None of the above |

## Підрахунок та зведення виборів

| Функція | Приклад | Результат |
|----------|---------|--------|
| `count-selected(field)` | `count-selected(${crops_grown})` | Кількість обраних варіантів |
| `selected(field, value)` | `selected(${crops_grown}, 'maize')` | true/false |
| `selected-at(field, index)` | `selected-at(${crops_grown}, 0)` | Перше обране значення |
| `choice-label(field, value)` | `choice-label(${crops_grown}, 'maize')` | Мітка для значення |

## Найкращі практики

1. Завжди використовуйте `selected()` в `relevant`, `constraint` та `calculate` — ніколи `=` або `!=`.
2. Додайте обмеження для обмеження максимальної кількості виборів, якщо дизайн питання вимагає цього.
3. Включайте варіант "Жоден" або "Не застосовується", коли нульова кількість виборів є дійсною відповіддю.
4. Для довгих списків (15+ варіантів) використовуйте `minimal` (мульти-вибір випадаючого списку) для уникнення надмірного прокручування.
5. Експортуйте дані та використовуйте розбиття рядків у вашому інструменті аналізу — формат, розділений пробілами, вимагає розбиття перед зведенням.

## Обмеження

- Значення select_multiple не можна безпосередньо порівнювати з `=`. Завжди використовуйте `selected()`.
- Appearance compact може відображатися не дуже добре для дуже довгих міток варіантів.
- При фільтрації варіантів за допомогою `choice_filter`, фільтрація застосовується до всіх відображуваних варіантів, так само як у `select_one`.
