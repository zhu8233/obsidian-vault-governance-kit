# Risk Levels

## Levels

- `L0`: read-only
- `L1`: safe writes
- `L2`: structural changes
- `L3`: canonical-impacting changes
- `L4`: destructive or coordination-level actions

## Rule

- `L0-L1` may run automatically
- `L2` requires state and ledger hygiene
- `L3` requires proposal or elevated review
- `L4` requires human approval or explicit coordination

Index rebuild and index audit normally stay in `L1-L2` because they update derived DBMS state rather than canonical knowledge.
