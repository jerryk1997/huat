# CPF rules and figures

**⚠️ Verification status: UNVERIFIED.** These figures were captured from design
conversation, not read off cpf.gov.sg. CPF ceilings and limits change most years —
often every January. **Verify against official sources before building the
calculator, and re-check every January.** Being wrong here is worse than being
absent: the whole product rests on this arithmetic.

Official sources: [cpf.gov.sg](https://www.cpf.gov.sg) — contribution rates,
allocation rates, and the annual Budget announcements.

| Figure | Value | As of | Verified |
|---|---|---|---|
| Ordinary Wage (OW) ceiling | $8,000 / month | Jan 2026 | ❌ |
| Annual CPF salary ceiling (OW+AW) | ~$102,000 / year | 2026 | ❌ |
| Basic Healthcare Sum (BHS) | $79,000 | 2026 | ❌ |
| Full Retirement Sum (FRS) | $220,400 | 2026 | ❌ |
| Basic Retirement Sum (BRS) | $110,200 | 2026 | ❌ |
| OA investment threshold | $20,000 | — | ❌ |
| Voluntary top-up tax relief cap | $8,000 / year | — | ❌ |
| Extra 1% interest | on first $60,000 combined | — | ❌ |

## Contribution rates by age

Rates step down as age rises. Figures below are the endpoints captured so far — the
**full bracket table is missing** and must be sourced before implementation.

| Age | Employee | Employer |
|---|---|---|
| ≤ 55 | 20% | 17% |
| 55–60 | *missing* | *missing* |
| 60–65 | *missing* | *missing* |
| 65–70 | *missing* | *missing* |
| > 70 | 5% | 7.5% |

## Account allocation

Contributions split across **OA** (Ordinary), **SA** (Special), **MA** (MediSave)
and **RA** (Retirement, after 55). The split depends on age bracket. **The allocation
table is not yet captured** — needed before the projection feature.

## Ordinary vs Additional Wage

This distinction is the subtle part, and the part generic finance apps get wrong.

- **Ordinary Wage (OW)** — monthly salary. Capped at the OW ceiling *per month*.
- **Additional Wage (AW)** — bonuses, commissions. Capped annually at
  `annual ceiling − total OW already contributed that year`.

So a bonus's CPF treatment depends on how much OW has been contributed earlier in the
same year. Huat tracks bonuses as separate logged events and computes the remaining
AW headroom at the time of each.

## Milestones Huat surfaces

- **MA → BHS** — once MA hits BHS, overflow is redirected (to SA before 55, RA after).
  Surface this because the user's contribution behaviour effectively changes.
- **SA/RA → FRS / BRS** — retirement adequacy; FRS is the headline target.
- **OA → $20,000** — only the amount above this is investable via CPFIS-OA.
- **Top-up headroom** — unused voluntary top-up allowance means forgone tax relief;
  worth prompting before year end.
- **First $60,000 combined** — earns an extra 1% interest.

## Derived outputs

From date of birth + gross monthly salary, Huat computes: employee deduction,
employer contribution, per-account allocation, and **take-home pay** — the number
that actually matters for budgeting, and the reason CPF is a first-class feature
rather than a footnote.
