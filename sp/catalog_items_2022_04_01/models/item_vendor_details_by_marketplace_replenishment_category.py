from enum import Enum


class ItemVendorDetailsByMarketplaceReplenishmentCategory(str, Enum):
    ALLOCATED = "ALLOCATED"
    BASIC_REPLENISHMENT = "BASIC_REPLENISHMENT"
    IN_SEASON = "IN_SEASON"
    LIMITED_REPLENISHMENT = "LIMITED_REPLENISHMENT"
    MANUFACTURER_OUT_OF_STOCK = "MANUFACTURER_OUT_OF_STOCK"
    NEW_PRODUCT = "NEW_PRODUCT"
    NON_REPLENISHABLE = "NON_REPLENISHABLE"
    NON_STOCKUPABLE = "NON_STOCKUPABLE"
    OBSOLETE = "OBSOLETE"
    PLANNED_REPLENISHMENT = "PLANNED_REPLENISHMENT"

    def __str__(self) -> str:
        return str(self.value)
