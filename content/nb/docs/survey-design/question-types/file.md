---
title: "Fil"
description: "Filspørsmål lar respondenter laste opp dokumenter og andre filer som en del av spørreundersøkelsessvaret."
icon: "upload_file"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 230
---

`file`-spørsmålstypen lar respondenter **laste opp en hvilken som helst fil** fra enheten sin — dokumenter, regneark, PDF-er eller andre filtyper. I motsetning til `image`, `audio` og `video` som starter spesifikke opptaksverktøy, åpner `file` en generell filvelger.

## Grunnleggende XLSForm-spesifikasjon

| type | name      | label                        |
|------|-----------|------------------------------|
| file | document  | Vennligst last opp dokumentet ditt |

## Brukstilfeller

Filspørsmål brukes vanligvis for:

1. Samle inn støttedokumenter (kvitteringer, sertifikater, kontrakter, rapporter)
2. Laste opp fullførte papirskjemaer som ble skannet
3. Samle inn regneark eller dataeksporter fra andre systemer
4. Enhver digital filtype som bilde/lyd/video ikke dekker

## Dataformat

Opplastede filer lagres som binære vedlegg:

- **Format:** Bevart i originalformat (PDF, XLSX, DOCX, osv.)
- **Navngivning:** `{instanceID}-{feltnavn}.{endelse}`
- **Lagring:** Lastet opp til servermediamappen ved siden av innsendingen
- **Tilgang:** Nedlastbar fra innsendingsstyringsgrensesnittet

## rtSurvey-utvidelser

### Aksepterte filtyper

Bruk `parameters`-kolonnen for å begrense hvilke filtyper som kan velges:

| type | name | label | parameters |
|------|------|-------|------------|
| file | report | Last opp inspeksjonsrapporten | `accept=.pdf` |
| file | spreadsheet | Last opp datafilen | `accept=.xlsx,.csv` |

`accept`-parameteren bruker standard filendelsessyntaks (kommaseparert).

### Integrasjon med enhetens filsystem og skylagring

På Android og iOS åpner `file`-spørsmålet enhetens native filvelger, som kan inkludere tilgang til:
- Lokal enhetslagring
- SD-kort (Android)
- iCloud Drive (iOS)
- Google Drive, Dropbox (hvis installert)

På web åpner det nettleserens standard filopplastingsdialog.

## Eksempelbruk

### Nødvendig PDF-opplasting

| type | name | label | hint | required | required_message |
|------|------|-------|------|----------|-----------------|
| file | signed_consent | Last opp det signerte samtykkeskjemaet | Kun PDF, maks 2MB | yes | Et samtykkeskjema er nødvendig |

### Betinget dokumentopplasting

| type | name | label | relevant |
|------|------|-------|----------|
| select_one yesno | has_land_title | Har husholdningen et landtitteldokument? | |
| file | land_title_doc | Last opp et bilde eller skanning av landtittelen | `${has_land_title} = 'yes'` |

## Beste praksis

1. Bruk `accept` for å begrense filtyper — dette forhindrer tellere fra å laste opp feil filer ved et uhell.
2. Inkluder alltid størrelses- og formatveiledning i `hint`-kolonnen.
3. For bilder, bruk `image`-typen i stedet — den gir bedre komprimering og konsekvent formatering.
4. For store undersøkelser med filvedlegg, planlegg datalagring og nedlastningsbåndbredde deretter.
5. Test filvelgeren på målenhetstypen (Android vs. iOS vs. web) før distribusjon — tilgang til skylager varierer.

## Begrensninger

- Filspørsmål validerer ikke filinnhold — bare filendelseskontrollen via `accept` håndheves på UI-nivå.
- Svært store filer (100 MB+) kan tidsavbrytes ved opplasting i lavkoblingsmiljøer.
- Frakoblede tellere kan vedlegge filer, men de lastes ikke opp før tilkobling er gjenopprettet.
- Noen enhetskonfigurasjoner begrenser tilgang til visse lagringsplasseringer (f.eks. bedriftens MDM-policyer).
