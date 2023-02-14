from enum import Enum


class GetCatalogItemIncludedDataItem(str, Enum):
    ATTRIBUTES = "attributes"
    DIMENSIONS = "dimensions"
    IDENTIFIERS = "identifiers"
    IMAGES = "images"
    PRODUCTTYPES = "productTypes"
    RELATIONSHIPS = "relationships"
    SALESRANKS = "salesRanks"
    SUMMARIES = "summaries"
    VENDORDETAILS = "vendorDetails"

    def __str__(self) -> str:
        return str(self.value)
