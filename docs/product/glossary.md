# Glossary

Singapore-specific and domain terms used across these docs. If a term in a doc is
unfamiliar, it should be here — add it if it isn't.

## CPF

| Term | Meaning |
|---|---|
| **CPF** | Central Provident Fund — Singapore's mandatory savings scheme. Both employee and employer contribute a percentage of salary. |
| **OA** | Ordinary Account. Usable for housing, insurance, investment, education. |
| **SA** | Special Account. Retirement savings, higher interest, restricted use. |
| **MA** | MediSave Account. Medical expenses and approved health insurance. |
| **RA** | Retirement Account. Created at 55 from OA+SA to fund retirement payouts. |
| **OW** | Ordinary Wage — monthly salary, subject to a monthly CPF ceiling. |
| **AW** | Additional Wage — bonuses and commissions, subject to an annual ceiling. |
| **BHS** | Basic Healthcare Sum — the MA cap. Excess overflows to SA/RA. |
| **FRS** | Full Retirement Sum — the headline retirement savings target. |
| **BRS** | Basic Retirement Sum — the lower target, roughly half of FRS. |
| **CPFIS** | CPF Investment Scheme — lets you invest OA/SA above set thresholds. |
| **Top-up** | Voluntary contribution, typically to SA/RA or MA, which attracts tax relief. |

## Singapore general

| Term | Meaning |
|---|---|
| **Take-home / nett pay** | Gross salary minus employee CPF. What's actually spendable. |
| **IRAS** | Inland Revenue Authority of Singapore — the tax authority. |
| **Integrated Shield Plan** | Private insurance layered on top of MediShield Life for hospitalisation. |
| **DBS / OCBC / UOB** | The three major local banks. Statement CSV import must handle all three. |
| **Huat** | 發/发, Hokkien — "to prosper". The product name. See `docs/decisions/0005`. |

## Product

| Term | Meaning |
|---|---|
| **Pot** | A category or goal balance that accumulates — base amount plus carried-over underspend. |
| **Rollover** | Month-end behaviour for unused budget: auto-carry, ask, or reset. |
| **Sinking fund** | A budget category used to accumulate toward a known future cost rather than to spend monthly. |
| **BYOK** | Bring Your Own Key — the user supplies their own AI API key. See `docs/decisions/0004`. |
| **Local-first** | All data lives on-device; no server in v1. See `docs/decisions/0003`. |
| **Digest** | A scheduled AI-written summary of the user's financial position. |
