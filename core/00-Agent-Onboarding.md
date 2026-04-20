# Agent Onboarding

## Required Read Order

1. `RULES.md`
2. local overrides if present
3. local vault registry
4. local role roster

For audit, scan, registry repair, or DBMS review tasks:

5. `01-Workflow/Knowledge-Governance/DBMS/state/last-index-run.json`
6. `01-Workflow/Knowledge-Governance/DBMS/index/findings.json`

## Required Decisions Before Editing

1. What is the `task_type`?
2. What is the `target_topic_id`?
3. What is the `target_layer`?
4. What is the `risk_level`?
5. Am I allowed to write here?

## Required Outputs

Tasks that modify state should normally produce:

- report or note output
- registry update when needed
- ledger entry
- state file update when the task defines one
