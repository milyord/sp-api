from enum import Enum


class DetailedShippingTimeTypeAvailabilityType(str, Enum):
    NOW = "NOW"
    FUTURE_WITHOUT_DATE = "FUTURE_WITHOUT_DATE"
    FUTURE_WITH_DATE = "FUTURE_WITH_DATE"

    def __str__(self) -> str:
        return str(self.value)
