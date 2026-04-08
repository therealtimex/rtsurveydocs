---
title: "అపీరెన్స్"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

rtSurvey లో `appearance` కాలమ్ మీ సర్వేలలో ప్రశ్నల దృశ్య ప్రదర్శన మరియు ప్రవర్తనను అనుకూలీకరించడానికి అనుమతిస్తుంది. ఈ ఫీచర్ వినియోగదారు అనుభవాన్ని మెరుగుపరుస్తుంది మరియు డేటా సేకరణ సామర్థ్యాన్ని గణనీయంగా మెరుగుపరుస్తుంది. rtSurvey స్టాండర్డ్ XLSForm అపీరెన్స్ లక్షణాలకు మద్దతు ఇస్తుంది మరియు వాటిని అదనపు ఎంపికలతో విస్తరిస్తుంది.

## స్టాండర్డ్ XLSForm అపీరెన్స్ లక్షణాలు

rtSurvey కింది స్టాండర్డ్ XLSForm అపీరెన్స్ లక్షణాలకు మద్దతు ఇస్తుంది:

| అపీరెన్స్ లక్షణం | ప్రశ్న రకాలు | వివరణ |
|----------------------|----------------|-------------|
| multiline | text | బహు-రేఖ టెక్స్ట్ బాక్స్ సృష్టిస్తుంది (వెబ్ క్లైంట్‌లకు ఉత్తమం) |
| minimal | select_one, select_multiple | ఎంపికలను డ్రాప్‌డౌన్ మెనూలో ప్రదర్శిస్తుంది |
| quick | select_one | ఎంపిక తర్వాత తదుపరి ప్రశ్నకు స్వయంచాలకంగా వెళ్తుంది (మొబైల్ మాత్రమే) |
| no-calendar | date | క్యాలెండర్ ప్రదర్శనను అణిచివేస్తుంది (మొబైల్ మాత్రమే) |
| month-year | date | నెల మరియు సంవత్సరం ఎంపికను మాత్రమే అనుమతిస్తుంది |
| year | date | సంవత్సరం ఎంపికను మాత్రమే అనుమతిస్తుంది |
| horizontal-compact | select_one, select_multiple | ఎంపికలను క్షితిజ సమాంతరంగా ప్రదర్శిస్తుంది (వెబ్ మాత్రమే) |
| horizontal | select_one, select_multiple | ఎంపికలను కాలమ్‌లలో క్షితిజ సమాంతరంగా ప్రదర్శిస్తుంది (వెబ్ మాత్రమే) |
| likert | select_one | ఎంపికలను Likert స్కేల్‌గా ప్రదర్శిస్తుంది |
| compact | select_one, select_multiple | కనీస ప్యాడింగ్‌తో ఎంపికలు పక్కపక్కన ప్రదర్శిస్తుంది |
| quickcompact | select_one | కాంపాక్ట్ ప్రదర్శనను స్వయంచాలిత-అడ్వాన్స్‌తో కలుపుతుంది (మొబైల్ మాత్రమే) |
| field-list | groups | మొత్తం సమూహాన్ని ఒక స్క్రీన్‌లో ప్రదర్శిస్తుంది (మొబైల్ మాత్రమే) |
| label | select_one, select_multiple | ఇన్‌పుట్‌లు లేకుండా ఎంపిక లేబుళ్ళు చూపిస్తుంది |
| list-nolabel | select_one, select_multiple | లేబుళ్ళు లేకుండా ఇన్‌పుట్‌లు చూపిస్తుంది (`label` తో ఉపయోగించండి) |
| table-list | groups | ప్రశ్నలను పట్టిక ఫార్మాట్‌లో ప్రదర్శిస్తుంది |
| signature | image | సంతకం సేకరణ ప్రారంభిస్తుంది (మొబైల్ మాత్రమే) |
| draw | image | చేత్తో గీయడానికి అనుమతిస్తుంది (మొబైల్ మాత్రమే) |
| map, quick map | select_one, select_one_from_file | మ్యాప్ ఫీచర్‌ల నుండి ఎంపికను ప్రారంభిస్తుంది |

## అపీరెన్స్ ఉపయోగించడంలో ఉత్తమ పద్ధతులు

1. **స్థిరత**: ఏకరీతి రూపుకోసం మీ సర్వే అంతటా అపీరెన్స్ లక్షణాలు స్థిరంగా ఉపయోగించండి.
2. **మొబైల్ vs వెబ్**: వివిధ పరికరాలు మరియు వేదికలలో అపీరెన్స్‌లు ఎలా రెండర్ అవుతాయో పరిగణించండి.
3. **పనితీరు**: ఫారం లోడింగ్‌ను నెమ్మదింపజేయగలిగే అపీరెన్స్ లక్షణాలతో జాగ్రత్తగా ఉండండి.
4. **వినియోగదారు అనుభవం**: ప్రతిస్పందించే వారికి డేటా ఎంట్రీని సులభంగా మరియు సహజంగా చేసే అపీరెన్స్‌లు ఎంచుకోండి.
5. **పరీక్ష**: అపీరెన్స్‌లు ఆశించిన విధంగా పని చేస్తున్నాయని నిర్ధారించడానికి లక్ష్య పరికరాలలో మీ ఫారాన్ని ఎల్లప్పుడూ పరీక్షించండి.

