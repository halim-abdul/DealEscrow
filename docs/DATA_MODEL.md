# Data Model

DealEscrow uses normalized application records plus CSV templates for research, prototyping and synthetic testing.

## Core entities

- User
- IdentityProfile
- Contact
- Subscription
- Deal
- DealParty
- AgreementVersion
- Acceptance
- Document
- ExtractedTerm
- Transaction
- Deadline
- InterestRule
- LegalRuleReference
- RiskEvent
- PaymentMandate
- Notification
- AuditEvent

## Privacy rule

Fields such as date of birth, citizenship or identity-document metadata should be collected only when necessary for a defined feature and legal basis. Criminal-record/PCC data is not a default profile field.

## CSV templates

See `data/templates/`.

### users.csv
`user_id,status,created_at,country_code`

### contacts.csv
`contact_id,user_id,type,value,verified_at`

### subscriptions.csv
`subscription_id,user_id,plan,status,start_at,end_at,auto_renew`

### deals.csv
`deal_id,title,status,currency,principal_amount,created_at,activated_at`

### deal_parties.csv
`deal_id,user_id,role,accepted_version_id`

### transactions.csv
`transaction_id,deal_id,payer_user_id,payee_user_id,amount,currency,status,provider_ref,created_at,short_remark`

### deadlines.csv
`deadline_id,deal_id,event_type,due_at,grace_days,status`

### interest_rules.csv
`interest_rule_id,deal_id,annual_rate_percent,interest_type,starts_after_days,day_count_basis,source,accepted_by_both`

### legal_rules.csv
`legal_rule_id,deal_id,jurisdiction,source_title,source_url,trigger,review_required`

### risk_events.csv
`risk_event_id,user_id,deal_id,event_type,severity,explanation,created_at,resolved_at`

### payment_mandates.csv
`mandate_id,user_id,provider,scope,status,created_at,revoked_at`

### audit_events.csv
`event_id,actor_id,deal_id,event_type,object_type,object_id,created_at,metadata_json`
