from enum import Enum


class OrderBuyerInvoicePreference(str, Enum):
    INDIVIDUAL = "INDIVIDUAL"
    BUSINESS = "BUSINESS"

    def __str__(self) -> str:
        return str(self.value)
