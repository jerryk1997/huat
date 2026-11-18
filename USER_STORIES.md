# User Stories

## Epic 1 — Onboarding & Profile Setup

| ID | User Story | Acceptance Criteria |
|----|-----------|---------------------|
| ONB-01 | As a new user, I want to enter my date of birth and gross monthly salary so that the app can calculate my CPF contributions and take-home pay automatically. | CPF contribution amounts and take-home are shown immediately after entry. Age bracket is derived from DOB. |
| ONB-02 | As a new user, I want to enter my current CPF account balances (OA, SA, MA) so that the app can project my milestone progress from an accurate starting point. | Balances are optional — app works with $0 as default. Balances can be edited later. |
| ONB-03 | As a new user, I want to be walked through creating my first budget categories so that I don't start with an empty app. | App offers pre-set category suggestions. User can accept, skip, or customise before finishing onboarding. |
| ONB-04 | As a new user, I want to optionally connect my AI API key during onboarding so that AI features are ready from day one. | Key is stored locally. Onboarding can be completed without it — AI features show a "connect key to unlock" state. |
| ONB-05 | As a returning user, I want to be able to skip onboarding steps I've already completed so that I'm not re-asked for information the app already has. | Each onboarding step tracks completion state. Revisiting settings allows editing individual fields. |
| ONB-06 | As a new user, I want to sign in with Google or Apple so that I don't have to create and remember a separate account. | Google SSO and Sign in with Apple both supported. Sign in with Apple required for iOS App Store compliance. Auth token stored securely in Keychain. Account created automatically on first sign-in. |

---

## Epic 2 — Dashboard

| ID | User Story | Acceptance Criteria |
|----|-----------|---------------------|
| DSH-01 | As a user, I want to see my take-home pay vs total spending this month at a glance so that I know immediately if I'm on track. | Shows gross salary, CPF deduction, take-home, and total spent. Remaining spendable amount is prominent. |
| DSH-02 | As a user, I want to see a summary of my top budget categories and how much I've used so that I can quickly spot where I'm overspending. | Shows top 3–5 categories with progress bars. Over-budget categories are visually distinct. |
| DSH-03 | As a user, I want to see all my active savings goals and their progress so that I stay motivated and aware. | Each goal shows name, % complete, amount saved vs target, and projected completion date. |
| DSH-04 | As a user, I want to see my CPF contribution for the current month summarised so that I understand my total compensation picture. | Shows employee deduction, employer contribution, and per-account allocation (OA/SA/MA). |
| DSH-05 | As a user, I want a quick-add button on the dashboard so that I can log a manual expense without navigating away. | Tapping FAB opens a minimal transaction entry sheet (amount, category, optional budget link, note). Saves in one tap. UI detail: budget field is optional and pre-filled if the selected category maps to an active budget. |
| DSH-06 | As a user, I want the dashboard to surface any active alerts (over-budget, insurance due, goal reached) so that I see important things without checking every section. | Alert feed shows up to 3 most recent/urgent items. Each is tappable to navigate to the relevant detail. |

---

## Epic 3 — Transactions

