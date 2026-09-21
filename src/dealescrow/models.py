from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from enum import StrEnum
from pydantic import BaseModel, Field


class DealStatus(StrEnum):
    DRAFT = "draft"
    EXTRACTED = "extracted"
    REVIEW_REQUIRED = "review_required"
    PROPOSED = "proposed"
    BOTH_ACCEPTED = "both_accepted"
    ACTIVE = "active"
    DUE = "due"
    GRACE = "grace"
    OVERDUE = "overdue"
    DISPUTED = "disputed"
    SETTLED = "settled"
    CANCELLED = "cancelled"


class InterestType(StrEnum):
    SIMPLE = "simple"


class InterestRule(BaseModel):
    annual_rate_percent: Decimal = Field(ge=0)
    starts_after_days: int = Field(default=0, ge=0)
    day_count_basis: int = Field(default=365, gt=0)
    interest_type: InterestType = InterestType.SIMPLE
    source: str
    accepted_by_both: bool = False


class DealTerms(BaseModel):
    deal_id: str
    principal: Decimal = Field(gt=0)
    currency: str = Field(min_length=3, max_length=3)
    start_date: date
    repayment_due_date: date
    grace_days: int = Field(default=0, ge=0)
    interest_rule: InterestRule | None = None


class ExtractedField(BaseModel):
    value: str | int | float | None
    confidence: float = Field(ge=0.0, le=1.0)
    source: str | None = None


class ExtractionResult(BaseModel):
    parties: list[str] = []
    principal: ExtractedField | None = None
    repayment_due_date: ExtractedField | None = None
    annual_interest_rate: ExtractedField | None = None
    grace_days: ExtractedField | None = None
    missing_terms: list[str] = []
    conflicts: list[str] = []


class AcceptanceEvent(BaseModel):
    agreement_version_id: str
    user_id: str
    accepted_at: datetime
    document_hash: str


class RiskEvent(BaseModel):
    user_id: str
    deal_id: str | None = None
    event_type: str
    severity: int = Field(ge=1, le=5)
    explanation: str
    created_at: datetime
