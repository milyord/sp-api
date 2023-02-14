from enum import Enum


class GetShipmentsShipmentStatusListItem(str, Enum):
    WORKING = "WORKING"
    READY_TO_SHIP = "READY_TO_SHIP"
    SHIPPED = "SHIPPED"
    RECEIVING = "RECEIVING"
    CANCELLED = "CANCELLED"
    DELETED = "DELETED"
    CLOSED = "CLOSED"
    ERROR = "ERROR"
    IN_TRANSIT = "IN_TRANSIT"
    DELIVERED = "DELIVERED"
    CHECKED_IN = "CHECKED_IN"

    def __str__(self) -> str:
        return str(self.value)
