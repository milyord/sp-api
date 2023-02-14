from enum import Enum


class WeightUnit(str, Enum):
    G = "g"
    KG = "kg"
    OZ = "oz"
    LB = "lb"

    def __str__(self) -> str:
        return str(self.value)
