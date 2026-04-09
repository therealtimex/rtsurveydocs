# XLSForm Agent — Design Spec

**Date:** 2026-04-09  
**Status:** Approved  

---

## Overview

A web-based AI chat agent that helps RTSurvey solution developers **design**, **review**, **debug**, and **create** XLSForm files. The agent is powered by `@mariozechner/pi-agent-core`, uses `@mariozechner/pi-web-ui`'s `AgentInterface` for the chat UI, and is deployed as a Next.js app on Vercel.

The agent reads skill definitions from the `agent-skills` GitLab repo at startup, injects them into its system prompt (knowledge), and exposes them as callable tools (execution). Skills are plugin-ready — new skills added to `agent-skills` automatically extend the agent after a reload.

---

## Goals

- Support DESIGN, DEBUG, and REVIEW modes for XLSForms (driven by `rtsurvey-xlsform` skill)
- Accept XLSX file uploads for review/validation
- Show generated XLSForm rows as inline artifacts (Markdown tables)
- Support slash commands for quick mode switching
- Work with any LLM provider — switch via env vars, no code changes
- Deploy to Vercel from a private GitLab repo with zero Docker overhead

---

## Architecture

### Layers

```
Browser
├── Next.js page (SSR shell only)
└── XlsformAgent component ('use client', dynamic import ssr:false)
    ├── SlashCommandOverlay  (our code, ~80 lines)
    └── AgentInterface       (@mariozechner/pi-web-ui)
        ├── streaming chat messages
        ├── XLSX file upload (built-in)
        ├── inline artifact rendering (ArtifactsToolRenderer)
        ├── API key dialog (ApiKeyPromptDialog)
        └── pi-agent-core Agent
            ├── system prompt ← skills injected
            └── tools → Next.js API routes

Vercel (Next.js)
├── /api/skills          Node.js — proxy to GitLab, module-level cache
├── /api/reload-skills   Node.js — clears cache, protected by RELOAD_SECRET
├── /api/validate        Python 3.13 — pyxform validation
└── /api/xlsform         Python 3.13 — xlsform_template + xlsform_writer scripts
```

### Agent runs client-side

The `pi-agent-core` Agent runs in the browser. LLM API calls go directly from the browser to the provider. API keys are entered by the user and stored in browser IndexedDB by `pi-web-ui`'s `ProviderKeysStore`. This means each team member uses their own API key — no shared server key to manage.

Python tool execution calls Next.js API routes via fetch.

---

## Repository

- **Name:** `xlsform-agent`
- **Host:** Private repo on `rtgit.rta.vn` (same GitLab as other RTLab projects)
- **Vercel:** Connected to the GitLab repo — push to `main` → auto-deploy

---

## LLM Provider

Multi-provider via environment variables. No code changes needed to switch.

```env
AGENT_PROVIDER=google          # google | anthropic | openai | qwen
AGENT_MODEL=gemini-2.5-pro     # any model supported by pi-ai for that provider
```

Each provider reads its API key from a standard env var:

| Provider | Env var |
|----------|---------|
| `google` | `GEMINI_API_KEY` |
| `anthropic` | `ANTHROPIC_API_KEY` |
| `openai` | `OPENAI_API_KEY` |
| `qwen` | `QWEN_API_KEY` + `QWEN_BASE_URL=https://dashscope-intl.aliyuncs.com/compatible-mode/v1` |

**Default for testing:** `AGENT_PROVIDER=google`, `AGENT_MODEL=gemini-2.5-pro`

### API key management

Because the agent runs client-side, API keys are entered by the user via `pi-web-ui`'s `ApiKeyPromptDialog` and stored in browser IndexedDB — not in any env var. Each team member manages their own key.

> **Note on Gemini OAuth:** `pi-ai` includes a full `geminiCliOAuthProvider` (Google Cloud Code Assist, PKCE flow). However, it requires Node.js `http.createServer` for the callback and is CLI-only — it cannot run in the browser. OAuth is a future option if the agent is ever moved server-side.

### Provider resolver

Since the agent runs client-side, provider config is exposed as `NEXT_PUBLIC_*` env vars (set in Vercel dashboard, safe to expose — they carry no secrets):

```env
NEXT_PUBLIC_AGENT_PROVIDER=google
NEXT_PUBLIC_AGENT_MODEL=gemini-2.5-pro
```

