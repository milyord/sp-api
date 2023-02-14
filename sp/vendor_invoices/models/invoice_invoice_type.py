from enum import Enum


class InvoiceInvoiceType(str, Enum):
    INVOICE = "Invoice"
    CREDITNOTE = "CreditNote"

    def __str__(self) -> str:
        return str(self.value)
