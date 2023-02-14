from enum import Enum


class UnitOfWeight(str, Enum):
    OZ = "oz"
    G = "g"

    def __str__(self) -> str:
        return str(self.value)