`lib/llm-provider.ts` reads these in the browser:

```typescript
export function getConfiguredModel(): Model<any> {
  return getModel(
    process.env.NEXT_PUBLIC_AGENT_PROVIDER ?? 'google',
    process.env.NEXT_PUBLIC_AGENT_MODEL ?? 'gemini-2.5-pro'
  )
}
```

---

## Skills Plugin System

### Source

Skills live in the `agent-skills` repo on `rtgit.rta.vn`. The relevant xlsx-related skills:

| Skill | Purpose |
|-------|---------|
| `rtsurvey-xlsform` | Core: design/debug/review XLSForms |
| `xlsform-write` | Create new forms or add rows to existing |
| `xlsform-read` | Read and inspect form structure |
| `form-validator` | Validate via pyxform |
| `form-uploader` | Upload validated XML to server |
| `xlsx-edit` | Edit existing xlsx files |

### Fetching

`/api/skills` route fetches skill `.md` files from GitLab raw URLs at first request, caches them in a module-level variable (persists across requests on the same Fluid Compute instance).

```typescript
// lib/skills-cache.ts
let cache: string | null = null

export async function getSkillsSystemPrompt(): Promise<string> {
  if (cache) return cache
  cache = await fetchSkillsFromGitLab()
  return cache
}
```

GitLab access uses a Deploy Token with `read_repository` scope:

```env
SKILLS_GITLAB_TOKEN_USER=xlsform-agent-deploy
SKILLS_GITLAB_TOKEN=<deploy-token-value>
SKILLS_GITLAB_BASE=https://rtgit.rta.vn/solutionteam/agent-skills/-/raw/main
```

### Reload

`POST /api/reload-skills` — sets `cache = null`, protected by `RELOAD_SECRET`. Call this after pushing new skills to the `agent-skills` repo.

### New plugins

When a new skill directory is added to `agent-skills`, it is auto-discovered at the next reload. No code changes to the agent app needed.

---

## Agent Tools

The agent has four callable tools that map to Next.js API routes:

| Tool | Route | Runtime | What it does |
|------|-------|---------|--------------|
| `validate_form` | `POST /api/validate` | Python 3.13 | Runs pyxform on uploaded xlsx, returns errors/warnings |
| `write_form` | `POST /api/xlsform` | Python 3.13 | Creates or edits a form using xlsform_template + xlsform_writer scripts |
| `read_form` | `POST /api/xlsform` | Python 3.13 | Reads xlsx structure, returns survey/choices/settings as JSON |
| `convert_xlsx` | `POST /api/xlsform` | Python 3.13 | Converts xlsx to XML or JSON |

### Private pyxform

pyxform is installed from the private GitLab repo using a Deploy Token:

```env
PYXFORM_GITLAB_TOKEN_USER=pyxform-deploy
PYXFORM_GITLAB_TOKEN=<deploy-token-value>
```

In `vercel.json` build command:
```bash
pip install git+https://$PYXFORM_GITLAB_TOKEN_USER:$PYXFORM_GITLAB_TOKEN@rtgit.rta.vn/rtlab/rta-odk/pyxform.git && next build
```

### Python scripts

The Python scripts from `agent-skills` (`xlsform_template.py`, `xlsform_writer.py`, `xlsform_read.py`) are **vendored** into the repo under `scripts/xlsform/`. They are small, stable utilities. When the agent-skills versions update, copy them over manually and commit.

---

## Chat UI

### Layout

Simple centered chat (Option A) — single column, dark header bar, clean message list, input at the bottom. Matches the ChatGPT/Claude aesthetic the team is familiar with.

```
┌─ header ─────────────────────────────────────┐
│ 📊 XLSForm Agent          ● gemini-2.5-pro   │
├───────────────────────────────────────────────┤
│                                               │
│  [agent message]                              │
│                        [user message]         │
│  [tool execution card]                        │
│  [inline artifact — xlsform table]            │
│                                               │
├───────────────────────────────────────────────┤
│  [input]                           📎  ↑      │
└───────────────────────────────────────────────┘
```

### Inline artifacts

`ArtifactsToolRenderer` from `pi-web-ui` renders generated XLSForm rows as Markdown tables inline in the message flow. No separate panel.

### Slash commands

Custom overlay triggered on `/` keypress in the input box. Filters as the user types. Selecting a command fills the input with a pre-written prompt.

