# Stack

Decided at the level of platform and data strategy. Nothing is scaffolded yet.
Each choice below links to the ADR holding the reasoning — read those before
proposing a change.

| Layer | Choice | ADR |
|---|---|---|
| App framework | Expo / React Native | [0001](../decisions/0001-expo-react-native.md) |
| Language | TypeScript | — |
| Platform order | iOS → web → Android | [0002](../decisions/0002-ios-first-then-web.md) |
| Local database | SQLite on device | [0003](../decisions/0003-local-first-sqlite.md) |
| Data access | Repository layer over SQLite | [0003](../decisions/0003-local-first-sqlite.md) |
| Secrets | iOS Keychain / platform secure storage | [0003](../decisions/0003-local-first-sqlite.md) |
| AI | User's own OpenAI / Anthropic / Google key | [0004](../decisions/0004-byok-ai.md) |
| Auth | Google SSO + Sign in with Apple | — |
| Backend | None in v1 | [0003](../decisions/0003-local-first-sqlite.md) |

## The one rule that matters

**Feature code must never touch SQLite directly.** Everything goes through the
repository layer. This is what keeps "add cloud sync later" from becoming a rewrite —
and it only works if it's respected from the first screen, because retrofitting it
means touching every feature.

## Undecided — PROPOSED only

These are open; no commitment has been made. Don't treat any as settled.

- **ORM / query layer** — Drizzle, Prisma, or hand-written SQL over `expo-sqlite`.
  Migrations matter more than ergonomics here: financial history can't be dropped
  and recreated.
- **State management** — React Query over the repository layer is the obvious shape,
  but unexamined.
- **Charting** — needs to work on both React Native and web; this constrains the
  options sharply.
- **Export / import format** — needed early given there is no backup (see 0003).
  CSV plus a full JSON dump is the likely answer.
- **Auth with no backend** — SSO without a server mostly gives identity, not sync.
  Worth questioning whether v1 needs sign-in at all, beyond App Store expectations.
