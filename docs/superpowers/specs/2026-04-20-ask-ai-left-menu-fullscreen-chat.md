# Ask AI Left Menu + Fullscreen Chat Spec

**Date:** 2026-04-20  
**Status:** Draft  

---

## Overview

Move AI chat entry point out of floating page button and into the docs left menu. The new entry point is a styled **Ask AI** button that opens a fullscreen popup chat experience.

Current implementation loads the Realtimex embedded chat script globally in `pages/_app.tsx`. That script creates a floating button. The improved implementation should keep the same assistant configuration, but replace the floating launcher with a first-class docs navigation action.

---

## Goals

- Remove floating AI chat button from all documentation pages.
- Add a styled **Ask AI** button to the left menu/sidebar.
- Open AI chat in a fullscreen popup/modal when **Ask AI** is clicked.
- Keep chat visible, spacious, and easier to use on desktop and mobile.
- Preserve current assistant identity and embed configuration.
- Avoid breaking Nextra navigation, search, locale routing, or theme switch.

---

## Non-Goals

- Do not redesign the AI assistant backend.
- Do not change assistant prompt, model, API endpoint, or embed ID.
- Do not add page-specific AI context in this change.
- Do not build a new custom chat UI unless the embed script cannot support controlled rendering.

---

## Current State

`pages/_app.tsx` loads:

```tsx
<Script
  src="https://embed-ex-5e9c7b7337.realtimex.ai/embed/realtimex-chat-widget.min.js"
  data-embed-id="d912063b-1519-4b6b-9e66-ead46ca6aa5e"
  data-base-api-url="https://embed-ex-5e9c7b7337.realtimex.ai/api/embed"
  data-assistant-name="Nagen agent assistent"
  data-greeting="Send a chat to get started."
  data-button-color="#262626"
  data-user-bg-color="#3DBEF5"
  data-assistant-bg-color="#FFFFFF"
  strategy="afterInteractive"
/>
```

This creates a global floating chat button. The button competes with docs content, mobile controls, and page scroll.

---

## Proposed UX

### Left Menu Button

Add an **Ask AI** button near the top of the left sidebar, below the logo/search area and above the navigation tree.

Desktop layout:

```text
rtSurvey Docs
[ Search documentation... ]

[ sparkle icon ] Ask AI

Getting Started
Survey Design
Platform Interfaces
Deployment
```

Button behavior:

- Full-width within sidebar.
- Uses icon + text.
- Looks like a primary utility action, not a normal doc page link.
- Has hover, active, focus-visible, light/dark states.
- Does not navigate away from current page.

Recommended visual style:

- Border radius: `8px` max.
- Background: subtle dark/brand fill in light mode, lighter elevated fill in dark mode.
- Text: `Ask AI`.
- Icon: inline SVG sparkle/message icon.
- Height: `40px`.
- Padding: `10px 12px`.
- Font weight: `600`.

### Mobile

When mobile menu is open, show the same **Ask AI** action at the top of the mobile sidebar. Tapping opens the fullscreen popup and closes or visually de-emphasizes the menu behind the popup.

### Fullscreen Popup

When user clicks **Ask AI**, show a fullscreen modal:

