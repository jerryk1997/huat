# 0004 — Bring-your-own-key for all AI features

**Status:** Accepted
**Date:** 2026-11-18 (decided earlier; recorded on this date)

## Context
AI categorisation, document parsing, digests and chat all need a model. Paying for
inference on behalf of users means a backend, a billing relationship and per-user
cost — before the product is validated.

## Decision
Users connect their own OpenAI / Anthropic / Google API key. The app injects the
user's financial context into a standardised system prompt so behaviour stays
consistent across providers. Rule-based alerts (budget thresholds, large
transactions, savings rate) are always on and need no key at all.

## Consequences
- No inference cost and no AI backend to operate.
- Every AI feature must degrade gracefully to a "connect a key to unlock" state, and
  the rule-based layer has to carry real value on its own.
- Narrows the audience: most people don't have an API key. Acceptable for v1, and a
  managed option can be added later without changing the architecture.
- The key is stored on-device and must never be logged or synced.
- A standardised system prompt across providers needs testing per provider; "works on
  Claude" does not mean "works on GPT".

## Alternatives considered
- **App-provided inference** — far better UX, but requires a backend, billing, and
  absorbing abuse risk pre-validation.
- **On-device models** — no cost and no data leaving the phone, but quality is not yet
  good enough for statement categorisation or document extraction.
