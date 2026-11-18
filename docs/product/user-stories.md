# User stories

10 epics. Format: **ID · want → why · acceptance criteria.** Actor is "user" unless noted.

## 1. Onboarding & profile (ONB)
| ID | Story | AC |
|---|---|---|
| ONB-01 | New user enters DOB + gross monthly salary → auto CPF + take-home | CPF + take-home shown immediately. Age bracket from DOB. |
| ONB-02 | New user enters OA/SA/MA balances → accurate milestone projection | Optional; default $0. Editable later. |
| ONB-03 | New user guided through first budget categories → not an empty app | Preset suggestions; accept, skip or customise before finishing. |
| ONB-04 | New user optionally connects AI key → AI ready day one | Stored locally. Onboarding completes without it; AI shows "connect key to unlock". |
| ONB-05 | Returning user skips completed steps → not re-asked | Per-step completion state. Settings edit individual fields. |
| ONB-06 | Sign in with Google/Apple → no separate account | Google SSO + Sign in with Apple (required for App Store). Token in Keychain. Account auto-created on first sign-in. |

## 2. Dashboard (DSH)
| ID | Story | AC |
|---|---|---|
| DSH-01 | Take-home vs spend this month → know if on track | Gross, CPF deduction, take-home, total spent. Remaining spendable prominent. |
| DSH-02 | Top budget categories + usage → spot overspend | Top 3–5 w/ progress bars. Over-budget visually distinct. |
| DSH-03 | Active goals + progress → motivation | Name, % complete, saved vs target, projected date. |
| DSH-04 | This month's CPF summary → full comp picture | Employee, employer, per-account (OA/SA/MA). |
| DSH-05 | Quick-add FAB → log expense without navigating | Minimal sheet: amount, category, optional budget link, note. One-tap save. Budget pre-filled if category maps to active budget. |
| DSH-06 | Active alerts on dashboard → see important items | Up to 3 most recent/urgent; tap → detail. |

## 3. Transactions (TXN)
| ID | Story | AC |
|---|---|---|
| TXN-01 | Manual add (amount, date, category, note) → log cash/card | Appears immediately. Date defaults today. Category picker w/ search. |
| TXN-02 | Upload CSV statement → fill gaps without replacing manual entries | DBS/OCBC/UOB. Match vs manual by amount + date (±3 days). Review groups: Matched (skipped), New (added), Unmatched manual (e.g. cash). User can override before confirm. Budget period by **transaction** date, not posting date. |
| TXN-09 | Prior-month rows apply to that month's budget retroactively → accurate history | Flagged in review ("applies to May's budget"). Past budgets adjusted. Post-import summary of retro changes. |
| TXN-10 | Review/override matching before confirm → fix bad matches, force duplicates | Pairs side by side. Unmatch (imports both) or manually match. Confirmed matches never double-counted. |
| TXN-03 | AI auto-categorises imports → no manual tagging | Suggested category per row; overridable. Corrections remembered for similar merchants. |
| TXN-04 | AI generates category tree from imports → fits real spending | After first import, proposes tree from merchant patterns; accept/merge/delete. |
| TXN-05 | Grouped by day w/ running total → see rhythm | Chronological, date-grouped. Month selector. Smooth scroll back through months. |
| TXN-06 | Search/filter by category, date range, amount | Category multi-select, date range, min/max. Live results. |
| TXN-07 | Split across categories → accurate mixed purchases | Long-press/swipe → Split. Parts must sum to total. |
| TXN-08 | Mark recurring → anticipate future months | Links to schedule (monthly, weekly, …). Placeholders created in future months. |

## 4. Budgets (BUD)
| ID | Story | AC |
|---|---|---|
| BUD-01 | Create category budget w/ monthly base → a limit | Requires category, base, month-end behaviour. Appears in list immediately. |
| BUD-02 | Auto-rollover unused → underspend rewarded | Month end: remainder added to next month. Running balance on card. |
| BUD-03 | Month-end prompt → decide in context | 1st of month, per "Ask me" budget: roll over / move to goal / reset. |
| BUD-04 | Reset monthly → fixed limit | Resets to base on the 1st. No carryover. |
| BUD-05 | Progress bar spent vs remaining → self-regulate | Amber at 80%, red at 100%. Exact spent / total available below bar. |
| BUD-06 | Edit/delete anytime | Edits apply to future months by default; option for current month. Delete confirms. |
| BUD-07 | Month-over-month trend → see patterns | Detail view: bar chart last 6 months + average. |

## 5. Goals (GOL)
| ID | Story | AC |
|---|---|---|
| GOL-01 | Create goal: name, target, monthly contribution | Those 3 required. Target date optional (auto-calculated if absent). |
| GOL-02 | Projected completion date → adjust to hit deadline | Updates live when contribution changes. |
| GOL-03 | Notify when fully funded → time to buy | Push when saved ≥ target. Card shows "Ready to redeem". |
| GOL-04 | One-off extra contributions → windfalls accelerate | "Add funds" on detail; logged w/ date + note. |
| GOL-05 | Pause contribution → redirect without deleting | Stops monthly deduction from spendable. "Paused" badge. |
| GOL-06 | Mark redeemed → archived as complete | "Mark as purchased"; moves to archive w/ purchase date. |

