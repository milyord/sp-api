from enum import Enum


class AssociatedItemItemStatus(str, Enum):
    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"

    def __str__(self) -> str:
        return str(self.value)
