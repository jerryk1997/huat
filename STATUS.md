# Status

**Updated:** 2026-11-18
**Phase:** Design & requirements gathering. No application code yet.

## Where things stand

The product scope is well defined — see `docs/product/overview.md` and the 10 epics
in `docs/product/user-stories.md`. Seven HTML prototypes explore the visual
direction. Architecture is decided at the level of stack and data strategy, but
there is no schema and no app scaffold.

| Area | State |
|---|---|
| Product scope | Defined. Stable enough to build against. |
| User stories | 10 epics with acceptance criteria. Not yet estimated or sequenced. |
| Visual design | Exploring. "Tokyo Riso" is the leading direction, not confirmed. |
| Design system | **Not written down.** Lives only inside the prototype HTML. |
| Architecture | Stack and data strategy decided. No data model yet. |
| CPF rules | Captured, but figures need verifying against official CPF sources. |
| App code | None. |

## Next actions

1. **Confirm or reject the "Tokyo Riso" visual direction.** Everything downstream in
   design waits on this.
2. **Extract the design system into `docs/design/design-system.md`** — colour tokens,
   type scale, spacing, component patterns. Right now it's trapped in HTML and will
   be lost or reinvented.
3. **Verify the CPF figures** in `docs/reference/cpf-rules.md` against cpf.gov.sg for
   the current year. They drive the core calculation; being wrong is worse than
   being absent.
4. **Draft the data model** (`docs/architecture/data-model.md`) — transactions,
   categories, budgets with rollover, goals, CPF accounts, insurance policies.
5. **Sequence the epics into milestones.** The CPF calculator should come first; it's
   the differentiator and the hardest to retrofit.

## Open questions

- Which visual direction wins — Tokyo Riso, or one of the variation sets?
- Budget rollover: what happens to a category that is *overspent* at month end? The
  underspend behaviour is specified; overspend is not.
- Where do AI-parsed insurance documents live? Local-first says on-device, but
  parsing needs an API call — does the document leave the phone, or only extracted text?
- Is there a web app before or after Android? `docs/decisions/0002` says web second,
  but no timeline.
- Does v1 need multi-currency, or is SGD-only acceptable?

## Not in scope (deliberately)

- Direct bank API integration (SG banks make this impractical) — CSV import instead
- Investment portfolio tracking beyond CPF
- Multi-user / household / shared budgets
- Non-Singapore markets
