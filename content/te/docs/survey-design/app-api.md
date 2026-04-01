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

AppAPI వినియోగదారులకు FormEngine మరియు DMView లో వివిధ పద్ధతులను ఉపయోగించి యాప్ నుండి సిస్టమ్ మెటా డేటా లోడ్ చేయడానికి అనుమతిస్తుంది. యాప్ నుండి నిర్దిష్ట సమాచారం పొందడానికి వివిధ డేటా కీలను యాక్సెస్ చేయడానికి ఇది అనుమతిస్తుంది.

xlsform లో, మీరు `pulldata()` ఫంక్షన్‌ను కింది సింటాక్స్‌తో ఉపయోగించవచ్చు:


{{< alert context="light" text="pulldata('app-api', 'data-key')" />}}

- `'app-api'`: ఈ కీవర్డ్ FormEngine కి App API నుండి డేటా లోడ్ చేయమని తెలియజేస్తుంది.
- `'data-key'`: మీరు App API నుండి లోడ్ చేయాలనుకున్న డేటా యొక్క కీ ఇది.
- డేటా కీ చెల్లుబాటు కాకపోతే లేదా మద్దతు లేకపోతే, లెక్కింపు "n/a" అని తిరిగి ఇస్తుంది.

App-API తో ఉపయోగించగల మద్దతు ఉన్న డేటా కీలు ఇక్కడ ఉన్నాయి:

`osPlatform`: ప్రస్తుత OS పేరు (Android లేదా iOS) మరియు OS వెర్షన్ తిరిగి ఇస్తుంది. వెబ్ ప్లాట్‌ఫారమ్‌లు ఖాళీ విలువ తిరిగి ఇస్తాయి.

`appPlatform`: యాప్ ప్లాట్‌ఫారమ్ పేరు తిరిగి ఇస్తుంది, ఇది `rtSurvey`.

`appVersion`: యాప్ వెర్షన్ పేరు తిరిగి ఇస్తుంది.

`getDisplayWidth`: పరికర స్క్రీన్ వెడల్పు పిక్సెల్‌లలో తిరిగి ఇస్తుంది.

`getDisplayHeight`: పరికర స్క్రీన్ ఎత్తు పిక్సెల్‌లలో తిరిగి ఇస్తుంది.

`getScreenSize`: పరికర స్క్రీన్ పరిమాణం అంగుళాలలో తిరిగి ఇస్తుంది.

`projectCode`: వినియోగదారుడు సైన్ ఇన్ చేస్తున్న సైట్ యొక్క ప్రస్తుత ప్రాజెక్ట్ కోడ్ తిరిగి ఇస్తుంది.

`projectURL`: వినియోగదారుడు సైన్ ఇన్ చేస్తున్న సైట్ యొక్క ప్రస్తుత ప్రాజెక్ట్ URL తిరిగి ఇస్తుంది. డిఫాల్ట్/ఫాల్‌బ్యాక్ విలువ ఖాళీ టెక్స్ట్ ("").

`startingPoint`: ఫారం ప్రారంభించే పాయింట్ యొక్క మార్గం తిరిగి ఇస్తుంది. మరిన్ని వివరాలకు "Form starting point" చూడండి.

`serverTime`: సర్వర్‌లో తేది మరియు సమయం యొక్క ఉత్తమంగా అందుబాటులో ఉన్న అంచనా తిరిగి ఇస్తుంది.

`user.[attribute]`: నిర్దేశించిన attribute కీ ఆధారంగా ప్రస్తుత వినియోగదారు attributes తిరిగి ఇస్తుంది. అందుబాటులో ఉన్న attribute కీలకు "User attributes" పట్టిక చూడండి.

ప్రస్తుత వినియోగదారు సమాచారం పొందడానికి `pulldata()` params లో "user." తో కింది attribute కీలు కలపండి. ఉదాహరణకు, `user.username`, `user.email` మొదలైనవి ఉపయోగించండి.

| Attribute Key        | వివరణ                                 |
|----------------------|---------------------------------------|
| username             | వినియోగదారు యొక్క వినియోగదారుపేరు    |
| name                 | వినియోగదారు యొక్క పూర్తి పేరు        |
| staffCode            | వినియోగదారు యొక్క స్టాఫ్ కోడ్        |
| phone                | వినియోగదారు యొక్క ఫోన్ నంబర్         |
| email                | వినియోగదారు యొక్క ఇమెయిల్ చిరునామా   |
| description          | వినియోగదారు సమాచారంలో వివరణ టెక్స్ట్  |
| organization_id      | వినియోగదారుడు చెందిన సంస్థ ID         |
| organization_name    | వినియోగదారుడు చెందిన సంస్థ పేరు       |
| team_id              | వినియోగదారుడు చెందిన టీమ్ ID          |
| supervisor_id        | వినియోగదారు సూపర్‌వైజర్ యొక్క ID      |
| is_supervisor        | వినియోగదారుడు సూపర్‌వైజర్ అయితే 1, కాకపోతే 0 |

