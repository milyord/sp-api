from enum import Enum


class GetOrderMetricsGranularity(str, Enum):
    HOUR = "Hour"
    DAY = "Day"
    WEEK = "Week"
    MONTH = "Month"
    YEAR = "Year"
    TOTAL = "Total"

    def __str__(self) -> str:
        return str(self.value)
