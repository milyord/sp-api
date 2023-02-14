from enum import Enum


class SearchCatalogItemsIdentifiersType(str, Enum):
    ASIN = "ASIN"
    EAN = "EAN"
    GTIN = "GTIN"
    ISBN = "ISBN"
    JAN = "JAN"
    MINSAN = "MINSAN"
    SKU = "SKU"
    UPC = "UPC"

    def __str__(self) -> str:
        return str(self.value)
