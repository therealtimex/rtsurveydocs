# Ask AI Left Menu + Fullscreen Chat Detailed Plan

> **Scope:** implement spec `docs/superpowers/specs/2026-04-20-ask-ai-left-menu-fullscreen-chat.md`. Do not change assistant backend, prompt, embed id, or docs content.

**Goal:** remove vendor floating AI launcher, add styled **Ask AI** action into Nextra left menu, open Realtimex chat as fullscreen popup.

**Stack:** Next.js, React 18, Nextra `^2.13.4`, `nextra-theme-docs` `^2.13.4`, Realtimex embed script.

---

## Decisions From Discovery

### Nextra

Evidence:

- `nextra-theme-docs` sidebar config has no `extraContent`.
- Sidebar DOM exists under `.nextra-sidebar-container`.
- Desktop menu class: `.nextra-menu-desktop`.
- Mobile menu class: `.nextra-menu-mobile`.

Decision:

- Do not fork Nextra theme.
- Do not patch `node_modules`.
- Use one client component that injects **Ask AI** into Nextra sidebar DOM after mount.
- Keep all DOM-class dependency inside `components/AskAiChat.tsx`.

### Realtimex

Evidence from fetched script tail:

- Global module: `EmbeddedRealTimeX`
- Chat container: `#realtimex-embed-chat-container`
- Vendor launcher container: `#realtimex-embed-chat-button-container`
- Chat shell: `#realtimex-chat`
- Settings seen: `openOnLoad`, `position`, `windowWidth`, `windowHeight`

Decision:

- Load vendor script from our component, not globally in `_app.tsx`.
- Set fullscreen-ish data attrs if accepted by script.
- Hide vendor launcher container before script loads.
- Custom **Ask AI** button opens vendor chat through stable API if present; else isolated synthetic click fallback.

Risk:

- Full no-launcher/custom-container mode not proven. If launcher flashes or click fallback breaks, stop and revisit iframe/custom UI fallback.

---

## File Changes

Create:

- `components/AskAiChat.tsx`

Modify:

- `pages/_app.tsx`

Do not modify:

- `theme.config.tsx` unless sidebar DOM injection fails.
- `node_modules`
- `dist/`

---

## Implementation Architecture

`AskAiChat` does three jobs:

1. Inject custom **Ask AI** launcher into sidebar DOM.
2. Own vendor script loading and config.
3. Own CSS overrides for vendor launcher/chat fullscreen.

Data flow:

```text
_app.tsx
  ├─ <Component {...pageProps} />
  └─ <AskAiChat />
        ├─ <style jsx global> vendor + Ask AI CSS
        ├─ <Script id="realtimex-chat-widget" ... />
        └─ effects:
             ├─ inject Ask AI hosts into Nextra menus
             ├─ observe DOM changes / route changes
             └─ open vendor chat on button click
```

---

## Task 1: Build `AskAiChat`

**File:** `components/AskAiChat.tsx`

- [ ] Create component with `useEffect`, `useRef`, `useCallback`.
- [ ] Import `Script` from `next/script`.
- [ ] Import `createRoot`, `Root` from `react-dom/client`.
- [ ] Export default `AskAiChat`.

Internal constants:

```ts
const SCRIPT_ID = 'realtimex-chat-widget-script';
const SIDEBAR_HOST_CLASS = 'rt-ask-ai-host';
const BUTTON_CONTAINER_ID = 'realtimex-embed-chat-button-container';
const CHAT_CONTAINER_ID = 'realtimex-embed-chat-container';
const CHAT_SHELL_ID = 'realtimex-chat';
```

State/refs:

- `mountedRef`: avoid SSR/browser mismatch.
- `rootsRef`: `Map<Element, Root>` for injected React roots.
- `observerRef`: `MutationObserver | null`.
- `lastFocusedButtonRef`: return focus after close if possible.

---

## Task 2: Inject Ask AI Button Into Sidebar

**Target menus:**

- `.nextra-menu-desktop`
- `.nextra-menu-mobile`

Insertion rule:

- Insert host before first menu child.
- Use same button in desktop and mobile menus.
- Host class: `.rt-ask-ai-host`.
- If host already exists in menu, do nothing.

Implementation steps:

- [ ] `findMenus()` returns existing desktop/mobile menu elements.
- [ ] `ensureButton(menu: Element)` creates host + React root.
- [ ] `injectButtons()` loops menus.
- [ ] Run `injectButtons()` on mount.
- [ ] Use `MutationObserver` on `document.body` to catch mobile menu mount/route changes.
- [ ] Cleanup: unmount roots, remove hosts, disconnect observer.

Button component:

- `<button type="button">`
- `aria-haspopup="dialog"`
- `aria-controls="realtimex-embed-chat-container"`
- icon SVG + text `Ask AI`
- `onClick={openChat}`

Do not create a fake route/link. Button must not navigate.

---

## Task 3: Style Ask AI Button

Add global CSS from `AskAiChat`.

Classes:

- `.rt-ask-ai-host`
- `.rt-ask-ai-button`
- `.rt-ask-ai-icon`

Style requirements:

- host margin bottom `12px`
- button width `100%`
- min height `40px`
- border radius `8px`
- padding `10px 12px`
- icon + text inline, gap `8px`
- font size `14px`
- font weight `600`
- no text overflow
- focus-visible outline

Light:

- background `#111827`
- color `#ffffff`
- hover `#1f2937`

Dark:

- background `rgba(61, 190, 245, 0.14)`
- border `1px solid rgba(61, 190, 245, 0.32)`
- color `#e6f8ff`
- hover `rgba(61, 190, 245, 0.22)`

---

## Task 4: Move Vendor Script Out Of `_app.tsx`

