from enum import Enum


class IdType(str, Enum):
    ASIN = "ASIN"
    SELLERSKU = "SellerSKU"

    def __str__(self) -> str:
        return str(self.value)
