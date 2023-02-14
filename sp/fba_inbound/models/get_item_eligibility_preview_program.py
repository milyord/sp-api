from enum import Enum


class GetItemEligibilityPreviewProgram(str, Enum):
    INBOUND = "INBOUND"
    COMMINGLING = "COMMINGLING"

    def __str__(self) -> str:
        return str(self.value)
