from enum import Enum


class ItemApprovalType(str, Enum):
    LEONARDI_APPROVAL = "LEONARDI_APPROVAL"

    def __str__(self) -> str:
        return str(self.value)
