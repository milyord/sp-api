from enum import Enum


class UnitOfWeight(str, Enum):
    POUNDS = "pounds"
    KILOGRAMS = "kilograms"

    def __str__(self) -> str:
        return str(self.value)
