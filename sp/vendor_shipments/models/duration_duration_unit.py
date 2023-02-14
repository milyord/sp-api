from enum import Enum


class DurationDurationUnit(str, Enum):
    DAYS = "Days"
    MONTHS = "Months"

    def __str__(self) -> str:
        return str(self.value)
