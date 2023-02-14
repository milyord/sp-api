from enum import Enum


class OrderStatusPurchaseOrderStatus(str, Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"

    def __str__(self) -> str:
        return str(self.value)
