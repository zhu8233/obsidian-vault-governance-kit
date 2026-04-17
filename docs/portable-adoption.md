# Portable Adoption Guide

## What to Copy

Copy `templates/vault-root/` into the root of the target vault.

## What to Customize

- absolute and relative paths
- local project folders
- topic naming conventions
- agent platform adapter notes
- human owner identity

## What Should Stay Stable

- layer model
- registry schemas
- promotion workflow
- ledger semantics
- skill responsibilities

## Recommended Rollout

1. Install root rules and registry files
2. Add compatibility adapters (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`)
3. Define the first 3-5 topics in the registry
4. Route one ingestion workflow through the model
5. Add canonical promotion only after the team is comfortable with intake and curation

## Migration Advice

- Do not migrate the entire vault at once
- Start with the highest-value topics
- Backfill frontmatter gradually
- Prefer registry-first stabilization before deep note refactors
