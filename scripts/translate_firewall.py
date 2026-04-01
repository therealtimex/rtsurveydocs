#!/usr/bin/env python3
"""Replace English firewall section with translated version in all 35 language linode.md files."""
import os, re

CONTENT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content")

EN_ANCHOR_START = "## Firewall rules (Linode Cloud Firewall)"
EN_ANCHOR_END   = "## Troubleshooting"

# Translated firewall sections per language.
# Format: heading + body. Code blocks and port labels stay in English.
SECTIONS = {
"vi": """## Quy tắc tường lửa (Linode Cloud Firewall)

Nếu bạn gắn Linode Cloud Firewall vào máy chủ này, hãy sử dụng các quy tắc sau:

### Inbound (Lưu lượng vào)

| Nhãn | Hành động | Giao thức | Cổng | Nguồn | Ghi chú |
|------|----------|----------|------|-------|---------|
| `accept-inbound-ssh` | Chấp nhận | TCP | 22 | All IPv4, All IPv6 | Truy cập SSH |
| `accept-inbound-http` | Chấp nhận | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + ACME challenge) |
| `accept-inbound-https` | Chấp nhận | TCP | 443 | All IPv4, All IPv6 | Nginx (HTTPS sau khi cài SSL) |
| `accept-inbound-shiny` | Chấp nhận | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (R analytics) |
| `accept-inbound-icmp` | Chấp nhận | ICMP | — | All IPv4, All IPv6 | Ping / chẩn đoán |
| Chính sách inbound mặc định | **Chặn** | | | | Chặn tất cả còn lại |

### Outbound (Lưu lượng ra)

| Nhãn | Hành động | Ghi chú |
|------|----------|---------|
| Chính sách outbound mặc định | **Chấp nhận** | Cho phép tất cả lưu lượng ra (Docker, certbot, GoDaddy API, v.v.) |

### Các cổng KHÔNG cần mở ra ngoài

Các cổng này chỉ được gắn với `127.0.0.1` và không thể truy cập từ bên ngoài:

| Cổng | Dịch vụ | Lý do |
|------|---------|-------|
| 8080 | App container | Nginx proxy nội bộ |
| 8090 | Keycloak container | Nginx proxy nội bộ |
| 3306 | MySQL | Chỉ trong mạng Docker nội bộ |""",

"fr": """## Règles de pare-feu (Linode Cloud Firewall)

Si vous associez un Linode Cloud Firewall à ce serveur, utilisez les règles suivantes :

### Trafic entrant (Inbound)

| Libellé | Action | Protocole | Port | Sources | Notes |
|---------|--------|-----------|------|---------|-------|
| `accept-inbound-ssh` | Accepter | TCP | 22 | All IPv4, All IPv6 | Accès SSH |
| `accept-inbound-http` | Accepter | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + challenge ACME) |
| `accept-inbound-https` | Accepter | TCP | 443 | All IPv4, All IPv6 | Nginx (HTTPS après configuration SSL) |
| `accept-inbound-shiny` | Accepter | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (analytics R) |
| `accept-inbound-icmp` | Accepter | ICMP | — | All IPv4, All IPv6 | Ping / diagnostics |
| Politique entrante par défaut | **Bloquer** | | | | Bloquer tout le reste |

### Trafic sortant (Outbound)

| Libellé | Action | Notes |
|---------|--------|-------|
| Politique sortante par défaut | **Accepter** | Autoriser tout le trafic sortant (Docker, certbot, API GoDaddy, etc.) |

### Ports NON requis en externe

Ces ports sont liés à `127.0.0.1` uniquement et ne sont jamais accessibles de l'extérieur :

| Port | Service | Raison |
|------|---------|--------|
| 8080 | Conteneur applicatif | Nginx fait le proxy en interne |
| 8090 | Conteneur Keycloak | Nginx fait le proxy en interne |
| 3306 | MySQL | Réseau Docker interne uniquement |""",

"de": """## Firewall-Regeln (Linode Cloud Firewall)

Wenn Sie eine Linode Cloud Firewall an diesen Server anhängen, verwenden Sie die folgenden Regeln:

### Eingehend (Inbound)

| Bezeichnung | Aktion | Protokoll | Port | Quellen | Hinweise |
|------------|--------|-----------|------|---------|---------|
| `accept-inbound-ssh` | Akzeptieren | TCP | 22 | All IPv4, All IPv6 | SSH-Zugriff |
| `accept-inbound-http` | Akzeptieren | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + ACME-Challenge) |
| `accept-inbound-https` | Akzeptieren | TCP | 443 | All IPv4, All IPv6 | Nginx (HTTPS nach SSL-Einrichtung) |
| `accept-inbound-shiny` | Akzeptieren | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (R-Analyse) |
| `accept-inbound-icmp` | Akzeptieren | ICMP | — | All IPv4, All IPv6 | Ping / Diagnose |
| Standard-Eingangsrichtlinie | **Verwerfen** | | | | Alles andere blockieren |

### Ausgehend (Outbound)

| Bezeichnung | Aktion | Hinweise |
|------------|--------|---------|
| Standard-Ausgangsrichtlinie | **Akzeptieren** | Alle ausgehenden Verbindungen erlauben (Docker, certbot, GoDaddy API usw.) |

### Ports, die extern NICHT benötigt werden

Diese Ports sind nur an `127.0.0.1` gebunden und von außen nicht erreichbar:

| Port | Dienst | Grund |
|------|--------|-------|
| 8080 | App-Container | Nginx leitet intern weiter |
| 8090 | Keycloak-Container | Nginx leitet intern weiter |
| 3306 | MySQL | Nur internes Docker-Netzwerk |""",

"es": """## Reglas de firewall (Linode Cloud Firewall)

Si adjunta un Linode Cloud Firewall a este servidor, utilice las siguientes reglas:

### Tráfico entrante (Inbound)

| Etiqueta | Acción | Protocolo | Puerto | Fuentes | Notas |
|---------|--------|-----------|--------|---------|-------|
| `accept-inbound-ssh` | Aceptar | TCP | 22 | All IPv4, All IPv6 | Acceso SSH |
| `accept-inbound-http` | Aceptar | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + desafío ACME) |
| `accept-inbound-https` | Aceptar | TCP | 443 | All IPv4, All IPv6 | Nginx (HTTPS tras configurar SSL) |
| `accept-inbound-shiny` | Aceptar | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (análisis R) |
| `accept-inbound-icmp` | Aceptar | ICMP | — | All IPv4, All IPv6 | Ping / diagnóstico |
| Política entrante predeterminada | **Bloquear** | | | | Bloquear todo lo demás |

### Tráfico saliente (Outbound)

| Etiqueta | Acción | Notas |
|---------|--------|-------|
| Política saliente predeterminada | **Aceptar** | Permitir todo el tráfico saliente (Docker, certbot, API GoDaddy, etc.) |

### Puertos NO necesarios externamente

Estos puertos solo están vinculados a `127.0.0.1` y nunca son accesibles desde el exterior:

| Puerto | Servicio | Motivo |
|--------|---------|--------|
| 8080 | Contenedor de la app | Nginx hace proxy internamente |
| 8090 | Contenedor Keycloak | Nginx hace proxy internamente |
| 3306 | MySQL | Solo red Docker interna |""",

"pt": """## Regras de firewall (Linode Cloud Firewall)

Se associar um Linode Cloud Firewall a este servidor, utilize as seguintes regras:

### Tráfego de entrada (Inbound)

| Etiqueta | Ação | Protocolo | Porta | Fontes | Notas |
|---------|------|-----------|-------|--------|-------|
| `accept-inbound-ssh` | Aceitar | TCP | 22 | All IPv4, All IPv6 | Acesso SSH |
| `accept-inbound-http` | Aceitar | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + desafio ACME) |
| `accept-inbound-https` | Aceitar | TCP | 443 | All IPv4, All IPv6 | Nginx (HTTPS após configurar SSL) |
| `accept-inbound-shiny` | Aceitar | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (análise R) |
| `accept-inbound-icmp` | Aceitar | ICMP | — | All IPv4, All IPv6 | Ping / diagnóstico |
| Política de entrada predefinida | **Bloquear** | | | | Bloquear tudo o resto |

### Tráfego de saída (Outbound)

| Etiqueta | Ação | Notas |
|---------|------|-------|
| Política de saída predefinida | **Aceitar** | Permitir todo o tráfego de saída (Docker, certbot, API GoDaddy, etc.) |

### Portas NÃO necessárias externamente

Estas portas estão ligadas apenas a `127.0.0.1` e nunca são acessíveis do exterior:

| Porta | Serviço | Motivo |
|-------|---------|--------|
| 8080 | Contentor da app | Nginx faz proxy internamente |
| 8090 | Contentor Keycloak | Nginx faz proxy internamente |
| 3306 | MySQL | Apenas rede Docker interna |""",

"pt-br": """## Regras de firewall (Linode Cloud Firewall)

Se você anexar um Linode Cloud Firewall a este servidor, use as seguintes regras:

### Tráfego de entrada (Inbound)

| Rótulo | Ação | Protocolo | Porta | Fontes | Notas |
|--------|------|-----------|-------|--------|-------|
| `accept-inbound-ssh` | Aceitar | TCP | 22 | All IPv4, All IPv6 | Acesso SSH |
| `accept-inbound-http` | Aceitar | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + desafio ACME) |
| `accept-inbound-https` | Aceitar | TCP | 443 | All IPv4, All IPv6 | Nginx (HTTPS após configurar SSL) |
| `accept-inbound-shiny` | Aceitar | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (análise R) |
| `accept-inbound-icmp` | Aceitar | ICMP | — | All IPv4, All IPv6 | Ping / diagnóstico |
| Política de entrada padrão | **Bloquear** | | | | Bloquear todo o resto |

### Tráfego de saída (Outbound)

| Rótulo | Ação | Notas |
|--------|------|-------|
| Política de saída padrão | **Aceitar** | Permitir todo o tráfego de saída (Docker, certbot, API GoDaddy, etc.) |

### Portas NÃO necessárias externamente

Estas portas estão vinculadas apenas a `127.0.0.1` e nunca são acessíveis externamente:

| Porta | Serviço | Motivo |
|-------|---------|--------|
| 8080 | Container da app | Nginx faz proxy internamente |
| 8090 | Container Keycloak | Nginx faz proxy internamente |
| 3306 | MySQL | Apenas rede Docker interna |""",

"it": """## Regole firewall (Linode Cloud Firewall)

Se si collega un Linode Cloud Firewall a questo server, utilizzare le seguenti regole:

### Traffico in entrata (Inbound)

| Etichetta | Azione | Protocollo | Porta | Sorgenti | Note |
|---------|--------|-----------|------|---------|------|
| `accept-inbound-ssh` | Accetta | TCP | 22 | All IPv4, All IPv6 | Accesso SSH |
| `accept-inbound-http` | Accetta | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + challenge ACME) |
| `accept-inbound-https` | Accetta | TCP | 443 | All IPv4, All IPv6 | Nginx (HTTPS dopo la configurazione SSL) |
| `accept-inbound-shiny` | Accetta | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (analisi R) |
| `accept-inbound-icmp` | Accetta | ICMP | — | All IPv4, All IPv6 | Ping / diagnostica |
| Criterio in entrata predefinito | **Rifiuta** | | | | Blocca tutto il resto |

### Traffico in uscita (Outbound)

| Etichetta | Azione | Note |
|---------|--------|------|
| Criterio in uscita predefinito | **Accetta** | Consenti tutto il traffico in uscita (Docker, certbot, API GoDaddy, ecc.) |

### Porte NON necessarie esternamente

Queste porte sono associate solo a `127.0.0.1` e non sono mai raggiungibili dall'esterno:

| Porta | Servizio | Motivo |
|-------|---------|--------|
| 8080 | Container app | Nginx fa il proxy internamente |
| 8090 | Container Keycloak | Nginx fa il proxy internamente |
| 3306 | MySQL | Solo rete Docker interna |""",

"nl": """## Firewallregels (Linode Cloud Firewall)

Als u een Linode Cloud Firewall aan deze server koppelt, gebruik dan de volgende regels:

### Inkomend verkeer (Inbound)

| Label | Actie | Protocol | Poort | Bronnen | Opmerkingen |
|-------|-------|---------|------|---------|------------|
| `accept-inbound-ssh` | Accepteren | TCP | 22 | All IPv4, All IPv6 | SSH-toegang |
| `accept-inbound-http` | Accepteren | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + ACME-challenge) |
| `accept-inbound-https` | Accepteren | TCP | 443 | All IPv4, All IPv6 | Nginx (HTTPS na SSL-instelling) |
| `accept-inbound-shiny` | Accepteren | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (R-analyse) |
| `accept-inbound-icmp` | Accepteren | ICMP | — | All IPv4, All IPv6 | Ping / diagnose |
| Standaard inkomend beleid | **Weigeren** | | | | Al het overige blokkeren |

### Uitgaand verkeer (Outbound)

| Label | Actie | Opmerkingen |
|-------|-------|------------|
| Standaard uitgaand beleid | **Accepteren** | Al het uitgaande verkeer toestaan (Docker, certbot, GoDaddy API, enz.) |

### Poorten die NIET extern nodig zijn

Deze poorten zijn alleen gebonden aan `127.0.0.1` en zijn nooit bereikbaar van buitenaf:

| Poort | Dienst | Reden |
|-------|--------|-------|
| 8080 | App-container | Nginx doet intern proxy |
| 8090 | Keycloak-container | Nginx doet intern proxy |
| 3306 | MySQL | Alleen intern Docker-netwerk |""",

"ja": """## ファイアウォールルール (Linode Cloud Firewall)

このサーバーにLinode Cloud Firewallを適用する場合は、以下のルールを使用してください：

### インバウンド (受信)

| ラベル | アクション | プロトコル | ポート | ソース | 備考 |
|-------|----------|----------|------|-------|------|
| `accept-inbound-ssh` | 許可 | TCP | 22 | All IPv4, All IPv6 | SSHアクセス |
| `accept-inbound-http` | 許可 | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + ACMEチャレンジ) |
| `accept-inbound-https` | 許可 | TCP | 443 | All IPv4, All IPv6 | Nginx (SSL設定後のHTTPS) |
| `accept-inbound-shiny` | 許可 | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (R分析) |
| `accept-inbound-icmp` | 許可 | ICMP | — | All IPv4, All IPv6 | Ping / 診断 |
| デフォルトインバウンドポリシー | **拒否** | | | | それ以外をすべてブロック |

### アウトバウンド (送信)

| ラベル | アクション | 備考 |
|-------|----------|------|
| デフォルトアウトバウンドポリシー | **許可** | すべての送信トラフィックを許可 (Docker、certbot、GoDaddy API 等) |

### 外部に開放不要なポート

これらのポートは `127.0.0.1` のみにバインドされており、外部からアクセスできません：

| ポート | サービス | 理由 |
|------|--------|------|
| 8080 | アプリコンテナ | Nginxが内部でプロキシ |
| 8090 | Keycloakコンテナ | Nginxが内部でプロキシ |
| 3306 | MySQL | Dockerの内部ネットワークのみ |""",

"zh-hans": """## 防火墙规则（Linode Cloud Firewall）

如果您将 Linode Cloud Firewall 附加到此服务器，请使用以下规则：

### 入站规则（Inbound）

| 标签 | 操作 | 协议 | 端口 | 来源 | 备注 |
|------|------|------|------|------|------|
| `accept-inbound-ssh` | 接受 | TCP | 22 | All IPv4, All IPv6 | SSH 访问 |
| `accept-inbound-http` | 接受 | TCP | 80 | All IPv4, All IPv6 | Nginx（HTTP + ACME 验证） |
| `accept-inbound-https` | 接受 | TCP | 443 | All IPv4, All IPv6 | Nginx（SSL 配置后的 HTTPS） |
| `accept-inbound-shiny` | 接受 | TCP | 3838 | All IPv4, All IPv6 | Shiny Server（R 分析） |
| `accept-inbound-icmp` | 接受 | ICMP | — | All IPv4, All IPv6 | Ping / 诊断 |
| 默认入站策略 | **丢弃** | | | | 阻止其他所有流量 |

### 出站规则（Outbound）

| 标签 | 操作 | 备注 |
|------|------|------|
| 默认出站策略 | **接受** | 允许所有出站流量（Docker、certbot、GoDaddy API 等） |

### 无需对外开放的端口

这些端口仅绑定到 `127.0.0.1`，无法从外部访问：

| 端口 | 服务 | 原因 |
|------|------|------|
| 8080 | 应用容器 | Nginx 在内部代理 |
| 8090 | Keycloak 容器 | Nginx 在内部代理 |
| 3306 | MySQL | 仅限 Docker 内部网络 |""",

"zh-hant": """## 防火牆規則（Linode Cloud Firewall）

如果您將 Linode Cloud Firewall 附加到此伺服器，請使用以下規則：

### 入站規則（Inbound）

| 標籤 | 操作 | 協定 | 連接埠 | 來源 | 備註 |
|------|------|------|--------|------|------|
| `accept-inbound-ssh` | 接受 | TCP | 22 | All IPv4, All IPv6 | SSH 存取 |
| `accept-inbound-http` | 接受 | TCP | 80 | All IPv4, All IPv6 | Nginx（HTTP + ACME 驗證） |
| `accept-inbound-https` | 接受 | TCP | 443 | All IPv4, All IPv6 | Nginx（SSL 設定後的 HTTPS） |
| `accept-inbound-shiny` | 接受 | TCP | 3838 | All IPv4, All IPv6 | Shiny Server（R 分析） |
| `accept-inbound-icmp` | 接受 | ICMP | — | All IPv4, All IPv6 | Ping / 診斷 |
| 預設入站原則 | **捨棄** | | | | 封鎖其他所有流量 |

### 出站規則（Outbound）

| 標籤 | 操作 | 備註 |
|------|------|------|
| 預設出站原則 | **接受** | 允許所有出站流量（Docker、certbot、GoDaddy API 等） |

### 無需對外開放的連接埠

這些連接埠僅綁定到 `127.0.0.1`，無法從外部存取：

| 連接埠 | 服務 | 原因 |
|--------|------|------|
| 8080 | 應用容器 | Nginx 在內部代理 |
| 8090 | Keycloak 容器 | Nginx 在內部代理 |
| 3306 | MySQL | 僅限 Docker 內部網路 |""",

"ko": """## 방화벽 규칙 (Linode Cloud Firewall)

이 서버에 Linode Cloud Firewall을 연결하는 경우 다음 규칙을 사용하세요:

### 인바운드 (수신)

| 레이블 | 작업 | 프로토콜 | 포트 | 소스 | 비고 |
|-------|------|---------|------|------|------|
| `accept-inbound-ssh` | 허용 | TCP | 22 | All IPv4, All IPv6 | SSH 접근 |
| `accept-inbound-http` | 허용 | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + ACME 챌린지) |
| `accept-inbound-https` | 허용 | TCP | 443 | All IPv4, All IPv6 | Nginx (SSL 설정 후 HTTPS) |
| `accept-inbound-shiny` | 허용 | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (R 분석) |
| `accept-inbound-icmp` | 허용 | ICMP | — | All IPv4, All IPv6 | Ping / 진단 |
| 기본 인바운드 정책 | **차단** | | | | 나머지 모두 차단 |

### 아웃바운드 (송신)

| 레이블 | 작업 | 비고 |
|-------|------|------|
| 기본 아웃바운드 정책 | **허용** | 모든 아웃바운드 트래픽 허용 (Docker, certbot, GoDaddy API 등) |

### 외부에 불필요한 포트

이 포트들은 `127.0.0.1`에만 바인딩되어 외부에서 접근할 수 없습니다:

| 포트 | 서비스 | 이유 |
|------|--------|------|
| 8080 | 앱 컨테이너 | Nginx가 내부에서 프록시 |
| 8090 | Keycloak 컨테이너 | Nginx가 내부에서 프록시 |
| 3306 | MySQL | Docker 내부 네트워크 전용 |""",

"ar": """## قواعد جدار الحماية (Linode Cloud Firewall)

إذا قمت بربط Linode Cloud Firewall بهذا الخادم، استخدم القواعد التالية:

### حركة المرور الواردة (Inbound)

| التسمية | الإجراء | البروتوكول | المنفذ | المصادر | ملاحظات |
|---------|--------|-----------|-------|---------|---------|
| `accept-inbound-ssh` | قبول | TCP | 22 | All IPv4, All IPv6 | وصول SSH |
| `accept-inbound-http` | قبول | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + تحدي ACME) |
| `accept-inbound-https` | قبول | TCP | 443 | All IPv4, All IPv6 | Nginx (HTTPS بعد إعداد SSL) |
| `accept-inbound-shiny` | قبول | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (تحليلات R) |
| `accept-inbound-icmp` | قبول | ICMP | — | All IPv4, All IPv6 | Ping / التشخيص |
| السياسة الافتراضية للوارد | **إسقاط** | | | | حظر كل شيء آخر |

### حركة المرور الصادرة (Outbound)

| التسمية | الإجراء | ملاحظات |
|---------|--------|---------|
| السياسة الافتراضية للصادر | **قبول** | السماح بكل حركة المرور الصادرة (Docker، certbot، GoDaddy API، إلخ) |

### المنافذ غير المطلوبة خارجياً

هذه المنافذ مرتبطة بـ `127.0.0.1` فقط ولا يمكن الوصول إليها من الخارج:

| المنفذ | الخدمة | السبب |
|-------|--------|-------|
| 8080 | حاوية التطبيق | Nginx يعمل كوسيط داخلياً |
| 8090 | حاوية Keycloak | Nginx يعمل كوسيط داخلياً |
| 3306 | MySQL | شبكة Docker الداخلية فقط |""",

"ru": """## Правила брандмауэра (Linode Cloud Firewall)

Если вы подключаете Linode Cloud Firewall к этому серверу, используйте следующие правила:

### Входящий трафик (Inbound)

| Метка | Действие | Протокол | Порт | Источники | Примечания |
|-------|---------|---------|------|---------|----------|
| `accept-inbound-ssh` | Разрешить | TCP | 22 | All IPv4, All IPv6 | Доступ по SSH |
| `accept-inbound-http` | Разрешить | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + ACME-проверка) |
| `accept-inbound-https` | Разрешить | TCP | 443 | All IPv4, All IPv6 | Nginx (HTTPS после настройки SSL) |
| `accept-inbound-shiny` | Разрешить | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (аналитика R) |
| `accept-inbound-icmp` | Разрешить | ICMP | — | All IPv4, All IPv6 | Ping / диагностика |
| Политика входящего трафика по умолчанию | **Отклонить** | | | | Блокировать всё остальное |

### Исходящий трафик (Outbound)

| Метка | Действие | Примечания |
|-------|---------|----------|
| Политика исходящего трафика по умолчанию | **Разрешить** | Разрешить весь исходящий трафик (Docker, certbot, GoDaddy API и т.д.) |

### Порты, НЕ требующие внешнего доступа

Эти порты привязаны только к `127.0.0.1` и недоступны снаружи:

| Порт | Сервис | Причина |
|------|--------|--------|
| 8080 | Контейнер приложения | Nginx проксирует внутренне |
| 8090 | Контейнер Keycloak | Nginx проксирует внутренне |
| 3306 | MySQL | Только внутренняя сеть Docker |""",

"uk": """## Правила брандмауера (Linode Cloud Firewall)

Якщо ви підключаєте Linode Cloud Firewall до цього сервера, використовуйте такі правила:

### Вхідний трафік (Inbound)

| Мітка | Дія | Протокол | Порт | Джерела | Примітки |
|-------|-----|---------|------|---------|---------|
| `accept-inbound-ssh` | Дозволити | TCP | 22 | All IPv4, All IPv6 | SSH-доступ |
| `accept-inbound-http` | Дозволити | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + ACME-перевірка) |
| `accept-inbound-https` | Дозволити | TCP | 443 | All IPv4, All IPv6 | Nginx (HTTPS після налаштування SSL) |
| `accept-inbound-shiny` | Дозволити | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (аналітика R) |
| `accept-inbound-icmp` | Дозволити | ICMP | — | All IPv4, All IPv6 | Ping / діагностика |
| Стандартна політика вхідного трафіку | **Відхилити** | | | | Блокувати все інше |

### Вихідний трафік (Outbound)

| Мітка | Дія | Примітки |
|-------|-----|---------|
| Стандартна політика вихідного трафіку | **Дозволити** | Дозволити весь вихідний трафік (Docker, certbot, GoDaddy API тощо) |

### Порти, що НЕ потребують зовнішнього доступу

Ці порти прив'язані лише до `127.0.0.1` і ніколи не доступні ззовні:

| Порт | Сервіс | Причина |
|------|--------|--------|
| 8080 | Контейнер застосунку | Nginx проксіює внутрішньо |
| 8090 | Контейнер Keycloak | Nginx проксіює внутрішньо |
| 3306 | MySQL | Лише внутрішня мережа Docker |""",

"tr": """## Güvenlik Duvarı Kuralları (Linode Cloud Firewall)

Bu sunucuya bir Linode Cloud Firewall bağlarsanız, aşağıdaki kuralları kullanın:

### Gelen Trafik (Inbound)

| Etiket | Eylem | Protokol | Port | Kaynaklar | Notlar |
|--------|-------|---------|------|---------|-------|
| `accept-inbound-ssh` | Kabul Et | TCP | 22 | All IPv4, All IPv6 | SSH erişimi |
| `accept-inbound-http` | Kabul Et | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + ACME doğrulaması) |
| `accept-inbound-https` | Kabul Et | TCP | 443 | All IPv4, All IPv6 | Nginx (SSL kurulumundan sonra HTTPS) |
| `accept-inbound-shiny` | Kabul Et | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (R analitik) |
| `accept-inbound-icmp` | Kabul Et | ICMP | — | All IPv4, All IPv6 | Ping / tanılama |
| Varsayılan gelen politikası | **Düşür** | | | | Diğer her şeyi engelle |

### Giden Trafik (Outbound)

| Etiket | Eylem | Notlar |
|--------|-------|-------|
| Varsayılan giden politikası | **Kabul Et** | Tüm giden trafiğe izin ver (Docker, certbot, GoDaddy API vb.) |

### Harici Olarak Gerekmeyen Portlar

Bu portlar yalnızca `127.0.0.1`'e bağlıdır ve dışarıdan hiçbir zaman erişilemez:

| Port | Servis | Neden |
|------|--------|-------|
| 8080 | Uygulama konteyneri | Nginx dahili olarak proxy yapıyor |
| 8090 | Keycloak konteyneri | Nginx dahili olarak proxy yapıyor |
| 3306 | MySQL | Yalnızca dahili Docker ağı |""",

"id": """## Aturan Firewall (Linode Cloud Firewall)

Jika Anda menghubungkan Linode Cloud Firewall ke server ini, gunakan aturan berikut:

### Lalu Lintas Masuk (Inbound)

| Label | Tindakan | Protokol | Port | Sumber | Catatan |
|-------|---------|---------|------|--------|--------|
| `accept-inbound-ssh` | Izinkan | TCP | 22 | All IPv4, All IPv6 | Akses SSH |
| `accept-inbound-http` | Izinkan | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + tantangan ACME) |
| `accept-inbound-https` | Izinkan | TCP | 443 | All IPv4, All IPv6 | Nginx (HTTPS setelah setup SSL) |
| `accept-inbound-shiny` | Izinkan | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (analitik R) |
| `accept-inbound-icmp` | Izinkan | ICMP | — | All IPv4, All IPv6 | Ping / diagnostik |
| Kebijakan masuk default | **Tolak** | | | | Blokir semua yang lain |

### Lalu Lintas Keluar (Outbound)

| Label | Tindakan | Catatan |
|-------|---------|--------|
| Kebijakan keluar default | **Izinkan** | Izinkan semua lalu lintas keluar (Docker, certbot, GoDaddy API, dll.) |

### Port yang TIDAK Diperlukan Secara Eksternal

Port-port ini hanya terikat ke `127.0.0.1` dan tidak pernah dapat diakses dari luar:

| Port | Layanan | Alasan |
|------|---------|--------|
| 8080 | Container aplikasi | Nginx melakukan proxy secara internal |
| 8090 | Container Keycloak | Nginx melakukan proxy secara internal |
| 3306 | MySQL | Hanya jaringan Docker internal |""",

"hi": """## फ़ायरवॉल नियम (Linode Cloud Firewall)

यदि आप इस सर्वर से Linode Cloud Firewall जोड़ते हैं, तो निम्नलिखित नियमों का उपयोग करें:

### आने वाला ट्रैफ़िक (Inbound)

| लेबल | कार्रवाई | प्रोटोकॉल | पोर्ट | स्रोत | नोट्स |
|------|---------|---------|------|-------|-------|
| `accept-inbound-ssh` | स्वीकार | TCP | 22 | All IPv4, All IPv6 | SSH पहुंच |
| `accept-inbound-http` | स्वीकार | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + ACME चुनौती) |
| `accept-inbound-https` | स्वीकार | TCP | 443 | All IPv4, All IPv6 | Nginx (SSL सेटअप के बाद HTTPS) |
| `accept-inbound-shiny` | स्वीकार | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (R विश्लेषण) |
| `accept-inbound-icmp` | स्वीकार | ICMP | — | All IPv4, All IPv6 | Ping / निदान |
| डिफ़ॉल्ट इनबाउंड नीति | **ड्रॉप** | | | | बाकी सब ब्लॉक करें |

### जाने वाला ट्रैफ़िक (Outbound)

| लेबल | कार्रवाई | नोट्स |
|------|---------|-------|
| डिफ़ॉल्ट आउटबाउंड नीति | **स्वीकार** | सभी आउटबाउंड ट्रैफ़िक की अनुमति दें (Docker, certbot, GoDaddy API, आदि) |

### बाहरी रूप से आवश्यक नहीं पोर्ट

ये पोर्ट केवल `127.0.0.1` से बंधे हैं और बाहर से कभी पहुंच योग्य नहीं हैं:

| पोर्ट | सेवा | कारण |
|------|------|------|
| 8080 | ऐप कंटेनर | Nginx आंतरिक रूप से प्रॉक्सी करता है |
| 8090 | Keycloak कंटेनर | Nginx आंतरिक रूप से प्रॉक्सी करता है |
| 3306 | MySQL | केवल आंतरिक Docker नेटवर्क |""",

"th": """## กฎไฟร์วอลล์ (Linode Cloud Firewall)

หากคุณแนบ Linode Cloud Firewall กับเซิร์ฟเวอร์นี้ ให้ใช้กฎต่อไปนี้:

### การรับส่งข้อมูลขาเข้า (Inbound)

| ป้ายกำกับ | การกระทำ | โปรโตคอล | พอร์ต | แหล่งที่มา | หมายเหตุ |
|---------|---------|---------|------|----------|---------|
| `accept-inbound-ssh` | ยอมรับ | TCP | 22 | All IPv4, All IPv6 | การเข้าถึง SSH |
| `accept-inbound-http` | ยอมรับ | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + ACME challenge) |
| `accept-inbound-https` | ยอมรับ | TCP | 443 | All IPv4, All IPv6 | Nginx (HTTPS หลังตั้งค่า SSL) |
| `accept-inbound-shiny` | ยอมรับ | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (R analytics) |
| `accept-inbound-icmp` | ยอมรับ | ICMP | — | All IPv4, All IPv6 | Ping / การวินิจฉัย |
| นโยบายขาเข้าเริ่มต้น | **ทิ้ง** | | | | บล็อกทุกอย่างที่เหลือ |

### การรับส่งข้อมูลขาออก (Outbound)

| ป้ายกำกับ | การกระทำ | หมายเหตุ |
|---------|---------|---------|
| นโยบายขาออกเริ่มต้น | **ยอมรับ** | อนุญาตการรับส่งข้อมูลขาออกทั้งหมด (Docker, certbot, GoDaddy API เป็นต้น) |

### พอร์ตที่ไม่ต้องการเปิดภายนอก

พอร์ตเหล่านี้ผูกกับ `127.0.0.1` เท่านั้น ไม่สามารถเข้าถึงได้จากภายนอก:

| พอร์ต | บริการ | เหตุผล |
|------|--------|--------|
| 8080 | App container | Nginx proxy ภายใน |
| 8090 | Keycloak container | Nginx proxy ภายใน |
| 3306 | MySQL | เครือข่าย Docker ภายในเท่านั้น |""",

"km": """## ច្បាប់ Firewall (Linode Cloud Firewall)

ប្រសិនបើអ្នកភ្ជាប់ Linode Cloud Firewall ទៅម៉ាស៊ីនមេនេះ សូមប្រើច្បាប់ដូចខាងក្រោម:

### ចរាចរណ៍ចូល (Inbound)

| ស្លាក | សកម្មភាព | ពិធីការ | ច្រក | ប្រភព | កំណត់ចំណាំ |
|------|---------|---------|------|-------|-----------|
| `accept-inbound-ssh` | ទទួល | TCP | 22 | All IPv4, All IPv6 | ការចូលប្រើ SSH |
| `accept-inbound-http` | ទទួល | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + ACME challenge) |
| `accept-inbound-https` | ទទួល | TCP | 443 | All IPv4, All IPv6 | Nginx (HTTPS បន្ទាប់ពីដំឡើង SSL) |
| `accept-inbound-shiny` | ទទួល | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (R analytics) |
| `accept-inbound-icmp` | ទទួល | ICMP | — | All IPv4, All IPv6 | Ping / ការធ្វើរោគវិនិច្ឆ័យ |
| គោលនយោបាយ inbound លំនាំដើម | **លុបចោល** | | | | រារាំងអ្វីៗផ្សេងទៀត |

### ចរាចរណ៍ចេញ (Outbound)

| ស្លាក | សកម្មភាព | កំណត់ចំណាំ |
|------|---------|-----------|
| គោលនយោបាយ outbound លំនាំដើម | **ទទួល** | អនុញ្ញាតចរាចរណ៍ចេញទាំងអស់ (Docker, certbot, GoDaddy API ។ល។) |

### ច្រកដែលមិនត្រូវការខាងក្រៅ

ច្រកទាំងនេះភ្ជាប់តែទៅ `127.0.0.1` ហើយមិនអាចចូលប្រើពីខាងក្រៅបានទេ:

| ច្រក | សេវាកម្ម | មូលហេតុ |
|------|---------|--------|
| 8080 | App container | Nginx proxy ខាងក្នុង |
| 8090 | Keycloak container | Nginx proxy ខាងក្នុង |
| 3306 | MySQL | បណ្តាញ Docker ខាងក្នុងតែប៉ុណ្ណោះ |""",

"bg": """## Правила на защитната стена (Linode Cloud Firewall)

Ако прикачите Linode Cloud Firewall към този сървър, използвайте следните правила:

### Входящ трафик (Inbound)

| Етикет | Действие | Протокол | Порт | Източници | Бележки |
|--------|---------|---------|------|---------|--------|
| `accept-inbound-ssh` | Разреши | TCP | 22 | All IPv4, All IPv6 | SSH достъп |
| `accept-inbound-http` | Разреши | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + ACME предизвикателство) |
| `accept-inbound-https` | Разреши | TCP | 443 | All IPv4, All IPv6 | Nginx (HTTPS след настройка на SSL) |
| `accept-inbound-shiny` | Разреши | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (R анализ) |
| `accept-inbound-icmp` | Разреши | ICMP | — | All IPv4, All IPv6 | Ping / диагностика |
| Политика за входящ трафик по подразбиране | **Откажи** | | | | Блокирай всичко останало |

### Изходящ трафик (Outbound)

| Етикет | Действие | Бележки |
|--------|---------|--------|
| Политика за изходящ трафик по подразбиране | **Разреши** | Разреши целия изходящ трафик (Docker, certbot, GoDaddy API и др.) |

### Портове, НЕ необходими externally

Тези портове са обвързани само с `127.0.0.1` и не са достъпни отвън:

| Порт | Услуга | Причина |
|------|--------|--------|
| 8080 | App контейнер | Nginx проксира вътрешно |
| 8090 | Keycloak контейнер | Nginx проксира вътрешно |
| 3306 | MySQL | Само вътрешна Docker мрежа |""",

"cs": """## Pravidla firewallu (Linode Cloud Firewall)

Pokud k tomuto serveru připojíte Linode Cloud Firewall, použijte následující pravidla:

### Příchozí provoz (Inbound)

| Označení | Akce | Protokol | Port | Zdroje | Poznámky |
|---------|------|---------|------|--------|--------|
| `accept-inbound-ssh` | Přijmout | TCP | 22 | All IPv4, All IPv6 | Přístup SSH |
| `accept-inbound-http` | Přijmout | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + ACME výzva) |
| `accept-inbound-https` | Přijmout | TCP | 443 | All IPv4, All IPv6 | Nginx (HTTPS po konfiguraci SSL) |
| `accept-inbound-shiny` | Přijmout | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (R analytika) |
| `accept-inbound-icmp` | Přijmout | ICMP | — | All IPv4, All IPv6 | Ping / diagnostika |
| Výchozí příchozí politika | **Zahodit** | | | | Blokovat vše ostatní |

### Odchozí provoz (Outbound)

| Označení | Akce | Poznámky |
|---------|------|--------|
| Výchozí odchozí politika | **Přijmout** | Povolit veškerý odchozí provoz (Docker, certbot, GoDaddy API atd.) |

### Porty nepotřebné externally

Tyto porty jsou vázány pouze na `127.0.0.1` a nikdy nejsou dostupné zvenčí:

| Port | Služba | Důvod |
|------|--------|-------|
| 8080 | App kontejner | Nginx interně proxuje |
| 8090 | Keycloak kontejner | Nginx interně proxuje |
| 3306 | MySQL | Pouze interní Docker síť |""",

"pl": """## Reguły zapory sieciowej (Linode Cloud Firewall)

Jeśli podłączasz Linode Cloud Firewall do tego serwera, użyj następujących reguł:

### Ruch przychodzący (Inbound)

| Etykieta | Akcja | Protokół | Port | Źródła | Uwagi |
|---------|-------|---------|------|--------|-------|
| `accept-inbound-ssh` | Zezwól | TCP | 22 | All IPv4, All IPv6 | Dostęp SSH |
| `accept-inbound-http` | Zezwól | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + wyzwanie ACME) |
| `accept-inbound-https` | Zezwól | TCP | 443 | All IPv4, All IPv6 | Nginx (HTTPS po konfiguracji SSL) |
| `accept-inbound-shiny` | Zezwól | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (analityka R) |
| `accept-inbound-icmp` | Zezwól | ICMP | — | All IPv4, All IPv6 | Ping / diagnostyka |
| Domyślna polityka przychodzącą | **Odrzuć** | | | | Zablokuj wszystko inne |

### Ruch wychodzący (Outbound)

| Etykieta | Akcja | Uwagi |
|---------|-------|-------|
| Domyślna polityka wychodząca | **Zezwól** | Zezwól na cały ruch wychodzący (Docker, certbot, GoDaddy API itp.) |

### Porty NIE wymagane zewnętrznie

Te porty są powiązane tylko z `127.0.0.1` i nigdy nie są dostępne z zewnątrz:

| Port | Usługa | Powód |
|------|--------|-------|
| 8080 | Kontener aplikacji | Nginx proxy wewnętrznie |
| 8090 | Kontener Keycloak | Nginx proxy wewnętrznie |
| 3306 | MySQL | Tylko wewnętrzna sieć Docker |""",
}

