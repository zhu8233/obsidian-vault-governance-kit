# Portable Adoption Guide

## What to Copy

Copy `templates/vault-root/` into the root of the target data vault.

## What to Customize

- absolute and relative paths
- local project folders
- topic naming conventions
- agent platform adapter notes
- human owner identity
- local overrides

## What Should Stay Stable

- layer model
- registry schemas
- promotion workflow
- ledger semantics
- skill responsibilities

## Recommended Rollout

1. Install root rules, registry files, `.dbms-system/`, and `LocalOverrides/`
2. Add compatibility adapters (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`)
3. Sync the system snapshot from the system repo into the data repo
4. Define the first 3-5 topics in the data repo registry
5. Route one ingestion workflow through the model
6. Add canonical promotion only after the team is comfortable with intake and curation

## Dual-repo principle

- system repo publishes the governance kernel
- data repo consumes a read-only snapshot
- local overrides stay small and explicit
- upgrades happen through DBA review, not automatic overwrite

## Migration Advice

- Do not migrate the entire vault at once
- Start with the highest-value topics
- Backfill frontmatter gradually
- Prefer registry-first stabilization before deep note refactors
