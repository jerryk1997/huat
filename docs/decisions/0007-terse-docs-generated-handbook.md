# 0007 — Terse working docs + generated pretty handbook
**Status:** Accepted · **Date:** 2026-11-18

## Context
Every session re-reads the docs; prose costs context on every task. Jerry still wants
complete, nicely formatted documentation for reading.

## Decision
- `docs/`, `STATUS.md`, `START_HERE.md` are canonical and **terse** (fragments, tables,
  all facts kept, filler dropped).
- `handbook/huat-handbook.html` is **generated** from them by `scripts/build_handbook.py`
  (stdlib Python, no deps). Never hand-edited.
- AI never reads/greps the handbook (or prototypes) for lookup — only when working on it.
  `.ignore` keeps both out of ripgrep.
- Existing ADRs/journal stay as written (append-only); read order uses the decisions index
  instead of every ADR. New entries use terse templates.

## Consequences
- Much smaller per-session reading; one source of truth, so no drift between layers.
- Handbook prose is as terse as its source — pretty = layout/typography, not rewritten copy.
- Regenerating the handbook is an end-of-session step; forgetting it leaves it stale (never
  wrong-but-trusted for AI, since AI doesn't read it).

## Alternatives
- Hand-maintained pretty docs alongside terse ones — two sources, guaranteed drift.
- Pretty docs only — keeps the context cost this decision removes.
