from enum import Enum


class CapacityType(str, Enum):
    SCHEDULED_CAPACITY = "SCHEDULED_CAPACITY"
    AVAILABLE_CAPACITY = "AVAILABLE_CAPACITY"
    ENCUMBERED_CAPACITY = "ENCUMBERED_CAPACITY"
    RESERVED_CAPACITY = "RESERVED_CAPACITY"

    def __str__(self) -> str:
        return str(self.value)
