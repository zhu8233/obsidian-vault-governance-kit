# Input Output Contracts

## Input Contract

Each task must resolve:

- `agent_id`
- `task_type`
- `target_topic_id`
- `target_layer`
- `risk_level`
- `required_reads`
- `allowed_writes`

## Output Contract

Each task should produce only the outputs appropriate to its task type.

Examples:

- maintenance -> report + ledger + state update
- growth -> growth report + paths + next question + ledger
- project archive -> manifest + source map + project index + ledger
- dbms -> system report + ledger + dbms state update
- index rebuild -> `DBMS/index/file-index.jsonl` + `topic-summary.json` + `findings.json` + report + ledger + `DBMS/state/last-index-run.json`
