# Design system

**NOT WRITTEN.** Biggest gap. Decisions live only as inline CSS in `prototypes/` —
unreviewable, unreusable, will be reinvented. STATUS next action #2.

**Blocked on:** Tokyo Riso sign-off (see `prototype-notes.md`).

## Must contain
- **Colour tokens** — semantic (surface, ink, accent, positive, negative, warning); light +
  dark. Gain/loss red/green must survive colour-blindness + both themes.
- **Type scale** — families, weights, sizes, line heights. Tabular/lining digits for money.
- **Spacing + radius scale** — discrete values only.
- **Components** — transaction row, budget card w/ progress, goal progress, CPF account tile,
  milestone meter, stat tile, empty state, "connect a key to unlock" AI state.
- **Money formatting** — SGD symbol placement, decimals, negatives (sign vs parens; never
  colour alone), grouping, large-number abbreviation.
- **Charts** — categorical palette for spend breakdown; sequential/diverging; consistent app-wide.
- **Accessibility floor** — min contrast, min touch target, no state by colour alone.

## Source material
`prototypes/menu-final.html` (nav), `prototypes/tokyo-riso.html` (visual direction);
cross-check screen coverage vs `prototypes/index.html`.
