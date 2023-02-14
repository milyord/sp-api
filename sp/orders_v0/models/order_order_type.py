from enum import Enum


class OrderOrderType(str, Enum):
    STANDARDORDER = "StandardOrder"
    LONGLEADTIMEORDER = "LongLeadTimeOrder"
    PREORDER = "Preorder"
    BACKORDER = "BackOrder"
    SOURCINGONDEMANDORDER = "SourcingOnDemandOrder"

    def __str__(self) -> str:
        return str(self.value)
