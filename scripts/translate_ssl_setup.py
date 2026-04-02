#!/usr/bin/env python3
"""
translate_ssl_setup.py
Uses Google Translate (via deep-translator) to translate ssl-setup.md into all 35 languages.

Usage:
    pip install deep-translator
    python3 scripts/translate_ssl_setup.py
"""
import os
import time
from deep_translator import GoogleTranslator

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT  = os.path.join(REPO_DIR, "content")

# Hugo lang code → Google Translate lang code
LANG_MAP = {
    "ar":      "ar",
    "bg":      "bg",
    "cs":      "cs",
    "da":      "da",
    "de":      "de",
    "el":      "el",
    "es":      "es",
    "fi":      "fi",
    "fr":      "fr",
    "hi":      "hi",
    "hu":      "hu",
    "id":      "id",
    "it":      "it",
    "ja":      "ja",
    "km":      "km",
    "ko":      "ko",
    "lt":      "lt",
    "lv":      "lv",
    "nb":      "no",
    "nl":      "nl",
    "pl":      "pl",
    "pt":      "pt",
    "pt-br":   "pt",
    "ru":      "ru",
    "sk":      "sk",
    "sq":      "sq",
    "sr":      "sr",
    "sv":      "sv",
    "te":      "te",
    "th":      "th",
    "tr":      "tr",
    "uk":      "uk",
    "vi":      "vi",
    "zh-hans": "zh-CN",
    "zh-hant": "zh-TW",
}

# All prose strings to translate (code blocks, paths, URLs are NOT included)
EN_STRINGS = {
    "title":             "Set Up SSL",
    "description":       "Configure HTTPS for your rtSurvey server. Required before you can log in.",
    "intro":             "SSL must be configured before you can log in. When you open the app for the first time, you will be redirected to the SSL setup screen automatically.",
    "h_options":         "SSL setup options",
    "img_alt":           "SSL setup options",
    "choose_three":      "Choose one of three options:",
    "th_option":         "Option",
    "th_when":           "When to use",
    "opt1_name":         "Free rtsurvey.com subdomain",
    "recommended":       "Recommended",
    "opt1_desc":         "No DNS setup needed. We create the record for you. Ready in 2–5 minutes.",
    "opt2_name":         "My own domain",
    "opt2_desc":         "You already have a domain and its DNS points to this server.",
    "opt3_name":         "Install certificate manually",
    "opt3_desc":         "Enterprise or custom CA. Requires SSH access.",
    "h_opt1":            "Option 1 — Free rtsurvey.com subdomain (Recommended)",
    "opt1_fastest":      "This is the fastest option. No domain registration or DNS changes required.",
    "opt1_s1":           "Click Free rtsurvey.com subdomain to expand the section",
    "opt1_s2":           "Type your desired subdomain name in the input field",
    "opt1_note":         "Use lowercase letters, numbers, and hyphens. 3–30 characters.",
    "opt1_example":      "Example:",
    "opt1_s3":           "Click Create",
    "opt1_s4":           "Wait 2–5 minutes while the certificate is issued",
    "opt1_s5":           "Once the certificate is ready, you will be redirected to your new HTTPS URL automatically",
    "h_opt2":            "Option 2 — My own domain",
    "opt2_intro":        "Use this if you have an existing domain and its DNS A record already points to this server's IP.",
    "opt2_s1":           "Click My own domain to expand the section",
    "opt2_s2":           "Enter your full domain name",
    "opt2_s3":           "Click Create certificate",
    "opt2_letsencrypt":  "Let's Encrypt will verify your domain and issue a certificate. This requires DNS to be correctly pointed first — the request will fail otherwise.",
    "h_opt3":            "Option 3 — Install certificate manually",
    "opt3_intro":        "For enterprise environments using a custom or internal CA. You will place your certificate files on the server via SSH, then enter your domain in the app.",
    "h_prereq":          "Prerequisites",
    "prereq1":           "SSH access to the server",
    "prereq2":           "A valid certificate and private key for your domain (PEM format)",
    "h_step1":           "Step 1 — SSH into the server",
    "h_step2":           "Step 2 — Place your certificate files",
    "step2_create":      "Create the directory and copy your files:",
    "step2_copy_intro":  "Copy your files into that directory with these exact names:",
    "th_file":           "File",
    "th_desc":           "Description",
    "fullchain_desc":    "Your certificate + any intermediate CA certificates (concatenated)",
    "privkey_desc":      "Your private key",
    "example_label":     "Example:",
    "copy_comment":      "Copy from your local machine (run this locally, not on the server)",
    "set_permissions":   "Set correct permissions:",
    "h_step3":           "Step 3 — Enter your domain in the app",
    "step3_s1":          "In the SSL setup screen, click Install certificate manually",
    "step3_s2":          "Enter your domain name (must match the certificate's Common Name or SAN)",
    "step3_s3":          "Click Apply",
    "step3_result":      "The server will configure Nginx with your certificate and reload automatically.",
    "h_next":            "Next step",
    "next_text":         "Once SSL is active, proceed to First Login.",
}


def translate_all(google_lang):
    """Translate all EN_STRINGS into google_lang. Returns dict with same keys."""
    translator = GoogleTranslator(source="en", target=google_lang)
    result = {}
    for key, text in EN_STRINGS.items():
        try:
            result[key] = translator.translate(text)
            time.sleep(0.05)   # gentle rate limit
        except Exception as e:
            print(f"    WARNING: failed to translate '{key}': {e} — using English fallback")
            result[key] = text
    return result


