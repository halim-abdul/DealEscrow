# AI Agent Design

## Agent responsibilities

### 1. Intake Agent
Normalises uploads and written comments, identifies document type and language.

### 2. OCR / Parsing Agent
Extracts text from PDF, DOCX and images through pluggable parsers/OCR providers.

### 3. Terms Extraction Agent
Returns structured candidate fields:
- parties
- principal/currency
- repayment deadline
- grace period
- interest clause
- payment method
- conditions precedent
- late-payment language
- governing-law references

### 4. Conflict Agent
Detects contradictions between uploaded documents, comments and later edits.

### 5. Agreement QA Agent
Generates questions for missing or ambiguous terms. It does not silently fill legal or financial terms.

### 6. Legal Retrieval Agent
Retrieves relevant uploaded law materials and approved public-law references. Output is citation-based and routed to human review for consequential use.

### 7. Monitor Agent
Summarises upcoming obligations and events from deterministic system state.

## Safety contract

LLMs may:
- extract,
- summarise,
- classify,
- retrieve,
- explain uncertainty.

LLMs may not independently:
- create a binding interest rate,
- debit a bank account,
- declare a party legally liable,
- decide guilt/fraud,
- approve regulated lending/payment activity.

## Example extraction JSON

```json
{
  "principal": {"amount": 1000, "currency": "EUR", "confidence": 0.98},
  "repayment_due_date": {"value": "2026-12-01", "confidence": 0.92},
  "interest": {
    "annual_rate_percent": 5.0,
    "starts_after_days": 45,
    "source": "agreement.pdf#p2",
    "confidence": 0.88
  },
  "missing_terms": [],
  "conflicts": []
}
```
