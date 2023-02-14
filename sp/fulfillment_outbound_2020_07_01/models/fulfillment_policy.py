from enum import Enum


class FulfillmentPolicy(str, Enum):
    FILLORKILL = "FillOrKill"
    FILLALL = "FillAll"
    FILLALLAVAILABLE = "FillAllAvailable"

    def __str__(self) -> str:
        return str(self.value)
