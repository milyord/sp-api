from enum import Enum


class ItemSummaryByMarketplaceItemClassification(str, Enum):
    BASE_PRODUCT = "BASE_PRODUCT"
    OTHER = "OTHER"
    PRODUCT_BUNDLE = "PRODUCT_BUNDLE"
    VARIATION_PARENT = "VARIATION_PARENT"

    def __str__(self) -> str:
        return str(self.value)
