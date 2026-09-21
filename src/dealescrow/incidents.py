from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class PlatformIncident:
    incident_id: str
    deal_id: str
    event_type: str
    occurred_at: datetime
    description: str
    verified: bool = False


REVIEW_EVENT_TYPES = {
    "repeated_overdue_event",
    "agreement_dispute",
    "payment_reversal",
    "identity_mismatch",
}


def needs_manual_review(incidents: list[PlatformIncident]) -> tuple[bool, list[str]]:
    """Surface verified platform incidents for a human reviewer.

    This is not a credit score and must not automatically approve, deny,
    price, or rank a financial agreement.
    """
    reasons = [
        f"{item.event_type}: {item.description}"
        for item in incidents
        if item.verified and item.event_type in REVIEW_EVENT_TYPES
    ]
    return bool(reasons), reasons
