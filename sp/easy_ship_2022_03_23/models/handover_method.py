from enum import Enum


class HandoverMethod(str, Enum):
    PICKUP = "Pickup"
    DROPOFF = "Dropoff"

    def __str__(self) -> str:
        return str(self.value)
