from enum import Enum


class FulfillmentShipmentFulfillmentShipmentStatus(str, Enum):
    PENDING = "PENDING"
    SHIPPED = "SHIPPED"
    CANCELLED_BY_FULFILLER = "CANCELLED_BY_FULFILLER"
    CANCELLED_BY_SELLER = "CANCELLED_BY_SELLER"

    def __str__(self) -> str:
        return str(self.value)
