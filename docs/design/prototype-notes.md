# Prototype notes

Standalone HTML in `prototypes/`, no build (`open docs/design/prototypes/index.html`).
Throwaway explorations, not a component library; never port. Once direction is settled,
decisions move to `design-system.md`. **Don't read the HTML unless working on it** (huge).

| File | Explores | Verdict |
|---|---|---|
| `index.html` | Main board: onboarding, CPF start, category setup, budgets, goals, alerts | Most complete flow coverage; **predates Tokyo Riso** — styling not decided |
| `variations.html` | R1: Sunset Editorial, Midnight Mercury, Citrus Pop, Aurora Glass | All set aside after R2 |
| `variations-2.html` | R2: Olive & Bone, Tokyo Riso, Tide | Tokyo Riso leads — unconfirmed |
| `tokyo-riso.html` | Tokyo Riso pushed: "tighter, denser, more grown-up" | Front-runner; needs sign-off |
| `menu.html` → `menu-final.html` | Nav/menu bar | Follow `menu-final` |
| `icons.html` | Icon system | Direction set; inventory not final |

## Open
- Tokyo Riso not formally decided; blocks design system.
- `index.html` says "Finlet" ×2 ("Welcome to Finlet", "Ask Finlet") — old name candidate.
  Confirm Huat final (ADR 0005), then clean.
- "Tokyo Riso" = risograph-print aesthetic, not the product.
