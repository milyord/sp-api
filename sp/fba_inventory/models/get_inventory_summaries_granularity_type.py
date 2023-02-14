from enum import Enum


class GetInventorySummariesGranularityType(str, Enum):
    MARKETPLACE = "Marketplace"

    def __str__(self) -> str:
        return str(self.value)
