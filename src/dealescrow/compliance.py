from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PaymentAuthorization:
    mandate_id: str | None
    status: str
    scope_allows_debit: bool
    provider_is_approved: bool


def can_request_automatic_debit(auth: PaymentAuthorization) -> tuple[bool, str]:
    """Return a conservative execution gate for automated payment requests."""
    if not auth.mandate_id:
        return False, "missing_mandate"
    if auth.status.lower() != "active":
        return False, "inactive_mandate"
    if not auth.scope_allows_debit:
        return False, "mandate_scope_disallows_debit"
    if not auth.provider_is_approved:
        return False, "unapproved_payment_provider"
    return True, "authorized"


def requires_human_legal_review(event_type: str) -> bool:
    return event_type in {
        "legal_notice",
        "dispute",
        "collections_escalation",
        "regulatory_classification",
        "identity_or_criminal_record_issue",
    }
