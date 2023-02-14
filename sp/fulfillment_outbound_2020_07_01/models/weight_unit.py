from enum import Enum


class WeightUnit(str, Enum):
    KG = "KG"
    KILOGRAMS = "KILOGRAMS"
    LB = "LB"
    POUNDS = "POUNDS"

    def __str__(self) -> str:
        return str(self.value)
