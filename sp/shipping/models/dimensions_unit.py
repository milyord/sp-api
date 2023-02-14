from enum import Enum


class DimensionsUnit(str, Enum):
    IN = "IN"
    CM = "CM"

    def __str__(self) -> str:
        return str(self.value)
