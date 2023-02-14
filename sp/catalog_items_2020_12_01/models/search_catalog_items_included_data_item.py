from enum import Enum


class SearchCatalogItemsIncludedDataItem(str, Enum):
    IDENTIFIERS = "identifiers"
    IMAGES = "images"
    PRODUCTTYPES = "productTypes"
    SALESRANKS = "salesRanks"
    SUMMARIES = "summaries"
    VARIATIONS = "variations"
    VENDORDETAILS = "vendorDetails"

    def __str__(self) -> str:
        return str(self.value)
