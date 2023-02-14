from enum import Enum


class GetOrderMetricsBuyerType(str, Enum):
    B2B = "B2B"
    B2C = "B2C"
    ALL = "All"

    def __str__(self) -> str:
        return str(self.value)
