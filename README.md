# Huat

A personal finance app for Singapore. Not just expense tracking — it ties together
spending, budgets, savings goals, CPF projections and insurance coverage into one
picture of your money.

> **Huat** (發 / 发, Hokkien) — "to prosper". As in *huat ah*.

**Status: design phase.** No application code yet. This repo is a working second
brain for the product — requirements, design exploration and decision history.

## 🤖 If you are an AI assistant

**Read [`START_HERE.md`](START_HERE.md), then [`STATUS.md`](STATUS.md).** They explain
this repository, the read order, and the rules for working in it. Don't start from
this README.

## If you are a human

- **[`STATUS.md`](STATUS.md)** — where the work stands, what's next, what's unresolved
- **[`docs/product/overview.md`](docs/product/overview.md)** — the full feature scope
- **[`docs/decisions/`](docs/decisions/)** — what's been settled, and why

## Layout

```
START_HERE.md         AI entry point: read order + working rules
STATUS.md             Living snapshot: phase, next actions, open questions
CLAUDE.md             Pointer to START_HERE (Claude Code auto-loads this)

docs/
  product/            Feature scope, user stories, glossary
  reference/          External figures (CPF rates, ceilings) with as-of dates
  design/             Design system + HTML prototypes
  architecture/       Stack and data model
  decisions/          Numbered ADRs — append-only
  journal/            Session logs — append-only
```

Design prototypes have no build step — `open docs/design/prototypes/index.html`.

## Why Singapore-specific

The CPF system is the thing generic finance apps get wrong. Gross salary tells you
almost nothing about what you can actually spend — the answer depends on your age
bracket, the Ordinary Wage ceiling, and how bonuses interact with the Additional
Wage ceiling. Huat treats that calculation as a first-class feature rather than a
footnote, and tracks progress toward the CPF milestones that actually change your
options (BHS, FRS/BRS, the $20k OA investment threshold, top-up tax relief headroom).

The flip side: the product as scoped is for an SG audience, and the name won't read
outside that market. Both are deliberate for v1 — see
[`docs/decisions/0005`](docs/decisions/0005-name-huat.md).

## Planned stack

Expo / React Native, TypeScript, iOS first, local-first SQLite with no backend in v1,
and bring-your-own-key for AI. Reasoning in
[`docs/architecture/stack.md`](docs/architecture/stack.md).

## History

Originally scaffolded as `expense-tracker`; renamed to **Huat** on 2026-11-18 once
the scope had clearly outgrown expense tracking.
