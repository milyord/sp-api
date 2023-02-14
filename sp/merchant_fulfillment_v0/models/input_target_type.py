from enum import Enum


class InputTargetType(str, Enum):
    SHIPMENT_LEVEL = "SHIPMENT_LEVEL"
    ITEM_LEVEL = "ITEM_LEVEL"

    def __str__(self) -> str:
        return str(self.value)