| ID | User Story | Acceptance Criteria |
|----|-----------|---------------------|
| TXN-01 | As a user, I want to manually add a transaction (amount, date, category, note) so that I can log cash or card expenses not in my bank statement. | Transaction appears immediately in the list. Date defaults to today. Category picker shows full list with search. |
| TXN-02 | As a user, I want to upload a CSV bank statement so that the app can fill in transactions I missed without replacing the ones I already entered manually. | App accepts CSV from major SG banks (DBS, OCBC, UOB). On import, app matches rows against existing manual entries by amount + date (±3 day tolerance). Review screen shows three groups: Matched (already in app — skipped), New (will be added), Unmatched manual entries (in app but not in statement, e.g. cash). User can override any match before confirming. App uses transaction date (not posting date) for budget period assignment. |
| TXN-09 | As a user, I want transactions from an imported statement that fall in a previous month to be applied to that month's budget retroactively so that my historical budget periods remain accurate. | "Late arriving" transactions are flagged in the review screen with a note (e.g. "This will be applied to May's budget"). Past month budgets are adjusted accordingly. A summary of retroactive changes is shown after import. |
| TXN-10 | As a user, I want to review and override the app's transaction matching before confirming an import so that I can fix incorrect matches or force-add a duplicate if needed. | Each matched pair is shown side by side (manual entry vs statement row). User can unmatch a pair (imports both), or manually match an unmatched entry to a statement row. Confirmed matches are never double-counted. |
| TXN-03 | As a user, I want the app to auto-categorise imported transactions using AI so that I don't have to tag every line manually. | Each transaction is assigned a suggested category. User can override any assignment. Corrections are remembered for similar merchants. |
| TXN-04 | As a user, I want to let AI generate custom categories and sub-categories from my imported transactions so that the category structure fits my actual spending. | After first import, AI proposes a category tree based on merchant patterns. User can accept, merge, or delete suggestions. |
| TXN-05 | As a user, I want to view my transactions grouped by day with a running total so that I can see my spending rhythm clearly. | Default view is chronological, grouped by date. Month selector at top. Scrolling back through months is smooth. |
| TXN-06 | As a user, I want to search and filter transactions by category, date range, or amount so that I can find specific items quickly. | Filter panel with category multi-select, date range picker, and min/max amount fields. Results update in real time. |
| TXN-07 | As a user, I want to split a transaction across multiple categories so that shared or mixed-purpose purchases are tracked accurately. | Long-press or swipe on a transaction reveals a "Split" option. Split amounts must sum to the original total. |
| TXN-08 | As a user, I want to mark a transaction as a recurring expense so that the app can anticipate it in future months. | Recurring flag links the transaction to a schedule (monthly, weekly, etc.). App creates a placeholder in future months. |

---

## Epic 4 — Budgets

| ID | User Story | Acceptance Criteria |
|----|-----------|---------------------|
| BUD-01 | As a user, I want to create a budget for a spending category with a monthly base amount so that I have a spending limit to work toward. | Budget creation requires: category, base amount, and end-of-month behavior. Saved budget appears in the budget list immediately. |
| BUD-02 | As a user, I want to set a budget to auto-rollover unused amounts so that underspending in one month rewards me in the next. | At month end, remaining balance is automatically added to next month's budget. Running balance is visible on the budget card. |
| BUD-03 | As a user, I want to be prompted at month end about what to do with unused budget amounts so that I can decide in context rather than set a fixed rule. | On the first day of a new month, a prompt appears for each "Ask me" budget: options are roll over, move to a goal, or reset. |
| BUD-04 | As a user, I want to set a budget to reset each month so that my limit is always fixed regardless of past spending. | Balance resets to base amount on the 1st of each month. No carryover. |
| BUD-05 | As a user, I want to see a visual progress bar for each budget showing how much I've spent vs remaining so that I can self-regulate at a glance. | Bar turns amber at 80%, red at 100%. Exact amounts shown below the bar (spent / total available). |
| BUD-06 | As a user, I want to edit or delete a budget at any time so that my limits stay relevant as my life changes. | Editing changes future months only by default, with an option to apply to current month. Deleting asks for confirmation. |
| BUD-07 | As a user, I want to see a month-over-month trend for each budget category so that I can understand my spending patterns over time. | Tapping a budget card opens a detail view with a bar chart of the last 6 months and a spend average. |

---

## Epic 5 — Goals (Savings)

| ID | User Story | Acceptance Criteria |
|----|-----------|---------------------|
| GOL-01 | As a user, I want to create a savings goal with a name, target amount, and monthly contribution so that I can work toward a specific purchase over time. | Goal creation requires: name, target amount, monthly contribution. Optional: target date (auto-calculated if not provided). |
| GOL-02 | As a user, I want to see a projected completion date for each goal based on my monthly contribution so that I can adjust contributions to hit a deadline. | Projected date updates dynamically if contribution amount changes. |
| GOL-03 | As a user, I want to receive a notification when a goal is fully funded so that I know it's time to make the purchase. | Push notification fires when accumulated savings >= target amount. Goal card shows a "Ready to redeem" state. |
| GOL-04 | As a user, I want to make one-off additional contributions to a goal so that windfalls (bonus, gift) can accelerate my progress. | "Add funds" option on goal detail. Amount is logged as a contribution with a date and note. |
| GOL-05 | As a user, I want to pause a goal's monthly contribution so that I can temporarily redirect funds without deleting the goal. | Pausing stops the monthly deduction from spendable income. Goal remains visible with a "Paused" badge. |
| GOL-06 | As a user, I want to mark a goal as redeemed when I've made the purchase so that the app records it as completed and archives it. | "Mark as purchased" action. Goal moves to a completed archive with purchase date logged. |

