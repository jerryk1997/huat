# Design system

**Status: NOT YET WRITTEN.** This is the single biggest gap in the repo.

The visual decisions currently exist **only as inline CSS inside the prototype HTML**
in `prototypes/`. That means they can't be reviewed, can't be reused, and will be
reinvented inconsistently the moment app code starts. Extracting them is next action
#2 in `STATUS.md`.

## Blocked on

Confirming the visual direction — **Tokyo Riso** is the front-runner but not signed
off. Writing a design system against an unconfirmed direction wastes the work.
See `prototype-notes.md`.

## What this document must contain, once written

- **Colour tokens** — semantic names (surface, ink, accent, positive, negative,
  warning), with light *and* dark values. A finance app shows gains and losses; red
  and green must survive colour-blindness and both themes.
- **Type scale** — families, weights, sizes, line heights. Numeric figures need
  tabular/lining digits so columns of money align.
- **Spacing and radius scale** — the discrete values allowed, not ad-hoc pixels.
- **Component patterns** — the recurring pieces: transaction row, category/budget
  card with progress, goal progress, CPF account tile, milestone meter, stat tile,
  empty state, "connect a key to unlock" AI state.
- **Money formatting** — SGD symbol placement, decimal handling, negative convention
  (minus sign vs parentheses vs colour-only — never colour alone), thousands grouping,
  how large figures abbreviate.
- **Chart conventions** — the categorical palette for spending breakdowns, and
  sequential/diverging choices. Must be consistent across every chart in the app.
- **Accessibility floor** — minimum contrast, minimum touch target, and the rule that
  no state is communicated by colour alone.

## Source material

Extract from `prototypes/menu-final.html` (resolved navigation) and
`prototypes/tokyo-riso.html` (current visual direction), cross-checking screen
coverage against `prototypes/index.html`.
