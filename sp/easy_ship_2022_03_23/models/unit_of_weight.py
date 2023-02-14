from enum import Enum


class UnitOfWeight(str, Enum):
    GRAMS = "Grams"
    G = "G"

    def __str__(self) -> str:
        return str(self.value)
