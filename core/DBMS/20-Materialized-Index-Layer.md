# Materialized Index Layer

The DBMS may maintain a derived file index for audit and scan tasks.

## Purpose

Separate:

- durable governance facts in `.knowledge-registry/`
- derived runtime scan state in `DBMS/index/`

## Default Maintainer

`db-admin-agent`

## Standard Outputs

- `DBMS/index/file-index.jsonl`
- `DBMS/index/topic-summary.json`
- `DBMS/index/findings.json`
- `DBMS/state/last-index-run.json`
- DBMS audit report

## Rule

The materialized index is derived state.

It helps agents:

- find unregistered files
- compare path and layer expectations
- inspect protected-zone drift
- audit topic coverage without rescanning everything manually

It does not replace the governance registry.
