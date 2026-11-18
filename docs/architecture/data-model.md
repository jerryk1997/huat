# Data model

**NOT STARTED.** No schema. STATUS next action #4. Entities below are implied by scope —
a starting point, not decided.

| Entity | Holds | Notes |
|---|---|---|
| `user_profile` | DOB, gross salary, onboarding state | Single row; DOB drives CPF rates |
| `transaction` | date, amount, description, category, source | Source: manual vs CSV |
| `category` | name, parent, budget link | Renamable; sub-categories |
| `budget` | category, base, rollover mode, accumulated balance | auto / ask / reset |
| `goal` | name, target, monthly contribution, balance | Shares pot mechanic |
| `cpf_account` | type (OA/SA/MA/RA), balance, as-of | Seeded once, then projected |
| `cpf_event` | salary contribution or bonus, period, computed split | Bonus needs AW context at event time |
| `insurance_policy` | name, type, premium, documents, payment history | Type AI-classified |
| `ai_config` | provider, key ref, digest schedule | Key in secure storage, never SQLite |
| `notification_rule` | type, threshold, enabled | Extensible |

## Questions to answer
- **Money:** integer cents, never floats. State once, enforce everywhere.
- **Budget periods:** row per month vs one row + running balance? Drives rollover + "ask me";
  hardest to change later.
- **Overspend:** carry negative or nothing? (only underspend specified)
- **Pots:** budgets + goals one table w/ discriminator, or two? Differ on month-end.
- **CPF projection:** stored rows vs derived on read? Derived more honest; stored faster and
  survives rate changes — history must stay accurate.
- **Rate tables as data:** versioned w/ effective dates, not code constants, or history goes
  silently wrong (`../reference/cpf-rules.md`).
- **Categorisation provenance:** AI vs user-set, so re-running AI doesn't clobber corrections.
- **Documents:** filesystem + DB pointer vs in DB? Affects export + AI-parsing privacy question.
