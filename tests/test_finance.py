from datetime import date
from decimal import Decimal

from dealescrow.finance import simple_interest, total_due
from dealescrow.models import DealTerms, InterestRule


def make_terms(accepted: bool = True) -> DealTerms:
    return DealTerms(
        deal_id="D-1",
        principal=Decimal("1000.00"),
        currency="EUR",
        start_date=date(2026, 1, 1),
        repayment_due_date=date(2026, 6, 1),
        grace_days=10,
        interest_rule=InterestRule(
            annual_rate_percent=Decimal("5"),
            starts_after_days=45,
            source="test",
            accepted_by_both=accepted,
        ),
    )


def test_interest_starts_only_after_delay():
    terms = make_terms()
    assert simple_interest(terms, date(2026, 2, 15)) == Decimal("0.00")
    assert simple_interest(terms, date(2026, 2, 16)) > Decimal("0.00")


def test_unaccepted_interest_is_not_applied():
    terms = make_terms(accepted=False)
    assert simple_interest(terms, date(2026, 8, 1)) == Decimal("0.00")


def test_total_due_includes_interest():
    terms = make_terms()
    assert total_due(terms, date(2026, 8, 1)) > Decimal("1000.00")
