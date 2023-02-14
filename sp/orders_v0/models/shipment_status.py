from enum import Enum


class ShipmentStatus(str, Enum):
    READYFORPICKUP = "ReadyForPickup"
    PICKEDUP = "PickedUp"
    REFUSEDPICKUP = "RefusedPickup"

    def __str__(self) -> str:
        return str(self.value)
