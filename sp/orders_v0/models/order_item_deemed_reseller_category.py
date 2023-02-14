from enum import Enum


class OrderItemDeemedResellerCategory(str, Enum):
    IOSS = "IOSS"
    UOSS = "UOSS"

    def __str__(self) -> str:
        return str(self.value)
