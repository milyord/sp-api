from enum import Enum


class OrderDetailsPaymentMethod(str, Enum):
    INVOICE = "Invoice"
    CONSIGNMENT = "Consignment"
    CREDITCARD = "CreditCard"
    PREPAID = "Prepaid"

    def __str__(self) -> str:
        return str(self.value)
