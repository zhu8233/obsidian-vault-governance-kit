# RULES.md

This is the system-kernel rule source for a governed vault.

## First Read Rule

Before changing governed vault content:

1. Read `RULES.md`
2. Read `00-Agent-Onboarding.md`
3. Read `Interfaces/20-Task-Types.md`
4. Read `Interfaces/40-Risk-Levels.md`
5. Read the local vault registry
6. Confirm your role and target layer

## Layer Model

- `system`
- `intake`
- `curation`
- `canonical`
- `archive`

## General Rules

- Ordinary agents should not write to the protected system zone by default.
- Canonical knowledge is not a scratchpad.
- Important changes must leave a registry and ledger trail.
- When uncertain, degrade to proposal instead of escalating risk.

## Protected System Zone

The protected system zone normally includes:

- rules
- onboarding
- interfaces
- planning
- dbms protocols
- registry files
- state files

Only explicitly authorized roles should modify those files.
