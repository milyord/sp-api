from enum import Enum


class FulfillmentChannelType(str, Enum):
    AMAZON = "Amazon"
    MERCHANT = "Merchant"

    def __str__(self) -> str:
        return str(self.value)
