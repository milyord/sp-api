from enum import Enum


class ItemDetailsHandlingCode(str, Enum):
    OVERSIZED = "Oversized"
    FRAGILE = "Fragile"
    FOOD = "Food"
    HANDLEWITHCARE = "HandleWithCare"

    def __str__(self) -> str:
        return str(self.value)
