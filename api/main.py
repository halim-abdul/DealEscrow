from datetime import date
from decimal import Decimal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from dealescrow.compliance import PaymentAuthorization, can_request_automatic_debit
from dealescrow.finance import simple_interest, total_due
from dealescrow.models import DealTerms, InterestRule
from dealescrow.monitoring import status_for_date

app = FastAPI(
    title="DealEscrow Research API",
    version="0.1.0",
    description="AI-assisted conditional financial agreement monitoring prototype.",
)


class InterestPreviewRequest(BaseModel):
    principal: Decimal
    currency: str = "EUR"
    start_date: date
    repayment_due_date: date
    as_of: date
    grace_days: int = 0
    annual_rate_percent: Decimal
    starts_after_days: int = 0
    accepted_by_both: bool = True


class DebitGateRequest(BaseModel):
    mandate_id: str | None = None
    status: str = "inactive"
    scope_allows_debit: bool = False
    provider_is_approved: bool = False


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/finance/preview")
def finance_preview(payload: InterestPreviewRequest) -> dict:
    if payload.repayment_due_date < payload.start_date:
        raise HTTPException(400, "repayment_due_date must not precede start_date")

    terms = DealTerms(
        deal_id="preview",
        principal=payload.principal,
        currency=payload.currency,
        start_date=payload.start_date,
        repayment_due_date=payload.repayment_due_date,
        grace_days=payload.grace_days,
        interest_rule=InterestRule(
            annual_rate_percent=payload.annual_rate_percent,
            starts_after_days=payload.starts_after_days,
            source="explicit_preview_input",
            accepted_by_both=payload.accepted_by_both,
        ),
    )
    return {
        "interest": str(simple_interest(terms, payload.as_of)),
        "total_due": str(total_due(terms, payload.as_of)),
        "status": status_for_date(terms, payload.as_of).value,
    }


@app.post("/payments/debit-gate")
def debit_gate(payload: DebitGateRequest) -> dict:
    allowed, reason = can_request_automatic_debit(PaymentAuthorization(**payload.model_dump()))
    return {"allowed": allowed, "reason": reason}