---

## Epic 6 — CPF Tracking

| ID | User Story | Acceptance Criteria |
|----|-----------|---------------------|
| CPF-01 | As a user, I want to enter my gross monthly salary once and have the app calculate my employee CPF deduction, employer contribution, and take-home pay so that I understand my full compensation. | Calculation uses age-bracket rates and the $8,000 OW ceiling. All figures shown in a breakdown card. |
| CPF-02 | As a user, I want to see exactly how my monthly CPF contribution is split across OA, SA, MA (and RA if 55+) so that I understand where my money is going. | Per-account dollar amounts shown alongside allocation percentages for the user's age bracket. |
| CPF-03 | As a user, I want to log a bonus payment separately so that the app calculates the correct CPF contribution using the Additional Wage (AW) ceiling. | User inputs bonus amount. App calculates AW ceiling (≈$102k - OW contributed YTD). CPF on AW is shown separately from monthly CPF. |
| CPF-04 | As a user, I want to input my current CPF account balances so that the app can track my progress toward key milestones. | Balance input for OA, SA, MA (and RA if applicable). App derives projected monthly growth from contribution amounts. |
| CPF-05 | As a user, I want to see my progress toward the MediSave BHS ($79,000) so that I know when my MA will overflow and where the excess will flow. | Progress bar with projected "BHS reached" date. Explanation of overflow behavior shown below. |
| CPF-06 | As a user, I want to see my progress toward the Full Retirement Sum (FRS, $220,400) so that I can assess my retirement readiness. | Progress bar for SA+RA balance vs FRS. Projected age at which FRS will be reached shown. |
| CPF-07 | As a user, I want to know when my OA balance will cross $20,000 so that I know when I become eligible to invest via CPFIS. | Milestone card in CPF section. Projected date shown if not yet reached. |
| CPF-08 | As a user, I want to see how much voluntary top-up tax relief headroom I have remaining this year so that I can decide whether to make a cash top-up before year end. | Shows $8,000 annual cap minus any top-ups logged. Resets on 1 Jan each year. |
| CPF-09 | As a user, I want to see the extra 1% interest I'm earning on my first $60,000 of combined CPF balances so that I understand the compounding benefit. | If combined balance < $60k, shows the extra interest earned YTD and the amount still eligible. |

---

## Epic 7 — Insurance

| ID | User Story | Acceptance Criteria |
|----|-----------|---------------------|
| INS-01 | As a user, I want to add an insurance policy by giving it a name and uploading a document so that the app can start tracking it. | Free-form name field. Document upload accepts PDF and image files. Policy appears in the insurance list immediately. |
| INS-02 | As a user, I want the app to use AI to parse my uploaded insurance document and extract the policy type, coverage details, and premium amount so that I don't have to enter everything manually. | AI classifies policy into: Health (ISP), Life, Critical Illness, Disability Income, ILP, or General. Extracted fields shown for user confirmation before saving. |
| INS-03 | As a user, I want to track how much I've paid in premiums over time for each policy so that I have a running cost of my insurance portfolio. | Each premium payment is logged with date and amount. Policy detail shows total paid to date and payment history. |
| INS-04 | As a user, I want to see a summary of what each policy actually covers (in plain language) so that I understand what I'm paying for. | AI-generated plain-language coverage summary per policy, extracted from the uploaded document. |
| INS-05 | As a user, I want to see a unified view of all my coverage across policy types so that I can understand my overall protection at a glance. | Insurance home screen shows a coverage summary card per type (health, life, CI, DI). Gaps shown where no policy exists for a type. |
| INS-06 | As a user, I want the app to flag potential coverage gaps relative to my life stage and goals so that I can assess whether I'm under-insured. | AI compares stated goals + income + age against coverage held. Gaps surfaced as recommendations (e.g. "No disability income coverage detected"). |
| INS-07 | As a user, I want to set a payment reminder for each insurance premium so that I never miss a renewal or payment date. | User sets premium frequency (monthly, annual) and due date. Notification fires X days before (configurable). |
| INS-08 | As a user, I want to see a breakdown of my total annual insurance spend so that I can assess whether I'm over- or under-spending on protection. | Insurance section shows total annual premium spend across all policies. Benchmarked against a rule-of-thumb (e.g. 5–10% of income). |

---

## Epic 8 — AI & Insights

