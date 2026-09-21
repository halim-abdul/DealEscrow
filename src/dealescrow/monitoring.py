from __future__ import annotations

from datetime import date, timedelta

from .models import DealStatus, DealTerms


def status_for_date(terms: DealTerms, as_of: date, is_settled: bool = False) -> DealStatus:
    if is_settled:
        return DealStatus.SETTLED

    due = terms.repayment_due_date
    grace_end = due + timedelta(days=terms.grace_days)

    if as_of < due:
        return DealStatus.ACTIVE
    if as_of == due:
        return DealStatus.DUE
    if terms.grace_days > 0 and as_of <= grace_end:
        return DealStatus.GRACE
    return DealStatus.OVERDUE


def reminder_events(terms: DealTerms, as_of: date) -> list[str]:
    events: list[str] = []
    days_to_due = (terms.repayment_due_date - as_of).days

    if days_to_due in {30, 14, 7, 3, 1}:
        events.append(f"repayment_due_in_{days_to_due}_days")
    if days_to_due == 0:
        events.append("repayment_due_today")
    if days_to_due < 0:
        events.append("repayment_overdue")
    return events
