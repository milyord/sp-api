from enum import Enum


class OrderItemAcknowledgementRejectionReason(str, Enum):
    TEMPORARILYUNAVAILABLE = "TemporarilyUnavailable"
    INVALIDPRODUCTIDENTIFIER = "InvalidProductIdentifier"
    OBSOLETEPRODUCT = "ObsoleteProduct"

    def __str__(self) -> str:
        return str(self.value)
