from enum import Enum


class VerificationStatus(str, Enum):
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    EXPIRED = "Expired"
    CANCELLED = "Cancelled"

    def __str__(self) -> str:
        return str(self.value)