# Languages that get the same structure with minor adaptations — use a generic template
GENERIC_LANGS = {
    "da": ("Firewall-regler (Linode Cloud Firewall)", "Hvis du tilknytter en Linode Cloud Firewall til denne server, skal du bruge følgende regler:", "Indgående trafik (Inbound)", "Label", "Handling", "Protokol", "Port", "Kilder", "Noter", "Udgående trafik (Outbound)", "Porte der IKKE er nødvendige eksternt", "Disse porte er kun bundet til", "og er aldrig tilgængelige udefra", "Tjeneste", "Årsag", "Accepter", "Afvis", "Tillad al udgående trafik"),
    "fi": ("Palomuurisäännöt (Linode Cloud Firewall)", "Jos liität Linode Cloud Firewallin tähän palvelimeen, käytä seuraavia sääntöjä:", "Saapuva liikenne (Inbound)", "Tunniste", "Toiminto", "Protokolla", "Portti", "Lähteet", "Huomiot", "Lähtevä liikenne (Outbound)", "Portit, joita EI tarvita ulkoisesti", "Nämä portit on sidottu vain osoitteeseen", "eivätkä ne ole koskaan ulkoa käsin saavutettavissa", "Palvelu", "Syy", "Hyväksy", "Hylkää", "Salli kaikki lähtevä liikenne"),
    "sv": ("Brandväggsregler (Linode Cloud Firewall)", "Om du kopplar en Linode Cloud Firewall till den här servern, använd följande regler:", "Inkommande trafik (Inbound)", "Etikett", "Åtgärd", "Protokoll", "Port", "Källor", "Anteckningar", "Utgående trafik (Outbound)", "Portar som INTE behövs externt", "Dessa portar är enbart bundna till", "och kan aldrig nås utifrån", "Tjänst", "Anledning", "Acceptera", "Avvisa", "Tillåt all utgående trafik"),
    "nb": ("Brannmurregler (Linode Cloud Firewall)", "Hvis du kobler en Linode Cloud Firewall til denne serveren, bruk følgende regler:", "Innkommende trafikk (Inbound)", "Etikett", "Handling", "Protokoll", "Port", "Kilder", "Notater", "Utgående trafikk (Outbound)", "Porter som IKKE er nødvendige eksternt", "Disse portene er kun bundet til", "og er aldri tilgjengelige utenfra", "Tjeneste", "Årsak", "Godta", "Dropp", "Tillat all utgående trafikk"),
    "hu": ("Tűzfalszabályok (Linode Cloud Firewall)", "Ha Linode Cloud Firewall-t csatol ehhez a szerverhez, használja a következő szabályokat:", "Bejövő forgalom (Inbound)", "Felirat", "Művelet", "Protokoll", "Port", "Források", "Megjegyzések", "Kimenő forgalom (Outbound)", "Kívülről NEM szükséges portok", "Ezek a portok csak a következőhöz vannak kötve:", "és soha nem érhetők el kívülről", "Szolgáltatás", "Ok", "Elfogad", "Elvet", "Minden kimenő forgalom engedélyezése"),
    "lt": ("Ugniasienės taisyklės (Linode Cloud Firewall)", "Jei prie šio serverio priskiriate Linode Cloud Firewall, naudokite šias taisykles:", "Gaunamasis srautas (Inbound)", "Etiketė", "Veiksmas", "Protokolas", "Prievadas", "Šaltiniai", "Pastabos", "Siunčiamas srautas (Outbound)", "Prievadai, kurių išoriškai NEREIKIA", "Šie prievadai susieti tik su", "ir niekada nepasiekiami iš išorės", "Paslauga", "Priežastis", "Priimti", "Atmesti", "Leisti visą siunčiamą srautą"),
    "lv": ("Ugunsmūra noteikumi (Linode Cloud Firewall)", "Ja pievienojat Linode Cloud Firewall šim serverim, izmantojiet šādus noteikumus:", "Ienākošā satiksme (Inbound)", "Etiķete", "Darbība", "Protokols", "Ports", "Avoti", "Piezīmes", "Izejošā satiksme (Outbound)", "Porti, kas NAV nepieciešami ārēji", "Šie porti ir piesaistīti tikai", "un nekad nav pieejami no ārpuses", "Pakalpojums", "Iemesls", "Pieņemt", "Nomest", "Atļaut visu izejošo satiksmi"),
    "sk": ("Pravidlá brány firewall (Linode Cloud Firewall)", "Ak k tomuto serveru pripojíte Linode Cloud Firewall, použite nasledujúce pravidlá:", "Prichádzajúca prevádzka (Inbound)", "Označenie", "Akcia", "Protokol", "Port", "Zdroje", "Poznámky", "Odchádzajúca prevádzka (Outbound)", "Porty NEPOTREBNÉ externe", "Tieto porty sú viazané len na", "a nikdy nie sú prístupné zvonka", "Služba", "Dôvod", "Prijať", "Zahodiť", "Povoliť všetku odchádzajúcu prevádzku"),
    "el": ("Κανόνες τείχους προστασίας (Linode Cloud Firewall)", "Αν συνδέσετε ένα Linode Cloud Firewall σε αυτόν τον διακομιστή, χρησιμοποιήστε τους παρακάτω κανόνες:", "Εισερχόμενη κίνηση (Inbound)", "Ετικέτα", "Ενέργεια", "Πρωτόκολλο", "Θύρα", "Πηγές", "Σημειώσεις", "Εξερχόμενη κίνηση (Outbound)", "Θύρες ΔΕΝ απαιτούνται εξωτερικά", "Αυτές οι θύρες είναι δεσμευμένες μόνο στο", "και δεν είναι ποτέ προσβάσιμες εξωτερικά", "Υπηρεσία", "Αιτία", "Αποδοχή", "Απόρριψη", "Επιτρέπεται όλη η εξερχόμενη κίνηση"),
    "sq": ("Rregullat e murit të zjarrit (Linode Cloud Firewall)", "Nëse lidhni një Linode Cloud Firewall me këtë server, përdorni rregullat e mëposhtme:", "Trafiku hyrës (Inbound)", "Etiketa", "Veprimi", "Protokolli", "Porta", "Burimet", "Shënime", "Trafiku dalës (Outbound)", "Portat që NUK nevojiten jashtë", "Këto porta janë të lidhura vetëm me", "dhe nuk janë kurrë të arritshme nga jashtë", "Shërbimi", "Arsyeja", "Pranoje", "Hidhe", "Lejoni gjithë trafikun dalës"),
    "sr": ("Правила заштитног зида (Linode Cloud Firewall)", "Ако повежете Linode Cloud Firewall са овим сервером, користите следећа правила:", "Долазни саобраћај (Inbound)", "Ознака", "Радња", "Протокол", "Порт", "Извори", "Белешке", "Одлазни саобраћај (Outbound)", "Портови који НИСУ потребни споља", "Ови портови су везани само за", "и никада нису доступни споља", "Услуга", "Разлог", "Прихвати", "Odbaci", "Dozvoliti sav odlazni saobraćaj"),
    "te": ("ఫైర్‌వాల్ నియమాలు (Linode Cloud Firewall)", "మీరు ఈ సర్వర్‌కు Linode Cloud Firewall జోడిస్తే, ఈ నియమాలను ఉపయోగించండి:", "ఇన్‌బౌండ్ ట్రాఫిక్", "లేబల్", "చర్య", "ప్రోటోకాల్", "పోర్ట్", "మూలాలు", "గమనికలు", "అవుట్‌బౌండ్ ట్రాఫిక్", "బాహ్యంగా అవసరం లేని పోర్ట్‌లు", "ఈ పోర్ట్‌లు కేవలం దీనికి మాత్రమే బంధించబడ్డాయి", "మరియు బాహ్యంగా ఎప్పుడూ చేరుకోలేవు", "సేవ", "కారణం", "అంగీకరించు", "వదలు", "అన్ని అవుట్‌బౌండ్ ట్రాఫిక్‌ని అనుమతించు"),
}