## rtSurvey విస్తరించిన అపీరెన్స్ లక్షణాలు

స్టాండర్డ్ XLSForm అపీరెన్స్‌లకు అదనంగా, rtSurvey కింది వేదిక-నిర్దిష్ట ఎంపికలకు మద్దతు ఇస్తుంది:

### డేటా మరియు ప్రదర్శన నియంత్రణ

| అపీరెన్స్ లక్షణం | ప్రశ్న రకాలు | వివరణ |
|----------------------|----------------|-------------|
| `invisible` | ఏదైనా | ఫీల్డ్‌ను దృశ్యం నుండి దాచుతుంది, దాని విలువ సేకరించబడుతూ లేదా లెక్కించబడుతూనే ఉంటుంది. `hidden` రకం నుండి భిన్నం — ఫీల్డ్ ఇంకా తర్కంలో పాల్గొంటుంది. |
| `displaytitle` | ఏదైనా | లేకుంటే అణిచివేయబడే ఫీల్డ్ లేబుల్/శీర్షికను బలవంతంగా ప్రదర్శిస్తుంది. |
| `autopull` | select_one, select_multiple | ఫారం లోడ్ అయినప్పుడు లేదా ట్రిగ్గర్ ఫీల్డ్ మారినప్పుడు ఎంపికలు నింపడానికి బాహ్య డేటాను స్వయంచాలకంగా తెస్తుంది. |
| `floating_hint` | text, integer, decimal | హింట్ టెక్స్ట్‌ను దిగువన కాకుండా ఇన్‌పుట్ ఫీల్డ్ పైన వెలుతున్న లేబుల్‌గా చూపిస్తుంది. |
| `calculate-button` | calculate | స్వయంచాలకంగా లెక్కించడం కాకుండా, డిమాండ్‌పై ఫీల్డ్‌ను మళ్ళీ లెక్కించే కనిపించే బటన్‌ను జోడిస్తుంది. |

### Layout

| అపీరెన్స్ లక్షణం | ప్రశ్న రకాలు | వివరణ |
|----------------------|----------------|-------------|
| `1screen` | group | సమూహ పరిమాణంతో సంబంధం లేకుండా మొత్తం సమూహాన్ని ఒకే స్క్రీన్‌లో ప్రదర్శించేలా బలవంతం చేస్తుంది. |
| `columns(n)` | select_one, select_multiple | ఎంపికలను `n` కాలమ్‌లలో ప్రదర్శిస్తుంది. ఉదాహరణ: `columns(3)` మూడు రేడియో బటన్‌ల కాలమ్‌లు చూపిస్తుంది. |
| `gridformat<row=R col=C colspan=S align=center>` | ఏదైనా | CSS-grid layout లో వరుస `R`, కాలమ్ `C` లో `S` కాలమ్‌లు స్పాన్ చేస్తూ ఫీల్డ్‌ను ఉంచుతుంది. `advanced-extension/grid-layout` తో ఉపయోగించబడుతుంది. |
| `ignore-simplify` | ఏదైనా | ఈ ఫీల్డ్ layout యొక్క స్వయంచాలిత సరళీకరణ లేదా కాంపాక్టింగ్‌ను దాటవేయమని ఫారం రెండరర్‌కు సూచిస్తుంది. |
| `required-but-simplify` | ఏదైనా | ఫీల్డ్ అవసరం కానీ దాని layout ఇప్పటికీ renderer సరళీకరిస్తుంది (అవసరమైన ఫీల్డ్‌లు సరళీకరణ నుండి మినహాయించబడే డిఫాల్ట్ ప్రవర్తనను override చేస్తుంది). |
| `embed` | ఏదైనా | ఫీల్డ్‌ను embedded/inline ప్రదర్శన మోడ్‌లో రెండర్ చేస్తుంది, దాని outer wrapper మరియు label container అణిచివేస్తుంది — custom HTML లో nested ప్రశ్న ఉన్నప్పుడు ఉపయోగించబడుతుంది. |
| `popup` | select_one, select_multiple | Choice జాబితాను inline కాకుండా popup/modal overlay లో రెండర్ చేస్తుంది. |
| `auto-hide-empty` | boxtag, select | Choice జాబితా ఖాళీగా ఉన్నప్పుడు (ఉదా. API ఫలితాలు తిరిగి రానప్పుడు) మొత్తం question widget దాచుతుంది. |
| `text-nolabel` | select_one, select_multiple | ప్రతి choice కోసం text label దాచుతుంది, కేవలం input control మాత్రమే చూపిస్తుంది. `list-nolabel` లాంటిది కానీ column split గా కాకుండా per-choice వర్తించబడుతుంది. |

### Widgets

