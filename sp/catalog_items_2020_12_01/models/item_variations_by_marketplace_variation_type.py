from enum import Enum


class ItemVariationsByMarketplaceVariationType(str, Enum):
    PARENT = "PARENT"
    CHILD = "CHILD"

    def __str__(self) -> str:
        return str(self.value)
