from enum import Enum


class InvalidItemReasonCode(str, Enum):
    INVALIDVALUES = "InvalidValues"
    DUPLICATEREQUEST = "DuplicateRequest"
    NOCOMPLETEDSHIPITEMS = "NoCompletedShipItems"
    NORETURNABLEQUANTITY = "NoReturnableQuantity"

    def __str__(self) -> str:
        return str(self.value)
