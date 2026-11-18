# 0001 — Expo / React Native, cross-platform from day one

**Status:** Accepted
**Date:** 2026-11-18 (decided earlier; recorded on this date)

## Context
Huat targets iOS first but web and Android are both planned. Jerry is building it
solo with AI assistance, so maintaining separate native codebases isn't realistic.

## Decision
Build on Expo / React Native from the first line of code, rather than writing a
native iOS app and porting later.

## Consequences
- One codebase serves iOS, Android and web.
- Expo handles the build and release machinery that would otherwise eat solo-dev time.
- Accepts a performance ceiling below native. For a finance app that is mostly lists,
  forms and charts, this is not a real constraint.
- Anything needing a native module may require an Expo config plugin or a dev build.
  Keychain/secure storage and local SQLite are all well supported.

## Alternatives considered
- **Native Swift first** — best iOS result, but makes web and Android a rewrite.
- **Flutter** — comparable capability; React/TypeScript is the more familiar and
  better AI-supported ecosystem.
