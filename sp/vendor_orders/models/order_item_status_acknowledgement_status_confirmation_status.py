from enum import Enum


class OrderItemStatusAcknowledgementStatusConfirmationStatus(str, Enum):
    ACCEPTED = "ACCEPTED"
    PARTIALLY_ACCEPTED = "PARTIALLY_ACCEPTED"
    REJECTED = "REJECTED"
    UNCONFIRMED = "UNCONFIRMED"

    def __str__(self) -> str:
        return str(self.value)
