# 0002 — iOS first, then web, Android last

**Status:** Accepted
**Date:** 2026-11-18 (decided earlier; recorded on this date)

## Context
Limited solo capacity means platforms must be sequenced rather than launched together.

## Decision
iOS first. Web app shortly after. Android on a longer horizon.

## Consequences
- Design and interaction decisions are made against a phone screen first; the web app
  will need a genuine responsive/desktop pass rather than a straight port.
- Sign in with Apple is required from the start for App Store compliance.
- Android-specific issues stay undiscovered for a long time. Keeping to cross-platform
  Expo APIs where possible limits the eventual surprise.

## Alternatives considered
- **Web first** — faster to ship and easier to iterate, but the product is a daily
  mobile habit; a web-first version would misjudge the core interactions.
