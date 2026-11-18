# Decisions

One decision per file: `NNNN-slug.md`, numbered in sequence. **Append-only** — never
edit or delete a past decision. To change your mind, write a new ADR and set the old
one's status to `Superseded by NNNN`.

A decision belongs here when reversing it would cost real work. Everyday choices
don't need an ADR.

| # | Decision | Status |
|---|---|---|
| [0001](0001-expo-react-native.md) | Expo / React Native, cross-platform from day one | Accepted |
| [0002](0002-ios-first-then-web.md) | iOS first, then web, Android last | Accepted |
| [0003](0003-local-first-sqlite.md) | Local-first SQLite with a cloud-ready repository layer | Accepted |
| [0004](0004-byok-ai.md) | Bring-your-own-key for all AI features | Accepted |
| [0005](0005-name-huat.md) | Name the product "Huat" | Accepted |
| [0006](0006-repo-as-second-brain.md) | Use this repo as the cross-session second brain | Accepted |

## Template

```markdown
# NNNN — <decision>

**Status:** Accepted | Proposed | Superseded by NNNN
**Date:** YYYY-MM-DD

## Context
What situation forced a choice.

## Decision
What we chose, stated plainly.

## Consequences
What this makes easy, and what it makes hard or expensive later.

## Alternatives considered
What else was on the table and why it lost.
```
