from enum import Enum


class GetCatalogItemIncludedDataItem(str, Enum):
    ATTRIBUTES = "attributes"
    IDENTIFIERS = "identifiers"
    IMAGES = "images"
    PRODUCTTYPES = "productTypes"
    SALESRANKS = "salesRanks"
    SUMMARIES = "summaries"
    VARIATIONS = "variations"
    VENDORDETAILS = "vendorDetails"

    def __str__(self) -> str:
        return str(self.value)
