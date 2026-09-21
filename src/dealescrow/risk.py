from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PlatformHistory:
    overdue_deals: int = 0
    disputed_deals: int = 0
    broken_acceptances: int = 0
    verified_settlements: int = 0


def platform_risk_signal(history: PlatformHistory) -> tuple[int, list[str]]:
    """Explainable internal operational signal; not a credit score."""
    score = 0
    reasons: list[str] = []

    if history.overdue_deals:
        score += min(history.overdue_deals * 15, 45)
        reasons.append(f"{history.overdue_deals} prior overdue DealEscrow deal(s)")
    if history.disputed_deals:
        score += min(history.disputed_deals * 10, 30)
        reasons.append(f"{history.disputed_deals} prior disputed DealEscrow deal(s)")
    if history.broken_acceptances:
        score += min(history.broken_acceptances * 10, 20)
        reasons.append("prior accepted obligation changed or abandoned")
    if history.verified_settlements >= 3:
        score -= min(history.verified_settlements, 10)
        reasons.append("history includes multiple verified settlements")

    return max(0, min(score, 100)), reasons


PROHIBITED_RISK_FEATURES = {
    "citizenship",
    "ethnicity",
    "religion",
    "health",
    "political_opinion",
    "sexual_orientation",
    "criminal_conviction_without_specific_lawful_basis",
}