| ID | User Story | Acceptance Criteria |
|----|-----------|---------------------|
| AI-01 | As a user, I want to connect my own AI API key (OpenAI, Anthropic, Google, etc.) so that I control the cost and model used for analysis. | Key entry field in settings. App validates the key with a test call. Key stored in local secure storage (Keychain on iOS). |
| AI-02 | As a user, I want to choose the AI digest frequency (on-demand, weekly, monthly, biannual) so that I get insights at a cadence that suits me. | Frequency picker in settings. On-demand means the user manually triggers a report. Scheduled digests fire as a notification. |
| AI-03 | As a user, I want to receive a financial digest that analyses my spending, savings progress, CPF, and insurance in one report so that I get a holistic picture. | Digest is a structured report with sections: spending summary, budget performance, goal progress, CPF update, insurance notes, and AI recommendations. |
| AI-04 | As a user, I want to chat with an AI that has context about my financial data so that I can ask specific questions like "am I on track for my MacBook goal?" | Chat interface with full financial context injected via system prompt. Responses reference the user's actual data, not generic advice. |
| AI-05 | As a user, I want the AI to use a standardised system prompt regardless of which model I connect so that the behavior and output format stay consistent. | System prompt is app-managed and includes: user profile, salary/CPF summary, budget status, goals, insurance summary. User cannot edit the system prompt directly but can add a personal note/preference. |
| AI-06 | As a user, I want rule-based alerts to fire even when I haven't connected an AI key so that core smart features work out of the box. | Rule engine runs locally: budget % thresholds, large transactions (>$X), consecutive overspend months, savings rate below target. No API key required. |
| AI-07 | As a user, I want the AI to recommend whether I'm spending too much on a category relative to my income and goals so that I get actionable guidance. | AI compares category spend % against income and flags outliers. Recommendation includes the specific category and a suggested adjustment. |

---

## Epic 9 — Notifications

| ID | User Story | Acceptance Criteria |
|----|-----------|---------------------|
| NOT-01 | As a user, I want to receive an alert when I've spent 80% of a budget category so that I can slow down before hitting the limit. | Threshold is configurable (default 80%). Notification includes category name, amount spent, and amount remaining. |
| NOT-02 | As a user, I want to receive a notification when a savings goal is fully funded so that I know I can make the purchase. | Fires once when accumulated savings first meets or exceeds target. Not repeated unless goal is reset. |
| NOT-03 | As a user, I want to receive a notification when I hit a CPF milestone (BHS, FRS, investment threshold) so that I'm aware of the change in behaviour. | Milestone notifications are one-time per milestone. Include a brief explanation of what the milestone means. |
| NOT-04 | As a user, I want to receive a reminder before an insurance premium is due so that I don't miss a payment. | Default reminder: 7 days before. User can configure per policy (3 / 7 / 14 / 30 days). |
| NOT-05 | As a user, I want to receive a month-end prompt for budgets set to "ask me" so that I decide what to do with unused balances. | Fires on the last day of the month (or first of next month). Lists each "ask me" budget with remaining balance and options. |
| NOT-06 | As a user, I want to control which notifications I receive and how so that I'm not overwhelmed. | Per-notification-type toggles in settings. Option to set quiet hours (no notifications between X and Y). |

---

## Epic 10 — Settings & Data

| ID | User Story | Acceptance Criteria |
|----|-----------|---------------------|
| SET-01 | As a user, I want to update my salary or date of birth at any time so that CPF calculations stay accurate after a pay rise or correction. | Changes take effect from the current month. Historical calculations are not retroactively altered. |
| SET-02 | As a user, I want to export all my data as a CSV or JSON so that I have a backup and can move to another tool if needed. | Export includes: transactions, budgets, goals, CPF inputs, insurance records. Single file download. |
| SET-03 | As a user, I want to manage my custom transaction categories (add, rename, merge, delete) so that my category structure stays tidy over time. | Category manager screen. Merging moves all transactions from one category to another. Deleting prompts to reassign transactions. |
| SET-04 | As a user, I want the app to be secured with biometric authentication (Face ID / Touch ID) so that my financial data is protected if my phone is accessed by someone else. | Biometric lock on app open. Optional — user can enable/disable in settings. Falls back to device PIN. |
| SET-05 | As a user, I want the data architecture to be cloud-ready so that when I add a web or Android app, my data can sync across devices without re-entering everything. | Data layer uses a repository pattern abstracted from local storage. Cloud sync can be added by swapping the storage adapter. |
