from enum import Enum


class ItemOfferByMarketplaceOfferType(str, Enum):
    B2C = "B2C"
    B2B = "B2B"

    def __str__(self) -> str:
        return str(self.value)
