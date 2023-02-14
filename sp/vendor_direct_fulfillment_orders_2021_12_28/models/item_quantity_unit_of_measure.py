from enum import Enum


class ItemQuantityUnitOfMeasure(str, Enum):
    EACH = "Each"

    def __str__(self) -> str:
        return str(self.value)
