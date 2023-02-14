from enum import Enum


class ShipmentType(str, Enum):
    SP = "SP"
    LTL = "LTL"

    def __str__(self) -> str:
        return str(self.value)
