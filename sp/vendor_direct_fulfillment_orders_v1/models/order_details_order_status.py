from enum import Enum


class OrderDetailsOrderStatus(str, Enum):
    NEW = "NEW"
    SHIPPED = "SHIPPED"
    ACCEPTED = "ACCEPTED"
    CANCELLED = "CANCELLED"

    def __str__(self) -> str:
        return str(self.value)