| Command | Fills input with |
|---------|-----------------|
| `/design` | `"I want to design a form that..."` |
| `/validate` | Opens file picker, attaches xlsx, fills `"Please validate this form"` |
| `/review` | Opens file picker, attaches xlsx, fills `"Please review this form for issues"` |
| `/debug` | `"Help me debug this expression: "` |
| `/convert` | Opens file picker, attaches xlsx, fills `"Convert this form to XML"` |

Implementation: detect `/` in `MessageEditor` textarea via `onInput`, render a floating dropdown overlay positioned above the input. ~80 lines of TypeScript in `components/SlashCommandOverlay.tsx`.

### XLSX file upload

Built into `AgentInterface` via `pi-web-ui`'s `loadAttachment`. Supported formats: XLSX, PDF, DOCX, PPTX, images. The agent receives the extracted text content and file name.

### API key management

`ApiKeyPromptDialog` from `pi-web-ui` prompts the user for their API key on first use. Key is stored in browser IndexedDB via `ProviderKeysStore`. No server-side key needed.

---

## File Structure

```
xlsform-agent/
├── app/
│   ├── page.tsx                    # loads XlsformAgent (ssr:false)
│   ├── layout.tsx
│   └── api/
│       ├── skills/route.ts         # proxy → GitLab, module cache
│       ├── reload-skills/route.ts  # clears cache, requires RELOAD_SECRET
│       ├── validate/index.py       # pyxform validation
│       └── xlsform/index.py        # template/write/read/convert
├── components/
│   ├── XlsformAgent.tsx            # 'use client' wrapper
│   └── SlashCommandOverlay.tsx     # slash command UI (~80 lines)
├── lib/
│   ├── agent.ts                    # pi-agent-core setup + tools
│   ├── skills-cache.ts             # module-level skills cache
│   └── llm-provider.ts             # reads AGENT_PROVIDER/AGENT_MODEL
├── scripts/
│   └── xlsform/                    # vendored Python scripts from agent-skills
│       ├── xlsform_template.py
│       ├── xlsform_writer.py
│       └── xlsform_read.py
├── requirements.txt                # pyxform (installed from rtgit.rta.vn)
├── vercel.json                     # build command, function config
└── package.json
```

---

## Vercel Configuration

```json
{
  "buildCommand": "pip install git+https://$PYXFORM_GITLAB_TOKEN_USER:$PYXFORM_GITLAB_TOKEN@rtgit.rta.vn/rtlab/rta-odk/pyxform.git && next build",
  "functions": {
    "app/api/validate/index.py": { "runtime": "python3.13" },
    "app/api/xlsform/index.py":  { "runtime": "python3.13", "maxDuration": 60 }
  }
}
```

---

## Environment Variables

| Variable | Purpose |
|----------|---------|
| `NEXT_PUBLIC_AGENT_PROVIDER` | LLM provider exposed to browser (`google` default) |
| `NEXT_PUBLIC_AGENT_MODEL` | Model name exposed to browser (`gemini-2.5-pro` default) |
| `SKILLS_GITLAB_TOKEN_USER` | Deploy token username for agent-skills |
| `SKILLS_GITLAB_TOKEN` | Deploy token value for agent-skills |
| `SKILLS_GITLAB_BASE` | Raw URL base for agent-skills repo |
| `PYXFORM_GITLAB_TOKEN_USER` | Deploy token username for private pyxform |
| `PYXFORM_GITLAB_TOKEN` | Deploy token value for private pyxform |
| `RELOAD_SECRET` | Bearer token protecting `/api/reload-skills` |

---

## Data Flow — Example: `/validate` command

```
1. User types /validate → slash overlay appears
2. User selects /validate → file picker opens
3. User picks household_survey.xlsx
4. AgentInterface attaches file, fills input "Please validate this form"
5. User submits → pi-agent-core sends to Gemini
6. Gemini responds with tool call: validate_form({ file: "household_survey.xlsx" })
7. Agent (browser) calls POST /api/validate with file content
8. Python function runs: pyxform → returns { errors, warnings, code }
9. Agent receives tool result, Gemini produces summary
10. Message appears with inline artifact showing validation results
```

---

## Out of Scope

- User authentication / multi-tenant sessions (single-user tool)
- Form upload to RTSurvey server (handled by `form-uploader` skill separately)
- Real-time collaboration
- Form version history
