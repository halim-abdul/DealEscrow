from dealescrow.compliance import PaymentAuthorization, can_request_automatic_debit


def test_debit_requires_mandate():
    allowed, reason = can_request_automatic_debit(
        PaymentAuthorization(
            mandate_id=None,
            status="active",
            scope_allows_debit=True,
            provider_is_approved=True,
        )
    )
    assert allowed is False
    assert reason == "missing_mandate"


def test_debit_allowed_only_when_all_gates_pass():
    allowed, reason = can_request_automatic_debit(
        PaymentAuthorization(
            mandate_id="M-1",
            status="active",
            scope_allows_debit=True,
            provider_is_approved=True,
        )
    )
    assert allowed is True
    assert reason == "authorized"