def build(t, hugo_lang):
    """Build the full markdown file content from a translation dict."""
    # Reconstruct headings that had formatting stripped for translation
    h_opt1 = t["h_opt1"].replace("(Recommended)", f"*({t['recommended']})*")
    opt1_name_fmt = f'**{t["opt1_name"]}**'
    opt2_name_fmt = f'**{t["opt2_name"]}**'
    opt3_name_fmt = f'**{t["opt3_name"]}**'

    c = t["copy_comment"]
    return (
        f'---\n'
        f'weight: 4\n'
        f'title: "{t["title"]}"\n'
        f'date: "2026-04-01T00:00:00+07:00"\n'
        f'lastmod: "2026-04-01T00:00:00+07:00"\n'
        f'draft: false\n'
        f'author: "rtSurvey"\n'
        f'icon: "lock"\n'
        f'toc: true\n'
        f'description: "{t["description"]}"\n'
        f'---\n'
        f'\n'
        f'{t["intro"]}\n'
        f'\n'
        f'---\n'
        f'\n'
        f'## {t["h_options"]}\n'
        f'\n'
        f'![{t["img_alt"]}](/img/ssl-setup/ssl-setup-options.png)\n'
        f'\n'
        f'{t["choose_three"]}\n'
        f'\n'
        f'| {t["th_option"]} | {t["th_when"]} |\n'
        f'|--------|-------------|\n'
        f'| {opt1_name_fmt} *({t["recommended"]})* | {t["opt1_desc"]} |\n'
        f'| {opt2_name_fmt} | {t["opt2_desc"]} |\n'
        f'| {opt3_name_fmt} | {t["opt3_desc"]} |\n'
        f'\n'
        f'---\n'
        f'\n'
        f'## {h_opt1}\n'
        f'\n'
        f'{t["opt1_fastest"]}\n'
        f'\n'
        f'1. {t["opt1_s1"]}\n'
        f'2. {t["opt1_s2"]}\n'
        f'\n'
        f'   > {t["opt1_note"]}\n'
        f'   > {t["opt1_example"]} `myproject` \u2192 `myproject.rtsurvey.com`\n'
        f'\n'
        f'3. {t["opt1_s3"]} **https://[subdomain].rtsurvey.com**\n'
        f'\n'
        f'<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->\n'
        f'\n'
        f'4. {t["opt1_s4"]}\n'
        f'\n'
        f'<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->\n'
        f'\n'
        f'5. {t["opt1_s5"]}\n'
        f'\n'
        f'<!-- SCREENSHOT NEEDED: success state / redirect to login -->\n'
        f'\n'
        f'---\n'
        f'\n'
        f'## {t["h_opt2"]}\n'
        f'\n'
        f'{t["opt2_intro"]}\n'
        f'\n'
        f'1. {t["opt2_s1"]}\n'
        f'2. {t["opt2_s2"]} (e.g. `survey.myorganization.org`)\n'
        f'3. {t["opt2_s3"]}\n'
        f'\n'
        f'<!-- SCREENSHOT NEEDED: own domain input form -->\n'
        f'\n'
        f'{t["opt2_letsencrypt"]}\n'
        f'\n'
        f'---\n'
        f'\n'
        f'## {t["h_opt3"]}\n'
        f'\n'
        f'{t["opt3_intro"]}\n'
        f'\n'
        f'### {t["h_prereq"]}\n'
        f'\n'
        f'- {t["prereq1"]}\n'
        f'- {t["prereq2"]}\n'
        f'\n'
        f'### {t["h_step1"]}\n'
        f'\n'
        '```bash\n'
        'ssh root@<server-ip>\n'
        '```\n'
        f'\n'
        f'### {t["h_step2"]}\n'
        f'\n'
        f'{t["step2_create"]}\n'
        f'\n'
        '```bash\n'
        'mkdir -p /etc/letsencrypt/live/<your-domain>\n'
        '```\n'
        f'\n'
        f'{t["step2_copy_intro"]}\n'
        f'\n'
        f'| {t["th_file"]} | {t["th_desc"]} |\n'
        f'|------|-------------|\n'
        f'| `fullchain.pem` | {t["fullchain_desc"]} |\n'
        f'| `privkey.pem` | {t["privkey_desc"]} |\n'
        f'\n'
        f'{t["example_label"]}\n'
        f'\n'
        '```bash\n'
        f'# {c}\n'
        'scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem\n'
        'scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem\n'
        '```\n'
        f'\n'
        f'{t["set_permissions"]}\n'
        f'\n'
        '```bash\n'
        'chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem\n'
        'chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem\n'
        '```\n'
        f'\n'
        f'### {t["h_step3"]}\n'
        f'\n'
        f'<!-- SCREENSHOT NEEDED: manual certificate form -->\n'
        f'\n'
        f'1. {t["step3_s1"]}\n'
        f'2. {t["step3_s2"]}\n'
        f'3. {t["step3_s3"]}\n'
        f'\n'
        f'{t["step3_result"]}\n'
        f'\n'
        f'---\n'
        f'\n'
        f'## {t["h_next"]}\n'
        f'\n'
        f'{t["next_text"].rstrip(".")} [first-login](first-login).\n'
    )


def main():
    for hugo_lang, google_lang in LANG_MAP.items():
        print(f"  {hugo_lang} ({google_lang}) ...", end=" ", flush=True)
        t = translate_all(google_lang)
        content = build(t, hugo_lang)
        out_path = os.path.join(
            CONTENT, hugo_lang,
            "docs/getting-started/self-hosting/ssl-setup.md"
        )
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("done")
    print(f"\nDone — {len(LANG_MAP)} files written")


if __name__ == "__main__":
    main()
