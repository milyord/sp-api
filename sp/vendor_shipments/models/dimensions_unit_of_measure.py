from enum import Enum


class DimensionsUnitOfMeasure(str, Enum):
    IN = "In"
    FT = "Ft"
    METER = "Meter"
    YARD = "Yard"

    def __str__(self) -> str:
        return str(self.value)
