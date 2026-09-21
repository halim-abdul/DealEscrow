# Research Plan

## Research questions

1. How reliably can LLMs extract financial obligations from heterogeneous agreements?
2. How should confidence, conflict detection and human review reduce extraction risk?
3. Can deterministic state/finance engines make agentic workflows auditable?
4. Which DealEscrow-native behavioural signals are useful without relying on protected or excessive personal data?
5. How can n8n orchestrate reminders and provider actions without becoming the source of truth?

## Evaluation tracks

### Document extraction
- exact match / token F1 for parties and clauses
- MAE for principal and interest-rate extraction
- date extraction accuracy
- calibration error for confidence
- conflict-detection recall

### Monitoring engine
- transition correctness
- deadline recall
- duplicate-notification rate
- false escalation rate

### Finance engine
- golden-test numerical accuracy
- day-count edge cases
- rounding reproducibility

### Risk research
- explainability coverage
- false-positive analysis
- feature-ablation studies
- fairness review for any feature correlated with protected traits

### Reliability
- workflow retry correctness
- idempotency
- provider failure recovery
- audit-event completeness

## Dataset policy

Use synthetic or properly licensed/de-identified agreements. Do not train on real user contracts or identity data without an explicit research governance process.
