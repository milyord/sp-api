from enum import Enum


class PackageStatus(str, Enum):
    SHIPPED = "SHIPPED"
    IN_TRANSIT = "IN_TRANSIT"
    DELIVERED = "DELIVERED"
    CHECKED_IN = "CHECKED_IN"
    RECEIVING = "RECEIVING"
    CLOSED = "CLOSED"
    DELETED = "DELETED"

    def __str__(self) -> str:
        return str(self.value)
