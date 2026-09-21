from datetime import date
from decimal import Decimal

from dealescrow.models import DealStatus, DealTerms
from dealescrow.monitoring import status_for_date


def terms() -> DealTerms:
    return DealTerms(
        deal_id="D-2",
        principal=Decimal("500"),
        currency="EUR",
        start_date=date(2026, 1, 1),
        repayment_due_date=date(2026, 1, 31),
        grace_days=5,
    )


def test_monitoring_states():
    t = terms()
    assert status_for_date(t, date(2026, 1, 30)) == DealStatus.ACTIVE
    assert status_for_date(t, date(2026, 1, 31)) == DealStatus.DUE
    assert status_for_date(t, date(2026, 2, 3)) == DealStatus.GRACE
    assert status_for_date(t, date(2026, 2, 6)) == DealStatus.OVERDUE