def make_generic_section(lang, t):
    h, intro, inbound_h, label, action, proto, port, sources, notes, outbound_h, no_ext_h, bound_note, unreachable_note, service, reason, accept, drop, allow_out = t
    return f"""## {h}

{intro}

### {inbound_h}

| {label} | {action} | {proto} | {port} | {sources} | {notes} |
|-------|--------|----------|------|---------|-------|
| `accept-inbound-ssh` | {accept} | TCP | 22 | All IPv4, All IPv6 | SSH access |
| `accept-inbound-http` | {accept} | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + ACME challenge) |
| `accept-inbound-https` | {accept} | TCP | 443 | All IPv4, All IPv6 | Nginx (HTTPS after SSL setup) |
| `accept-inbound-shiny` | {accept} | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (R analytics) |
| `accept-inbound-icmp` | {accept} | ICMP | — | All IPv4, All IPv6 | Ping / diagnostics |
| Default inbound policy | **{drop}** | | | | Block everything else |

### {outbound_h}

| {label} | {action} | {notes} |
|-------|--------|-------|
| Default outbound policy | **{accept}** | {allow_out} (Docker, certbot, GoDaddy API, etc.) |

### {no_ext_h}

{bound_note} `127.0.0.1` {unreachable_note}:

| {port} | {service} | {reason} |
|------|---------|--------|
| 8080 | App container | Nginx proxies internally |
| 8090 | Keycloak container | Nginx proxies internally |
| 3306 | MySQL | Internal Docker network only |"""


