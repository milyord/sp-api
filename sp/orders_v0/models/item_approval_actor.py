from enum import Enum


class ItemApprovalActor(str, Enum):
    SELLING_PARTNER = "SELLING_PARTNER"
    AMAZON = "AMAZON"

    def __str__(self) -> str:
        return str(self.value)
