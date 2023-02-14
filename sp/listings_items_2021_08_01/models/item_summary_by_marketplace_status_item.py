from enum import Enum


class ItemSummaryByMarketplaceStatusItem(str, Enum):
    BUYABLE = "BUYABLE"
    DISCOVERABLE = "DISCOVERABLE"

    def __str__(self) -> str:
        return str(self.value)
