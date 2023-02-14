from enum import Enum


class FulfillmentType(str, Enum):
    AFN = "AFN"
    MFN = "MFN"

    def __str__(self) -> str:
        return str(self.value)
