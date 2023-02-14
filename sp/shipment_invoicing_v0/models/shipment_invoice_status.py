from enum import Enum


class ShipmentInvoiceStatus(str, Enum):
    PROCESSING = "Processing"
    ACCEPTED = "Accepted"
    ERRORED = "Errored"
    NOTFOUND = "NotFound"

    def __str__(self) -> str:
        return str(self.value)
