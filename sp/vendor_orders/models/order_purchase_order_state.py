from enum import Enum


class OrderPurchaseOrderState(str, Enum):
    NEW = "New"
    ACKNOWLEDGED = "Acknowledged"
    CLOSED = "Closed"

    def __str__(self) -> str:
        return str(self.value)
