from enum import Enum


class ReasonReasonCode(str, Enum):
    APPROVAL_REQUIRED = "APPROVAL_REQUIRED"
    ASIN_NOT_FOUND = "ASIN_NOT_FOUND"
    NOT_ELIGIBLE = "NOT_ELIGIBLE"

    def __str__(self) -> str:
        return str(self.value)
