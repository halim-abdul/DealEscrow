from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from .models import ExtractionResult


SUPPORTED_SUFFIXES = {".pdf", ".docx", ".txt", ".png", ".jpg", ".jpeg"}


@dataclass(frozen=True)
class ParsedDocument:
    filename: str
    text: str
    page_count: int | None = None


class OCRProvider(Protocol):
    def extract(self, path: Path) -> ParsedDocument: ...


class TermsExtractor(Protocol):
    def extract_terms(self, text: str, source_name: str) -> ExtractionResult: ...


def validate_upload_name(filename: str) -> str:
    suffix = Path(filename).suffix.lower()
    if suffix not in SUPPORTED_SUFFIXES:
        raise ValueError(f"Unsupported document type: {suffix or '<none>'}")
    return suffix


def confidence_requires_review(result: ExtractionResult, threshold: float = 0.85) -> bool:
    fields = [
        result.principal,
        result.repayment_due_date,
        result.annual_interest_rate,
        result.grace_days,
    ]
    return bool(
        result.conflicts
        or result.missing_terms
        or any(field is not None and field.confidence < threshold for field in fields)
    )
