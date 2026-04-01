#!/usr/bin/env python3
"""Add the Firewall rules section to all 35 language versions of linode.md.

The existing translated files follow the site convention:
- front-matter `title` and `description` are translated per language
- all body content is kept in English

This script inserts the new Firewall rules section (in English, matching the
convention) between Step 6 and the Troubleshooting section in every file.
"""

import os

BASE = "/Volumes/ExDisk/rtLab/webapp/doc.rtsurvey.com/content"
REL = "docs/getting-started/self-hosting/cloud-deployment/linode.md"

LANGUAGES = [
    "ar", "bg", "cs", "da", "de", "el", "es", "fi", "fr", "hi",
    "hu", "id", "it", "ja", "km", "ko", "lt", "lv", "nb", "nl",
    "pl", "pt", "pt-br", "ru", "sk", "sq", "sr", "sv", "te", "th",
    "tr", "uk", "vi", "zh-hans", "zh-hant",
]

# The new section to insert between Step 6 and Troubleshooting.
# Label names, port numbers, code blocks, and URLs are kept unchanged per rules.
FIREWALL_SECTION = """\
## Firewall rules (Linode Cloud Firewall)

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
| 3306 | MySQL | Internal Docker network only |

---

"""

# The anchor text that immediately follows where we want to insert the new section.
ANCHOR = "## Troubleshooting"


def process_file(lang: str) -> None:
    path = os.path.join(BASE, lang, REL)
    if not os.path.isfile(path):
        print(f"  SKIP  {lang}: file not found at {path}")
        return

    with open(path, "r", encoding="utf-8") as fh:
        content = fh.read()

    if "## Firewall rules" in content:
        print(f"  OK    {lang}: firewall section already present, skipping")
        return

    if ANCHOR not in content:
        print(f"  ERROR {lang}: anchor '{ANCHOR}' not found — skipping")
        return

    new_content = content.replace(ANCHOR, FIREWALL_SECTION + ANCHOR, 1)

    with open(path, "w", encoding="utf-8") as fh:
        fh.write(new_content)

    print(f"  DONE  {lang}")


def main() -> None:
    print(f"Processing {len(LANGUAGES)} language files…")
    for lang in LANGUAGES:
        process_file(lang)
    print("All done.")


if __name__ == "__main__":
    main()
