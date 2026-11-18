# START HERE

Repo = second brain for **Huat** (SG personal-finance app). No app code yet. Sessions
share no memory; this repo is the only continuity. Owner: Jerry.

## Read order
1. `STATUS.md` — phase, next actions, open questions. Always.
2. `docs/product/overview.md` — scope.
3. `docs/decisions/README.md` — index of settled decisions. Open an ADR only if relevant.
4. Latest `docs/journal/` entry.
5. Whatever STATUS points to. On demand only: `user-stories.md`, `glossary.md`,
   `reference/cpf-rules.md`, `architecture/`, `design/`.

## Two layers (ADR 0007)
- **`docs/`, `STATUS.md`, this file = working docs.** Terse, canonical. Read/edit these.
- **`handbook/huat-handbook.html` = pretty docs for humans.** Generated from the working
  docs by `python3 scripts/build_handbook.py`. **Never read or grep it** for lookup or
  reasoning; never hand-edit it. Touch it only when working on the handbook itself.
- Also never read `docs/design/prototypes/*.html` (40–110 KB each) unless the task is the
  prototypes. `prototype-notes.md` summarises them.
- `.ignore` excludes both from ripgrep/Grep.

## Writing style for working docs
Fragments over sentences. Tables/bullets over prose. No preamble, no restating. Keep every
fact and every "why"; drop filler. Link ADRs by number. Pretty presentation is the
handbook's job, not yours.

## Layout
```
STATUS.md  START_HERE.md  CLAUDE.md(pointer)  README.md(humans)
docs/product/      overview, user-stories, glossary
docs/reference/    external figures w/ as-of dates (cpf-rules)
docs/design/       design-system, prototype-notes, prototypes/
docs/architecture/ stack, data-model
docs/decisions/    NNNN-slug.md  append-only ADRs
docs/journal/      YYYY-MM-DD-slug.md  append-only session logs
handbook/          GENERATED pretty HTML — don't read
scripts/           build_handbook.py
```

## Rules
- **ADRs are settled.** Flag a problem once; change only via a new superseding ADR.
- **Unconfirmed ideas → mark `PROPOSED`.** Only Jerry promotes them.
- **`docs/reference/` figures carry as-of dates.** Check before quoting; say if stale.
- **Living docs** (STATUS, product, design, architecture, glossary) describe the present —
  edit in place. **History** (decisions, journal) — add files, never rewrite.

## End of session (all steps)
1. Update `STATUS.md`.
2. Journal entry `docs/journal/YYYY-MM-DD-slug.md` (real date; template in journal README).
3. ADR per real decision (next number; template in decisions README).
4. Fold durable facts into living docs (journal says *that*, living docs say *what*).
5. `python3 scripts/build_handbook.py` to regenerate the handbook.
6. Commit (descriptive message) and push. Unpushed = lost.
