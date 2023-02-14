from enum import Enum


class WeightUnitOfMeasure(str, Enum):
    G = "G"
    KG = "Kg"
    OZ = "Oz"
    LB = "Lb"

    def __str__(self) -> str:
        return str(self.value)
