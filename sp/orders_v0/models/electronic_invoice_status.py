from enum import Enum


class ElectronicInvoiceStatus(str, Enum):
    NOTREQUIRED = "NotRequired"
    NOTFOUND = "NotFound"
    PROCESSING = "Processing"
    ERRORED = "Errored"
    ACCEPTED = "Accepted"

    def __str__(self) -> str:
        return str(self.value)
