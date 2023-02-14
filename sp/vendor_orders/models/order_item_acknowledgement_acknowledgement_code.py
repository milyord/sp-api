from enum import Enum


class OrderItemAcknowledgementAcknowledgementCode(str, Enum):
    ACCEPTED = "Accepted"
    BACKORDERED = "Backordered"
    REJECTED = "Rejected"

    def __str__(self) -> str:
        return str(self.value)