```text
┌──────────────────────────────────────────────────────────────┐
│ Ask AI                                      [ close icon ]    │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│                  embedded AI chat iframe/widget              │
│                                                              │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

Desktop:

- Modal covers full viewport with fixed positioning.
- Header height: `56px`.
- Chat area fills remaining viewport.
- Optional max content width: none. Chat should feel like workspace, not small bubble.

Mobile:

- Modal covers full viewport.
- Respect safe areas with `env(safe-area-inset-*)`.
- Header stays fixed.
- Input remains usable above browser UI/keyboard where possible.

Close behavior:

- Close button.
- `Escape` key.
- Click outside only if there is a visible backdrop outside chat shell. If modal is true fullscreen, outside click is not needed.
- Restore body scroll when closed.

Accessibility:

- Button has `aria-haspopup="dialog"`.
- Modal has `role="dialog"` and `aria-modal="true"`.
- Modal title is exposed through `aria-labelledby`.
- Focus moves to close button or chat frame when opened.
- Focus returns to **Ask AI** button when closed.

---

## Technical Approach

### Discovery Gate

Before implementation, complete these checks and record the chosen path in the implementation plan:

1. **Realtimex embed control**
   - Confirm whether the embed supports disabling the floating launcher.
   - Confirm whether the embed supports mounting into a custom container.
   - Confirm whether the embed exposes a programmatic open/close API.
   - Confirm whether a hosted iframe/chat URL exists for fullscreen embedding.

2. **Nextra sidebar integration**
   - Confirm the installed Nextra version and available sidebar/menu extension points.
   - Prefer a documented theme hook.
   - If no supported sidebar hook exists, explicitly choose one fallback:
     - navbar action as temporary fallback,
     - small local sidebar wrapper,
     - or theme override with documented maintenance cost.

3. **Mobile behavior**
   - Confirm modal input remains usable on iOS Safari and Android Chrome sized viewports.
   - Confirm body scroll lock does not persist after modal close or route change.

Do not proceed with UI implementation until these decisions are known. This avoids building a styled launcher around a vendor widget that cannot be safely controlled.

### Evidence Standards

Each discovery result must include evidence, not just a judgment.

| Discovery claim | Acceptable evidence | Falsified when | Required action if falsified |
|-----------------|---------------------|----------------|------------------------------|
| Embed supports disabling floating launcher | Vendor docs, script option found in source, or fresh local load showing no launcher with the option enabled | Script creates launcher unconditionally during hard reload | Do not use script-owned launcher path; test iframe fallback |
| Embed supports custom container mount | Vendor docs, source option, or local reproduction mounting chat into a chosen DOM node | Widget always mounts to `document.body` or its own portal with no target option | Do not promise in-modal mount; use iframe fallback if available |
| Embed exposes programmatic open/close | Documented global API or observed stable event/API in script source with local reproduction | Only interaction path is synthetic click on vendor DOM | Treat synthetic click as high-risk fallback; require explicit approval in plan |
| Hosted iframe/chat URL exists | Working URL or documented embed endpoint that renders chat without floating launcher | No URL can render chat directly, or URL requires unavailable auth/session | Stop and choose between vendor widget fallback or custom UI scope change |
| Nextra sidebar hook exists | Installed version docs/types/source show supported sidebar/menu customization | Only viable path is editing `node_modules` or copying large theme internals | Do not patch `node_modules`; pick documented fallback and record tradeoff |
| Mobile input stays usable | Playwright/mobile emulation screenshot plus manual browser check when possible | Focused input is hidden by keyboard or viewport height is wrong after keyboard opens | Adjust modal sizing/scroll strategy before shipping |
| Body scroll restores | Local reproduction: open modal, scroll lock active, close, route change, lock removed | `document.body` remains locked after close/unmount/route change | Add cleanup on close and unmount before shipping |

### Stop Conditions

Implementation should pause and update this spec or the implementation plan if any of these are true:

- No supported embed path can remove the floating launcher without brittle CSS.
- Fullscreen chat requires a custom UI, contradicting the non-goal in this spec.
- Left sidebar placement requires a large Nextra theme fork.
- Mobile keyboard behavior cannot be made usable with the vendor embed.
- Accessibility can only be partially satisfied because chat is inside a third-party iframe; in that case, document wrapper-only accessibility and do not claim full chat accessibility.

### Preferred Implementation

Create a React component that controls the chat launcher and modal:

- `components/AskAiChat.tsx`
- `components/AskAiButton.tsx` if splitting improves readability.

Responsibilities:

- Render sidebar button.
- Manage open/close state.
- Lock body scroll while modal is open.
- Load or mount the chat embed only inside the fullscreen modal.
- Hide or disable the vendor floating button.

### Embed Control Options

Investigate the Realtimex embed script behavior before implementation.

Preferred options, in order:

1. Use supported data attributes or API to disable the floating launcher and mount chat into a custom container.
2. If supported, render embed inside a modal container with a target element ID.
3. If no supported container mode exists, load the script as-is, hide its floating launcher with scoped CSS, and programmatically trigger/open the widget from **Ask AI**.
4. If widget cannot be controlled safely, use a fullscreen iframe to the hosted embed/chat endpoint if supported by Realtimex.

Any fallback must avoid brittle global selectors where possible. If vendor DOM selectors are required, keep them isolated in `AskAiChat` and document why.

If the only workable approach is hiding vendor UI with global CSS, treat that as a high-risk fallback. It must include a visible comment naming the vendor DOM selector dependency and a verification step checking that the floating launcher never flashes during initial page load.

### Nextra Integration

Need place button in left menu. Check Nextra docs/theme extension points available in this project version.

Likely options:

- Use `theme.config.tsx` sidebar customization if supported.
- Add custom component through `navbar.extraContent` only if sidebar has no supported injection point.
- Override Nextra sidebar component only as last resort.

Preferred outcome: **Ask AI** appears in left docs sidebar, not top navbar.

### Current Script Change

Remove global chat script from `pages/_app.tsx` after controlled component owns script loading.

Keep assistant config centralized:

```ts
const ASK_AI_CONFIG = {
  scriptSrc: 'https://embed-ex-5e9c7b7337.realtimex.ai/embed/realtimex-chat-widget.min.js',
  embedId: 'd912063b-1519-4b6b-9e66-ead46ca6aa5e',
  baseApiUrl: 'https://embed-ex-5e9c7b7337.realtimex.ai/api/embed',
  assistantName: 'Nagen agent assistent',
  greeting: 'Send a chat to get started.',
  buttonColor: '#262626',
  userBgColor: '#3DBEF5',
  assistantBgColor: '#FFFFFF',
};
```

---

## Files Likely Impacted

- `pages/_app.tsx`
  - Remove current global embed script or move config to controlled component.
- `theme.config.tsx`
  - Add sidebar/menu integration if Nextra supports it.
- `components/AskAiChat.tsx`
  - New controlled Ask AI button/modal component.
- `styles` or global CSS file if present
  - Add modal/sidebar styles if inline styles are not enough.

Possible additional files after investigation:

- `components/AskAiButton.tsx`
- `components/AskAiModal.tsx`
- Nextra sidebar override file, only if required.

---

## Styling Requirements

### Ask AI Button

Light mode:

- Background: `#111827` or project brand-compatible dark neutral.
- Text/icon: `#ffffff`.
- Hover: slightly lighter dark.
- Focus: visible outline using brand blue.

