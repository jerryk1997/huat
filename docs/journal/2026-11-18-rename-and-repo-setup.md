# 2026-11-18 — Rename to Huat, GitHub setup, second-brain structure

## What we worked on

Started from a local folder (`~/expense-tracker`) with no version control: a
`USER_STORIES.md`, seven HTML design prototypes, and product requirements living
only in one assistant's local memory file.

1. **Named the product.** Reviewed candidates against an SG-focused scope; chose
   **Huat**. Renamed the folder to `~/huat` and updated the `<title>`/`<h1>` strings
   in the design prototypes. Left the "Tokyo Riso" titles alone — that's the visual
   style name, not the product.
2. **Put it under version control and pushed** to `github.com/jerryk1997/huat`.
   Wrote a README, a `PRODUCT.md` brain dump from the assistant's memory file, and a
   `.gitignore` (excludes `.DS_Store` and `.claude/settings.local.json`).
3. **Restructured into a second brain.** Moved everything under `docs/`, and added
   the entry-point and continuity layer: `START_HERE.md`, `CLAUDE.md`, `STATUS.md`,
   `docs/decisions/`, `docs/journal/`, plus a glossary, a CPF reference, and
   architecture docs.

## Decisions made

- [0005](../decisions/0005-name-huat.md) — name the product Huat
- [0006](../decisions/0006-repo-as-second-brain.md) — repo is the cross-session brain
- [0001](../decisions/0001-expo-react-native.md)–[0004](../decisions/0004-byok-ai.md) —
  recorded retroactively. These were settled in earlier sessions and existed only in
  assistant memory; written up as ADRs so they're portable.

## Things found along the way

- **CPF figures are unverified.** Every number in `reference/cpf-rules.md` came from
  conversation, not from cpf.gov.sg. The age-bracket rate table and the account
  allocation table are both **incomplete** — only the ≤55 and >70 endpoints are
  captured. This blocks the CPF calculator, which is the product's differentiator.
- **The design system exists only as inline CSS** inside the prototype HTML. It will
  be reinvented inconsistently the moment app code starts.
- **`prototypes/index.html` still says "Finlet"** in two places — an earlier name
  candidate. Left as-is rather than silently rewritten; needs confirming.
- **Local-first means no backup** (ADR 0003). Losing the phone loses everything. An
  export path is a real v1 gap, not a nice-to-have.
- Fixed an unrelated typo in `~/.ssh/config` (pointed at a non-existent
  `ide_ed25519`) that was breaking SSH to GitHub in every repo on this machine.
  Backup at `~/.ssh/config.bak-20261118`.

## Still open

Carried in `STATUS.md`. Headline items: the Tokyo Riso sign-off, CPF figure
verification, overspend behaviour, and whether insurance documents leave the device
for AI parsing.

## Next session should

1. Confirm or reject Tokyo Riso — it blocks the design-system extraction.
2. Verify the CPF figures and complete both missing tables.
3. Then either extract the design system, or draft the data model. Both are unblocked
   by the above and either is a reasonable next move.
