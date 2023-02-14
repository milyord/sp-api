from enum import Enum


class GetShipmentsQueryType(str, Enum):
    SHIPMENT = "SHIPMENT"
    DATE_RANGE = "DATE_RANGE"
    NEXT_TOKEN = "NEXT_TOKEN"

    def __str__(self) -> str:
        return str(self.value)
