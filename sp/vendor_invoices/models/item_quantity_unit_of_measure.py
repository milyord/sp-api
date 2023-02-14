from enum import Enum


class ItemQuantityUnitOfMeasure(str, Enum):
    CASES = "Cases"
    EACHES = "Eaches"

    def __str__(self) -> str:
        return str(self.value)