EN_SECTION = """## Firewall rules (Linode Cloud Firewall)

If you attach a Linode Cloud Firewall to this server, use the following rules:

### Inbound

| Label | Action | Protocol | Port | Sources | Notes |
|-------|--------|----------|------|---------|-------|
| `accept-inbound-ssh` | Accept | TCP | 22 | All IPv4, All IPv6 | SSH access |
| `accept-inbound-http` | Accept | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + ACME challenge) |
| `accept-inbound-https` | Accept | TCP | 443 | All IPv4, All IPv6 | Nginx (HTTPS after SSL setup) |
| `accept-inbound-shiny` | Accept | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (R analytics) |
| `accept-inbound-icmp` | Accept | ICMP | — | All IPv4, All IPv6 | Ping / diagnostics |
| Default inbound policy | **Drop** | | | | Block everything else |

### Outbound

| Label | Action | Notes |
|-------|--------|-------|
| Default outbound policy | **Accept** | Allow all outbound (Docker pulls, certbot, GoDaddy API, etc.) |

### Ports NOT needed externally

These ports are bound to `127.0.0.1` only and never reachable from outside the server:

| Port | Service | Reason |
|------|---------|--------|
| 8080 | App container | Nginx proxies to it internally |
| 8090 | Keycloak container | Nginx proxies to it internally |
| 3306 | MySQL | Internal Docker network only |"""

all_langs = [
    "ar","bg","cs","da","de","el","es","fi","fr","hi","hu","id","it","ja","km","ko",
    "lt","lv","nb","nl","pl","pt","pt-br","ru","sk","sq","sr","sv","te","th","tr","uk","vi","zh-hans","zh-hant"
]

updated = 0
for lang in all_langs:
    path = os.path.join(CONTENT, lang, "docs/getting-started/self-hosting/cloud-deployment/linode.md")
    if not os.path.exists(path):
        print(f"  SKIP {lang} — file not found")
        continue
    with open(path, encoding="utf-8") as f:
        content = f.read()
    if EN_SECTION not in content:
        print(f"  SKIP {lang} — anchor not found")
        continue
    if lang in SECTIONS:
        translated = SECTIONS[lang]
    elif lang in GENERIC_LANGS:
        translated = make_generic_section(lang, GENERIC_LANGS[lang])
    else:
        print(f"  SKIP {lang} — no translation defined")
        continue
    content = content.replace(EN_SECTION, translated)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    updated += 1
    print(f"  ok {lang}")

print(f"\nDone — {updated} files updated")