| అపీరెన్స్ లక్షణం | ప్రశ్న రకాలు | వివరణ |
|----------------------|----------------|-------------|
| `likert` | select_one | ఎంపికలను Likert scale వరుసగా ప్రదర్శిస్తుంది (ఇప్పటికే పైన standard table లో ఉంది; మద్దతు ఉందని confirm చేయబడింది). |
| `distress` | select_one | ఎంపికలను Kessler Psychological Distress Scale (K10) visual widget గా emotional icons తో రెండర్ చేస్తుంది. |

### Select visual widgets

ఈ appearances select choice జాబితాల మొత్తం rendering మారుస్తాయి.

| అపీరెన్స్ లక్షణం | ప్రశ్న రకాలు | వివరణ |
|----------------------|----------------|-------------|
| `tagging` | select_one, select_multiple | ఎంపికలు pill-ఆకారపు క్లిక్ చేయగలిగే tag chips గా రెండర్ అవుతాయి. |
| `boxtag` | select_one, select_multiple | ఎంపికలు వినియోగదారు నొక్కే styled rectangular boxes గా రెండర్ అవుతాయి. |
| `boxtag -search` | select_one, select_multiple | Boxes పైన live search/filter input తో boxtag layout. |
| `duolingo-style1` | select_one, select_multiple | Duolingo స్ఫూర్తిపొందిన card layout — icons తో short lists కు అనుకూలం. |
| `rating_box` | select_one, select_multiple | Tappable numbered boxes grid — scale లేదా NPS ప్రశ్నలకు అనుకూలం. |
| `star_rating` | select_one | ఎంపికలు stars గా రెండర్ అవుతాయి; star count choices సంఖ్యకు సమానం. |
| `choices-noshow` | select_one, select_multiple | మొదట్లో కేవలం మొదటి 10 choices "Show more" control తో చూపిస్తుంది. |
| `noshow` | select_one, select_multiple | Choices జాబితాను పూర్తిగా దాచుతుంది; విలువ `calculate` లేదా API ద్వారా programmatically సెట్ చేయబడుతుంది. |
| `checkall` | select_multiple | Choice జాబితా పైభాగంలో "Select all" shortcut జోడిస్తుంది. |
| `max-items(N)` | select_one, select_multiple | Visible choice జాబితాను N items కు పరిమితం చేస్తుంది. ఉదాహరణ: `max-items(5)`. |

### Text visual widgets

| అపీరెన్స్ లక్షణం | ప్రశ్న రకాలు | వివరణ |
|----------------------|----------------|-------------|
| `richtext` | text | Plain text box ని rich text editor తో replace చేస్తుంది (bold, italic, lists, links). HTML నిల్వ చేస్తుంది. |
| `typingtest` | text | Typing test widget — label text passage; widget typed response మరియు timing record చేస్తుంది. |

### Media పొడిగింపులు

| అపీరెన్స్ లక్షణం | ప్రశ్న రకాలు | వివరణ |
|----------------------|----------------|-------------|
| `watermark("expression")` | image | Captured photos పై text watermark overlay చేస్తుంది. Argument capture సమయంలో evaluate చేయబడే XPath expression. ఉదాహరణ: `watermark("${id} ${today()}")`. |
| `editable` | image | Save అవ్వడానికి ముందు captured photo పై annotation/drawing enable చేస్తుంది. |

### Inline display configuration

`display{}` మరియు `results{}` modifiers `inline` appearances కు icon alignment మరియు result display నియంత్రించడానికి append చేయవచ్చు.

#### `display{}` parameters

```
inline display{left}
inline display{right,small}
inline display{top,large,inline-icon}
```

| పారామీటర్ | విలువలు | వివరణ |
|-----------|---------|-------|
| Alignment | `left`, `right`, `top`, `bottom`, `center` | Input field కు relative గా icon position |
| Size | `small`, `medium`, `large` | Icon size (వరుసగా 2.5 rem, 5 rem, 8 rem) |
| Mode | `inline-icon` | Trigger ని icon మాత్రమే గా రెండర్ చేస్తుంది (button border లేకుండా) |
| Mode | `inline-button` | Trigger ని full button గా రెండర్ చేస్తుంది |

#### `results{}` parameters

```
inline results{right}
inline results{left,hide(seconds)}
```

| పారామీటర్ | విలువలు | వివరణ |
|-----------|---------|-------|
| Alignment | `left`, `right`, `top`, `bottom`, `center` | Result value display position |
| `hide(field)` | ఏ sub-field పేరైనా | Result యొక్క నిర్దిష్ట component దాచుతుంది (ఉదా. `hide(seconds)`) |

## తెలిసిన పరిమితులు

- సంక్లిష్ట అపీరెన్స్‌లు అన్ని వేదికలలో ఒకేలా రెండర్ కాకపోవచ్చు.
- కొన్ని అధునాతన rtSurvey అపీరెన్స్‌లు ఆఫ్‌లైన్ మోడ్‌లో మద్దతు ఉండకపోవచ్చు.
