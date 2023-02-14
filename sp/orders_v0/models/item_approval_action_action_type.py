from enum import Enum


class ItemApprovalActionActionType(str, Enum):
    APPROVE = "APPROVE"
    DECLINE = "DECLINE"
    APPROVE_WITH_CHANGES = "APPROVE_WITH_CHANGES"

    def __str__(self) -> str:
        return str(self.value)
