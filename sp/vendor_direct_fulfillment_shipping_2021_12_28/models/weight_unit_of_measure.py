from enum import Enum


class WeightUnitOfMeasure(str, Enum):
    KG = "KG"
    LB = "LB"

    def __str__(self) -> str:
        return str(self.value)
