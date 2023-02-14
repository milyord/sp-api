from enum import Enum


class GetItemOffersCustomerType(str, Enum):
    CONSUMER = "Consumer"
    BUSINESS = "Business"

    def __str__(self) -> str:
        return str(self.value)
