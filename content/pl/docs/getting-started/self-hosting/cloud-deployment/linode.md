---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Wdróż rtCloud na Linode za pomocą StackScript. Nie jest wymagana żadna konfiguracja — po prostu utwórz serwer i postępuj zgodnie z instrukcjami po wdrożeniu."
---

## Krok 1 — Uruchom StackScript

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

This opens the StackScript page in Linode Cloud Manager. Kliknij **Wdróż nowy Linode**.

---

## Krok 2 — Wypełnij formularz Linode

Wypełnij standardowy formularz tworzenia serwera Linode:

| Pole | Recommended value |
|-------|----------------------|
| **Image** | Ubuntu 22.04 LTS |
| **Region** | Closest to your users |
| **Plan** | Wspólny procesor 4 GB lub większy |
| **Hasło roota** | Ustaw silne hasło |
| **Strefa czasowa** *(nasze jedyne pole)* | Twoja strefa czasowa serwera (domyślnie: `Asia/Ho_Chi_Minh`) |

Po zakończeniu kliknij **Utwórz Linode**.

---

## Krok 3 — Poczekaj na zakończenie instalacji

Skrypt uruchamia się automatycznie przy pierwszym uruchomieniu. Instaluje Dockera, pobiera obraz rtSurvey, inicjuje bazę danych i uruchamia wszystkie usługi. Zajmuje to **5–10 minut**.

Możesz śledzić postęp bezpośrednio w **Linode Cloud Manager** — nie jest wymagane SSH:

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Kliknij nowo utworzony Linode
3. Kliknij **Uruchom konsolę LISH** (w prawym górnym rogu strony szczegółów Linode)

Otworzy się terminal przeglądarki pokazujący dziennik rozruchu na żywo — karta **Weblish** działa bezpośrednio w przeglądarce, nie jest potrzebny klient SSH.

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

Poczekaj, aż zobaczysz:

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

Dziennik pokazuje również adres IP Twojego serwera — będziesz go potrzebować w następnym kroku.

---

## Step 4 — Set up SSL

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

Postępuj zgodnie z **[Przewodnikiem konfiguracji SSL →](../ssl-setup)**, aby skonfigurować HTTPS. Bezpłatna subdomena **rtsurvey.com** to najszybsza opcja — nie jest wymagana konfiguracja DNS.

---

## Krok 5 — Pierwsze logowanie

Po włączeniu protokołu SSL postępuj zgodnie z **[Przewodnikiem po pierwszym logowaniu →](../first-login)**, aby uzyskać dostęp do konta administratora.

---

## Krok 6 — Zmień domyślne hasło

Wszystkie hasła domyślnie ustawione są na „admin”. Zmień je natychmiast po pierwszym logowaniu:

- **Hasło administratora aplikacji** — ustawienia konta w aplikacji
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## Reguły zapory sieciowej (zapora sieciowa Linode Cloud)

Jeśli podłączysz zaporę sieciową Linode Cloud do tego serwera, zastosuj następujące zasady:

### Przychodzące

| Etykieta | Akcja | Protokół | Port | Źródła | Notatki |
|-------|--------|----------|------|---------|-------|
| `zaakceptuj-przychodzący-ssh` | Zaakceptuj | TCP | 22 | Wszystkie IPv4, wszystkie IPv6 | Dostęp SSH |
| `zaakceptuj-przychodzący-http` | Zaakceptuj | TCP | 80 | Wszystkie IPv4, wszystkie IPv6 | Nginx (wyzwanie HTTP + ACME) |
| `accept-inbound-https` | Accept | TCP | 443 | All IPv4, All IPv6 | Nginx (HTTPS after SSL setup) |
| `akceptuj-przychodzące-błyszczące` | Zaakceptuj | TCP | 3838 | Wszystkie IPv4, wszystkie IPv6 | Shiny Server (analiza R) |
| `zaakceptuj-przychodzący-icmp` | Zaakceptuj | ICMP | — | Wszystkie IPv4, wszystkie IPv6 | Ping / diagnostyka |
| Domyślna polityka przychodząca | **Upuść** | | | | Zablokuj wszystko inne |

### Wychodzące

| Etykieta | Akcja | Notatki |
|-------|------------|------|
| Domyślna polityka wychodząca | **Zaakceptuj** | Zezwalaj na wszystkie połączenia wychodzące (ściągnięcia Dockera, certbot, GoDaddy API itp.) |

### Porty NIE są potrzebne zewnętrznie

Te porty są powiązane tylko z `127.0.0.1` i nigdy nie są osiągalne spoza serwera:

| Port | Usługa | Powód |
|------|---------|--------|
| 8080 | Kontener aplikacji | Nginx proxy do niego wewnętrznie |
| 8090 | Pojemnik na klucze | Nginx proxy do niego wewnętrznie |
| 3306 | MySQL | Tylko wewnętrzna sieć Docker |

---

## Rozwiązywanie problemów

### Sprawdź dziennik konfiguracji

```bash
tail -200 /var/log/stackscript.log
```

### Sprawdź dziennik SSL

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### Wyświetl status kontenera

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
