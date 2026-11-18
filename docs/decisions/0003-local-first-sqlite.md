# 0003 — Local-first SQLite with a cloud-ready repository layer

**Status:** Accepted
**Date:** 2026-11-18 (decided earlier; recorded on this date)

## Context
The app holds salary, CPF balances, full transaction history and insurance documents
— about as sensitive as personal data gets. Jerry wants no server to run or secure
in v1, but doesn't want to foreclose on sync across devices.

## Decision
Store everything in SQLite on the device. No data leaves the phone in v1 (the one
exception is AI calls, see 0004). All data access goes through a clean
data/repository layer so a sync backend can be added without touching feature code.

## Consequences
- Strongest possible privacy story, and no backend cost or operational burden.
- No cross-device sync, and **no backup** — losing the phone loses the data. An
  export/import path is needed early; this is a real v1 gap to confirm.
- The repository layer must be respected from the start. Feature code reaching
  straight into SQLite is the one thing that would make later sync a rewrite.
- Adding sync later means confronting conflict resolution, which is deferred, not solved.

## Alternatives considered
- **Cloud backend from day one** — gives sync and backup immediately, but means
  running a server holding highly sensitive financial data, for a pre-validation product.
- **Device-encrypted cloud (e.g. iCloud/CloudKit)** — attractive middle ground; ties
  the architecture to Apple, which conflicts with 0001/0002.
