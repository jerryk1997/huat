# Prototype notes

Standalone HTML explorations in `prototypes/`. No build step — open any file
directly in a browser (`open docs/design/prototypes/index.html`).

These are **throwaway visual explorations, not a component library.** Nothing here
is production code, and nothing here should be ported directly. Their job is to
settle the visual direction; once that's settled, the decisions get written into
`design-system.md` and the HTML stops being load-bearing.

| File | What it explores | Verdict |
|---|---|---|
| `index.html` | Main design board — full screen flows: onboarding, CPF starting point, category setup, budgets, goals, alerts | Reference board. Shows the most complete picture of the app. |
| `variations.html` | Round 1 themes: **Sunset Editorial**, **Midnight Mercury**, **Citrus Pop**, **Aurora Glass** | All four set aside after round 2 |
| `variations-2.html` | Round 2 themes: **Olive & Bone**, **Tokyo Riso**, **Tide** | **Tokyo Riso** leading — not confirmed |
| `tokyo-riso.html` | Tokyo Riso pushed further — "tighter, denser, more grown-up" | Current front-runner. Needs sign-off. |
| `menu.html` → `menu-final.html` | Navigation / menu bar; `menu-final` is the resolved version | `menu-final.html` is the one to follow |
| `icons.html` | Icon system | Direction set; inventory not finalised |

## Open

- **Tokyo Riso is not formally decided.** `STATUS.md` carries this as the top open
  question; it blocks writing the design system.
- **`index.html` predates the Tokyo Riso direction** — it's the most complete flow
  coverage but not the current visual language. Don't read its styling as decided.
- **Stale product name:** `index.html` still says **"Finlet"** in two places
  ("Welcome to Finlet", "Ask Finlet") — an earlier name candidate, left as-is rather
  than silently rewritten. Worth confirming Huat is final (`docs/decisions/0005`) and
  then cleaning up.
- The "Tokyo Riso" name refers to a **risograph-print visual aesthetic**, not to the
  product. The product is Huat.
