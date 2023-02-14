from enum import Enum


class ProductTypeDefinitionRequirements(str, Enum):
    LISTING = "LISTING"
    LISTING_PRODUCT_ONLY = "LISTING_PRODUCT_ONLY"
    LISTING_OFFER_ONLY = "LISTING_OFFER_ONLY"

    def __str__(self) -> str:
        return str(self.value)
