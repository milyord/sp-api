from enum import Enum


class QuantityDiscountType(str, Enum):
    QUANTITY_DISCOUNT = "QUANTITY_DISCOUNT"

    def __str__(self) -> str:
        return str(self.value)