**File:** `pages/_app.tsx`

- [ ] Remove `import Script from 'next/script';`.
- [ ] Remove existing global `<Script ... />`.
- [ ] Import `AskAiChat` from `../components/AskAiChat`.
- [ ] Render `<AskAiChat />` after page component.

Expected:

```tsx
<>
  <Component {...pageProps} />
  <AskAiChat />
</>
```

---

## Task 5: Load Vendor Script In `AskAiChat`

Render `Script` after CSS, so launcher-hide CSS exists before script executes.

Use current config:

```tsx
<Script
  id={SCRIPT_ID}
  src="https://embed-ex-5e9c7b7337.realtimex.ai/embed/realtimex-chat-widget.min.js"
  data-embed-id="d912063b-1519-4b6b-9e66-ead46ca6aa5e"
  data-base-api-url="https://embed-ex-5e9c7b7337.realtimex.ai/api/embed"
  data-assistant-name="Nagen agent assistent"
  data-greeting="Send a chat to get started."
  data-button-color="#262626"
  data-user-bg-color="#3DBEF5"
  data-assistant-bg-color="#FFFFFF"
  data-open-on-load="off"
  data-window-width="100vw"
  data-window-height="100dvh"
  strategy="afterInteractive"
/>
```

Important:

- `data-open-on-load`, `data-window-width`, `data-window-height` are assumed from fetched script setting names. Verify in browser. If ignored, CSS fullscreen overrides still apply.
- Do not load this script anywhere else.

---

## Task 6: Hide Vendor Floating Launcher

CSS:

```css
#realtimex-embed-chat-button-container {
  display: none !important;
}
```

Reason:

- Vendor renders launcher when chat closed.
- Custom sidebar button is only visible launcher.

Verification:

- hard refresh page
- no floating button appears in bottom-right
- no one-frame flash visible

Stop if flash cannot be prevented.

---

## Task 7: Fullscreen Vendor Chat Styling

CSS target:

- `#realtimex-embed-chat-container`
- `#realtimex-chat`

Rules:

```css
#realtimex-embed-chat-container {
  z-index: 9999 !important;
}

#realtimex-chat {
  position: fixed !important;
  inset: 0 !important;
  width: 100vw !important;
  height: 100dvh !important;
  max-width: none !important;
  max-height: none !important;
  margin: 0 !important;
  border-radius: 0 !important;
}

@supports not (height: 100dvh) {
  #realtimex-chat {
    height: 100vh !important;
  }
}
```

Also remove vendor bottom/right offsets if needed:

- `bottom: 0 !important`
- `right: 0 !important`
- `top: 0 !important`
- `left: 0 !important`

Keep overrides narrow. Add comment explaining vendor ids came from embed script.

---

## Task 8: Open Chat From Ask AI

Implement `openChat(button: HTMLButtonElement)`.

Priority:

1. Check for stable global API:
   - inspect `window.EmbeddedRealTimeX`
   - if method exists, call it
2. Fallback: synthetic click on vendor launcher:
   - find `#realtimex-embed-chat-button-container button`
   - fallback selector: `#realtimex-embed-chat-button-container [role="button"]`
   - call `.click()`
3. If not ready:
   - retry for up to `2000ms`
   - show console warning only after timeout

Helper shape:

```ts
function clickVendorLauncher(): boolean {
  const container = document.getElementById(BUTTON_CONTAINER_ID);
  const trigger = container?.querySelector('button, [role="button"]') as HTMLElement | null;
  if (!trigger) return false;
  trigger.click();
  return true;
}
```

Comment:

- This is vendor fallback. Keep isolated. Remove if vendor exposes official API.

Focus:

- Save custom button as `lastFocusedButtonRef`.
- If vendor close can be detected, return focus to saved button.

---

## Task 9: Route + Mobile Menu Stability

Problems:

- Nextra mobile menu mounts only when opened.
- Nextra route change can rerender menus.

Plan:

- MutationObserver watches `document.body` child/subtree changes.
- Debounce injection via `requestAnimationFrame`.
- `ensureButton()` checks existing host before create.

Acceptance:

- desktop button appears after initial load
- mobile button appears after opening menu
- route change does not duplicate button

---

## Task 10: Failure UI

If script not ready after timeout:

- keep button usable
- no modal fake state
- console.warn message:
  - `Ask AI chat widget is not ready yet.`
- optional inline small text under button only if easy:
  - `Chat loading...`

Do not create custom chat UI.

---

## Task 11: Verification

Run dev server:

```bash
yarn dev
```

Desktop `1440x900`:

- [ ] no old floating button on load
- [ ] no launcher flash on hard reload
- [ ] **Ask AI** appears above left nav
- [ ] click opens fullscreen chat
- [ ] close returns page usable
- [ ] route change keeps one button only

Mobile `390x844`:

- [ ] open mobile menu
- [ ] **Ask AI** appears near top
- [ ] click opens fullscreen chat
- [ ] input visible/focusable
- [ ] body scroll restored after close

Repeated interaction:

- [ ] open/close 3+ times
- [ ] one script tag only
- [ ] one vendor chat container only
- [ ] one Ask AI host per menu

Chat:

- [ ] send one test message
- [ ] assistant response renders

Console:

- [ ] no duplicate widget errors
- [ ] no hydration errors
- [ ] no unhandled exceptions

---

## Stop Conditions

Stop and update spec/plan if:

- vendor launcher flashes and cannot be hidden before first paint
- vendor widget cannot open without brittle selector clicks
- Nextra menu injection duplicates across routes
- mobile input hidden behind keyboard
- implementation needs Nextra theme fork
- chat cannot send/receive test message
