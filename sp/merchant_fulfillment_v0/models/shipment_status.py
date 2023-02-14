from enum import Enum


class ShipmentStatus(str, Enum):
    PURCHASED = "Purchased"
    REFUNDPENDING = "RefundPending"
    REFUNDREJECTED = "RefundRejected"
    REFUNDAPPLIED = "RefundApplied"

    def __str__(self) -> str:
        return str(self.value)
