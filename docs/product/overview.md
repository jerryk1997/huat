# Product overview

Source of truth for scope. `user-stories.md` = testable form. Updated 2026-11-18.

**Pitch:** SG personal finance — spending, budgets, goals, CPF projection, insurance in one
picture. CPF is first-class: gross salary says little about spendable pay (age bracket,
OW ceiling, bonus/AW interaction). Generic apps get this wrong.

## Platform
iOS → web soon after → Android later (ADR 0002). Expo/RN from day one (ADR 0001).

## Transactions & import
- CSV import from SG banks (DBS, OCBC, UOB, …).
- AI auto-categorises imported rows.
- Preset category list; user can rename/add/delete.
- Option: AI generates categories + sub-categories from CSV.
- Manual entry supported.

## Budgets
- Per-category, configurable month-end behaviour:
  - **Auto-rollover** — unused carries forward silently.
  - **Ask me** — month-end prompt: roll over / move to goal / reset.
  - **Reset** — back to base each month.
- Balance = base + accumulated rollover (pot grows if underspent).
- A category can act as a sinking fund (contribute; don't spend until target).

## Goals
- Name, target, monthly contribution → progress + projected completion date.
- Notify when reached (user then buys).
- Top-level, separate from budgets, same "pot" mechanic.

## CPF
- Inputs: DOB + gross monthly salary.
- Computes: employee deduction (age-based, 20% ≤55 → 5% >70), employer (17% ≤55 → 7.5%
  >70), split across OA/SA/MA/RA by age, take-home pay.
- OW ceiling $8,000/mo (Jan 2026, unverified).
- Bonus logged separately; CPF via AW ceiling (~$102k/yr − OW contributed YTD).
- User enters OA/SA/MA balances once; app projects forward.
- Milestones: MA → BHS $79k (overflow changes) · SA/RA → FRS $220.4k / BRS $110.2k ·
  OA $20k investment threshold · top-up tax relief $8k/yr · extra 1% on first $60k combined.
- All figures: see `../reference/cpf-rules.md` (unverified).

## Insurance
- Free-form: name policy, upload docs (PDF/image).
- Tracks premiums paid over time.
- AI parses docs → coverage details + type: ISP (health) · Life (term/whole) · CI · DI ·
  ILP · General (travel/car/home).
- Per-type UI: what user has + financial impact.
- Coverage gap analysis vs life goals and spending.

## AI (ADR 0004)
- Rule-based alerts always on, no key: budget thresholds, large txns, savings rate.
- BYOK: OpenAI / Anthropic / Google.
- Standardised system prompt + injected context (salary, goals, CPF, insurance) for
  consistent behaviour across models.
- Digest on schedule: on-demand / weekly / monthly / biannual.
- On-demand chat over own data.

## Notifications (extensible)
Budget threshold (e.g. 80%) · goal reached · CPF milestone · premium due · month-end
budget prompt.

## Data & privacy (ADR 0003)
- Local-first SQLite; no data leaves phone in v1 (except AI calls).
- Repository layer so sync can be added later; future backend (self-hosted or managed) TBD.

## Build approach
Design first, then Jerry builds with Claude Code.
