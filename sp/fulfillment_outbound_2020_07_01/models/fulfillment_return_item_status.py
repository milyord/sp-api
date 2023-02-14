from enum import Enum


class FulfillmentReturnItemStatus(str, Enum):
    NEW = "New"
    PROCESSED = "Processed"

    def __str__(self) -> str:
        return str(self.value)
