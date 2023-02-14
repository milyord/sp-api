from enum import Enum


class GetShipmentItemsQueryType(str, Enum):
    DATE_RANGE = "DATE_RANGE"
    NEXT_TOKEN = "NEXT_TOKEN"

    def __str__(self) -> str:
        return str(self.value)
