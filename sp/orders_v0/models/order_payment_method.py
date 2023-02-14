from enum import Enum


class OrderPaymentMethod(str, Enum):
    COD = "COD"
    CVS = "CVS"
    OTHER = "Other"

    def __str__(self) -> str:
        return str(self.value)
