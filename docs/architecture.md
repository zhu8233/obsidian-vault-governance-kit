# Architecture

## Purpose

The kit is built for knowledge vaults maintained by:

- humans
- ingestion workflows
- specialist agents
- coordinator agents
- multiple model ecosystems

## Governance Layers

### 1. System

- rules
- schemas
- registries
- audits
- local entry instructions

### 2. Intake

- raw sources
- imported documents
- NotebookLM outputs
- quick captures

### 3. Curation

- reorganized notes
- working summaries
- topic indexes
- draft synthesis

### 4. Canonical

- high-reuse, high-findability knowledge
- stable topic indexes
- durable summaries

### 5. Archive

- frozen material
- retired topics
- old canonical snapshots

## Four Coordination Primitives

### RULES

Human-readable operating source.

### Registry

Machine-readable facts:

- topics
- objects
- roles
- promotion queue
- change ledger

### Skills

Behavioral procedures for agents.

### Audit

Drift detection and repair loop.

## Portability Principle

Everything in this kit should be separable into:

- universal governance logic
- environment-specific adapters

Universal logic belongs in `docs/`, `schemas/`, `skills/`, and `templates/`.
Environment-specific notes belong in the target vault after installation.
