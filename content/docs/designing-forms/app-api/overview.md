---
title: "App API overview"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 301
---

The AppAPI allows users to load system meta data from the app using different methods in the FormEngine and DMView. It provides access to various data keys for retrieving specific information from the app.

In the xlsform, you can use the `pulldata()` function with the following syntax:


{{< alert context="light" text="calculate | any_name | pulldata('app-api', 'data-key')" />}}

- `'app-api'`: This keyword informs the FormEngine to load the data from the App API.
- `'data-key'`: This is the key of the data you want to load from the App API.
- If the data key is invalid or not supported, the calculation will return "n/a".

