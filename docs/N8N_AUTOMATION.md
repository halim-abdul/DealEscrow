# n8n Automation

n8n is used as the event/workflow layer around the DealEscrow backend.

## Workflows

1. **Document Intake**
   - Webhook
   - file metadata validation
   - backend ingestion request
   - async extraction status update

2. **Daily Deal Monitor**
   - Schedule Trigger
   - fetch active deals
   - compute due/grace/overdue state in backend
   - branch by event type
   - send notifications

3. **Agreement Accepted**
   - webhook from backend
   - verify both parties accepted same version
   - activate deal
   - create initial deadline events

4. **Payment Request**
   - verify mandate and entitlement
   - call approved payment-provider adapter
   - record result
   - notify both parties

5. **Compliance Escalation**
   - receive risk/compliance event
   - create manual review item
   - suppress automatic consequential action until cleared

## Design principle

n8n orchestrates; it does not own the source of truth. Financial math, authorization checks and agreement state transitions remain in the backend.
