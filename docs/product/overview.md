# Huat — Product Brain Dump

Everything decided so far about what Huat is and does. Captured from the initial
design sessions. This is the source of truth for scope; `user-stories.md` turns it
into testable stories.

Last updated: 2026-11-18

## Platform

- iOS first → web app shortly after → Android on a longer horizon
- Cross-platform framework from day one (Expo / React Native)

## Bank Import & Transactions
- CSV upload from SG banks (DBS, OCBC, UOB, etc.)
- AI auto-categorises transactions from uploaded statement
- Pre-set category list (user can rename, add, delete)
- Option to let AI auto-generate categories + sub-categories from CSV data
- Manual transaction entry also supported

## Budget System
- Per-category budgets with configurable end-of-month behavior:
  - **Auto-rollover**: unused amount carries forward silently
  - **Ask me**: month-end prompt — roll over, move to a goal, or reset?
  - **Reset**: wipes back to base amount each month
- Balance = base amount + accumulated rollover (pot grows if underspent)
- A budget category can function as a sinking fund (keep contributing, don't spend until target hit)

## Goals (Savings)
- User names a goal (e.g. "New MacBook"), sets target amount + monthly contribution
- App tracks progress, projects completion date
- Notifies user when goal is reached — user then goes to buy the item
- Goals are a top-level concept separate from budgets but share the same "pot" mechanic

## CPF (Singapore-specific)
- User inputs: date of birth + gross monthly salary
- App auto-calculates:
  - Employee CPF deduction (age-dependent: 20% at ≤55, down to 5% at >70)
  - Employer contribution (17% at ≤55, down to 7.5% at >70)
  - Allocation per account (OA / SA / MA / RA) based on age bracket
  - Take-home pay (spendable income)
- Ordinary Wage ceiling: $8,000/month (Jan 2026)
- **Bonus CPF tracked separately**: user logs bonus, app calculates CPF using AW ceiling (~$102k/yr minus OW contributed that year)
- User manually inputs current OA/SA/MA balances once; app projects forward from there
- Milestone tracking:
  - MA toward BHS ($79,000) — surface when overflow behavior changes
  - SA/RA toward FRS ($220,400) / BRS ($110,200)
  - OA investment threshold ($20,000)
  - Voluntary top-up tax relief headroom ($8,000/yr)
  - Extra 1% interest on first $60k combined

## Insurance
- Free-form: user names the policy, uploads any documents (PDF/image)
- App tracks payment history (how much paid in over time)
- AI parses uploaded documents to extract coverage details and classify type:
  - Integrated Shield Plan (health/hospitalisation)
  - Life (term / whole life)
  - Critical Illness (CI)
  - Disability Income (DI)
  - Investment-linked policy (ILP)
  - General (travel / car / home)
- Separate UI per insurance type showing what user actually has and financial impact
- Coverage gap analysis relative to life goals and spending

## AI / Smart Features
- Rule-based alerts (always on): budget thresholds, large transactions, savings rate
- BYOK (bring your own key/model): user connects OpenAI / Anthropic / Google API
- App uses standardized system prompt injected with user's financial context (salary, goals, CPF, insurance) — consistent behavior across models
- AI digest: user-configurable schedule (on-demand, weekly, monthly, biannual)
- On-demand chat: ask questions against your own financial data

## Notifications (all of the below + extensible)
- Budget threshold alert (e.g. 80% of category spent)
- Goal reached / CPF milestone crossed
- Insurance premium due soon
- Month-end budget prompt (what to do with unused balances)

## Data & Privacy
- Local-first (SQLite on device — no data leaves phone initially)
- Architecture must be cloud-ready: clean data/repository layer so sync can be added later
- Preparation for future cloud backend (user-controlled server or managed service TBD)

## Build Approach
- Design phase first, then build together (user codes with AI assistance)
- User will build it themselves with Claude Code help
