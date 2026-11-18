# Status

**Updated:** 2026-11-18 · **Phase:** design & requirements. No app code.

| Area | State |
|---|---|
| Product scope | Defined; stable enough to build against |
| User stories | 10 epics w/ AC; not estimated or sequenced |
| Visual design | Exploring; Tokyo Riso leads, unconfirmed |
| Design system | **Not written** — only inline CSS in prototypes |
| Architecture | Stack + data strategy decided; no data model |
| CPF rules | Captured, **unverified**; 2 tables incomplete |
| Docs | Terse working docs + generated handbook (ADR 0007) |
| App code | None |

## Next actions
1. Confirm/reject Tokyo Riso. Blocks all downstream design.
2. Write `docs/design/design-system.md` from prototypes (tokens, type, spacing, components).
3. Verify `docs/reference/cpf-rules.md` vs cpf.gov.sg; fill age-bracket + allocation tables.
   Drives core calc — wrong is worse than absent.
4. Draft `docs/architecture/data-model.md` (txns, categories, budgets+rollover, goals, CPF,
   insurance).
5. Sequence epics into milestones. CPF calculator first (differentiator, hardest to retrofit).

## Open questions
- Visual direction: Tokyo Riso or a variation?
- Budget overspend at month end: carry negative or nothing? (underspend is specified)
- AI insurance parsing: does the document leave the phone, or only extracted text?
- Web app timeline (ADR 0002 says web second, no date).
- v1 multi-currency or SGD-only?
- Export/backup path for v1 (ADR 0003 gap).
- `prototypes/index.html` still says "Finlet" ×2 — confirm Huat final, then clean.

## Out of scope
Direct bank APIs (CSV instead) · investment tracking beyond CPF · multi-user/household ·
non-SG markets.
