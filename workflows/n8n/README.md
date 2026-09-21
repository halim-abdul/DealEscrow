# n8n Workflow Catalog

These workflows are orchestration examples. They assume the DealEscrow backend remains the source of truth.

## Included

- `daily_deal_monitor.json` — scheduled monitoring-event retrieval and human-review branch.

## Planned workflows

- document intake webhook
- dual-acceptance activation
- repayment reminder sequence
- grace-period expiry
- payment-provider request with mandate gate
- failed-payment retry policy
- dispute freeze
- compliance escalation
- subscription renewal/update
- monthly de-identified research export

## Environment

Use n8n credentials/secrets for API keys. Never place payment credentials, identity data or real agreements inside exported workflow JSON.
