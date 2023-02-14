from enum import Enum


class FulfillmentAction(str, Enum):
    SHIP = "Ship"
    HOLD = "Hold"

    def __str__(self) -> str:
        return str(self.value)
