from enum import Enum


class ChargeDetailsType(str, Enum):
    GIFTWRAP = "GIFTWRAP"
    FULFILLMENT = "FULFILLMENT"
    MARKETINGINSERT = "MARKETINGINSERT"
    PACKAGING = "PACKAGING"
    LOADING = "LOADING"
    FREIGHTOUT = "FREIGHTOUT"
    TAX_COLLECTED_AT_SOURCE = "TAX_COLLECTED_AT_SOURCE"

    def __str__(self) -> str:
        return str(self.value)
