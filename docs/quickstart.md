# Quickstart

## Goal

Get a governed vault working with the least number of moving parts.

## Minimal install

Copy into the target vault:

- `templates/vault-root/RULES.md`
- one of `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`
- `templates/vault-root/.knowledge-registry/`
- `templates/vault-root/01-Workflow/Knowledge-Governance/DBMS/index/`

## Minimal setup

1. Add one human agent to `agent-roster.json`
2. Add one coordinator agent if needed
3. Register one real topic in `vault-registry.json`
4. Start with intake and curation only

## Minimal success criteria

- two different agents both read the same `RULES.md`
- both resolve the same `topic_id`
- both respect canonical write restrictions
- both append to the change ledger for meaningful work
- `db-admin-agent` can rebuild the DBMS index and surface unregistered files
