# Huat

A personal finance app for Singapore. Not just expense tracking — it ties together
spending, budgets, savings goals, CPF projections and insurance coverage into one
picture of your money.

> **Huat** (發 / 发, Hokkien) — "to prosper". As in *huat ah*.

## Status

**Design phase.** No application code yet. This repo currently holds the product
definition and visual design exploration.

| Path | What it is |
|---|---|
| `PRODUCT.md` | Full product brain dump — features, scope, SG-specific rules, architecture decisions |
| `USER_STORIES.md` | 10 epics of user stories with acceptance criteria |
| `design/` | Standalone HTML design explorations (open directly in a browser, no build step) |

### Design files

| File | Purpose |
|---|---|
| `design/index.html` | Main design board / visual design system |
| `design/variations.html` | Theme variations (round 1) |
| `design/variations-2.html` | Theme variations (round 2) |
| `design/tokyo-riso.html` | "Tokyo Riso" visual direction — risograph-print aesthetic |
| `design/menu.html`, `design/menu-final.html` | Navigation / menu bar exploration |
| `design/icons.html` | Icon system |

`open design/index.html` to view.

## Why Singapore-specific

The CPF system is the thing generic finance apps get wrong. Gross salary tells you
almost nothing about what you can actually spend — the answer depends on your age
bracket, the Ordinary Wage ceiling, and how bonuses interact with the Additional
Wage ceiling. Huat treats that calculation as a first-class feature rather than a
footnote, and tracks progress toward the CPF milestones that actually change your
options (BHS, FRS/BRS, the $20k OA investment threshold, top-up tax relief headroom).

The flip side: the product as scoped is for an SG audience. The name won't read
outside that market either. Both are deliberate for v1.

## Planned stack

- **Expo / React Native** — cross-platform from day one
- **iOS first**, then web, Android on a longer horizon
- **Local-first**: SQLite on device, nothing leaves the phone in v1
- Clean data/repository layer so cloud sync can be added later without a rewrite
- **BYOK for AI**: user connects their own OpenAI / Anthropic / Google key

## Roadmap

1. Finish visual design direction (in progress)
2. Scaffold the Expo app + data layer
3. CPF calculator — the core differentiator, build and validate it first
4. Transactions (manual entry → bank CSV import → AI categorisation)
5. Budgets with rollover mechanics
6. Goals
7. Insurance tracking + document parsing
8. AI digest and on-demand chat

## History

Originally scaffolded as `expense-tracker`; renamed to **Huat** on 2026-11-18 once
the scope had clearly outgrown expense tracking.
