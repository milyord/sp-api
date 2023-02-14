from enum import Enum


class ContentStatus(str, Enum):
    APPROVED = "APPROVED"
    DRAFT = "DRAFT"
    REJECTED = "REJECTED"
    SUBMITTED = "SUBMITTED"

    def __str__(self) -> str:
        return str(self.value)
