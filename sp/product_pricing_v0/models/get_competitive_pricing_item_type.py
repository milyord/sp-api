from enum import Enum


class GetCompetitivePricingItemType(str, Enum):
    ASIN = "Asin"
    SKU = "Sku"

    def __str__(self) -> str:
        return str(self.value)
