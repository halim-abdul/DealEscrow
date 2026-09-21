from __future__ import annotations

from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP

from .models import DealTerms


MONEY = Decimal("0.01")


def interest_start_date(terms: DealTerms) -> date | None:
    rule = terms.interest_rule
    if rule is None or not rule.accepted_by_both:
        return None
    return terms.start_date + timedelta(days=rule.starts_after_days)


def simple_interest(terms: DealTerms, as_of: date) -> Decimal:
    """Compute simple interest only from explicitly accepted terms."""
    rule = terms.interest_rule
    start = interest_start_date(terms)
    if rule is None or start is None or as_of <= start:
        return Decimal("0.00")

    days = (as_of - start).days
    rate = rule.annual_rate_percent / Decimal("100")
    amount = terms.principal * rate * Decimal(days) / Decimal(rule.day_count_basis)
    return amount.quantize(MONEY, rounding=ROUND_HALF_UP)


def total_due(terms: DealTerms, as_of: date) -> Decimal:
    return (terms.principal + simple_interest(terms, as_of)).quantize(
        MONEY, rounding=ROUND_HALF_UP
    )
