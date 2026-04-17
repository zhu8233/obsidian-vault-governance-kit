# Regression Plan

## Objective

Prove that the repository stays internally consistent after changes.

## Repository-level regression

- all required files still exist
- schemas still parse
- template registries still parse
- example registries still parse
- adapter files still point to `RULES.md`
- skill metadata still has valid trigger descriptions
- skill UI prompts still mention the correct `$skill-name`

## Human-readable regression

- README still explains design, quickstart, validation, and publishing
- quickstart still matches the actual template layout
- example vault still mirrors the intended governance model

## Future behavioral regression

Not yet automated in this repository:

- cross-model agent enters a governed vault and converges on the same layer decision
- non-Hermes agent proposes rather than directly overwriting canonical
- audit skill correctly classifies drift scenarios

These should be added after collecting real usage transcripts.
