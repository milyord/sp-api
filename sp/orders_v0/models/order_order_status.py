from enum import Enum


class OrderOrderStatus(str, Enum):
    PENDING = "Pending"
    UNSHIPPED = "Unshipped"
    PARTIALLYSHIPPED = "PartiallyShipped"
    SHIPPED = "Shipped"
    CANCELED = "Canceled"
    UNFULFILLABLE = "Unfulfillable"
    INVOICEUNCONFIRMED = "InvoiceUnconfirmed"
    PENDINGAVAILABILITY = "PendingAvailability"

    def __str__(self) -> str:
        return str(self.value)
