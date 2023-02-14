from enum import Enum


class GetListingOffersCustomerType(str, Enum):
    CONSUMER = "Consumer"
    BUSINESS = "Business"

    def __str__(self) -> str:
        return str(self.value)
