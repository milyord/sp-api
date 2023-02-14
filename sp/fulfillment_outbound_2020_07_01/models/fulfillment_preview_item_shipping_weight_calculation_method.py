from enum import Enum


class FulfillmentPreviewItemShippingWeightCalculationMethod(str, Enum):
    PACKAGE = "Package"
    DIMENSIONAL = "Dimensional"

    def __str__(self) -> str:
        return str(self.value)
