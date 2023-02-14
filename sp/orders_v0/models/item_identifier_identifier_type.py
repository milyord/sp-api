from enum import Enum


class ItemIdentifierIdentifierType(str, Enum):
    ASIN = "ASIN"
    SELLER_SKU = "SELLER_SKU"
    EXTERNAL_ID = "EXTERNAL_ID"

    def __str__(self) -> str:
        return str(self.value)
