# Dual Repo Architecture

## Purpose

Separate the Agents Knowledge DB system repository from the governed data repository.

## Repositories

### System repository

Agents Knowledge DB system repository  
Current repository slug may still be `obsidian-vault-governance-kit` until renamed.

Owns:

- governance kernel
- interfaces
- planning
- DBMS rules
- schemas
- skills
- templates
- tooling

### Data repository

Any governed data repository, for example:

- `your-governed-vault`

Owns:

- real knowledge data
- local registry
- local reports
- local state
- local overrides
- read-only snapshot of the system release

## Data Repository Read Order

1. local `RULES.md`
2. `.dbms-system/`
3. `LocalOverrides/`
4. `.knowledge-registry/`

## Why snapshots instead of direct repo reads

- better portability
- stable versioning
- no cross-repo path dependency
- easier upgrade review

## Product Framing

Agents Knowledge DB is the combined model:

- system repository
- data repository
- snapshot boundary
- local override layer

This repository contains only the system side.