## 6. CPF (CPF)
| ID | Story | AC |
|---|---|---|
| CPF-01 | Salary once → employee, employer, take-home | Age-bracket rates + $8k OW ceiling. Breakdown card. |
| CPF-02 | Split across OA/SA/MA (+RA if 55+) → where money goes | Per-account $ + allocation % for age bracket. |
| CPF-03 | Log bonus separately → correct AW-ceiling CPF | AW ceiling ≈ $102k − OW contributed YTD. Shown separately from monthly CPF. |
| CPF-04 | Enter current balances → milestone tracking | OA, SA, MA (+RA). Projected monthly growth from contributions. |
| CPF-05 | Progress to BHS ($79k) → know when MA overflows, and where | Bar + projected "BHS reached" date. Overflow explanation below. |
| CPF-06 | Progress to FRS ($220.4k) → retirement readiness | SA+RA vs FRS bar. Projected age FRS reached. |
| CPF-07 | When OA crosses $20k → CPFIS eligibility | Milestone card; projected date if not reached. |
| CPF-08 | Top-up tax relief headroom left this year → decide on cash top-up | $8k cap − logged top-ups. Resets 1 Jan. |
| CPF-09 | Extra 1% on first $60k combined → see compounding | If combined < $60k: extra interest YTD + amount still eligible. |

## 7. Insurance (INS)
| ID | Story | AC |
|---|---|---|
| INS-01 | Add policy: name + document → start tracking | Free-form name. PDF/image upload. Appears in list immediately. |
| INS-02 | AI extracts type, coverage, premium → less manual entry | Classifies: Health (ISP), Life, CI, DI, ILP, General. User confirms extracted fields before save. |
| INS-03 | Track premiums paid → running cost | Each payment logged w/ date + amount. Detail: total paid + history. |
| INS-04 | Plain-language coverage summary → understand what I pay for | AI-generated per policy from the document. |
| INS-05 | Unified coverage view → protection at a glance | Home: summary card per type (health, life, CI, DI). Gaps where no policy. |
| INS-06 | Flag gaps vs life stage + goals → under-insured? | AI compares goals + income + age vs coverage. Recommendations (e.g. "No DI coverage detected"). |
| INS-07 | Premium reminder → never miss payment | Frequency (monthly/annual) + due date. Notify X days before (configurable). |
| INS-08 | Total annual insurance spend → over/under-spending? | Total annual premiums; benchmark vs rule of thumb (e.g. 5–10% of income). |

## 8. AI & insights (AI)
| ID | Story | AC |
|---|---|---|
| AI-01 | Connect own key (OpenAI/Anthropic/Google/…) → control cost + model | Settings field. Validated by test call. Keychain/secure storage. |
| AI-02 | Choose digest frequency (on-demand/weekly/monthly/biannual) | Picker in settings. On-demand = manual trigger. Scheduled → notification. |
| AI-03 | Holistic digest | Sections: spending, budget performance, goals, CPF, insurance, recommendations. |
| AI-04 | Chat with context ("on track for MacBook?") | Full financial context via system prompt. Answers cite user's data, not generic advice. |
| AI-05 | Standard system prompt across models → consistent output | App-managed: profile, salary/CPF, budgets, goals, insurance. Not user-editable; user can add personal note/preference. |
| AI-06 | Rule alerts without a key → works out of the box | Local engine: budget %, large txns (>$X), consecutive overspend months, savings rate below target. |
| AI-07 | Category overspend vs income + goals → actionable advice | Flags outlier category %; names category + suggested adjustment. |

## 9. Notifications (NOT)
| ID | Story | AC |
|---|---|---|
| NOT-01 | Alert at 80% of a budget → slow down | Configurable, default 80%. Includes category, spent, remaining. |
| NOT-02 | Goal fully funded | Once, when saved first ≥ target. Not repeated unless goal reset. |
| NOT-03 | CPF milestone hit (BHS, FRS, investment threshold) | One-time per milestone; brief explanation. |
| NOT-04 | Premium due reminder | Default 7 days before; per-policy 3/7/14/30. |
| NOT-05 | Month-end prompt for "Ask me" budgets | Last day of month (or 1st). Lists each budget, remainder, options. |
| NOT-06 | Control which notifications + how → not overwhelmed | Per-type toggles. Quiet hours X–Y. |

## 10. Settings & data (SET)
| ID | Story | AC |
|---|---|---|
| SET-01 | Update salary/DOB anytime → CPF stays accurate | Effective from current month. History not retroactively altered. |
| SET-02 | Export all data CSV/JSON → backup, portability | Transactions, budgets, goals, CPF inputs, insurance. Single file. |
| SET-03 | Manage categories (add/rename/merge/delete) | Manager screen. Merge moves txns. Delete prompts reassign. |
| SET-04 | Biometric lock (Face ID/Touch ID) | On app open. Optional toggle. Falls back to device PIN. |
| SET-05 | Cloud-ready data → future sync across devices | Repository pattern over local storage; sync = swap storage adapter. |
