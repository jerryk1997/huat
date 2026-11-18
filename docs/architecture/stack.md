# Stack

Decided at platform/data level; nothing scaffolded. Read the ADR before proposing changes.

| Layer | Choice | ADR |
|---|---|---|
| Framework | Expo / React Native | 0001 |
| Language | TypeScript | — |
| Platform order | iOS → web → Android | 0002 |
| Local DB | SQLite on device | 0003 |
| Data access | Repository layer over SQLite | 0003 |
| Secrets | iOS Keychain / platform secure storage | 0003 |
| AI | User's own OpenAI/Anthropic/Google key | 0004 |
| Auth | Google SSO + Sign in with Apple | — |
| Backend | None in v1 | 0003 |

## The one rule
**Feature code never touches SQLite directly** — only via the repository layer. Keeps
"add sync later" from being a rewrite; must hold from the first screen.

## PROPOSED / undecided
- ORM/query: Drizzle vs Prisma vs raw SQL on `expo-sqlite`. Migrations > ergonomics —
  financial history can't be dropped/recreated.
- State: React Query over repository layer — obvious, unexamined.
- Charts: must work on RN + web; narrows options.
- Export/import: needed early (no backup, 0003). Likely CSV + full JSON dump.
- Auth w/o backend gives identity, not sync. Does v1 need sign-in beyond App Store
  expectations?
