from enum import Enum


class UnitOfMeasurement(str, Enum):
    INCHES = "inches"
    CENTIMETERS = "centimeters"

    def __str__(self) -> str:
        return str(self.value)
