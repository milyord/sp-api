from enum import Enum


class GetListingsItemIncludedDataItem(str, Enum):
    SUMMARIES = "summaries"
    ATTRIBUTES = "attributes"
    ISSUES = "issues"
    OFFERS = "offers"
    FULFILLMENTAVAILABILITY = "fulfillmentAvailability"
    PROCUREMENT = "procurement"

    def __str__(self) -> str:
        return str(self.value)
