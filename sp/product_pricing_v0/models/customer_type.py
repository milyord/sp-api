from enum import Enum


class CustomerType(str, Enum):
    CONSUMER = "Consumer"
    BUSINESS = "Business"

    def __str__(self) -> str:
        return str(self.value)
