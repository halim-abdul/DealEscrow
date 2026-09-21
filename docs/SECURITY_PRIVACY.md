# Security & Privacy Model

## Threat model

DealEscrow processes high-value documents and potentially sensitive identity/payment metadata. Assume:
- uploaded files may be malicious;
- OCR/LLM outputs may be wrong;
- users may dispute agreement versions;
- API credentials may be targeted;
- financial notifications may be socially engineered.

## Controls

- Object storage outside the public web root.
- Malware/file-type scanning before parsing.
- Encryption in transit and at rest.
- Per-deal access control.
- MFA for consequential operations.
- Document hashes and immutable acceptance events.
- Secrets in a secret manager, never CSV/Git.
- Tokenized bank/provider identifiers rather than raw bank credentials.
- Structured audit events.
- Data-retention and deletion schedules.
- Export/delete workflows for data-subject requests.
- Human review on legal/compliance escalation.

## Identity data

Store only the minimum fields required for identity verification. Prefer verification-provider references over copies of identity documents whenever feasible.

## Research datasets

Repository CSV files are schema templates and synthetic examples only. Never commit real identity documents, bank-account information, addresses, PCC records or agreement contents.