Dark mode:

- Background: `rgba(61, 190, 245, 0.14)`.
- Border: `rgba(61, 190, 245, 0.32)`.
- Text/icon: light cyan or normal foreground.
- Hover: stronger blue tint.

### Modal

Light mode:

- Backdrop/shell: `#ffffff`.
- Header border: `rgba(17, 24, 39, 0.12)`.

Dark mode:

- Backdrop/shell: `#0b0f17`.
- Header border: `rgba(255, 255, 255, 0.12)`.

Modal should avoid heavy gradients. Chat must remain readable and dominant.

---

## Edge Cases

- User opens chat, then changes route: modal should stay open only if current app state preserves it; either behavior is acceptable if no errors occur.
- User changes language: **Ask AI** text can stay English in first version.
- Chat script fails to load: show compact error state inside modal with retry button.
- Script loads slowly: show loading state in chat area.
- Multiple clicks on **Ask AI** should not inject duplicate scripts.
- Body scroll must restore after close.
- Vendor script injects its own portal or fixed-position UI: ensure it stays visually inside the fullscreen chat experience or choose iframe fallback.
- Vendor script initially renders its floating launcher before suppression: prevent the launcher flash or reject that integration path.
- Chat conversation state after close/reopen must be intentional: either preserve current conversation or document reset behavior.

---

## Risks

### Vendor Embed Control Risk

The current embed is script-owned and may not support custom launchers or custom containers. If it only supports a floating widget, CSS suppression and synthetic clicks may be fragile.

Mitigation:

- Prefer documented embed options or iframe mode.
- Keep vendor integration isolated in one component.
- Do not scatter vendor DOM selectors across layout or theme code.

### Sidebar Integration Risk

Nextra may not expose a clean sidebar insertion point in the installed version. A deep theme override can break during dependency upgrades.

Mitigation:

- Verify extension points before implementation.
- Document the chosen hook or override.
- Keep any override small and local.

### Mobile Modal Risk

Fullscreen chat can regress mobile usability if the keyboard covers the input, if body scroll remains locked, or if safe-area spacing is ignored.

Mitigation:

- Test mobile viewport with chat input focused.
- Use `100dvh` where supported, with fallback.
- Restore body overflow on close and component unmount.

---

## Acceptance Criteria

1. No floating chat button appears on any docs page.
2. **Ask AI** button appears in the left sidebar on desktop.
3. **Ask AI** button appears in the mobile menu/sidebar.
4. Clicking **Ask AI** opens fullscreen chat popup.
5. Popup layout uses full viewport and gives chat a large readable area.
6. Close button and `Escape` close popup.
7. Page scroll is locked while popup is open and restored after close.
8. Light and dark themes both look intentional.
9. Existing search, language switcher, theme switcher, and doc navigation still work.
10. No duplicate chat scripts or duplicate widget instances are created after repeated open/close cycles.
11. No floating launcher flashes during initial page load.
12. A test chat message can be sent and an assistant response can be received.
13. Close/reopen behavior for conversation state is verified and documented.
14. Mobile chat input remains usable with the keyboard open on a `390x844` viewport.

---

## Verification Plan

- Run local dev server.
- Test desktop viewport: `1440x900`.
- Test tablet/mobile viewport: `390x844`.
- Verify left sidebar placement.
- Verify floating button is gone.
- Hard refresh and verify floating button does not flash before suppression.
- Open and close chat at least three times.
- Send one test chat message and verify assistant response renders.
- Close and reopen chat, then verify expected conversation state behavior.
- Switch light/dark theme with modal open and closed.
- Navigate to another doc page, then open chat again.
- Focus chat input on mobile viewport and verify keyboard does not hide the usable input area.
- Check browser console for duplicate widget errors or script load errors.

---

## Implementation Notes

- Prefer component-level CSS or inline style objects consistent with existing `theme.config.tsx`.
- Keep vendor integration isolated from docs layout code.
- Do not touch generated `dist/` output unless release process explicitly requires it.
- Do not localize **Ask AI** in first pass unless implementation already has a simple label map pattern available.
