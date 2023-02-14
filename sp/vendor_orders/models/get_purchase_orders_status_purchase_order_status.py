from enum import Enum


class GetPurchaseOrdersStatusPurchaseOrderStatus(str, Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"

    def __str__(self) -> str:
        return str(self.value)
