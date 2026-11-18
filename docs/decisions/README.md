# Decisions

One per file, `NNNN-slug.md`, sequential. **Append-only** — to change, write a new ADR and
set old status to `Superseded by NNNN`. Only for decisions costly to reverse.
**Read this index; open an ADR only when relevant.**

| # | Decision | Gist | Status |
|---|---|---|---|
| [0001](0001-expo-react-native.md) | Expo / React Native from day one | One codebase iOS/Android/web; solo dev | Accepted |
| [0002](0002-ios-first-then-web.md) | iOS → web → Android | Phone-first design; Sign in with Apple required | Accepted |
| [0003](0003-local-first-sqlite.md) | Local-first SQLite + repository layer | Privacy, no backend; no backup/sync yet | Accepted |
| [0004](0004-byok-ai.md) | BYOK for all AI | No inference cost; rule alerts work keyless | Accepted |
| [0005](0005-name-huat.md) | Name: Huat | SG-warm; doesn't travel, accepted | Accepted |
| [0006](0006-repo-as-second-brain.md) | Repo = cross-session second brain | Living docs / append-only history / dated reference | Accepted |
| [0007](0007-terse-docs-generated-handbook.md) | Terse working docs + generated pretty handbook | Save context; AI never reads handbook | Accepted |

## Template
```markdown
# NNNN — <decision>
**Status:** Accepted | Proposed | Superseded by NNNN · **Date:** YYYY-MM-DD
## Context
## Decision
## Consequences
## Alternatives
```
