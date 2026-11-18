# START HERE

**You are an AI assistant picking up work on Huat. Read this file first, then follow
the read order below.**

This repository is a *second brain*, not a codebase (yet). Jerry designs Huat across
many separate chat sessions, with different AI assistants and no shared memory
between them. This repo is the only continuity. Everything decided must live here,
or it is lost.

## 1. Read order

Read these in order before doing anything else. It's about 10 minutes of reading.

| # | File | Why |
|---|---|---|
| 1 | `STATUS.md` | **Where the work actually stands right now.** Current phase, next actions, open questions. Always read this. |
| 2 | `docs/product/overview.md` | What Huat is and every feature in scope |
| 3 | `docs/decisions/` | Decisions already settled — **do not re-litigate these** |
| 4 | `docs/journal/` (latest 1–2 entries) | What happened in recent sessions and why |
| 5 | Whatever `STATUS.md` points you at | Depends on the task at hand |

Skim-only unless relevant to the task: `docs/product/user-stories.md` (long),
`docs/reference/cpf-rules.md`, `docs/architecture/`, `docs/design/`.

## 2. What goes where

```
START_HERE.md              You are here. The contract for working in this repo.
STATUS.md                  Living snapshot: phase, next actions, open questions.
CLAUDE.md                  Pointer to this file (Claude Code auto-loads it).
README.md                  Human-facing intro. Not the AI entry point.

docs/
  product/
    overview.md            Full feature scope — the source of truth for "what is Huat"
    user-stories.md        10 epics, stories + acceptance criteria
    glossary.md            SG/CPF//domain terms. Read if a term is unfamiliar.
  reference/
    cpf-rules.md           Hard numbers (rates, ceilings, milestones) + as-of dates
  design/
    design-system.md       Visual decisions in words — tokens, type, colour
    prototypes/            Standalone HTML explorations. Open in a browser.
    prototype-notes.md     What each prototype was testing, and the verdict
  architecture/
    stack.md               Tech choices and why
    data-model.md          Entities and relationships
  decisions/
    NNNN-slug.md           One decision per file, numbered, append-only
  journal/
    YYYY-MM-DD-slug.md     One entry per working session, append-only
```

## 3. Rules for working here

**Settled decisions are settled.** If `docs/decisions/` has an entry, treat it as
decided. You may flag a problem with it — say so once, clearly — but don't quietly
redesign around it. Changing a decision means writing a *new* ADR that supersedes
the old one; never edit history.

**Reference numbers carry an as-of date.** Anything in `docs/reference/` is a real
external figure that changes over time (CPF ceilings change most years). Never
state one without checking its date. If it's stale, say so rather than using it.

**Distinguish decided from proposed.** When you add an idea that Jerry hasn't
confirmed, mark it `PROPOSED`. Only Jerry's confirmation promotes it.

**Living vs. append-only.** `STATUS.md`, `glossary.md`, `design-system.md`,
`data-model.md`, `stack.md` and the product docs are *living* — edit them in place
so they always describe the present. `docs/decisions/` and `docs/journal/` are
*append-only* history — add files, never rewrite them.

## 4. Before you end a session

This is the part that makes the second brain work. Do all of it:

1. **Update `STATUS.md`** — current phase, what changed, next actions, open questions.
   This is the single most important file for the next session.
2. **Write a journal entry** — `docs/journal/YYYY-MM-DD-slug.md`. What was worked on,
   what was decided, what's still open. Use today's real date.
3. **Write an ADR for each real decision** — `docs/decisions/NNNN-slug.md`, next
   number in sequence.
4. **Fold durable facts into the living docs** — a new feature belongs in
   `docs/product/overview.md`, not only in a journal entry. The journal records
   *that* something was decided; the living docs record *what is true now*.
5. **Commit and push.** Unpushed work does not exist — the next session is on a
   different machine or a different AI. Use a message that says what changed, not
   "update docs".

## 5. Journal entry template

```markdown
# YYYY-MM-DD — <topic>

## What we worked on
## Decisions made
(link to the ADR for each)
## Still open
## Next session should
```
