# Task Types

## Common Task Types

- `capture_source`
- `curate_topic`
- `project_archive`
- `proposal_creation`
- `promotion_review`
- `maintenance_weekly`
- `maintenance_monthly_audit`
- `growth_expand_topic`
- `growth_fill_gap`
- `registry_repair`
- `disorder_recovery`
- `system_guard`
- `index_rebuild`
- `index_audit`
- `post_archive_audit_repair`
- `system_snapshot_sync_review`
- `system_snapshot_upgrade_proposal`
- `system_snapshot_apply`

## Rule

Each task should declare exactly one primary `task_type`.

## Index Tasks

- `index_rebuild`
  - default layer: `system`
  - default risk: `L1-L2`
  - output: DBMS index artifacts + report + ledger + index state update

- `index_audit`
  - default layer: `system`
  - default risk: `L1-L2`
  - output: findings review + report + ledger + index state update
