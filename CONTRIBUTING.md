# Contributing

## Principles

- keep core governance platform-neutral
- avoid encoding one vendor's file names into the universal rule source
- update schemas, templates, and skills together when changing the model

## Before opening a PR

1. Validate changed skills
2. Validate changed JSON files
3. Confirm `templates/` still matches the intended architecture
4. Confirm examples still demonstrate the current model

## Good contribution targets

- new adapter patterns for more agent ecosystems
- better audit patterns
- better promotion workflows
- improved portability guidance

## Avoid

- hardwiring one model vendor into the core architecture
- putting mutable local secrets or personal paths into the templates
