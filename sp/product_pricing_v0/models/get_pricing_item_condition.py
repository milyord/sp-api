from enum import Enum


class GetPricingItemCondition(str, Enum):
    NEW = "New"
    USED = "Used"
    COLLECTIBLE = "Collectible"
    REFURBISHED = "Refurbished"
    CLUB = "Club"

    def __str__(self) -> str:
        return str(self.value)
