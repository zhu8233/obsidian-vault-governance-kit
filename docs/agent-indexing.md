# Agent Indexing

## Purpose

Provide a DBMS-maintained materialized index for agent audit and whole-vault scanning.

## Two Layers

### Governance registry

`.knowledge-registry/vault-registry.json` remains the source of truth for:

- topics
- governed object identity
- adapters

### DBMS materialized index

`01-Workflow/Knowledge-Governance/DBMS/index/` stores derived scan artifacts:

- `file-index.jsonl`
- `topic-summary.json`
- `findings.json`
- `../state/last-index-run.json`

The index is not a second source of truth. It is a scan view maintained by `db-admin-agent`.

## Read Order For Audit And Scan Tasks

When an agent is performing audit, scan, registry repair, or DBMS review work, read in this order:

1. `RULES.md`
2. `.dbms-system/RULES.md`
3. `.knowledge-registry/vault-registry.json`
4. `01-Workflow/Knowledge-Governance/DBMS/state/last-index-run.json`
5. `01-Workflow/Knowledge-Governance/DBMS/index/file-index.jsonl`
6. `01-Workflow/Knowledge-Governance/DBMS/index/findings.json`

## Rebuild Model

- default maintainer: `db-admin-agent`
- default task type: `index_rebuild`
- default cadence: periodic or on-demand full rebuild
- default risk: `L1-L2`

## Finding Types

The first release classifies:

- `unregistered_file`
- `registry_missing_file`
- `duplicate_registry_path`
- `layer_path_mismatch`
- `topic_unresolved`
- `frontmatter_missing`
- `protected_zone_unexpected_file`
- `canonical_orphan_index`

## Design Boundary

- file coverage is whole-vault
- index depth is metadata-only
- non-text objects may be indexed without deep content parsing
- registry facts always win over derived index state
