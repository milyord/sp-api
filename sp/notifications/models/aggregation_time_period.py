from enum import Enum


class AggregationTimePeriod(str, Enum):
    FIVEMINUTES = "FiveMinutes"
    TENMINUTES = "TenMinutes"

    def __str__(self) -> str:
        return str(self.value)
