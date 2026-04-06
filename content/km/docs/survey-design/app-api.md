---
title: "App API"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 300
---

AppAPI អនុញ្ញាតឱ្យ users load system metadata ពី app ក្នុង FormEngine ។

ក្នុង xlsform, ប្រើ `pulldata()` function ជ ា ម ួ យ syntax ខ ាង ក ្ រ ោ ម :

{{< alert context="light" text="pulldata('app-api', 'data-key')" />}}

- `'app-api'`: keyword ណ ែ ន ា ំ FormEngine ឱ ្ យ load data ពី App API ។
- `'data-key'`: key ន ៃ data ។
- ប ្ រ ស ិ ន ប ើ data key invalid, calculation return "n/a" ។

## Data Keys ដែល គាំទ្រ

`osPlatform`: Returns OS name (Android ឬ iOS) ។

`appVersion`: Returns version name ។

`projectCode`: Returns project code ។

`serverTime`: Returns server date and time ។

`user.[attribute]`: Returns user attributes ។

| Attribute Key        | ការពិពណ៌នា                          |
|----------------------|--------------------------------------|
| username             | Username                              |
| name                 | Full name                             |
| staffCode            | Staff code                            |
| phone                | Phone number                          |
| email                | Email address                         |
| organization_id      | Organization ID                       |
| organization_name    | Organization name                     |
| is_supervisor        | 1 ប ្ រ ស ិ ន ប ើ supervisor, 0 ប ្ រ ស ិ ន ប ើ ម ិ ន ម ែ ន |

## Usage Examples

### Store enumerator's username

```
| type      | name           | label | calculation                          |
|-----------|----------------|-------|--------------------------------------|
| calculate | enumerator_name|       | pulldata('app-api', 'user.name')      |
| calculate | enumerator_org |       | pulldata('app-api', 'user.organization_name') |
```

### Server time

```
| type      | name      | label | calculation                       |
|-----------|-----------|-------|-----------------------------------|
| calculate | server_ts |       | pulldata('app-api', 'serverTime') |
```

### Conditional logic based on user role

```
| type      | name          | label | relevant                    |
|-----------|---------------|-------|-----------------------------|
| calculate | is_supervisor |       | pulldata('app-api', 'user.is_supervisor') |
| begin_group | supervisor_section | Supervisor review | ${is_supervisor} = '1' |
| text      | supervisor_notes | Supervisor notes | |
| end_group |               |       |                             |
```

## Notes

- calls `pulldata('app-api', ...)` ទ ាំ ង អ ស ់ ត ្ រ ូ វ ប ា ន evaluate ន ៅ ព េ ល form ត ្ រ ូ វ ប ា ន បើ ក ។
- ប ្ រ ស ិ ន ប ើ key unsupported, function return `'n/a'` ។
