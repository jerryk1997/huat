# 0006 — Use this repo as the cross-session second brain

**Status:** Accepted
**Date:** 2026-11-18

## Context
Design and requirements work happens across many chat sessions, with different AI
assistants, on different machines, with no shared memory between them. Context was
living in chat transcripts and in one assistant's local memory file — neither
portable, neither durable. Work was being re-explained every session.

## Decision
The Git repository is the single source of truth. A fresh session with any AI starts
by reading `START_HERE.md` → `STATUS.md`, and ends by updating `STATUS.md`, adding a
journal entry, recording ADRs, folding durable facts into the living docs, and
pushing.

Structure separates three kinds of knowledge:
- **Living docs** — always describe the present; edited in place.
- **Append-only history** — `decisions/` and `journal/`; never rewritten.
- **Reference data** — external figures carrying as-of dates.

## Consequences
- Any AI, in any chat, can be productive within ~10 minutes of reading.
- Decisions stop being re-litigated, which was the main tax on each new session.
- Requires discipline: an un-pushed session is a lost session, and docs that drift
  out of date are worse than no docs because they are trusted.
- Prose docs duplicate some of what code would eventually express (e.g. the data
  model). Accepted while there is no code; the docs must yield to code once it exists.

## Alternatives considered
- **Assistant-local memory** — zero effort, but locked to one tool on one machine.
- **Notion / external wiki** — better editing, but splits the brain from the eventual
  codebase and needs an integration for each AI.
