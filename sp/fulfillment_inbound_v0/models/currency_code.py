from enum import Enum


class CurrencyCode(str, Enum):
    USD = "USD"
    GBP = "GBP"

    def __str__(self) -> str:
        return str(self.value)
