from enum import Enum


class GetPurchaseOrdersPoItemState(str, Enum):
    CANCELLED = "Cancelled"

    def __str__(self) -> str:
        return str(self.value)
