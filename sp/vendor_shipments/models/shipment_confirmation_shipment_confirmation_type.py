from enum import Enum


class ShipmentConfirmationShipmentConfirmationType(str, Enum):
    ORIGINAL = "Original"
    REPLACE = "Replace"

    def __str__(self) -> str:
        return str(self.value)
