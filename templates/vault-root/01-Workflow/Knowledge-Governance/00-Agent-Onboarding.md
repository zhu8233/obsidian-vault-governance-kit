# Agent Onboarding

Use this file to align any agent entering the vault.

## Required Reading Order

1. `RULES.md`
2. nearest adapter file if present
3. `.knowledge-registry/vault-registry.json`
4. `.knowledge-registry/agent-roster.json`

## Required Decisions Before Editing

1. What `topic_id` am I touching?
2. Which layer is this file in?
3. Am I allowed to write to this layer?
4. If not, should I propose, promote, audit, or escalate to Hermes?

## After Important Changes

- update registry if object metadata changed
- append to `change-ledger.jsonl`
- if the note should become stable knowledge, use promotion workflow instead of direct canonical write
