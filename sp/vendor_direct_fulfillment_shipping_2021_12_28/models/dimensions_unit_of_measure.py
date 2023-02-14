from enum import Enum


class DimensionsUnitOfMeasure(str, Enum):
    IN = "IN"
    CM = "CM"

    def __str__(self) -> str:
        return str(self.value)
