# 2026-11-18 — Terse working docs + generated handbook

## Worked on
- Jerry: full docs should be pretty; working context as short as possible; AI never uses the
  pretty version for lookup.
- Rewrote all living docs terse (no facts dropped): START_HERE, STATUS, CLAUDE.md, product/*,
  reference/cpf-rules, design/*, architecture/*, decisions + journal READMEs.
- Added `scripts/build_handbook.py` → `handbook/huat-handbook.html` (single self-contained
  page, sidebar nav, light/dark).
- Added `.ignore` (handbook + prototypes out of Grep). CLAUDE.md now a 3-line pointer.
- Read order: decisions index (with gists) instead of all ADRs.
- STATUS open questions gained two items already raised in the previous journal: export/backup
  gap, "Finlet" cleanup.

## Decided
- [0007](../decisions/0007-terse-docs-generated-handbook.md)

## Open
Unchanged from STATUS.

## Next
Same as STATUS next actions (Tokyo Riso sign-off first).
