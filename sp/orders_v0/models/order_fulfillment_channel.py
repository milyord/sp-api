from enum import Enum


class OrderFulfillmentChannel(str, Enum):
    MFN = "MFN"
    AFN = "AFN"

    def __str__(self) -> str:
        return str(self.value)
