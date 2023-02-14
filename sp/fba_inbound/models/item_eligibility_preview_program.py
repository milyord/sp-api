from enum import Enum


class ItemEligibilityPreviewProgram(str, Enum):
    INBOUND = "INBOUND"
    COMMINGLING = "COMMINGLING"

    def __str__(self) -> str:
        return str(self.value)
