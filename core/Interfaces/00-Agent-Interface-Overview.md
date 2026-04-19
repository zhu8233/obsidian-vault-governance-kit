# Agent Interface Overview

Every governed task should be expressed through a stable task contract.

## Minimum Task Contract

```yaml
agent_id:
task_type:
target_topic_id:
target_layer:
risk_level:
required_reads: []
allowed_writes: []
required_outputs: []
must_update_registry:
must_append_ledger:
needs_proposal:
```

No high-impact task should execute without these fields being resolved.
