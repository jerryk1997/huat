# Data model

**Status: NOT STARTED.** No schema exists. This is next action #4 in `STATUS.md`.

Listed below are the entities the product scope clearly implies, as a starting point
for the real modelling pass — not a schema, and not decided.

## Entities implied by scope

| Entity | Holds | Notes |
|---|---|---|
| `user_profile` | DOB, gross monthly salary, onboarding state | Single row. DOB drives every CPF rate lookup. |
| `transaction` | date, amount, description, category, source | Source distinguishes manual entry from CSV import. |
| `category` | name, parent, budget link | User-renamable; supports sub-categories. |
| `budget` | category, base amount, rollover mode, accumulated balance | Rollover mode: auto / ask / reset. |
| `goal` | name, target amount, monthly contribution, balance | Shares the "pot" mechanic with budgets. |
| `cpf_account` | type (OA/SA/MA/RA), balance, as-of date | Manually seeded once, then projected. |
| `cpf_event` | salary contribution or bonus, period, computed split | Bonus needs AW-ceiling context at time of event. |
| `insurance_policy` | name, type, premium, documents, payment history | Type is AI-classified from uploaded documents. |
| `ai_config` | provider, key reference, digest schedule | Key lives in secure storage, never in SQLite. |
| `notification_rule` | type, threshold, enabled | Must be extensible — new alert types are expected. |

## Questions the modelling pass has to answer

- **Money representation.** Integer minor units (cents), never floats. Needs stating
  once and enforcing everywhere.
- **Budget periods.** Is a budget a row per month, or one row plus a running balance?
  The rollover and "ask me at month end" behaviour depends on this, and it's the
  hardest thing to change later.
- **Overspend.** Specified behaviour covers underspend only. What does an overspent
  category carry into next month — nothing, or a negative?
- **Pots.** Budgets and goals share the accumulate-and-draw mechanic. One table with
  a type discriminator, or two? They diverge on month-end behaviour.
- **CPF projection.** Stored as computed rows, or derived on read from events plus
  the rate tables? Derived is more honest; stored is faster and survives rate changes
  — this matters because rates change yearly and history must stay accurate.
- **Rate tables as data.** CPF rates and ceilings change annually (see
  `../reference/cpf-rules.md`). They need to be versioned data with effective dates,
  not constants in code, or historical calculations silently become wrong.
- **Categorisation provenance.** Was a category AI-assigned or user-set? Needed so
  re-running AI doesn't overwrite the user's own corrections.
- **Documents.** Insurance PDFs/images on the filesystem with a DB pointer, or in the
  DB? Interacts with export and with the AI-parsing privacy question in `STATUS.md`.
