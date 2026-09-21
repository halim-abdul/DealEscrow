from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


@dataclass
class AgreementVersion:
    version_id: str
    canonical_text: str
    party_user_ids: tuple[str, str]
    acceptances: dict[str, tuple[str, datetime]] = field(default_factory=dict)

    @property
    def document_hash(self) -> str:
        return sha256_text(self.canonical_text)

    def accept(self, user_id: str, expected_hash: str) -> None:
        if user_id not in self.party_user_ids:
            raise PermissionError("Only a party to this deal can accept the agreement.")
        if expected_hash != self.document_hash:
            raise ValueError("Agreement changed; review the latest version before accepting.")
        self.acceptances[user_id] = (expected_hash, datetime.now(timezone.utc))

    @property
    def both_accepted(self) -> bool:
        return all(uid in self.acceptances for uid in self.party_user_ids)
