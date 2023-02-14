from enum import Enum


class ShipmentDetailsShipmentStatus(str, Enum):
    SHIPPED = "SHIPPED"
    FLOOR_DENIAL = "FLOOR_DENIAL"

    def __str__(self) -> str:
        return str(self.value)
