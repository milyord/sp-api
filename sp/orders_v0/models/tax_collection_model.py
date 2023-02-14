from enum import Enum


class TaxCollectionModel(str, Enum):
    MARKETPLACEFACILITATOR = "MarketplaceFacilitator"

    def __str__(self) -> str:
        return str(self.value)
