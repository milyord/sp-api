from enum import Enum


class FulfillmentOrderStatus(str, Enum):
    NEW = "New"
    RECEIVED = "Received"
    PLANNING = "Planning"
    PROCESSING = "Processing"
    CANCELLED = "Cancelled"
    COMPLETE = "Complete"
    COMPLETEPARTIALLED = "CompletePartialled"
    UNFULFILLABLE = "Unfulfillable"
    INVALID = "Invalid"

    def __str__(self) -> str:
        return str(self.value)