`instancePath`: ప్రస్తుత ఇన్‌స్టెన్స్ ఫోల్డర్ మార్గం తిరిగి ఇస్తుంది.

`appLanguage`: యాప్ సెట్టింగులలో సెట్ చేయబడిన ప్రస్తుత యాప్ భాష తిరిగి ఇస్తుంది (ఉదా. vi, en).

`openArgs.[attribute]`: ActionButton (act_fill_form, act_get_instance) నుండి పాస్ చేయబడిన open-form-argument తిరిగి ఇస్తుంది. డిఫాల్ట్/ఫాల్‌బ్యాక్ విలువ ఖాళీ టెక్స్ట్ ("").

`primaryAppColor`: యాప్ యొక్క ప్రాథమిక రంగు తిరిగి ఇస్తుంది.

---

## వినియోగ ఉదాహరణలు

### గణికుని వినియోగదారు పేరు మరియు సంస్థ నిల్వ చేయడం

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | enumerator_name | | `pulldata('app-api', 'user.name')` |
| calculate | enumerator_org | | `pulldata('app-api', 'user.organization_name')` |
| calculate | enumerator_email | | `pulldata('app-api', 'user.email')` |

ఆడిట్ ప్రయోజనాల కోసం నోట్ లేబుళ్ళలో వీటిని ఉపయోగించండి:
```
note | interviewer_info | Interviewer: ${enumerator_name} (${enumerator_org})
```

### పరికరం మరియు స్క్రీన్ సమాచారం

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | device_platform | | `pulldata('app-api', 'osPlatform')` |
| calculate | app_ver | | `pulldata('app-api', 'appVersion')` |
| calculate | screen_w | | `pulldata('app-api', 'getDisplayWidth')` |

నివారణకు ఉపయోగకరం: ప్రతి సమర్పణకు ఏ పరికర వెర్షన్ ఉపయోగించబడిందో గుర్తించడానికి మీ డేటాతో పాటు `device_platform` మరియు `app_ver` ఎగుమతి చేయండి.

### పరికర సమయం బదులు సర్వర్ సమయం

పరికర గడియారాలు తప్పు కావచ్చు. మరింత నమ్మదగిన టైమ్‌స్టాంప్ కోసం `serverTime` ఉపయోగించండి:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | server_ts | | `pulldata('app-api', 'serverTime')` |

### వినియోగదారు పాత్ర ఆధారంగా షరతులతో కూడిన లాజిక్

సూపర్‌వైజర్‌లకు మాత్రమే సూపర్‌వైజర్ విభాగం చూపించండి:

| type | name | label | relevant |
|------|------|-------|----------|
| calculate | is_supervisor | | `pulldata('app-api', 'user.is_supervisor')` |
| begin_group | supervisor_section | Supervisor review | `${is_supervisor} = '1'` |
| text | supervisor_notes | Supervisor notes | |
| end_group | | | |

### యాక్షన్ బటన్ నుండి arguments పాస్ చేయడం

ఫారం అనుకూల arguments తో `act_fill_form` యాక్షన్ బటన్ నుండి ప్రారంభించబడినప్పుడు:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | passed_hh_id | | `pulldata('app-api', 'openArgs.household_id')` |
| calculate | passed_task | | `pulldata('app-api', 'openArgs.task_code')` |

యాక్షన్ బటన్ సరిపోలే కీలతో arguments పాస్ చేయాలి (ఉదా. `household_id`, `task_code`).

### ప్రాజెక్ట్ సమాచారం ఉపయోగించడం

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | project | | `pulldata('app-api', 'projectCode')` |
| calculate | project_url | | `pulldata('app-api', 'projectURL')` |

---

## గమనికలు

- అన్ని `pulldata('app-api', ...)` కాల్‌లు ఫారం తెరిచినప్పుడు మూల్యాంకనం చేయబడతాయి మరియు సెషన్ సమయంలో డైనమిక్‌గా తిరిగి మూల్యాంకనం చేయబడవు (`serverTime` మరియు `now()` మినహా).
- ఒక కీ మద్దతు లేకపోతే లేదా డేటా అందుబాటులో లేకపోతే, ఫంక్షన్ `'n/a'` తిరిగి ఇస్తుంది (ఖాళీ స్ట్రింగ్ కాదు — `!= ''` బదులు `!= 'n/a'` తో పరీక్షించండి).
- `openArgs` విలువలు ఫారం యాక్షన్ బటన్ నుండి ప్రారంభించబడినప్పుడు మాత్రమే అందుబాటులో ఉంటాయి; లేకపోతే అవి ఖాళీ స్ట్రింగ్ తిరిగి ఇస్తాయి.
